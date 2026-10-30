---
id: con-pdyevw
type: topic
kind: concept
description: The CSCI 566 argument that benchmark accuracy, broad usefulness, and reliable deployment are different claims, and that the unit of evaluation moved from one label to repeated, least-privilege agent behavior.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - What Does Solved Mean
  - Units of evaluation
  - Benchmark vs. deployment claims
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources:
  - "[[Block 1 Slides]]"
up:
  - "[[Deep Learning]]"
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Deep Learning]]

## Definition

"Benchmark accuracy, broad usefulness, and reliable deployment are different claims" ([[Block 1 Slides]], p. 74). The slides name three units of evaluation, synthesized from Bommasani et al. (arXiv 2021) and Yao et al. (ICLR 2025):

| Unit | Claim |
| --- | --- |
| Fixed test set (benchmark) | accuracy on held-out examples |
| Broad interface (interface) | useful behavior across many requests |
| Repeated behavior (system) | correct outcomes across repeated runs |

## Explanation

The slides then show how the target moved ([[Block 1 Slides]], pp. 75–78):

1. **Supervised prediction is strong, but scoped.** "A strong result inherits the scope of its task, distribution, and metric." [[AlexNet]]'s 15.3% top-5 error (vs. 26.2% second place) holds only inside all three (p. 75).
2. **Self-supervision changes reuse, not the meaning of "solved".** Broad unlabeled text trains one pretrained model that serves QA, translation, coding, and classification. BERT reported state of the art on 11 NLP tasks (p. 76).
3. **Sequential decisions: one success is not reliability.** "Repeatability is a property of a sequence of runs, not one successful trajectory." On τ-bench, pass^1 is below 50%, and retail pass^8 is below 25%. "The evaluation unit changes from one outcome to repeatability" (p. 77). The slide adds: "RL is a learning setting; an agent is a runtime system. They can overlap."
4. **The target moved** from predict one label, to generate one response, to change the environment through tools, to repeat reliably under policy and least privilege. "Each expansion of the evaluation unit creates a new failure condition." "The unit we evaluate is no longer a model alone" (p. 78).

Synthesis: a model that passes a benchmark can still fail as a deployed system; [[Deployment Failure Modes]] covers those failures. The last step, least privilege, is what [[FORTIS]] measures.

## Related

- [[Machine Learning Task Types]]: the task, experience, and performance table by system level
- [[Model Evaluation]]: test error for a single model
- [[Deployment Failure Modes]]
- [[FORTIS]]
- [[AlexNet]]
- [[Evolution of Machine Learning]]

## Sources

- [[Block 1 Slides]], pp. 74–78
