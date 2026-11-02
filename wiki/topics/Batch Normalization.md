---
description: A layer that normalizes each channel of a batch to zero mean and unit variance and then applies a learned scale and shift; it makes deep networks easier to train, and it computes a different function in training and eval mode.
aliases: [BatchNorm, Batch Norm, BN]
sources:
  - "[[Block 3 Slides]]"
  - "[[Block 1 Slides]]"
  - "Sep 14 Lecture Account"
  - "[[Block 4 Slides]]"
  - "[[Block 7 Slides]]"
  - "[[F26-midterm-review-234p]]"
subject: 3 Training
---

## Definition

Batch normalization (BN) normalizes each channel of a batch of activations to zero mean and unit variance, then applies a learned per-channel scale $\gamma$ and shift $\beta$. It makes deep networks easier to train. The layer computes a different function in training mode and in eval mode.
Place after a fully connected or conv layer and before the nonlinearity: Conv, BN, ReLU.

**Benefits**
- Deep networks train more easily and gradients flow better; with good [[Activation Functions]], BN is a fix for the [[Vanishing Gradient Problem]].
- Higher learning rates and faster convergence.
- Less sensitivity to initialization.
- Batch-statistics noise acts as [[Regularization]] during training.
- Zero overhead at test time.

Why it works is open. Reducing internal covariate shift was the original motivation, not an established explanation.

**Pitfalls:**
- Small batches: who else is in the batch becomes part of the model. A batch of 2 with $x = [1, 3]$ always normalizes to $[-1, +1]$. A batch of 1 has variance 0, and PyTorch `BatchNorm1d` raises an error on a $[1, C]$ input in training mode. Group Normalization targets this dependence.
- The train and eval mismatch above is the most common BN bug.
### Training-Time Computation

Input $x$ has shape $N \times D$. Every statistic is per channel $j$, averaged over the $N$ examples in the batch.

**Batch mean.**
$$\mu_j = \frac{1}{N}\sum_{i=1}^{N} x_{i,j}$$

**Batch variance (biased, divide by $N$).**
$$\sigma_j^2 = \frac{1}{N}\sum_{i=1}^{N} (x_{i,j} - \mu_j)^2$$

**Normalize.**
$$\hat{x}_{i,j} = \frac{x_{i,j} - \mu_j}{\sqrt{\sigma_j^2 + \epsilon}}$$

**Scale and shift.**
$$y_{i,j} = \gamma_j \hat{x}_{i,j} + \beta_j$$

- $\epsilon$ is a small constant that prevents division by zero.
- $\gamma, \beta \in \mathbb{R}^D$ are learned. Setting $\gamma = \sigma$ and $\beta = \mu$ recovers the identity, so the output need not have zero mean and unit variance.
- Centering and scaling do not make the values Gaussian.

### Which Axes Are Averaged

| Input | Shape of $x$ | Averaged over | Shape of $\mu, \sigma^2, \gamma, \beta$ |
| --- | --- | --- | --- |
| Fully connected | $N \times D$ | $N$ | $D$ |
| Convolutional | $N \times C \times H \times W$ | $N, H, W$ | $C$ |

### Eval Time

**Running statistics.** Training also keeps exponential moving averages of the batch statistics, updated every step with **momentum** $m$ (PyTorch default 0.1)

At eval time the stored running values replace $\mu_j$ and $\sigma_j^2$; $\gamma$ and $\beta$ stay. **BN then becomes a fixed per-channel affine map**, so it can be fused into the preceding FC or conv layer and adds zero overhead at test time. One input gets the same output whatever else is in the batch.

| Mode | Statistics used | Running estimates | $\gamma, \beta$ |
| --- | --- | --- | --- |
| Train | current batch | updated | learned |
| Eval | stored running | frozen | same values, fixed |


## Related

- [[Layer Normalization]]: normalizes within one example, not across the batch
- [[Switch the Model to Evaluation Mode When Evaluating]]: makes BN use its stored statistics
- [[Vanishing Gradient Problem]]
- [[Exploding Gradient Problem]]
- [[Residual Connections]]
- [[ResNet]]: BN after every conv layer
- [[Regularization]]
- [[Dropout]]: another layer with its own evaluation rule
- [[Activation Functions]]
- [[Data Preprocessing]]: input normalization, done once
- Flower Classifier Running Example
- [[Gradient Descent]]: mini-batch methods

## Sources

- Sep 14 Lecture Account
- [[Block 3 Slides]]
- [[Block 1 Slides]]
- [[Block 4 Slides]]
- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
