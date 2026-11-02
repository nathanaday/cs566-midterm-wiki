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

### Error

A loss function $\ell: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}$ defines how bad a prediction $\hat{y}$ is compared to the true label $y$. Squared loss $(y - \hat{y})^2$ is for regression. Binary or 0-1 loss $\mathbb{1}(y \neq \hat{y})$ is for classification (p. 253). See [[Loss Functions]].

$$err(h, \mathcal{D}) = \frac{1}{N} \sum_{n=1}^{N} \mathbb{1}\left(y^{(n)} \neq \hat{y}^{(n)}\right)$$

The test error rate compares the predictions on $D_{test}$ with their true labels (pp. 252–254).

Three errors for a hypothesis $h$ (p. 255):

- $error(h, D_{train})$: error rate over all training data
- $error(h, D_{test})$: error rate over all test data
- $error_{true}(h)$: true error over all data. "This is the quantity we care most about! But, in practice, error_true(h) is unknown."

### Metrics

| Task | Metrics |
| --- | --- |
| Regression | MSPE, MSAE, R², adjusted R² |
| Classification | precision-recall, ROC-AUC, accuracy, log-loss |
| Unsupervised models | Rand index, mutual information |
| Others | CV error, heuristic methods to find K, BLEU score (NLP) |

- Loss measures how well the model predicts the outcome in supervised learning.
- Other metrics are model specific (accuracy for classification, mAP for object detection) or business specific (revenue, inference latency).
- We select models by several metrics, as we choose a car.

### Metrics for binary classification

| Metric    | Definition                                             | Formula               | Description                                                                           |
| --------- | ------------------------------------------------------ | --------------------- | ------------------------------------------------------------------------------------- |
| Accuracy  | "# correct predictions / # examples"                   | $\dfrac{TP + TN}{N}$  | `sum(y == y_hat) / y.size`                                                            |
| Precision | "# True positive / # (True positive + False positive)" | $\dfrac{TP}{TP + FP}$ | when the model says yes, how often is it right? Its enemy is the false positive.      |
| Recall    | "# True positive / # Positive examples"                | $\dfrac{TP}{TP + FN}$ | of the real positives, how many did the model catch? Its enemy is the false negative. |
| F1        | "the harmonic mean of precision and recall"            | $\dfrac{2pr}{p + r}$  |                                                                                       |

- A model that predicts positive for every example has recall 1 and precision equal to the base rate. 
- A model that predicts positive only when it is certain has high precision and low recall. 
- The harmonic mean punishes the imbalance: F1 is low when either $p$ or $r$ is low, where the arithmetic mean would hide it. 
- Accuracy alone misleads on imbalanced data, since predicting the majority class for every example scores the base rate without finding any positive.

### Hyperparameters

A hyperparameter is a choice about the algorithm itself. Hyperparameters depend heavily on the problem and the dataset, so you must try them and see what works best.
- Hyperparameters: "usually set beforehand".
- Parameters: "learnable, e.g., model weights".

| Idea | Method | Verdict |
| --- | --- | --- |
| #1 | Choose what works best on the training data | Bad: k = 1 always works perfectly on training data (pp. 166–167) |
| #2 | Choose what works best on the test data | Bad: you then have no idea how the algorithm will perform on new data. "Never do this!" (pp. 168–169) |
| #3 | Split data into train, validation, and test. Choose on validation, evaluate on test | "Better!" (p. 170, credit Stanford CS 229) |
| #4 | Cross-validation: split data into folds, try each fold as validation, and average the results. The test set stays separate | Useful for small datasets, but not used often in deep learning (p. 171) |

### Cross-validation

Synthesis: test error estimates the true error, which matters most and which no one can measure directly. A low training error alone can hide [[Overfitting and Underfitting]]. If you tune on the test set, the test error no longer estimates the true error, which is why the validation split exists. For agents, a single test error is not enough; see What Counts as Solved.

## Related

- [[Function Approximation]]: $c^*$ here plays the role of the $f^*$ that $f$ approximates
- Machine Learning Task Types
- [[Loss Functions]]
- [[Overfitting and Underfitting]]
- Model Selection
- Test Set Contamination: what happens when test items reach training
- [[Fit Preprocessing on Training Data Only]]
- [[Early Stopping]]
- [[Regularization]]: choose the penalty strength on validation data
- [[Transfer Learning]]: the same evaluation rule for pretrained starts
- [[Batch Normalization]]: different behavior in training and evaluation mode
- Tree Ensembles: out-of-bag rows give free validation data
- Flower Classifier Running Example
- What Counts as Solved

## Sources

- [[Block 1 Slides]], pp. 238–256
- CSCI 566 Syllabus, schedule
- [[Block 2 Slides]], pp. 136–138, 165–171, 174, 180
- [[Block 7 Slides]], pp. 17, 34, 135, 173, 190, 315, 319, 326
- [[F26-midterm-review-234p]], pp. 4–9, 21, 125, 139–140, 145
