---
description: A binary data set is linearly separable if a linear decision boundary separates its classes; data that is not motivates feature transforms and non-linear deep learning.
aliases:
  - Linearly separable
  - Non-separability
  - Why nonlinearity
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
---

## Definition

"For a binary classification problem, a set of examples S is linearly separable if there exists a linear decision boundary that can separate the points" ([[Block 1 Slides]], p. 342, credited to CMU 10601). The slide shows four cases. In the last one the + and − points mix, and no line separates them.

## Explanation

A feature transform can make such data separable. Red and blue points that no line separates in $(x, y)$ become separable after the map to polar coordinates, $f(x, y) = (r(x, y), \theta(x, y))$ ([[Block 1 Slides]], p. 343).

### Why it matters

The [[Perceptron]] and other linear models draw only linear boundaries ([[Block 1 Slides]], p. 341). The section title states the consequence: "Why nonlinearity is the next step" ([[Block 1 Slides]], p. 340). If data is not linearly separable, gradient descent on a linear model still converges, but only to the best linear boundary ([[Block 1 Slides]], p. 345). [[Block 3 Slides]] says the same of one perceptron, and adds that "connecting them together makes a huge difference" ([[Block 3 Slides]], p. 27).

The slides then show a linear model as one unit in a multi-layer network ([[Block 1 Slides]], p. 347). The next lectures cover models that do not follow the form $WX + b$ (decision trees, k-nearest neighbors, clustering) and extend linear models to non-linear deep learning ([[Block 1 Slides]], p. 349).

Synthesis: a hand-made transform like the polar map works when the right transform is known. Deep networks learn such transforms from data, which is the non-linear property in [[Deep Learning]]. The non-linearity comes from [[Activation Functions]]; without them, stacked layers are still one linear model.

## Related

- [[Perceptron]]
- [[Linear Classification]]
- [[Deep Learning]]
- [[Activation Functions]]
- [[Neural Networks]]
- [[Overfitting and Underfitting]]

## Sources

- [[Block 1 Slides]], pp. 340–349
- [[Block 3 Slides]], p. 27
