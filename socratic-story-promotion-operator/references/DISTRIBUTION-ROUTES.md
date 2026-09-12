# Distribution Routes

Use this file as a maintained action pool. Prefer routes with current evidence and available execution permissions. Re-check details before submitting because external venues can change.

## 1. LinkedIn via Metricool

Current status: connector is available, but the LinkedIn publishing connection is currently blocked by authentication failure.

Current evidence:
- scheduled tester-recruitment post `371923844` was due 2026-09-11 11:00 Asia/Shanghai
- on 2026-09-12, Metricool still returned the post as scheduled with provider status `ERROR` and detailed status `authentication failure`
- therefore the recruitment experiment did not actually launch

Best current use after reconnection:
- professional story developers
- producers, editors, screenwriters, long-form AI users
- tester recruitment
- proof-led case studies
- value-proposition experiments

Operational rule:
- do not reschedule or duplicate the recruitment post while the same authentication failure persists
- the account owner must reconnect/repair the LinkedIn connection in Metricool before this route is executable again
- once restored, prefer evidence, protocols, failures, and concrete workflow pain over generic announcements
- avoid repeating substantially the same message without new evidence
- verify scheduled/published state in Metricool after every write

## 2. GitHub repository

Current status: connected with admin/push access to `OakcoderX/awesome-agent-skills`.

Best current use:
- README/onboarding changes tied to observed friction
- benchmark/protocol/result publication
- skill maintenance
- persistent promotion state
- public experiment artifacts

Known limitation:
- Issues are disabled in the current repository, so do not use issue creation as a recruitment route unless repository settings change.

## 3. OpenAgentSkill

Repository: `Leon-Drq/openagentskill`
Website: `https://www.openagentskill.com/`

Current status: verified executable through the official GitHub Skill-submission issue template; no fork is required. Socratic Story Cartographer is live as a `Community listed` / `Unverified` entry after static checks passed. An ownership/claim-path inquiry is now active on issue #118.

Observed submission model:
- open an issue titled `[Skill]: <name>` using `.github/ISSUE_TEMPLATE/skill.yml`
- provide a direct public repository / Skill-directory / SKILL.md URL
- mark `New Skill`
- include workflow, optional suggested tags, evidence, and maintainer/promoter disclosure
- repository automation validates and ingests the Skill into a review/listing pipeline

Current evidence:
- Socratic Story Cartographer submitted as issue `Leon-Drq/openagentskill#118` on 2026-09-08
- initial automation ingested it into the community review queue and requested clearer install/usage instructions inside `SKILL.md`
- the requested Quick start correction was committed on 2026-09-09 and the issue was reprocessed
- static checks passed; issue #118 closed on 2026-09-09
- OpenAgentSkill's public listing is `Community listed` and `Unverified`
- OpenAgentSkill states that claim/verification requires OAuth or repository-ownership proof
- on 2026-09-12, a maintainer-facing comment was posted on #118 asking for the supported repository-ownership proof path; comment id `5642783940`
- the listing is external discovery evidence, not evidence of runtime quality, installations, or real-user adoption

Best use:
- external discovery
- independent registry-quality feedback
- install/readiness friction detection
- ownership/verification trust signal if the claim path succeeds
- later outcome/adoption signals if usage appears

Operational rule:
- search existing issues before submitting
- respond to concrete review feedback rather than opening duplicate submissions
- distinguish `Community listed` / `Unverified` from reviewed or verified status
- verify issue comments/status and public listing state after submission
- do not resubmit merely to obtain a stronger label unless the registry explicitly requests it
- while the ownership inquiry is awaiting a response, do not post repetitive claim requests

## 4. libukai/awesome-agent-skills

Repository: `libukai/awesome-agent-skills`

Observed submission model:
- repository accepts `Add: ...` skill-submission issues; issue #124 is a current example
- submission can include repository URL, Skill directory, raw `SKILL.md`, license, category, description, compatibility, install command, and inclusion rationale
- this is relevant external discovery because the repository curates Agent Skills and explicitly welcomes issues

Current execution constraint:
- duplicate search on 2026-09-12 found no existing Socratic Story Cartographer issue
- a prepared submission was attempted on 2026-09-12, but GitHub returned `403 Resource not accessible by integration`
- therefore this route is blocked in the current GitHub connector even though the repository itself accepts issues

Use when:
- GitHub integration permission changes, or a minimal human issue-submission handoff is justified by expected discovery value

Operational rule:
- do not retry the same connector write on each daily run while permission is unchanged

## 5. Agent Mag Skills Registry

Repository: `Agent-mag/skills`

Observed submission model:
- community contributions via pull request
- requires registry-specific skill files such as `manifest.json`, `prompt.md`, and tools/config metadata

Current execution constraint:
- the available GitHub connector does not expose repository forking, so a first-time external fork/PR may require a human setup step unless a compatible fork already exists in the authenticated account.

Use when:
- the Cartographer is packaged to the registry schema
- the expected discovery value justifies maintaining a second package format

## 6. Microsoft cat-agent-skills

Repository: `microsoft/cat-agent-skills`

Observed submission model:
- add a submission under `submissions/<slug>/`
- include gallery metadata plus one canonical Agent Skill payload
- submit through pull request

Current execution constraint:
- same external-fork limitation as above unless an authenticated fork already exists.

Use when:
- the canonical SKILL.md format is accepted with limited repackaging
- submission provides meaningful external discovery

## 7. Agent Skill Source

Submission page: `agentskillsource.com/submit`

Observed submission model:
- public GitHub repository URL
- name, short/full description, version
- usage/inputs/outputs/limitations
- execution-type classification
- reviewed submission

Current execution constraint:
- submission is web-form based and the current runtime cannot perform arbitrary interactive form submission.

Minimal human handoff when chosen:
- open the submission page
- paste the prepared fields generated by the operator
- submit/complete any required human verification

The operator should prepare every field before handing off.

## 8. Reddit / community forums

Current status: public discovery/search available; direct posting is not currently connected as an executable tool.

Best use:
- only when there is new evidence, a reproducible experiment, or a question genuinely useful to the community
- do not repeat launch-style promotion

Minimal human handoff when chosen:
- prepare channel-specific copy
- name the exact community and why it is relevant
- provide the smallest posting step

## Known stale / blocked routes

### skillsdir.dev GitHub issue submission

Observed on 2026-09-08:
- `https://skillsdir.dev/add` still advertises GitHub-issue submission
- its submission link currently resolves to `brunogalvao/claude-skills-directory`, which returned 404 / Not Found

Operational rule:
- do not spend a daily run rediscovering this route unless the public submission backend visibly changes

## Route Selection Rule

For each run, choose the route that maximizes:

`expected information gain × relevance × executable now × non-spam value`

Do not choose a route merely because it is available.

If a route is blocked, record the blocker in `STATE.md`, switch to the next viable route in the same run, and avoid rediscovering the same blocker repeatedly.