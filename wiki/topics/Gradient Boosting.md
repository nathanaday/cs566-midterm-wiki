---
id: con-0abyeq
type: topic
kind: concept
description: "Gradient boosting builds a model in stages: each new learner is fit to the current residual, the negative gradient of the loss, and added to the model, F_m = F_{m-1} + h_m; XGBoost, LightGBM, and CatBoost implement it."
tags: [machine-learning/cs566-deeplearning]
aliases: [Boosting, GBDT, Gradient-boosted decision trees, XGBoost, LightGBM, CatBoost, TabPFN-3, TabArena, Tune baselines before comparing, tabular baseline policy]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 2 Slides]]"]
up: ["[[Tree Ensembles]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Tree Ensembles]]

## Definition

Boosting fits a learner $h_m$ to the current residual and then adds it to the model: $F_m = F_{m-1} + h_m$ ([[Block 2 Slides]], p. 109). For squared loss, the residuals are the negative gradient of the loss (p. 109).

## Explanation

### Worked example

The slides use squared loss, $F_0 = 0$, shrinkage 1, and six points with $y = -8, -8, 0, 0, 8, 8$. Three stumps split after $x = 4$, $2$, and $4$. After the three stumps, the residuals are $-1, -1, 1, 1, 0, 0$ ([[Block 2 Slides]], p. 109).

### Implementations

XGBoost, LightGBM, and CatBoost differ in engineering and defaults, but they belong to one algorithm family ([[Block 2 Slides]], p. 110).

| Library | What the slide says it does (p. 110) |
| --- | --- |
| XGBoost | Regularized objective with a second-order loss approximation |
| LightGBM | Histogram-binned features and best-first, leaf-wise tree growth |
| CatBoost | Ordered target statistics for categorical features, plus ordered boosting |

### Boosted trees against deep tabular models

- TabPFN-3 (2026) reports that one forward pass beats tuned and ensembled baselines ([[Block 2 Slides]], p. 111).
- The TabArena benchmark reports that boosted trees are still strong contenders, and that deep learning catches up under larger budgets with ensembling (p. 111).
- Both results can hold, because the studies differ in time budget, ensembling, and data regime (p. 111).

### Course rules for tabular baselines

- "An untuned baseline is not a baseline" ([[Block 2 Slides]], p. 110).
- "Policy here: evaluate a tuned GBDT and TabPFN-3 under one protocol" (p. 111). The slide states this as of August 2026. The reason it gives: the published claims conflict only because they differ in time budget, ensembling, and data regime (p. 111).

Synthesis: a bagged forest averages trees that are fit in parallel to lower variance (see [[Tree Ensembles]]). Boosting adds trees in sequence, and each tree corrects what the sum of the earlier trees still gets wrong.

## Related

- [[Tree Ensembles]]: bagging and random forests
- [[Gradient Descent]]: boosting steps along the negative gradient in function space instead of weight space
- [[Loss Functions]]: squared loss makes the residual equal the negative gradient
- [[Model Evaluation]]: tuning and comparing under one protocol

## Sources

- [[Block 2 Slides]], pp. 109–111
