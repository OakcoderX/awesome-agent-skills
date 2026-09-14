# Promotion State

## Current objective
Generate new evidence of real adoption for Socratic Story Cartographer, with emphasis on long-form narrative professionals who already use AI for story review.

## Current beliefs
- Segment: professional story developers working with long-form or multi-file narrative material (confidence: medium-low). No qualified external tester response has yet been observed, so this remains the strongest hypothesis rather than a validated segment.
- Value proposition: verify source coverage, attack the first diagnosis, and turn supported findings into revision decisions (confidence: medium-low). The public Skill-vs-strong-prompt claim is testable, but no independent behavioral result has yet validated the advantage.
- Strongest validated external route: OpenAgentSkill for discovery and registry-quality onboarding feedback (confidence: medium). It produced a live `Community listed` entry and concrete install/usage feedback, but not runtime-quality or adoption evidence.
- LinkedIn remains the most plausible professional-audience channel, but the tester-recruitment experiment is still unlaunched because Metricool reports `authentication failure` (confidence: medium-low).
- GitHub PR #1 is a usable public feedback surface, but it has not produced human tester evidence. Its only comment is the Codex review bot and its only +1 reaction is also from the Codex connector bot (confidence: high).
- AgentSkillsHub is a relevant external discovery candidate: its repository currently reports 357 stars, its README explicitly accepts community submissions by form or issue, and it says community submissions enter an 8-hour sync. However the current GitHub integration cannot create the submission issue, and its automated form deduplicates by repository rather than skill subdirectory, so a manual issue is the more appropriate path for this skill (confidence: high).
- External GitHub directory submissions remain broadly permission-limited in the current integration: `libukai/awesome-agent-skills`, OmniSkill, AgentCaps, and now AgentSkillsHub returned `403 Resource not accessible by integration` (confidence: high).

## Active experiment
- Hypothesis: professionals who already use AI to review long-form narrative work will volunteer for a rigorous Skill-vs-strong-prompt A/B test when the ask is framed as falsifiable product validation rather than generic promotion.
- Status: BLOCKED / NOT LAUNCHED on LinkedIn. Metricool post `371923844` was scheduled for 2026-09-11 11:00 Asia/Shanghai and still reports LinkedIn provider `ERROR / authentication failure`. Because its publication time is in the past, a successful reconnection will require rescheduling the same recruitment message once at a new strong-time window rather than assuming the old post will recover automatically.
- Supporting feedback surface: GitHub PR #1 is open as a public external A/B tester thread and the main README links to it.
- Success signal: at least 1 qualified tester response or substantive inquiry after a successful audience-facing launch, or an external A/B result posted to PR #1.
- Failure signal: no qualified response after a successful publication and reasonable observation window. Authentication failure does not count as evidence against the recruitment hypothesis.

## Previous commitment
- Action: inspect only three decision-relevant signals: comments/reactions on GitHub PR #1, any maintainer response or claim-state change for OpenAgentSkill #118/listing, and Metricool LinkedIn authentication; if still blocked, pursue only an independent route with real discovery/information value.
- Status: EXECUTED. PR #1 has no human tester response; the single comment and reaction are bot-generated. OpenAgentSkill #118 remains closed with five comments and no response after the ownership inquiry. Metricool still reports the same LinkedIn authentication failure.

## Latest executed action
- Date: 2026-09-14
- Action: after verifying the blocked primary experiment, searched for one independent discovery route rather than duplicating tester outreach. Validated `zhuyansen/agent-skills-hub` as an active Agent Skills directory (357 stars) whose README explicitly accepts community submissions by form or issue and says submissions enter the next 8-hour sync. Confirmed there was no existing Socratic Story Cartographer issue, prepared a transparent submission, and attempted to create it.
- External state change: none. The issue write failed with `403 Resource not accessible by integration`, and a post-attempt duplicate search verified that no issue was created.
- Evidence: AgentSkillsHub README documents the submission path; recent issues #15 and #16 demonstrate active repository-submission use. Its frontend `sbSubmitSkill()` implementation extracts only `owner/repo` from a GitHub URL and deduplicates on `repo_full_name`, so the automated form cannot uniquely represent the `socratic-story-cartographer` subdirectory inside `OakcoderX/awesome-agent-skills`.
- Failed route / fallback: the AgentSkillsHub GitHub issue route failed with the same integration-permission class seen on other external registries. The public form/API is intentionally available, but the current runtime has no authorized arbitrary form/POST capability, and its repository-level deduplication makes it a weaker fit for this subdirectory skill anyway. With LinkedIn auth still broken, OpenAgentSkill verification requiring site sign-in, direct email unavailable, and known registry writes blocked, no further non-contaminating external action with real expected value was executable. The active tester experiment was deliberately preserved rather than padded with duplicate promotion.

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
- Submitting upstream to `VoltAgent/awesome-agent-skills` before the skill has real community usage; current CONTRIBUTING rules explicitly require community-adopted, proven skills

## Blockers requiring human action
- Metricool's LinkedIn connection must be reconnected/re-authorized by the account owner before LinkedIn publishing is executable again. This remains the highest-value unblock because it enables the active professional-tester experiment.
- OpenAgentSkill ownership verification supports repository-file proof, but starting the claim/challenge requires signing in to the OpenAgentSkill website. The smallest human step is to sign in and start `Verify ownership`; if GitHub OAuth matches `OakcoderX`, verification may be immediate, otherwise the site will issue a repository-file challenge that the operator can complete in GitHub.
- AgentSkillsHub accepts a manual GitHub issue submission and is relevant enough to keep as a fallback, but the current integration cannot create that external issue. If chosen later, the smallest human step is to open one prepared submission issue; do not submit the automated form as though it uniquely indexes the subdirectory.
- `libukai/awesome-agent-skills`, OmniSkill, and AgentCaps external GitHub submissions may require a minimal manual issue/comment submission unless GitHub integration permission changes; do not hand off all of them merely to increase volume.
- External GitHub registry submissions that require a first fork remain blocked when no authenticated fork exists and the connector cannot create one.
- Gmail direct-outreach search remains gated by interactive user input in this runtime, so it is not an executable fallback here.

## Next committed action
Resume external execution when one meaningful blocker changes. Highest priority is LinkedIn: once Metricool is re-authorized, reschedule the original tester-recruitment message exactly once at the next strong professional window and begin a clean 48-72 hour observation period, judging qualified tester responses rather than impressions. If OpenAgentSkill ownership verification is started first, complete any repository-file challenge through GitHub and verify the listing state. If AgentSkillsHub GitHub-write permission changes, submit the prepared manual issue once and verify indexing. Until one of those states changes, do not create duplicate outreach or retry known 403 routes.