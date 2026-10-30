---
description: A residual connection adds a block's input to its output, y = x + f(x), so the layers learn only the residual and the gradient gets an identity route around the block.
aliases: [Skip Connection, Residual Path, Residual Block, Identity Shortcut, Shortcut Connection, Residual Learning]
sources: ["[[Block 3 Slides]]", "[[Block 4 Slides]]", "[[Block 5 Slides]]", "[[F26-midterm-review-234p]]"]
---

> [!concept] Concept
> 4 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Vanishing Gradient Problem]]

## Definition

A residual connection adds a block's input to its output: $y = x + f(x)$. Then $\dfrac{dy}{dx} = I + J_f$, where $I$ is the identity and $J_f$ is the Jacobian of $f$ ([[Block 3 Slides]], p. 233, citing He et al., CVPR 2016; [[Block 4 Slides]], p. 210). The $I$ term gives the gradient a direct route around $f$.

A residual block is the unit that [[ResNet]] stacks. It applies conv, ReLU, conv to compute $F(x)$, adds the identity $x$, and applies ReLU to $F(x) + x$ ([[Block 4 Slides]], pp. 201, 208).

## Explanation

### The problem: degradation

[[Block 4 Slides]] asks what happens when we keep stacking layers on a "plain" CNN (p. 202):

- A 56-layer plain model has higher training error and higher test error than a 20-layer model (pp. 203-204).
- The deeper model performs worse, but overfitting does not cause this (p. 204). Synthesis: the higher training error rules out overfitting.
- Fact: deeper models have more representation power (more parameters) than shallower models (p. 205).
- Hypothesis: this is an optimization problem, because deeper models are harder to optimize (p. 205).
- A solution by construction: copy the learned layers of the shallower model and set the extra layers to identity. The deeper model is then at least as good as the shallower one (p. 206).

[[Block 3 Slides]] says of He et al.: "They target degradation; the identity route for gradients follows" (p. 233).

### Residual learning

The layers fit a residual mapping $F(x) = H(x) - x$ instead of the desired mapping $H(x)$. The block then outputs $H(x) = F(x) + x$ ([[Block 4 Slides]], pp. 207-209). If $F(x) = 0$, the block is the identity, $H(x) = x$ (p. 208). The slides say that learning the residual is easier than learning $H(x)$ (p. 209).

Synthesis: the block starts close to the identity solution of p. 206. The layers need only learn a change from the input.

### The gradient through residual blocks

For $y = x + f(x)$, the Jacobian is $J_y = I + J_f$. In one dimension, $y' = 1 + f'$ ([[Block 4 Slides]], p. 210). Take three scalar blocks with $f' = 0.10, 0.20, 0.10$:

- With residual connections: $(1.10)(1.20)(1.10) = 1.452$.
- Without the identity path: $(0.10)(0.20)(0.10) = 0.002$.

The expanded product has an all-identity term, so one path escapes repeated shrinking. The slide says this does not guarantee that gradients do not vanish (p. 210).

The midterm review works one block with numbers: "In y = x + F(x), the gradient to x is the sum of an identity path and a branch path" ([[F26-midterm-review-234p]], p. 101). With $\partial L / \partial y = 3$ and $F'(x) = -0.25$:

- Identity path: $3 \times 1 = 3$.
- Branch path: $3 \times (-0.25) = -0.75$.
- $\partial L / \partial x = 3 - 0.75 = 2.25$.

"The branch cancels part of the identity: 1 + F'(x) = 0.75, so 2.25 < 3" (p. 101). Synthesis: the identity path does not keep the gradient at its upstream value. A negative $F'$ makes it smaller. This agrees with [[Block 4 Slides]], p. 210.

### Pre-activation block

In "Identity Mappings in Deep Residual Networks", the creators of ResNet reorder the block: BN, ReLU, conv, BN, ReLU, conv, then add the identity shortcut. This gives a more direct path to propagate information through the network, and better performance ([[Block 4 Slides]], p. 223). See [[Batch Normalization]].

### Use in deep models

[[Block 3 Slides]] says residual paths plus normalization are common in deep models in 2026, and cites Hyper-Connections (ICLR 2025) as evidence that the path is being redesigned (p. 233).

The slide groups three fixes for the [[Vanishing Gradient Problem]]: "avoid saturation" ([[Activation Functions]]), "control scale" ([[Batch Normalization]]), and "preserve an identity path for the gradient" (this page) (p. 233).

The [[Transformers]] block also uses residual paths. In the course's text-generating Transformer, each block runs causal multi-head attention, then "+ input → LayerNorm", then the MLP at each position, then "+ input → LayerNorm" again. "Gray: shortcuts + normalization help train the stack." ([[Block 5 Slides]], p. 149; repeated in [[F26-midterm-review-234p]], p. 194). A simpler diagram of the block leaves them out: "Residual connections and LayerNorm omitted for clarity" ([[F26-midterm-review-234p]], p. 189). See [[Layer Normalization]].

Open question: the [[Block 3 Slides]] text "Week 5 opens f." is cut off. What does it mean?

## Related

- [[ResNet]]: the network built from residual blocks, with its bottleneck block
- [[Vanishing Gradient Problem]]
- [[Batch Normalization]]
- [[Layer Normalization]]: the normalization after each residual add in a Transformer block
- [[Convolutional Neural Networks (CNN)]]
- [[Transformers]]

## Sources

- [[Block 3 Slides]], p. 233
- [[Block 4 Slides]], pp. 201-210, 223
- [[Block 5 Slides]], p. 149
- [[F26-midterm-review-234p]], pp. 101, 189, 194
