# Socratic Story Cartographer

**Version:** 2.1  
**Author:** Solopup.co

## About this skill

Socratic Story Cartographer is a story-diagnosis skill for creators and production teams.

It supports:

- Novels
- Screenplays
- Multi-episode outlines
- Scenes and story concepts

Its goal is to help you find what matters first, avoid endless edits, and get to the next useful revision faster.

## Discoverability (for humans & AI)

### Search keywords

**Main keywords:** Socratic storytelling, story diagnosis, screenplay evaluation, script triage, outline review, novel critique, producer-ready script, root-cause fix, 3-loop review, blind re-check, minimal intervention.

### AI-search invocation phrases

- `Socratic Story Loop, diagnose this outline for producer readiness.`
- `Run 3 loops on this screenplay and propose the first high-leverage fix.`
- `Use Socratic Story Loop for a benchmark check on this novel draft.`
- `苏格拉底式 剧本 诊断`
- `多集大纲 初审 根因 修复`

## Origin

The concept is inspired by Li Feifei’s view that good prompting is not about giving answers quickly, but about asking the right questions early.

I built this skill from that idea to support first-pass diagnostics of fiction and scripts. It works as a small review partner: keep asking until the highest-leverage uncertainty is narrowed, then make the smallest useful intervention.

## What this version improves

- Input type classification: Novel / Screenplay / Outline / Scene / Character / Mixed / Unclear.
- Clear separation of **author intent** and **text reality**.
- Evidence-first diagnosis with test/反例/反事实 checks.
- A stronger loop structure for blind re-check and belief update.
- A compact result format that points to the most important next fix.

## Core flow

A complete pass follows the default `Observe -> Compete -> Attack -> Locate -> Intervene -> Re-test -> Update` cycle.

The default is 3 loops, but can be adjusted by user request.

## How to use

### 1) First-pass / triage

Paste the text and tell me the goal.

Example prompt:

- `Run 3 loops and diagnose this outline for producer readiness.`
- `I need a quick first-pass on this novel. Do 3 loops and tell me the highest-leverage uncertainty and next fix.`

### 2) Scene/episode check

Paste one scene or chapter and ask for the leverage point.

Example prompt:

- `Run 3 loops on this scene and tell me the minimal next fix.`
- `Run 3 loops on this pilot scene only; judge whether the exit state has changed and what should be fixed first.`

### 3) Risk-only check

If you only need a stop/no-stop judgment, ask for benchmark mode questions.

Example prompt:

- `Do this in benchmark mode and compare it to [target].`

### 4) What I should include in one ask

To get good results, include:

- The text itself (one outline / one scene / one episode / one chapter).
- Your current goal:
  - `初审` / `给制片人看`
  - `找根因`
  - `确认最小化修改方向`
  - `评估是否值得继续改写`
- Allowed scope:
  - `先不改文`（只要问题定位）
  - `可做最小修改`（只做最小干预）
  - `可结构性重做`（允许较大改法）

### 5) When to ask fewer questions

The skill only asks for extra information when answers materially change the decision path.  

For example:

- You did not specify whether this is `小说` 还是 `剧本` and the difference affects judging criteria.
- A missing world/genre rule changes causality.
- A protection rule (`不改这个底色/不要失去悬念`) is unclear.

If the text is already enough, it will not ask for extra clarification.

## Before / after example

Use this prompt template to keep the process stable:

1. `Object: <novel|screenplay|outline|scene>`  
2. `Goal: <first-pass|benchmark|minimum-edit|full triage>`  
3. `Loops: 3`  
4. `Scope: <text>  （paste here）`  
5. `Restrictions: <if any>`

Then paste your text.

### Typical output shape

You will receive:

- Current belief
- Evidence-backed diagnosis
- Competing hypotheses
- Testing logic (falsification + counterfactual)
- Leverage point
- Minimal fix + fallback option
- Consequence prediction and regression risk
- Open uncertainty
- Decision recommendation

It stays in story language (goal, obstacle, choice, cost, consequence), not abstract grading labels.

## Output language

The output is practical, avoiding abstract grading labels, and focuses on:

- what the story currently does,
- what changed in our judgment,
- what likely has the highest downstream value,
- what to fix next.

## Documentation

- [README.en.md (English)](./README.en.md)
- [README.zh.md (中文)](./README.zh.md)
- [SKILL.md (runtime spec)](./SKILL.md)

Use the English or Chinese version according to your reading preference.