---
id: con-cm8p90
type: topic
kind: concept
description: Decision forests combine many decision trees by vote or average, which lowers variance, the spread of predictions across refits; bagging fits each tree on a bootstrap sample, and a random forest also draws a random feature subset at every node so that the trees' errors are less alike.
tags: [machine-learning/cs566-deeplearning]
aliases: [Random forest, Random forests, Decision forest, Decision Forests, Bagging, Bootstrap aggregating, Bootstrap AGGregatING, Bias and variance, bias-variance, refit stability, ensemble of decision trees, Ensemble averaging, Averaging an ensemble, ensemble of trees]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 2 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Decision Trees]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Decision Trees]]

## Definition

A decision forest learns many decision trees from random subsets of features and combines their results. The slides call it "a very powerful example of an ensemble method" ([[Block 2 Slides]], p. 102). Each of N trees produces a result, and majority voting or averaging combines the N results into the final result (p. 105).

## Explanation

### Bias and variance

- **Bias** is the error left when the fitted rule is too simple for the pattern ([[Block 2 Slides]], p. 106).
- **Variance** is how much predictions move when the training sample changes (p. 106).
- You can measure variance without algebra: resample, refit, and compare predictions at the same input (p. 106).
- An average of many deep trees moves less than a single deep tree. The slides call this "the whole argument for the forest" (p. 106).

The midterm review makes the measurement concrete. To study a training recipe, draw four training sets D1–D4 independently from one source, fit the same recipe on each, and ask each fitted model to predict at the same input x0 ([[F26-midterm-review-234p]], p. 16). It then defines the two terms: "Bias: mean − target" and "Variance: spread across refits" ([[F26-midterm-review-234p]], p. 17).

In its toy example, the noise-free target is 10, and the predictions are unitless ([[F26-midterm-review-234p]], p. 17; predictions read from the plot):

| Recipe | Predictions at x0 (D1, D2, D3, D4) | Mean | Slide reading |
| --- | --- | --- | --- |
| A | 5, 6, 6, 7 | 6 | "mean misses the target" |
| B | 4, 16, 6, 14 | 10 | "mean on target, larger spread" |

Synthesis: Recipe A has high bias and low variance. Recipe B has no bias in this example and high variance. The review's definition of bias (mean prediction minus target) is the quantity that Block 2's definition (the error left by a rule that is too simple) explains. The Block 2 measurement of variance (resample, refit, compare) is the review's four-refit experiment.

### Averaging an ensemble

Three trees fitted on resampled data give different predictions for the same input: 2, 5, and 8. The ensemble reports their mean, (2 + 5 + 8) / 3 = 5 ([[F26-midterm-review-234p]], p. 19). "Resampling the training data changes the trees that are learned." "Averaging aims to reduce sensitivity, but correlated errors limit it." (p. 19). The review repeats the limit on its error-diagnosis slide: "Averaging an ensemble may reduce variability, but correlated member errors limit the benefit." ([[F26-midterm-review-234p]], p. 18). See [[Overfitting and Underfitting]] for that diagnosis.

### Bagging

Bagging (bootstrap aggregating) draws n rows with replacement, fits one tree, and repeats ([[Block 2 Slides]], p. 107).

- Each bootstrap sample holds about 63% unique rows, because $1 - (1 - 1/n)^n \to 1 - 1/e$ (p. 107).
- The rows that a sample leaves out are that tree's out-of-bag set. This set is free validation data (p. 107).
- Classification aggregates by vote. Regression aggregates by average (p. 107).

### Random forest

A random forest is bagging plus a random feature subset at every node ([[Block 2 Slides]], p. 107).

The two main settings do different things (p. 108):

| Setting | Effect |
| --- | --- |
| `max_depth` | Changes the capacity of each tree. Deeper trees can overfit. |
| `n_estimators` | Changes how many trees are averaged. With the tree settings fixed, more trees approach a limiting forest vote, so they converge and do not overfit. |

### Uncertainty

Dispersion across trees is only a heuristic sign of ensemble disagreement. Calibrated uncertainty needs the infinitesimal jackknife, quantile forests, or conformal calibration ([[Block 2 Slides]], p. 108).

### Learning outcomes

The slides list these outcomes for ensemble learning ([[Block 2 Slides]], p. 112): explain why averaging lowers variance, describe bagging, say what random forests add to bagging, and name the setting that converges (tree count) and the setting that overfits (depth).

Synthesis: bagging lowers variance through averaging. The review's caveat explains why that is not enough: trees fitted on overlapping bootstrap samples make correlated errors, and averaging cannot cancel an error that all the trees share. The random feature subset makes the trees less alike, so their errors are less correlated and their average moves less again. [[Gradient Boosting]] builds its trees in sequence instead, each tree fit to the error that the model still makes.

## Related

- [[Decision Trees]]: the base learner, whose high variance a forest reduces
- [[Gradient Boosting]]: the other main family of tree ensembles in the same lecture
- [[Overfitting and Underfitting]]: depth controls overfitting; tree count does not
- [[Model Evaluation]]: out-of-bag rows serve as validation data

## Sources

- [[Block 2 Slides]], pp. 102, 105–108, 112
- [[F26-midterm-review-234p]], pp. 16–19
