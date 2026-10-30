---
id: con-218fzg
type: topic
kind: concept
description: k-means clusters unlabeled points by repeating two steps, assign each point to its nearest center and move each center to the mean of its points, which lowers the total squared distance from points to their centers; it assumes spherical clusters of similar size, and different runs can stop at different answers.
tags: [machine-learning/cs566-deeplearning]
aliases: [k-means, K-Means, KMeans, k-means clustering, k-means algorithm, k-means objective, CuraWeb, Semantic deduplication, semantic dedup, MinHash deduplication]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 2 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Clustering]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Clustering]]

## Definition

k-means is a [[Clustering]] algorithm. It scores each observation by its distance to a cluster center, and a smaller score is better ([[Block 2 Slides]], p. 194; repeated in [[F26-midterm-review-234p]], p. 30). It repeats two steps: assign each point to a center, then revise the centers. The deck calls this "assign, revise, repeat" ([[Block 2 Slides]], p. 211). The midterm review states the goal: "k-means clusters by minimizing a squared distance objective." ([[F26-midterm-review-234p]], p. 4)

## Explanation

### The algorithm

1. Initialize cluster centers $\mu_1, \dots, \mu_k$ ([[Block 2 Slides]], pp. 195-196; [[F26-midterm-review-234p]], p. 31).
2. Assign each observation to the closest center: $z_i \leftarrow \arg\min_j \lVert \mu_j - x_i \rVert_2^2$ ([[Block 2 Slides]], p. 196; [[F26-midterm-review-234p]], p. 32). Here $z_i$ is an inferred label. In supervised learning, the label $y_i$ is given ([[Block 2 Slides]], p. 196).
3. Revise each center as the mean of its assigned observations: $\mu_j = \frac{1}{n_j} \sum_{i: z_i = j} x_i$ ([[Block 2 Slides]], p. 197; [[F26-midterm-review-234p]], p. 33).
4. Repeat until convergence. The Block 2 slide writes "Repeat 1.+2." ([[Block 2 Slides]], p. 198). The copy of the same slide in the midterm review writes "Repeat 2.+3. until convergence" ([[F26-midterm-review-234p]], p. 34), which matches the step numbers in this list.

The review credits these slides to Stanford CS 229 ([[F26-midterm-review-234p]], pp. 30-34).

### The objective

"k-means scores a clustering by the total squared distance from points to their assigned centers." The slide calls this total J ([[F26-midterm-review-234p]], p. 35).

Example: points 1, 5, and 6 are assigned to one center. The center is their mean, (1 + 5 + 6) / 3 = 4, and J = (1 − 4)² + (5 − 4)² + (6 − 4)² = 14. "With assignments fixed, the mean minimizes the sum of squared distances." ([[F26-midterm-review-234p]], p. 35)

Synthesis, in the notation of the steps above (the slide states J in words): $J = \sum_i \lVert x_i - \mu_{z_i} \rVert_2^2$. Step 2 cannot raise J, because each point moves to a center at the same or a smaller distance. Step 3 cannot raise J, because the mean minimizes the squared distances for fixed assignments. So J never rises from one step to the next.

### Different runs, different answers

The review runs k-means twice on the same data {1, 3, 5, 9} with k = 2 ([[F26-midterm-review-234p]], p. 36):

| Run | Centers | J |
| --- | --- | --- |
| A | μ1 = 2, μ2 = 7 | 1 + 1 + 4 + 4 = 10 |
| B | μ1 = 3, μ2 = 9 | 4 + 0 + 4 + 0 = 8 |

"Repeating the assignment and mean steps changes neither run." Run B has the lower total, 8 against 10, "so it wins this comparison." But "Comparing two converged runs does not prove global optimality." ([[F26-midterm-review-234p]], p. 36)

Synthesis: Run A groups {1, 3} and {5, 9}. Run B groups {1, 3, 5} and {9}. Both are stable, so the result of k-means depends on the start. To compare runs, compute J for each run and keep the run with the lowest J. The lowest J found is still not a proof of the global minimum.

### The shape assumption

- In k-means, only the center matters. This is equivalent to an assumption of spherically symmetric clusters ([[Block 2 Slides]], p. 199).
- k-means can use a weighted Euclidean distance. But the weights must be known, and all clusters still get the same axis-aligned ellipse ([[Block 2 Slides]], p. 199).
- k-means fails on clusters of very different sizes, on overlapping clusters, and on clusters with different shapes or orientations ([[Block 2 Slides]], p. 200).
- Students must be able to name a case where the shape assumption fails ([[Block 2 Slides]], p. 211).

### Learning goals

Describe the input (unlabeled observations) and output (labels) of a clustering algorithm; tell whether a task is supervised or unsupervised; cluster documents with k-means; and describe applications of clustering ([[Block 2 Slides]], p. 201). The deck credits the k-means section to Stanford CS 229 ([[Block 2 Slides]], p. 201).

### k-means at web scale: CuraWeb

- CuraWeb (June 2026) is a pretraining corpus built from 184.9 billion raw web documents ([[Block 2 Slides]], p. 202).
- It has two deduplication stages. MinHash removes documents by surface overlap and cuts 23.29B documents to 7.97B. Semantic deduplication then cuts them to 6.42B, another 19.4% ([[Block 2 Slides]], p. 202).
- k-means supports both halves of the pipeline. Semantic deduplication runs cluster by cluster on k-means output, and about 49,000 clusters later score diversity for sampling ([[Block 2 Slides]], p. 202).
- One assignment pass over 6.42B points against 49K centroids is roughly $3 \times 10^{14}$ distance computations, before the cost of the dimension ([[Block 2 Slides]], p. 202).
- Caveats on the slide: CuraWeb is arXiv v1 and not peer reviewed. Its 1.82-point gain comes from the whole pipeline and is not a k-means ablation. An ICLR 2026 paper reports that semantic deduplication alone scores below the raw corpus ([[Block 2 Slides]], p. 202).

### Baseline in LLM-guided clustering

In the few-shot clustering results, plain KMeans averages 76.7 on OPIEC59k and 82.7 on ReVerb45k. It scores 64.0 accuracy on Bank77, 77.7 on CLINC, and 57.5 on Tweet ([[Block 2 Slides]], p. 210, Tables 1-2). See [[Clustering]] for the LLM-guided variants that improve on it.

## Related

- [[Clustering]]: the task k-means solves
- [[k-Nearest Neighbors]]: also uses distance to points, but with given labels
- [[Machine Learning Task Types]]: supervised and unsupervised learning

## Sources

- [[Block 2 Slides]], pp. 194-202, 210-211
- [[F26-midterm-review-234p]], pp. 4, 30–36. Pp. 30–34 repeat Block 2 slides 194–198.
