# Socratic Reasoning Lab

[中文](README.md) · English

**Experimental 0.1.0: one questioning method, domain-specific standards.**

A derivative of [Socratic Story Cartographer v2.2](https://github.com/OakcoderX/awesome-agent-skills/tree/f5e95e6fc93a92569bf7c1592a3aebf2462d15f8/socratic-story-cartographer). It carries forward competing explanations, falsification, minimum-sufficient intervention, and re-checking, with separate adapters for product, business, research, and visual design.

This is a separate development branch and skill folder in the existing repository, not a new GitHub fork repository. The original story skill remains unchanged. The experimental branch is not yet merged into main.

## Use it for

- Product reviews that distinguish unmet needs, friction, reliability, and measurement problems
- Business plans that separate demand evidence, delivery costs, contribution, and cash timing
- Research arguments that distinguish description, association, and causal claims
- Storyboards and visual designs that need medium-specific attention and continuity checks

The method transfers; the domain criteria do not. Simple questions should still get simple answers. Deferring a judgment when evidence is missing is valid. This is not a substitute for medical, legal, investment, or other qualified professional advice.

## Install

Review [SKILL.md](SKILL.md) and the references before installing.

For environments supporting the Skills CLI:

```bash
DISABLE_TELEMETRY=1 npx skills add https://github.com/OakcoderX/awesome-agent-skills/tree/socratic-reasoning-lab-v0.1/socratic-reasoning-lab
```

The environment variable disables the installer CLI’s anonymous telemetry; the skill itself contains none. See the [CLI documentation](https://www.skills.sh/docs/cli).

Alternatively, copy this complete folder into your agent's supported skill directory. Preserve the relative paths and confirm that `socratic-reasoning-lab` is discoverable.

File structure and instruction behavior were checked in this development pass. End-to-end installation and automatic discovery across clients were not tested.

## First run

Supply the artifact, the decision, and what must be protected:

> Use Socratic Reasoning Lab to review this product proposal. Decide what we should learn before committing development time. Test explanations that imply different actions and recommend the smallest useful next test. Keep uncertainty when evidence is missing. Use at most two passes; do not deploy or contact users.

Other entry points:

> Review whether this research conclusion exceeds its evidence, and suggest defensible wording.

> Check the unit economics in this business plan. Separate known inputs, assumptions, and untested demand.

> Review this shot sequence while preserving its setting, language, and quiet tone. Suggest a minimal change before expanding the story.

## Evidence and limitations

See [evaluation/REPORT.md](evaluation/REPORT.md) for the actual test record, raw responses, and limitations. Synthetic cases and a small model-judged comparison cannot establish broad superiority, professional validity, or user adoption. Do not turn rubric scores into a performance-improvement marketing claim.

No telemetry, automatic upload, paid API dependency, or default external publishing is included. The package contains no private user fiction, screenshots, or business documents.

## Try to break it

Compare the ordinary assistant, the original Story Cartographer, and this variant on the same material and model with equal length limits. Hide version labels before judging. Reports where the skill performs worse are especially useful.

For feedback, include the task, input scope, model, exact version, response, and observed failure. Remove private material before posting public feedback.

[Cases](evaluation/cases.json) · [Distribution and measurement](PROMOTION.md) · [Attribution and license](NOTICE.md)

