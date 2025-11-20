# Launch Checklist

Pre-deployment verification checklist. All items must be completed before requesting human approval for launch.

---

## Game Quality

### Core Experience
- [ ] Core loop is satisfying after 100+ plays
- [ ] All levels completable (verified by playthrough)
- [ ] Difficulty curve feels fair
- [ ] Tutorial teaches mechanics clearly
- [ ] No levels feel unfair or broken

### Technical Quality
- [ ] Crash-free rate >99% in testing
- [ ] Load time <3 seconds on target devices
- [ ] Stable 60fps (or 30fps if intentional)
- [ ] Memory usage within acceptable limits
- [ ] No memory leaks during extended play
- [ ] Battery drain is reasonable

### Polish
- [ ] All placeholder art replaced
- [ ] All sounds implemented and balanced
- [ ] Animations smooth and purposeful
- [ ] No visual glitches or artifacts
- [ ] Text is readable at all sizes
- [ ] Colors work for common color blindness

---

## User Experience

### Accessibility
- [ ] Touch targets minimum 44x44 points
- [ ] Text contrast meets WCAG guidelines
- [ ] Game playable with one hand
- [ ] No flashing lights >3 per second
- [ ] Audio not required for gameplay

### Onboarding
- [ ] First-time experience is smooth
- [ ] No confusion about what to do first
- [ ] Skip option for tutorial (after basics)
- [ ] Game state saves correctly
- [ ] Resume from where left off

### UI/UX
- [ ] All buttons clearly tappable
- [ ] Back/exit always accessible
- [ ] Pause functionality works
- [ ] Settings persist correctly
- [ ] No dead ends in navigation

---

## Monetization Compliance

### CONSTRAINTS.md Verification
- [ ] No loot boxes or randomized purchases
- [ ] No dynamic pricing
- [ ] No personalized offers based on behavior
- [ ] No artificial energy/lives pressure
- [ ] No pay-to-win mechanics
- [ ] Prices are static and clear
- [ ] Ad frequency is fixed, not behavior-based

### Purchase Flow
- [ ] Prices clearly displayed before purchase
- [ ] Purchase confirmation dialog
- [ ] Successful purchase feedback
- [ ] Failed purchase handled gracefully
- [ ] Restore purchases works (IAP)

### Ads (if applicable)
- [ ] Ads don't interrupt active gameplay
- [ ] Clear close button on ads
- [ ] Rewarded ads deliver promised reward
- [ ] Frequency is reasonable and fixed

---

## Legal & Compliance

### Privacy
- [ ] Privacy policy written and accessible
- [ ] Data collection matches policy
- [ ] No unnecessary data collection
- [ ] GDPR compliance (if applicable)
- [ ] COPPA compliance (if applicable)
- [ ] Data deletion mechanism exists

### App Store Guidelines
- [ ] Content appropriate for age rating
- [ ] No prohibited content
- [ ] Screenshots accurate to gameplay
- [ ] Description not misleading
- [ ] Required disclosures included

### Legal
- [ ] All assets properly licensed
- [ ] No trademark infringement
- [ ] No copyrighted content without permission
- [ ] Credits/attributions included

---

## Analytics Setup

### Quality Metrics Only (per CONSTRAINTS.md)
- [ ] Crash reporting enabled
- [ ] Load time tracking
- [ ] Level completion tracking
- [ ] Tutorial completion tracking
- [ ] Performance metrics

### Prohibited Metrics NOT Collected
- [ ] No ad optimization tracking
- [ ] No purchase conversion optimization
- [ ] No engagement manipulation metrics
- [ ] No user segmentation for monetization

---

## Store Listing

### Required Assets
- [ ] App icon (all required sizes)
- [ ] Screenshots (all required sizes)
- [ ] Feature graphic (if applicable)
- [ ] Promotional video (optional)

### Metadata
- [ ] App name finalized
- [ ] Description written (accurate, not misleading)
- [ ] Keywords/tags selected
- [ ] Category selected
- [ ] Age rating determined
- [ ] Contact email set
- [ ] Privacy policy URL set

### Localization (if applicable)
- [ ] Store listing translated
- [ ] In-game text translated
- [ ] Screenshots for each locale

---

## Testing Sign-Off

### Device Testing
- [ ] Tested on low-end device
- [ ] Tested on mid-range device
- [ ] Tested on high-end device
- [ ] Tested on different screen sizes
- [ ] Tested on different OS versions

### Scenario Testing
- [ ] Fresh install experience
- [ ] Resume after background
- [ ] Resume after device restart
- [ ] Interrupt during gameplay (call, notification)
- [ ] Offline behavior
- [ ] Low storage handling
- [ ] Low battery handling

### Edge Cases
- [ ] Rapid repeated input
- [ ] Input during transitions
- [ ] Back button behavior
- [ ] Screen rotation (if supported)
- [ ] Multi-touch (if applicable)

---

## Pre-Launch Tasks

### Build
- [ ] Release build created (not debug)
- [ ] Build signed correctly
- [ ] Version number incremented
- [ ] All debug code removed
- [ ] All test content removed

### Backup
- [ ] Source code committed
- [ ] Assets backed up
- [ ] Build archived

### Documentation
- [ ] Release notes written
- [ ] Known issues documented
- [ ] Support FAQ prepared

---

## Final Approval

### Human Review Required

Before deployment, ensure human reviews:
- [ ] Complete playthrough of final build
- [ ] Monetization implementation
- [ ] Privacy policy and data collection
- [ ] Store listing accuracy
- [ ] All checklist items above

### Approval Record

| Reviewer | Date | Approved | Notes |
|----------|------|----------|-------|
| | | | |

---

## Post-Launch Monitoring

After launch, monitor:
- [ ] Crash reports
- [ ] User reviews
- [ ] Quality metrics
- [ ] Download/usage patterns

Have plan for:
- [ ] Critical bug hotfix process
- [ ] User feedback response
- [ ] First update timeline

---

*All items must be checked before requesting deployment approval. Do not skip items even if they seem unnecessary.*
