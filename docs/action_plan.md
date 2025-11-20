# Action Plan

Checklist-based development phases for the Mobile Game Factory. Work at your own pace - check items off as completed, no deadlines.

---

## Phase 1: Foundation & First Prototype

### Setup
- [x] Create repository structure
- [x] Document ethical constraints (CONSTRAINTS.md)
- [x] Build orchestrator with approval gates
- [x] Build prototype generator framework
- [x] Build market analyzer (ethical)
- [x] Build analytics system (quality-focused)
- [x] Create action plan and governance docs

### First Prototype: Screw Puzzle
- [ ] Research screw puzzle mechanics (play existing games, note patterns)
- [ ] Document core loop in game_design_framework.md
- [ ] Design 5 tutorial levels (teach mechanics)
- [ ] Design 15 main levels (gradual difficulty)
- [ ] Implement core screw removal mechanic in Godot
- [ ] Implement obstacle system (blocking pieces)
- [ ] Implement win/lose conditions
- [ ] Create placeholder art (shapes/colors)
- [ ] Add basic UI (level select, pause, win/lose screens)
- [ ] Playtest and iterate on difficulty curve
- [ ] Document learnings

### First Prototype: Polish Pass
- [ ] Add basic sound effects
- [ ] Add simple animations (screw removal, obstacles)
- [ ] Implement one monetization hook (remove ads placeholder)
- [ ] Add analytics event hooks (quality metrics only)
- [ ] Final playtest

---

## Phase 2: Expand Mechanics

Build prototypes for additional mechanics. Order is flexible - pursue what's interesting.

### Path-Runner Prototype
- [ ] Research path-runner/choice mechanics
- [ ] Document core loop
- [ ] Design level generation algorithm (branching paths)
- [ ] Design upgrade/downgrade system
- [ ] Implement prototype
- [ ] Playtest and document learnings

### Thread Puzzle Prototype
- [ ] Research thread/yarn puzzle mechanics
- [ ] Document core loop (build vs. deconstruct variants)
- [ ] Design thread physics/interaction system
- [ ] Design image reveal/creation mechanics
- [ ] Implement prototype
- [ ] Playtest and document learnings

### Merge-2 Prototype
- [ ] Research merge-2 mechanics (simpler than merge-3)
- [ ] Document core loop
- [ ] Design grid and merging rules
- [ ] Design progression targets
- [ ] Implement prototype
- [ ] Playtest and document learnings

### Block Puzzle Prototype
- [ ] Research block sorting/matching mechanics
- [ ] Document core loop
- [ ] Design block types and rules
- [ ] Implement prototype
- [ ] Playtest and document learnings

### Additional Mechanics (To Explore)
- [ ] Identify other simple-but-engaging mechanics
- [ ] Document candidates in game_design_framework.md
- [ ] Prioritize based on decision framework

---

## Phase 3: Meta-Systems & Content Generation

After core mechanics are proven, build supporting systems.

### Procedural Content
- [ ] Analyze which mechanics support procedural generation
- [ ] Design level generation algorithms
- [ ] Implement generators for 2-3 mechanics
- [ ] Test quality of generated content
- [ ] Tune generation parameters

### Meta-Progression
- [ ] Design meta-layer options (collections, upgrades, themes)
- [ ] Evaluate which meta-systems fit which mechanics
- [ ] Implement meta-system for one prototype
- [ ] Test retention impact (quality metric, not manipulation)

### Content Pipeline
- [ ] Document asset requirements per game type
- [ ] Create asset prompt templates for AI generation
- [ ] Test asset generation workflow
- [ ] Build asset integration pipeline

---

## Phase 4: Production Readiness

Prepare one or more prototypes for actual release.

### Quality Assurance
- [ ] Comprehensive playtesting
- [ ] Performance profiling (load times, frame rate, battery)
- [ ] Crash testing
- [ ] Accessibility review

### Monetization Implementation
- [ ] Implement chosen monetization (per CONSTRAINTS.md)
- [ ] Test purchase flows
- [ ] Verify no prohibited patterns

### Legal & Compliance
- [ ] Write privacy policy
- [ ] Age rating assessment
- [ ] App store guideline review
- [ ] Accessibility compliance check

### Pre-Launch
- [ ] Complete launch_checklist.md items
- [ ] Prepare store listing materials
- [ ] Human review and approval for deployment

---

## Phase 5: Post-Launch & Iteration

After launch (with human approval).

### Monitoring
- [ ] Set up analytics dashboard (quality metrics)
- [ ] Monitor crash reports
- [ ] Track user reviews for quality issues

### Iteration
- [ ] Analyze quality metrics
- [ ] Identify improvement opportunities
- [ ] Implement fixes (with human approval for deployment)
- [ ] Plan content updates

### Portfolio Expansion
- [ ] Evaluate which other prototypes are ready
- [ ] Apply learnings from first launch
- [ ] Repeat Phase 4 for next game

---

## Ongoing Activities

These happen throughout all phases:

### Research
- [ ] Monitor industry reports for trends
- [ ] Play competitor games for inspiration
- [ ] Document interesting mechanics

### Tool Improvement
- [ ] Identify repetitive tasks to automate
- [ ] Improve prototype generator
- [ ] Enhance analytics insights
- [ ] Build new tools as needed

### Documentation
- [ ] Update game_design_framework.md with learnings
- [ ] Refine decision_framework.md based on experience
- [ ] Keep technical_standards.md current

---

## Progress Notes

Use this section to track overall progress and learnings.

### Session Log

| Date | Work Done | Notes |
|------|-----------|-------|
| 2025-11-20 | Initial setup complete | Constraints, tools, docs created |

### Key Learnings

(Add insights as you discover them)

### Blockers & Questions

(Track things that need resolution)

---

*This plan is a living document. Update as the project evolves.*
