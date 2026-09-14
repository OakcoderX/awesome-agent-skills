# Promotion State

## Current objective
Generate new evidence of real adoption for Socratic Story Cartographer, with emphasis on long-form narrative professionals who already use AI for story review.

## Current beliefs
- Segment: professional story developers working with long-form or multi-file narrative material (confidence: medium-low). No qualified external tester response has yet been observed, so this remains the strongest hypothesis rather than a validated segment.
- Value proposition: verify source coverage, attack the first diagnosis, and turn supported findings into revision decisions (confidence: medium-low). The public Skill-vs-strong-prompt claim is now easier to test, but no independent behavioral result has yet validated the advantage.
- Strongest validated external route: OpenAgentSkill for discovery and registry-quality onboarding feedback (confidence: medium). It produced a live `Community listed` entry and concrete install/usage feedback, but not runtime-quality or adoption evidence.
- LinkedIn remains the most plausible professional-audience channel, but the tester-recruitment experiment is still unlaunched because Metricool reports `authentication failure` (confidence: medium-low).
- GitHub is now a usable public feedback surface through PR #1, but not yet a validated discovery channel. Repository adoption remains weak and unchanged at 1 star / 1 fork (confidence: high).
- External GitHub directory submissions remain broadly permission-limited in the current integration: `libukai/awesome-agent-skills`, OmniSkill, and AgentCaps previously returned `403 Resource not accessible by integration` (confidence: high).

## Active experiment
- Hypothesis: professionals who already use AI to review long-form narrative work will volunteer for a rigorous Skill-vs-strong-prompt A/B test when the ask is framed as falsifiable product validation rather than generic promotion.
- Status: BLOCKED / NOT LAUNCHED on LinkedIn. Metricool post `371923844` was scheduled for 2026-09-11 11:00 Asia/Shanghai and still reports LinkedIn provider `ERROR / authentication failure`. Because its publication time is now in the past, a successful reconnection will require rescheduling the same recruitment message once at a new best-time window rather than assuming the old post will recover automatically.
- Supporting feedback surface: GitHub PR #1 is now open as a public external A/B tester thread and the main README links to it.
- Success signal: at least 1 qualified tester response or substantive inquiry after a successful audience-facing launch, or an external A/B result posted to PR #1.
- Failure signal: no qualified response after a successful publication and reasonable observation window. Authentication failure does not count as evidence against the recruitment hypothesis.

## Previous commitment
- Action: inspect `Leon-Drq/openagentskill#118` for a maintainer response, the OpenAgentSkill claim/verification path, and Metricool for LinkedIn authentication recovery; avoid retrying known 403 registry routes without permission change.
- Status: EXECUTED. Issue #118 still has no maintainer reply after the ownership inquiry. Metricool still reports the same LinkedIn authentication failure and no LinkedIn post analytics rows for 2026-09-07 through 2026-09-14. Code inspection of OpenAgentSkill established that a one-time repository-file ownership proof is supported, but creating the claim/challenge requires an authenticated OpenAgentSkill user session; GitHub OAuth owner-match can approve instantly, otherwise the site issues a 24-hour repository-file challenge.

## Latest executed action
- Date: 2026-09-14
- Action: completed Weekly Mode using only executed/observed evidence. Verified OpenAgentSkill #118, Metricool scheduled-post state, LinkedIn analytics, current GitHub adoption, and recent repository activity. Because LinkedIn remained blocked and repeated external-registry writes are known permission failures, created an independent public feedback surface inside the connected GitHub repository: branch `cartographer-feedback-thread-20260914`, file `socratic-story-cartographer/EXTERNAL-TESTER-FEEDBACK.md`, and open PR #1 titled `Feedback thread: Socratic Story Cartographer external A/B tests`. Then made the week's single evidence-justified README improvement by linking the public A/B section directly to PR #1 for tester reports.
- External state change: PR #1 is publicly open for external tester comments, and the main Cartographer README now exposes that feedback route. This does not prove adoption; it removes a concrete feedback-conversion gap while Issues are disabled.
- Evidence: PR #1 is open at `https://github.com/OakcoderX/awesome-agent-skills/pull/1`; README commit `282082386eca599f25a78ce9d83ce86b0f0da391` links external testers to that thread. The fork still reports 1 star / 1 fork. Metricool returns zero LinkedIn post rows for the week and post `371923844` remains `ERROR / authentication failure`. OpenAgentSkill #118 still has five comments with no response after the ownership inquiry.
- Failed route / fallback: primary professional-audience route remained blocked by LinkedIn authentication. OpenAgentSkill verification could not be completed non-interactively because claim creation requires a site-authenticated user session. Known external registry routes were not wastefully retried. Fallback was a non-spam, public GitHub feedback thread that directly supports the pending A/B recruitment experiment.

## Stopped tactics
- Generic weekly review without execution
- Treating README edits or internal planning as sufficient promotion progress
- Repeating generic Reddit/LinkedIn announcements without new evidence
- Switching strategy merely because a new week begins
- Rediscovering known blocked routes on every run
- Treating the stale `skillsdir.dev` GitHub issue route as executable unless its submission backend changes
- Opening duplicate directory submissions merely to satisfy an execution quota while an active experiment is awaiting clean evidence
- Rescheduling or duplicating the LinkedIn recruitment message while Metricool still reports the same authentication failure
- Assuming the failed 2026-09-11 LinkedIn post can publish automatically after reconnection; it must be deliberately rescheduled once because the original publication time is past
- Retrying `libukai/awesome-agent-skills`, OmniSkill, or AgentCaps through the same GitHub integration until permissions change
- Submitting upstream to `VoltAgent/awesome-agent-skills` before the skill has real community usage; current CONTRIBUTING rules explicitly require community-adopted, proven skills

## Blockers requiring human action
- Metricool's LinkedIn connection must be reconnected/re-authorized by the account owner before LinkedIn publishing is executable again.
- OpenAgentSkill ownership verification supports repository-file proof, but starting the claim/challenge requires signing in to the OpenAgentSkill website. The smallest human step is to sign in and start `Verify ownership`; if GitHub OAuth matches `OakcoderX`, verification may be immediate, otherwise the site will issue a repository-file challenge that the operator can complete in GitHub.
- `libukai/awesome-agent-skills`, OmniSkill, and AgentCaps external GitHub submissions may require a minimal manual issue/comment submission unless GitHub integration permission changes; do not hand off all three merely to increase volume.
- External GitHub registry submissions that require a first fork remain blocked when no authenticated fork exists and the connector cannot create one.
- Web-form-only directories may require a minimal manual submission step after the operator prepares all fields.
- Gmail direct-outreach search remains gated by interactive user input in this automation runtime, so it is not an executable fallback here.

## Next committed action
First inspect only three decision-relevant signals: comments/reactions on GitHub PR #1, any maintainer response or claim-state change for OpenAgentSkill #118/listing, and Metricool LinkedIn authentication. If LinkedIn authentication is restored, reschedule the original tester-recruitment message exactly once at the next strong LinkedIn window and begin a clean 48-72 hour observation period; while current best-time data holds, prefer a workday 11:00 Asia/Shanghai slot, especially Friday. If PR #1 receives an external result first, respond to that evidence before launching new promotion. Do not retry known 403 directory routes or add generic channels without new evidence.