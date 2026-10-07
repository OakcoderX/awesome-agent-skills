# Socratic Reasoning Lab

[English](README.en.md) · 中文

**实验版 0.1.0：和 AI 一起，把自己还没说清的问题想清楚。**

当你觉得一个方案「哪里不对」，却暂时说不出原因时，Socratic Reasoning Lab 提供一套对话支架：把隐含的目标和假设摊开，比较不同解释，找出真正会改变判断的证据，再决定一个小而具体的下一步。它面向需要亲自思考和作决定的人。

这是正在验证的用途与设计目标。首轮 21 份模型回答的对照结果大体持平；我们还没有证明它能提高人的洞察力、决策质量或 AI 回答准确率。

从 [Socratic Story Cartographer v2.2](https://github.com/OakcoderX/awesome-agent-skills/tree/f5e95e6fc93a92569bf7c1592a3aebf2462d15f8/socratic-story-cartographer) 衍生而来。保留「竞争解释 → 找反证 → 最小干预 → 重新检查」的方法，新增产品、商业、研究论证、分镜／视觉设计四个适配器。

这是同一仓库中的独立开发分支与独立 Skill 目录，并非新的 GitHub fork 仓库。原小说 Skill 保持不变。实验版通过分支提供，尚未合并进 main。

## 先选一个具体问题

- **说不清卡在哪里**：一次延期究竟需要更多提醒，还是先解决验收分歧？
- **分镜动作没有动机**：想表达人物犹豫，镜头里实际给到了什么？
- **决定藏着假设**：注册人数变多，就足够支持全面上线吗？

**[复制一个完整小例子开始试用 →](https://github.com/OakcoderX/awesome-agent-skills/blob/socratic-reasoning-lab-v0.1/socratic-reasoning-lab/FIRST-TRY.md)** · [安装](#安装)

三个原创虚构例子都附了可检查的要点，不需要你先准备私人材料；它们不是效果证明。

## 想清楚哪些问题

- 产品：「用户不继续用了，我怎么知道该改需求、流程，还是先查数据？」
- 商业：「看起来有收入，哪些假设决定它能不能持续？」
- 研究：「这份材料实际支持了什么？我是不是把相关当成了因果？」
- 分镜：「我想要的感觉还没出来，问题在空间、注意力，还是信息释放？」

通用的是提问与检验过程。判断标准随任务变化，不把商业计划当小说，不把画面效果当作已观察到的观众反应。

简单计算和事实查询直接回答；证据不足时可以停止。它不承诺提高所有任务的质量，也不能替代临床、法律、投资等专业判断。

## 安装

先阅读 [SKILL.md](SKILL.md) 和 references，确认来源和权限边界，再选择安装方式。

需要 Node.js、npm，以及支持 Skills 的 agent。以下命令用于 macOS / Linux 的 bash 或 zsh；在项目目录中运行，并在安装器里选择要使用的 agent：

```bash
DISABLE_TELEMETRY=1 npx skills add https://github.com/OakcoderX/awesome-agent-skills/tree/socratic-reasoning-lab-v0.1/socratic-reasoning-lab
```

上面的环境变量关闭安装 CLI 的匿名遥测；Skill 本身不包含遥测。[CLI 说明](https://www.skills.sh/docs/cli)。

或者把本目录完整复制到所用 agent 支持的 Skill 目录。保留 SKILL.md 和 references 的相对位置。在 agent 中确认能发现名称 `socratic-reasoning-lab`。

如果只想先检查 CLI 能发现什么，可在同一命令末尾加 `--list`；这不会安装 Skill。安装后在同一目录运行 `DISABLE_TELEMETRY=1 npx skills list`，确认有 `socratic-reasoning-lab`，再让 agent 确认加载了实际的 SKILL.md。列表出现不等于 agent 已成功加载。

Windows PowerShell 可先运行 `$env:DISABLE_TELEMETRY='1'`，再运行上面以 `npx skills add` 开始的部分。没有 Node.js / npm 时，使用完整目录复制方式。

命令的分支与子目录形式已对照 [Skills CLI 官方源码说明](https://github.com/vercel-labs/skills#source-formats)，并与本分支的文件结构核对。本次未运行客户端安装或跨客户端自动发现测试；不同客户端的支持可能不同。

## 第一次使用

提供你有权使用的材料、要做的决定，以及不能损坏的部分。也可以从一个还没想清楚的困惑开始：

> 我觉得这份方案有问题，但还说不清。用 Socratic Reasoning Lab 帮我找出隐含假设和最值得想清楚的一处。只在答案会改变建议时问我一个关键问题；区分事实和猜测，并告诉我什么证据会让我们改主意。

有明确任务时：

> 用 Socratic Reasoning Lab 审查这份产品方案。目标是判断下一步该不该投入开发。先找最重要的不确定性，比较会导向不同动作的解释，再建议最小测试。没有证据就保留不确定性。最多两轮，不要部署或联系用户。

也可以直接要求：

> 审查下面研究结论是否超出数据能支持的范围，给出更准确的表述。

> 检查这份商业计划的单位经济模型。把已知数据、假设和还没验证的需求分开。

> 看这组分镜是否能表达我想要的感觉。保留原有国家、语言和安静感，先给最小修改，不要扩写剧情。

## 输出应当帮助你决定什么

你可以用它检查：我现在到底在决定什么、哪一个假设最关键、我忽略了哪一种解释，以及什么观察会让我改变看法。通常会给出当前建议、关键证据、最强的不同解释、最小下一步和仍不能决定的事。不会为了凑轮数制造新结论。

阅读后，试着用自己的话写下「我原先怎么想，现在多看见了什么」。如果没有新理解，或者只是多了一份更长的报告，也值得记录。

## 测试与限制

请看 [evaluation/REPORT.md](evaluation/REPORT.md) 的实际结果、原始输出和局限。样例是合成任务；小样本模型评审不能证明普遍提升、专业有效性或用户采纳。不要把对照测试的分数当作产品宣传中的提升百分比。

没有遥测、自动上传、付费 API 依赖或默认对外发布。文件中没有用户的小说原文、截图或私人业务资料。

## 参与试用

带一份你有权分享的材料，比较默认 assistant、原 Story Cartographer 与本变体。用同一输入、同一模型和同样的长度限制，先隐藏版本再评判。尤其欢迎「它比普通回答更差」的例子。

反馈至少保留：任务、输入范围、模型、所用版本、输出、你原先的理解，以及是否发现了此前未察觉且可检验的问题。没有帮助、引入误解和实际失败点同样重要。主观觉得有启发、独立核实的正确性与真实决策结果应分开记录。公开分享反馈前删除私人内容。

[测试材料](evaluation/cases.json) · [推广与测量说明](PROMOTION.md) · [来源与许可](NOTICE.md)

