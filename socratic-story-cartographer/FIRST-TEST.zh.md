# Socratic Story Cartographer：第一次试用

[English](./FIRST-TEST.md) · [中文说明](./README.zh.md) · [完整中英示例](./DEMO.md)

先用一小段材料判断这个工作方式是否适合你。安装和生成耗时取决于网络、客户端和模型，不承诺固定用时。

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
