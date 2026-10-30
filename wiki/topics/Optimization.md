---
description: "Finding the weights W that minimize a loss function L; CSCI 566 compares random search, the analytic least-squares solution, and gradient descent, and names the loss-surface problems that slow SGD: poor conditioning, local minima, saddle points, and noisy gradients."
aliases:
  - Loss minimization
  - Random search
  - Analytic solution
  - Normal equation
  - Condition number
  - Poor conditioning
  - Local minimum
  - Local minima
  - Saddle point
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 2 Slides]]"
  - "[[Block 7 Slides]]"
---

## Definition

Optimization finds the $W$ that minimizes a loss function $L$ ([[Block 1 Slides]], pp. 300, 339; [[Block 2 Slides]], p. 27). "Note that we are finding W based on L!" ([[Block 1 Slides]], p. 301). The worked example uses a model $f(x; W)$, an ideal output $y^*$, and the simple loss $L(W) = \lVert f(x; W) - y^* \rVert_2$ ([[Block 1 Slides]], pp. 302–308).

## Explanation

The slides give three strategies ([[Block 1 Slides]], p. 309):

| Strategy | Method | Verdict on the slide |
| --- | --- | --- |
| 1. Random search | try random $W$, keep the best | "Too slow" (pp. 310–312) |
| 2. Analytic solution | solve for $W$ in closed form | "Very hard to find." (pp. 313–316) |
| 3. Numerical approach | [[Gradient Descent]] | used in the course (pp. 317–338) |

In the random-search example, one random $W$ gives $L(W) = 1.7401$ ([[Block 1 Slides]], p. 311).

This random search samples weights. Block 7 also uses random search and grid search to sample hyperparameters ([[Block 7 Slides]], pp. 188, 327). That is a different task. See Model Selection.

### Analytic solution

The slides write the least-squares minimizer as $(X^T X)^{-1} X^T y^*$ ([[Block 1 Slides]], p. 314), then ask "Do you know why it is hard?" (p. 315). In the normal equation $(A^T A)\hat{\beta} = A^T Y$, $A$ is $X$ and $\beta$ is $W$. If $A^T A$ is invertible, $\hat{\beta} = (A^T A)^{-1} A^T Y$ ([[Block 1 Slides]], p. 316). The slides ask two questions there: when is $A^T A$ invertible, and what if it is invertible but expensive because $p$ is very large?

[[Block 2 Slides]] returns to the first question. If $A^T A$ is not invertible, the system is underdetermined and has many feasible solutions. An L2 (ridge) or L1 (lasso) penalty constrains the solution toward small $\beta$ ([[Block 2 Slides]], p. 100). See [[Regularization]].

### Hard loss surfaces: the problems with SGD

Block 7 gives three problems that the shape of the loss and the mini-batch gradient cause for stochastic gradient descent ([[Block 7 Slides]], pp. 91–97). [[Gradient-Based Optimizers]] covers the update rules that answer them.

**Problem #1: poor conditioning.** The slides ask: "What if loss changes quickly in one direction and slowly in another? What does gradient descent do?" ([[Block 7 Slides]], p. 91). The answer: "Very slow progress along shallow dimension, jitter (zigzag) along steep direction" (p. 92). The slides call this a high **condition number**: the "ratio of largest to smallest singular value of the Hessian matrix is large" (pp. 91–92). The slide adds "no need to know details though" (p. 91).

**Problem #2: local minima and saddle points.** At a **local minimum** or a **saddle point** the gradient is zero, so "gradient descent gets stuck" ([[Block 7 Slides]], pp. 93–94). The slides draw a local minimum as a low point on a 1-D loss curve, lower than its neighbors but not the lowest point (pp. 93–94). "Saddle points much more common in high dimension" (p. 95). The slide cites Dauphin et al., "Identifying and attacking the saddle point problem in high-dimensional non-convex optimization", NIPS 2014 (p. 95). The 2-D example is $f(x, y) = x^2 - y^2$. Both partial derivatives are zero at the origin: $\partial f / \partial x = 2x \to 2(0) = 0$ and $\partial f / \partial y = -2y \to -2(0) = 0$ (p. 96). Synthesis: the surface curves up along $x$ and down along $y$, so the origin is not a minimum, but the gradient alone cannot tell this.

**Problem #3: noisy gradients.** "Our gradients come from minibatches so they can be noisy!" ([[Block 7 Slides]], p. 97). One mini-batch gives "a cheap but noisy estimate of the training objective." Across many mini-batches, "repeated updates can make progress without every step lowering loss" (p. 98). The slide's advice: "Judge the trend over many updates" (p. 98). An earlier slide gives the same advice for gradient flow: "Inspect actual loss and gradient behavior" (p. 83).

### Summary

"Loss function (L) measures how well learned W can map X to Y (compared to y*)." "Optimization finds the best W given a loss function L (i.e. finding W that minimizes L)" ([[Block 1 Slides]], p. 339; [[Block 2 Slides]], p. 27).

### Why it matters

The slides note that some linear models have an analytical solution, and that gradient descent can be preferred for very large data sets ([[Block 1 Slides]], p. 344). Synthesis: closed forms exist only for some models and losses, and they do not scale to very large $p$. Random search does not scale either. So deep learning trains with gradient descent. Plain SGD then meets the three problems above, which is why the course moves on to other optimizers.

## Related

- [[Gradient Descent]]
- [[Gradient-Based Optimizers]]
- Learning Rate Schedules
- [[Loss Functions]]
- [[Regularization]]
- [[Linear Classification]]
- Model Selection

## Sources

- [[Block 1 Slides]], pp. 300–316, 339, 344
- [[Block 2 Slides]], pp. 27, 100
- [[Block 7 Slides]], pp. 83, 91–98, 188, 327
