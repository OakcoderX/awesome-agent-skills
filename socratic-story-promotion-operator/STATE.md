# Promotion State

## Current objective
Generate new evidence of real adoption for Socratic Story Cartographer, with emphasis on long-form narrative professionals who already use AI for story review.

## Current beliefs
- Segment: professional story developers working with long-form or multi-file narrative material (confidence: medium-low)
- Value proposition: verify source coverage, attack the first diagnosis, and turn supported findings into revision decisions (confidence: medium)
- Strongest currently executable channel: LinkedIn through Metricool (confidence: medium-low)
- External skill directories are a plausible secondary discovery route, but discovery value is not yet validated (confidence: low)

## Active experiment
- Hypothesis: professionals who already use AI to review long-form narrative work will volunteer for a rigorous Skill-vs-strong-prompt A/B test when the ask is framed as falsifiable product validation rather than generic promotion.
- Status: scheduled and independently verified as PENDING in Metricool
- Success signal: at least 1 qualified tester response or substantive inquiry from the LinkedIn recruitment post.
- Failure signal: no qualified response after the post has had a reasonable observation window.

## Previous commitment
- Action: recruit 3 long-form narrative testers for the public A/B protocol.
- Status: EXECUTED

## Latest executed action
- Date: 2026-09-07
- Action: verified the scheduled LinkedIn recruitment post remains present and PENDING in Metricool; converted the promotion process into the reusable `socratic-story-promotion-operator` Skill with persistent state and a maintained distribution-route reference.
- External state change: the LinkedIn test remains scheduled for automatic publication on 2026-09-11 11:00 Asia/Shanghai; the promotion workflow is now public/versioned and can be loaded by scheduled operators.
- Evidence: Metricool post id 371923844, uuid 1023591338346497620; GitHub skill and state committed under `socratic-story-promotion-operator/`.
- Failed route / fallback: GitHub Issues remain unavailable for recruitment. Research found external skill registries, but current runtime lacks external repository forking and arbitrary web-form submission, so these are maintained as secondary routes rather than treated as completed submissions.

## Stopped tactics
- Generic weekly review without execution
- Treating README edits or internal planning as sufficient promotion progress
- Repeating generic Reddit/LinkedIn announcements without new evidence
- Switching strategy merely because a new week begins
- Rediscovering known blocked routes on every run

## Blockers requiring human action
- External GitHub registry submissions may require an initial fork if no authenticated fork exists and the connector cannot create one.
- Web-form-only directories may require a minimal manual submission step after the operator prepares all fields.

## Next committed action
Do not add another substantially similar LinkedIn post before the current recruitment experiment produces evidence. Daily runs before publication should maintain readiness, inspect only genuinely new signals, and pursue a different high-value route only if it does not contaminate the active experiment. After the LinkedIn recruitment post publishes, inspect real responses and engagement. If at least one qualified tester responds, move immediately into test execution and feedback capture. If there is no qualified response after a reasonable observation window, treat that as evidence against the current recruitment/message approach and execute a materially different distribution route or segment test rather than repeating the same post.