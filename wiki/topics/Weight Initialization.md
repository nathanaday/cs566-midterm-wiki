---
description: "Weight initialization sets the starting values of a network's weights: random starts break the symmetry between hidden units, and a scale such as small random numbers, Xavier (std = 1/sqrt(Din)), or He/Kaiming (std = sqrt(2/Din)) keeps activations and gradients usable across layers."
aliases: [Initialization, Weight W Initialization, Xavier initialization, Glorot initialization, He initialization, Kaiming initialization, MSRA initialization, He scaling, Xavier scaling, Zero initialization, Small random number initialization, Hidden-unit symmetry, Symmetry breaking]
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 3 Training
---

## Definition

Weight initialization sets a network's starting weights: random, so hidden units differ, and at a scale that keeps activations and gradients usable across layers. The three options are small random numbers, Xavier / Glorot, and He / Kaiming.

### Why All-Zero or Constant Starts Fail

Two hidden units with identical incoming and outgoing weights compute the same output, receive the same gradient, and take the same update, so they stay identical forever. All-zero weights make every unit in a layer identical, and gradient descent cannot separate them. Random starts break the symmetry.

**Symmetry example.** $h = wx$ with $x = 2$, $w_1 = w_2 = 0.4$, $dL/dh = 1$, rate 0.1: both weights move to $0.4 - 0.1 \times 2 = 0.2$ and stay equal. Start at $w_1 = 0.3$, $w_2 = 0.7$ instead and the units compute different things.

> [!warning] Exam trap
> Zero weights are the problem, not zero values in general. Zero biases are valid once the weights are random, and [[LoRA]] starts one factor at zero beside a random factor so the adapter begins as the identity.

### Why the Scale Matters

| Scale | Effect across depth |
|---|---|
| Too small | Signals and gradients shrink |
| Too large | Signals and gradients grow or saturate |
| Suitable (Xavier / He) | Accounts for layer width and activation |

Check the activation scale before training. See [[Vanishing Gradient Problem]] and [[Exploding Gradient Problem]].

### Schemes

| Scheme | $\mathrm{Var}(W)$ | Std | Pairs with | Code |
|---|---|---|---|---|
| Small random | fixed, e.g. $0.01^2$ | $0.01$ | shallow nets only | `0.01 * randn(Din, Dout)` |
| Xavier / Glorot | $1 / D_{in}$ | $1 / \sqrt{D_{in}}$ | tanh, sigmoid-like | `randn(Din, Dout) / sqrt(Din)` |
| He / Kaiming / MSRA | $2 / D_{in}$ | $\sqrt{2 / D_{in}}$ | ReLU family | `randn(Din, Dout) * sqrt(2/Din)` |

All sample from a zero-mean Gaussian. For a conv layer, $D_{in} = \text{filter\_size}^2 \times \text{input\_channels}$ (see [[Convolutional Layer]]).

**Xavier variance.**

$$\mathrm{Var}(W) = \frac{1}{D_{in}}$$

**Xavier derivation.** For $y = \sum_{i=1}^{D_{in}} x_i w_i$ with iid, zero-mean $x_i$ and $w_i$:

$$\mathrm{Var}(y) = D_{in}\,\mathrm{Var}(x_i)\,\mathrm{Var}(w_i), \qquad \mathrm{Var}(y) = \mathrm{Var}(x_i) \iff \mathrm{Var}(w_i) = \frac{1}{D_{in}}$$

**He variance.**

$$\mathrm{Var}(W) = \frac{2}{D_{in}}, \qquad \text{std} = \sqrt{2 / D_{in}}$$

ReLU drops negative pre-activations, which removes about half of the second moment. The factor 2 restores it.

### Activation Statistics Across Six Layers

Forward pass through six layers of width 4096 on a batch of 16 Gaussian inputs. Std of the activations by layer:

| Scheme, activation | Std, layers 1 to 6 | Verdict |
|---|---|---|
| 0.01, tanh | 0.49, 0.29, 0.18, 0.11, 0.07, 0.05 | collapses to zero, tiny gradients |
| Xavier, tanh | 0.63, 0.49, 0.41, 0.36, 0.32, 0.30 | just right |
| Xavier, ReLU | 0.58, 0.41, 0.30, 0.21, 0.15, 0.10 | shrinks, ReLU halves the scale |
| He, ReLU | 0.83, 0.83, 0.83, 0.81, 0.81, 0.81 | just right |

> [!tip]
> Xavier with ReLU is the classic mismatch. Changing the activation may require changing the initialization (see [[Activation Functions]]).

### Choosing an Initialization

- ReLU-family hidden layer (CNN, MLP): He / Kaiming.
- Other feed-forward layer (tanh, sigmoid): Xavier.
- Pretrained backbone: start from its learned weights ([[Transfer Learning]]).
- Otherwise use the library initialization intended for the architecture.
- Initialization helps gradient flow without guaranteeing convergence; depth, activations, and residual paths also matter ([[Residual Connections]], [[Batch Normalization]]).

> [!warning] Exam trap
> Xavier is described as balancing input and output scales, but the course formula uses only the input count. Write $\mathrm{Var}(W) = 1 / D_{in}$.

## Related

- [[Activation Functions]]
- [[Vanishing Gradient Problem]]
- [[Exploding Gradient Problem]]
- [[Batch Normalization]]
- [[Residual Connections]]
- [[ResNet]]
- [[Convolutional Layer]]
- [[LoRA]]: one factor starts at zero
- [[Dying ReLU]]: a different ReLU failure
- [[Transfer Learning]]
- Pretrained Visual Encoders
- [[Optimization]]
- [[Gradient Descent]]

## Sources

- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
