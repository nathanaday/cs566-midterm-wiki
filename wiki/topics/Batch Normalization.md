---
id: con-an15dx
type: topic
kind: concept
description: A layer that normalizes each channel of a batch to zero mean and unit variance and then applies a learned scale and shift; it makes deep networks easier to train, and it computes a different function in training and eval mode.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - BatchNorm
  - Batch Norm
  - BN
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources:
  - "[[Block 3 Slides]]"
  - "[[Block 1 Slides]]"
  - "Sep 14 Lecture Account"
  - "[[Block 4 Slides]]"
  - "[[Block 7 Slides]]"
  - "[[F26-midterm-review-234p]]"
up:
  - "[[Neural Network Training]]"
---

> [!concept] Concept
> 6 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Neural Network Training]]

## Definition

Batch normalization (BN) normalizes each dimension of a batch of activations to zero mean and unit variance, then applies a learned scale and shift ([[Block 4 Slides]], pp. 169-172, citing Ioffe and Szegedy, 2015).

[[Block 3 Slides]] lists it under "Fixing Vanishing Gradients": "the idea is to fix the range". "During training this standardizes each channel using mini-batch statistics, then applies a learned scale and shift, so the output need not have mean 0 and variance 1. It often stabilizes optimization; reducing internal covariate shift was the original motivation, not an established explanation" (p. 232).

[[Block 7 Slides]] places BN inside the network: "Input preprocessing happens once. Hidden activations change during training." BN takes the hidden activations, normalizes them, and learns a scale and shift before the next layer. "Normalization also changes the optimization behavior" (p. 24). [[F26-midterm-review-234p]] repeats this slide (p. 116). See [[Data Preprocessing]].

The Sep 14 lecture named batch normalization, with appropriate activation functions, as one of two fixes for the [[Vanishing Gradient Problem]] (Sep 14 Lecture Account, § Vanishing gradients). The week 1 deck lists it with dropout, stochastic depth, and fractional pooling as more complex regularization methods ([[Block 1 Slides]], p. 297; see [[Regularization]]).

## Explanation

### The problem it solves

For a layer $y = Wx$, optimization is hard in two cases ([[Block 4 Slides]], p. 168):

- The inputs are not centered around zero, so the layer needs a large bias.
- The inputs have a different scale per element, so the entries of $W$ must vary a lot.

The idea is to force the inputs of each layer to be "nicely scaled" (p. 168): "you want zero-mean unit-variance activations? just make them so." Normalization is a vanilla differentiable function (p. 169).

### Training-time computation

For an input $x$ of shape $N \times D$, BN computes the mean $\mu_j$ and the variance $\sigma_j^2$ of each channel $j$ over the batch ([[Block 4 Slides]], p. 170). The variance is the biased one (p. 177):

$$\mu_j = \frac{1}{N}\sum_{i=1}^{N} x_{i,j} \qquad \sigma_j^2 = \frac{1}{N}\sum_{i=1}^{N} (x_{i,j} - \mu_j)^2$$

$$\hat{x}_{i,j} = \frac{x_{i,j} - \mu_j}{\sqrt{\sigma_j^2 + \epsilon}} \qquad y_{i,j} = \gamma_j \hat{x}_{i,j} + \beta_j$$

- $\epsilon$ is a small constant that prevents division by 0 (p. 170).
- Zero mean and unit variance may be too hard a constraint. So $\gamma$ and $\beta$ (shape $D$) are learned. Learning $\gamma = \sigma$ and $\beta = \mu$ recovers the identity function (pp. 171-172).

[[Block 7 Slides]] gives the same computation. It first shows plain normalization, $\hat{x}^{(k)} = (x^{(k)} - \mathrm{E}[x^{(k)}]) / \sqrt{\mathrm{Var}[x^{(k)}]}$ (pp. 25, 29). It computes "the empirical mean and variance independently for each dimension", one column of the $N \times D$ batch $X$ (p. 28). Then it shows the algorithm of Ioffe and Szegedy (2015) for a mini-batch $\mathcal{B} = \{x_{1 \ldots m}\}$: mini-batch mean, mini-batch variance with $1/m$, normalize with $\epsilon$, and scale and shift $y_i = \gamma \hat{x}_i + \beta$, with $\gamma$ and $\beta$ learned (p. 30). [[F26-midterm-review-234p]] repeats these slides (pp. 119-120).

### A worked example

One feature across four examples: 2, 4, 6, and 8 ([[Block 7 Slides]], p. 26).

| Input | 2 | 4 | 6 | 8 |
| --- | --- | --- | --- | --- |
| Subtract mean 5 | −3 | −1 | 1 | 3 |
| Divide by √5 | −1.34 | −0.45 | 0.45 | 1.34 |

The variance is 5. The example sets $\gamma = 1$ and $\beta = 0$, and omits $\epsilon$. "Training learns γ and β after this normalization" (p. 26). [[F26-midterm-review-234p]] repeats this slide (p. 117).

### A worked example of the two stages

"Batch normalization first standardizes with statistics, then applies a learned scale and shift" ([[F26-midterm-review-234p]], p. 123). The slide takes one input $x = 7$ with $\mu = 3$, $\sigma^2 = 4$, and $\epsilon = 0$ (p. 123):

1. Standardize: $\hat{x} = (7 - 3) / \sqrt{4} = 2$.
2. Scale and shift with $\gamma = 0.5$ and $\beta = -1$: $y = 0.5 \times 2 - 1 = 0$.

### What normalization does not do

"Centering and scaling do not force an arbitrary distribution to become Gaussian." BN subtracts the mean and divides by a scale estimate, but "the resulting values need not follow a bell-shaped distribution". "BatchNorm then learns an additional scale and shift" ([[Block 7 Slides]], p. 27). [[F26-midterm-review-234p]] repeats this slide (p. 118).

### Test time

At test time, $\mu$ and $\sigma^2$ are running averages of values seen during training. BN then becomes a linear operator that can be fused with the previous fully-connected or conv layer ([[Block 4 Slides]], p. 173). It adds zero overhead at test time (p. 175).

[[Block 7 Slides]] states the same thing: at test time "the mean and variance are not computed based on the batch". The layer uses "stored running means and variances from training" (p. 32). The deck contrasts the two modes (p. 34):

- During training: use mini-batch statistics, update the running estimates, and learn the scale and shift.
- During evaluation: "usually use stored running statistics", and keep the same learned scale and shift.

The deck's reason: "The flower classifier may receive one new photo at a time" (p. 34; see Flower Classifier Running Example). Its rule: "Switch the model to evaluation mode when evaluating" (p. 34). Later the deck lists BN with [[Dropout]] and [[Data Augmentation]]. "Each method has its own evaluation rule." For BN: "Use stored training statistics in the usual running-statistics mode." "Decide the evaluation protocol before comparing models" (p. 165).

[[F26-midterm-review-234p]] repeats the slides of pp. 32 and 34 (pp. 121-122). It adds: "In standard evaluation, stored running mean and variance replace the batch statistics; γ and β stay" (p. 123). Its summary of Block 7 states: "Normalization layers can behave differently in training mode and evaluation mode" (p. 112). See [[Switch the Model to Evaluation Mode When Evaluating]].

The review then shows why the stored statistics matter: "Stored running statistics give one photo the same normalized activation, whatever else is in the batch" ([[F26-midterm-review-234p]], p. 124). The same photo, $x = 7$, in three cases (p. 124):

| Mode | Batch | Statistics | Normalized value |
| --- | --- | --- | --- |
| Training mode (wrong at evaluation) | [7, 3] | $\mu = 5$, $\sigma^2 = 4$ | $(7 - 5) / \sqrt{4} = 1$ |
| Training mode (wrong at evaluation) | [7, 11] | $\mu = 9$, $\sigma^2 = 4$ | $(7 - 9) / \sqrt{4} = -1$ |
| Evaluation mode | either | stored running mean 3, variance 4 | $(7 - 3) / 2 = 2$ |

The slide's assumptions: "Illustrative numbers; epsilon 0, gamma 1, beta 0, population variance; intermediate activation only" (p. 124). Synthesis: this is the small-batch pitfall below, seen at evaluation. In training mode, the other members of the batch change the output for one input.

### Placement

BN usually comes after a fully-connected or conv layer and before the nonlinearity ([[Block 4 Slides]], p. 174). [[ResNet]] puts BN after every conv layer (p. 218). The pre-activation residual block puts BN and ReLU before each conv (p. 223; see [[Residual Connections]]).

[[Block 7 Slides]] gives the same rule: "Usually added after convolutional layers or fully connected layers", "before non-linearities". Its figure repeats 3 x 3 Conv, Batch Norm, and ReLU twice, from Johnson, Alahi, and Fei-Fei (ECCV 2016) (p. 33).

### Benefits

[[Block 4 Slides]] lists these benefits (p. 175):

- Deep networks are much easier to train.
- Gradient flow improves.
- Higher learning rates and faster convergence are possible.
- The network is more robust to initialization.
- It acts as regularization during training.
- It adds zero overhead at test time.

[[Block 7 Slides]] states them with more care, as "Possible benefits, depending on the training setup" (p. 31):

- It can improve optimization and gradient flow.
- It can allow a higher learning rate.
- It can reduce sensitivity to initialization.
- Batch statistics can add training-time noise.

The two lists agree in content. Block 4 states the benefits as facts. Block 7 states them as possible and dependent on the setup. The Block 7 slides cite Ioffe and Szegedy (2015) and Santurkar et al. (2018) for BN (pp. 24, 27, 34, 35). They do not say what Santurkar et al. found. The review slides repeat these two citations (pp. 116, 122).

Ioffe and Szegedy (ICML 2015) report the regularizing effect in some settings, not as a universal rule ([[Block 4 Slides]], p. 177). [[Block 3 Slides]] says the reason it works is open: internal covariate shift was the motivation, "not an established explanation" (p. 232).

The slides name three fixes for unusable gradients: "avoid saturation, control scale, and preserve an identity path for the gradient". Normalization is the second: "Keeping signals in range helps gradients stay usable". "Residual paths plus normalization are common in deep models" ([[Block 3 Slides]], p. 233). See [[Residual Connections]].

Synthesis: BN keeps the inputs of sigmoid and tanh units near 0, where their derivative is largest. The training-time noise from batch statistics (Block 7, p. 31) is one plausible source of the regularizing effect that Block 4 lists.

### Pitfalls

BN behaves differently during training and testing. The slides call this a very common source of bugs ([[Block 4 Slides]], p. 175).

- **One layer, two functions.** `bn.train()` uses the statistics of the current batch and updates the running estimates. `bn.eval()` uses the stored running estimates, so the same $x$ can give a different output. With `bn = nn.BatchNorm1d(1)` and `x = [[1.],[3.]]`, train mode gives `[-1.0, 1.0]` and eval mode gives `[0.7628, 2.6697]`. The rule: "Mode is part of the function. Call model.eval() before inference." (p. 176).
- **Small batches.** For a batch of 2, $x = [1, 3]$ gives mean 2 and biased variance 1, so the normalized values are $[-1, +1]$ before scale and shift. For a batch of 1, $x = [3]$ gives variance 0, and PyTorch `BatchNorm1d` raises an error on a `[1, C]` input in training mode. "With small batches, who else is in the batch becomes part of the model." (p. 177).
- **Group Normalization.** Group Normalization (Wu and He, ECCV 2018) targets this small-batch dependence (p. 177).

### Batch normalization and layer normalization

"Both normalize activations, using different groups of values" ([[Block 7 Slides]], p. 35). BatchNorm compares one feature across the examples in a mini-batch, and is common in CNNs. LayerNorm compares features within one example or token, and is common in Transformers. "Identify which values supply the normalization statistics" (p. 35). See [[Layer Normalization]].

## Related

- [[Layer Normalization]]: normalizes within one example, not across the batch
- [[Switch the Model to Evaluation Mode When Evaluating]]: the rule that makes BN use its stored statistics
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

- Sep 14 Lecture Account, § Vanishing gradients
- [[Block 3 Slides]], pp. 232-233
- [[Block 1 Slides]], p. 297
- [[Block 4 Slides]], pp. 168-177, 218, 223
- [[Block 7 Slides]], pp. 24-35, 165
- [[F26-midterm-review-234p]], pp. 112, 116-124
