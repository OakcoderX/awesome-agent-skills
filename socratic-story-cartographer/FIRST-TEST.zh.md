# Socratic Story Cartographer：第一次试用

[English](./FIRST-TEST.md) · [中文说明](./README.zh.md) · [完整中英示例](./DEMO.md)

先用一小段材料判断这个工作方式是否适合你。安装和生成耗时取决于网络、客户端和模型，不承诺固定用时。

## 免安装试用

如果你的智能体能完整读取公开 GitHub 文件，可先在本次对话中使用指令，无需 Node.js、npm 或安装。先阅读链接中的指令，认可后复制下面的启动文本。等智能体确认实际读取情况，再发送[已有示例场景](./DEMO.md)。

```text
请只在本次对话中使用以下公开 Skill 的指令。不安装、不运行命令、不写文件。

先用读取工具完整读取 SKILL.md：
https://raw.githubusercontent.com/OakcoderX/awesome-agent-skills/4f1a12ae8da3ddbb3dca57240f8d0415be8f9021/socratic-story-cartographer/SKILL.md

如果无法实际读取全文，请指出不可用或不完整的文件并停止；不要凭名称、搜索摘要或记忆补出指令。

我接下来会发一个场景。仓库中的短场景示例只需主 SKILL.md。分析其他材料前，按其中的模式路由完整读取适用参考文件，全部使用同一提交：
- 长篇或多文件材料：
https://raw.githubusercontent.com/OakcoderX/awesome-agent-skills/4f1a12ae8da3ddbb3dca57240f8d0415be8f9021/socratic-story-cartographer/references/long-work-evidence.md
- 需要制片审阅的全季或多集大纲：
https://raw.githubusercontent.com/OakcoderX/awesome-agent-skills/4f1a12ae8da3ddbb3dca57240f8d0415be8f9021/socratic-story-cartographer/references/producer-outline-review.md
两种条件都适用时，先读 long-work-evidence.md。任何必需参考文件无法完整读取，都请指出文件并停止，不开始分析。

确认文件中的名称和版本，列出实际读取过的完整来源链接。说明这只是本次对话使用，没有安装，也不代表客户端已自动发现 Skill。先等我发场景再分析。不发布内容，不联系他人。
```

请检查读取工具返回的内容与来源；仅打开链接或说“已启用”不能证明完整读取。这条路径尚未在各客户端验证，也不证明能改善写作效果。若智能体读不到必需文件，请停止，或使用下面的安装方式。

## 1. 安装并确认

在支持 Agent Skills 的环境里运行：

```bash
npx skills add https://github.com/OakcoderX/awesome-agent-skills/tree/main/socratic-story-cartographer
```

不使用终端时，可把下面这段交给有技能安装能力的智能体：

```text
请从以下目录安装 Socratic Story Cartographer：
https://github.com/OakcoderX/awesome-agent-skills/tree/main/socratic-story-cartographer

按当前环境支持的方法安装，并确认能够发现这个技能。
如果没有安装权限或当前环境不支持，请明确说明，给出适用于这里的步骤，
不要把“已读到网页”说成“已安装成功”。
```

命令格式见 [Skills CLI 官方说明](https://github.com/vercel-labs/skills#install-a-skill)。本次文档核对不等于在每个客户端做过安装测试。

## 2. 选一段可使用的文本

最好用你熟悉且有权交给当前模型处理的一个场景。暂时不要告诉模型你认为什么地方有问题。也可以使用仓库中的[原创虚构示例](./DEMO.md)，不用上传私人稿件。

## 3. 复制提问

```text
用 Socratic Story Cartographer 诊断以下材料，最多 3 轮，用中文回答。
先不改写。先找一处最值得优先处理的问题，用具体原文作依据。
提出一个会导向不同改法的竞争解释，寻找能推翻第一判断的证据，
并用一个反事实检验因果关系。
最后给出最小可试修改及它可能破坏的已有优点。
如果继续分析不再改变判断或修改方案，就停止。

材料：
[粘贴场景]
```

## 4. 用结果检查它

1. 它有没有把自己的推测说成原文事实？
2. 它有没有认真处理反证，还是每轮只换句话重复？
3. 建议是否可执行，是否保护了你原本想保留的东西？

满意、不满意、与普通提示词没有区别，都可以记录。一次体验不能证明普遍效果。

## 5. 留下一条有用的反馈

[现有公开反馈帖](https://github.com/OakcoderX/awesome-agent-skills/pull/1)接受具体成功或失败案例。第一次可以只发：

```text
模型 / 客户端：
使用语言：
材料范围：场景 / 一章 / 一集 / 全季大纲
最有用或最不可信的一条判断：
原文依据是否充分：
下一步是否真的知道怎么改：
```

不要公开未获许可的稿件、私人内容或个人信息。需要严格比较时，再使用 [A/B 协议](./AB-TEST.md)，保持模型、材料和设置一致。
