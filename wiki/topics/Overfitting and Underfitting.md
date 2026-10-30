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
---

> [!concept] Concept
> 5 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Model Evaluation]]

## Definition

A figure with two classes (X and O) shows three decision boundaries ([[Block 1 Slides]], p. 292; repeated in [[Block 2 Slides]], p. 82, and in [[F26-midterm-review-234p]], p. 12):

| Fit | Slide label | Boundary |
| --- | --- | --- |
| Underfitting | "too simple to explain the variance" | a straight line that misses the structure |
| Appropriate fit | "Appropirate-fitting" (typo on the slide) | a smooth curve that separates the classes |
| Overfitting | "forcefitting--too good to be true" | a curve that bends around single points |

"We favor the case where the ML model appropriately depict the underlying data" ([[Block 1 Slides]], p. 292; [[F26-midterm-review-234p]], p. 12).

[[Block 2 Slides]] gives the causes ([[Block 2 Slides]], p. 84):

- An **underfit** model is too simple. It cannot capture the trends in the data and has too much bias. Examples: a majority-vote classifier (a decision tree of depth zero), and a toddler with no medical school who tries a medical diagnosis.
- An **overfit** model is too complex. It fits the noise in the data, or "outliers", and does not have enough bias. Examples: a "memorizer" that responds to an irrelevant attribute, and a medical student who memorizes patient case studies but cannot apply the knowledge to new patients.

### Formal definition

The slide is adapted from Tom Mitchell ([[Block 2 Slides]], p. 85). With $error(h, D_{train})$, $error(h, D_{test})$, and $error_{true}(h)$ as in [[Model Evaluation]]:

- Hypothesis $h$ overfits the training data if some other $h'$ has $error(h, D_{train}) < error(h', D_{train})$ but $error_{true}(h) > error_{true}(h')$.
- Amount of overfitting $= error_{true}(h) - error(h, D_{train})$. In practice $error_{true}(h)$ is unknown.

## Explanation

### Training error and generalization error

"Generalization means low error on new data from the same source as the training data." The midterm review puts generalization together with data splits and simple predictors: "Data splits, generalization, and simple predictors set the standard for judging any model." ([[F26-midterm-review-234p]], p. 4)

Training error is model error on the training data. Generalization error is model error on new data ([[Block 2 Slides]], p. 87, credited to Stanford CS 329P):

| | Training error low | Training error high |
| --- | --- | --- |
| **Generalization error low** | Good | Bug? |
| **Generalization error high** | Overfitting | Underfitting |

In Tom Mitchell's decision-tree figure, accuracy on training data keeps rising with tree size, to about 0.86 at 90+ nodes. Test accuracy peaks near 0.75 at small sizes and falls to about 0.69 ([[Block 2 Slides]], p. 86; repeated in [[F26-midterm-review-234p]], p. 13).

### The generalization gap

The generalization gap is the distance between performance on the training data and performance on new data. Better optimization algorithms help reduce the training loss, "But we really care about error on new data - how to reduce the gap?" ([[Block 7 Slides]], p. 131). In the slide's example, train accuracy rises to about 0.74 at 20,000 iterations, but validation accuracy rises only from about 0.50 to about 0.55 ([[Block 7 Slides]], p. 131; values read from the plot). The deck shows the same plot under the title "How to improve single-model performance?" and gives the answer "Regularization" ([[Block 7 Slides]], p. 137). See [[Regularization]].

### Model complexity

Model complexity is "the capacity of a set of function to fit data points" ([[Block 2 Slides]], p. 89). The summary slide calls it "the ability to fit various functions" (p. 95). In ML it usually means the number of learnable parameters and the value range of those parameters. It is hard to compare across model types, for example trees and neural networks. A more precise measure is the VC dimension: for a classification model, the maximum number of examples the model can shatter ([[Block 2 Slides]], p. 89).

As model complexity grows, training error keeps falling. Generalization error falls, reaches a minimum at the optimal model, and then rises. The gap on the left, where both errors are high, is underfitting. The gap on the right is overfitting ([[Block 2 Slides]], p. 90; repeated in [[F26-midterm-review-234p]], p. 14, credited to Stanford CS 329P).

Example: the depth of a decision tree sets its size. "The tree size can be controlled by the number of levels." The slide fits scikit-learn `DecisionTreeRegressor(max_depth=n)` on house sales data. Training error falls toward zero as `max_depth` grows to 50. Validation error bottoms out near depth 10 and then rises slightly ([[Block 2 Slides]], p. 91; repeated in [[F26-midterm-review-234p]], p. 15).

Network size is another source of capacity. On one dataset, 3, 6, and 20 hidden neurons draw more and more complex boundaries: "more neurons = more capacity" ([[Block 3 Slides]], p. 95). The next slide, "Larger Model Capacity May Overfit – Need to Regularize them", shows that a larger regularization strength $\lambda$ smooths the boundary ([[Block 3 Slides]], p. 96). See [[Neural Networks]].

In [[k-Nearest Neighbors]], the number of neighbors k controls capacity. Small k leads to overfitting, and large k leads to underfitting ([[Block 2 Slides]], p. 180). On the Fisher Iris data, k = 1 gives small islands around single points, and the boundary becomes smoother as k grows ([[Block 2 Slides]], pp. 153-160). At k = 150, the whole plane is predicted as one class ([[Block 2 Slides]], p. 163).

### Data complexity

Data complexity is "the richness of information" ([[Block 2 Slides]], p. 95). It depends on the number of examples, the number of features in each example, and the separability of the classes. It is hard to compare across very different data, for example a character and a pixel. A more precise measure is Kolmogorov complexity: data is simple if a short program can generate it ([[Block 2 Slides]], p. 92).

The slides give an alternative view of fit as model complexity against data complexity ([[Block 2 Slides]], p. 88):

| | Data complexity low | Data complexity high |
| --- | --- | --- |
| **Model complexity low** | Normal | Underfitting |
| **Model complexity high** | Overfitting | Normal |

"Complex models need more data." At low data complexity, a simple (linear) model has lower generalization error. At higher data complexity, a complex model such as a deep neural network reaches a lower generalization error ([[Block 2 Slides]], p. 93). Matching the two complexities is Model Selection ([[Block 2 Slides]], p. 95).

### Memorization is not overfitting

The slides separate the two ([[Block 2 Slides]], p. 98):

- **Memorization**: a model can reproduce a particular training string.
- **Overfitting**: training fit improves while performance on new data worsens.

They can come apart. When Pythia, Llama3, and Mistral models from 1.4B to 70B parameters were fine-tuned, memorization rose sharply in the first few epochs, often before validation perplexity was best. "Validation error can improve while verbatim leakage grows." The slide's rule: "When privacy or copyright matters, track held-out performance and memorization together." A memorization-aware regularizer cut memorization by up to 40% across the model families tested ([[Block 2 Slides]], p. 98).

### Reading training and validation curves

Learning curves plot the training loss, and the training and validation accuracy, against the iteration or epoch. The deck's advice is "Look at learning curves!" ([[Block 7 Slides]], p. 183). For loss curves, its rule is: "Evaluate both curves using comparable loss definitions and modes." ([[Block 7 Slides]], p. 132; repeated in [[F26-midterm-review-234p]], p. 137). Synthesis, not stated on the slide: "modes" probably means training mode and evaluation mode. Layers such as [[Dropout]] act differently in the two modes.

The slides read six patterns. The loss plots on pp. 132-134 are labeled "Loss (illustrative)" and "Course teaching example".

| Curves | What the slides say | Next step | Source |
| --- | --- | --- | --- |
| Training and validation loss fall together | "The model is learning patterns that transfer to held-out data." | None given | p. 132; review p. 137 |
| Both loss curves stay high | "The model has not yet fit even the training examples well." | "Check the training pipeline before adding more regularization." | p. 133 |
| Training loss falls, validation loss rises | "The best training checkpoint may not be the best held-out checkpoint." | "Select checkpoints using the chosen validation metric." See [[Early Stopping]]. | p. 134; review p. 138 |
| Train and validation accuracy both still rise | "Validation accuracy still improves: a longer run may help." | Train longer | p. 180 |
| Large gap; validation accuracy peaks early and then falls while train accuracy keeps rising | "A large gap can suggest overfitting." | "Check the split, labels and regularization." | p. 181 |
| Both accuracies low, with a small gap | "Both accuracies low: possible underfitting. A small gap alone is inconclusive." | None given | p. 182 |

The pages in the Source column are in [[Block 7 Slides]]. "Review p." marks the copy of the same slide in [[F26-midterm-review-234p]]. Open point: the p. 182 plot has no values on its accuracy axis, and both curves rise much like the p. 180 plot. Only the slide text, not the plot, shows that the accuracies are "low".

Practical advice from the deck ([[Block 7 Slides]], pp. 183-185):

- "Losses may be noisy, use a scatter plot and also plot moving average to see trends better" (p. 183). In that example, train accuracy reaches about 98 and validation accuracy about 95 after about 600,000 iterations (values read from the plot).
- "You can plot all your loss curves for different HPs on a single plot" (p. 184). See Model Selection.
- A humorous slide warns: "Don't look at accuracy or loss curves for too long!" (p. 185).

### Train and validation errors as clues

The midterm review reads the two error levels as clues: "When train and validation data come from the same source, the pattern of their errors suggests a first thing to try, not a proven cause." ([[F26-midterm-review-234p]], p. 18)

| Observed pattern | Possible cause | First things to try |
| --- | --- | --- |
| Training and validation errors both high | Too rigid, weak features, or incomplete training | Inspect fit and features; consider more capacity |
| Training low; validation much higher | Model fits training-specific details | More data, regularization, or a simpler model |

([[F26-midterm-review-234p]], p. 18)

Synthesis: the first row is the underfitting cell of the Stanford CS 329P table above, and the second row is the overfitting cell. "Incomplete training" as a cause fits the Block 7 rule to check the training pipeline first when both curves stay high ([[Block 7 Slides]], p. 133).

### Diagnose, then choose a fix

The slide "Regularization: Diagnose, Then Choose" tells the reader to "Return to the gap between training and validation performance" before choosing a fix ([[Block 7 Slides]], p. 170):

| Fix | When and how |
| --- | --- |
| More or better data | "Improve coverage and inspect labels or duplicates." |
| Augmentation / weight decay | "Test task-appropriate transformations and constraints." |
| Dropout / early stopping | "Use when they fit the architecture and validation protocol." |

Its rule: "Compare one controlled change at a time." ([[Block 7 Slides]], p. 170). See [[Data Augmentation]], [[Regularization]], [[Dropout]], and [[Early Stopping]].

Synthesis: the two rules on pp. 133 and 170 fit together. When both curves stay high, the model underfits, and more regularization constrains a model that already fails to fit the training data. So check the pipeline first. When the gap is large, choose one of the fixes in the table and test it alone.

### Ensembles

An ensemble combines the predictions of several trained models. In the slide's example, three trained classifiers disagree on one flower photo. The ensemble averages the class probabilities of Model 1, 2, and 3, and it chooses the class with the highest score. The slide's rule: "Measure any accuracy gain together with serving cost." ([[Block 7 Slides]], p. 136). See Flower Classifier Running Example. Synthesis: the deck puts this slide just before "How to improve single-model performance?" (p. 137). So the deck offers ensembles as one way to raise held-out accuracy and regularization as the way to improve a single model.

The midterm review states the limit of this method on its diagnosis slide: "Averaging an ensemble may reduce variability, but correlated member errors limit the benefit." ([[F26-midterm-review-234p]], p. 18). See Tree Ensembles for its worked example and for bias and variance.

Later, the deck names ensemble learning as an alternative to AutoML: "One may use stable & robust methods like ensemble learning to combine multiple models together." If you do not know which algorithm and hyperparameters to select, "It is possible to randomly build multiple models with different hyperparameters and then combine them, e.g., taking the average." The drawback: "building many diversified models may be slow for prediction." ([[Block 7 Slides]], p. 318). For ensembles of decision trees, see Tree Ensembles.

### Why it matters

Synthesis: only data the model did not train on shows overfitting, because training error falls with complexity in every figure above. That held-out data must stay unseen; see Test Set Contamination. [[Regularization]] reduces overfitting by preferring simple models, [[Early Stopping]] keeps the checkpoint with the best validation metric, and Model Selection picks the complexity with the lowest generalization error.

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
