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

An **underfit** model is too simple. It cannot capture the trends in the data and has too much bias

An **overfit** model is too complex. It fits the noise in the data, or "outliers", and does not have enough bias

### Formal definition

With $error(h, D_{train})$, $error(h, D_{test})$, and $error_{true}(h)$ as in [[Model Evaluation]]:

- Hypothesis $h$ overfits the training data if some other $h'$ has:
	- $error(h, D_{train}) < error(h', D_{train})$
	- AND $error_{true}(h) > error_{true}(h')$.
- Amount of overfitting $= error_{true}(h) - error(h, D_{train})$. In practice $error_{true}(h)$ is unknown.

### Training error and generalization error

**Training error** is model error on the training data. **Generalization error** is model error on new data.

| | Training error low | Training error high |
| --- | --- | --- |
| **Generalization error low** | Good | Bug? |
| **Generalization error high** | Overfitting | Underfitting |


### The generalization gap

The **generalization gap** is the distance between performance on the training data and performance on new data. Better optimization algorithms help reduce the training loss.

### Model complexity

Model complexity is "the capacity of a set of function to fit data points". In ML it usually means the **number of learnable parameters** and the **value range of those parameters**. 

As model complexity grows, training error keeps falling. Generalization error falls, reaches a minimum at the optimal model, and then rises. The gap on the left, where both errors are high, is underfitting. The gap on the right is overfitting.

![[Screenshot 2026-11-01 at 9.06.55 PM.png]]


Network size is another source of capacity. "more neurons = more capacity" 

"Larger Model Capacity May Overfit – Need to Regularize them", shows that a larger regularization strength $\lambda$ smooths the boundary 

In [[k-Nearest Neighbors]], the number of neighbors k controls capacity. Small k leads to overfitting, and large k leads to underfitting ([[Block 2 Slides]], p. 180). 

### Data complexity

Data complexity is "the richness of information" ([[Block 2 Slides]], p. 95). It depends on the number of examples, the number of features in each example, and the separability of the classes.

It is hard to compare across very different data, for example a character and a pixel. A more precise measure is **Kolmogorov** complexity: data is simple if a short program can generate it ([[Block 2 Slides]], p. 92).

| | Data complexity low | Data complexity high |
| --- | --- | --- |
| **Model complexity low** | Normal | Underfitting |
| **Model complexity high** | Overfitting | Normal |

"Complex models need more data." At low data complexity, a simple (linear) model has lower generalization error. At higher data complexity, a complex model such as a deep neural network reaches a lower generalization error ([[Block 2 Slides]], p. 93). Matching the two complexities is Model Selection ([[Block 2 Slides]], p. 95).

### Memorization is not overfitting

- **Memorization**: a model can reproduce a particular training string.
- **Overfitting**: training fit improves while performance on new data worsens.

### Reading training and validation curves

| Curves                                                                                      | Meaning                                                                          | Next step                                                                        |
| ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Training and validation loss fall together                                                  | "The model is learning patterns that transfer to held-out data."                 | None given                                                                       |
| Both loss curves stay high                                                                  | "The model has not yet fit even the training examples well."                     | "Check the training pipeline before adding more regularization."                 |
| Training loss falls, validation loss rises                                                  | "The best training checkpoint may not be the best held-out checkpoint."          | "Select checkpoints using the chosen validation metric." See [[Early Stopping]]. |
| Train and validation accuracy both still rise                                               | "Validation accuracy still improves: a longer run may help."                     | Train longer                                                                     |
| Large gap; validation accuracy peaks early and then falls while train accuracy keeps rising | "A large gap can suggest overfitting."                                           | "Check the split, labels and regularization."                                    |
| Both accuracies low, with a small gap                                                       | "Both accuracies low: possible underfitting. A small gap alone is inconclusive." | None given                                                                       |

### Train and validation errors as clues

| Observed pattern | Possible cause | First things to try |
| --- | --- | --- |
| Training and validation errors both high | Too rigid, weak features, or incomplete training | Inspect fit and features; consider more capacity |
| Training low; validation much higher | Model fits training-specific details | More data, regularization, or a simpler model |

### Diagnose, then choose a fix

| Fix | When and how |
| --- | --- |
| More or better data | "Improve coverage and inspect labels or duplicates." |
| Augmentation / weight decay | "Test task-appropriate transformations and constraints." |
| Dropout / early stopping | "Use when they fit the architecture and validation protocol." |


## Related

- [[VC Dimension]]: the shattering measure of capacity
- [[Regularization]]
- [[Early Stopping]]: checkpoint selection when validation loss turns up
- [[Dropout]]
- [[Data Augmentation]]
- Model Selection
- [[Model Evaluation]]
- Tree Ensembles: ensembles of decision trees, and bias and variance measured across refits
- AutoML: ensemble learning as an alternative
- [[k-Nearest Neighbors]]: k as a capacity setting
- Test Set Contamination
- [[Neural Networks]]
- [[Linear Separability]]: when a linear boundary underfits; class separability is also a factor of data complexity

## Sources

- [[Block 1 Slides]], p. 292
- [[Block 3 Slides]], pp. 95–96
- [[Block 2 Slides]], pp. 82, 84–93, 95, 98, 153-163, 180
- [[Block 7 Slides]], pp. 131–137, 170, 180–185, 318
- [[F26-midterm-review-234p]], pp. 4, 12–15, 18, 137–138. Pp. 12–15 repeat Block 2 slides 82, 86, 90, and 91. Pp. 137–138 repeat Block 7 slides 132 and 134.
