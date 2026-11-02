---
description: In backpropagation, the gradient for early layers shrinks toward zero when many small local derivatives multiply, so those layers learn slowly or not at all.
aliases: [Vanishing Gradients]
sources: ["[[Block 3 Slides]]", "Sep 14 Lecture Account", "[[Block 4 Slides]]", "[[Block 5 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 3 Training
---

## Definition

In [[Backpropagation]], the gradient for an early layer is a product of local derivatives, one factor per later layer. When those factors are below 1 the product shrinks at every layer, so the early layers receive a gradient near 0 and learn slowly or not at all. Factors above 1 give the mirror case, the [[Exploding Gradient Problem]].

### Why the Product Shrinks

**Chain rule across four layers.**

$$\frac{\partial J^{(4)}}{\partial h^{(1)}} = \frac{\partial h^{(2)}}{\partial h^{(1)}} \times \frac{\partial h^{(3)}}{\partial h^{(2)}} \times \frac{\partial h^{(4)}}{\partial h^{(3)}} \times \frac{\partial J^{(4)}}{\partial h^{(4)}}$$

**Sigmoid gate.** Each sigmoid layer contributes one factor, and that factor is small everywhere:

$$\frac{\partial L}{\partial x} = \sigma(x)\big(1 - \sigma(x)\big) \cdot \frac{\partial L}{\partial \sigma}, \qquad \max_x \sigma'(x) = 0.25 \text{ at } x = 0$$

- Saturation: at $x = 10$, $\sigma' = 1(1 - 1) \approx 0$, so almost nothing flows back.
- Depth: 10 sigmoid layers scale the gradient by at most $0.25^{10} \approx 9.5 \times 10^{-7}$, even with no saturation.
- $\tanh' \le 1$, so tanh also shrinks the product once units saturate at large $\lvert x \rvert$.

> [!warning] Exam trap
> Sigmoid vanishes the gradient even in the steep middle of its curve. Saturation makes it worse, but the 0.25 cap alone is enough in a deep stack.

### Where It Shows Up

- Any deep network: more layers means more factors below 1.
- Vanilla RNNs, where time steps act as layers; this is where the problem is most often discussed ([[Recurrent Neural Networks (RNN)]], Backpropagation Through Time).

**RNN gradient to the shared weight.**

$$\frac{\partial L_T}{\partial W} = \frac{\partial L_T}{\partial h_T} \Big( \prod_{t=2}^{T} \tanh'(W_{hh} h_{t-1} + W_{xh} x_t) \Big) W_{hh}^{T-1} \frac{\partial h_1}{\partial W}$$

- The product of $\tanh'$ terms, each at most 1, drives the gradient to 0 as $T$ grows.
- With no non-linearity, $W_{hh}^{T-1}$ vanishes when the largest singular value of $W_{hh}$ is below 1 (Bengio et al. 1994; Pascanu et al. 2013).

### Why It Hurts

- Near effects win: the gradient from far-away steps is tiny next to nearby ones, so weights learn only short-range dependencies.
- A gradient near 0 is ambiguous: either the data has no long-range dependency, or the parameters fail to capture one.
- [[Gradient Descent]] cannot update the early layers, so adding layers stops helping.

### Remedies

Three goals: avoid saturation, control scale, and preserve an identity path for the gradient.

| Remedy | Why it works |
| --- | --- |
| ReLU in hidden layers | derivative 1 for $x > 0$, no saturation on the positive side; still 0 for $x < 0$ |
| Leaky ReLU, PReLU, ELU | non-zero gradient for $x < 0$ (Leaky ReLU: 0.01), avoids [[Dying ReLU]] |
| [[Batch Normalization]] | standardizes each channel per mini-batch, keeping inputs out of the flat regions |
| [[Residual Connections]] | $y = x + f(x)$ gives the gradient an identity route around each block |
| Change the RNN architecture | gated cells such as Long Short-Term Memory replace the repeated $\tanh'$ product |

> [!tip]
> Sigmoid is still fine at the output of a binary classifier: the gradient passes through only one sigmoid there. See [[Activation Functions]].

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

- [[Block 3 Slides]]
- [[Block 4 Slides]]
- [[Block 5 Slides]]
- Sep 14 Lecture Account
- [[F26-midterm-review-234p]]
