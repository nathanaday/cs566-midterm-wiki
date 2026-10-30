---
description: The CSCI 566 framing of ML as learning a function f(X) that approximates an unknown exact function f*(X) mapping inputs to outputs, with deep networks as a high-capacity choice of f.
aliases:
  - ML as function approximation
  - One function f(X)
  - Universal approximation
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
---

> [!concept] Concept
> 2 sources · refreshed 2026-09-28 · #machine-learning/cs566-deeplearning

## Definition

The lecture treats many ML tasks as one function $f(X) \to Y$ ([[Block 1 Slides]], p. 209):

| Task | $X$ | $Y$ |
| --- | --- | --- |
| Object detection | image | object label and bounding box |
| Semantic segmentation | image | pixel-level label |
| Image captioning | image | description (a deep CNN, then a language-generating RNN) |
| Machine translation | text in language A | text in language B |

Sources: [[Block 1 Slides]], pp. 210–218. The slides then ask: "How is this related to intelligence?", "What does it mean to have one function for all intelligence?", and "How do we learn this function?" (pp. 220–221).

An exact function $f^*$ may map $X$ to $Y$. The goal is not to find $f^*$. The goal is a learned $f(X)$ that approximates $f^*(X)$: "f does NOT have to be exactly f*" (p. 223).

## Explanation

The course is about two questions (p. 224):

1. How do we learn this function (using ML and DL)?
2. How do we formulate a problem into this form?

"For f(X) to approximate any f*(X), f is better to be highly capable." The slides propose deep learning because it is non-linear (high capacity), hierarchical, and learned end to end (pp. 226–227). They cite the universal approximation theorem: "Given certain conditions, a deep neural net can approximate any f(x)" (p. 228). The slides do not state the conditions.

[[Block 3 Slides]] repeats this framing (pp. 3–10). It shows object detection as a photo with labeled boxes (person, sheep, cow) and as one cat image with the output "cat (0.92)" (pp. 5–6).

### One function, many behaviors

[[Block 3 Slides]] adds a 2026 view: one parameter set can serve chat, math, instruction following, many languages, and image-plus-text input. "The task description now rides inside X, along with context and data. The model still computes f(x; W)." The slide names the limit: "That is conditional reuse, not a universal solver. Strong on one instruction, weak on another" (p. 4).

### The learning chain

A bridge slide gives the chain: examples $(x, y)$ → model $f(x; W)$ → prediction $\hat{y}$ → loss $L(\hat{y}, y)$ → update $W$. It maps these steps to function approximation, supervised learning, linear models, and optimization ([[Block 1 Slides]], p. 207).

Synthesis: [[Linear Classification]] is the simplest $f$. [[Loss Functions]] measure how far $f$ is from the target. [[Optimization]] adjusts $f$. [[Model Evaluation]] checks $f$ on data it did not see.

## Related

- [[Parameterization of a Hypothesis Class]]: how the parameters enter the function decides which functions are reachable
- [[Deep Learning]]
- [[Neural Networks]]
- [[Linear Classification]]
- [[Model Evaluation]]
- [[Loss Functions]]
- [[Optimization]]
- Machine Learning Task Types

## Sources

- [[Block 1 Slides]], pp. 207–228
- [[Block 3 Slides]], pp. 3–10
