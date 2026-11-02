---
description: A normalization layer that normalizes the features within one example or token, not one feature across a mini-batch as batch normalization does; it is the common choice in Transformers.
aliases: [LayerNorm, Layer Norm, LN]
sources: ["[[Block 7 Slides]]", "[[Block 5 Slides]]"]
subject: 3 Training
---

## Definition

Layer normalization (LayerNorm) normalizes the activations of one example or token over its own features. [[Batch Normalization]] normalizes one feature over the examples in a mini-batch. Both then apply a learned scale and shift per feature.

### Equation

**Normalization.** For one example $x \in \mathbb{R}^D$, average over the $D$ features:

$$
\mu = \frac{1}{D}\sum_{j=1}^{D} x_j, \qquad
\sigma^2 = \frac{1}{D}\sum_{j=1}^{D} (x_j - \mu)^2, \qquad
\hat{x}_j = \frac{x_j - \mu}{\sqrt{\sigma^2 + \epsilon}}
$$

**Scale and shift.** $y_j = \gamma_j \hat{x}_j + \beta_j$, with $\gamma, \beta \in \mathbb{R}^D$ learned.

- On an $N \times D$ batch $X$, LayerNorm uses one row (one example); BatchNorm uses one column (one feature).
- Rule for the exam: identify which values supply the normalization statistics.

### LayerNorm vs BatchNorm

| | BatchNorm | LayerNorm |
| --- | --- | --- |
| Averages over | One feature across the mini-batch | All features of one example or token |
| Axis of $X$ | Column | Row |
| Depends on other examples | Yes | No |
| Running statistics | Yes, used at eval | None |
| Train vs eval | Different function | Same function |
| Small batch | Noisy statistics | No effect |
| Common in | CNNs | Transformers |

> [!warning] Exam trap
> LayerNorm has no train/eval mode switch and no batch-size pitfall. Both problems belong to BatchNorm only.

### In Transformers

Each Transformer block runs causal multi-head attention, adds the input, applies LayerNorm, runs the per-position MLP, adds the input, and applies LayerNorm again. Shortcuts plus normalization make the deep stack trainable. See [[Transformers]] and [[Residual Connections]].

> [!tip]
> The course gives no LayerNorm formula and does not discuss pre-norm versus post-norm placement. The equation above is the standard one.

## Related

- [[Batch Normalization]]: same idea, different group of values
- [[Transformers]]: LayerNorm after each residual add
- [[Residual Connections]]
- [[Data Preprocessing]]: input normalization, done once before training

## Sources

- [[Block 7 Slides]]
- [[Block 5 Slides]]
