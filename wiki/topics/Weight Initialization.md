---
description: "Weight initialization sets the starting values of a network's weights: random starts break the symmetry between hidden units, and a scale such as small random numbers, Xavier (std = 1/sqrt(Din)), or He/Kaiming (std = sqrt(2/Din)) keeps activations and gradients usable across layers."
aliases: [Initialization, Xavier initialization, Glorot initialization, He initialization, Kaiming initialization, Symmetry breaking]
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 3 Training
---

## Definition

Weight initialization sets a network's starting weights: random, so hidden units differ, and at a scale that keeps activations and gradients usable across layers. The three options are small random numbers, Xavier / Glorot, and He / Kaiming.

### Why All-Zero or Constant Starts Fail

Two hidden units with identical incoming and outgoing weights compute the same output, receive the same gradient, and take the same update, so they stay identical forever. All-zero weights make every unit in a layer identical, and gradient descent cannot separate them. Random starts break the symmetry.

### Choosing an Initialization

- ReLU-family hidden layer (CNN, MLP): He / Kaiming.
- Other feed-forward layer (tanh, sigmoid): Xavier.
- Pretrained backbone: start from its learned weights ([[Transfer Learning]]).
- Otherwise use the library initialization intended for the architecture.
- Initialization helps gradient flow without guaranteeing convergence; depth, activations, and residual paths also matter ([[Residual Connections]], [[Batch Normalization]]).

> [!tip]
> Xavier is described as balancing input and output scales, but the course formula uses only the input count. Write $\mathrm{Var}(W) = 1 / D_{in}$.

> [!tip]
> Xavier with ReLU is the classic mismatch. Changing the activation may require changing the initialization (see [[Activation Functions]]).

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
