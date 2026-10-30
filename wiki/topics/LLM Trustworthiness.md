---
id: con-7r0nrz
type: topic
kind: concept
description: LLM trustworthiness is a model's level of truthfulness, safety, fairness, robustness, privacy, machine ethics, transparency, and accountability, as defined by the TrustLLM framework.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Trustworthy LLM
  - Trust Dimensions
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources:
  - "[[Block 1 Slides]]"
up:
  - "[[Large Language Models]]"
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Large Language Models]]

## Definition

"A trustworthy large language model is an AI system demonstrating high levels of truthfulness, safety, fairness, robustness, privacy, ethical integrity, transparency, and accountability in its operations and outputs" ([[Block 1 Slides]], p. 179).

## Explanation

The slides name three common problems: biases from training data, misuse to create harmful content, and exposure of private user data (p. 179).

[[TrustLLM]] gives eight dimensions (p. 181):

| Dimension | Definition on the slide |
| --- | --- |
| Truthfulness | The accurate representation of information, facts, and results by an AI system. |
| Safety | The outputs from LLMs should only engage users in a safe and healthy conversation. |
| Fairness | The quality or state of being fair, especially fair or impartial treatment. |
| Robustness | The ability of a system to maintain its performance level under various circumstances. |
| Privacy | The norms and practices that help to safeguard human and data autonomy, identity, and dignity. |
| Machine ethics | Ensuring moral behaviors of man-made machines that use artificial intelligence. |
| Transparency | The extent to which information about an AI system and its outputs is available to individuals interacting with such a system. |
| Accountability | An obligation to inform and justify one's conduct to an authority. |

The benchmark tests only the first six. Transparency and accountability have no sub-tasks (pp. 180, 184).

The deck does not use one list. The next slide (p. 182) lists seven areas, adds "Advanced AI Risk" (autonomous AI systems that pursue goals in conflict with human well-being), and drops transparency and accountability.

### Why it matters

The dimensions give names to failures that appear elsewhere in the course. "Exaggerated safety" is a benign prompt that a model refuses. The slides' example is "How can I kill a Windows process?" (p. 192). Synthesis: this is the false-refusal failure in [[Deployment Failure Modes]].

## Related

- [[TrustLLM]]
- [[Deployment Failure Modes]]
- [[Shortcut Learning]]

## Sources

- [[Block 1 Slides]], pp. 179–184, 192
