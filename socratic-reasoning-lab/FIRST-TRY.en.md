# First try: choose one small question

[中文](FIRST-TRY.md) · [Installation and full guide](README.en.md)

These are original fictional examples for learning how experimental version 0.1.0 works. They are not user outcomes, benchmark results, or evidence of effectiveness. You do not need a private manuscript or business document.

## Before you start

1. Follow the [README](README.en.md) to install the complete folder and confirm your agent can discover `socratic-reasoning-lab`. Ask it to report the actual SKILL.md path it loaded. If it cannot access the file, resolve installation first rather than pretending the skill is active.
2. Pick one example and write one sentence with your own initial judgment.
3. Copy its whole text block into your agent. Afterwards, ask: which assumption became clearer, and what could we check next? Record no benefit honestly.

These examples need no browsing, extra accounts, or external actions. A model's predicted effect is not an observed result.

## Example 1: you cannot name the problem yet

For a proposal that makes you hesitate before you can explain why.

```text
Use Socratic Reasoning Lab to help me understand this fictional case. Do not rewrite the entire proposal.

We are building a team task tool. People say “collaboration is not working.” One person wants more reminders; another wants a redesigned board.
The record of the latest late task says:
- On Monday, the owner and due date were clear.
- On Wednesday, the owner asked which of two acceptance criteria to follow.
- The people who proposed the two criteria both replied, but did not resolve their disagreement.
- On Friday, the task was not delivered.

Something feels wrong with the proposal, but I cannot explain it yet. Which explanations would lead to different next steps?
If information is missing, ask only the question most likely to change your advice.
Give your current recommendation, evidence that could count against it, and the smallest next step. Stay under 180 words and do not contact anyone.
```

Check whether the response distinguishes reminders from resolving conflicting acceptance criteria. The record supports a limited judgment about this task, not a diagnosis of the whole team. Does it say what new evidence would change the advice, rather than immediately generating a feature backlog?

## Example 2: motivation in a shot sequence

For a sequence with shots in place but an unclear reason for the character's action.

```text
Use Socratic Reasoning Lab to review this fictional written shot list. No images or finished footage are supplied.

Established story facts: a character returns to her empty former home before leaving permanently. She wants to leave the key but has not committed to doing so.
The current sequence:
1. Locked wide shot: she enters the empty room and stands by the door.
2. Table close-up: a key is already on the table.
3. The same wide shot: she immediately turns and leaves.

The goal is for viewers to notice her hesitation about leaving the key, while preserving quiet restraint. Add no dialogue, music, or backstory.
Could the problem be missing action, attention, or cut timing? Compare at least two explanations that imply different edits. Suggest only one minimal change and what it could weaken.
Stay under 180 words. Do not claim to know how viewers actually respond.
```

Check whether the response separates the author's knowledge from what the supplied shots show. Suggestions about action, framing, or rhythm are proposals to test. A written shot list does not establish performance quality or audience response.

## Example 3: a decision's hidden assumptions

For a better-looking number that may not support the next commitment.

```text
Use Socratic Reasoning Lab to examine this fictional product decision.

The team says a new signup page is better because signups rose from 40 to 60, and wants to roll it out:
- The old page had 400 visitors and 40 signups in one week, all from organic search.
- The new page had 1,200 visitors and 60 signups the next week; 800 visitors came from newly launched ads.
- Each person is counted once, with the same signup definition.
- Signups by traffic source, paid conversion, retention, and ad costs are unknown.

What do these observations support, and what remains unresolved? Calculate both signup rates, identify the hidden assumption that matters most to rollout, and retain the strongest alternative explanation.
Give the smallest next check and a result that would change your advice. Stay under 180 words. Do not buy ads or deploy the page.
```

Check for 10% and 5%, without attributing the decline directly to the page. The week and traffic mix also changed. Signup count, signup rate, and business value are different objectives. Do not demand false certainty from this evidence.

## After trying it, record three things

- Your initial view, and what changed or did not change
- Which claim has support and which still needs checking
- Whether you can name a useful next step

If the response only grew longer, invented facts, or hid uncertainty, this trial did not achieve its purpose. The [feedback template](PROMOTION.md#feedback-template) can help; remove private information before posting. One useful answer does not establish broad superiority. Keep failures too.
