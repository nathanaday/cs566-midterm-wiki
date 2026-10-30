---
description: The L1 penalty (Lasso) drives some weights to exactly zero and so selects features, while the L2 penalty (Ridge) shrinks all weights toward zero without removing any.
aliases: [Lasso, Ridge vs Lasso, L1 Penalty, Sparsity, Sparse Weights]
sources: ["[[Block 1 Slides]]", "[[Block 2 Slides]]", "[[F26-midterm-review-234p]]", "[[CSCI 566 Midterm (Spring 2024)]]"]
---

## Definition

The L1 penalty is the sum of the absolute values of the weights, $R(W) = \sum_{k,l} \lvert W_{k,l} \rvert$, and the L2 penalty is the sum of their squares, $R(W) = \sum_{k,l} W_{k,l}^2$ ([[Block 1 Slides]], p. 296). In least squares the L1 form is called Lasso and the L2 form is called Ridge regression ([[Block 2 Slides]], p. 100). The two penalties shrink the weights in different ways: "Lasso (l1 penalty) results in sparse solutions – vector with more zero coordinates" ([[Block 1 Slides]], p. 298). A weight that is exactly zero removes its feature from the model, so Lasso performs feature selection and Ridge does not.

## Explanation

The parent topic [[Regularization]] gives the full objective $L(W) = \text{data loss} + \lambda R(W)$ and the table of penalties. This topic covers one question: why L1 zeroes weights and L2 only shrinks them.

### The diamond and the circle

The slide credited to CMU 10701 solves $\min_\beta (A\beta - Y)^T(A\beta - Y) + \lambda\,\text{pen}(\beta)$ and draws the two penalties in the $(\beta_1, \beta_2)$ plane ([[Block 1 Slides]], p. 298). The ellipses are the level sets of the data loss $J(\beta)$ around the unpenalized optimum $\hat\beta$. The set of $\beta$ with constant L2 norm is a circle, and the set with constant L1 norm is a diamond with its corners on the axes. The penalized solution is where the smallest ellipse touches the constraint shape. A diamond's corners stick out along the axes, so the ellipse tends to touch it at a corner, where one coordinate is zero. A circle has no corners, so the ellipse touches it at a point where both coordinates are nonzero. The slide adds that the sparse solution is "Good for high-dimensional problems – don't have to store all coordinates, interpretable solution!" and that an L0 penalty, which counts nonzero weights, would be ideal, "but optimization becomes non-convex" (p. 298).

### The gradient view

Synthesis: the decks only draw the picture; the same fact follows from the gradients. The L2 term $\lambda w^2$ has gradient $2\lambda w$, which shrinks as $w$ shrinks, so each step removes a fraction of the weight and the weight approaches zero without reaching it. The L1 term $\lambda \lvert w \rvert$ has gradient $\lambda\,\text{sign}(w)$, a constant pull of size $\lambda$ toward zero no matter how small $w$ is. When the data gradient at $w = 0$ is weaker than $\lambda$, the weight is pinned at exactly zero. In a linear model a zero weight means the feature has no effect on the prediction, which is the sense in which Lasso selects features.

### Elastic net

Elastic net adds the two penalties, $R(W) = \sum_{k,l} \beta W_{k,l}^2 + \lvert W_{k,l} \rvert$ ([[Block 1 Slides]], p. 296). The midterm review lists "L2 regularization (Weight decay)", "L1 regularization", and "Elastic net (L1 + L2)" as the penalties "In common use" ([[F26-midterm-review-234p]], p. 126, a copy of Block 7 slide 139). Synthesis: the decks do not say why one would mix them. The L1 part keeps the sparsity, and the L2 part keeps the solution stable when features are correlated, where Lasso alone tends to pick one of the correlated features at random.

### What the decks cover

The decks state the L1 and L2 formulas, the ridge and lasso names, and the sparsity claim with its figure ([[Block 1 Slides]], pp. 296, 298; [[Block 2 Slides]], p. 100). The phrase "feature selection", the gradient argument, and the reason for elastic net are Synthesis. [[Block 3 Slides]] uses "sparsity" for ReLU activations that are zero (pp. 79-86); that is activation sparsity, a different thing from sparse weights.

## Exam Questions

**Q35.** Comparing Ridge regression and Lasso regression, which can help feature selection? Answer: B, Lasso regression (L1) ([[CSCI 566 Midterm (Spring 2024)]], Q35).

Reasoning: Lasso's L1 penalty yields "sparse solutions – vector with more zero coordinates" ([[Block 1 Slides]], p. 298). A zero weight drops its feature from the model, which is feature selection. Ridge's L2 penalty shrinks every weight by a fraction and leaves all of them nonzero, so it keeps every feature. "Both" and "Neither" are wrong for the same reason.

## Related

- [[Regularization]]: the full objective, the penalty table, and the L2 worked example
- [[Overfitting and Underfitting]]: what the penalty guards against
- [[Linear Classification]]: the models on which Lasso and Ridge are defined
- [[Loss Functions]]: the data loss the penalty is added to
- [[Gradient Descent]]: the update whose pull toward zero differs between L1 and L2

## Sources

- [[Block 1 Slides]], pp. 296, 298
- [[Block 2 Slides]], p. 100
- [[F26-midterm-review-234p]], p. 126
- [[CSCI 566 Midterm (Spring 2024)]], Q35
