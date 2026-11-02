---
description: k-nearest neighbors (kNN) stores the training set and labels a new point by majority vote over its k nearest training points under a chosen distance function; k sets the model's capacity, and all the cost is at prediction time.
aliases: [kNN, KNN, k-NN, k Nearest Neighbor, k-nearest neighbors, k Nearest Neighbor Algorithm, Nearest Neighbor Algorithm, 1-NN, nearest neighbor classifier, Voronoi diagram, kNN-LM, Nearest Neighbor Language Models, Semantic caching with kNN, semantic cache, Approximate nearest neighbor search, ANN search, Distance function, k-nearest neighbor voting]
sources: ["[[Block 2 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 1 Foundations and classical machine learning
---

## Definition

k-nearest neighbors (kNN) is a classifier that labels a new point by majority vote over its k nearest training points. The user must pick two things: k and the distance metric The cost of kNN is in prediction, not training. 

## Explanation

### Nearest neighbor (k = 1)

- `train(D)` only stores the dataset D. `h(x')` finds the point $x^{(i)}$ in D nearest to $x'$ and returns its label $y^{(i)}$
- The 1-NN partition of the input space is a Voronoi diagram
- The 1-NN decision boundary follows the Voronoi edges between training points that have different labels 
- **Nearest neighbor needs no training. It always has zero training error**

### The kNN algorithm

- "The prediction depends on k, because a larger k lets more neighbors vote." 
- Five neighbors, sorted by increasing distance, have the labels purple, orange, purple, orange, orange. k = 1 predicts purple. k = 3 predicts purple, 2 to 1. k = 5 predicts orange, 3 to 2. In this example the votes are unweighted and the distances are distinct

### Distance functions

kNN requires a distance function $d: \mathbb{R}^M \times \mathbb{R}^M \to \mathbb{R}$

| Distance | Formula | Note |
| --- | --- | --- |
| Euclidean (L2) | $d(u, v) = \sqrt{\sum_{m=1}^{M} (u_m - v_m)^2}$ | the most common choice for kNN |
| Manhattan (L1) | $d(u, v) = \sum_{m=1}^{M} \lvert u_m - v_m \rvert$ | one alternative |

### Choosing k

- k controls the model capacity. A large k makes the decision boundary smoother. Small k leads to overfitting, and large k leads to underfitting 
- Ways to choose k: monitor the error rate or accuracy; use systematic methods (automated ML, cross-validation, Bayesian optimization); or use the heuristic $k = \sqrt{N}$, where N is the total number of samples
- "choose k by validation results"
- A learner should be able to explain what k trades off and how to choose it ([[Block 2 Slides]], p. 182)
- Don't decide on training data alone; K=1 always works perfectly on training data

### Pros and cost

- Pros: intuitive and explainable, no training or retraining, and provably near-optimal in terms of true error rate 
- kNN must always store all data, $O(ND)$. Finding the k closest points in D dimensions costs $O(ND + N \log k)$
- Data structures can speed up the search, with a trade-off between training and test costs. Stochastic methods can approximate it 


Synthesis: semantic caching, kNN-LM, and RAG all run the same nearest-neighbor lookup. They differ in what they do with the neighbors: return a stored answer, vote on the next token, or insert text into the context.

## Related

- [[kNN Regression]]: the same neighbors, averaged instead of voted
- [[Outlier Detection]]: the k-th neighbor distance as an outlier score
- [[Overfitting and Underfitting]]: k sets where kNN falls between the two
- [[Linear Classification]]: a parametric classifier, in contrast to kNN, which stores the data
- [[Model Evaluation]]: why zero training error for 1-NN says little about true error, and how validation data chooses k
- [[k-Means]]: also assigns points by distance, but without labels
- Autoregressive Language Modeling: the model that kNN-LM interpolates with
- KV Cache: a different cache, inside one generation
- Agent Memory: retrieval into context

## Sources

- [[Block 2 Slides]], pp. 143-182. The deck credits CMU 10601 for the nearest neighbor and kNN slides (pp. 143-150) and Matt Gormley for the kNN figures on the Fisher Iris data (pp. 152-164).
- [[F26-midterm-review-234p]], pp. 4, 26–28. Pp. 27–28 repeat Block 2 slides 148 and 150.
