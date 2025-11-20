"""
Prototype Generator - Creates game prototypes from design specifications

This tool generates playable game prototypes locally. It does not deploy
anything or access external paid services without going through approval gates.
"""

import json
import logging
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

from .orchestrator import Orchestrator, ActionType, RequiresHumanApproval

logger = logging.getLogger('prototype_generator')


class GameMechanic(Enum):
    """Supported game mechanics for prototype generation."""
    BLOCK_PUZZLE = "block_puzzle"
    MERGE_TWO = "merge_two"
    SCREW_PUZZLE = "screw_puzzle"
    MATCH_THREE = "match_three"


class MonetizationType(Enum):
    """Allowed monetization types (per CONSTRAINTS.md)."""
    REMOVE_ADS = "remove_ads"
    FULL_UNLOCK = "full_unlock"
    COSMETICS = "cosmetics"
    TIP_JAR = "tip_jar"

    # Explicitly NOT supported (would violate constraints)
    # LOOT_BOX = "loot_box"  # Not allowed
    # DYNAMIC_PRICING = "dynamic_pricing"  # Not allowed
    # ENERGY_SYSTEM = "energy_system"  # Not allowed


@dataclass
class GameDesign:
    """Specification for a game prototype."""
    name: str
    mechanic: GameMechanic
    level_count: int = 20
    difficulty_curve: str = "gradual"  # gradual, steep, flat
    monetization: list[MonetizationType] = field(default_factory=list)
    description: str = ""

    def validate(self) -> list[str]:
        """Validate design against constraints. Returns list of issues."""
        issues = []

        if self.level_count < 1:
            issues.append("Must have at least 1 level")
        if self.level_count > 1000:
            issues.append("Too many levels for prototype (max 1000)")

        # Monetization is optional but must be from allowed types
        for mon in self.monetization:
            if not isinstance(mon, MonetizationType):
                issues.append(f"Invalid monetization type: {mon}")

        return issues


@dataclass
class LevelSpec:
    """Specification for a single level."""
    level_number: int
    difficulty: float  # 0.0 to 1.0
    elements: dict = field(default_factory=dict)


@dataclass
class Prototype:
    """A generated game prototype."""
    design: GameDesign
    levels: list[LevelSpec]
    output_path: Path
    godot_project: dict = field(default_factory=dict)


class PrototypeGenerator:
    """
    Generates game prototypes from design specifications.

    All generation happens locally. No external services are called
    without explicit approval through the orchestrator.
    """

    def __init__(self, orchestrator: Orchestrator, output_dir: Path):
        self.orchestrator = orchestrator
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"PrototypeGenerator initialized, output: {output_dir}")

    def generate(self, design: GameDesign) -> Prototype:
        """
        Generate a complete game prototype from a design specification.

        Args:
            design: The game design specification

        Returns:
            Generated prototype with all levels and project files
        """
        # Validate design
        issues = design.validate()
        if issues:
            raise ValueError(f"Invalid design: {', '.join(issues)}")

        # Request approval for code generation (this is autonomous)
        self.orchestrator.request_action(
            ActionType.GENERATE_CODE,
            f"Generate {design.mechanic.value} prototype: {design.name}",
            {"levels": design.level_count, "mechanic": design.mechanic.value}
        )

        logger.info(f"Generating prototype: {design.name}")

        # Generate levels
        levels = self._generate_levels(design)

        # Create output directory for this prototype
        prototype_dir = self.output_dir / self._sanitize_name(design.name)
        prototype_dir.mkdir(parents=True, exist_ok=True)

        # Generate Godot project structure
        godot_project = self._generate_godot_project(design, levels, prototype_dir)

        prototype = Prototype(
            design=design,
            levels=levels,
            output_path=prototype_dir,
            godot_project=godot_project
        )

        # Save prototype metadata
        self._save_metadata(prototype)

        logger.info(f"Prototype generated at: {prototype_dir}")
        return prototype

    def _generate_levels(self, design: GameDesign) -> list[LevelSpec]:
        """Generate level specifications based on difficulty curve."""
        levels = []

        for i in range(design.level_count):
            # Calculate difficulty based on curve
            progress = i / max(1, design.level_count - 1)

            if design.difficulty_curve == "gradual":
                difficulty = progress * 0.8 + 0.1  # 0.1 to 0.9
            elif design.difficulty_curve == "steep":
                difficulty = (progress ** 2) * 0.9 + 0.1
            else:  # flat
                difficulty = 0.5

            # Generate level elements based on mechanic
            elements = self._generate_level_elements(design.mechanic, difficulty)

            levels.append(LevelSpec(
                level_number=i + 1,
                difficulty=difficulty,
                elements=elements
            ))

        return levels

    def _generate_level_elements(self, mechanic: GameMechanic,
                                  difficulty: float) -> dict:
        """Generate mechanic-specific level elements."""
        if mechanic == GameMechanic.BLOCK_PUZZLE:
            return {
                "grid_size": 5 + int(difficulty * 4),  # 5x5 to 9x9
                "block_types": 3 + int(difficulty * 3),  # 3 to 6 types
                "moves_limit": max(10, int(30 - difficulty * 15))
            }
        elif mechanic == GameMechanic.MERGE_TWO:
            return {
                "grid_size": 4 + int(difficulty * 2),  # 4x4 to 6x6
                "target_value": 2 ** (4 + int(difficulty * 6)),  # 16 to 1024
                "starting_tiles": 2 + int(difficulty * 2)
            }
        elif mechanic == GameMechanic.SCREW_PUZZLE:
            return {
                "screw_count": 3 + int(difficulty * 7),  # 3 to 10 screws
                "obstacle_count": int(difficulty * 5),
                "time_limit": max(30, int(120 - difficulty * 60))
            }
        else:
            return {"difficulty": difficulty}

    def _generate_godot_project(self, design: GameDesign,
                                 levels: list[LevelSpec],
                                 output_dir: Path) -> dict:
        """Generate Godot project files."""
        # Create project.godot
        project_config = {
            "config_version": 5,
            "project_name": design.name,
            "description": design.description or f"A {design.mechanic.value} game"
        }

        # Write project.godot
        project_file = output_dir / "project.godot"
        project_file.write_text(self._format_godot_config(project_config))

        # Create directory structure
        (output_dir / "scenes").mkdir(exist_ok=True)
        (output_dir / "scripts").mkdir(exist_ok=True)
        (output_dir / "assets").mkdir(exist_ok=True)
        (output_dir / "levels").mkdir(exist_ok=True)

        # Generate main scene
        main_scene = self._generate_main_scene(design)
        (output_dir / "scenes" / "main.tscn").write_text(main_scene)

        # Generate level data
        levels_data = {"levels": [
            {"number": l.level_number, "difficulty": l.difficulty, "elements": l.elements}
            for l in levels
        ]}
        (output_dir / "levels" / "levels.json").write_text(
            json.dumps(levels_data, indent=2)
        )

        # Generate game script
        game_script = self._generate_game_script(design)
        (output_dir / "scripts" / "game.gd").write_text(game_script)

        return {
            "project_file": str(project_file),
            "main_scene": str(output_dir / "scenes" / "main.tscn"),
            "levels_file": str(output_dir / "levels" / "levels.json")
        }

    def _format_godot_config(self, config: dict) -> str:
        """Format dictionary as Godot project file."""
        lines = ['[gd_resource type="ProjectSettings"]', '', '[application]']
        for key, value in config.items():
            if isinstance(value, str):
                lines.append(f'{key}="{value}"')
            else:
                lines.append(f'{key}={value}')
        return '\n'.join(lines)

    def _generate_main_scene(self, design: GameDesign) -> str:
        """Generate main scene TSCN file."""
        return f'''[gd_scene format=3]

[node name="Main" type="Node2D"]

[node name="Game" type="Node2D" parent="."]
script = ExtResource("res://scripts/game.gd")

[node name="UI" type="CanvasLayer" parent="."]

[node name="ScoreLabel" type="Label" parent="UI"]
offset_right = 200.0
offset_bottom = 40.0
text = "Score: 0"
'''

    def _generate_game_script(self, design: GameDesign) -> str:
        """Generate main game script."""
        return f'''extends Node2D

# {design.name} - {design.mechanic.value} game
# Generated by Mobile Game Factory

var current_level: int = 1
var score: int = 0
var levels_data: Array = []

func _ready():
    load_levels()
    start_level(1)

func load_levels():
    var file = FileAccess.open("res://levels/levels.json", FileAccess.READ)
    if file:
        var json = JSON.new()
        json.parse(file.get_as_text())
        levels_data = json.data.get("levels", [])
        file.close()

func start_level(level_num: int):
    current_level = level_num
    var level_data = get_level_data(level_num)
    if level_data:
        setup_level(level_data)
    else:
        print("Level not found: ", level_num)

func get_level_data(level_num: int) -> Dictionary:
    for level in levels_data:
        if level.get("number") == level_num:
            return level
    return {{}}

func setup_level(data: Dictionary):
    # Override in specific game implementation
    print("Setting up level: ", data.get("number"))

func complete_level():
    score += calculate_score()
    if current_level < levels_data.size():
        start_level(current_level + 1)
    else:
        game_complete()

func calculate_score() -> int:
    return 100  # Override with actual scoring logic

func game_complete():
    print("Congratulations! Game complete!")
    print("Final score: ", score)
'''

    def _save_metadata(self, prototype: Prototype):
        """Save prototype metadata for tracking."""
        metadata = {
            "name": prototype.design.name,
            "mechanic": prototype.design.mechanic.value,
            "level_count": len(prototype.levels),
            "monetization": [m.value for m in prototype.design.monetization],
            "output_path": str(prototype.output_path)
        }

        metadata_file = prototype.output_path / "prototype_metadata.json"
        metadata_file.write_text(json.dumps(metadata, indent=2))

    def _sanitize_name(self, name: str) -> str:
        """Sanitize name for use as directory name."""
        return "".join(c if c.isalnum() or c in "-_" else "_" for c in name).lower()


# Example usage
if __name__ == "__main__":
    from .orchestrator import create_orchestrator

    orch = create_orchestrator()
    generator = PrototypeGenerator(orch, Path("./prototypes"))

    # Create a simple puzzle game design
    design = GameDesign(
        name="Block Master",
        mechanic=GameMechanic.BLOCK_PUZZLE,
        level_count=20,
        difficulty_curve="gradual",
        monetization=[MonetizationType.REMOVE_ADS],
        description="A relaxing block puzzle game"
    )

    # Generate prototype
    prototype = generator.generate(design)
    print(f"Generated prototype at: {prototype.output_path}")
