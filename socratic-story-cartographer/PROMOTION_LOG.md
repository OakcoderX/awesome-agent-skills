# Socratic Story Cartographer — Promotion Log

Last updated: 2026-08-20

This file is the working record for distribution experiments. The goal is not maximum posting volume; it is to learn which channels produce real installs, real story tests, and useful feedback.

## Distribution strategy

Target: **15 channels in three waves**. Do not publish the identical article everywhere. Registries get structured metadata, developer communities get methodology/benchmark framing, and creator communities get the editing problem + first-test framing.

### Wave A — Agent / Skill discovery (highest intent)

| Channel | Why it matters | Action owner | Status | Result / next signal |
|---|---|---|---|---|
| skills.sh | Cross-agent install ecosystem; real installs create discovery/leaderboard signals | Automatic after real user installs | READY | No public listing signal yet; acquire first real installs |
| SkillsMP | Very large GitHub-indexed Agent Skill marketplace | Automatic crawl / monitor | READY | Exact-name search not yet surfaced; wait for re-crawl after metadata normalization |
| dmgrok Agent Skills Directory | Quality/security-validated directory with provider submissions | User must submit GitHub issue; current GitHub App has read-only access there | PREPARED | Submission body prepared in `PROMOTION_KIT.md` |
| Claude Skills Directory (skillsdir.dev) | Explicit community submission flow; accepts SKILL.md + links | User: GitHub issue or `skill publish` login | PREPARED | Submission metadata prepared |
| SkillsDirectory.com | Large scanned skills catalog with GitHub-authenticated submission | User: GitHub sign-in/form | PREPARED | Submission metadata prepared |
| SkillHub | Writing category + publish flow; supports uploaded SKILL.md/ZIP | User: account/upload | PREPARED | Submission metadata prepared |

### Wave B — AI / developer communities

| Channel | Why it matters | Action owner | Status | Notes |
|---|---|---|---|---|
| r/claudeskills | Direct Skill Share audience | User | PREPARED | Use Skill Share framing, not generic advertising |
| r/ClaudeCode | Large harness audience; benchmark/eval framing fits | User | PREPARED | Lead with self-falsifying diagnosis + benchmark, not creative-writing pitch |
| V2EX | Chinese Claude Code / Codex / Agent Skill builders are active | User | PREPARED | Chinese technical post; installation command near top |
| Hacker News Show HN | Good fit for open-source AI tooling with technical methodology | User | PREPARED | Use benchmark and design rationale; avoid marketing copy |
| X / Twitter | Fastest place to test the one-line value proposition among Agent builders | Assistant via Metricool after account connection | BLOCKED_ON_ACCOUNT | Metricool plugin connected; Metricool brand currently reports no connected social networks |

### Wave C — creators / professional users

| Channel | Why it matters | Action owner | Status | Notes |
|---|---|---|---|---|
| r/WritingWithAI | Community explicitly discussing AI as editor/co-writer | User | PREPARED | Ask for real manuscripts/tests, not stars |
| 即刻 | Chinese AI + creative-professional overlap | User | PREPARED | Short Chinese post + personal origin + 3-minute test |
| 知乎 | Best home for the long-form article explaining Socratic prompting + benchmark | User | PREPARED | Publish full reasoning article; link repo at end |
| LinkedIn | Professional AI/content-production audience; good for methodology and open-source positioning | Assistant via Metricool after account connection | BLOCKED_ON_ACCOUNT | Metricool plugin connected; Metricool brand currently reports no connected social networks |

## Explicit exclusions

- r/writing: do not post. Its current rules prohibit generative-AI advocacy/content.
- r/selfpublish: do not post. Current rules prohibit AI posts and restrict self-promotion.
- r/Writers: deprioritized. It permits resources but is broad and self-promotion-sensitive; lower expected conversion than WritingWithAI.
- Repeated cross-posts to adjacent Reddit communities in the same day: avoid.
- VoltAgent/awesome-agent-skills upstream PR: defer. Their contribution rules require real community usage for new community skills.

## What can be automated here vs. what requires the user

### Assistant can execute directly

- Update the public GitHub skill files and documentation in `OakcoderX/awesome-agent-skills`.
- Maintain this promotion log and channel-specific copy kit.
- Monitor public search/indexing signals for skills.sh, SkillsMP, SkillHub and other directories.
- Prepare exact metadata, issue bodies, titles, install commands and community-specific drafts.
- Attempt connector-backed GitHub writes when the connected GitHub App has write permission.
- Publish/schedule X and LinkedIn through Metricool once those networks are connected inside the Metricool brand.

### User action currently required

- Third-party GitHub issues/PRs where the installed GitHub App has read-only access.
- Websites requiring GitHub/user sign-in or form submission (SkillsDirectory.com, SkillHub, etc.).
- Reddit, Hacker News, V2EX, 即刻 and 知乎 posting because no authenticated posting connector is available in this runtime.
- Connect X and LinkedIn accounts inside Metricool. The ChatGPT Metricool plugin is already connected, but the current Metricool brand reports `connectedNetworks: []`.

## Actions already completed

### 2026-08-19 / 2026-08-20 — Repository conversion funnel

- Added one-command cross-agent install to README.
- Added a 3-minute first-test flow (`FIRST-TEST.md`).
- Added public benchmark methodology and limitations (`BENCHMARK.md`).
- Normalized `SKILL.md` frontmatter so the machine name matches the directory: `socratic-story-cartographer`.
- Added standard `license`, `compatibility`, and `metadata` fields.
- Added `skill.json` and a benchmark reference file for directory/registry compatibility.
- Changed positioning from “Codex skill” to portable Agent Skill across supported harnesses.

### 2026-08-20 — External distribution investigation

- Tested direct issue creation against `dmgrok/agent-plugins`.
- Result: GitHub App returned 403 because the current connection has read-only access to that third-party repository.
- Conclusion: own-repo GitHub writes can be automated; arbitrary third-party GitHub submissions require user-level GitHub authorization not currently available in this runtime.
- Verified that an independent repository is not necessary for adoption: successful Agent Skill ecosystems often use monorepos.
- Verified current registry landscape and removed low-fit/spam-sensitive communities from the launch plan.
- Created `PROMOTION_KIT.md` with registry metadata and platform-specific drafts.
- Created this persistent `PROMOTION_LOG.md` to record all subsequent promotion experiments.
- Updated belief: highest-value sequence is standards compliance → real installs → quality-directory submissions → developer communities → creator communities.

### 2026-08-20 — Metricool automation check

- Connected the Metricool for Social Media plugin to ChatGPT.
- Queried the active Metricool brand (timezone `Asia/Shanghai`).
- Observable result: `connectedNetworks` was empty, so X and LinkedIn cannot yet be scheduled or published.
- Next action: user connects X and LinkedIn inside Metricool; assistant then chooses network-specific best times and schedules the launch posts automatically.

### 2026-08-20 — Creator falsification challenge

- Public search still found no exact-name listing for `Socratic Story Cartographer` on the monitored skill directories.
- A current `r/WritingWithAI` Weekly Tool Thread provides an explicitly appropriate place for tool promotion, while current Hacker News discussion shows meaningful skepticism toward Agent Skills that behave like over-engineered prompts.
- Hypothesis: asking writers to **break the skill on a story they know well** will create more useful first usage than another generic feature announcement.
- Executed: changed `FIRST-TEST.md` from a simple demo into a falsifiable test with three concrete failure modes: unsupported diagnosis, repetitive loops, and regression caused by a proposed fix.
- Observable result at execution time: repository conversion path now explicitly asks for counterexamples rather than praise; no external install signal is yet available.
- Belief update: the next scarce resource is not more documentation. It is independent story tests that can produce either confirmed utility or concrete failure cases.
- Next action: publish one creator-facing test invitation in the current `r/WritingWithAI` Weekly Tool Thread, then do not cross-post the same message elsewhere until there is a response signal.

## Success metrics

Track these instead of raw post count:

1. Confirmed external installs.
2. Number of people who run the skill on their own story.
3. Useful failure reports: wrong diagnosis, weak evidence, loop not updating, over-editing.
4. Registry/directory acceptance.
5. Organic mentions or stars only as secondary signals.

## Experiment rule

For each new channel, log:

- date
- channel
- exact message variant
- hypothesis
- observable result (24h / 72h when available)
- belief update
- next action

Do not repeat a channel until there is new evidence or a materially different message to test.
