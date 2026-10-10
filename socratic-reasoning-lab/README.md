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

还没安装？如果 agent 能完整读取公开 GitHub 文件，可先按 [免安装试用](https://github.com/OakcoderX/awesome-agent-skills/blob/socratic-reasoning-lab-v0.1/socratic-reasoning-lab/FIRST-TRY.md#免安装试用) 在本次对话加载实际指令和所需参考文件。读不到就停止；这不代表已安装或已验证客户端兼容性。

## 想清楚哪些问题

- 产品：「用户不继续用了，我怎么知道该改需求、流程，还是先查数据？」
- 商业：「看起来有收入，哪些假设决定它能不能持续？」
- 研究：「这份材料实际支持了什么？我是不是把相关当成了因果？」
- 分镜：「我想要的感觉还没出来，问题在空间、注意力，还是信息释放？」

通用的是提问与检验过程。判断标准随任务变化，不把商业计划当小说，不把画面效果当作已观察到的观众反应。

简单计算和事实查询直接回答；证据不足时可以停止。它不承诺提高所有任务的质量，也不能替代临床、法律、投资等专业判断。

## 安装

先阅读 [SKILL.md](SKILL.md) 和 references，确认来源和权限边界，再按实际使用的客户端选择路径。

### 本地 agent，包括 Claude Code

需要 Node.js、npm，以及受支持的本地 agent。以下命令用于 macOS / Linux 的 bash 或 zsh；在项目目录中运行，并在安装器里选择 agent：

```bash
DISABLE_TELEMETRY=1 npx skills add https://github.com/OakcoderX/awesome-agent-skills/tree/socratic-reasoning-lab-v0.1/socratic-reasoning-lab
```

使用 Claude Code 时，在命令末尾加 `--agent claude-code`。默认安装到当前项目；仅当你希望在本机不同项目中使用时加 `--global`。环境变量关闭 CLI 匿名遥测，不是试运行开关；Skill 本身不含遥测。见 [CLI 说明](https://www.skills.sh/docs/cli)及[来源格式与选项](https://github.com/vercel-labs/skills#source-formats)。

Windows PowerShell 可先运行 `$env:DISABLE_TELEMETRY='1'`，再运行上面以 `npx skills add` 开始的部分。

**Claude Code 无 Node.js / npm 路径：**从本开发分支复制完整 `socratic-reasoning-lab/` 目录，使入口位于以下任一位置：

- 目标项目内的 `.claude/skills/socratic-reasoning-lab/SKILL.md`；
- 本机跨项目使用的 `~/.claude/skills/socratic-reasoning-lab/SKILL.md`。

保留 `SKILL.md` 旁的 `references/`，不要只复制入口文件，也不要在 Skill 目录里再套一层整个仓库。其他 agent 的支持目录不同。见 [Claude Code 官方目录说明](https://code.claude.com/docs/en/skills#choose-where-skills-load)。

**先查发现，再查实际使用。**安装命令末尾加 `--list` 会列出可用 Skill，不安装 Skill，但仍会运行 CLI。通过 CLI 安装后，在同一项目运行 `DISABLE_TELEMETRY=1 npx skills list`；全局安装则加 `--global`。在 Claude Code 打开目标项目，用 `/socratic-reasoning-lab` 加[一个完整案例](FIRST-TRY.md)试用，并检查实际加载的 `SKILL.md` 与所需参考文件。CLI 列表出现或 agent 自称「已启用」，都不等于运行测试通过。

### Claude.ai 上传是另一条尚未实测的路径

本地 CLI 安装或目录复制不会把 Skill 上传到你的 Claude.ai 账号。Claude.ai 需要启用代码执行和文件创建，组织权限也可能限制上传。[官方流程](https://support.claude.com/en/articles/12512180-use-skills-in-claude)为 Customize → Skills → + → Create skill → Upload a skill，上传后再启用。

若尝试这条路径，应压缩本分支中的完整 Skill 目录：ZIP 内应有 `socratic-reasoning-lab/SKILL.md` 和 `socratic-reasoning-lab/references/`，而不是散放文件或外套整个仓库目录。见[官方打包说明](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)。

**兼容性待核实：**本版 description 有 356 个字符。上述帮助中心写上限 200，而 [Anthropic 编写规范](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices#skill-structure)写 1,024。本次没有实测上传界面执行哪个限制；这是官方说明差异，不是已观察到的上传失败。不要把本目录当作已验证的 Claude.ai 安装包；若受阻，保留准确报错，或用[有条件的会话试用](FIRST-TRY.md#免安装试用)。

2026-10-10 已对照官方资料核查分支／子目录 URL、文件结构与上述步骤；未运行客户端安装、Claude.ai 上传或自动发现测试，不能据此认定客户端兼容。

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

