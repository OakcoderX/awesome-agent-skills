# Promotion State

## Current objective
Generate new evidence of real adoption for Socratic Story Cartographer, with emphasis on long-form narrative professionals who already use AI for story review.

## Current beliefs
- Segment: professional story developers working with long-form or multi-file narrative material (confidence: medium-low). No qualified external tester response has yet been observed, so this remains the strongest hypothesis rather than a validated segment.
- Value proposition: verify source coverage, attack the first diagnosis, and turn supported findings into revision decisions (confidence: medium-low). The public Skill-vs-strong-prompt claim is testable, but no independent behavioral result has yet validated the advantage.
- Strongest validated external route: OpenAgentSkill for discovery and registry-quality onboarding feedback (confidence: medium). It produced a live `Community listed` entry and concrete install/usage feedback, but still not runtime-quality or adoption evidence.
- LinkedIn remains the most plausible professional-audience channel, but the tester-recruitment experiment is still unlaunched because Metricool continues to report `authentication failure` (confidence: medium-low). This is a channel-access failure, not a negative result for the message or segment.
- GitHub PR #1 remains a usable public feedback surface but has produced no human tester evidence. Its only comment and +1 reaction are still from the Codex connector bot (confidence: high).
- GitHub repository adoption signals remain flat at 1 star / 1 fork, and there were no repository pushes after 2026-09-14 before this weekly run (confidence: high).
- The promotion bottleneck is now distribution infrastructure/permissions more than copy optimization: the strongest audience route is auth-blocked, several external GitHub registries are write-blocked, and the daily operator had silently become disabled after the prior blocked run (confidence: high).
- A second class of discovery routes increasingly depends on repository packaging rather than message copy. Current public directories include routes that scrape GitHub topics or require non-fork repositories; the current Cartographer lives as a subdirectory of a fork, so some routes are structurally ineligible or ambiguous (confidence: medium; treat as infrastructure evidence, not a reason to migrate without a specific payoff).

## Active experiment
- Hypothesis: professionals who already use AI to review long-form narrative work will volunteer for a rigorous Skill-vs-strong-prompt A/B test when the ask is framed as falsifiable product validation rather than generic promotion.
- Status: BLOCKED / NOT LAUNCHED on LinkedIn. Metricool post `371923844`, originally scheduled for 2026-09-11 11:00 Asia/Shanghai, still reports LinkedIn provider `ERROR / authentication failure` on 2026-09-21. Because the publication time is in the past, a successful reconnection will require rescheduling the same recruitment message once at a new strong-time window rather than assuming the old post will recover automatically.
- Supporting feedback surface: GitHub PR #1 is open as a public external A/B tester thread and the main README links to it. On 2026-09-21 it still had no human comment or reaction.
- Success signal: at least 1 qualified tester response or substantive inquiry after a successful audience-facing launch, or an external A/B result posted to PR #1.
- Failure signal: no qualified response after a successful publication and reasonable observation window. Authentication failure does not count as evidence against the recruitment hypothesis.

## Previous commitment
- Action: resume external execution only when one meaningful blocker changes; highest priority LinkedIn reauthorization, otherwise OpenAgentSkill claim-state change or a documented registry route becoming executable.
- Status: EXECUTED as a watch decision, with no external trigger. On 2026-09-21 PR #1 still had no human tester response, OpenAgentSkill #118 still had exactly five comments with no maintainer response after the ownership inquiry, and Metricool still reported the same LinkedIn authentication failure. Known 403 registry routes were not retried.

## Latest executed action
- Date: 2026-09-21
- Action: audited the week's actual execution and discovered that `Daily Promotion Operator` had been disabled after its 2026-09-14 blocked run. Restored it as a watch-and-execute loop: unchanged blocker state is now treated as a normal no-trigger condition, while any LinkedIn auth recovery, human PR #1 feedback, OpenAgentSkill claim change, or documented route-permission change triggers immediate execution and verification.
- External state change: no new audience-facing distribution or adoption evidence was possible because all currently highest-value routes remain blocked. Operational state did change: the daily promotion loop is enabled again and will no longer manufacture posts or silently stop merely because no blocker changed on a given day.
- Evidence: Metricool still returns post `371923844` as `ERROR / authentication failure`; GitHub PR #1 still contains only the Codex bot comment/reaction; OpenAgentSkill #118 is still closed/completed with five comments and no response after the 2026-09-12 ownership inquiry; the repo remains at 1 star / 1 fork and had no pushes after 2026-09-14 before this run.
- Failed route / fallback: X/Metricool best-time access also returned a permissions `403`, so it is not a usable social fallback in the current connection. Known external GitHub registry writes were deliberately not retried because no permission change was observed. The fallback was to repair the recurring execution/watch layer so the next real unblock is acted on immediately instead of losing another week silently.

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
- Retrying `libukai/awesome-agent-skills`, OmniSkill, AgentCaps, or AgentSkillsHub through the same GitHub integration until permissions change
- Submitting upstream to `VoltAgent/awesome-agent-skills` before the skill has real community usage; current contribution rules require community-adopted, proven skills
- Treating directory count as the next growth lever while the first qualified external A/B result is still missing
- Allowing a no-trigger daily run to disable the promotion loop; unchanged blocker state should remain a quiet watch state instead

## Blockers requiring human action
- Metricool's LinkedIn connection must be reconnected/re-authorized by the account owner before LinkedIn publishing is executable again. This remains the highest-value unblock because it enables the active professional-tester experiment.
- OpenAgentSkill ownership verification supports repository-file proof, but starting the claim/challenge requires signing in to the OpenAgentSkill website. The smallest human step is to sign in and start `Verify ownership`; if GitHub OAuth matches `OakcoderX`, verification may be immediate, otherwise the site will issue a repository-file challenge that the operator can complete in GitHub.
- AgentSkillsHub accepts a manual GitHub issue submission and is relevant enough to keep as a fallback, but the current integration cannot create that external issue. If chosen later, the smallest human step is to open one prepared submission issue; do not submit the automated form as though it uniquely indexes the subdirectory.
- `libukai/awesome-agent-skills`, OmniSkill, and AgentCaps external GitHub submissions may require a minimal manual issue/comment submission unless GitHub integration permission changes; do not hand off all of them merely to increase volume.
- Some newly observed discovery routes require site GitHub authorization, a non-fork repository, repository topics, or payment. Do not escalate these into migration/payment work until one has a clear expected discovery advantage over simply restoring LinkedIn and obtaining the first qualified tester.
- External GitHub registry submissions that require a first fork remain blocked when no authenticated fork exists and the connector cannot create one.

## Next committed action
Keep the active tester experiment unchanged. The daily operator now watches for unblock events. Highest priority remains LinkedIn: once Metricool is re-authorized, reschedule the original tester-recruitment message exactly once at the next strong professional window and begin a clean 48-72 hour observation period, judging qualified tester responses rather than impressions. If a human tester appears first on PR #1, process that result before any new outreach. If OpenAgentSkill ownership verification is started first, complete any repository-file challenge through GitHub and verify the listing state. Do not add more directory research or packaging work until one of these conditions changes or new evidence shows a specific directory can deliver qualified users.