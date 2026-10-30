---
id: con-a1g9v8
type: topic
kind: concept
description: In backpropagation, the gradient for early layers shrinks toward zero when many small local derivatives multiply, so those layers learn slowly or not at all.
tags: [machine-learning/cs566-deeplearning]
aliases: [Vanishing Gradients]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 3 Slides]]", "Sep 14 Lecture Account", "[[Block 4 Slides]]", "[[Block 5 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Neural Network Training]]"]
---

> [!concept] Concept
> 5 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Neural Network Training]]

## Definition

In backpropagation, the gradient for an early layer is a product of local derivatives, with one factor for each later layer (Computational Graphs). [[Block 3 Slides]] writes it for four layers (pp. 224–229):

$$\frac{\partial J^{(4)}}{\partial h^{(1)}} = \frac{\partial h^{(2)}}{\partial h^{(1)}} \times \frac{\partial h^{(3)}}{\partial h^{(2)}} \times \frac{\partial h^{(4)}}{\partial h^{(3)}} \times \frac{\partial J^{(4)}}{\partial h^{(4)}}$$

"When these are small, the gradient shrinks at every step" ([[Block 3 Slides]], p. 229). The early layers then get a gradient near 0, so they learn slowly or not at all. The problem "can occur in any type of deep neural network", but it "is more prominently discussed in the architecture with sequential data" (p. 225). The slides' summary: "In deep networks, gradients can become very small, so the weights update extremely slowly" (p. 269).

## Explanation

### One saturated activation

[[Block 4 Slides]] shows the cause at a single sigmoid, $Y = \sigma(X)$ (p. 158, figure credited to Stanford CS231n). The chain rule gives

$$\frac{\partial Y}{\partial X} = \frac{\partial Y}{\partial \sigma} \cdot \frac{\partial \sigma}{\partial X}$$

The factor $\partial \sigma / \partial X$ "is almost 0 for most of X": the slide marks the two flat ends of the curve. "Thus, $\partial Y / \partial X$ also goes to 0" (p. 158). Synthesis: in a deep network this small factor appears once for each sigmoid layer, so the product in the definition above shrinks fast.

The midterm review repeats the sigmoid gate from [[Block 3 Slides]]: $\partial L / \partial x = (\partial \sigma / \partial x)(\partial L / \partial \sigma)$, with $\partial \sigma / \partial x = \sigma(x)(1 - \sigma(x))$. At $x = 10$ this is $1(1 - 1) = 0$ ([[F26-midterm-review-234p]], p. 98). "Then the gradients flowing back are tiny (about 4.5e-5 here) and the weights barely move" (p. 100).

### In recurrent networks

In a vanilla RNN, the time steps play the part of layers. The gradient from the last loss back to the shared weight is ([[Block 5 Slides]], p. 101):

$$\frac{\partial L_T}{\partial W} = \frac{\partial L_T}{\partial h_T} \Big( \prod_{t=2}^{T} \tanh'(W_{hh} h_{t-1} + W_{xh} x_t) \Big) W_{hh}^{T-1} \frac{\partial h_1}{\partial W}$$

Two factors shrink it:

- $\tanh' \le 1$ at every step, so the product of $\tanh'$ terms makes the gradient vanish (p. 101).
- With no non-linearity, the gradient is $\frac{\partial L_T}{\partial h_T} W_{hh}^{T-1} \frac{\partial h_1}{\partial W}$. It vanishes when the largest singular value of $W_{hh}$ is less than 1 (pp. 102–103).

The slides cite Bengio et al. (1994) and Pascanu et al. (ICML 2013) (pp. 94–105). See [[Recurrent Neural Networks (RNN)]] and Backpropagation Through Time.

### Why it is a problem

The slides give two reasons ([[Block 3 Slides]], pp. 230–231):

1. **Near effects win.** "Gradient signal from faraway is lost because it's much smaller than gradient signal from close-by." So the weights are updated only for near effects, not long-term effects (p. 230).
2. **The gradient measures the effect of the past on the future.** If the gradient from step $t$ to step $t + n$ becomes very small, we cannot tell if there is no dependency between $t$ and $t+n$ in the data, or if we have the wrong parameters to capture a true dependency (p. 231).

Synthesis: without a usable gradient, [[Gradient Descent]] cannot update the early layers, so more layers do not help. The opposite problem is the [[Exploding Gradient Problem]]: factors above 1 make the gradient grow at each layer.

Example (general background, not from a course source): the sigmoid derivative is at most 0.25 ([[Activation Functions]]). Across 10 sigmoid layers, the activation derivatives alone multiply the gradient by at most $0.25^{10} \approx 9.5 \times 10^{-7}$.

### Fixes

The Sep 14 lecture named two fixes: appropriate activation functions and batch normalization (Sep 14 Lecture Account, § Vanishing gradients). The slides confirm both and add a third ([[Block 3 Slides]], pp. 232–233). They sum them up as: "avoid saturation, control scale, and preserve an identity path for the gradient" (p. 233).

**Fix 1: appropriate activation functions.** "ReLU (Rectified Linear Unit) is less susceptible to the vanishing gradient problem because it does not saturate in the positive region. Variants like Leaky ReLU, Parametric ReLU (PReLU), or Exponential Linear Unit (ELU) can also be used to avoid dead neurons in ReLU" ([[Block 3 Slides]], p. 232). [[Block 4 Slides]] agrees: ReLU prevents gradient vanishing when $x > 0$, but it still loses the gradient when $x < 0$ (p. 160). The midterm review's activation slides make the same two points. Sigmoid is "Prone to vanishing gradient problem (discussed later)" ([[F26-midterm-review-234p]], p. 49). ReLU belongs "In most hidden layers, as it helps with the vanishing gradient problem and speeds up training" (p. 50).

The table and bullets below are general background, consistent with the slides:

| Function | Largest derivative | Effect on the gradient in hidden layers |
| --- | --- | --- |
| Sigmoid | 0.25 | shrinks at each layer, and is near 0 when the unit saturates |
| tanh | 1 | shrinks when the unit saturates, for large $\lvert x \rvert$ |
| ReLU | 1 for $x > 0$ | passes through unchanged for active units |
| Leaky ReLU | 1 for $x > 0$, 0.01 for $x < 0$ | never exactly 0 |

- Use ReLU or a variant in hidden layers ([[Activation Functions]]).
- Sigmoid is still fine at the output of a binary classifier, because the gradient passes through only one sigmoid.
- ReLU has its own risk: a unit with a gradient of 0 for all inputs stops learning ([[Dying ReLU]]).

**Fix 2: batch normalization.** The slides use batch normalization "to fix the range" ([[Block 3 Slides]], p. 232). During training it standardizes each channel with mini-batch statistics, then applies a learned scale and shift (p. 232). See [[Batch Normalization]].

**Fix 3: residual connections.** A residual path $y = x + f(x)$ gives the gradient an identity route around a block ([[Block 3 Slides]], p. 233). See [[Residual Connections]].

**For RNNs: change the architecture.** For vanishing gradients in a vanilla RNN, the slides' remedy is to change the RNN architecture ([[Block 5 Slides]], p. 105). The deck then moves to the LSTM; see Long Short-Term Memory.

## Related

- [[Exploding Gradient Problem]]
- [[Activation Functions]]
- [[Batch Normalization]]
- [[Residual Connections]]
- [[Dying ReLU]]
- [[Backpropagation]]
- Backpropagation Through Time
- Computational Graphs
- [[Gradient Descent]]
- [[Recurrent Neural Networks (RNN)]]
- Long Short-Term Memory

## Sources

- [[Block 3 Slides]], pp. 224–233, 269
- [[Block 4 Slides]], pp. 158, 160. The figure on p. 158 is credited to Stanford CS231n.
- [[Block 5 Slides]], pp. 101–105, citing Bengio et al. (1994) and Pascanu et al. (2013)
- Sep 14 Lecture Account, § Vanishing gradients
- [[F26-midterm-review-234p]], pp. 49-50, 98-100
- The sigmoid example, the activation table, and the bullets under it: general background, not from a course source
