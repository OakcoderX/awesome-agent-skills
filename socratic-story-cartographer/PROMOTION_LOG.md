# Socratic Story Cartographer — Promotion Log

Last updated: 2026-08-21

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
| X / Twitter | Fastest place to test the one-line value proposition among Agent builders | Assistant via Metricool after account connection | BLOCKED_ON_ACCOUNT | LinkedIn is connected; X still needs account connection |

### Wave C — creators / professional users

| Channel | Why it matters | Action owner | Status | Notes |
|---|---|---|---|---|
| r/WritingWithAI | Community explicitly discussing AI as editor/co-writer | User | PUBLISHED | Creator falsification challenge posted 2026-08-20; collect 24h/72h response signal before reusing this message elsewhere |
| 即刻 | Chinese AI + creative-professional overlap | User | PREPARED | Short Chinese post + personal origin + 3-minute test |
| 知乎 | Best home for the long-form article explaining Socratic prompting + benchmark | User | PREPARED | Publish full reasoning article; link repo at end |
| LinkedIn | Professional AI/content-production audience; good for methodology and open-source positioning | Assistant via Metricool | PUBLISHED | Methodology/falsification post published 2026-08-21 11:00; analytics had not populated by the evening review |

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
- Publish/schedule LinkedIn through Metricool; publish/schedule X once X is connected inside the Metricool brand.

### User action currently required

- Third-party GitHub issues/PRs where the installed GitHub App has read-only access.
- Websites requiring GitHub/user sign-in or form submission (SkillsDirectory.com, SkillHub, etc.).
- Reddit, Hacker News, V2EX, 即刻 and 知乎 posting because no authenticated posting connector is available in this runtime.
- Connect X inside Metricool if X automation is wanted. LinkedIn is already connected.

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
- Initial query reported no connected social networks.
- User subsequently refreshed the social login; a later check confirmed `linkedin` is connected.
- X is not yet connected.
- Updated action: LinkedIn can now be handled by the assistant; X still requires connection if desired.

### 2026-08-20 — Creator falsification challenge

- Public search still found no exact-name listing for `Socratic Story Cartographer` on the monitored skill directories.
- A current `r/WritingWithAI` Weekly Tool Thread provides an explicitly appropriate place for tool promotion, while current Hacker News discussion shows meaningful skepticism toward Agent Skills that behave like over-engineered prompts.
- Hypothesis: asking writers to **break the skill on a story they know well** will create more useful first usage than another generic feature announcement.
- Executed: changed `FIRST-TEST.md` from a simple demo into a falsifiable test with three concrete failure modes: unsupported diagnosis, repetitive loops, and regression caused by a proposed fix.
- User then published the full creator-facing falsification challenge in `r/WritingWithAI`; screenshot confirmation received at approximately 21:43 UTC+8 on 2026-08-20.
- Observable result at launch: the post is publicly submitted; response quality, test attempts, comments, and any install signal are not yet known.
- Belief update: the experiment is now live. Do not dilute it by immediately cross-posting identical copy elsewhere.
- Next action: collect the first 24h signal, then decide whether the stronger next move is LinkedIn methodology framing, an Agent-builder challenge, or a product revision triggered by concrete failure evidence.

### 2026-08-21 — Daily review

- The Reddit falsification challenge is now discoverable in public search inside the `r/WritingWithAI` weekly tool thread. This confirms the post is live and indexable, but public search did not surface a substantive reply, independent test report, or other clear conversion event during this review.
- A separate LinkedIn methodology/falsification post was published through Metricool at 11:00 Asia/Shanghai on 2026-08-21. Metricool's post analytics endpoint still returned no populated metrics by the evening review, so impressions/clicks/reactions cannot yet be used as evidence.
- GitHub still reports 0 stars and 0 forks on the fork repository. Those are weak proxies because the skill lives inside a larger fork, but they provide no positive adoption signal yet.
- Fresh exact-name searches still did not surface `Socratic Story Cartographer` on the monitored skill directories. Discovery remains unproven.
- **Belief strengthened:** more documentation is not the current bottleneck. The repo already explains the method, benchmark, installation, and first test.
- **Belief weakened:** simply putting the same falsification message in more channels is unlikely to teach us much. Reddit and LinkedIn now provide two different audiences; wait for behavior before adding another generic channel.
- **New hypothesis:** the creator audience may face too much onboarding friction from a terminal-first `npx skills add` instruction. A useful story tool can still fail conversion if the first-run path feels like developer tooling.
- **New hypothesis:** the most important product claim is not “Socratic” but “better than one good prompt.” Until that is shown on unseen texts, promotion risks sounding like packaging around prompt engineering.

#### Next-day top three experiments

1. **24-hour conversion read on Reddit + LinkedIn.** Do not add a third broad channel before reading behavior. Success = at least one substantive signal: a real story test, an outbound click, a concrete question about using the skill, or a counterexample. Impressions alone do not count as success.
2. **First-run friction test with 3 unfamiliar users.** Give them only the public GitHub entry point and observe whether they can reach a completed first analysis without coaching. Success = at least 2/3 complete a run within 5 minutes; failure if 2/3 are blocked by CLI/harness/install ambiguity. If failed, design a no-terminal first-test path before further promotion.
3. **Skill vs. one-good-prompt blind A/B on unseen material.** Same model, same text, same evaluation dimensions: evidence anchoring, diagnosis update, regression awareness, stop discipline. Success = the Skill clearly wins at least 3 of 4 dimensions on a majority of unseen texts. If not, simplify the Skill before expanding distribution.

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
