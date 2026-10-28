# Socratic Story Cartographer — 3-Minute First Test

This is the fastest way to decide whether the skill is useful on your own work.

## 1. Install

```bash
npx skills add https://github.com/OakcoderX/awesome-agent-skills/tree/main/socratic-story-cartographer
```

The Skills CLI supports many AI harnesses, including Codex, Claude Code, Cursor, OpenCode, and others.

## 2. Choose material you can use

Use a piece of writing you know well and have permission to share with your chosen model, or copy the [original bilingual practice scene](./DEMO.md) without sharing a private manuscript. The practice scene is an input and checklist, not a recorded model test or evidence of improved writing.

Do **not** tell the agent what you already think is wrong.

## 3. Run this prompt

```text
Run Socratic Story Cartographer for up to 3 loops.
Do not rewrite yet.
Find the single highest-leverage issue, anchor the diagnosis to concrete evidence in the text, attack your first diagnosis with falsification and a counterfactual test, and stop early if another loop no longer changes the belief.
```

## 4. Judge only three things

After the run, ask yourself:

1. Did it find a problem I would actually prioritize?
2. Did it show enough textual evidence that I can disagree with it intelligently?
3. Did the second/third loop genuinely update the diagnosis instead of merely generating more notes?

If the answer to all three is **yes**, the skill is doing what it was designed to do.

## Try to break it

A useful test is not whether the output sounds smart. Try to catch one of these failures on a story you know well:

- it confidently diagnoses something the text does not support;
- the second or third loop merely restates the first diagnosis;
- its proposed fix solves one problem by damaging a stronger quality already working in the story.

If you find one, keep the smallest example that demonstrates the failure. Those counterexamples are more useful for improving the skill than generic praise.

## What makes this different

The goal is not to produce a longer critique. The loop is designed to make the agent **challenge its own first explanation before recommending a fix**, preserve qualities that already work, and stop when more analysis stops adding information.

See [BENCHMARK.md](./BENCHMARK.md) for the structured comparison that shaped v2.1.