---
id: doc-feakck
type: topic
kind: policy
description: In CSCI 566 training and tuning experiments, keep the data split, metric, and compute budget the same, change one factor per run so the cause of a result is clear, and record the setting and outcome of every run.
tags: [machine-learning/cs566-deeplearning]
aliases: [One Experiment Should Answer One Question, Controlled comparison, Matched comparison]
created: 2026-10-12T16:58:10
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 7 Slides]]"]
strength: should
up: ["[[Neural Network Training]]"]
---

> [!policy] Should · holds for repositories tagged #machine-learning/cs566-deeplearning
> 1 source · refreshed 2026-10-13
> Up: [[Neural Network Training]]

## Rule

- "Keep the same data split, metric and training budget" ([[Block 7 Slides]], p. 172).
- Change one factor per experiment. The slide's "controlled comparison" keeps the same backbone and preprocessing, changes the learning rate, and compares validation results (p. 172).
- "Record the setting and the outcome of every run" (p. 172).
- Compare candidate settings on validation data "under the same metric and budget" (p. 326).
- When you compare automated or architecture searches: "Compare searches under matched tasks, search spaces and compute budgets" (p. 399).

## Why

- The slide calls it "A hard-to-interpret comparison" when you "Change data, model and optimizer at the same time". Then you cannot answer: "Which change caused the result?" ([[Block 7 Slides]], p. 172).
- "A fixed compute budget makes comparisons meaningful" (p. 187).
- "A benchmark result has limits set by its evaluation conditions" (p. 399). "A benchmark measures a defined set of candidate architectures" (p. 399).
- The run record is also the input to automated search. The AutoML slide starts from the case where "our manual experiment already records settings and validation scores" (p. 312).

## Applies when

Any training or tuning run for the CSCI 566 assignments or project, for example:

- the steps of the hyperparameter procedure in [[Model Selection]]
- a comparison of [[AutoML]] or architecture searches

## Exceptions

The slides state none. Synthesis: step 4 of the hyperparameter procedure trains a coarse grid over learning rate and weight decay together ([[Block 7 Slides]], p. 177). Such a grid stays a controlled comparison only if every run shares the split, metric, and budget, and each run records its full setting.

## Sources

- [[Block 7 Slides]], pp. 172, 177, 187, 312, 326, 399
