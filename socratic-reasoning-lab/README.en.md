# Socratic Reasoning Lab

[中文](README.md) · English

**Experimental 0.1.0: think through the problem you haven't quite put into words.**

When a proposal feels wrong but you cannot yet explain why, Socratic Reasoning Lab offers a structure for thinking with an AI: make implicit goals and assumptions visible, compare explanations, identify evidence that would change your view, and choose a small next step. It is designed for people who need to do the thinking and make the decision.

This is an intended use, still being tested. The first comparison of 21 model responses was largely tied. We have not established better human insight, better decisions, or more accurate AI answers.

A derivative of [Socratic Story Cartographer v2.2](https://github.com/OakcoderX/awesome-agent-skills/tree/f5e95e6fc93a92569bf7c1592a3aebf2462d15f8/socratic-story-cartographer). It carries forward competing explanations, falsification, minimum-sufficient intervention, and re-checking, with separate adapters for product, business, research, and visual design.

This is a separate development branch and skill folder in the existing repository, not a new GitHub fork repository. The original story skill remains unchanged. The experimental branch is not yet merged into main.

## Start with a concrete question

- **You cannot name the problem yet**: does a late task need more reminders, or agreement on acceptance criteria?
- **A shot sequence lacks motivation**: what in the shots actually conveys the character's hesitation?
- **A decision hides an assumption**: do more signups justify rolling out the new page?

**[Copy one complete example and try it →](https://github.com/OakcoderX/awesome-agent-skills/blob/socratic-reasoning-lab-v0.1/socratic-reasoning-lab/FIRST-TRY.en.md)** · [Install](#install)

Three original fictional examples include things to check, so you do not need to bring private material first. They are not evidence of effectiveness.

Not installed yet? If your agent can read complete public GitHub files, [try the session-only route](https://github.com/OakcoderX/awesome-agent-skills/blob/socratic-reasoning-lab-v0.1/socratic-reasoning-lab/FIRST-TRY.en.md#try-without-installing) to load the actual instructions and required references in this conversation. Stop if they cannot be read. This is not an installation or proof of client compatibility.

## Questions to think through

- Product: "People stop using this. Should I rethink the need, change the flow, or check the measurement first?"
- Business: "There is revenue, but which assumptions determine whether this can last?"
- Research: "What does this evidence actually support? Am I confusing association with causation?"
- Visual design: "The intended feeling isn't coming across. Is it the space, the attention, or the timing of information?"

The method transfers; the domain criteria do not. Simple questions should still get simple answers. Deferring a judgment when evidence is missing is valid. This is not a substitute for medical, legal, investment, or other qualified professional advice.

## Install

Review [SKILL.md](SKILL.md) and the references before installing. Choose the route for the client you actually use.

### Local agents, including Claude Code

You need Node.js, npm, and a supported local agent. Run this in your project directory with bash or zsh on macOS / Linux, then select your agent in the installer:

```bash
DISABLE_TELEMETRY=1 npx skills add https://github.com/OakcoderX/awesome-agent-skills/tree/socratic-reasoning-lab-v0.1/socratic-reasoning-lab
```

For Claude Code, append `--agent claude-code`. Installation is project-scoped by default; add `--global` only if you want personal installation across projects. The environment variable disables the CLI's anonymous telemetry; it is not a dry-run switch. The skill itself contains no telemetry. See the [CLI documentation](https://www.skills.sh/docs/cli) and [source formats and options](https://github.com/vercel-labs/skills#source-formats).

In Windows PowerShell, run `$env:DISABLE_TELEMETRY='1'`, then run the portion above beginning with `npx skills add`.

**Claude Code without Node.js / npm:** copy the complete `socratic-reasoning-lab/` folder from this development branch so its entrypoint is either:

- `.claude/skills/socratic-reasoning-lab/SKILL.md` in the intended project; or
- `~/.claude/skills/socratic-reasoning-lab/SKILL.md` for personal use across local projects.

Keep `references/` beside `SKILL.md`; do not copy only the entrypoint or nest the whole repository inside the skill directory. Other agents have their own supported locations. See [Claude Code skill locations](https://code.claude.com/docs/en/skills#choose-where-skills-load).

**Check discovery, then actual use.** Adding `--list` to the install command lists available skills without installing the skill, but still runs the CLI. After CLI installation, run `DISABLE_TELEMETRY=1 npx skills list` in the same project, or add `--global` for a global installation. In Claude Code, open the intended project and invoke `/socratic-reasoning-lab` with [one complete example](FIRST-TRY.en.md). Check which actual `SKILL.md` and required references were loaded. A CLI listing or the agent saying “enabled” is not a runtime test result.

### Claude.ai upload is a separate, unverified route

A local CLI install or folder copy does not upload the skill to your Claude.ai account. Claude.ai requires code execution/file creation to be enabled, and organizational permissions can limit uploads. Its [official upload flow](https://support.claude.com/en/articles/12512180-use-skills-in-claude) is Customize → Skills → + → Create skill → Upload a skill, followed by enabling it.

If attempting that route, ZIP the complete skill folder from this branch: the archive must contain `socratic-reasoning-lab/SKILL.md` and `socratic-reasoning-lab/references/`, not loose files or the enclosing repository. See [packaging guidance](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

**Compatibility caveat:** this release's description is 356 characters. The Help Center above lists a 200-character limit, while [Anthropic's authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#skill-structure) allows 1,024. We have not tested which limit the upload interface enforces. This is an unresolved documentation difference, not an observed upload failure. Do not treat the folder as a verified Claude.ai package; if blocked, retain the exact error or use the [conditional session-only trial](FIRST-TRY.en.md#try-without-installing).

The branch/subdirectory URL, file layout, and these instructions were checked against official documentation on 2026-10-10. Client installation, Claude.ai upload, and automatic discovery were not run; the checks do not establish client compatibility.

## First run

Supply material you are entitled to use, the decision, and what must be protected. You can begin with an unresolved concern:

> Something feels wrong with this proposal, but I can't yet explain it. Use Socratic Reasoning Lab to surface implicit assumptions and the most important issue to think through. Ask one decisive question only if my answer would change your advice. Separate facts from guesses and say what evidence would change our view.

For a defined task:

> Use Socratic Reasoning Lab to review this product proposal. Decide what we should learn before committing development time. Test explanations that imply different actions and recommend the smallest useful next test. Keep uncertainty when evidence is missing. Use at most two passes; do not deploy or contact users.

Other entry points:

> Review whether this research conclusion exceeds its evidence, and suggest defensible wording.

> Check the unit economics in this business plan. Separate known inputs, assumptions, and untested demand.

> Review this shot sequence while preserving its setting, language, and quiet tone. Suggest a minimal change before expanding the story.

## What to notice

Can you now explain the decision, the crucial assumption, an overlooked alternative, and what would change your mind? Write a short before-and-after account in your own words. Record when you learned nothing new or received only a longer report, too.

## Evidence and limitations

See [evaluation/REPORT.md](evaluation/REPORT.md) for the actual test record, raw responses, and limitations. Synthetic cases and a small model-judged comparison cannot establish broad superiority, professional validity, or user adoption. Do not turn rubric scores into a performance-improvement marketing claim.

No telemetry, automatic upload, paid API dependency, or default external publishing is included. The package contains no private user fiction, screenshots, or business documents.

## Try to break it

Compare the ordinary assistant, the original Story Cartographer, and this variant on the same material and model with equal length limits. Hide version labels before judging. Reports where the skill performs worse are especially useful.

For feedback, include the task, input scope, model, exact version, response, your initial understanding, and any previously unnoticed issue you can now test. No benefit, new misconceptions, and failures matter too. Keep perceived insight, independently checked accuracy, and real decision outcomes separate. Remove private material before posting public feedback.

[Cases](evaluation/cases.json) · [Distribution and measurement](PROMOTION.md) · [Attribution and license](NOTICE.md)

