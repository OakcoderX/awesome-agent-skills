# Socratic Story Cartographer — Promotion Log

Last updated: 2026-08-20

This file is the working record for distribution experiments. The goal is not maximum posting volume; it is to learn which channels produce real installs, real story tests, and useful feedback.

## Distribution strategy

Target: 14 channels in three waves.

### Wave A — Agent / Skill discovery (highest intent)

| Channel | Why it matters | Action owner | Status | Result / next signal |
|---|---|---|---|---|
| skills.sh | Cross-agent install ecosystem; real installs create discovery/leaderboard signals | Automatic after real user installs | READY | No public listing signal yet; acquire first real installs |
| SkillsMP | Large GitHub-indexed Agent Skill marketplace | Automatic crawl / monitor | READY | Exact-name search not yet surfaced; wait for re-crawl after metadata normalization |
| dmgrok Agent Skills Directory | Quality/security-validated directory with provider submissions | User must submit GitHub issue; current GitHub App has read-only access there | PREPARED | Submission body prepared in PROMOTION_KIT.md |
| Claude Skills Directory (skillsdir.dev) | Explicit community submission flow; accepts SKILL.md + links | User: GitHub issue or `skill publish` login | PREPARED | Submit after first external validation |
| SkillsDirectory.com | Large scanned skills catalog with GitHub-authenticated submission | User: GitHub sign-in/form | PREPARED | Submit after first external validation |
| SkillHub | Writing category + publish flow; supports uploaded SKILL.md/ZIP | User: account/upload | PREPARED | Submit after first external validation |

### Wave B — AI / developer communities

| Channel | Why it matters | Action owner | Status | Notes |
|---|---|---|---|---|
| r/claudeskills | Direct Skill Share audience | User | PREPARED | Use Skill Share framing, not generic advertising |
| r/ClaudeCode | Large harness audience; benchmark/eval framing fits | User | PREPARED | Lead with self-falsifying diagnosis + benchmark, not creative-writing pitch |
| V2EX | Chinese Claude Code / Codex / Agent Skill builders are active | User | PREPARED | Chinese technical post; installation command near top |
| Hacker News Show HN | Good fit for open-source AI tooling with technical methodology | User | PREPARED | Use benchmark and design rationale; avoid marketing copy |

### Wave C — creators who actually need the skill

| Channel | Why it matters | Action owner | Status | Notes |
|---|---|---|---|---|
| r/WritingWithAI | Large community explicitly discussing AI as editor/co-writer | User | PREPARED | Ask for real manuscripts/tests, not stars |
| r/Writers | Allows resources but warns against spam | User | OPTIONAL | Frame as request for critique / first-test, not repeated promotion |
| 即刻 | Chinese AI + creative-professional overlap | User | PREPARED | Short Chinese post + personal origin + 3-minute test |
| 知乎 | Best home for the longer article explaining Socratic prompting + benchmark | User | PREPARED | Publish full reasoning article; link repo at end |

## Explicit exclusions

- r/writing: do not post. Its current rules prohibit generative-AI advocacy/content.
- r/selfpublish: do not post. Current rules prohibit AI posts and restrict self-promotion.
- Repeated cross-posts to adjacent Reddit communities in the same day: avoid.
- VoltAgent/awesome-agent-skills upstream PR: defer. Their contribution rules require real community usage for new community skills.

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
- Updated belief: highest-value sequence is standards compliance → real installs → quality-directory submissions → wider social promotion.

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
