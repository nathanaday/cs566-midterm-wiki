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
subject: 3 Training
---

## Definition

Regularization keeps a model from fitting the training data too well. Two families: add a penalty $\lambda R(W)$ to the data loss, or add randomness during training that evaluation removes. $\lambda$ is a hyperparameter; pick it on validation data, since the training loss always prefers $\lambda = 0$.

**Regularized loss.**

$$L(W) = \frac{1}{N} \sum_{i=1}^{N} L_i(f(x_i, W), y_i) + \lambda R(W)$$

**Gradient.**

$$\nabla_W L(W) = \frac{1}{N} \sum_{i=1}^{N} \nabla_W L_i(x_i, y_i, W) + \lambda \nabla_W R(W)$$

### Weight Penalties

| Name | $R(W)$ | $\nabla_W(\lambda R)$ | Effect on weights |
| --- | --- | --- | --- |
| L2 (weight decay, ridge) | $\sum_{k,l} W_{k,l}^2$ | $2\lambda W$ | Shrinks all by a fraction; spreads weight evenly; never exactly zero |
| L1 (lasso) | $\sum_{k,l} \lvert W_{k,l} \rvert$ | $\lambda\, \mathrm{sign}(W)$ | Constant pull to zero; weights the data loss cannot overcome stay at zero; sparse |
| Elastic net | $\sum_{k,l} \beta W_{k,l}^2 + \lvert W_{k,l} \rvert$ | $2\lambda\beta W + \lambda\, \mathrm{sign}(W)$ | Both |

**Ridge and lasso in least squares.** When $A^T A$ is not invertible the penalty picks one solution among many, biased toward small $\beta$:

$$\hat{\beta}_{\text{ridge}} = \arg\min_\beta \sum_{i=1}^{n} (Y_i - X_i\beta)^2 + \lambda \lVert \beta \rVert_2^2$$

$$\hat{\beta}_{\text{lasso}} = \arg\min_\beta \sum_{i=1}^{n} (Y_i - X_i\beta)^2 + \lambda \lVert \beta \rVert_1$$

- Constant L2 norm is a circle; constant L1 norm is a diamond, so lasso lands on corners and zeroes coordinates. See [[L1 Regularization and Feature Selection]].
- An L0 penalty would be ideal but is non-convex.
- Ridge (Tikhonov) equals weight decay under plain SGD, not under the decoupled form in AdamW.
- Why regularize: express preferences over weights, keep the model simple for test data, add curvature for [[Optimization]].
- On a [[Neural Networks|neural network]], sum the penalty over every weight matrix. Larger $\lambda$ gives a smoother decision boundary.

**L2 example** ($\lambda = 0.2$, both vectors have data loss 0.4):

- $A = (3, 0)$: $J = 0.4 + 0.2 \cdot 9 = 2.2$
- $B = (2, 1)$: $J = 0.4 + 0.2 \cdot 5 = 1.4$, so L2 prefers the spread-out $B$
- L1 ties them: $3 + 0 = 2 + 1 = 3$

> [!warning] Exam trap
> L1 deletes weights; L2 only shrinks them. Read $\lambda$ and any factor of $\frac{1}{2}$ from the definition: $\frac{1}{2}\lambda \lVert W \rVert^2$ has gradient $\lambda W$, not $2\lambda W$.

### Training Randomness, Full Model at Test

Training adds randomness or removes part of the model or input; testing uses the full model or input. The network cannot depend on one unit, connection, layer, or image region.

| Method | Training | Testing |
| --- | --- | --- |
| [[Dropout]] | Zero random hidden activations | Full network, scaled |
| [[Batch Normalization]] | Normalize with batch statistics | Running statistics |
| [[Data Augmentation]] | Random transforms of the input | Fixed transform or averaging protocol |
| DropConnect | Zero random weights (connections) | All connections |
| Stochastic depth | Skip random [[Residual Connections|residual blocks]]; the shortcut carries the signal | All layers |
| Cutout | Zero random image regions | Full image |
| Mixup | Train on random blends of image pairs; blend the labels the same way | Original images |
| Fractional max pooling | Named in the course list only | |

- [[Dropout]] masks a unit's output, so all its outgoing connections go at once; DropConnect masks single connections.
- Cutout suits small datasets like CIFAR, less so ImageNet.
- Mixup: 40% cat plus 60% dog gives the target cat 0.4, dog 0.6.

### Train vs. Eval Mode

Each method has its own evaluation rule (the Testing column above). Decide the evaluation protocol before comparing models, or a score difference can come from the protocol instead of the models. See [[Switch the Model to Evaluation Mode When Evaluating]].

> [!warning] Exam trap
> A model left in train mode at evaluation still drops units and uses batch statistics, so its validation score is wrong even though the weights are right.

### Diagnose, Then Choose

Check the gap between training and validation performance before picking a regularizer, then compare one controlled change at a time. See [[Overfitting and Underfitting]].

| Symptom | Remedy |
| --- | --- |
| Train good, validation poor; data is the limit | More or better data: improve coverage, inspect labels and duplicates |
| Train good, validation poor; data fixed | [[Data Augmentation]] or weight decay: task-appropriate transforms and constraints |
| Train good, validation poor; architecture allows | [[Dropout]] or [[Early Stopping]], when they fit the architecture and validation protocol |
| Train and validation both poor | Underfitting: lower $\lambda$ or add capacity |

## Related

- [[L1 Regularization and Feature Selection]]: why L1 zeroes weights and L2 only shrinks them
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
- [[Switch the Model to Evaluation Mode When Evaluating]]: the evaluation rule for the randomness methods

## Sources

- [[Block 1 Slides]]
- [[Block 3 Slides]]
- [[Block 2 Slides]]
- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
