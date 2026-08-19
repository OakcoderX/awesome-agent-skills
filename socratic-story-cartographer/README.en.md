# Socratic Story Cartographer

## Overview

A creator-oriented narrative diagnostic skill that uses Socratic questioning to support first-pass reading of fiction.
It is designed for novels, screenplays, scenes, and multi-episode outlines.

Version: 2.1
Author: Solopup.co

The goal is not to give a final verdict, but to identify the highest-leverage story issues and the next correction that can be tried first.

## Origin

The concept was inspired by Li Feifei’s point that Socratic questioning, when used early, can reduce uncertainty faster than immediate assertions.

I also used this approach in my own writing workflow and applied it to first-pass reviews of novels and scripts.

## What this version improves

- Automatic input type classification: Novel / Screenplay / Outline / Scene / Mixed / Unclear.
- Story-facing output language: goals, obstacles, choices, stakes, causality, and consequences.
- Fixed loop for fast diagnosis and re-checking.
- Clear handoff summary for producers and writers: what changed, what remains, what to fix next.

## Loop structure (default 3 loops)

Each loop follows:

1. Observe
2. Generate 2–3 competing interpretations
3. Test the strongest interpretation with:
   - one falsification test
   - one counterfactual test
4. Choose the leverage point (root-cause first)
5. Suggest interventions
   - minimal option
   - optional alternative
6. Predict consequences
7. Ask at most 1–2 key questions when needed
8. Blind re-check and update belief

## Output shape

Each loop outputs:

- Current belief
- Competing diagnosis
- Test design
- Leverage point
- Intervention suggestion(s)
- Expected consequence
- Regression check
- Open uncertainty
- Optional author questions (if needed)

Final pass includes:

- What the story is currently centered on
- What was changed and why
- Remaining risks
- Top 3 follow-up fixes (priority order)
- Continue / stop recommendation

## Scope and constraints

- No guarantee of acceptance labels (no “greenlight/reject” verdicts).
- No replacement for human legal, rights, or production decisions.
- No full rewrite mode.
- No invention of missing facts, motivations, or plot events.

## Suggested skill name

**Socratic Story Cartographer**  
Repository name: `socratic-story-cartographer`

Use this skill when you want:

- fast first-pass reading
- precise producer triage
- smallest useful intervention suggestions