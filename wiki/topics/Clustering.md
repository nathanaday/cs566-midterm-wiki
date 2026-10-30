---
id: con-xx1gx7
type: topic
kind: concept
description: Clustering is the unsupervised task of grouping unlabeled observations by their inputs alone; CSCI 566 covers the center-and-spread view of a cluster, the clusters that are hard to find, and how an LLM can replace most of the human feedback in semi-supervised clustering.
tags: [machine-learning/cs566-deeplearning]
aliases: [cluster analysis, unsupervised clustering, Unsupervised learning, Semi-supervised clustering, constrained clustering, LLM-guided few-shot clustering, few-shot clustering, LLMs for clustering, Keyphrase Clustering, LLM Correction, PCKMeans, Large language models enable few-shot clustering]
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

Clustering discovers groups (clusters) of related items, for example Sports and World News articles ([[Block 2 Slides]], pp. 184-185). It is an unsupervised learning task: it uses inputs X only, with no labels Y ([[Block 2 Slides]], p. 188). In the words of the slide: "No labels provided", "uncover cluster structure from input alone" ([[Block 2 Slides]], p. 189; repeated in [[F26-midterm-review-234p]], p. 29). The input is documents as vectors $x_i$, and the output is cluster labels $z_i$ ([[Block 2 Slides]], p. 189; [[F26-midterm-review-234p]], p. 29, credited to Stanford CS 229). When the labels are known, the task becomes classification on a labeled training set ([[Block 2 Slides]], p. 188).

## Explanation

### Clustering and supervised learning

- Unsupervised learning infers labels $z_i$. Supervised learning has given labels $y_i$ ([[Block 2 Slides]], p. 196).
- Clustering and classification differ by what the task gives you. Clustering gets unlabeled observations and outputs labels ([[Block 2 Slides]], pp. 201, 211).

See [[Machine Learning Task Types]] for the full list of task types.

### What defines a cluster

- A cluster is defined by a center and a shape or spread ([[Block 2 Slides]], p. 190).
- An observation $x_i$ goes to cluster k if its score under cluster k is lower than under the other clusters. For simplicity, the score is often the distance to the cluster center, which ignores shape ([[Block 2 Slides]], p. 190). [[k-Means]] uses this score.
- Cluster structure can be easy, impossible, or in between to recover without labels ([[Block 2 Slides]], p. 191). Hard cases include two spirals, a cluster inside a cluster, corners, half-kernel, crescent and full moon, and outliers ([[Block 2 Slides]], pp. 192-193).

### Application: user preferences

Feedback on the clustered documents that a user reads gives a preference distribution over topics ([[Block 2 Slides]], pp. 186-187).

### Semi-supervised clustering

- Unsupervised clustering groups data automatically, but the groups may not match what the user expects ([[Block 2 Slides]], p. 203).
- In semi-supervised clustering, users give guidance such as constraints or seed points ([[Block 2 Slides]], p. 203). Humans supply "must-link" and "cannot-link" constraints ([[Block 2 Slides]], p. 207).
- This needs a lot of user feedback, so it costs many resources and much time ([[Block 2 Slides]], p. 204). The slide sums up: traditional methods either lack intelligence (unsupervised) or need too much expert labeling (semi-supervised) ([[Block 2 Slides]], p. 203).

### LLM-guided few-shot clustering

The deck follows Viswanathan, Gashteovski, Lawrence, Wu, and Neubig, "Large language models enable few-shot clustering", TACL 12, 321-333 (2024) ([[Block 2 Slides]], pp. 203-210). The core idea: the LLM simulates expert feedback. The user gives a small amount of input, and the LLM turns it into a large amount of pseudo-feedback, so clustering needs fewer user interventions ([[Block 2 Slides]], pp. 204-205). The paper uses the LLM at three stages ([[Block 2 Slides]], p. 205):

1. **Before clustering: keyphrase expansion.** Word embeddings can miss key information. The LLM generates keyphrases for each text, and the final input vector is the text vector plus the keyphrase vector ([[Block 2 Slides]], p. 206). For "How do I locate my credit card?" the LLM gives ['card status', 'card location'] ([[Block 2 Slides]], p. 206).
2. **During clustering: LLM as pseudo-oracle.** The LLM, not a human, generates must-link and cannot-link constraints from a few examples. This reduces manual annotation ([[Block 2 Slides]], p. 207).
3. **After clustering: correction.** Run regular clustering such as k-means, find low-confidence points that could belong to more than one cluster, and ask the LLM to reassign them ([[Block 2 Slides]], p. 208). For each such point, the LLM first judges whether the current assignment is correct. If not, it picks among the top-5 nearest clusters ([[Block 2 Slides]], p. 209, Figure 3).

The paper evaluates entity canonicalization (OPIEC59k, ReVerb45k) and text clustering (Bank77, CLINC, Tweet) against CMVC, SCCL, and ClusterLLM baselines ([[Block 2 Slides]], p. 210, Tables 1-2). Reported results ([[Block 2 Slides]], p. 210, Tables 1-2):

- KMeans baseline: 76.7 average on OPIEC59k, 82.7 on ReVerb45k; accuracy 64.0 on Bank77, 77.7 on CLINC, 57.5 on Tweet.
- Keyphrase clustering: 80.0 on OPIEC59k, 84.2 on ReVerb45k; 65.3 accuracy and 82.4 NMI on Bank77.
- PCKMeans with LLM constraints: 79.6 accuracy on CLINC; 65.3 accuracy and 85.1 NMI on Tweet (KMeans: 57.5 and 80.6).
- LLM correction: 78.4 on OPIEC59k, 82.5 on ReVerb45k.

The slide calls keyphrase generation the most effective approach and says it improves clustering quality on all datasets. The pseudo-oracle works well, most of all when the LLM can make strong similarity judgments. Correction has limited impact, with a smaller gain than the other two ([[Block 2 Slides]], pp. 208, 210).

## Related

- [[k-Means]]: the standard clustering algorithm and the baseline above
- [[Machine Learning Task Types]]: supervised, unsupervised, and semi-supervised learning
- [[k-Nearest Neighbors]]: the supervised counterpart that also relies on distance

## Sources

- [[Block 2 Slides]], pp. 184-211
- [[F26-midterm-review-234p]], p. 29, which repeats Block 2 slide 189
