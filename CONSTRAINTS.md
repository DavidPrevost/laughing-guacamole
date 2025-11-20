# Project Constraints and Ethical Boundaries

This document defines the explicit legal, ethical, and operational boundaries for the Mobile Game Factory project. All tools and systems in this repository must operate within these constraints.

## Core Principles

1. **Human oversight for consequential actions** - Autonomous systems assist and recommend; humans approve and execute
2. **Transparency over manipulation** - Monetization must provide clear value, not exploit psychology
3. **Quality over extraction** - Optimize for player enjoyment, not revenue maximization
4. **Legal compliance** - Follow all applicable laws, terms of service, and platform guidelines

---

## Market Research Boundaries

### Allowed
- Public APIs with proper authentication (e.g., licensed data.ai, SensorTower subscriptions)
- Published industry reports (Newzoo, Statista, GamesIndustry.biz)
- Manual research and documentation of successful games
- Analysis of publicly available reviews and ratings
- Studying game design patterns through normal gameplay

### Not Allowed
- Automated scraping of app stores (violates ToS)
- Circumventing rate limits or access controls
- Collecting data not intended to be public
- Reverse engineering competitor apps
- Any data collection that violates platform Terms of Service

---

## Monetization Boundaries

### Acceptable (Static, Transparent)
- **One-time purchases with clear value**
  - Remove ads ($2.99)
  - Full game unlock
  - Level packs or content expansions
- **Cosmetic items** with fixed, visible prices
- **Supporter tiers** / tip jar (optional, no gameplay advantage)
- **Standard ad placements**
  - Banner ads in non-intrusive locations
  - Interstitial ads between levels (not mid-gameplay)
  - Rewarded video ads (user-initiated, clear reward)

### Not Acceptable (Manipulative/Predatory)
- **Loot boxes** or any randomized purchases
- **Dynamic pricing** based on user behavior or spending history
- **Personalized "special offers"** targeting individual spending patterns
- **Artificial scarcity** (limited-time offers designed to pressure)
- **Energy/lives systems** designed to create purchase pressure
- **Ad frequency manipulation** based on engagement metrics
- **"First hit free" currency** designed to create sunk cost fallacy
- **Pay-to-win mechanics** that gate progression behind payment
- **Targeting vulnerable users** (children, compulsive spenders)
- **Dark patterns** (confusing UI, hidden costs, difficult cancellation)

### Requires Human Review
- All pricing decisions
- Ad placement locations and frequency caps
- What content is free vs. paid
- Any changes to monetization after initial release

---

## System Autonomy Boundaries

### Never Autonomous (Requires Human Approval)

| Action | Reason |
|--------|--------|
| Spend money or authorize purchases | Financial liability |
| Deploy to app stores | User-facing impact |
| Deploy to any environment with real users | User safety |
| Modify monetization parameters | Ethical implications |
| Collect or process user data | Privacy obligations |
| Change production content | User experience impact |
| A/B test monetization | Manipulation risk |
| Send notifications to users | Spam/manipulation risk |
| Access external paid APIs | Cost control |
| Modify these constraints | Integrity of boundaries |

### Allowed Autonomous Actions

| Action | Conditions |
|--------|------------|
| Generate code and prototypes | Local environment only |
| Run local tests | No external dependencies |
| Analyze public data | Within rate limits, respecting ToS |
| Generate reports and recommendations | For human review |
| Create assets and content | For human review before use |
| Commit to development branches | Not production/main |
| Refactor and improve local code | Standard development |

### Approval Gate Implementation

All systems must implement approval gates for restricted actions:

```python
class ApprovalGate:
    REQUIRES_APPROVAL = [
        "deploy",
        "spend_money",
        "modify_monetization",
        "collect_user_data",
        "external_api_call",
        "production_change",
        "send_notification"
    ]

    def check(self, action_type: str) -> bool:
        if action_type in self.REQUIRES_APPROVAL:
            raise RequiresHumanApproval(
                f"Action '{action_type}' requires human approval. "
                f"Please review and execute manually."
            )
        return True
```

---

## Learning System Boundaries

### Acceptable Analytics (Quality-Focused)

| Metric | Purpose | Allowed Use |
|--------|---------|-------------|
| Level completion rates | Identify difficulty issues | Adjust level design |
| Quit points | Find frustration sources | Improve game flow |
| Session length | Understand engagement | Improve content pacing |
| Crash reports | Fix bugs | Stability improvements |
| Feature usage | Understand preferences | Inform future design |

### How Insights Must Be Used

1. **System generates reports** with data and recommendations
2. **Humans review** the insights and implications
3. **Humans decide** what changes to implement
4. **Changes go through normal review** before deployment
5. **No autonomous deployment** of "optimizations"

### Not Acceptable (Manipulation-Focused)

| Metric | Prohibited Use |
|--------|----------------|
| Ad engagement | Optimizing ad timing/frequency for clicks |
| Spending patterns | Identifying/targeting high spenders |
| Session timing | Optimizing notifications for re-engagement |
| Drop-off points | Adding monetization pressure at frustration |
| Any metric | Optimizing revenue over user experience |

---

## Data and Privacy

### Requirements
- Collect only data necessary for game functionality
- Clear privacy policy before any data collection
- No selling or sharing user data with third parties
- Comply with COPPA (if any possibility of child users)
- Comply with GDPR for EU users
- Provide data deletion mechanism

### Prohibited
- Collecting data without disclosure
- Fingerprinting or tracking across apps
- Collecting sensitive personal information
- Sharing data with ad networks beyond standard attribution

---

## Success Metrics

### Primary (Quality-Focused)
- **Player satisfaction**: Ratings, reviews, completion rates
- **Game quality**: Crash-free sessions, bug reports
- **Development efficiency**: Time from concept to prototype

### Secondary (Sustainability-Focused)
- **Revenue sufficiency**: Covers development costs
- **Retention**: Players return because they enjoy the game

### Explicitly Not Primary
- Revenue maximization
- Engagement maximization (can lead to addiction)
- Viral growth (can lead to manipulative sharing prompts)

---

## Enforcement

### Code Review
All code must be reviewed against these constraints before merging to main.

### Logging
All system actions must be logged with:
- Timestamp
- Action type
- Whether approval was required
- Outcome

### Violations
If a system attempts a prohibited action:
1. Action must be blocked
2. Incident must be logged
3. Human must be notified
4. System should suggest compliant alternative

---

## Amendments

These constraints may only be modified through explicit human decision with documented rationale. The autonomous systems cannot modify this document or circumvent these restrictions.

---

*Last updated: 2025-11-20*
*Version: 1.0*
