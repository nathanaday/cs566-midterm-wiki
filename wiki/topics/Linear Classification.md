---
id: con-ebq6j5
type: topic
kind: concept
description: A parametric classifier that scores each class with f(x; W, b) = Wx + b, the first learned function in CSCI 566 and the unit that deep networks stack.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Linear classifier
  - Linear models
  - Wx + b
  - Linear model
  - Parametric function
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 2 Slides]]"
  - "[[Block 4 Slides]]"
up:
  - "[[Function Approximation]]"
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Function Approximation]]

## Definition

Linear classification is the first simple function the lecture learns ([[Block 1 Slides]], p. 229).

Example: $X$ is a car image of 50×50×3 = 7,500 numbers. $Y$ is a one-hot vector over 5 classes, such as $\langle 0,0,0,1,0 \rangle$ ([[Block 1 Slides]], p. 230; [[Block 2 Slides]], p. 24).

The parametric approach uses weights $W$ and a bias $b$ that the model learns ([[Block 1 Slides]], pp. 231–235; [[Block 2 Slides]], pp. 24–25):

$$f(x; W, b) = Wx + b$$

| Term | Shape |
| --- | --- |
| $x$ | 7500 × 1 |
| $W$ | 5 × 7500 |
| $b$ | 5 × 1 |
| $f(x; W, b)$ | 5 × 1, one score per class |

The slides label $Y$ as output, $X$ as input, and $W, b$ as the learned weights ([[Block 1 Slides]], p. 235; [[Block 2 Slides]], p. 26). Writing $f(x; W)$ shows $W$, the part to learn, and makes $f$ a parametric function ([[Block 2 Slides]], p. 27).

## Explanation

### A small example

The slides call this a dummy example, not the real dimensions. A 3×4 $W$, $x = [10, 150, 7, 232]^T$, and $b = [0.2, -1, -0.9]^T$ give scores $[96.4, 212.8, 181.1]^T$ ([[Block 1 Slides]], p. 236).

### A learned boundary

On a 2-D example, the learned weights are 0.22 for $h_0(x) = 1$, 1.12 for $h_1(x) = x[1]$, and −1.07 for $h_2(x) = x[2]$. They give a straight diagonal decision boundary. The slides show it as a baseline next to decision trees ([[Block 2 Slides]], p. 73).

### One template per class

Each row of $W$ scores one class, so a linear classifier learns one template per class. [[Block 4 Slides]] shows the templates for ten classes: plane, car, bird, cat, deer, dog, frog, horse, ship, and truck ([[Block 4 Slides]], p. 87).

### Place in the course

In the Week 1 recap, data is the experience, the linear model is the learning algorithm, and the output is knowledge measured as performance on a task ([[Block 2 Slides]], p. 22). See Machine Learning Task Types. Linear models are parametric, and "there are more approaches beyond linear models", such as decision trees ([[Block 2 Slides]], p. 29).

### From linear classification to deep learning

The slides show this linear unit inside a multi-layer network: "Apparently, this is a unit used in deep neural networks too" ([[Block 1 Slides]], pp. 237, 347; [[Block 2 Slides]], p. 28).

### Linear models: summary

The slides list these properties ([[Block 1 Slides]], pp. 344–346):

- $W$ and $b$ define a linear decision boundary.
- Some linear models and losses have an analytical solution, often from the normal equation. Gradient descent can be preferred for very large data sets.
- The loss is usually convex for linear models.
- If the data is not linearly separable, gradient descent still converges, but only to the best linear boundary.
- L1 (lasso) and L2 (ridge) regularization reduce overfitting and handle multicollinearity.
- Linear models generalize well when the true relation is linear or close to linear. For non-linear relations, use more complex models or transform the features.
- Metrics: R-squared for regression; accuracy, precision, recall, and F1 for classification.

### Why it matters

Synthesis: the [[Perceptron]] adds a sign function to this score. [[Loss Functions]] and [[Optimization]] choose $W$ and $b$. [[Linear Separability]] shows what a linear boundary cannot do, which motivates [[Deep Learning]].

## Related

- [[Function Approximation]]
- Machine Learning Task Types
- [[Perceptron]]
- [[Linear Separability]]
- [[Loss Functions]]
- [[Optimization]]
- [[Regularization]]
- [[Neural Networks]]

## Sources

- [[Block 1 Slides]], pp. 229–237, 344–347
- [[Block 2 Slides]], pp. 22, 24–29, 73
- [[Block 4 Slides]], p. 87
