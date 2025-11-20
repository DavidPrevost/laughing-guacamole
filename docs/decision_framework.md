# Decision Framework

Criteria and processes for evaluating game concepts, deciding when to pivot, and knowing when to kill a project.

---

## Concept Evaluation

Use this scorecard when evaluating whether to pursue a game concept.

### Evaluation Criteria

| Criterion | Weight | Score (1-5) | Notes |
|-----------|--------|-------------|-------|
| **Mechanical Clarity** | High | | Is the core loop simple and clear? |
| **Tactile Satisfaction** | High | | Does the main action feel good? |
| **Visual Feedback** | Medium | | Is progress/success visible? |
| **Difficulty Scalability** | High | | Can we easily make harder levels? |
| **Procedural Potential** | Medium | | Can levels be generated? |
| **Theme Flexibility** | Low | | Can it be re-skinned? |
| **Monetization Fit** | Medium | | Does ethical monetization make sense? |
| **Technical Feasibility** | High | | Can we build it with current tools? |
| **Differentiation** | Medium | | What makes it stand out? |
| **Personal Interest** | Medium | | Do we want to build this? |

### Scoring Guide

- **5**: Excellent, strong advantage
- **4**: Good, solid
- **3**: Adequate, no concerns
- **2**: Weak, potential problem
- **1**: Poor, likely blocker

### Thresholds

- **Total 40+**: Strong candidate, proceed
- **Total 30-39**: Viable, consider improvements
- **Total 20-29**: Weak, needs significant changes
- **Below 20**: Likely not worth pursuing

### Red Flags (Automatic Concerns)

- Any "High weight" criterion scores 1-2
- Core loop requires explanation
- Main action isn't satisfying in prototype
- Can't identify ethical monetization approach

---

## Go/No-Go Checkpoints

Evaluation points during development.

### Checkpoint 1: After Core Mechanic Prototype

**Time invested**: ~2-4 hours

**Questions**:
1. Is the core action satisfying? (Play it 50 times)
2. Can you explain the rules in one sentence?
3. Does it work on mobile (touch, portrait)?
4. Can you see how to make it harder?

**Decision**:
- All yes → Continue to full prototype
- 1-2 no → Try to fix, re-evaluate
- 3+ no → Kill or pivot mechanic

---

### Checkpoint 2: After Playable Prototype (20 levels)

**Time invested**: ~8-16 hours

**Questions**:
1. Did you enjoy playing all 20 levels?
2. Could you make 100 more levels?
3. Is the difficulty curve working?
4. Does it feel like other games you'd play?

**Decision**:
- All yes → Continue to polish
- 1-2 no → Iterate on weak points
- 3+ no → Likely kill, review learnings

---

### Checkpoint 3: After Polish Pass

**Time invested**: ~16-24 hours

**Questions**:
1. Would you recommend this to a friend?
2. Does it meet quality metrics (crash-free, load time)?
3. Is monetization implemented and tested?
4. Does it pass the launch checklist?

**Decision**:
- All yes → Prepare for launch (human approval needed)
- 1-2 no → Address specific issues
- 3+ no → Major rework or kill

---

## Pivot vs. Kill

### When to Pivot

Pivoting = Keeping some elements while changing others

**Pivot signals**:
- Core mechanic is satisfying but context/theme isn't working
- Good engagement but difficulty curve is wrong
- Players like it but for unexpected reasons
- Technical issues are solvable with different approach

**Pivot options**:
- Change theme/visual style
- Adjust difficulty curve
- Simplify or add complexity
- Change level structure
- Modify win/lose conditions

### When to Kill

Killing = Stop development, capture learnings, move on

**Kill signals**:
- Core action isn't satisfying after multiple iterations
- Can't explain the game simply
- Players consistently confused
- Technical barriers are fundamental
- Lost interest in the project

**Kill process**:
1. Document what didn't work and why
2. Note any reusable components
3. Identify learnings for future projects
4. Archive (don't delete) the prototype
5. Move on without guilt

---

## Comparison Analysis

When choosing between multiple viable concepts.

### Head-to-Head Template

| Factor | Concept A | Concept B | Winner |
|--------|-----------|-----------|--------|
| Development time estimate | | | |
| Procedural generation potential | | | |
| Monetization clarity | | | |
| Technical risk | | | |
| Personal excitement | | | |
| Differentiation | | | |

### Tiebreakers

When concepts score similarly:
1. **Personal interest** - You'll build better what you care about
2. **Technical learning** - Choose what teaches new skills
3. **Faster to test** - Get to validation quicker
4. **Gut feeling** - Trust your instincts

---

## Risk Assessment

### Risk Categories

**Technical Risks**:
- Novel mechanics without proven solutions
- Performance-intensive features
- Complex procedural generation

**Design Risks**:
- Unclear core loop
- Difficulty balancing challenges
- Unproven mechanic combinations

**Market Risks**:
- Oversaturated mechanic
- Niche appeal
- Poor monetization fit

### Risk Mitigation

For each identified risk:
1. **Accept**: Risk is low impact, proceed
2. **Mitigate**: Take action to reduce risk
3. **Avoid**: Change approach to eliminate risk
4. **Test Early**: Prototype the risky part first

---

## Decision Log

Track major decisions for future reference.

| Date | Decision | Options Considered | Rationale | Outcome |
|------|----------|-------------------|-----------|---------|
| | | | | |

---

## Common Traps to Avoid

### Sunk Cost Fallacy
- Don't continue just because you've invested time
- Each checkpoint is a fresh evaluation
- It's okay to kill after significant work

### Feature Creep
- Core loop should be fun without additions
- Add features to enhance, not fix
- Every feature must justify its complexity

### Perfectionism
- "Good enough to test" beats "perfect in theory"
- Real player feedback > assumptions
- You can always iterate

### Comparison Paralysis
- Don't endlessly compare to competitors
- Make your version, then evaluate
- Different doesn't have to mean better

### Over-Optimization
- Don't optimize before validating fun
- Performance can be fixed later
- Get to "is it fun?" as fast as possible

---

*Update this framework based on experience. What decision criteria matter most will become clearer over time.*
