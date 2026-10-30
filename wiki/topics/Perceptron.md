---
description: A linear model that applies a step function to a weighted sum plus bias, f(x; W) = sign(Wx + b); alone it solves only linearly separable problems.
aliases:
  - Perceptron algorithm
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
  - "Lecture 1"
  - "CSCI 566 Syllabus"
---

## Definition

The perceptron is a linear model. It computes a weighted sum of the inputs plus a bias, then applies a step function ([[Block 1 Slides]], p. 341):

$$f(x; W) = \text{sign}(Wx + b)$$

The diagram shows inputs $x_1, \dots, x_n$ with weights $w_1, \dots, w_n$, a constant input of 1 with weight $w_0$ (the bias), a weighted-sum node, and a step function.

## Explanation

The slides titled "Linear ML Classification (Perceptron)" use the score $Wx + b$ for a multi-class image example ([[Block 1 Slides]], p. 261). See [[Linear Classification]] for the shapes.

### Example: W and b matter

Three images (car, cat, airplane), each a 2×2 grid of four numbers, are scored for the classes Cat, Car, and Airplane ([[Block 1 Slides]], pp. 262–274):

| Image | Scores (Cat, Car, Airplane), first $W, b$ | Scores, second $W, b$ |
| --- | --- | --- |
| Car | 0.631, **0.969**, 0.71 | **0.884**, 0.34, 0.455 |
| Cat | **0.73**, 0.598, 0.161 | **0.699**, 0.39, 0.181 |
| Airplane | 0.04, 0.317, **0.707** | **0.558**, 0.04, 0.453 |

With the first weights, each image gets its correct class: "Looks perfect! Doesn't it?" ([[Block 1 Slides]], p. 267). With the second weights, all three images score highest on Cat: "Oops…" and "W and b matter!" ([[Block 1 Slides]], pp. 273–274).

### Connecting perceptrons

[[Block 3 Slides]] draws the same unit again, labels the sum a linear combination, and adds: "Itself can only address linearly separable problem; but connecting them together makes a huge difference" ([[Block 3 Slides]], p. 27). See [[Neural Networks]].

### Why it matters

The example sets up the next question: which $W$ is better? [[Loss Functions]] answer it with a number, and [[Optimization]] searches for the $W$ with the lowest loss ([[Block 1 Slides]], pp. 275–276).

A perceptron draws a linear boundary, so it fails on data that is not linearly separable ([[Block 1 Slides]], pp. 341–343). See [[Linear Separability]].

### History and course placement

The slides date the perceptron algorithm to 1958, in a timeline credited to CMU 15884 by Tianqi Chen ([[Block 1 Slides]], p. 28). Lecture 1 say the 1950s (§ Background Topics). The CSCI 566 Syllabus covers the perceptron again in week 3, with gradient descent and forward propagation.

## Related

- [[Linear Classification]]
- [[Neural Networks]]
- [[Loss Functions]]
- [[Optimization]]
- [[Linear Separability]]
- Evolution of Machine Learning

## Sources

- [[Block 1 Slides]], pp. 28, 261–276, 341–343
- [[Block 3 Slides]], p. 27
- Lecture 1, § Background Topics
- CSCI 566 Syllabus, week 3
