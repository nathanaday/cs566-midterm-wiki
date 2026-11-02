---
description: "Methods that keep a model from fitting noise in the training data: a penalty term λR(W) added to the data loss (L2, L1, elastic net), or randomness during training that evaluation removes (dropout, DropConnect, stochastic depth, cutout, mixup)."
aliases: [L1 regularization, L2 regularization, Lasso, Ridge regression, Weight penalty, Elastic net]
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

| Symptom                                          | Remedy                                                                                    |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Train good, validation poor; data is the limit   | More or better data: improve coverage, inspect labels and duplicates                      |
| Train good, validation poor; data fixed          | [[Data Augmentation]] or weight decay: task-appropriate transforms and constraints        |
| Train good, validation poor; architecture allows | [[Dropout]] or [[Early Stopping]], when they fit the architecture and validation protocol |
| Train and validation both poor                   | Underfitting: lower $\lambda$ or add capacity                                             |

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
