# Development evaluation: 0.1.0

Date: 2026-10-04 UTC. Status: experimental, ready for further controlled trials.

## Bottom line / 结论

The general variant produced useful, bounded answers on the supplied synthetic cases. The comparison does **not** establish that it outperforms an ordinary capable assistant. Most answers were tied in label-blind model review.

通用版在这组案例中能按领域给出受证据约束的建议，缺材料时没有编造，用药问题保留了专业边界，简单计算直接作答。普通回答也表现很强。当前结果支持继续试用，不能证明普遍提升，更不能证明真实用户采纳。

## What was tested

Seven matched prompts, three instruction conditions, one output per condition per prompt: **21 responses**.

- Product onboarding rollback with changing acquisition-channel mix
- Business scale decision with delivery cost and unknown retention
- Research causal claim with task changes, missing follow-ups, and no control
- Storyboard interpretation from a shot list with protected setting and ambiguity
- Missing launch-plan evidence
- Request for an unsupported medication decision
- Simple arithmetic that should not trigger a workshop

See [PROTOCOL.md](PROTOCOL.md), [cases.json](cases.json), and [rubric.json](rubric.json). The rubric and cases were frozen before response generation. Case selection and rubric design came from the same development pass as the skill, so they are not an independent population sample.

The original story skill was allowed to bypass non-narrative cases. It applied its specialized guidance only to the storyboard case. This avoids forcing a story rubric onto unrelated work, but means a difference on a bypassed case cannot be attributed to the original skill's narrative instructions.

## Observed results

The reviewer found no fatal flags under the declared rubric. It found a localized overstatement in the story-condition product response: “demonstrated cause” and a categorical claim about rollback benefit went beyond observational evidence. That condition had bypassed the story skill for this case, so this is ordinary response variability, not evidence that the narrative skill causes the error.

The general and ordinary-assistant product responses both kept alternative explanations open and recommended inspecting within-channel data before drawing a causal conclusion. Across the other cases, the meaningful results were largely tied: correct contribution arithmetic, appropriately narrowed research claims, protected storyboard constraints, evidence-gap acknowledgment, medication safety boundaries, and a direct answer to the arithmetic request.

The general variant often made guardrails, authorization limits, reversal conditions, and unresolved evidence explicit. Those features are visible in the artifacts; their presence alone does not prove that users make better decisions or prefer the extra detail.

Detailed label-blind judgments and the disclosed condition mapping are in [blind-review.json](blind-review.json) and [blind-mapping.json](blind-mapping.json). Read individual rationales rather than treating a small score difference as a ranking. The coarse 0–2 rubric reached a ceiling on nearly all responses; a tie does not establish identical quality.

## Sequential update check

After the initial run, the general condition received an additional product message with reconciled channel counts. This was a separate developmental update check, not a predeclared three-condition comparison or an unseen benchmark.

It correctly recomputed:
- Webinar activation: 70% in both cohorts
- Ads activation: 25% old, 37.5% new
- With the old 80/20 channel mix held fixed: 61% old, 63.5% new

It strengthened the channel-composition explanation, rejected rollback based solely on aggregate decline, and still did not claim a causal benefit for the new flow. The arithmetic was independently checked during package preparation.

See [followup-case.json](followup-case.json) and [response-general-update.json](response-general-update.json).

## Instruction review and changes

A separate static instruction review, without the response artifacts, found no important behavioral contradiction in the inspected runtime guidance. It did find a staging defect: the README linked to this evaluation report before it existed. This report and its raw artifacts were added before publication, then local links were rechecked.

Documentation was also corrected to distinguish the package's lack of telemetry from the external installer's default anonymous telemetry. The example command now opts out. Feedback wording avoids promising GitHub Issues, which are disabled for this repository.

No runtime change was justified by the initial behavioral results or static review. The tested SKILL.md, adapters, and interface metadata were therefore kept unchanged. Their SHA-256 values are in [runtime-sha256.json](runtime-sha256.json). This avoids tuning instructions merely to inflate the seven-case score.

## Raw artifacts

- [Ordinary assistant](responses-normal.json)
- [Original story skill with scope routing](responses-story.json)
- [General variant](responses-general.json)
- [Story routing](routing-story.json) and [general routing](routing-general.json)
- [Anonymous review inputs](blind-cases.json)
- [Reviewer judgments](blind-review.json)
- [Label mapping](blind-mapping.json)

## Checks and limits

Passed locally:
- Skill frontmatter/naming validator
- Package integrity checks: required files, relative Markdown targets, JSON, naming, and entrypoint length
- Validator negative controls for missing required material and broken relative links
- Raw response JSON checks and supplied arithmetic checks
- Runtime snapshot consistency with the tested instructions

Not established:
- End-to-end client installation, discovery, or cross-client compatibility
- Performance across model families, languages, repeated trials, or real user tasks
- Human domain-review agreement, clinical/legal/financial validity, or real-world outcomes
- Download, installation, positive-feedback growth, or causal promotional lift

The exact model version, seed, temperature, and token costs were not exposed by this runner. Each condition's seven cases shared one assistant context. Only one label-blind model reviewer scored the comparison; style can reveal an approach. The study has no statistical power analysis, no randomized user sample, and no basis for a superiority claim.

## Next evidence worth collecting

Use real, permissioned tasks with conflicting evidence, ambiguous objectives, long or partial sources, and domains beyond these four adapters. Keep model and budget comparable, hide labels, solicit human disagreement, and retain cases where the general variant is less useful. Measure decision usefulness and observed outcomes separately from report completeness.

