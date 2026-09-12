# Promotion State

## Current objective
Generate new evidence of real adoption for Socratic Story Cartographer, with emphasis on long-form narrative professionals who already use AI for story review.

## Current beliefs
- Segment: professional story developers working with long-form or multi-file narrative material (confidence: medium-low)
- Value proposition: verify source coverage, attack the first diagnosis, and turn supported findings into revision decisions (confidence: medium)
- LinkedIn through Metricool is not currently executable because the scheduled recruitment post failed on provider authentication; its value as an audience channel remains plausible but untested by this experiment (confidence: medium-low)
- External skill directories can produce independent discovery/review evidence without contaminating recruitment tests. OpenAgentSkill has produced a live community listing plus actionable onboarding feedback and is now the strongest currently executable external-feedback route, although the listing remains unverified (confidence: medium)

## Active experiment
- Hypothesis: professionals who already use AI to review long-form narrative work will volunteer for a rigorous Skill-vs-strong-prompt A/B test when the ask is framed as falsifiable product validation rather than generic promotion.
- Status: BLOCKED / NOT LAUNCHED. Metricool post `371923844` was scheduled for 2026-09-11 11:00 Asia/Shanghai, but on 2026-09-12 Metricool still returned it as scheduled with LinkedIn provider status `ERROR` and detailed status `authentication failure`.
- Success signal: at least 1 qualified tester response or substantive inquiry from the recruitment message after it is actually published.
- Failure signal: no qualified response after a successful publication and reasonable observation window. The current authentication failure is an execution failure, not evidence against the recruitment hypothesis.

## Previous commitment
- Action: after the scheduled LinkedIn post published, verify published state and inspect only conversion-quality signals; avoid duplicate recruitment during the observation window.
- Status: BLOCKED. Verification was executed, but the post did not publish because the LinkedIn provider authentication failed, so no valid observation window began.

## Latest executed action
- Date: 2026-09-12
- Action: verified that the LinkedIn recruitment experiment failed to launch, then followed the fallback chain. A targeted direct-outreach fallback through Gmail could not run in this non-interactive automation runtime because the connector required user input. A new external directory fallback was then prepared for `libukai/awesome-agent-skills`; duplicate search found no Socratic Story Cartographer submission, but GitHub issue creation returned `403 Resource not accessible by integration`. The next viable non-contaminating action was executed on the existing OpenAgentSkill listing: comment `5642783940` was posted to `Leon-Drq/openagentskill#118`, asking for the supported repository-ownership proof path to claim/verify the community listing without website OAuth.
- External state change: OpenAgentSkill maintainers now have a concrete ownership/claim request attached to the existing listing thread. This creates a new external feedback path that can either produce verification instructions or reveal that OAuth/manual proof is unavoidable.
- Evidence: Metricool post `371923844` remains scheduled with LinkedIn provider `status=ERROR`, `detailedStatus=authentication failure`; OpenAgentSkill issue #118 visibly contains comment id `5642783940`; distribution route pool updated in commit `3d243244ce438d2a33009bc61ca4cd2f86bd71ab`.
- Failed route / fallback: primary LinkedIn publication failed on authentication. Gmail direct outreach was unavailable in the non-interactive runtime. `libukai/awesome-agent-skills` accepts skill-submission issues, but the current GitHub integration cannot create one there (403). Fallback succeeded via maintainer contact on the already-listed OpenAgentSkill entry.

## Stopped tactics
- Generic weekly review without execution
- Treating README edits or internal planning as sufficient promotion progress
- Repeating generic Reddit/LinkedIn announcements without new evidence
- Switching strategy merely because a new week begins
- Rediscovering known blocked routes on every run
- Treating the stale `skillsdir.dev` GitHub issue route as executable unless its submission backend changes
- Opening duplicate directory submissions merely to satisfy an execution quota while an active experiment is awaiting clean evidence
- Rescheduling or duplicating the LinkedIn recruitment message while Metricool still reports the same authentication failure
- Retrying `libukai/awesome-agent-skills` issue creation through the same GitHub integration until permissions change

## Blockers requiring human action
- Metricool's LinkedIn connection must be reconnected/re-authorized by the account owner before LinkedIn publishing is executable again.
- `libukai/awesome-agent-skills` issue submission may require a minimal manual GitHub issue submission unless integration permission changes.
- External GitHub registry submissions that require a first fork remain blocked when no authenticated fork exists and the connector cannot create one.
- Web-form-only directories may require a minimal manual submission step after the operator prepares all fields.
- Gmail direct-outreach search was gated by an interactive user-input requirement in this automation runtime, so it is not currently an executable fallback here.
- No human action is yet required for the OpenAgentSkill ownership inquiry; wait for maintainer evidence before escalating.

## Next committed action
First inspect `Leon-Drq/openagentskill#118` for a maintainer response to the ownership-proof question. If the maintainer provides a repository-proof step executable through GitHub, complete it and verify whether the public listing changes from claimable/unverified. Also re-check the Metricool LinkedIn provider only to see whether authentication has been restored; do not reschedule the recruitment experiment while the same auth failure persists. If LinkedIn becomes healthy, publish the original tester-recruitment experiment once and begin a clean observation window. If OpenAgentSkill has no new response and LinkedIn remains blocked, do not manufacture volume; choose another independent route only if it is both executable and expected to produce real discovery or feedback.