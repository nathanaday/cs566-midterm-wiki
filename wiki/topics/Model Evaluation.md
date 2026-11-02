---
description: "How CSCI 566 evaluates supervised models: test error estimates the unknown true error, the training, validation, and test splits each have one job, hyperparameters are chosen on validation data or by cross-validation, and the test set stays outside every selection loop."
aliases:
  - Evaluation of ML Algorithms
  - Error rate
  - Test error
  - ML evaluation metrics
  - Model metrics
  - Evaluation metrics
  - Hyperparameter
  - Hyperparameters
  - Train/validation/test split
  - Validation set
  - Val split
  - Cross-validation
  - Accuracy
  - Precision
  - Recall
  - F1 score
  - Precision and recall
  - Metrics for binary classification
  - k-fold cross-validation
  - 5-fold cross-validation
  - Do not tune hyperparameters on training or test data
  - Deciding hyperparameters
  - Training, validation and test splits
  - Data splits
  - Three data splits
  - Hyperparameters vs. parameters
  - Keep near-duplicate photos in the same split
  - Evaluate once on held-out test data
  - Repeated validation can overfit the selection process
  - Keep the test score outside the hyperparameter search loop
  - Keep the test set out of stopping decisions
  - Fixed stopping protocol
  - Training, validation, and test split
  - Held-out test set
  - Evaluate on the test set once, after selection
  - Evaluate once, after selection
  - Keep the test set out of model selection
  - Select by validation, test the final choice
  - Keep grouped samples in the same split
  - Split by plant
  - Group split
sources:
  - "[[Block 1 Slides]]"
  - "CSCI 566 Syllabus"
  - "[[Block 2 Slides]]"
  - "[[Block 7 Slides]]"
  - "[[F26-midterm-review-234p]]"
subject: 1 Foundations and classical machine learning
---

## Definition

Model evaluation measures how well a hypothesis $h$ predicts unseen data. The test error estimates the true error, which is the quantity we care about but cannot measure. Hyperparameters are chosen on validation data, and the test set is touched once, after every choice is final.

### Error Rate

A loss $\ell(y, \hat{y})$ scores a prediction: squared loss $(y - \hat{y})^2$ for regression, 0-1 loss $\mathbb{1}(y \neq \hat{y})$ for classification. See [[Loss Functions]].

**Error rate on a dataset.**

$$err(h, \mathcal{D}) = \frac{1}{N} \sum_{n=1}^{N} \mathbb{1}\left(y^{(n)} \neq \hat{y}^{(n)}\right)$$

| Error | Measured on | Role |
| --- | --- | --- |
| $err(h, D_{train})$ | training data | fit; low value can hide [[Overfitting and Underfitting]] |
| $err(h, D_{test})$ | held-out test data | estimate of true error |
| $err_{true}(h)$ | all possible data | the target; unknown in practice |

### Metrics by Task

| Task | Metrics |
| --- | --- |
| Regression | MSPE, MSAE, $R^2$, adjusted $R^2$ |
| Classification | accuracy, precision-recall, ROC-AUC, log-loss |
| Object detection | mAP |
| Unsupervised | Rand index, mutual information |
| Other | CV error, BLEU (NLP), revenue, latency |

Loss is the training signal; the other metrics are model specific or business specific.

### Binary Classification Metrics

**Confusion matrix.** $N = TP + TN + FP + FN$.

| | Predicted positive | Predicted negative |
| --- | --- | --- |
| Actual positive | $TP$ | $FN$ |
| Actual negative | $FP$ | $TN$ |

**Accuracy.**

$$\text{Accuracy} = \frac{TP + TN}{N}$$

**Precision.** Enemy: the false positive.

$$p = \frac{TP}{TP + FP}$$

**Recall.** Enemy: the false negative.

$$r = \frac{TP}{TP + FN}$$

**F1 score.** Harmonic mean of precision and recall.

$$F_1 = \frac{2pr}{p + r}$$

| Model | Precision | Recall |
| --- | --- | --- |
| Predicts positive for everyone | base rate | 1 |
| Predicts positive only when certain | high | low |

> [!warning] Exam trap
> Accuracy misleads on imbalanced data: the majority-class model scores the base rate while finding no positive. F1 is low when either $p$ or $r$ is low; the arithmetic mean would hide the gap.

### Hyperparameters and Data Splits

| | Set | Chosen by |
| --- | --- | --- |
| Hyperparameters | before training ($k$ in kNN, learning rate) | trying values and measuring |
| Parameters | during training (weights) | the learning algorithm |

| Idea | Method | Verdict |
| --- | --- | --- |
| 1 | Pick what works best on training data | Bad: $k = 1$ is perfect on training data |
| 2 | Pick what works best on test data | Never: no estimate of performance on new data |
| 3 | Train, validation, test split; pick on validation, report on test | Good |
| 4 | Cross-validation: rotate folds as validation, average; test stays separate | Good for small data; rare in deep learning |

> [!warning] Exam trap
> Any choice made with the test score, including when to stop training, turns the test error into a training signal. It then no longer estimates the true error. Pick on validation, test the final model once.

> [!tip]
> Keep grouped or near-duplicate samples (photos of the same plant) in the same split, or the validation score is inflated.

## Related

- [[Function Approximation]]
- Machine Learning Task Types
- [[Loss Functions]]
- [[Overfitting and Underfitting]]
- Model Selection
- Test Set Contamination
- [[Fit Preprocessing on Training Data Only]]
- [[Early Stopping]]
- [[Regularization]]
- [[Transfer Learning]]
- [[Batch Normalization]]
- Tree Ensembles
- Flower Classifier Running Example
- What Counts as Solved

## Sources

- [[Block 1 Slides]]
- CSCI 566 Syllabus
- [[Block 2 Slides]]
- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
