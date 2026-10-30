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

To evaluate a machine learning algorithm, check its error rate on a separate test dataset $D_{test}$ ([[Block 1 Slides]], p. 253). The slides build this from a medical-diagnosis example credited to CMU 10601 (pp. 238–256).

## Explanation

### Example

Five patients have four yes/no attributes: hives, sneezing, red eye, and has cat. The label is "allergic?" (+ or −). So $N = 5$ training examples and $M = 4$ attributes (pp. 238, 247). The same table becomes multi-class classification when the label is the allergy type (none, dust, mold), and regression when the output is the treatment cost (pp. 241–242).

One example hypothesis: $h(x) = +$ if sneezing = Y, else $-$ (p. 249).

### Problem setting

- Inputs $x \in \mathcal{X}$ (all possible patients) and outputs $y \in \mathcal{Y}$ (all possible diagnoses).
- An unknown target function $c^*: \mathcal{X} \to \mathcal{Y}$ (the doctor's brain).
- A set $\mathcal{H}$ of candidate hypotheses $h: \mathcal{X} \to \mathcal{Y}$ (for example, all possible decision trees).
- Training data $D = \{(x^{(1)}, y^{(1)}), \dots, (x^{(N)}, y^{(N)})\}$ with $y^{(i)} = c^*(x^{(i)})$ (the history of patients and their diagnoses).
- The learner produces $\hat{y} = h(x)$ that best approximates $c^*$ on the training data.

Classification has discrete outputs; regression has real-valued outputs (pp. 250–251).

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

Source: [[Block 1 Slides]], p. 256.

Loss and other metrics do different jobs ([[Block 2 Slides]], p. 136):

- Loss measures how well the model predicts the outcome in supervised learning.
- Other metrics are model specific (accuracy for classification, mAP for object detection) or business specific (revenue, inference latency).
- We select models by several metrics, as we choose a car.

The Block 2 metric slides are adapted from Stanford CS 329P (2021 Fall) (pp. 136–138). For the formulas of accuracy, precision, recall, F1, ROC-AUC, and PR-AUC, see Classification Metrics.

### Three data splits

The Block 7 slide "Three Data Splits, Three Jobs" gives each split one job ([[Block 7 Slides]], p. 17):

| Split | Job |
| --- | --- |
| Training | "Fit model weights and preprocessing statistics." |
| Validation | "Choose settings and a checkpoint (saved model weights)." |
| Test | "Evaluate the final selected model." |

The slide uses the Flower Classifier Running Example and gives two rules (p. 17):

- "Split the flower photos before fitting preprocessing or models."
- "Keep near-duplicate photos in the same split."

The midterm review states the three jobs in one line: "Training data fits parameters, validation data selects settings, and test data gives a final check." ([[F26-midterm-review-234p]], p. 4).

Synthesis: if a near-duplicate of a test photo is in the training split, the model has seen the test item in another form. This is a form of Test Set Contamination. The training split alone supplies the preprocessing statistics; see [[Fit Preprocessing on Training Data Only]].

#### Worked example: splitting by plant

The midterm review splits an illustrative set of 120 daisy and tulip photos. The photos come from 24 plants, with 5 photos for each plant ([[F26-midterm-review-234p]], p. 5):

| Split | Size | Job |
| --- | --- | --- |
| Training | 16 plants / 80 photos | "Fit weights" |
| Validation | 4 plants / 20 photos | "Select depth or checkpoint" |
| Test | 4 plants / 20 photos | "Evaluate once, after selection" |

The slide's rule: "All 5 photos of a plant stay together". Its goal: "Generalize to unseen plants, same source" (p. 5).

Synthesis: the plant is a group of near-duplicate photos, so this rule applies the Block 7 near-duplicate rule to a whole group. If photos of a test plant were in the training split, the test error would overstate how well the model does on a new plant.

#### Worked example: choosing between two trees

The next slide fits two decision trees on the same 80 training photos (illustrative results) ([[F26-midterm-review-234p]], p. 6):

| Candidate | Training error | Validation error |
| --- | --- | --- |
| A: depth 2 | 8/80 (10%) | 3/20 (15%) |
| B: depth 10 | 0/80 (0%) | 5/20 (25%) |

"Select A: lower validation error". Then: "Choice frozen". "A on test: 4/20 errors (20%)". "Test is not used to switch candidate" (p. 6).

Synthesis: B has no training error but the higher validation error, which is the pattern of [[Overfitting and Underfitting|overfitting]]. A's test error (20%) is higher than its validation error (15%). The test score is reported as it is, and it does not reopen the choice.

#### Check question: which plan keeps each split's job

The midterm review asks which of four plans is correct. Its summary: "Train fits weights and preprocessing, validation chooses settings and checkpoint, and test evaluates the final selected model." ([[F26-midterm-review-234p]], p. 8). The answer is plan B: "Fit on train, choose learning rate and checkpoint on validation, then evaluate that choice on test." (p. 8). The reason: "Each split keeps its taught role, and the test set stays unseen until it evaluates the final selected model." (p. 9).

Each wrong plan breaks one split's job (pp. 8–9):

| Plan | What it does | Why it is wrong |
| --- | --- | --- |
| A | "Try several learning rates, keep the one with the best test accuracy, and report that accuracy." | "Choosing settings with test accuracy makes the test set a selection tool, so its score no longer checks unseen data." |
| C | "Compute normalization statistics from all data including test, then train and tune on validation." | "Preprocessing is fitted on the training set only. Using test statistics leaks test information into the model." See [[Fit Preprocessing on Training Data Only]]. |
| D | "Add the test set to training for more data, then choose settings on validation and report validation." | "Fitting weights on test data removes the held-out check, and a validation score used for choosing is not a final result." |

### Hyperparameters

A hyperparameter is a choice about the algorithm itself. For kNN, the best value of k and the best distance metric are hyperparameters ([[Block 2 Slides]], p. 165). Hyperparameters depend heavily on the problem and the dataset, so you must try them and see what works best (p. 165).

Block 7 sets hyperparameters apart from parameters ([[Block 7 Slides]], p. 173):

- Hyperparameters: "usually set beforehand".
- Parameters: "learnable, e.g., model weights".

"Hyperparameters are specific settings of a selected algorithm, such as the tree depth of decision tree or the number of nearest neighbors for kNN." "Models are the combination of algorithms and hyperparameters", for example {kNN, n_neighbors=5} or {Decision tree, tree_depth=10} ([[Block 7 Slides]], p. 319). Once an algorithm is chosen, you must decide its hyperparameters (p. 315):

- Data preprocessing, such as PCA: how many principal components (the target dimension).
- Classical ML: the number of nearest neighbors for kNN, the number of base trees for random forests.
- Deep learning: the learning rate and the dropout rate.

The slides compare four ways to choose them:

| Idea | Method | Verdict |
| --- | --- | --- |
| #1 | Choose what works best on the training data | Bad: k = 1 always works perfectly on training data (pp. 166–167) |
| #2 | Choose what works best on the test data | Bad: you then have no idea how the algorithm will perform on new data. "Never do this!" (pp. 168–169) |
| #3 | Split data into train, validation, and test. Choose on validation, evaluate on test | "Better!" (p. 170, credit Stanford CS 229) |
| #4 | Cross-validation: split data into folds, try each fold as validation, and average the results. The test set stays separate | Useful for small datasets, but not used often in deep learning (p. 171) |

Rule from these slides: choose hyperparameters on a validation split, and evaluate on the test set once. Do not choose them on the training set or on the test set (pp. 166–170).

### Keep the test set outside every selection loop

Block 7 applies the same rule to every choice made during training:

- **Repeated validation.** The slide "Repeated Validation Can Overfit the Selection Process" says: "Trying many settings also uses information from the validation set." The flow is: many training runs, then choose with validation data, then "Evaluate once on held-out test data". "Model selection is part of the learning process." ([[Block 7 Slides]], p. 190). See Model Selection.
- **Hyperparameter search.** Fit each candidate model on the training data. "Compare candidate settings under the same metric and budget" on the validation data. Use the test data to "Evaluate the selected procedure after tuning is complete." "The test score remains outside the search loop." (p. 326). See Model Selection.
- **Stopping.** "Use a fixed protocol": "Keep the test set out of stopping decisions." "Choose the stopping rule before inspecting test performance." The same slide keeps the checkpoint with the best value of the selected validation metric (p. 135). The midterm review repeats this slide ([[F26-midterm-review-234p]], p. 139) and adds: "Test set: evaluate once, after all choices are fixed." (p. 140). See [[Early Stopping]].
- **Regularization strength.** For a weight penalty, "λ controls the tradeoff. Choose it using validation data." ([[F26-midterm-review-234p]], p. 125). See [[Regularization]].
- **Training and transfer.** The same classifier can start from random or pretrained weights. In both cases the evaluation rule is: "Select by validation performance and test the final choice." ([[F26-midterm-review-234p]], p. 145). See [[Transfer Learning]].
- **Evaluation mode.** "Switch the model to evaluation mode when evaluating." At evaluation, BatchNorm usually uses stored running statistics, and "The flower classifier may receive one new photo at a time." ([[Block 7 Slides]], p. 34). See [[Batch Normalization]].

Synthesis: when a score drives a choice, the data behind that score becomes part of the learning process. The validation split takes this role, so the test error can still estimate the true error.

### Cross-validation

In the slides' example of 5-fold cross-validation over k, each point is a single outcome, the line goes through the mean, and the bars show the standard deviation. For that data, k of about 7 works best ([[Block 2 Slides]], p. 174). Cross-validation is one systematic way to choose k. Automated ML and Bayesian optimization are others (p. 180).

Synthesis: test error estimates the true error, which matters most and which no one can measure directly. A low training error alone can hide [[Overfitting and Underfitting]]. If you tune on the test set, the test error no longer estimates the true error, which is why the validation split exists. For agents, a single test error is not enough; see What Counts as Solved.

The CSCI 566 Syllabus covers model metrics in week 2.

## Related

- [[Function Approximation]]: $c^*$ here plays the role of the $f^*$ that $f$ approximates
- Machine Learning Task Types
- [[Loss Functions]]
- Classification Metrics
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
- [[F26-midterm-review-234p]], pp. 4–9, 125, 139–140, 145
