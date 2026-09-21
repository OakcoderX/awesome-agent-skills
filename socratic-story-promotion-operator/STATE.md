# Promotion State

## Current objective
Generate new evidence of real adoption for Socratic Story Cartographer, with emphasis on long-form narrative professionals who already use AI for story review.

## Current beliefs
- Segment: professional story developers working with long-form or multi-file narrative material (confidence: medium-low). No qualified external tester response has yet been observed, so this remains the strongest hypothesis rather than a validated segment.
- Value proposition: verify source coverage, attack the first diagnosis, and turn supported findings into revision decisions (confidence: medium-low). The public Skill-vs-strong-prompt claim is testable, but no independent behavioral result has yet validated the advantage.
- LinkedIn is again the highest-value professional-audience route (confidence: medium). On 2026-09-21 Metricool returned current LinkedIn best-time data and accepted a reschedule of the failed tester-recruitment post with provider status `PENDING`, so the previous authentication blocker has materially changed.
- Strongest validated external discovery route: OpenAgentSkill (confidence: medium). It produced a live `Community listed` / `Unverified` entry and concrete install/usage feedback, but still not runtime-quality or adoption evidence.
- GitHub PR #1 remains a usable public feedback surface but has produced no human tester evidence. Its only comment and +1 reaction are still from the Codex connector bot (confidence: high).
- GitHub repository adoption signals remain weak; no qualified external A/B result has yet arrived (confidence: high).
- The main near-term bottleneck is now experiment conversion rather than channel access: LinkedIn scheduling is executable again, so the next evidence should come from whether the tester ask actually reaches and converts qualified users (confidence: medium).

## Active experiment
- Hypothesis: professionals who already use AI to review long-form narrative work will volunteer for a rigorous Skill-vs-strong-prompt A/B test when the ask is framed as falsifiable product validation rather than generic promotion.
- Status: LAUNCH SCHEDULED. The original failed Metricool post was rescheduled exactly once on 2026-09-21 for 11:00 Asia/Shanghai. New Metricool post id: `379101947`; uuid remains `1023591338346497620`; LinkedIn provider status is `PENDING / Pending`.
- Supporting feedback surface: GitHub PR #1 remains open as the public external A/B tester thread and the main README links to it. On 2026-09-21 it still had no human comment or reaction.
- Success signal: at least 1 qualified tester response or substantive inquiry after successful LinkedIn publication, or an external A/B result posted to PR #1.
- Failure signal: no qualified response after successful publication and a clean 48-72 hour observation window. Scheduling or publication failure does not count as evidence against the recruitment hypothesis.

## Previous commitment
- Action: keep the tester experiment unchanged and execute immediately when LinkedIn auth recovers, a human tester appears on PR #1, OpenAgentSkill claim state changes, or a documented route becomes newly executable.
- Status: EXECUTED. On 2026-09-21 the LinkedIn condition changed: Metricool returned live best-time data and successfully accepted the existing tester-recruitment message for a new publication time. The post was rescheduled once rather than duplicated.

## Latest executed action
- Date: 2026-09-21
- Action: rechecked only the four monitored conditions. PR #1 still had no human feedback; OpenAgentSkill #118 remained closed with five comments and no maintainer response after the ownership inquiry; known 403 registry routes were not retried. LinkedIn was the changed condition, so the existing tester-recruitment post was rescheduled to the next strong professional window, 2026-09-21 11:00 Asia/Shanghai.
- External state change: Metricool created updated post id `379101947` with the original message, auto-publish enabled, and LinkedIn provider status `PENDING`. A second read of the planner confirmed the post remains scheduled for 11:00 with the same uuid.
- Evidence: Metricool best-time data was available for LinkedIn on 2026-09-21; Monday 11:00 was the strongest remaining near-term slot. The update call returned `PENDING / Pending`, and `getScheduledPosts` independently returned the same scheduled state.
- Failed route / fallback: no fallback was needed because the highest-priority route became executable.

## Stopped tactics
- Generic weekly review without execution
- Treating README edits or internal planning as sufficient promotion progress
- Repeating generic Reddit/LinkedIn announcements without new evidence
- Switching strategy merely because a new week begins
- Rediscovering known blocked routes on every run
- Treating the stale `skillsdir.dev` GitHub issue route as executable unless its submission backend changes
- Opening duplicate directory submissions merely to satisfy an execution quota while an active experiment is awaiting clean evidence
- Duplicating the LinkedIn recruitment message during the active publication/observation window
- Retrying `libukai/awesome-agent-skills`, OmniSkill, AgentCaps, or AgentSkillsHub through the same GitHub integration until permissions change
- Submitting upstream to `VoltAgent/awesome-agent-skills` before the skill has real community usage; current contribution rules require community-adopted, proven skills
- Treating directory count as the next growth lever while the first qualified external A/B result is still missing
- Allowing a no-trigger daily run to disable the promotion loop; unchanged blocker state should remain a quiet watch state instead

## Blockers requiring human action
- OpenAgentSkill ownership verification supports repository-file proof, but starting the claim/challenge requires signing in to the OpenAgentSkill website. The smallest human step is to sign in and start `Verify ownership`; if GitHub OAuth matches `OakcoderX`, verification may be immediate, otherwise the site will issue a repository-file challenge that the operator can complete in GitHub.
- AgentSkillsHub accepts a manual GitHub issue submission and is relevant enough to keep as a fallback, but the current integration cannot create that external issue. If chosen later, the smallest human step is to open one prepared submission issue; do not submit the automated form as though it uniquely indexes the subdirectory.
- `libukai/awesome-agent-skills`, OmniSkill, and AgentCaps external GitHub submissions may require a minimal manual issue/comment submission unless GitHub integration permission changes; do not hand off all of them merely to increase volume.
- Some discovery routes require site GitHub authorization, a non-fork repository, repository topics, or payment. Do not escalate these into migration/payment work until one has a clear expected discovery advantage over obtaining the first qualified tester.
- External GitHub registry submissions that require a first fork remain blocked when no authenticated fork exists and the connector cannot create one.

## Next committed action
Preserve the now-launched LinkedIn experiment. On the next watch, first verify whether post `379101947` actually published successfully. If published, inspect only conversion-quality evidence for 48-72 hours: qualified tester replies, substantive inquiries, or external A/B results on PR #1. Do not duplicate outreach during that clean window. If a qualified tester appears, convert that contact into the published Skill-vs-strong-prompt protocol before opening another channel. If publication fails again, treat it as an infrastructure blocker and resume the documented fallback hierarchy without counting it as a negative message result.