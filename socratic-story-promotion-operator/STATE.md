# Promotion State

## Current objective
Generate new evidence of real adoption for Socratic Story Cartographer, with emphasis on long-form narrative professionals who already use AI for story review.

## Current beliefs
- Segment: professional story developers working with long-form or multi-file narrative material (confidence: medium-low). No qualified external tester response has yet been observed, so this remains the strongest hypothesis rather than a validated segment.
- Value proposition: verify source coverage, attack the first diagnosis, and turn supported findings into revision decisions (confidence: medium-low). The public Skill-vs-strong-prompt claim is testable, but no independent behavioral result has yet validated the advantage.
- LinkedIn remains the highest-value professional-audience route in principle, but it is currently infrastructure-blocked (confidence: medium). The rescheduled tester post failed again with `ERROR / authentication failure`, and Metricool now reports that brand `6751659` has no social network connected.
- Strongest validated external discovery route: OpenAgentSkill (confidence: medium). It produced a live `Community listed` / `Unverified` entry and concrete install/usage feedback, but still not runtime-quality or adoption evidence.
- GitHub PR #1 remains a usable public feedback surface but has produced no human tester evidence. Its only discussion remains the Codex connector bot (confidence: high).
- GitHub repository adoption signals remain weak; no qualified external A/B result has yet arrived (confidence: high).
- The tester-recruitment hypothesis is still untested. Two LinkedIn publication failures are infrastructure evidence, not negative evidence about the message or segment (confidence: high).

## Active experiment
- Hypothesis: professionals who already use AI to review long-form narrative work will volunteer for a rigorous Skill-vs-strong-prompt A/B test when the ask is framed as falsifiable product validation rather than generic promotion.
- Status: NOT LAUNCHED / INFRASTRUCTURE BLOCKED. Metricool post `379101947` (uuid `1023591338346497620`) was scheduled for 2026-09-21 11:00 Asia/Shanghai but is now `ERROR / authentication failure`. Metricool brand settings currently report no social network connected.
- Supporting feedback surface: GitHub PR #1 remains open as the public external A/B tester thread and the main README links to it. On 2026-09-22 it still had no human comment or reaction.
- Success signal: at least 1 qualified tester response or substantive inquiry after successful LinkedIn publication, or an external A/B result posted to PR #1.
- Failure signal: no qualified response after successful publication and a clean 48-72 hour observation window. Scheduling or publication failure does not count as evidence against the recruitment hypothesis.

## Previous commitment
- Action: verify whether post `379101947` actually published; if published, preserve a clean conversion window; if publication failed again, treat it as an infrastructure blocker and resume only documented non-spam fallbacks whose permission or eligibility has materially changed.
- Status: EXECUTED. On 2026-09-22 the post was verified as failed with `ERROR / authentication failure`; Metricool also reports no social network connected. No known 403 route was retried because there is no evidence that its permission changed.

## Latest executed action
- Date: 2026-09-22
- Action: ran the watch-only checks. Metricool showed post `379101947` in `ERROR / authentication failure` and brand settings reported no connected social network. GitHub PR #1 still had only the Codex bot discussion and no human tester reaction. OpenAgentSkill #118 remained closed with five comments and no maintainer response after the ownership inquiry. Known 403 registry routes were not retried.
- External state change: the LinkedIn route changed from `PENDING` to failed/disconnected. The intended recruitment experiment therefore never launched and no 48-72 hour audience observation window began.
- Evidence: Metricool `getScheduledPosts` returned LinkedIn provider status `ERROR` with detailed status `authentication failure`; `getBrandSettings` returned that brand `6751659` currently has no social network connected. PR #1 and OpenAgentSkill #118 showed no new human evidence.
- Failed route / fallback: the LinkedIn route is infrastructure-blocked. All already-documented independent fallbacks remain either permission-blocked, human-auth gated, or unchanged; no duplicate outreach or known-403 retry was performed.

## Stopped tactics
- Generic weekly review without execution
- Treating README edits or internal planning as sufficient promotion progress
- Repeating generic Reddit/LinkedIn announcements without new evidence
- Switching strategy merely because a new week begins
- Rediscovering known blocked routes on every run
- Treating the stale `skillsdir.dev` GitHub issue route as executable unless its submission backend changes
- Opening duplicate directory submissions merely to satisfy an execution quota while an active experiment is awaiting clean evidence
- Duplicating the LinkedIn recruitment message while the experiment is infrastructure-blocked or during any later clean observation window
- Retrying `libukai/awesome-agent-skills`, OmniSkill, AgentCaps, or AgentSkillsHub through the same GitHub integration until permissions change
- Submitting upstream to `VoltAgent/awesome-agent-skills` before the skill has real community usage; current contribution rules require community-adopted, proven skills
- Treating directory count as the next growth lever while the first qualified external A/B result is still missing
- Allowing a no-trigger daily run to disable the promotion loop; unchanged blocker state should remain a quiet watch state instead

## Blockers requiring human action
- Metricool currently reports no social network connected for brand `6751659`. The smallest human step is to reconnect/re-authorize LinkedIn in Metricool at `https://app.metricool.com/brands/connections?blogId=6751659`. Do not reschedule the tester post until the LinkedIn connection is verified live.
- OpenAgentSkill ownership verification supports repository-file proof, but starting the claim/challenge requires signing in to the OpenAgentSkill website. The smallest human step is to sign in and start `Verify ownership`; if GitHub OAuth matches `OakcoderX`, verification may be immediate, otherwise the site will issue a repository-file challenge that the operator can complete in GitHub.
- AgentSkillsHub accepts a manual GitHub issue submission and is relevant enough to keep as a fallback, but the current integration cannot create that external issue. If chosen later, the smallest human step is to open one prepared submission issue; do not submit the automated form as though it uniquely indexes the subdirectory.
- `libukai/awesome-agent-skills`, OmniSkill, and AgentCaps external GitHub submissions may require a minimal manual issue/comment submission unless GitHub integration permission changes; do not hand off all of them merely to increase volume.
- Some discovery routes require site GitHub authorization, a non-fork repository, repository topics, or payment. Do not escalate these into migration/payment work until one has a clear expected discovery advantage over obtaining the first qualified tester.
- External GitHub registry submissions that require a first fork remain blocked when no authenticated fork exists and the connector cannot create one.

## Next committed action
Remain in watch-and-execute mode. First watch Metricool LinkedIn connection state, PR #1 for new human feedback, OpenAgentSkill #118 / claim state, and already-documented routes for a real permission or eligibility change. If LinkedIn reconnects, reschedule the original tester-recruitment message once and verify actual publication before starting the 48-72 hour conversion window. If a human tester appears on PR #1, convert that contact directly into the published A/B protocol. If OpenAgentSkill or a documented route becomes newly executable, perform the smallest high-value non-spam action and verify the external result. If none changes, make no duplicate outreach, no known-403 retries, and no state-only maintenance edit.