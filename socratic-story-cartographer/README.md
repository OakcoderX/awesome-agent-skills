# Socratic Story Cartographer

**English first, Chinese follows.**

A creator-first prompt skill for first-pass narrative diagnosis of fiction.
Its goal is to locate the highest-leverage storytelling breakpoints first, rather than giving instant yes/no verdicts.

面向创作者的一套叙事诊断 Skill，用于小说、剧本、场景与多集大纲的第一轮判断。核心目标是先找出最能改变故事方向的问题点，而不是立刻给“合格/不合格”结论。

## Origin / 来历

This version was inspired by Feifei Li’s observation that Socratic questioning can make uncertainty shrink faster than giving direct answers: by testing assumptions, fiction can be evaluated with lower ambiguity and clearer intervention priorities.

我做这个版本的起点，是李飞飞关于苏格拉底式提问的启发：先问对问题、再做反例验证，往往比先下结论更能快速降低不确定性，找到更真实的修改优先级。

I also used it in my own writing practice, and used it for early passes on novels and screenplays.

我也在自己的小说/剧本工作里使用过，作为初审的判断框架。

## What this version improves / 本版优化点

- Input-aware diagnosis: automatically classifies input as **novel / screenplay / outline / scene / mixed / unclear** before analysis.
- Story-driven output: outputs are written in scene/goals/conflict/consequence language, not engineering terms.
- Structured loops: each diagnosis uses a compact Socratic loop and supports parallel interpretation checks.
- Producer-grade summary: identifies root causes, risks, and modification priorities for planning.

- 增加输入自判定：先判断是**小说/剧本/大纲/片段/混合/不确定**。
- 输出改为叙事语言（目标、阻碍、选择、代价、后果）而非术语化断言。
- 固定结构化循环：每次诊断都围绕一套可复用的苏格拉底链条。
- 提供可执行摘要，便于制片/编剧快速定任务顺序。

## Core principle / 核心原则

- It is a partner, not an oracle.
- Every conclusion is provisional and can be revised.
- The priority is leverage: fix causes first, polish second.

- 这不是裁判，而是陪你一起找问题的搭档。
- 每轮结论都可被反驳并更新。
- 优先修根因，边际修饰在后。

## Scope / 适用范围

- Novel / 小说
- Screenplay / 剧本
- Outline / 大纲
- Scene / 场景片段

Used for first-pass editorial positioning and producer-readable diagnostic summaries.

用于初审定位，不替代完整版改稿。

## What the skill returns / 输出是什么

Per loop (normally 3 rounds total):

- **Current belief / 当前判断**
- **Competing interpretations / 竞争解释**
- **Evidence tests / 证据测试**
- **Leverage point / 根因杠杆**
- **Intervention options / 调整建议（小修 + 备选方向）**
- **Expected impact / 预期影响**
- **Regression risk / 回归风险**
- **Open questions / 未闭合问题**

Final pass includes:

- Story focus after this round / 这轮后故事重点
- What changed / 已确认问题与修正方向
- Remaining risks / 剩余风险
- What to change next / 下一步最值得改的点
- Continue / stop recommendation / 继续或暂停建议

每轮一般输出 1 组以上判断框架，不给技术化评分，不给绝对绿灯。

## Question policy / 提问规则

Ask at most 2 high-value questions only when answers would materially change the chosen intervention.
Do not use interview-style checklists.

最多在答案会改变决策时才提 1–2 个关键问题；不做低价值采访式追问。

## Boundaries / 边界

- Not a guaranteed acceptance detector.
- Not a replacement for legal/rights/compliance checks.
- Not a full rewrite workflow.

- 不做“是否一定播出/通过”式断言。
- 不替代版权、合规、人审判断。
- 不替代完整重写。

## Recommended structure in this repository / 推荐文件结构

- `README.md` (this file)
- `SKILL.md` (execution policy)
- `references/` (optional: mode notes / example traces)

## Suggested skill name / 建议技能名

### English
**Socratic Story Cartographer**

### Identifier
`socratic-story-cartographer`

## Notes / 附注

This directory should contain the updated executable instructions in `SKILL.md`.
