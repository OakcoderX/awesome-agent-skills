# Socratic Story Cartographer

**A Socratic story-development skill for novels, screenplays, scenes, and series outlines.**  
Instead of jumping to a verdict, it runs a loop of competing diagnoses, falsification, counterfactual tests, minimal intervention, and blind re-check to find the highest-leverage problem first.

## Install

Install the skill with the cross-agent Skills CLI:

```bash
npx skills add https://github.com/OakcoderX/awesome-agent-skills --skill socratic-story-loop
```

Then give your agent the story material and ask, for example:

```text
Run Socratic Story Cartographer on this story for 3 loops. Find the highest-leverage issue first, test competing explanations, and do not rewrite until the diagnosis survives falsification and counterfactual checks.
```

## What it is good at

- **Novel / short fiction:** distinguish author intent from what the text actually produces; protect ambiguity, voice, restraint, and residue while finding the smallest useful revision.
- **Screenplay / episode:** diagnose protagonist choice, scene engine, causality, information release, state change, and where the series engine actually starts.
- **Series outline / treatment:** test story-engine causality, escalation, competing explanations, phase transitions, and whether a structural rewrite is still necessary.
- **Benchmark mode:** after diagnosis, compare a work against a target level without pretending editorial or commercial acceptance can be predicted precisely.

## The loop

`Observe → Compete → Attack → Locate → Intervene → Re-test → Update`

Default: **3 loops**. A requested loop count is a maximum, not an obligation: if a new loop produces no belief update or better intervention, the skill stops early.

Every root-level diagnosis must be anchored to concrete textual evidence. Important changes are checked for regression so that solving one problem does not accidentally destroy a stronger quality already working in the story.

## Quick prompts

**Novel**
```text
Run 3 loops on this short story. Separate author intent from text reality and find the single issue most likely to limit its ceiling. Preserve ambiguity and restraint.
```

**Screenplay**
```text
Run 3 loops on this episode. Find the most causally upstream problem before suggesting edits. Test whether protagonist choices actually create the next problem.
```

**Series outline**
```text
Run 3 loops on this season outline. Identify the story engine, attack your diagnosis with falsification and counterfactual tests, then tell me whether to stop, locally revise, or structurally rebuild.
```

## Version

**2.1** — adds mandatory Evidence Anchors and Loop Delta checks to reduce unsupported diagnosis drift and repetitive loops.

Author: **Solopup.co**

## Documentation

- [English](./README.en.md)
- [中文](./README.zh.md)
- [Runtime specification](./SKILL.md)
