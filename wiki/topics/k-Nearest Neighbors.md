---
description: k-nearest neighbors (kNN) stores the training set and labels a new point by majority vote over its k nearest training points under a chosen distance function; k sets the model's capacity, and all the cost is at prediction time.
aliases: [kNN, KNN, k-NN, k-nearest neighbors, Nearest Neighbor Algorithm, 1-NN]
sources: ["[[Block 2 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 1 Foundations and classical machine learning
---

## Definition

k-nearest neighbors (kNN) labels a new point by majority vote over its k nearest training points. The user picks two things: k and the distance function. Training only stores the data, so all the cost falls on prediction.

### Algorithm

- `train(D)`: store D. Nothing is fit.
- `h(x')`: compute $d(x', x^{(i)})$ for every $i$, take the k smallest, return the majority label.
- k = 1 (nearest neighbor): the partition of the input space is a Voronoi diagram, and the decision boundary follows the Voronoi edges between points with different labels.
- Five neighbors by distance with labels P, O, P, O, O: k = 1 gives P, k = 3 gives P (2 to 1), k = 5 gives O (3 to 2).

### Distance Functions

kNN needs $d: \mathbb{R}^M \times \mathbb{R}^M \to \mathbb{R}$.

**Euclidean (L2), the default choice.**

$$
d(u, v) = \sqrt{\sum_{m=1}^{M} (u_m - v_m)^2}
$$

**Manhattan (L1).**

$$
d(u, v) = \sum_{m=1}^{M} \lvert u_m - v_m \rvert
$$

### Choosing k

k sets model capacity. See [[Overfitting and Underfitting]].

| k | Boundary | Failure mode | Training error |
| --- | --- | --- | --- |
| Small | jagged, follows noise | overfits | zero at k = 1 |
| Large | smooth | underfits | rises |
| k = N | constant majority class | ignores x | high |

- Pick k on a validation split: fit on one part, score accuracy on the held-out part, keep the best k. See [[Model Evaluation]].
- Alternatives: cross-validation, automated search, or $k = \sqrt{N}$ as a starting point.

> [!tip]
> Training error cannot choose k. 1-NN always scores zero on the training set because every point is its own nearest neighbor.

### Cost

| Phase | Cost | Note |
| --- | --- | --- |
| Train | $O(1)$ compute, $O(ND)$ memory | stores all N points of D dimensions |
| Predict one point | $O(ND + N \log k)$ | distance to every point, then select the k closest |

- Search structures (trees, hashing) and approximate nearest neighbor (ANN) search move cost from prediction into a build step.
- Pros: explainable, no training or retraining, near-optimal true error rate as N grows.

> [!tip]
> Curse of dimensionality: in high dimensions every point sits at nearly the same distance from every other, so "nearest" loses meaning and kNN needs exponentially more data. Scale features first, because distance weights every dimension equally.

## Related

- [[kNN Regression]]: average instead of vote
- [[Outlier Detection]]: k-th neighbor distance as a score
- [[Overfitting and Underfitting]]: what k trades off
- [[Linear Classification]]: parametric, in contrast to kNN
- [[Model Evaluation]]: validation chooses k
- [[k-Means]]: distance without labels
- Autoregressive Language Modeling: what kNN-LM interpolates with
- KV Cache: a different cache
- Agent Memory: retrieval into context

## Sources

- [[Block 2 Slides]]
- [[F26-midterm-review-234p]]
