---
description: Underfitting is a model too simple for its data (high training and generalization error), and overfitting is a model that fits noise (low training error, high generalization error); CSCI 566 frames both as a mismatch between model complexity and data complexity and diagnoses them from training and validation curves.
aliases:
  - Overfitting
  - Underfitting
  - Appropriate fitting
  - Model capacity
  - Model complexity
  - Data complexity
  - Generalization
  - Generalization error
  - Training error
  - Generalization gap
  - Train/validation gap
  - Learning curves
  - Loss curves
  - Accuracy curves
  - Train and validation errors as clues
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
  - "[[Block 2 Slides]]"
  - "[[Block 7 Slides]]"
  - "[[F26-midterm-review-234p]]"
subject: 1 Foundations and classical machine learning
---

## Definition

An **underfit** model is too simple for its data: training and validation error are both high. An **overfit** model is too complex and fits the noise: training error is low, validation error high. Both are a mismatch between model complexity and data complexity.

**Formal overfitting.** Hypothesis $h$ overfits if some $h'$ has higher training error but lower true error:

$$
error(h, D_{train}) < error(h', D_{train}) \quad\text{and}\quad error_{true}(h) > error_{true}(h')
$$

**Generalization gap.** The amount of overfitting; validation error stands in for the unknown $error_{true}$:

$$
\text{gap} = error_{true}(h) - error(h, D_{train})
$$

### Bias and Variance

| Model | Bias | Variance | Fit |
| --- | --- | --- | --- |
| Too simple | High | Low | Underfit |
| Right size | Low | Low | Appropriate |
| Too complex | Low | High | Overfit |

- **Bias**: the model cannot represent the trend; every refit errs the same way.
- **Variance**: the model tracks its sample; refits on new samples disagree.
- Capacity trades bias for variance. [[Regularization]] trades it back.

### Train/Validation Gap Patterns

| Train error | Val error | Gap | Diagnosis | Remedy |
| --- | --- | --- | --- | --- |
| Low | High | Large | Overfitting | More data, [[Data Augmentation]], [[Regularization]], [[Dropout]], [[Early Stopping]], smaller model |
| High | High | Small | Underfitting | More capacity, better features, train longer |
| Low | Low | Small | Good fit | None; confirm the split is clean |
| High | Low | Negative | Bug | Check for leakage, label errors, or a bad split |

> [!warning] Exam trap
> A small gap alone proves nothing. Both errors high with a small gap is underfitting. Read the absolute level first, then the gap.

### Learning Curves in Words

Loss against epochs:

- Healthy: train and validation loss fall together and flatten.
- Overfitting: train loss keeps falling while validation loss bottoms out and turns up. Keep the checkpoint at the validation minimum; see [[Early Stopping]].
- Underfitting: both curves stay high, or are still falling when training stops. Train longer or add capacity before regularizing.

Error against model complexity:

- Training error keeps falling as complexity grows.
- Generalization error is U shaped: it falls, reaches a minimum at the right-sized model, then rises.
- Left of the minimum is underfitting (both high); right of it is overfitting (gap widens).

### Model Complexity vs Data Complexity

Model complexity: the number of learnable parameters and their value range; more neurons, more capacity. Data complexity: the number of examples, features per example, and class separability.

| | Data simple | Data complex |
| --- | --- | --- |
| **Model simple** | Normal | Underfitting |
| **Model complex** | Overfitting | Normal |

- Complex models need more data. Matching the two is model selection.
- A larger regularization strength $\lambda$ smooths the decision boundary.
- In [[k-Nearest Neighbors]], small $k$ overfits and large $k$ underfits.

> [!warning] Exam trap
> Memorization is not overfitting. Memorization: the model can reproduce a training string. Overfitting: training fit improves while held-out performance worsens.

## Related

- [[VC Dimension]]: capacity by shattering
- [[Regularization]]
- [[Early Stopping]]: checkpoint at the validation minimum
- [[Dropout]]
- [[Data Augmentation]]
- Model Selection
- [[Model Evaluation]]
- Tree Ensembles
- AutoML
- [[k-Nearest Neighbors]]: k as a capacity setting
- Test Set Contamination
- [[Neural Networks]]
- [[Linear Separability]]: linear boundaries underfit

## Sources

- [[Block 1 Slides]]
- [[Block 3 Slides]]
- [[Block 2 Slides]]
- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
