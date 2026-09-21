# Distribution Routes

Use this file as a maintained action pool. Prefer routes with current evidence and available execution permissions. Re-check details before submitting because external venues can change.

## 1. LinkedIn via Metricool

Current status: executable again as of 2026-09-21. Metricool returned current LinkedIn best-time data and accepted the previously failed tester-recruitment message for a new publication time with provider status `PENDING`.

Current evidence:
- original tester-recruitment post `371923844` was due 2026-09-11 11:00 Asia/Shanghai and failed with `ERROR / authentication failure`
- on 2026-09-21, LinkedIn best-time lookup succeeded and the original message was rescheduled exactly once to 2026-09-21 11:00 Asia/Shanghai
- updated Metricool post id is `379101947`; uuid remains `1023591338346497620`
- post-read verification returned LinkedIn provider status `PENDING / Pending`
- this is restored scheduling evidence, not yet publication or adoption evidence

Best current use:
- professional story developers
- producers, editors, screenwriters, long-form AI users
- tester recruitment
- proof-led case studies
- value-proposition experiments

Operational rule:
- do not duplicate the recruitment message while post `379101947` is pending or during its clean 48-72 hour observation window after successful publication
- first verify actual publication state after the scheduled time
- judge the experiment on qualified tester replies, substantive inquiries, or external A/B results, not impressions
- if publication fails again, treat it as infrastructure failure rather than message failure and resume the documented fallback hierarchy
- prefer evidence, protocols, failures, and concrete workflow pain over generic announcements
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
- PR #1 is intentionally open as the external A/B feedback thread. As of 2026-09-21 it has no human tester response; its only comment and +1 reaction are bot-generated and must not be counted as adoption evidence.

## 3. OpenAgentSkill

Repository: `Leon-Drq/openagentskill`
Website: `https://www.openagentskill.com/`

Current status: Socratic Story Cartographer is live as a `Community listed` / `Unverified` entry after static checks passed. An ownership/claim-path inquiry is active on issue #118, but no maintainer response was present when rechecked on 2026-09-21.

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
- on 2026-09-21, issue #118 still had five comments and no response after that ownership inquiry
- code inspection established that claim creation requires a site-authenticated OpenAgentSkill session; GitHub OAuth owner-match may verify immediately, otherwise the site can issue a 24-hour repository-file challenge
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

## 5. AgentCaps Registry

Repository: `agentcaps/registry`
Standing intake: `agentcaps/registry#1` — `Submit your SKILL.md URL`

Observed submission model:
- the open standing issue explicitly invites maintainers to comment with a SKILL.md URL, purpose, audience, suggested tags/capabilities, and representative queries
- the stated goal is to improve import behavior, CatalogEntry mapping, validation findings, and search quality
- this is a relevant external discovery/validation route rather than a generic announcement channel

Current execution constraint:
- issue #1 was verified open on 2026-09-13 with zero comments
- a complete Socratic Story Cartographer submission comment was attempted on 2026-09-13
- GitHub returned `403 Resource not accessible by integration`
- issue #1 remained at zero comments after verification, so no submission occurred

Use when:
- GitHub integration permission changes, or a minimal human comment handoff is justified by expected registry/import feedback

Operational rule:
- do not retry the same connector write daily while permission is unchanged
- if eventually submitted, do not duplicate while awaiting import/validation feedback

## 6. OmniSkill Registry

Website: `https://omniskill.online/`
Repository / manual fallback: `diegosouzapw/awesome-omni-skill`

Observed submission model:
- the public registry exposes a `Submit a Skill Repository` flow for a GitHub repository containing SKILL.md files
- recent repository issues are also being used as manual indexing requests when the public submit path fails
- the repository is an external aggregator/discovery surface, so a successful submission would create independent discovery evidence

Current execution constraint:
- exact duplicate search on 2026-09-13 found no Socratic Story Cartographer issue
- a prepared `Add Socratic Story Cartographer skill` issue was attempted on 2026-09-13
- GitHub returned `403 Resource not accessible by integration`
- a post-attempt duplicate search still found no submission, confirming no external state change
- the current runtime also cannot operate the interactive website form directly

Use when:
- GitHub integration permission changes, or the registry exposes an executable non-interactive submission route

Operational rule:
- do not retry the same GitHub issue write daily while permission is unchanged

## 7. AgentSkillsHub

Repository: `zhuyansen/agent-skills-hub`
Website: `https://agentskillshub.top/`

Current status: active external Agent Skills directory and discovery route. The repository reported 357 stars when checked on 2026-09-14, and its README says community submissions can use the homepage form or open a GitHub issue; submitted repositories enter the next 8-hour sync.

Observed submission model:
- homepage `Submit Skill` flow for a GitHub repository
- GitHub issue fallback explicitly documented in the README
- recent issues #15 and #16 are repository-submission examples
- directory classifies/scans Agent Skills, MCP servers, Codex skills, and related projects and refreshes its dataset every 8 hours

Important subdirectory caveat:
- frontend `sbSubmitSkill()` extracts only `owner/repo` from the supplied GitHub URL and deduplicates on `repo_full_name`
- therefore submitting `https://github.com/OakcoderX/awesome-agent-skills/tree/main/socratic-story-cartographer` through the automated form collapses to `OakcoderX/awesome-agent-skills` rather than uniquely identifying the Cartographer subdirectory
- for this Skill, the manual issue route is preferable because it can name the subdirectory and provide Skill-specific metadata

Current execution constraint:
- duplicate search on 2026-09-14 found no existing `Socratic Story Cartographer` submission issue
- a complete manual issue submission was attempted on 2026-09-14
- GitHub returned `403 Resource not accessible by integration`
- a second duplicate search verified that no issue was created
- the current runtime has no authorized arbitrary form/POST capability for the public submission form

Use when:
- GitHub integration permission changes, or a minimal manual issue submission becomes justified

Operational rule:
- do not retry the same connector write daily while permission is unchanged
- if submitted manually, use the issue route rather than assuming the automated repo-level form creates a distinct subdirectory Skill entry
- verify actual indexing after at least one sync cycle; issue creation alone is not listing evidence

## 8. Agent Mag Skills Registry

Repository: `Agent-mag/skills`

Observed submission model:
- community contributions via pull request
- requires registry-specific skill files such as `manifest.json`, `prompt.md`, and tools/config metadata

Current execution constraint:
- the available GitHub connector does not expose repository forking, so a first-time external fork/PR may require a human setup step unless a compatible fork already exists in the authenticated account.

Use when:
- the Cartographer is packaged to the registry schema
- the expected discovery value justifies maintaining a second package format

## 9. Microsoft cat-agent-skills

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

## 10. Agent Skill Source

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

## 11. Reddit / community forums

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