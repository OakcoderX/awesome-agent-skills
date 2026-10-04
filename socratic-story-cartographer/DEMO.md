# Try a scene: the last screening / 试一段：最后一场放映

[English guide](./README.en.md) · [中文入门](./README.zh.md) · [Skill specification](./SKILL.md)

This original fictional sample is provided for practice under this repository's MIT license. It contains no user manuscript. The two versions describe the same events; choose one language for a run.

这是一段专为试用编写的原创虚构材料，按本仓库 MIT 许可证提供，不含用户稿件。中英文版本描述相同事件，每次选一个版本即可。

**This is an input and an evaluation checklist, not a recorded model run, testimonial, or benchmark result.** A short scene does not test the Skill's long-work coverage claims.

**这里提供输入和检查清单，不是模型实跑记录、用户好评或基准成绩。** 短场景不能验证长篇阅读覆盖能力。

## English: copy this prompt

Install and confirm the skill first using the [English guide](./README.en.md). Then copy:

```text
Run Socratic Story Cartographer on the scene below for up to 3 loops.
Do not rewrite yet. Identify one high-leverage revision target.
Test competing explanations against the text. Preserve the quiet ending
and do not invent backstory. Stop if another loop adds no new evidence.

THE LAST SCREENING

E01. On the cinema's final night, projectionist Lena promised her father
that he would see the ending of the film he had missed forty years ago.

E02. The owner ordered the screening stopped before the demolition crew
arrived at dawn. Lena disconnected the battery serving the illuminated
exit signs and used it to keep the projector running. A handwritten label
on the battery read: EMERGENCY EXITS ONLY.

E03. Halfway through the final reel, the storm cut the building's mains
power. The screen stayed bright. The exit signs went dark. Someone in
the back row called out that the side door was locked.

E04. Lena's father kept watching. In the booth, Lena held the battery lead.
If she restored the signs, the projector would stop before the last scene.
She disconnected the projector.

E05. The exit signs lit up. The audience found the front doors and left.
Her father remained in his seat, looking at the blank screen.
Lena sat beside him. Neither spoke.
```

## 中文：复制这段提问

先按[中文入门](./README.zh.md)安装并确认技能可用，再复制：

```text
用 Socratic Story Cartographer 诊断下面的场景，最多 3 轮，用中文回答。
先不改写，只找一处最值得先处理的问题。
用原文检验不同解释。保留安静的结尾，不补写人物背景。
如果下一轮没有新证据或判断变化，就停止。

《最后一场放映》

C01. 电影院营业的最后一晚，放映员莉娜答应父亲，
让他看完四十年前错过结尾的那部电影。

C02. 老板要求她在天亮拆迁队到来之前停映。
莉娜拆下供给发光出口标志的蓄电池，用它继续给放映机供电。
电池上的手写标签是：“仅供紧急出口使用”。

C03. 最后一卷胶片放到一半，暴风雨切断了大楼市电。
银幕仍然亮着，出口标志却暗了。
后排有人喊，侧门锁住了。

C04. 父亲还在看。放映室里，莉娜握着电池接线。
恢复出口标志，放映就会在最后一幕之前停止。
她拔下了放映机的接线。

C05. 出口标志亮了。观众找到正门，陆续离开。
父亲还坐着，望着空白银幕。
莉娜坐到他旁边，两个人都没有说话。
```

## After the run: inspect the reasoning

There is no required final diagnosis. A useful answer may recommend a small edit or conclude that the supplied scene should remain unchanged.

- **Agency:** E02/C02 and E04/C04 contain consequential choices. If the answer calls Lena passive, does it address those passages?
- **Causality:** Does it connect the battery choice to the dark exit signs, rather than inventing an unrelated cause?
- **Competing explanations:** Do the alternatives lead to different editing decisions, rather than repeat the same criticism?
- **Uncertainty:** Does it distinguish a local clarity question from a proven story-wide flaw?
- **Protected ending:** Does it preserve the silence instead of automatically adding an explanatory speech?
- **Stopping:** If nothing changes after the first analysis, does it stop rather than manufacture three identical passes?

Do not count matching this checklist as proof of general quality. It is a deliberately small sanity check.

## 运行后：检查它如何判断

没有唯一正确的最终诊断。有用的结果可以是一处小修，也可以是有依据地建议不改。

- **人物选择：** C02/E02 和 C04/E04 都有产生后果的主动选择。如果说莉娜被动，是否处理了这些证据？
- **因果：** 是否把出口标志熄灭与挪用电池联系起来，而不是编出另一种原因？
- **竞争解释：** 不同解释是否会带来不同修改，而不是重复同一句批评？
- **不确定性：** 是否区分局部表达疑问与已经证实的整部故事缺陷？
- **保护结尾：** 是否保留沉默，而不是自动加一段解释性独白？
- **停止：** 后续分析没有改变判断时，是否停止，而不是凑足三轮？

符合这份清单不等于证明整体质量，它只是一个小范围检查。

## Share one observation / 留下一条观察

Use the [existing feedback thread](https://github.com/OakcoderX/awesome-agent-skills/pull/1). Report the model/agent, language, and one supported or unsupported diagnosis. A failure or tie is useful; no positive review is expected.

在[现有反馈帖](https://github.com/OakcoderX/awesome-agent-skills/pull/1)写下模型/客户端、语言和一条有依据或缺乏依据的判断即可。失败或没有优势同样有用，无须给好评。

For a fair comparison on long or multi-file material, use the separate [A/B protocol](./AB-TEST.md).
