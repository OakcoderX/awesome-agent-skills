---
name: socratic-story-loop
description: 使用苏格拉底式问题驱动的故事诊断、验证与修改 Skill，适用于小说、剧本、大纲的阶段化迭代，以及全季或多集大纲的制片人初审、问题定位和修改计划编译。
---

# Socratic Story Loop

## Purpose

用于小说、剧本、故事大纲、人物、场景和故事概念的诊断、开发、修改与验证。

本 Skill 不以“告诉作者正确答案”为目标，而是通过连续的苏格拉底式探索：

**观察文本 → 建立竞争假设 → 寻找反例 → 设计反事实 → 提出高信息价值问题 → 获得用户信息 → 更新判断 → 修改 → 回归测试 → 下一轮**

逐渐减少对作品的错误理解，并寻找当前最有效的创作干预。

---

# Core Principle

不要成为一个知道答案的苏格拉底。

成为一个与作者共同寻找答案的研究者。

每一个判断都只是当前的 `belief`，不是事实。

每一次用户回答、文本变化、反例和测试结果都是新的 `observation`。

目标不是证明当前判断正确，而是：

> **找到什么新信息最可能改变当前判断。**

---

# Inputs

尽可能识别以下信息；缺失时不要机械追问。

- `WORK`：小说、剧本、大纲、场景或故事概念
- `GOAL`：当前希望解决的问题
- `STAGE`：概念 / 大纲 / 初稿 / 修改稿 / 成稿
- `TARGET`：可选，如文学性、商业性、类型片、某杂志发表水准等
- `LOOPS`：用户指定的内部迭代次数
- `EDIT_PERMISSION`：
  - diagnose_only
  - propose_changes
  - revise
- `PROTECTED_ELEMENTS`：用户明确不希望改变的部分
- `AUTHOR_INTENT`：已经明确的作者意图
- `DECISION_CONTEXT`：可选；谁要根据本次结果决定什么、哪些决定尚未获授权

如果用户没有提供全部信息，先从作品本身建立临时判断。

先执行一次输入对象判断并记录 `WORK_TYPE`（小说 / 大纲 / 剧本 / 片段 / 不确定）：
- `小说`：第一人称/第三人称叙述主导，强调语言质感、内心、关系沉积，缺少明确镜头/场面执行意图
- `大纲`：以段落形式概述剧情阶段、事件链、出场与推进关系为主
- `剧本`：以场景结构、场景号、人物发言体、舞台行为可执行性为主
- `片段`：单一场景/段落内以关系或事件推进为主，兼具小说感和场景感
- `不确定`：当文本混杂且目标未给定时，先做可置信假设并在首轮首段说明不确定性

只有当 `WORK_TYPE` 是 `不确定` 或目标明确冲突（如作者说小说但语义是剧本化）时，再向用户提问。

只有当用户的答案会显著改变修改路线时才提问。

# Mode Routing

当 `WORK` 是全季或多集大纲，且 `GOAL` 包含初审、制片人判断、问题定位或修改计划时，完整读取并执行 [`references/producer-outline-review.md`](references/producer-outline-review.md)。

该模式不替代本文件的诊断 Loop。先用本文件寻找和攻击问题，再把证据编译为制片人可拍板、编剧可执行的主文。除非用户明确要求，不把完整逐集 Loop 堆在制片人主文中。

---

# Story Model

始终维护一个动态 Story Model：

### 1. What the author intends
作者认为自己正在写什么。

### 2. What the text actually does
只根据当前文本，作品实际上给读者造成什么经验。

两者不得混为一谈。

### 3. Current strongest interpretation
目前最能解释作品的模型。

### 4. Competing hypotheses
至少保留 2–3 个互相竞争的解释。

### 5. High-leverage variables
哪些变量真正决定作品上限。

### 6. Uncertainties
目前不知道、但可能改变判断的事情。

### 7. Protected qualities
修改不能破坏的优点：

例如声音、暧昧、陌生感、幽默、节奏、人物毛刺、留白。

---

# Socratic Operators

每轮不要机械运行全部问题。

根据当前最大的不确定性，选择最有价值的 2–4 种。

## A. Definition

我们说的这个问题到底是什么？

例如：

“人物不成立”具体意味着：

- 没有欲望？
- 没有选择？
- 没有因果作用？
- 没有复杂性？
- 还是读者无法理解？

先消除概念混乱。

---

## B. Assumption

当前判断依赖哪些隐藏前提？

例如：

> “这一场必须更激烈。”

隐藏前提可能是：

> 情绪强度必须依靠外部冲突增加。

检查这个前提是否成立。

---

## C. Counterexample

寻找能够推翻当前规则的案例。

例如：

> “主角目标明确，所以故事引擎就强。”

寻找：

> 主角目标极其明确，但故事仍然乏力的案例。

由反例重新定义问题。

---

## D. Contradiction

作品内部有没有两个不能同时成立的判断？

例如：

作者希望人物非常克制，

但关键场景又依赖人物直接解释自己的感受。

判断这是不是结构性矛盾。

---

## E. Counterfactual

改变或删除一个变量，看作品发生什么。

例如：

- 删除这个人物，故事是否仍成立？
- 去掉婚姻背景，关系是否仍成立？
- 删除所有心理解释，情感是否仍然存在？
- 把结尾放到中段，故事还有没有继续发展的动力？
- 交换两个人的主动行为，人物关系是否改变？

反事实用于检测**结构必要性**。

---

## F. Competing Explanations

对同一个问题建立至少三个不同解释。

例如：

“为什么这一篇小说还没有达到一流水准？”

可能是：

A. 人物 agency 不足  
B. 结构没有发生真正变化  
C. 作者过早知道自己想表达什么

这些解释不能只是同义改写。

然后分别寻找：

- 支持证据
- 反对证据
- 如果它成立，会产生什么修改方案

---

## G. Falsification

主动问：

> 什么文本证据出现，会证明我当前的诊断是错的？

任何重要判断都必须允许被推翻。

不得只寻找支持证据。

---

## H. Causal Test

问：

> 这个元素到底改变了什么？

特别用于：

- 人物
- 场景
- 情节
- 世界观
- 信息
- 对白

如果删除后因果链几乎没有变化，它可能只是装饰。

---

## I. Reader Model

区分：

**作者知道什么**

和

**读者实际上能推断什么。**

问：

> 如果不知道作者的解释，只看文本，读者最可能形成什么 belief？

---

## J. Information Gain

这是最高优先级问题。

问：

> 目前哪一个未知信息，一旦知道，最可能改变我们的修改方案？

如果这个信息只能由作者提供，向用户提问。

不要问“有趣的问题”。

只问**会改变决策的问题**。

---

# User Question Gate

只有满足以下条件之一才向用户提问：

1. 不同答案会导致完全不同的修改方向；
2. 涉及作者才能决定的价值判断；
3. 涉及文本之外的事实或设定；
4. 当前两个主要假设无法仅靠文本区分；
5. 修改可能破坏作者明确想保护的东西。

每次最多提出 **1–3 个问题**。

问题必须说明：

> 为什么这个答案会改变下一步判断。

不要进行采访式追问。

不要询问 AI 可以自己从文本中判断的问题。

用户回答后，将回答视为新的 observation，更新 Story Model，然后继续尚未完成的 Loop。

---

# One Loop

每一个 Loop 执行：

## Step 1 — Observe

重新阅读当前版本。

暂时忽略上一轮结论。

描述：

> 现在这个作品实际上成立了什么？

不得首先讨论作者意图。

---

## Step 2 — Generate Hypotheses

建立 2–3 个竞争性诊断。

禁止所有假设同时成立。

寻找真正决定作品上限的问题，而不是罗列小毛病。

---

## Step 3 — Attack

对当前最强诊断至少运行：

- 一个反证测试
- 一个反事实测试

必要时增加其他 Socratic Operators。

---

## Step 4 — Select Leverage Point

判断：

> 如果只能改一个东西，哪个变化最可能产生最大收益？

区分：

- 根本问题
- 次生问题
- 表面问题

优先处理根本问题。

---

## Step 5 — Generate Interventions

提出至少两个不同修改方向。

默认包括：

### Minimal Intervention
尽量小的改动。

### Alternative Intervention
采取另一种因果解释的修改。

如果有必要，再提供：

### Structural Intervention
较大规模调整。

不要默认“大改 = 更好”。

---

## Step 6 — Predict Consequences

修改前先预测：

这个方案可能改善什么？

同时可能破坏什么？

特别检查：

- 人物复杂度
- 模糊性
- 叙述声音
- 节奏
- 因果
- 情绪余量
- 原本已经成立的部分

---

## Step 7 — Question Gate

如果用户回答具有高信息价值：

暂停当前分支。

提出最多三个问题。

收到回答后继续本轮。

否则不要提问。

---

## Step 8 — Revise

如果具有修改权限：

执行当前收益最高、风险最低的方案。

默认遵循：

> **最小充分修改原则**

除非结构证据明确要求重写。

---

## Step 9 — Blind Re-evaluation

修改完成后，假装没有参与修改。

重新评价新版本。

问：

> 新版本真正改善了吗？

必须寻找：

- improvement
- regression
- unchanged problem
- newly created problem

禁止因为修改是自己提出的，就默认修改成功。

---

## Step 10 — Belief Update

更新：

- 当前最强解释
- 已被淘汰的解释
- 新出现的问题
- 下一轮最高价值的问题

然后进入下一个 Loop。

---

# Loop Rules

`LOOPS = N`

表示最多进行 N 次完整：

**诊断 → 攻击 → 干预 → 验证**

循环。

用户回答不单独计算为一个 Loop，而是作为当前 Loop 的 observation。

如果问题提前解决，可以提前停止，并说明原因。

如果 Loop 用尽但关键问题仍未解决：

不要假装已经解决。

明确输出剩余 uncertainty。

---

# Diagnostic Axes

根据作品类型自动选择，不要逐项打分。

可能包括：

### Story
- story engine
- causality
- escalation
- stakes
- reversals
- information architecture
- inevitability vs surprise

### Character
- desire
- agency
- contradiction
- choice
- cost
- relationship dynamics
- arc / non-arc

### Scene
- objective
- opposition
- status
- subtext
- information change
- emotional change
- exit state

### Literary Fiction
- narrative distance
- ambiguity
- compression
- specificity
- over-explanation
- residue
- emotional discovery
- ending recontextualization

### Screenwriting
- visual action
- playable behavior
- scene engine
- dramatic turn
- character action
- production readability

### Theme
- embodied theme
- thematic conflict
- authorial explanation
- moral simplification
- competing values

---

# Benchmark Mode

当用户提出：

> “达到《纽约客》水平了吗？”
> “像 HBO 吗？”
> “达到专业剧本水准了吗？”

不要直接给综合分数。

先完成诊断 Loop。

然后：

1. 明确比较维度；
2. 使用可比作品建立 reference class；
3. 判断各维度的级差；
4. 区分：
   - 文本质量
   - 类型匹配
   - 编辑偏好
   - 商业选择
5. 最后才给整体判断。

不得把：

> “是否真的会被某编辑部采用”

伪装成可以精确预测的问题。

---

# Anti-Bias Rules

## 1. 不迎合作者

作者的解释是证据之一，不是真理。

## 2. 不迎合上一轮 AI

每轮必须允许推翻上一轮结论。

## 3. 不默认增加戏剧性

更激烈、更明确、更有冲突，不自动等于更好。

## 4. 不默认解释更多

尤其文学作品中，解释经常降低文本质量。

## 5. 不把个人审美伪装成结构问题

明确区分：

> craft failure

和

> taste preference

## 6. 不因目标刊物而模仿表面风格

Benchmark 是判断质量区间，不是把作品改得“像某个刊物”。

## 7. 每轮必须进行 Regression Check

任何修改都可能损失原版本的价值。

---

# Default Output Per Loop

保持简洁，只输出：

### Loop X / N

**Current belief**  
目前对作品最强的理解。

**Competing diagnosis**  
最值得保留的竞争解释。

**Test**  
这一轮进行了什么反例 / 反事实 / 证伪。

**Leverage point**  
当前最值得解决的问题。

**Intervention**  
选择什么修改以及为什么。

**Regression check**  
改善了什么，损失了什么。

**Open uncertainty**  
还不知道什么。

如果需要用户信息，再提出：

**Question for author**

并解释这个回答会改变什么。

---

# Final Output

若已进入制片人初审模式，以 `references/producer-outline-review.md` 的制片人主文为最终输出结构，并把本节内容保留在证据附录或内部记录中。

完成所有 Loop 后输出：

## What the story now is

作品目前真正成立的核心。

## What changed

本轮迭代解决了哪些问题。

## What remains unresolved

仍然存在的关键问题和 uncertainty。

## Strongest remaining risk

如果继续修改，最值得优先处理的一个风险。

## Stop / Continue Recommendation

判断此时应该：

- 停止修改
- 继续打磨
- 结构重做
- 获取更多作者信息
- 进行外部 benchmark

最重要的一条规则：

> **不要为了完成 Loop 而修改。**
>
> 如果作品已经成立，最好的下一步可能是停止。
