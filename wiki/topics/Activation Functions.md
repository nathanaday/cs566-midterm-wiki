---
description: The non-linear function a neural network applies to each unit's weighted sum, such as sigmoid, tanh, ReLU, Leaky ReLU, PReLU, Maxout, ELU, or GELU, without which stacked layers collapse to one linear map.
aliases: [Activation Function, Nonlinearity, Nonlinear Activation, ReLU, Rectified Linear Unit, Sigmoid, Logistic Function, tanh, Leaky ReLU, PReLU, Parametric ReLU, Parametric Rectifier, ELU, Exponential Linear Unit, Maxout, Activation Saturation, Saturated Neurons]
sources: ["[[Block 3 Slides]]", "CSCI 566 Syllabus", "Sep 14 Lecture Account", "[[Block 4 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 2 Neural networks
---

## Definition

A layer computes $h = f(Wx + b)$, where $f$ is the activation function applied to each unit's weighted sum. Without $f$, stacked layers collapse into one linear map.

### Why a Network Needs One

**Collapse without non-linearity.**

$$W_2(W_1 x + b_1) + b_2 = (W_2 W_1)x + (W_2 b_1 + b_2)$$

- $Y = H(G(F(X)))$ becomes $Y = (HGF)(X)$: one matrix multiplication, a linear boundary only. See [[Linear Separability]].

### Comparison Table

![[graph.png]]

| Function | Formula | Derivative | Range | Main drawback |
| --- | --- | --- | --- | --- |
| Sigmoid | $\sigma(x) = \dfrac{1}{1 + e^{-x}}$ | $\sigma(x)(1 - \sigma(x))$, max 0.25 | $(0, 1)$ | saturates, not zero-centered, exp() |
| tanh | $\tanh(x) = 2\sigma(2x) - 1$ | $1 - \tanh^2(x)$, max 1 | $(-1, 1)$ | saturates |
| ReLU | $\max(0, x)$ | 1 if $x > 0$, 0 if $x < 0$ | $[0, \infty)$ | [[Dying ReLU]], not zero-centered |
| Leaky ReLU | $\max(0.1x, x)$ | 1 if $x > 0$, 0.1 if $x < 0$ | $(-\infty, \infty)$ | gain over ReLU inconsistent |
| PReLU | $\max(\alpha x, x)$, $\alpha$ learned | 1 if $x > 0$, $\alpha$ if $x < 0$ | $(-\infty, \infty)$ | one extra parameter |
| ELU | $x$ if $x \geq 0$; $\alpha(e^x - 1)$ if $x < 0$ | 1 if $x > 0$; $\alpha e^x$ if $x < 0$ | $(-\alpha, \infty)$ | exp() |
| Maxout | $\max(w_1^T x + b_1,\ w_2^T x + b_2)$ | from the larger piece | depends on weights | doubles the weights |
| GELU | $x \cdot \Phi(x)$, Gaussian CDF weighting | smooth everywhere | $\approx (-0.17, \infty)$ | compute |

- ReLU is the Maxout special case $w_1 = 0$, $b_1 = 0$, so Maxout has no zero-gradient region.
- ELU's negative saturation adds some robustness to noise over Leaky ReLU.

### Saturation

A unit saturates when its input falls in a flat region of $f$: the local derivative is near 0 and little gradient passes backward. One cause of the [[Vanishing Gradient Problem]].

| Input $x$ | $\sigma(x)$ | $\sigma'(x)$ |
| --- | --- | --- |
| $-10$ | $\approx 0.000045$ | $\approx 0.000045$ |
| $0$ | $0.50$ | $0.25$ |
| $10$ | $\approx 0.999955$ | $\approx 0.000045$ |

> [!warning] Exam trap
> Each sigmoid layer multiplies the backward gradient by at most 0.25; tanh by at most 1. ReLU does not saturate for $x > 0$ but passes zero gradient for $x < 0$.

### Sigmoid Is Not Zero-Centered

**Gradient on a weight.**

$$\frac{\partial L}{\partial w_i} = \sigma(z)(1 - \sigma(z))\, x_i \cdot \frac{\partial L}{\partial h}, \quad z = \sum_i w_i x_i + b$$

- The local sigmoid gradient is always positive, so if every $x_i > 0$, all $\partial L / \partial w_i$ share the sign of the upstream gradient.
- All weights move in the same direction and the path to the optimum zig-zags.
- tanh is zero-centered but still saturates for large $|x|$.

### ReLU in Practice

- Does not saturate for $x > 0$; cheap; converges about 6x faster than sigmoid or tanh.
- Good default for hidden layers; eases the vanishing gradient problem.
- Sparse activation (many units output 0); see [[Activation Sparsity]].
- Leaky ReLU keeps a small gradient for $x < 0$, so it is less prone to [[Dying ReLU]].
- Pair with He scaling ([[Weight Initialization]]).

> [!tip]
> Use ReLU. Watch the learning rate. Try Leaky ReLU, Maxout, or ELU for marginal gains. Do not default to sigmoid or tanh in hidden layers.

### Where Each Is Used

| Layer | Common choice |
| --- | --- |
| CNN / MLP hidden layers | ReLU family |
| Transformer hidden layers | GELU or gated SiLU variants (BERT, GPT-3 use GELU) |
| Binary classification output | sigmoid (outputs are probabilities) |
| Gates (LSTM, GRU) | sigmoid or tanh |

GELU's soft threshold lets a unit recover instead of sticking at zero output.

## Related

- [[Neural Networks]]
- [[Fundamentals of Deep Learning Nonlinear Activation]]
- [[Deep Learning]]
- [[Linear Separability]]
- [[Perceptron]]: uses the step function $\text{sign}$
- [[Backpropagation]]: the sigmoid derivative in a worked example
- [[Forward Propagation]]: the 2-2-1 ReLU example
- Computational Graphs
- [[Gradient Descent]]
- [[Dying ReLU]]
- [[Activation Sparsity]]
- [[Batch Normalization]]
- [[Weight Initialization]]: He scaling for ReLU layers
- [[Vanishing Gradient Problem]]
- [[Exploding Gradient Problem]]
- [[Convolutional Neural Networks (CNN)]]
- [[AlexNet]]
- [[Transformers]]

## Sources

- [[Block 3 Slides]]
- [[Block 4 Slides]]
- CSCI 566 Syllabus
- Sep 14 Lecture Account
- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
