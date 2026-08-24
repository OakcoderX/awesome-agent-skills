# Socratic Story Cartographer — Promotion Log

Last updated: 2026-08-24

This file is the working record for distribution experiments. The goal is not maximum posting volume; it is to learn which channels produce real installs, real story tests, and useful feedback.

## Distribution strategy

Target: **15 channels in three waves**. Do not publish the identical article everywhere. Registries get structured metadata, developer communities get methodology/benchmark framing, and creator communities get the editing problem + first-test framing.

### Wave A — Agent / Skill discovery (highest intent)

| Channel | Why it matters | Action owner | Status | Result / next signal |
|---|---|---|---|---|
| skills.sh | Cross-agent install ecosystem; real installs create discovery/leaderboard signals | Automatic after real user installs | HOLD | Exact-name public search still does not surface the skill; do not optimize for registry placement before real usage evidence |
| SkillsMP | Very large GitHub-indexed Agent Skill marketplace | Automatic crawl / monitor | HOLD | Exact-name public search still does not surface the skill; monitor, but do not spend launch effort here yet |
| dmgrok Agent Skills Directory | Quality/security-validated directory with provider submissions | User must submit GitHub issue; current GitHub App has read-only access there | DEFER | Submission body exists, but community-usage evidence is still too weak |
| Claude Skills Directory (skillsdir.dev) | Explicit community submission flow; accepts SKILL.md + links | User | DEFER | Wait for external usage proof |
| SkillsDirectory.com | Large scanned skills catalog with GitHub-authenticated submission | User | DEFER | Wait for external usage proof |
| SkillHub | Writing category + publish flow; supports uploaded SKILL.md/ZIP | User | DEFER | Wait for external usage proof |

### Wave B — AI / developer communities

| Channel | Why it matters | Action owner | Status | Notes |
|---|---|---|---|---|
| r/claudeskills | Direct Skill Share audience | User | NEXT_AFTER_PROOF | Use A/B evidence, not a generic launch post |
| r/ClaudeCode | Large harness audience; benchmark/eval framing fits | User | NEXT_AFTER_PROOF | Lead with “Skill vs one good prompt” evidence |
| V2EX | Chinese Claude Code / Codex / Agent Skill builders are active | User | HOLD | Do not publish until there is one clean external proof case |
| Hacker News Show HN | Good fit for open-source AI tooling with technical methodology | User | HOLD | Current objection is exactly whether Skills add functional depth beyond prompts; answer with evidence before posting |
| X / Twitter | Fast place to test one-line value proposition among Agent builders | Assistant via Metricool after connection | BLOCKED_ON_ACCOUNT | X is still not connected |

### Wave C — creators / professional users

| Channel | Why it matters | Action owner | Status | Notes |
|---|---|---|---|---|
| r/WritingWithAI | Community explicitly discussing AI as editor/co-writer | User | PUBLISHED | Creator falsification challenge posted 2026-08-20; public search shows it remains indexable, but no substantive external test report is visible |
| 即刻 | Chinese AI + creative-professional overlap | User | HOLD | Do not reuse generic launch copy; wait for proof-led post |
| 知乎 | Long-form home for methodology and benchmark | User | HOLD | Best used after an external case study exists |
| LinkedIn | Professional AI/content-production audience | Assistant via Metricool | STRONGEST_SIGNAL | 2026-08-21 post: 57 impressions, 11 reactions, ~19.3% engagement; small reach but the clearest positive response so far |

## Explicit exclusions

- r/writing: do not post. Its current rules prohibit generative-AI advocacy/content.
- r/selfpublish: do not post. Current rules prohibit AI posts and restrict self-promotion.
- r/Writers: deprioritized. It permits resources but is broad and self-promotion-sensitive.
- Repeated cross-posts of the same launch message: stop.
- Upstream `VoltAgent/awesome-agent-skills` PR: defer until real community usage exists.
- Treating stars/forks on the parent fork as the primary KPI: stop; they are structurally poor adoption proxies for one subdirectory skill.

## What can be automated here vs. what requires the user

### Assistant can execute directly

- Update the public GitHub skill files and documentation in `OakcoderX/awesome-agent-skills`.
- Maintain this promotion log and channel-specific copy kit.
- Monitor public search/indexing signals.
- Publish/schedule LinkedIn through Metricool.
- Prepare A/B proof artifacts and channel-specific posts.

### User action currently required

- Third-party GitHub issues/PRs where the installed GitHub App has read-only access.
- Websites requiring GitHub/user sign-in or form submission.
- Reddit, Hacker News, V2EX, 即刻 and 知乎 posting because no authenticated posting connector is available in this runtime.
- Connect X inside Metricool if X automation is wanted.

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

- Tested direct issue creation against `dmgrok/agent-plugins`; third-party write access was unavailable.
- Verified that an independent repository is not necessary for adoption.
- Created `PROMOTION_KIT.md` and this persistent log.
- Updated belief: real usage evidence should precede broad directory submission.

### 2026-08-20 — Creator falsification challenge

- User published the creator-facing falsification challenge in `r/WritingWithAI`.
- Message centered on “break the skill” rather than “please star it.”
- Public search later confirmed the post is indexable.

### 2026-08-21 — LinkedIn methodology test

- Assistant published a separate methodology/falsification post through Metricool at 11:00 Asia/Shanghai.
- By 2026-08-24, Metricool reports **57 impressions and 11 reactions**, with an engagement ratio of about **19.3%**.
- Reach is small, but response density is materially stronger than the visible Reddit signal.

### 2026-08-24 — Weekly strategy review

**Channel comparison**

- **LinkedIn:** strongest positive signal. The audience is small but highly responsive to the methodology framing: AI critique has a hidden failure mode because the model tends to defend its first plausible diagnosis.
- **r/WritingWithAI:** appropriate venue and the post remains publicly indexable, but no substantive external test report, reply, or visible conversion signal has surfaced.
- **Skill directories:** exact-name searches still do not surface the skill. No evidence yet that registry work is the best use of launch effort.
- **GitHub:** repository remains at 0 stars / 0 forks. This is not a clean skill-level metric because the skill lives in a forked monorepo, but there is still no independent adoption signal visible there.

**Message comparison**

- The strongest message is not “Socratic storytelling.”
- The strongest current framing is: **AI story critique often locks onto its first plausible diagnosis; this skill forces the model to attack that diagnosis before telling you what to fix.**
- A second important claim remains unproven: **does the Skill reliably outperform one carefully written prompt?** Public Agent-Skill discussions repeatedly raise this objection, so broad developer promotion before answering it would be premature.

**Strongest current user segment**

Professional or serious AI-assisted story developers — people who already use general-purpose models for story/creative review and care about diagnosis quality, revision control, and repeatable workflows. The current evidence does **not** prove that general fiction writers are the best early adopters; the LinkedIn signal is stronger than the creator-tool-thread signal.

**Tactics to stop or pause**

1. Stop generic cross-posting of the same launch message.
2. Pause directory-submission work until there is at least one independent usage case or failure report.
3. Stop optimizing for GitHub stars on the fork as the core metric.
4. Pause long-form “what the Skill is” documentation; the repository already has enough explanatory material.

**Next week's highest-leverage distribution strategy: proof-led professional distribution**

Produce one compact public case study on **unseen story material** comparing:

- the same model with one strong story-diagnosis prompt;
- the same model with Socratic Story Cartographer.

Judge only four dimensions already central to the product: evidence anchoring, diagnosis update, regression awareness, and stop discipline. Publish the result first to LinkedIn, where the methodology framing already showed response, then use the same evidence — not the same copy — for one Agent-builder community. The goal is not reach; the goal is to answer the most repeated objection with an observable example.

**Product / README improvement executed**

Added a **no-terminal quick start** to the README. A creator can now paste one natural-language installation request directly into an AI harness, while the CLI path remains available for technical users. This addresses the strongest unresolved onboarding hypothesis: terminal-first installation may be suppressing conversion among creators even when the method itself is interesting.

**Next success signal**

The next meaningful milestone is one of:

- an independent user completes a real story diagnosis and reports a concrete result;
- a blind A/B shows a clear Skill advantage on unseen material;
- an external tester produces a falsifying failure case that materially improves v2.2.

Until one of those happens, additional broad-channel posting has low information value.

## Success metrics

Track these instead of raw post count:

1. Confirmed external installs.
2. Number of people who run the skill on their own story.
3. Useful failure reports: wrong diagnosis, weak evidence, loop not updating, over-editing.
4. Blind A/B evidence against one strong prompt.
5. Registry/directory acceptance after real usage exists.
6. Organic mentions or stars only as secondary signals.

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
