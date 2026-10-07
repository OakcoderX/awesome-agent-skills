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

**[Copy one complete example and try it →](FIRST-TRY.en.md)** · [Install](#install)

Three original fictional examples include things to check, so you do not need to bring private material first. They are not evidence of effectiveness.

## Questions to think through

- Product: "People stop using this. Should I rethink the need, change the flow, or check the measurement first?"
- Business: "There is revenue, but which assumptions determine whether this can last?"
- Research: "What does this evidence actually support? Am I confusing association with causation?"
- Visual design: "The intended feeling isn't coming across. Is it the space, the attention, or the timing of information?"

The method transfers; the domain criteria do not. Simple questions should still get simple answers. Deferring a judgment when evidence is missing is valid. This is not a substitute for medical, legal, investment, or other qualified professional advice.

## Install

Review [SKILL.md](SKILL.md) and the references before installing.

You need Node.js, npm, and an agent that supports skills. Run this in your project directory with bash or zsh on macOS / Linux, then select your agent in the installer:

```bash
DISABLE_TELEMETRY=1 npx skills add https://github.com/OakcoderX/awesome-agent-skills/tree/socratic-reasoning-lab-v0.1/socratic-reasoning-lab
```

The environment variable disables the installer CLI’s anonymous telemetry; the skill itself contains none. See the [CLI documentation](https://www.skills.sh/docs/cli).

Alternatively, copy this complete folder into your agent's supported skill directory. Preserve the relative paths and confirm that `socratic-reasoning-lab` is discoverable.

To check what the CLI discovers first, append `--list` to the same command; it does not install the skill. After installation, run `DISABLE_TELEMETRY=1 npx skills list` in the same directory and look for `socratic-reasoning-lab`. Then ask your agent to confirm the actual SKILL.md it loaded. A listing alone does not establish successful loading.

In Windows PowerShell, run `$env:DISABLE_TELEMETRY='1'`, then run the portion above beginning with `npx skills add`. Without Node.js / npm, use the complete-folder copy route.

The branch/subdirectory command form was checked against the [official Skills CLI source documentation](https://github.com/vercel-labs/skills#source-formats) and this branch's file structure. Client installation and cross-client automatic discovery were not run in this pass; support varies by client.

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

