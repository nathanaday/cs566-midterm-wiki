---
id: con-7kqrrf
type: topic
kind: concept
description: k-nearest neighbors (kNN) stores the training set and labels a new point by majority vote over its k nearest training points under a chosen distance function; k sets the model's capacity, and all the cost is at prediction time.
tags: [machine-learning/cs566-deeplearning]
aliases: [kNN, KNN, k-NN, k Nearest Neighbor, k-nearest neighbors, k Nearest Neighbor Algorithm, Nearest Neighbor Algorithm, 1-NN, nearest neighbor classifier, Voronoi diagram, kNN-LM, Nearest Neighbor Language Models, Semantic caching with kNN, semantic cache, Approximate nearest neighbor search, ANN search, Distance function, k-nearest neighbor voting]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 2 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Classical Machine Learning]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Classical Machine Learning]]

## Definition

k-nearest neighbors (kNN) is a classifier that labels a new point by majority vote over its k nearest training points ([[Block 2 Slides]], p. 182). The midterm review puts it in one line: "kNN predicts by a vote among nearby labels." ([[F26-midterm-review-234p]], p. 4). The user must pick two things: k and the distance metric ([[Block 2 Slides]], p. 182). The cost of kNN is in prediction, not training ([[Block 2 Slides]], p. 182).

## Explanation

### Nearest neighbor (k = 1)

- `train(D)` only stores the dataset D. `h(x')` finds the point $x^{(i)}$ in D nearest to $x'$ and returns its label $y^{(i)}$ ([[Block 2 Slides]], p. 143).
- The 1-NN partition of the input space is a Voronoi diagram. Each cell contains one training example, and all points in a cell are closer to that example than to any other training example. Points on the cell edges are equidistant to one or more training examples ([[Block 2 Slides]], p. 145).
- The 1-NN decision boundary follows the Voronoi edges between training points that have different labels ([[Block 2 Slides]], p. 146).
- Nearest neighbor needs no training. It always has zero training error, because a data point is always its own nearest neighbor ([[Block 2 Slides]], p. 147).

### The kNN algorithm

- `set_hyperparameters(k, d)` stores the number of neighbors k and the distance function d. `train(D)` stores the dataset D. `h(x')` takes the set S of the k points in D nearest to $x'$ under $d(u, v)$ and returns `majority_vote(S)` ([[Block 2 Slides]], p. 148; repeated in [[F26-midterm-review-234p]], p. 27, credited to CMU 10601).
- The label of a new point depends on k. In the slide example, k = 2 gives +1, k = 3 gives -1, and k = 5 gives +1 ([[Block 2 Slides]], p. 149).
- The midterm review gives a second example: "The prediction depends on k, because a larger k lets more neighbors vote." Five neighbors, sorted by increasing distance, have the labels purple, orange, purple, orange, orange. k = 1 predicts purple. k = 3 predicts purple, 2 to 1. k = 5 predicts orange, 3 to 2. In this example the votes are unweighted and the distances are distinct ([[F26-midterm-review-234p]], p. 26).

### Distance functions

kNN requires a distance function $d: \mathbb{R}^M \times \mathbb{R}^M \to \mathbb{R}$ ([[Block 2 Slides]], p. 150; repeated in [[F26-midterm-review-234p]], p. 28).

| Distance | Formula | Note |
| --- | --- | --- |
| Euclidean (L2) | $d(u, v) = \sqrt{\sum_{m=1}^{M} (u_m - v_m)^2}$ | the most common choice for kNN |
| Manhattan (L1) | $d(u, v) = \sum_{m=1}^{M} \lvert u_m - v_m \rvert$ | one alternative |

(Both rows: [[Block 2 Slides]], p. 150; [[F26-midterm-review-234p]], p. 28.) kNN is affected by feature scale ([[Block 2 Slides]], p. 181).

### Choosing k

- k controls the model capacity. A large k makes the decision boundary smoother. Small k leads to overfitting, and large k leads to underfitting ([[Block 2 Slides]], p. 180). See [[Overfitting and Underfitting]].
- The deck shows this on the Fisher Iris data, plotted by sepal width and sepal length with three classes. Class y = 0 separates from the others, and classes y = 1 and y = 2 overlap ([[Block 2 Slides]], p. 152).
  - At k = 1 (uniform weights), the boundary has small islands around single points. The boundaries become smoother as k grows through 2, 3, 5, 10, 20, 30, and 50 ([[Block 2 Slides]], pp. 153-160).
  - At k = 100 and k = 120, the boundaries are coarse, and a large region goes to one class ([[Block 2 Slides]], pp. 161-162).
  - At k = 150, the whole plane is predicted as a single class ([[Block 2 Slides]], p. 163).
  - Side-by-side plots for k = 1, 20, and 120 show the boundary move from jagged and fragmented to smooth ([[Block 2 Slides]], p. 164).
- Ways to choose k: monitor the error rate or accuracy; use systematic methods (automated ML, cross-validation, Bayesian optimization), which a later lecture covers; or use the heuristic $k = \sqrt{N}$, where N is the total number of samples ([[Block 2 Slides]], p. 180).
- The midterm review's rule: "choose k by validation results" ([[F26-midterm-review-234p]], p. 26). See [[Model Evaluation]] for the job of the validation split.
- A learner should be able to explain what k trades off and how to choose it ([[Block 2 Slides]], p. 182).

### Pros and cost

- Pros: intuitive and explainable, no training or retraining, and provably near-optimal in terms of true error rate ([[Block 2 Slides]], p. 181).
- kNN must always store all data, $O(ND)$. Finding the k closest points in D dimensions costs $O(ND + N \log k)$ ([[Block 2 Slides]], p. 181).
- Data structures can speed up the search, with a trade-off between training and test costs. Stochastic methods can approximate it ([[Block 2 Slides]], p. 181).

### Example: CIFAR-10

CIFAR-10 has 10 classes (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck), 50,000 training images, and 10,000 test images (Krizhevsky, "Learning Multiple Layers of Features from Tiny Images", technical report, 2009) ([[Block 2 Slides]], p. 172). The slides show test images next to their nearest training images. The neighbors often come from other classes, which shows the limits of kNN on pixel distance ([[Block 2 Slides]], p. 173).

### Nearest neighbors in LLM systems

- **Semantic caching.** Store each prompt vector with the answer the model gave. For a new prompt, find its nearest cached prompt. If the similarity clears a threshold, reuse that answer; otherwise call the model and store the new pair ([[Block 2 Slides]], p. 175). The threshold is the design: a false hit returns a wrong answer, while a miss only costs time and money. One global threshold treats easy and ambiguous prompts alike ([[Block 2 Slides]], p. 175). vCache (ICLR 2026) learns a threshold for each cached prompt under a user-set error bound. It reports up to 12.5x higher hit rates and 26x lower error rates than static-threshold baselines ([[Block 2 Slides]], p. 175).
- **kNN-LM** (Khandelwal et al., "Generalization through Memorization: Nearest Neighbor Language Models", ICLR 2020) ([[Block 2 Slides]], pp. 176-178). The datastore has one entry for each training-set token, keyed by an encoding of its leftward context. At inference, the model encodes the test context and retrieves the k most similar training contexts and their targets ([[Block 2 Slides]], p. 176). A distribution over targets comes from the distances, $p(k_i) \propto \exp(-d_i)$, and is interpolated with the model's output: $p(y) = \lambda \, p_{kNN}(y) + (1 - \lambda) \, p_{LM}(y)$ ([[Block 2 Slides]], p. 176). The hyperparameter $\lambda$ balances the two parts ([[Block 2 Slides]], p. 178). The neighbors vote on the next token. The method is still used in specialist work (ACL 2025), but it is not how a general model meets retrieval ([[Block 2 Slides]], p. 179).
- **Approximate nearest neighbor search.** Production search is approximate: HNSW, ScaNN, and DiskANN trade exact neighbors for speed, and the part given up is called recall ([[Block 2 Slides]], p. 179). Google states that ScaNN uses the same algorithm as Google Search. Microsoft reports one 50-billion-vector index across 1,000+ machines at 26 ms median latency, in Bing ([[Block 2 Slides]], p. 179).
- **Retrieval-augmented generation (RAG).** The nearest passages become readable, citable text in the model's input, so a RAG system can show its sources. RAG and kNN-LM use the same nearest-neighbor geometry through a different interface ([[Block 2 Slides]], p. 179). Across the eleven models of the LaRA benchmark, long context led retrieval by about 2.4 points at 32K tokens, and retrieval led by 3.68 at 128K ([[Block 2 Slides]], p. 179).

Synthesis: semantic caching, kNN-LM, and RAG all run the same nearest-neighbor lookup. They differ in what they do with the neighbors: return a stored answer, vote on the next token, or insert text into the context.

## Related

- [[Overfitting and Underfitting]]: k sets where kNN falls between the two
- [[Linear Classification]]: a parametric classifier, in contrast to kNN, which stores the data
- [[Model Evaluation]]: why zero training error for 1-NN says little about true error, and how validation data chooses k
- [[k-Means]]: also assigns points by distance, but without labels
- [[Autoregressive Language Modeling]]: the model that kNN-LM interpolates with
- [[KV Cache]]: a different cache, inside one generation
- [[Agent Memory]]: retrieval into context

## Sources

- [[Block 2 Slides]], pp. 143-182. The deck credits CMU 10601 for the nearest neighbor and kNN slides (pp. 143-150) and Matt Gormley for the kNN figures on the Fisher Iris data (pp. 152-164).
- [[F26-midterm-review-234p]], pp. 4, 26–28. Pp. 27–28 repeat Block 2 slides 148 and 150.
