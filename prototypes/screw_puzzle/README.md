# Screw Puzzle Prototype

A satisfying puzzle game where you remove screws in the correct order to disassemble objects.

## How to Play

1. **Tap and hold** a screw to remove it
2. Some screws are **blocked** by pieces (shown with red overlay)
3. Remove the screws holding a piece to make it fall away
4. Remove **all screws** to complete the level

## Running Locally

### Requirements
- Godot 4.2+

### Steps
1. Open Godot and import the project (select `project.godot`)
2. Press F5 or click the Play button

### Android Testing
1. Install Android SDK and set up export templates in Godot
2. Export to APK or use one-click deploy to connected device/emulator

## Project Structure

```
screw_puzzle/
├── project.godot       # Godot project configuration
├── scenes/
│   ├── main.tscn       # Main scene with all screens
│   ├── screw.tscn      # Screw prefab
│   ├── piece.tscn      # Piece/plate prefab
│   └── level_button.tscn
├── scripts/
│   ├── main.gd         # Screen management
│   ├── game.gd         # Core game logic
│   ├── game_state.gd   # Persistent state (autoload)
│   ├── screw.gd        # Screw behavior
│   ├── piece.gd        # Piece behavior
│   └── ...
├── levels/
│   └── levels.json     # Level definitions
└── assets/             # Art and audio (placeholder)
```

## Levels

- **Levels 1-5**: Tutorial (with hints)
- **Levels 6-20**: Main game (increasing difficulty)

## Features

- 20 hand-designed levels
- Save/load progress
- Ad placeholder (every 3 levels)
- Touch-optimized for mobile

## Monetization Hooks

Per project CONSTRAINTS.md, only ethical monetization:
- Ad placeholder shown every 3 completed levels
- Would support: remove ads purchase (not implemented in prototype)

## Known Limitations

- Placeholder graphics (colored rectangles)
- No sound effects
- No animations beyond basic tweens
- Level designs not playtested for balance

## Next Steps

- [ ] Playtest all levels for difficulty
- [ ] Add satisfying sound effects
- [ ] Improve visual feedback
- [ ] Add level completion animations
- [ ] Test on actual Android devices
