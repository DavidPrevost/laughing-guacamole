# Technical Standards

Lightweight conventions for Godot projects and Python tools. Keeps prototypes consistent and maintainable without being overly prescriptive.

---

## Godot Project Structure

### Standard Directory Layout

```
project_name/
├── project.godot
├── scenes/
│   ├── main.tscn           # Entry point
│   ├── game.tscn           # Core gameplay
│   ├── ui/                 # UI scenes
│   │   ├── main_menu.tscn
│   │   ├── level_select.tscn
│   │   ├── pause_menu.tscn
│   │   └── hud.tscn
│   └── levels/             # Level scenes (if not procedural)
├── scripts/
│   ├── game.gd             # Main game logic
│   ├── level.gd            # Level management
│   ├── autoloads/          # Global scripts
│   │   ├── game_state.gd   # Persistent state
│   │   └── audio_manager.gd
│   └── components/         # Reusable components
├── assets/
│   ├── sprites/
│   ├── audio/
│   │   ├── music/
│   │   └── sfx/
│   ├── fonts/
│   └── themes/
├── levels/
│   └── levels.json         # Level data
└── export/                 # Export presets
```

### Naming Conventions

**Files and Directories**:
- `snake_case` for all files and directories
- Descriptive names: `level_select.tscn` not `ls.tscn`

**Nodes**:
- `PascalCase` for node names
- Prefix with type for clarity: `ScoreLabel`, `PlayButton`

**Scripts**:
- Match script name to primary scene/node: `level_select.gd` for `level_select.tscn`

### GDScript Style

```gdscript
extends Node2D

# Constants at top
const MAX_LEVELS = 100
const TILE_SIZE = 64

# Signals after constants
signal level_completed(level_number)
signal score_updated(new_score)

# Exported vars (configurable in editor)
@export var speed: float = 100.0
@export var lives: int = 3

# Private vars
var _current_level: int = 1
var _score: int = 0

# Onready vars
@onready var score_label = $UI/ScoreLabel

func _ready():
    _initialize_game()

func _process(delta):
    _update_game(delta)

# Public functions
func start_level(level_num: int) -> void:
    _current_level = level_num
    _load_level_data()

func add_score(points: int) -> void:
    _score += points
    score_updated.emit(_score)

# Private functions (prefixed with _)
func _initialize_game() -> void:
    pass

func _load_level_data() -> void:
    pass
```

**Key Points**:
- Type hints encouraged but not required
- Private members prefixed with `_`
- Group related functions together
- Comments for non-obvious logic

---

## Python Tools Structure

### Standard Layout

```
tools/
├── __init__.py
├── orchestrator.py
├── prototype_generator.py
├── market_analyzer.py
├── analytics.py
└── utils/
    ├── __init__.py
    ├── file_helpers.py
    └── logging_config.py
```

### Python Style

```python
"""
Module docstring explaining purpose.
"""

import logging
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class MyData:
    """Data class description."""
    name: str
    value: int = 0


class MyClass:
    """Class description."""

    def __init__(self, config: dict):
        """Initialize with config."""
        self.config = config
        self._cache = {}

    def public_method(self, param: str) -> Optional[str]:
        """
        Method description.

        Args:
            param: Parameter description

        Returns:
            Return value description
        """
        return self._internal_logic(param)

    def _internal_logic(self, param: str) -> Optional[str]:
        """Private method."""
        pass


# Module-level convenience functions
def create_instance(config_path: Path) -> MyClass:
    """Factory function description."""
    pass
```

**Key Points**:
- Docstrings for modules, classes, public methods
- Type hints for function signatures
- Use `dataclass` for data structures
- Use `pathlib.Path` not string paths
- Private methods prefixed with `_`

---

## Data Formats

### Level Data (JSON)

```json
{
  "levels": [
    {
      "number": 1,
      "difficulty": 0.1,
      "elements": {
        "specific_to_mechanic": "values"
      },
      "metadata": {
        "author": "generator",
        "created": "2025-11-20"
      }
    }
  ]
}
```

### Game State (JSON)

```json
{
  "version": 1,
  "player": {
    "current_level": 5,
    "high_scores": [100, 95, 90],
    "settings": {
      "music_volume": 0.8,
      "sfx_volume": 1.0
    }
  },
  "unlocks": {
    "levels": [1, 2, 3, 4, 5],
    "cosmetics": []
  }
}
```

### Configuration (JSON)

```json
{
  "game": {
    "name": "Block Master",
    "version": "1.0.0"
  },
  "monetization": {
    "remove_ads_price": 2.99,
    "ad_frequency": {
      "interstitial_every_n_levels": 3
    }
  },
  "analytics": {
    "enabled": true,
    "quality_metrics_only": true
  }
}
```

---

## Version Control

### Commit Messages

Format: `<type>: <short description>`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code change without behavior change
- `docs`: Documentation only
- `style`: Formatting, no code change
- `test`: Adding tests
- `chore`: Maintenance tasks

Examples:
```
feat: Add level selection screen
fix: Prevent crash when loading corrupted save
refactor: Extract score calculation to separate function
docs: Update README with setup instructions
```

### Branch Naming

- `main` - Stable, releasable code
- `dev` - Integration branch
- `feature/description` - New features
- `fix/description` - Bug fixes

### What to Commit

**Do commit**:
- All source code
- Project files (project.godot, etc.)
- Level data (JSON)
- Configuration files
- Documentation

**Don't commit**:
- Generated files (.import, builds)
- Large binary assets (use Git LFS if needed)
- Personal IDE settings
- Secrets or API keys

### .gitignore Template

```gitignore
# Godot
.godot/
*.import
export/

# Python
__pycache__/
*.pyc
.venv/
*.egg-info/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Project specific
*.log
temp/
```

---

## Testing

### Godot Testing

For now, manual testing with documented test cases. Consider GdUnit4 for automated testing as projects mature.

**Manual Test Template**:
```markdown
## Test: [Feature Name]

### Steps
1. [Action]
2. [Action]
3. [Action]

### Expected Result
[What should happen]

### Actual Result
[ ] Pass / [ ] Fail

### Notes
[Any observations]
```

### Python Testing

Use pytest for tool testing.

```python
# tests/test_orchestrator.py

import pytest
from tools.orchestrator import Orchestrator, ActionType

def test_autonomous_action_approved():
    orch = Orchestrator()
    result = orch.request_action(
        ActionType.GENERATE_CODE,
        "Test action"
    )
    assert result.approved == True

def test_restricted_action_blocked():
    orch = Orchestrator()
    result = orch.request_action(
        ActionType.DEPLOY,
        "Test deploy"
    )
    assert result.approved == False
```

---

## Performance Guidelines

### Godot

- Use `@onready` not repeated `get_node()` calls
- Pool frequently spawned objects
- Use `call_deferred()` for node tree changes
- Profile before optimizing (use Godot profiler)

### General

- Load time <3 seconds target
- Maintain 60fps (30fps acceptable with justification)
- Memory usage should be stable over time
- Test on low-end target device

---

## Documentation Standards

### Code Comments

```gdscript
# Good: Explains WHY
# Prevent division by zero when player hasn't scored yet
var average = total / max(attempts, 1)

# Bad: Explains WHAT (code already shows this)
# Divide total by attempts
var average = total / attempts
```

### README Template

Each prototype should have a README:

```markdown
# [Game Name]

Brief description.

## How to Play
[Simple explanation]

## Running Locally
[Setup instructions]

## Project Structure
[Key files explained]

## Known Issues
[Current problems]

## Future Improvements
[Planned enhancements]
```

---

## Security Considerations

### Sensitive Data

- Never commit API keys or secrets
- Use environment variables for configuration
- Don't log sensitive information

### User Data

- Minimal data collection
- Encrypt stored data if sensitive
- Clear data on uninstall

### Input Validation

- Validate all external input
- Sanitize file paths
- Check bounds on arrays/indices

---

*These standards should evolve based on what works. Update as patterns emerge.*
