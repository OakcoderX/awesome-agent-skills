# Socratic Reasoning Lab

[English](README.en.md) · 中文

**实验版 0.1.0：用共同的提问方法，配合不同领域的判断标准。**

从 [Socratic Story Cartographer v2.2](https://github.com/OakcoderX/awesome-agent-skills/tree/f5e95e6fc93a92569bf7c1592a3aebf2462d15f8/socratic-story-cartographer) 衍生而来。保留「竞争解释 → 找反证 → 最小干预 → 重新检查」的方法，新增产品、商业、研究论证、分镜／视觉设计四个适配器。

这是同一仓库中的独立开发分支与独立 Skill 目录，并非新的 GitHub fork 仓库。原小说 Skill 保持不变。实验版通过分支提供，尚未合并进 main。

## 适合做什么

- 产品：区分需求问题、交互阻力、可靠性问题与数据偏差
- 商业：检查需求证据、获客、交付成本、贡献利润与现金时点
- 研究：区分描述、相关与因果，检查比较对象和证据边界
- 分镜：检查空间、注意力、信息释放和节奏，保护原有风格

通用的是提问与检验过程。判断标准随任务变化，不把商业计划当小说，不把画面效果当作已观察到的观众反应。

简单计算和事实查询直接回答；证据不足时可以停止。它不承诺提高所有任务的质量，也不能替代临床、法律、投资等专业判断。

## 安装

先阅读 [SKILL.md](SKILL.md) 和 references，确认来源和权限边界，再选择安装方式。

支持 Skills CLI 的环境：

```bash
DISABLE_TELEMETRY=1 npx skills add https://github.com/OakcoderX/awesome-agent-skills/tree/socratic-reasoning-lab-v0.1/socratic-reasoning-lab
```

上面的环境变量关闭安装 CLI 的匿名遥测；Skill 本身不包含遥测。[CLI 说明](https://www.skills.sh/docs/cli)。

或者把本目录完整复制到所用 agent 支持的 Skill 目录。保留 SKILL.md 和 references 的相对位置。在 agent 中确认能发现名称 `socratic-reasoning-lab`。

本次只验证了文件结构与指令行为；没有验证每种客户端的自动发现或实际安装流程。不同客户端的 Skill 支持可能不同。

## 第一次使用

提供真实材料、要做的决定，以及不能损坏的部分：

> 用 Socratic Reasoning Lab 审查这份产品方案。目标是判断下一步该不该投入开发。先找最重要的不确定性，比较会导向不同动作的解释，再建议最小测试。没有证据就保留不确定性。最多两轮，不要部署或联系用户。

也可以直接要求：

> 审查下面研究结论是否超出数据能支持的范围，给出更准确的表述。

> 检查这份商业计划的单位经济模型。把已知数据、假设和还没验证的需求分开。

> 看这组分镜是否能表达我想要的感觉。保留原有国家、语言和安静感，先给最小修改，不要扩写剧情。

## 输出应当帮助你决定什么

通常会给出：当前建议、关键证据、最强的不同解释、能改变建议的观察、最小下一步，以及仍不能决定的事。不会为了凑轮数制造新结论。

## 测试与限制

请看 [evaluation/REPORT.md](evaluation/REPORT.md) 的实际结果、原始输出和局限。样例是合成任务；小样本模型评审不能证明普遍提升、专业有效性或用户采纳。不要把对照测试的分数当作产品宣传中的提升百分比。

没有遥测、自动上传、付费 API 依赖或默认对外发布。文件中没有用户的小说原文、截图或私人业务资料。

## 参与试用

带一份你有权分享的材料，比较默认 assistant、原 Story Cartographer 与本变体。用同一输入、同一模型和同样的长度限制，先隐藏版本再评判。尤其欢迎「它比普通回答更差」的例子。

反馈至少保留：任务、输入范围、模型、所用版本、输出，以及实际失败点。公开分享反馈前删除私人内容。

[测试材料](evaluation/cases.json) · [推广与测量说明](PROMOTION.md) · [来源与许可](NOTICE.md)

