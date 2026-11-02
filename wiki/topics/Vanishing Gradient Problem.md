---
description: In backpropagation, the gradient for early layers shrinks toward zero when many small local derivatives multiply, so those layers learn slowly or not at all.
aliases: [Vanishing Gradients]
sources: ["[[Block 3 Slides]]", "Sep 14 Lecture Account", "[[Block 4 Slides]]", "[[Block 5 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 3 Training
---
## Definition

In [[Backpropagation]], the gradient for an early layer is a product of local derivatives, one factor per later layer. When those factors are below 1 the product shrinks at every layer, so the early layers receive a gradient near 0 and learn slowly or not at all. Factors above 1 give the mirror case, the [[Exploding Gradient Problem]].

### Why the Product Shrinks


**Sigmoid gate.** Each sigmoid layer contributes one factor, and that factor is small everywhere:
- Saturation: at $x = 10$, $\sigma' = 1(1 - 1) \approx 0$, so almost nothing flows back.
- Depth: 10 sigmoid layers scale the gradient by at most $0.25^{10} \approx 9.5 \times 10^{-7}$, even with no saturation.
- $\tanh' \le 1$, so tanh also shrinks the product once units saturate at large $\lvert x \rvert$.

> [!tip]
> Sigmoid vanishes the gradient even in the steep middle of its curve. Saturation makes it worse, but the 0.25 cap alone is enough in a deep stack.

### Where It Shows Up

- Any deep network: more layers means more factors below 1.
- Vanilla RNNs, where time steps act as layers; this is where the problem is most often discussed ([[Recurrent Neural Networks (RNN)]], Backpropagation Through Time).

### Remedies

Three goals: avoid saturation, control scale, and preserve an identity path for the gradient.

| Remedy | Why it works |
| --- | --- |
| ReLU in hidden layers | derivative 1 for $x > 0$, no saturation on the positive side; still 0 for $x < 0$ |
| Leaky ReLU, PReLU, ELU | non-zero gradient for $x < 0$ (Leaky ReLU: 0.01), avoids [[Dying ReLU]] |
| [[Batch Normalization]] | standardizes each channel per mini-batch, keeping inputs out of the flat regions |
| [[Residual Connections]] | $y = x + f(x)$ gives the gradient an identity route around each block |
| Change the RNN architecture | gated cells such as Long Short-Term Memory replace the repeated $\tanh'$ product |



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
