---
id: doc-94j4sz
type: topic
kind: policy
description: Split the data first, fit every preprocessing statistic (such as a mean, a standard deviation, or an imputation value) on the training split only, and apply that fitted transformation unchanged to validation and test data.
tags: [machine-learning/cs566-deeplearning]
aliases: [Split the data before fitting preprocessing or models, "Fit preprocessing on training data, then reuse it", "Fit the transformation on training data, then reuse it", Validation set uses training statistics, Preprocessing data leakage, "Fit once, apply everywhere"]
created: 2026-10-12T16:58:10
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
strength: should
up: ["[[Data Preprocessing]]"]
---

> [!policy] Should · holds for repositories tagged #machine-learning/cs566-deeplearning
> 2 sources · refreshed 2026-10-19
> Up: [[Data Preprocessing]]

## Rule

1. Split the data into training, validation, and test sets before you fit any preprocessing or model. The slide: "Split the flower photos before fitting preprocessing or models" ([[Block 7 Slides]], p. 17). The same slide adds: "Keep near-duplicate photos in the same split" (p. 17).
2. Fit every preprocessing statistic on the training split only. The training split "fit[s] model weights and preprocessing statistics" (p. 17). "Fit the transformation on training data, then reuse it" (p. 18). "Fit any imputation rule on training data" (p. 39).
3. Apply the fitted transformation unchanged to the validation and test data. "Preprocessing steps should be defined and fitted on the training data, then applied to the test data" (p. 40). For standardization, the mean and standard deviation "should be derived from the training data and then used to scale the test data" (p. 40). The midterm review states steps 2 and 3 in one line: "Fit preprocessing statistics on training data only, then apply them unchanged to validation and test." ([[F26-midterm-review-234p]], p. 4).
4. Treat the fitted rule as part of the model. "The fitted preprocessing rule is part of the model pipeline" ([[Block 7 Slides]], p. 23).

Example from the slides (p. 23): the training-set mean of one feature is 100. Training example 120 becomes 120 − 100 = 20. Validation example 130 becomes 130 − 100 = 30. "We do not recompute a new centering rule from validation data."

The midterm review's slide "Fit Once, Apply Everywhere" extends this example to the test split ([[F26-midterm-review-234p]], p. 7). The feature is the average pixel intensity of each photo. Its mean over all 80 training photos is 100 (illustrative), so the stored rule is x → x − 100:

| Photo | Value | Centered value |
| --- | --- | --- |
| Training | 120 | 20 |
| Validation | 130 | 30 |
| Test | 90 | −10 |

"Outputs are centered feature values, not prediction errors" (p. 7).

## Why

From the slide: this "prevents data leakage and ensures that the model's performance is evaluated on the same terms as it was trained" ([[Block 7 Slides]], p. 40).

The midterm review's check question rejects a plan to "Compute normalization statistics from all data including test, then train and tune on validation." ([[F26-midterm-review-234p]], p. 8). Its reason: "Preprocessing is fitted on the training set only. Using test statistics leaks test information into the model." (p. 9).

Synthesis: a statistic computed on validation or test data carries information about the held-out data into the model. The validation and test errors then no longer measure performance on unseen data. This is the same failure as Test Set Contamination, in a smaller form. See [[Model Evaluation]] for the jobs of the three splits.

## Applies when

Synthesis: CS566 course and project work that trains or evaluates a model with a fitted input transformation. Examples from the deck: zero-centering, standardization, PCA whitening, and imputation of missing values ([[Block 7 Slides]], pp. 19-23, 36-41). See [[Data Preprocessing]].

## Exceptions

The slides state no exceptions.

Synthesis, not a slide claim: two cases do not use statistics fitted on your own training split.

- A pretrained model has its own input convention. Apply its specified per-channel mean and scale ([[Block 7 Slides]], p. 38).
- Normalization layers inside the network, such as [[Batch Normalization]], compute statistics on hidden activations during training. That is not input preprocessing (p. 24).

## Sources

- [[Block 7 Slides]], pp. 17-18, 23, 38-41
- [[F26-midterm-review-234p]], pp. 4, 7-9
