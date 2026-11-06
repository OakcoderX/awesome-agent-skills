# Socratic Story Cartographer — 3-Minute First Test

This is the fastest way to decide whether the skill is useful on your own work.

## No-install option

If your agent can read public GitHub files in full, you can try the instructions in this conversation without Node.js, npm, or installation. Review the linked instructions before using them, then copy the block below. Wait for the agent to confirm its actual reads before sending the [existing sample scene](./DEMO.md).

```text
Use the following public Skill instructions only in this conversation. Do not install anything, run commands, or write files.

First use a reading tool to read this entire SKILL.md:
https://raw.githubusercontent.com/OakcoderX/awesome-agent-skills/4f1a12ae8da3ddbb3dca57240f8d0415be8f9021/socratic-story-cartographer/SKILL.md

If you cannot read the full file, identify the unavailable or incomplete file and stop. Do not reconstruct instructions from the name, search snippets, or memory.

I will send a scene next. For the short sample scene, the main SKILL.md is sufficient. Before analyzing other material, follow its mode-routing rules and fully read the applicable references from the same commit:
- Long or multi-file work:
https://raw.githubusercontent.com/OakcoderX/awesome-agent-skills/4f1a12ae8da3ddbb3dca57240f8d0415be8f9021/socratic-story-cartographer/references/long-work-evidence.md
- Full-season or multi-episode outlines requiring producer review:
https://raw.githubusercontent.com/OakcoderX/awesome-agent-skills/4f1a12ae8da3ddbb3dca57240f8d0415be8f9021/socratic-story-cartographer/references/producer-outline-review.md
When both apply, read long-work-evidence.md first. If any required reference cannot be read in full, identify it and stop before analysis.

Confirm the name and version stated in the file and list the full source URLs actually read. State that this is conversation-only use, not installation or automatic Skill discovery. Wait for my scene before analyzing it. Do not publish anything or contact anyone.
```

Check the reading tool's returned content and sources; opening a link or saying “enabled” is not proof of a complete read. This path has not been validated across clients and does not establish writing-quality gains. If your agent cannot read the required files, stop or use the installation option below.

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