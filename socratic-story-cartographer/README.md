# Socratic Story Cartographer

## English Documentation

### Overview

A creator-oriented narrative diagnostic skill that uses Socratic questioning to support first-pass reading of fiction.
It is designed for novels, screenplays, scenes, and multi-episode outlines.

The goal is not to give a final verdict, but to identify the highest-leverage story issues and the next correction that can be tried first.

### Origin

The concept was inspired by Li Feifei’s point that Socratic questioning, when used early, can reduce uncertainty faster than immediate assertions.

I also used this approach in my own writing workflow and applied it to first-pass reviews of novels and scripts.

### What this version improves

- Automatic input type classification: Novel / Screenplay / Outline / Scene / Mixed / Unclear.
- Story-facing output language: goals, obstacles, choices, stakes, causality, and consequences.
- Fixed loop for fast diagnosis and re-checking.
- Clear handoff summary for producers and writers: what changed, what remains, what to fix next.

### Loop structure (default 3 loops)

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

### Output shape

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

### Scope and constraints

- No guarantee of acceptance labels (no “greenlight/reject” verdicts).
- No replacement for human legal, rights, or production decisions.
- No full rewrite mode.
- No invention of missing facts, motivations, or plot events.

### Suggested skill name

**Socratic Story Cartographer**  
Repository name: `socratic-story-cartographer`

---

## 中文文档

### 概览

一个面向创作者的叙事诊断 skill，用苏格拉底式提问支持小说、剧本、片段和多集大纲的初审。

目标不是直接下“通过/不通过”结论，而是先找出最有杠杆作用的问题点，并定位最值得先改的方向。

### 来历

该版本受李飞飞“提问先于答案”这一思路启发：先通过有约束的提问降低不确定性，再做判断，通常比直接给结论更稳。

我在自己的创作流程中也在用，并用于小说与剧本的初步评估。

### 本版强化

- 输入自动分类：小说 / 剧本 / 大纲 / 场景 / 混合 / 不确定。
- 输出使用叙事语言：人物目标、阻碍、选择、代价、因果、后果。
- 固定化诊断循环，支持快速迭代复测。
- 产出可用于制片会的结论摘要：已确认问题、未闭合问题、下一步优先修复项。

### 诊断循环（默认3轮）

每轮执行：

1. 观察
2. 提出2–3个竞争解释
3. 用两个测试验证当前最强解释：
   - 一次可证伪测试
   - 一次反事实测试
4. 选一个根因杠杆
5. 给修正方案
   - 小修优先方案
   - 可选替代方向
6. 预估后果
7. 仅在关键时提出1–2个高价值问题
8. 盲测后更新判断

### 输出内容

每轮固定返回：

- 当前判断
- 竞争解释
- 测试设计
- 根因杠杆点
- 方案建议
- 预期影响
- 回归风险
- 未闭合疑点
- 可选作者提问（仅在有实质影响时）

最终补充：

- 这轮故事的核心结论
- 做了什么变化、为什么这样做
- 剩余风险
- 下一步Top3修复优先级
- 继续/暂停建议

### 边界

- 不输出“绿灯/不绿灯”这类绝对判定。
- 不替代版权、法律、合规、制作流程决策。
- 不做完整重写流程。
- 不臆造未写明的人物信息、动机和剧情细节。

### 技能名

**Socratic Story Cartographer**
仓库名：`socratic-story-cartographer`