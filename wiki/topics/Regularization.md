---
description: "Methods that keep a model from fitting noise in the training data: a penalty term λR(W) added to the data loss (L2, L1, elastic net), or randomness during training that evaluation removes (dropout, DropConnect, stochastic depth, cutout, mixup)."
aliases:
  - L1 regularization
  - L2 regularization
  - Lasso
  - Ridge regression
  - Elastic net
  - Weight penalty
  - L1 penalty
  - L2 penalty
  - Tikhonov regularization
  - Linear model regularization
  - Regularization penalty
  - DropConnect
  - Stochastic Depth
  - Cutout
  - Mixup
  - Fractional Max Pooling
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
  - "[[Block 2 Slides]]"
  - "[[Block 7 Slides]]"
  - "[[F26-midterm-review-234p]]"
---

## Definition

Regularization adds a penalty to the loss so the model does not fit the training data too well ([[Block 1 Slides]], pp. 293–296):

$$L(W) = \frac{1}{N} \sum_{i=1}^{N} L_i(f(x_i, W), y_i) + \lambda R(W)$$

- Data loss, "fitting to the data": "Model predictions should match training data."
- Regularization, "preferring a simple model": "Prevent the model from doing too well on training data."
- $\lambda$ is the regularization strength, a hyperparameter. "Regularization strength is a hyperparameter, so validation data decides whether it helps generalization" ([[F26-midterm-review-234p]], p. 112).

The gradient of this loss is the average gradient of the data loss plus $\lambda \nabla_W R(W)$ ([[F26-midterm-review-234p]], p. 108, a copy of Block 7 slide 88):

$$\nabla_W L(W) = \frac{1}{N} \sum_{i=1}^{N} \nabla_W L_i(x_i, y_i, W) + \lambda \nabla_W R(W)$$

Block 7 states the purpose in one line: "The training loss rewards fitting labels. A penalty also constrains the weights." Objective = data loss + λ × weight penalty. "λ controls the tradeoff. Choose it using validation data" ([[Block 7 Slides]], p. 138). [[F26-midterm-review-234p]] repeats this slide (p. 125).

A second family of regularizers adds randomness during training and uses the full model at test time. [[Dropout]] is the main example. See [Training randomness, full model at test](#Training randomness, full model at test).

## Explanation

### Toy example

The slides fit the same points with a curve that passes through every point ($f_1$) and a straight line ($f_2$). New points show that $f_2$ is better. "Regularization pushes against fitting the data too well so we don't fit noise in the data" ([[Block 1 Slides]], pp. 288–290). The slides quote Ockham's razor: "Among competing hypotheses, the simplest is the best" ([[Block 1 Slides]], p. 291).

### Common regularizers

| Name | $R(W)$ |
| --- | --- |
| L2 | $\sum_k \sum_l W_{k,l}^2$ |
| L1 | $\sum_k \sum_l \lvert W_{k,l} \rvert$ |
| Elastic net (L1 + L2) | $\sum_k \sum_l \beta W_{k,l}^2 + \lvert W_{k,l} \rvert$ |

Source: [[Block 1 Slides]], p. 296. Block 7 gives the same three forms "in common use" and labels L2 "(Weight decay)". It adds $\lambda R(W)$ to the multiclass SVM loss $L = \frac{1}{N} \sum_{i=1}^{N} \sum_{j \neq y_i} \max(0, f(x_i; W)_j - f(x_i; W)_{y_i} + 1)$ ([[Block 7 Slides]], p. 139). It also states: "L2 penalty = sum of squared weights" (p. 138). [[F26-midterm-review-234p]] repeats both slides (pp. 125-126). The slides list more complex methods to revisit later: dropout, [[Batch Normalization|batch normalization]], stochastic depth, and fractional pooling ([[Block 1 Slides]], p. 297). Block 7 covers them below.

### L2 example: equal data loss, different norms

The midterm review adds a worked example: "With equal data loss, the L2 penalty separates two weight vectors by their squared norms" ([[F26-midterm-review-234p]], p. 127). The objective is $J(w) = \text{data loss} + \lambda \sum_i w_i^2$ with $\lambda = 0.2$ (p. 127):

| Weights | Data loss | Squared norm | $J(w)$ |
| --- | --- | --- | --- |
| A = (3, 0) | 0.4 | 9 | 0.4 + 0.2 × 9 = 2.2 |
| B = (2, 1) | 0.4 | 5 | 0.4 + 0.2 × 5 = 1.4 |

The slide adds: "Read lambda and any factor of one half from the definition; validation judges generalization" (p. 127).

Synthesis: the L2 objective prefers B, which spreads the weight over both entries. An L1 penalty would not separate these two vectors: |3| + |0| = 3 and |2| + |1| = 3.

### L1 vs. L2

Credited to CMU 10701 ([[Block 1 Slides]], p. 298). Solve $\min_\beta (A\beta - Y)^T (A\beta - Y) + \lambda\, \text{pen}(\beta)$:

- Ridge regression: $\text{pen}(\beta) = \lVert \beta \rVert_2^2$. The set of $\beta$ with constant L2 norm is a circle.
- Lasso: $\text{pen}(\beta) = \lVert \beta \rVert_1$. The set with constant L1 norm is a diamond. "Lasso (l1 penalty) results in sparse solutions – vector with more zero coordinates." The slide adds that this is good for high-dimensional problems and gives an interpretable solution.
- An L0 penalty would be ideal, but the optimization becomes non-convex.

### Linear models: when $A^T A$ is not invertible

Credited to CMU 10601 ([[Block 2 Slides]], p. 100). The least-squares solution in [[Optimization]] needs $A^T A$ to be invertible. If it is not, the system has $r$ equations and $p$ unknowns and is underdetermined. It has many feasible solutions, so the solution must be constrained further. One constraint biases the solution toward small values of $\beta$, so that small changes in input do not give large changes in output. The two penalized estimates are:

$$\hat{\beta}_{MAP} = \arg\min_\beta \sum_{i=1}^{n} (Y_i - X_i\beta)^2 + \lambda \lVert \beta \rVert_2^2 \quad \text{(ridge regression, L2 penalty)}$$

$$\hat{\beta}_{MAP} = \arg\min_\beta \sum_{i=1}^{n} (Y_i - X_i\beta)^2 + \lambda \lVert \beta \rVert_1 \quad \text{(lasso, L1 penalty)}$$

A note on naming: the L2 penalty is called ridge in least squares and is a special case of Tikhonov regularization. It matches weight decay under plain SGD, but not under the decoupled form in AdamW ([[Block 2 Slides]], p. 100).

### Why regularize

Also credited to CMU 10701 ([[Block 1 Slides]], p. 299):

- Express preferences over weights.
- Make the model simple so it works on test data.
- Improve optimization by adding curvature.

### On a neural network

[[Block 3 Slides]] shows the same formula on a neural network with $\lambda \in \{0.001, 0.01, 0.1\}$, under the title "Larger Model Capacity May Overfit – Need to Regularize them". A larger $\lambda$ gives a smoother decision boundary ([[Block 3 Slides]], p. 96). The next slides add the penalty for each weight matrix to a network's total loss ([[Block 3 Slides]], p. 102). See [[Neural Networks]]. Regularization is also a hyperparameter choice in Model Selection for neural networks ([[Block 2 Slides]], p. 94).

### Training randomness, full model at test

Block 7 shows a common pattern. Training adds randomness or removes part of the model or the input. Testing uses the full model or the full input. Each slide adds one method to a growing list of examples: Dropout, Batch Normalization, Data Augmentation, DropConnect, Fractional Max Pooling, Stochastic Depth, Cutout / Random Crop, and Mixup ([[Block 7 Slides]], pp. 166–169).

| Method | Training | Testing | Source |
| --- | --- | --- | --- |
| [[Dropout]] | Set some hidden activations to zero at random. | Turn off the mask; apply the chosen scaling convention. | pp. 140–153, 165 |
| DropConnect | "Drop connections between neurons (set weights to 0)". | "Use all the connections". | p. 166; Wan et al., "Regularization of Neural Networks using DropConnect", ICML 2013 |
| Stochastic depth | "Skip some layers in the network". | Use all the layers. | p. 167; Huang et al., "Deep Networks with Stochastic Depth", ECCV 2016 |
| Cutout | "Set random image regions to zero". | "Use full image". | p. 168; DeVries and Taylor, "Improved Regularization of Convolutional Neural Networks with Cutout", arXiv 2017 |
| Mixup | "Train on random blends of images". | "Use original images". | p. 169; Zhang et al., "mixup: Beyond Empirical Risk Minimization", ICLR 2018 |

Notes on the methods:

- **DropConnect** zeroes weights, not activations. Synthesis: dropout masks a unit's output, so it removes all of the unit's outgoing connections at once. DropConnect masks single connections (p. 166).
- **Stochastic depth.** The figure shows a stack of residual blocks. In training, some blocks are grayed out, and the identity shortcut carries the signal past them (p. 167). See [[Residual Connections]] and [[ResNet]]. The slide's printed text is "Use all the layer"; this topic reads it as "all the layers".
- **Cutout** "works very well for small datasets like CIFAR, less common for large datasets like ImageNet" (p. 168). The slide pairs it with random crop in the list: "Cutout / Random Crop". Random crops are covered in [[Data Augmentation]].
- **Mixup** blends the pixels of pairs of training images at random, for example 40% cat and 60% dog. The target label is blended in the same way: cat: 0.4, dog: 0.6 (p. 169). The slide also shows a U-shaped curve on [0, 1] with no label or caption. The slides do not say what it plots.
- **Fractional Max Pooling** appears in the example list from p. 167 onward, but Block 7 has no slide that explains it. [[Block 1 Slides]], p. 297, also names "fractional pooling" only in a list.
- [[Batch Normalization]] and [[Data Augmentation]] are in the same list. Their own topics explain them.

### Each method has its own evaluation rule

A course schematic states: "Each method has its own evaluation rule" ([[Block 7 Slides]], p. 165):

| Method | Evaluation rule |
| --- | --- |
| Dropout | "Turn off the random mask; apply the chosen scaling convention." |
| BatchNorm | "Use stored training statistics in the usual running-statistics mode." |
| Augmentation | "Use a fixed evaluation transform, or a predefined averaging protocol." |

The slide ends with a rule: "Decide the evaluation protocol before comparing models" (p. 165). Synthesis: if two models use different evaluation rules, a difference in their scores can come from the protocol and not from the models. See [[Switch the Model to Evaluation Mode When Evaluating]].

### Diagnose, then choose

Block 7 tells the reader to "return to the gap between training and validation performance" before choosing a regularizer ([[Block 7 Slides]], p. 170):

| Option | When to use it |
| --- | --- |
| More or better data | "Improve coverage and inspect labels or duplicates." |
| Augmentation / weight decay | "Test task-appropriate transformations and constraints." |
| Dropout / early stopping | "Use when they fit the architecture and validation protocol." |

"Compare one controlled change at a time" (p. 170). See [[Overfitting and Underfitting]], [[Data Augmentation]], and [[Early Stopping]].

### Why it matters

Regularization is the main tool in this lecture against [[Overfitting and Underfitting]]. Synthesis: a penalty puts Ockham's razor into the objective that [[Optimization]] minimizes. For linear least squares it also picks one answer when the normal equation has many. The training-randomness methods reach a similar goal without a penalty term: the network cannot depend on one unit, connection, layer, or image region.

## Related

- [[L1 Regularization and Feature Selection]]: why the L1 penalty zeroes weights and the L2 penalty only shrinks them
- [[Dropout]]
- [[Loss Functions]]
- [[Overfitting and Underfitting]]
- [[Optimization]]
- Model Selection
- [[Linear Classification]]
- [[Neural Networks]]
- [[Batch Normalization]]
- [[Data Augmentation]]
- [[Early Stopping]]
- [[Residual Connections]]
- [[Switch the Model to Evaluation Mode When Evaluating]]: the rule for the training-randomness methods at evaluation

## Sources

- [[Block 1 Slides]], pp. 288–299
- [[Block 3 Slides]], pp. 96, 102
- [[Block 2 Slides]], pp. 94, 100
- [[Block 7 Slides]], pp. 138–139, 165–170
- [[F26-midterm-review-234p]], pp. 108, 112, 125–127
