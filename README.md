# Mobile Game Factory

An experimental project exploring AI-assisted game development tools with strong ethical constraints and human oversight.

## Project Goals

Build development tools that can:
- Generate game prototypes from design concepts
- Create procedural content (levels, puzzles)
- Analyze game performance for quality improvements
- Streamline the development workflow

**Important**: This project prioritizes player experience over revenue optimization. See [CONSTRAINTS.md](CONSTRAINTS.md) for ethical boundaries.

## Directory Structure

```
/src          - Core game code (Godot/GDScript)
/tools        - Python automation tools
/prototypes   - Generated game prototypes
/docs         - Documentation
/config       - Configuration files
/tests        - Test suites
```

## Core Systems

### Orchestrator (`tools/orchestrator.py`)
Central control system with approval gates. Ensures all consequential actions require human approval.

### Prototype Generator (`tools/prototype_generator.py`)
Generates playable game prototypes from design specifications. Creates levels, implements mechanics, sets up basic structure.

### Market Analyzer (`tools/market_analyzer.py`)
Researches game market using ethical methods (public APIs, published reports). No scraping.

### Analytics (`tools/analytics.py`)
Analyzes game performance for quality improvements. Bounded to quality metrics only - no monetization optimization.

## Key Constraints

- **No autonomous spending** - All purchases require human approval
- **No autonomous deployment** - Human approves all releases
- **No predatory monetization** - No loot boxes, dynamic pricing, or manipulation
- **No app store scraping** - Only legitimate data sources
- **Quality over revenue** - Optimize for player enjoyment

See [CONSTRAINTS.md](CONSTRAINTS.md) for complete details.

## Technology Stack

- **Game Engine**: Godot 4.x (open-source)
- **Scripting**: GDScript (games), Python (tools)
- **Version Control**: Git

## Getting Started

1. Review [CONSTRAINTS.md](CONSTRAINTS.md) to understand project boundaries
2. Check `/tools` for available automation systems
3. See `/docs` for detailed documentation

## Human Oversight Requirements

The following actions always require human approval:
- Deploying to any environment with real users
- Any purchases or spending
- Monetization configuration
- User data collection
- External API calls to paid services

## License

[To be determined]

---

*This is an experimental project exploring the boundaries of AI-assisted development while maintaining ethical standards.*
