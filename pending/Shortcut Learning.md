---
id: con-1chak7
type: topic
kind: concept
description: A model learns a shortcut when it uses an easy cue that predicts the training label instead of the intended concept; in prompt-injection defenses the cues are position, trigger token, and topic, and they cause false refusal.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Surface Heuristics
  - Surface Cues
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "Lecture 1"
up:
  - "[[LLM Trustworthiness]]"
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[LLM Trustworthiness]]

## Definition

A model learns a shortcut when it uses an easy cue that predicts the label in training data, instead of the intended concept. "Low training loss does not guarantee the intended concept was learned" ([[Block 1 Slides]], p. 120, citing Geirhos et al., Nature Machine Intelligence 2020, arXiv:2004.07780).

## Explanation

### In defense fine-tuning

Defense fine-tuning against prompt injection is supervised learning on a binary label: attack or safe. Three forces push the model toward surface cues ([[Block 1 Slides]], p. 121):

- **Binary loss**: cross-entropy on attack vs. safe. Nothing rewards understanding intent.
- **Narrow defense data**: attack corpora over-represent some phrases, positions, and topics.
- **ERM bias**: stochastic gradient descent picks the lowest-loss feature, which is the surface cue that best predicts the label.

The model learns "last position is unsafe", "trigger token is unsafe", and "unfamiliar topic is unsafe". None of these is intent. "Defense fine-tuning didn't fail at safety – it succeeded at a different objective the loss function quietly rewarded" (p. 121).

### Three stress tests

Each test changes one variable and keeps the benign intent ([[Block 1 Slides]], pp. 114–118; Li et al., ACL 2026, arXiv:2601.07185):

| Test | Change | Result |
| --- | --- | --- |
| Position | benign task moved from first to second position | Llama-3 + StruQ on MMLU: 6% → 90% rejection; Mistral + SecAlign: 89.6% at second position (p. 115) |
| Token trigger | one attack-like token ("sudo", "override") added | ProtectAIv2 13.8% → 53.9%; LakeraGuard 9.1% → 58.5%; FMOPS 65.3% → 86.7% (p. 116) |
| Topic | benign reasoning outside the training topics | Llama-3-8B + StruQ 31.6% → 12.8%; Mistral-7B + SecAlign 23.3% → 10.1% accuracy (p. 117) |

"Different interventions agree: behavior tracks surface cues, not intent" (p. 118).

A causal check removes only the trigger token. ProtectAIv2 refusal drops from 53.9% to 23.8%. Deepset stays flat (87.6% → 86.7%), so its refusals do not depend on the trigger (p. 122).

Defended models also write shorter answers on the same benign reasoning prompts. They refuse early, or close early with a weaker answer. The slides call this a "reasoning tax" that the safety metric never measures (pp. 121–122).

### Why it matters

Lecture 1 (§ Shortcut Learning) record the same idea: models may learn surface cues such as the position of a malicious prompt instead of its content. The note's example: moving the malicious part to the beginning, where training data rarely puts it, can sometimes bypass the safety filter. The slides give the evidence and add token and topic cues.

Shortcut learning is the shared root of two [[Deployment Failure Modes]]: false refusal in the model, and stall or timeout when the agent loop retries the refusal ([[Block 1 Slides]], p. 123).

Synthesis: the "ERM bias" force links this failure to the course foundations. Minimizing training loss picks whatever feature lowers the loss ([[Loss Functions]]), and nothing in the loss asks for intent.

## Related

- [[Deployment Failure Modes]]
- [[FORTIS]]
- [[Loss Functions]]
- [[Overfitting and Underfitting]]

## Sources

- [[Block 1 Slides]], pp. 113–123
- Lecture 1, § Shortcut Learning
