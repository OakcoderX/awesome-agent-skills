# Promotion State

## Current objective
Generate new evidence of real adoption for Socratic Story Cartographer, with emphasis on long-form narrative professionals who already use AI for story review.

## Current beliefs
- Segment: professional story developers working with long-form or multi-file narrative material (confidence: medium-low)
- Value proposition: verify source coverage, attack the first diagnosis, and turn supported findings into revision decisions (confidence: medium)
- LinkedIn through Metricool is not currently executable because the scheduled recruitment post failed on provider authentication; its value as an audience channel remains plausible but this experiment is still untested (confidence: medium-low)
- External skill directories can produce independent discovery/review evidence without contaminating recruitment tests. OpenAgentSkill already produced a live community listing plus actionable onboarding feedback, but the listing remains unverified and the ownership inquiry has no maintainer response yet (confidence: medium)
- New external GitHub directory submissions are broadly permission-limited in the current GitHub integration: `libukai/awesome-agent-skills`, OmniSkill, and AgentCaps all returned `403 Resource not accessible by integration` on attempted writes. Treat this as an execution constraint rather than evidence against those channels (confidence: high)

## Active experiment
- Hypothesis: professionals who already use AI to review long-form narrative work will volunteer for a rigorous Skill-vs-strong-prompt A/B test when the ask is framed as falsifiable product validation rather than generic promotion.
- Status: BLOCKED / NOT LAUNCHED. Metricool post `371923844` was scheduled for 2026-09-11 11:00 Asia/Shanghai; on 2026-09-13 Metricool still returned it as scheduled with LinkedIn provider status `ERROR` and detailed status `authentication failure`.
- Success signal: at least 1 qualified tester response or substantive inquiry from the recruitment message after it is actually published.
- Failure signal: no qualified response after a successful publication and reasonable observation window. The current authentication failure is an execution failure, not evidence against the recruitment hypothesis.

## Previous commitment
- Action: inspect `Leon-Drq/openagentskill#118` for a maintainer response, re-check LinkedIn authentication without rescheduling, and if both remained blocked choose another independent route only when it had real discovery/feedback value.
- Status: EXECUTED. OpenAgentSkill #118 had no new maintainer response; LinkedIn still reported the same authentication failure. Two independent registry routes with real expected discovery value were then tried in a fallback chain, but both writes were blocked by GitHub integration permissions and verification confirmed that neither submission was created.

## Latest executed action
- Date: 2026-09-13
- Action: verified the previous commitment first. OpenAgentSkill issue #118 still contained the 2026-09-12 repository-ownership inquiry with no maintainer reply. Metricool still reported LinkedIn post `371923844` as `ERROR / authentication failure`, so no duplicate recruitment was launched. A fresh independent discovery route was then evaluated: OmniSkill Registry / `diegosouzapw/awesome-omni-skill` visibly accepts repository submissions and recent manual indexing issues; duplicate search found no Cartographer submission, but creating `Add Socratic Story Cartographer skill` returned `403 Resource not accessible by integration`. Fallback moved to AgentCaps Registry issue #1, an open standing intake explicitly requesting SKILL.md URLs plus audience/tags/capabilities; the issue had zero comments, but posting a complete Cartographer submission comment also returned `403 Resource not accessible by integration`.
- External state change: none on audience/discovery surfaces in this run. Post-write verification found no Socratic Story Cartographer issue in OmniSkill and AgentCaps issue #1 still had zero comments. The active LinkedIn experiment was deliberately preserved rather than duplicated.
- Evidence: Metricool post `371923844` remains scheduled with LinkedIn provider `status=ERROR`, `detailedStatus=authentication failure`; OpenAgentSkill #118 has no reply after comment `5642783940`; OmniSkill exact issue search returned no Cartographer submission after the failed write; AgentCaps issue #1 remained open with `comments=0` after the failed write. The maintained route pool was updated in commit `6a0fa2504245359631c36661d7af0d303c9ec29b` so these permission blockers will not be rediscovered daily.
- Failed route / fallback: primary LinkedIn route remained blocked by authentication. OpenAgentSkill had no new response and was intentionally not spammed. OmniSkill issue creation failed with 403. AgentCaps standing-intake comment failed with 403. Because no remaining non-contaminating route with both real expected value and executable write permission was available, the run stopped after required state/route maintenance rather than manufacturing activity.

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
- Retrying OmniSkill issue creation through the same GitHub integration until permissions change
- Retrying AgentCaps issue comments through the same GitHub integration until permissions change

## Blockers requiring human action
- Metricool's LinkedIn connection must be reconnected/re-authorized by the account owner before LinkedIn publishing is executable again.
- `libukai/awesome-agent-skills`, OmniSkill, and AgentCaps external GitHub submissions may require a minimal manual issue/comment submission unless GitHub integration permission changes; do not hand off all three merely to increase volume.
- External GitHub registry submissions that require a first fork remain blocked when no authenticated fork exists and the connector cannot create one.
- Web-form-only directories may require a minimal manual submission step after the operator prepares all fields.
- Gmail direct-outreach search was previously gated by an interactive user-input requirement in this automation runtime, so it is not currently an executable fallback here.
- No human action is yet required for the OpenAgentSkill ownership inquiry; wait for maintainer evidence before escalating.

## Next committed action
First inspect only three decision-relevant signals: `Leon-Drq/openagentskill#118` for a maintainer response, the public OpenAgentSkill listing for any claim/verification or usage-signal change, and Metricool for LinkedIn authentication recovery. If OpenAgentSkill provides an executable repository-proof step, complete it and verify the listing. If LinkedIn authentication is restored, publish the original tester-recruitment experiment once and begin a clean observation window. Do not retry `libukai`, OmniSkill, or AgentCaps through the same GitHub integration while permissions are unchanged. If all three signals are unchanged and no newly executable independent route has real expected information/discovery value, deliberately preserve the blocked experiment and perform only necessary state maintenance; the highest-value unavoidable human step remains reconnecting LinkedIn in Metricool.