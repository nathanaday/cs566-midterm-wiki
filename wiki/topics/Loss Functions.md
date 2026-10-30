---
id: con-mq9wak
type: topic
kind: concept
description: A loss function L converts a model's scores into one number that training reduces, measuring how well learned weights W map X to Y against the ground truth; CSCI 566 covers hinge, L1, L2 (squared), cross-entropy, and 0/1 loss, shows that the choice of loss changes which W wins, and shows why a 0/1 mistake count gives no gradient.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Loss function
  - Hinge loss
  - Cross-entropy loss
  - L1 loss
  - L2 loss
  - Empirical risk minimization
  - Squared loss
  - Squared error loss
  - Squared error
  - 0/1 loss
  - 0-1 loss
  - 0/1 mistake loss
  - Mistake count
  - Hard loss
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
  - "[[Block 2 Slides]]"
  - "[[Block 7 Slides]]"
  - "[[F26-midterm-review-234p]]"
up:
  - "[[Function Approximation]]"
---

> [!concept] Concept
> 5 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Function Approximation]]

## Definition

A loss function $L$ measures how well a learned $W$ maps $X$ to $Y$, compared with the ground truth $y^*$. Optimization finds the $W$ that minimizes $L$ ([[Block 1 Slides]], pp. 258–259, 339; [[Block 2 Slides]], p. 27).

The midterm review gives the loss its place in training: "A loss converts model scores into a number that training tries to reduce." "Training turns a score into a loss, a loss into gradients, and gradients into parameter updates." ([[F26-midterm-review-234p]], p. 78)

## Explanation

### Four losses

Given $f(x; W, b)$ and examples $(x_i, y_i)$, the slides define four losses to minimize ([[Block 1 Slides]], pp. 276–280). The formulas follow the slides' notation.

**Hinge loss** (p. 277)

$$Loss = \frac{1}{N} \sum_{i=1}^{N} \sum_{j \neq y_i} \max\left(0,\ 1 + f(x_i; W, b)_j - f(x_i; W, b)_{y_i}\right)$$

**L1 loss** (p. 278)

$$Loss = \frac{1}{N} \sum_{i=1}^{N} \lVert y_i - f(x_i; W, b) \rVert_1$$

**L2 loss** (p. 279)

$$Loss = \frac{1}{N} \sum_{i=1}^{N} \lVert y_i - f(x_i; W, b) \rVert_2^2$$

**Cross-entropy loss** (p. 280)

$$Loss = -\frac{1}{N} \sum_{i=1}^{N} \hat{y}_i \log P(y_i = j \mid x_i), \qquad P(y_i = j \mid x_i) = \frac{e^{f(x_i; W, b)}}{\sum_{j=1}^{C} e^{f(x_j; W, b)}}$$

"Each loss function penalizes differently" ([[Block 1 Slides]], p. 281).

### Squared loss and its slope

For one numeric prediction $\hat{y}$ and target $t$, the squared loss is $L = (\hat{y} - t)^2$. The L2 loss above averages this over examples. [[F26-midterm-review-234p]] returns to the Block 3 network of [[Forward Propagation]]: $\hat{y} = 1$ and target 2, so $L = (1 - 2)^2 = 1$. "Prediction and target meet at the output." "The loss measures the output error before any parameter is updated." (p. 48)

With $t = 2$, the deck tabulates the loss and its local slope (p. 81):

| $\hat{y}$ | $L$ | $\partial L / \partial \hat{y}$ |
| --- | --- | --- |
| 0 | 4 | −4 |
| 1 | 1 | −2 |
| 3 | 1 | +2 |

"A negative slope calls for raising ŷ a little; a positive slope calls for lowering it." (p. 81)

With the error $e = \hat{y} - t$, $\partial L / \partial \hat{y} = 2e$ (p. 89). For $L = e^2$ the slope is $2e$. For $L = \tfrac{1}{2}e^2$ it is $e$ (p. 96). [[Backpropagation]] starts from this slope.

Synthesis: the factor ½ only multiplies the gradient by one half. It does not move the minimum, which stays at $\hat{y} = t$.

### Why a 0/1 loss gives no gradient

The 0/1 loss counts a mistake as 1 and a correct prediction as 0. [[Model Evaluation]] uses it, $\mathbb{1}(y \neq \hat{y})$, for the classification error rate. The midterm review shows why training cannot use it ([[F26-midterm-review-234p]], pp. 79–80). A model outputs a real-valued score $s$ (not a probability) and predicts spam when $s \geq 0$. One email is known spam, so the target is $y = 1$ (p. 79):

| Score $s$ | Prediction (threshold 0) | 0/1 loss |
| --- | --- | --- |
| −2 | Not spam | 1 |
| −1 | Not spam | 1 |
| +2 | Spam | 0 |

"Moving the score from −2 to −1 brings it closer to spam, yet the 0/1 loss stays at 1." (p. 79)

As a function of $s$, the loss has flat regions with slope 0 and a jump at $s = 0$ where the slope is undefined. "A small score change within either flat region leaves the hard loss unchanged." (p. 80)

Synthesis: gradient descent moves the weights by the slope of the loss. A slope of 0 almost everywhere gives no step. So training minimizes a loss with a useful slope, such as squared, hinge, or cross-entropy loss, and the 0/1 loss stays an evaluation measure.

### Worked example: softmax and cross-entropy for the next token

Given the context "The light is", a linear head gives one logit per vocabulary token: $z = Wh + b$ ([[Block 3 Slides]], p. 98). For three tokens (red, blue, green) with logits $(\ln 2, 0, 0)$, softmax gives $e^z = (2, 1, 1)$, sum 4, and $p = (0.5, 0.25, 0.25)$ ([[Block 3 Slides]], p. 99).

The observed token "red" is the target: $L = -\ln 0.5 = 0.693$ ([[Block 3 Slides]], p. 100). The gradient with respect to the logits is $\partial L / \partial z = p - y = (-0.5, +0.25, +0.25)$. One step $z \leftarrow z - 0.4(p - y)$ moves the probabilities to (0.574, 0.213, 0.213) and lowers the loss from 0.693 to 0.554. The slide notes that it steps the logits directly, while training updates the network parameters ([[Block 3 Slides]], p. 101).

### Worked example: one flower prediction

[[Block 7 Slides]] recaps cross-entropy with the course's flower classifier (p. 13; see Flower Classifier Running Example). The true label is rose. Cross-entropy is $-\ln P(\text{rose})$, the negative log of the probability assigned to the true label (p. 13). The slide calls both predictions illustrative.

| Prediction | Daisy | Rose | Tulip | Loss |
| --- | --- | --- | --- | --- |
| Before: daisy | 0.60 | 0.30 | 0.10 | 1.20 |
| Improved: rose | 0.20 | 0.70 | 0.10 | 0.36 |

"Higher probability for the correct label gives lower loss" ([[Block 7 Slides]], p. 13).

Synthesis: only the probability of the true label enters the loss. $-\ln 0.30 \approx 1.204$ and $-\ln 0.70 \approx 0.357$, which round to the slide's values. The daisy probability falls and the tulip probability stays the same, but neither one changes the loss directly.

### Empirical risk minimization

The optimal predictor minimizes the expected loss: $f^* = \arg\min_f \mathbb{E}[(f(X) - Y)^2]$. Learning uses the empirical mean over training data instead ([[Block 1 Slides]], p. 282):

$$\hat{f}_n = \arg\min_{f \in \mathcal{F}} \frac{1}{n} \sum_{i=1}^{n} (f(X_i) - Y_i)^2$$

By the law of large numbers, the empirical mean of the loss approaches the expected loss as $n \to \infty$. "This explains why we could learn from many training samples to approximate the optimal predictor" ([[Block 1 Slides]], p. 282).

### Loss on a neural network

[[Block 3 Slides]] plugs a two-layer network into a hinge loss with L2 regularization, credited to Stanford CS 231n ([[Block 3 Slides]], p. 102):

- Score: $s = W_2 \max(0, W_1 x)$
- Data loss: $L_i = \sum_{j \neq y_i} \max(0, s_j - s_{y_i} + 1)$
- Total loss: $L = \frac{1}{N}\sum_i L_i + \lambda R(W_1) + \lambda R(W_2)$, with $R(W) = \sum_k W_k^2$

See [[Regularization]] and [[Backpropagation]].

### The choice of loss changes the answer

One car image, ground truth (Cat, Car, Airplane) = (0, 1, 0). Two weight matrices give different outputs ([[Block 1 Slides]], pp. 284–287):

| Weights | Output | L1 loss | L2 loss |
| --- | --- | --- | --- |
| $W_1$ | (0, 1.2, 0) | **0.2** | 0.04 |
| $W_2$ | (0.07, 0.9, 0.05) | 0.22 | **0.0174** |

L1 prefers $W_1$. L2 prefers $W_2$. "Loss function matters!" ([[Block 1 Slides]], p. 287).

### Why it matters

Synthesis: the loss defines what "better" means before training starts. Two losses can rank the same models in opposite order. Minimizing a loss also rewards any feature that lowers it, including a surface cue; see Shortcut Learning.

## Related

- [[Optimization]]
- [[Gradient Descent]]
- [[Backpropagation]]: the backward pass starts from $\partial L / \partial \hat{y}$
- [[Forward Propagation]]: the Block 3 network behind the squared-loss example
- [[Regularization]]
- [[Perceptron]]
- [[Model Evaluation]]: 0-1 and squared loss for evaluation
- Classification Metrics: accuracy is one minus the mean 0/1 loss
- Autoregressive Language Modeling: the next token as a classification
- Flower Classifier Running Example: the course example behind the flower loss table

## Sources

- [[Block 1 Slides]], pp. 258–287, 339
- [[Block 3 Slides]], pp. 98–102
- [[Block 2 Slides]], p. 27
- [[Block 7 Slides]], p. 13
- [[F26-midterm-review-234p]], pp. 48, 78–81, 89, 96
