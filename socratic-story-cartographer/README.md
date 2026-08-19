# Socratic Story Cartographer

## Overview / 概览

**English first. 中文同样可用。**

A creator-first prompt skill for diagnosing and improving fiction using Socratic questioning loops.
It is designed for initial evaluation of novels, scripts, scenes, and multi-episode outlines. The focus is
on finding the next highest-value intervention, not producing instant verdicts.

一个面向创作的故事诊断 Skill，用苏格拉底式提问来做“第一轮判断 + 递进修正”。用于小说、剧本、单场景和大纲的结构问题定位。核心目标不是立刻下定义，而是找到下一步最有价值的修改点。

## Origin / 来历

This skill is inspired by remarks by **Feifei Li** that Socrates is one of the earliest “prompting experts”:
asking better questions can guide uncertainty reduction faster than giving assertions.

它受李飞飞最近采访中“苏格拉底式提问先于答案”启发：在故事判断里，先把问题问精、找假设、做反证，更容易推进到真实可执行的修改，而不是先“拍脑袋定论”。

I built and used it across my own fiction workflows, and applied it to first-pass reading of novels and scripts.

我本人也在自己的小说工作中使用过，并把它用在小说+剧本的初审场景里。

## What problem this solves / 解决什么问题

- It helps teams separate **what the author intends** from **what the text actually delivers**.
- It reduces blind editing by testing competing interpretations instead of accepting one hypothesis.
- It helps script/outline teams prioritize fixes that change the story engine, not just surface polish.

- 区分“作者想表达什么”与“读者从文本读到什么”。
- 避免拍脑袋修改，通过“竞争假设 + 反例 + 反事实”找优先修复点。
- 在剧本/大纲里优先修复能改变引擎、因果和观看决策点的节点，而不是堆积小修。

## Core principle / 核心原则

Not an oracle. The skill behaves like a partner:

- 每一轮结论都是当前信念（belief），不是终局真理。
- 它允许被反驳（falsification first）。
- 它更重视“下一条能改变判断的证据”而非“更高级的语句评价”。

## Supported inputs / 适用输入

It supports:

- Novel / 小说
- Screenplay / 剧本
- Outline / 大纲
- Scene / 片段

The input is first classified into `WORK_TYPE` automatically (小说/剧本/大纲/片段/不确定).

先自动判断文本类型，记录为 `WORK_TYPE`：
- 小说
- 剧本
- 大纲
- 片段
- 不确定

## Loop model / 核心循环

Each loop follows:

1. **Observe**
2. **Generate hypotheses**（2-3个）
3. **Attack** strongest hypothesis with:
   - one falsification test
   - one counterfactual test
4. **Select leverage point**（根因优先）
5. **Generate interventions** (minimal + alternative, optional structural)
6. **Predict consequences**
7. **Question gate** (ask only when decision changes materially)
8. **Revise** (if allowed)
9. **Blind re-evaluation**
10. **Belief update**

Each cycle is compact and evidence-led; if uncertainty is already low, it can stop early.

每轮按上述顺序执行：观察→竞争判断→反证/反事实→定位杠杆点→给方案→预测后果→必要提问→（有权限则）改动→盲测→更新信念。若问题已解决可提前停。

## Output contract / 输出约定

Per loop, it returns:

- **Current belief**
- **Competing diagnosis**
- **Test**
- **Leverage point**
- **Intervention**
- **Regression check**
- **Open uncertainty**
- Optional **Question for author** (only if high information gain)

Final summary:

- What the story now is
- What changed
- What remains unresolved
- Strongest remaining risk
- Stop / Continue recommendation

每轮输出固定结构，最终给出：作品当前成立的故事是什么、已经改了什么、还未解决什么、最重要风险、继续还是停止。

## Key operators / 常用问法

- Definition（定义问题）
- Assumption（拆前提）
- Counterexample（反例）
- Contradiction（矛盾）
- Counterfactual（反事实）
- Competing explanations（竞争解释）
- Falsification（可证伪）
- Causal test（因果测试）
- Reader model（读者能推断到什么）
- Information gain（最关键的问题是什么）

## Question policy / 提问规则

It only asks the author when the answer can materially change the edit direction, and at most 1–3 questions.
No interview-style or low-value questions.

只在“答案会影响判断路径”时才提问；每次最多 1–3 个问题；不做流水账式采访。

## Scope / 边界

- Not for giving guaranteed acceptance labels (e.g., platform greenlight).
- Not a direct proof of quality certification.
- Benchmarking against high-level references is handled as a separate mode, not casual scoring.

- 不做“是否一定绿灯”等绝对预测。
- 不替代人工决策与合规核验。
- 高级对比（如向某类头部作品标杆）在明确请求下进入专门流程。

## Why this is useful / 为什么对你有用

In creator-facing workflows it gives:

- a faster way to localize what is truly broken
- a cleaner distinction between root-cause and surface polish
- an auditable paper trail of why a change was chosen
- a lower-friction first-pass for narrative development and producer-readable diagnostics

在创作流程里，它能更快定位真正的叙事问题，区分“根因/表层”修改，形成可追溯修改依据，降低初审阶段反复试错。

## Recommended file structure / 建议发布结构

If you are publishing as a GitHub skill package, keep it small and readable:

- `README.md` (this file)
- `SKILL.md` (execution rules, if you want plugin-like behavior)
- `references/` (optional mode notes)

GitHub 发布可先从这个 README 起步，后续再补 `SKILL.md`（规则层）与 `references`（模式说明）。

## Suggested skill name / 建议的skill名字

**Socratic Story Cartographer**

建议技术名：`socratic-story-cartographer`

## Non-goals / 非目标

- Not a magic judge.
- Not replacing long-form rewriting.
- Not a substitute for human legal, rights, or production constraints.

- 不做“万能裁判”。
- 不代替完整重写。
- 不替代版权/制作方审计。