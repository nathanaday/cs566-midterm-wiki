---
id: con-409zjq
type: topic
kind: concept
description: When the gradient becomes too large, a gradient descent step overshoots to a high-loss configuration or fills the network with Inf or NaN values.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Exploding Gradients
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources:
  - "[[Block 3 Slides]]"
  - "[[Block 1 Slides]]"
  - "Sep 14 Lecture Account"
  - "[[Block 5 Slides]]"
up:
  - "[[Neural Network Training]]"
---

> [!concept] Concept
> 4 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Neural Network Training]]

## Definition

The exploding gradient problem occurs when the gradient becomes too large. "If the gradient becomes too big, then the SGD update step becomes too big", with $\theta^{new} = \theta^{old} - \alpha \nabla_\theta J(\theta)$ ([[Block 3 Slides]], p. 234). The effects (p. 234):

1. The step reaches "a bad parameter configuration (with large loss)". This is a bad update.
2. In the worst case, values in the network become `Inf` or `NaN`.
3. Then you must restart training from an earlier checkpoint.

The slides' summary: gradients "can become excessively large, leading to divergent behavior" (p. 269). The week 1 deck lists "Exploding gradient" as one of three issues with gradient descent, with local minima and inexact gradient ([[Block 1 Slides]], p. 338).

## Explanation

### Why a large gradient gives a large step

The update rule is $W \leftarrow W - \eta \cdot dW$ ([[Block 1 Slides]], p. 336; see [[Gradient Descent]]). The step is the learning rate times the gradient, so a large $dW$ has the same effect as a large $\eta$. The slides say a large learning rate can "overshoot or diverge" (p. 336).

Example (general background), with $\eta = 0.01$:

- $dW = 0.5$ gives a step of 0.005.
- $dW =$ 5,000 gives a step of 50. The weight moves far past any nearby minimum.

### In recurrent networks

A vanilla RNN multiplies by the same $W_{hh}$ once for each time step on the way back. With no non-linearity, the gradient from the last loss is ([[Block 5 Slides]], pp. 102–103):

$$\frac{\partial L_T}{\partial W} = \frac{\partial L_T}{\partial h_T} W_{hh}^{T-1} \frac{\partial h_1}{\partial W}$$

When the largest singular value of $W_{hh}$ is greater than 1, gradients can explode (p. 103). The slides' fix is gradient clipping (p. 104). They cite Bengio et al. (1994) and Pascanu et al. (ICML 2013) (pp. 94–105). See [[Recurrent Neural Networks (RNN)]] and [[Backpropagation Through Time]].

### Gradient clipping

The slides give gradient clipping as the "solution for exploding gradient" (pp. 235–237). If $\lVert g \rVert$ is at or above a threshold, rescale $g$ to the threshold. "Take a step in the same direction, but a smaller step" (p. 235, citing Pascanu et al. 2013). "Clipping limits the damage of one step. Finding the cause is a separate job" (p. 237). [[Block 5 Slides]] gives the same rule for RNNs: $n = \lVert g \rVert_2$; if $n > \tau$, $g \leftarrow (\tau / n)\, g$ (p. 104). See [[Gradient Clipping]].

### Cause and other fixes

General background, not from a course source:

- **Cause:** the opposite of the [[Vanishing Gradient Problem]]. The backward pass multiplies factors layer by layer ([[Computational Graphs]]). If most factors are above 1, the gradient grows exponentially with depth. The RNN case above is one example.
- A smaller learning rate, careful weight initialization, and [[Batch Normalization]] also help.
- **Checkpoints:** save the weights and the optimizer state at regular steps. A run that reaches `NaN` can then restart from the last good copy.

The slides' triage list says to skip a batch, restore a checkpoint, or check the data and the learning rate ([[Block 3 Slides]], p. 237).

### Why it matters

Synthesis: one bad update can undo many good ones. Any calculation with `NaN` gives `NaN`, so the value spreads through the network and training cannot recover by itself. That is why the lecture (Sep 14 Lecture Account, § Exploding gradients) and the slides (p. 234) say to restart from a checkpoint.

## Related

- [[Vanishing Gradient Problem]]
- [[Gradient Clipping]]
- [[Gradient Descent]]
- [[Batch Normalization]]
- [[Computational Graphs]]
- [[Optimization]]
- [[Recurrent Neural Networks (RNN)]]
- [[Backpropagation Through Time]]

## Sources

- [[Block 3 Slides]], pp. 234–237, 269
- [[Block 5 Slides]], pp. 102–104, citing Bengio et al. (1994) and Pascanu et al. (2013)
- [[Block 1 Slides]], p. 336 (learning rate) and p. 338 (issues with gradient descent)
- Sep 14 Lecture Account, § Exploding gradients
- The step-size example, the general cause, and the checkpoint details: general background, not from a course source
