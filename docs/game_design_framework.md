# Game Design Framework

Templates, mechanics catalog, and design principles for Mobile Game Factory games.

---

## Mechanics Catalog

### Currently Planned

#### 1. Screw Puzzle (First Prototype)
**Core Loop**: Remove screws in correct order to disassemble object
- Player taps/holds screws to remove them
- Some screws blocked by overlapping pieces
- Must find correct removal sequence
- Win: All screws removed
- Lose: Time limit or move limit exceeded

**Why It Works**:
- Satisfying tactile feedback
- Clear visual cause-and-effect
- Intuitive (everyone knows screws)
- Scales difficulty easily (more screws, more obstacles)

**Difficulty Levers**:
- Number of screws (3-15)
- Number of blocking pieces
- Overlap complexity
- Time/move limits

**Monetization Fit**: Remove ads, hints, undo moves

---

#### 2. Path-Runner (Choice-Based)
**Core Loop**: Navigate character through branching paths, choices determine upgrades/downgrades
- Character auto-runs forward
- Player chooses left/right at decision points
- Choices grant multipliers, items, or penalties
- Goal: Maximize score/resources by end of level

**Why It Works**:
- Simple input (binary choice)
- Risk/reward decisions
- Visual feedback (character grows/shrinks, etc.)
- Quick levels, high replay

**Difficulty Levers**:
- Speed of approach to decisions
- Complexity of math (2x vs. +50 vs. ÷3)
- Number of decision points
- Obstacle integration

**Monetization Fit**: Remove ads, continue after failure, cosmetics

---

#### 3. Thread Puzzle
**Core Loop**: Manipulate thread/yarn to build or deconstruct images
- **Build variant**: Guide thread through pegs to create picture
- **Deconstruct variant**: Untangle thread to reveal image

**Why It Works**:
- Visually satisfying (image reveal)
- Unique mechanic (less saturated)
- Zen/relaxing potential
- Clear success state

**Difficulty Levers**:
- Image complexity
- Number of threads/colors
- Peg density
- Crossing restrictions

**Monetization Fit**: Remove ads, hints, unlock image packs

---

#### 4. Merge-2
**Core Loop**: Combine two identical items to create next tier
- Grid-based play area
- Drag items together to merge
- Goal: Reach target item tier

**Why It Works**:
- Simpler than merge-3 (lower barrier)
- Satisfying progression (watch items evolve)
- Proven monetization
- Easy to theme

**Difficulty Levers**:
- Grid size
- Target tier
- Item spawn rate
- Space limitations

**Monetization Fit**: Remove ads, extra space, faster spawns

---

#### 5. Block Puzzle
**Core Loop**: Sort colored blocks into correct positions
- Move blocks within constrained space
- Clear when color-grouped or pattern-matched
- Similar to sliding puzzles or sorting games

**Why It Works**:
- Established market
- Clear rules
- Satisfying "click" when solved
- Procedural generation friendly

**Difficulty Levers**:
- Grid size
- Number of colors
- Movement constraints
- Move limits

**Monetization Fit**: Remove ads, hints, undo

---

### Future Exploration

Mechanics to research and potentially prototype:

- **Water Sort**: Pour colored liquids between tubes to sort
- **Rope Cutting**: Cut ropes in sequence to achieve goal
- **Pin Pull**: Remove pins to guide balls/liquids
- **Tile Match**: Collect matching tiles from 3D structures
- **Stack/Balance**: Build stable structures
- **Drawing**: Draw shapes or paths to solve puzzles

When exploring new mechanics, document:
1. Core loop
2. Why it works
3. Difficulty levers
4. Monetization fit
5. Technical complexity estimate

---

## Game Design Template

Use this template when designing a new game concept.

```markdown
# [Game Name]

## Overview
- **Mechanic**: [From catalog]
- **Theme**: [Visual theme]
- **Target Session**: [How long is one play session?]
- **Tone**: [Relaxing / Challenging / Frantic / etc.]

## Core Loop
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Win/Lose condition]

## Progression
- **Level count**: [Number]
- **Difficulty curve**: [Gradual / Steep / Flat]
- **Unlock system**: [How players access new levels]

## Monetization (per CONSTRAINTS.md)
- [ ] Remove ads
- [ ] Full unlock
- [ ] Cosmetics
- [ ] Tip jar
- [ ] Other: [Describe]

## Visual Style
- **Color palette**: [Describe]
- **Art style**: [Minimal / Cartoon / Realistic / etc.]
- **UI approach**: [Describe]

## Audio
- **Music**: [Describe mood]
- **SFX**: [Key sound effects needed]

## Technical Notes
- **Procedural potential**: [Can levels be generated?]
- **Performance concerns**: [Any heavy features?]
- **Platform considerations**: [Portrait/landscape, one-hand, etc.]

## Success Metrics (Quality-Focused)
- Target completion rate: [X%]
- Target crash-free rate: [99%+]
- Target load time: [<3s]

## Open Questions
- [Questions to resolve during development]
```

---

## Visual Style Principles

Lightweight guidelines for visual consistency. Not a full brand guide - allows flexibility between games while maintaining quality.

### Universal Principles

1. **Clarity First**
   - Game state must be immediately readable
   - Interactive elements clearly distinguished
   - No ambiguity about what can be tapped

2. **Satisfying Feedback**
   - Visual response to every input
   - Celebratory effects for success
   - Clear (not punishing) failure states

3. **Mobile-Appropriate**
   - Touch targets minimum 44x44 points
   - Works in both bright and dim environments
   - Text readable without zooming

4. **Consistent Within Game**
   - One color palette per game
   - Consistent iconography
   - Predictable UI placement

### Per-Game Flexibility

Games can vary in:
- Color palette (match theme/mood)
- Art style (minimal, cartoon, etc.)
- Animation intensity (zen vs. energetic)
- Theme (abstract, nature, urban, etc.)

### UI Conventions

Standard placement (can adjust per game if justified):
- **Pause/Settings**: Top-left or top-right
- **Level indicator**: Top-center
- **Score/Progress**: Top area
- **Primary actions**: Bottom half (thumb-reachable)
- **Back/Exit**: Top-left

### Asset Generation Prompts

When generating assets with AI tools, include:
- Style reference (flat, 3D, cartoon, etc.)
- Color palette (hex codes or descriptions)
- Mood (playful, calm, intense)
- Technical requirements (size, transparency, format)

Example prompt template:
```
[Object description], [art style], [color palette],
[mood], game asset, clean edges, [size]px, PNG with transparency
```

---

## Level Design Principles

### Difficulty Curve

**Gradual (Recommended for casual)**:
- Levels 1-3: Tutorial, impossible to fail
- Levels 4-10: Introduce mechanics one at a time
- Levels 11-15: Combine mechanics
- Levels 16-20: Challenge, allow failure

**Steep**:
- Quick tutorial, rapid difficulty increase
- For players who want challenge
- Higher churn but dedicated players

**Flat**:
- Consistent difficulty, zen experience
- For relaxation-focused games

### Tutorial Design

1. **Show, don't tell**: Demonstrate mechanics visually
2. **Forced success**: First interaction can't fail
3. **One thing at a time**: Each tutorial level teaches one concept
4. **Skip option**: Let experienced players skip (after level 1)

### Level Flow

- **Quick wins early**: Build confidence
- **Breather levels**: After hard levels, give easy one
- **Milestone rewards**: Every 5-10 levels, celebrate
- **End strong**: Last level should feel like achievement

---

## Audio Guidelines

### Music

- **Loop seamlessly**: No jarring restart
- **Match intensity to gameplay**: Calm for zen, upbeat for action
- **Not fatiguing**: Players may play for extended sessions
- **Memorable but not annoying**: Hummable, not grating

### Sound Effects

Essential SFX for most puzzle games:
- Button tap
- Success/win
- Failure/lose
- Level complete
- Progress tick
- Special action (power-up, hint, etc.)

Principles:
- **Satisfying**: Core action should feel good
- **Distinct**: Each sound clearly different
- **Not harsh**: Avoid piercing frequencies
- **Volume balance**: SFX shouldn't overpower music

---

## Quality Checklist for Designs

Before moving to implementation:

- [ ] Core loop documented and clear
- [ ] Difficulty levers identified
- [ ] Tutorial approach planned
- [ ] At least 20 levels sketched
- [ ] Monetization fits CONSTRAINTS.md
- [ ] Visual style described
- [ ] Audio needs listed
- [ ] Success metrics defined
- [ ] Technical concerns noted
- [ ] Open questions documented

---

*Update this framework as you learn what works.*
