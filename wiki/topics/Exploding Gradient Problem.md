---
description: When the gradient becomes too large, a gradient descent step overshoots to a high-loss configuration or fills the network with Inf or NaN values.
aliases:
  - Exploding Gradients
sources:
  - "[[Block 3 Slides]]"
  - "[[Block 1 Slides]]"
  - "Sep 14 Lecture Account"
  - "[[Block 5 Slides]]"
subject: 3 Training
---

## Definition

The exploding gradient problem occurs when the gradient grows so large that one [[Gradient Descent]] step overshoots to a high-loss configuration or fills the network with `Inf` or `NaN`. It is the mirror image of the [[Vanishing Gradient Problem]]: the backward pass multiplies factors layer by layer, and when most factors exceed 1 the product grows exponentially with depth.

### Cause

**Update rule.** The step is the learning rate times the gradient, so a huge gradient acts like a huge learning rate.

$$\theta^{new} = \theta^{old} - \alpha \nabla_\theta J(\theta)$$

Example with $\alpha = 0.01$: $dW = 0.5$ gives a step of $0.005$; $dW = 5000$ gives a step of $50$, far past any nearby minimum.

**RNN case.** A vanilla RNN multiplies by the same $W_{hh}$ once per time step on the way back. With no non-linearity, the gradient from the last loss is

$$\frac{\partial L_T}{\partial W} = \frac{\partial L_T}{\partial h_T} W_{hh}^{T-1} \frac{\partial h_1}{\partial W}$$

Largest singular value of $W_{hh}$ above 1 gives explosion; below 1 gives vanishing. See [[Recurrent Neural Networks (RNN)]].

### Symptoms

- One update jumps to a bad parameter configuration with large loss.
- Loss diverges instead of decreasing.
- Values become `Inf` or `NaN`; any arithmetic with `NaN` yields `NaN`, so it spreads through the whole network.
- Training cannot recover on its own; restart from an earlier checkpoint.

> [!warning] Exam trap
> One bad update can undo many good ones. The answer to a `NaN` run is restore a checkpoint, not keep training.

### Gradient Clipping

The main fix (Pascanu et al. 2013). Keep the direction, shrink the step. See [[Gradient Clipping]].

**Clipping rule.** With $n = \lVert g \rVert_2$ and threshold $\tau$:

$$g \leftarrow \frac{\tau}{n}\, g \quad \text{if } n > \tau$$

> [!tip]
> Clipping limits the damage of one step. Finding the cause is a separate job.

### Remedies

| Remedy | What it does |
| --- | --- |
| [[Gradient Clipping]] | Caps the step norm at $\tau$ |
| Smaller learning rate | Scales every step down |
| Careful weight initialization | Keeps factors near 1 |
| [[Batch Normalization]] | Keeps activations in range |
| Checkpoints | Restore weights and optimizer state after `NaN` |
| Skip the batch | Drops one bad update |
| Check data and learning rate | Finds the cause |

## Related

- [[Vanishing Gradient Problem]]
- [[Gradient Clipping]]
- [[Gradient Descent]]
- [[Batch Normalization]]
- Computational Graphs
- [[Optimization]]
- [[Recurrent Neural Networks (RNN)]]
- Backpropagation Through Time

## Sources

- [[Block 3 Slides]]
- [[Block 5 Slides]]
- [[Block 1 Slides]]
- Sep 14 Lecture Account
