---
id: con-zgmcce
type: topic
kind: concept
description: Measured power-law relations between loss and model size, data, and compute (Kaplan et al. 2020), and the Chinchilla result that at fixed compute, parameters and training data must be chosen together.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Neural scaling laws
  - Kaplan scaling laws
  - Chinchilla scaling
  - Compute-optimal scaling
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "Lecture 1"
  - "CSCI 566 Syllabus"
up:
  - "[[Deep Learning]]"
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Deep Learning]]

## Definition

Model size $N$ (parameters), data $D$ (tokens), and compute $C$ have measurable relationships with loss. The power-law trends "span >7 orders of magnitude" ([[Block 1 Slides]], p. 72, citing Kaplan et al., "Scaling Laws for Neural Language Models", arXiv:2001.08361, 2020). The slide title calls this the point where "Scaling Becomes a Measurable Design Rule".

## Explanation

### Allocation at fixed compute

Scale "Is an Allocation Problem, Not a Parameter Contest". At fixed compute, parameters and training data must be configured together ([[Block 1 Slides]], p. 73, citing Hoffmann et al., "Training Compute-Optimal Large Language Models", NeurIPS 2022, arXiv:2203.15556):

| Model | Parameters | Training data | MMLU |
| --- | --- | --- | --- |
| Gopher | 280B | less | — |
| Chinchilla | 70B | 4× more | 67.5%, more than 7 points above Gopher |

Both models used the same training compute.

### Link to the lecture notes

The slides answer the open entry in Lecture 1, § Background Topics: "2020 - model, data, compute >7 orders (power law)". It is the Kaplan et al. result ([[Block 1 Slides]], p. 41). The ">7 points" figure for Chinchilla is a different claim from a different paper.

Synthesis: after [[AlexNet]] crossed the data and GPU threshold ([[Deep Learning]]), scaling laws turned further gains into a design question: how to split compute between model size and data.

The CSCI 566 Syllabus covers scaling laws in week 12.

## Related

- [[Deep Learning]]
- [[Evolution of Machine Learning]]
- [[Autoregressive Language Modeling]]

## Sources

- [[Block 1 Slides]], pp. 41, 72–73
- Lecture 1, § Background Topics
- CSCI 566 Syllabus, schedule
