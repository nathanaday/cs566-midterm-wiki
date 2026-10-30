---
description: Outlier detection finds the observations that differ significantly from the rest of a dataset, usually without labels; the kNN detector scores each point by the distance to its k-th nearest neighbor and flags the points with the largest scores, the points with the fewest close neighbors.
aliases: [Anomaly Detection, Outlier, Anomaly, OD, kNN outlier detection, k-th nearest neighbor distance, Outlier score, Out-of-distribution detection, OOD detection, Novelty detection]
sources: ["[[Block 1 Slides]]", "[[Block 2 Slides]]", "[[Block 6 Slides]]", "[[Block 7 Slides]]", "[[CSCI 566 Midterm (Spring 2024)]]"]
subject: 1 Foundations and classical machine learning
---

## Definition

Outlier detection (OD) finds "observations unusual relative to a reference dataset" ([[Block 7 Slides]], p. 355). The sample midterm defines an outlier the same way: a data point that differs significantly from the other observations in the dataset ([[CSCI 566 Midterm (Spring 2024)]], Q39). The decks file the task under unsupervised learning, next to clustering and compression ([[Block 1 Slides]], p. 58), and the detector they describe is the kNN detector, which uses the "$k$-th nearest neighbor distance as the outlier score" ([[Block 7 Slides]], p. 290).

## Explanation

### Why it recurs in this course

The instructor's research is "anomaly/OOD detection in data" together with trust evaluation of foundation models and audit of agent systems, through the FORTIS Lab at USC ([[Block 1 Slides]], p. 4). The lab's flagship project is PyOD, an "Anomaly-detection library; the lab's OOD / reliability anchor", with PyGOD as its sister library for graph outlier detection (p. 5). Block 7 devotes two research examples to the subject: TOD, a GPU system for outlier detection (pp. 288-310), and MetaOD, a method for choosing a detector without labels (pp. 356-396). The schedule places a full lecture on "out-of-distribution and anomaly detection" in week 11, after the midterm (p. 22).

### What an outlier is

The deck's one-table definition separates two tasks ([[Block 7 Slides]], p. 355):

| Task | Deck definition |
| --- | --- |
| Outlier detection (OD) | "Find observations unusual relative to a reference dataset." |
| Out-of-distribution (OOD) detection | "Identify inputs outside the reference distribution." |

Block 1 lists "Outlier/Out-of-distribution (OOD) detection" as an unsupervised task, with rare disease and fake news as the examples ([[Block 1 Slides]], p. 58). The word also appears on the supervised side: an overfit model is one that fits "the noise in the data or fitting 'outliers'" ([[Block 2 Slides]], p. 84), and a cluster with a few scattered points around it is one of the hard clustering cases (p. 193).

Synthesis: the exam's distractors are the three things an outlier is not. It is not an error in data collection, although a collection error can produce one. It is not a point inside the normal range. It is not the most frequent value. An outlier is defined by its relation to the rest of the data, so the same point can be normal in one dataset and an outlier in another.

### Why detection is unsupervised

Outliers are rare and labels for them are scarce, so the decks treat OD as unsupervised: a detector sees the inputs $\mathbf{X}$ and no $\mathbf{y}$. Block 7 makes the consequence explicit for model selection. With ground-truth labels one can run grid search, random search, or a bandit over detectors and pick the best by evaluation; "For unsupervised ML, there is no labels for evaluation" ([[Block 7 Slides]], pp. 358-359). The new dataset in the model-selection problem is written $\mathbf{D}_{test} = (\mathbf{X}_{test}, \emptyset)$, inputs with no labels (p. 368).

Synthesis: the decks state that OD is unsupervised and do not say why. The usual reasons are that outliers are too rare to label in bulk, that future outliers need not resemble past ones, and that the point of the task is often to find what nobody has labeled yet. The meta-learning method of [[Unsupervised Outlier Model Selection]] is a way around the missing labels on the new dataset, since it uses historical datasets that do have labels (p. 365).

### The kNN detector

The decks give the kNN detector in one slide box: "$k$NN: $k$-th nearest neighbor distance as the outlier score." The figure shows a blue outlier point whose three nearest neighbors (k = 3) sit far away in two separate clusters of normal yellow points, so its score is large, and it notes a "Dependency: Need all samples for pairwise dist." ([[Block 7 Slides]], p. 290). This is the whole of the deck's description of a basic detector. The rest of this section is background.

Synthesis: the method, written out.

1. Pick a distance $d$ and an integer $k$, as for the kNN classifier ([[Block 2 Slides]], p. 182).
2. For each point $x_i$ in the dataset, find its $k$ nearest other points under $d$.
3. Score the point by the distance to its $k$-th nearest neighbor, $s(x_i) = d(x_i, x_{(k)})$. A common variant uses the mean distance to the $k$ neighbors instead.
4. Rank the points by score. The points with the largest scores are the outliers; either report the top $n$ or threshold the score.

A point with a large score has no close neighbors: the $k$ nearest points are all far away. A point with a small score sits in a dense region, where $k$ neighbors are found within a short radius. The score therefore measures the inverse of local density, and the exam phrases the rule that way: the outliers are the points with the lowest density of neighbors ([[CSCI 566 Midterm (Spring 2024)]], Q40). Every point in the dataset is scored against the same dataset, which is why the slide says all samples are needed for the pairwise distances.

Synthesis: the deck's complexity table follows from the pairwise step. Scoring $n$ points needs all $n^2$ pairwise distances, so the kNN detector is listed at $O(n^2)$ time and $O(n^2)$ space ([[Block 7 Slides]], pp. 289-290). TOD's answer is to express the detector as the tensor operators `cdist` (pairwise distances) and `topk` (the $k$ smallest per row) and run them on GPUs (pp. 296-299).

### Choosing k and the distance

The two hyperparameters are the same two the kNN classifier needs, $k$ and the distance function, and the deck's advice is the same: they are "Very problem/dataset-dependent. Must try them all out and see what works best" ([[Block 2 Slides]], p. 165). Euclidean (L2) distance is the common choice and Manhattan (L1) the usual alternative (p. 150), and kNN is affected by feature scale (p. 181), so the features need scaling first ([[Data Preprocessing]]).

Synthesis: in the detector, $k$ sets how large a group can be before it counts as normal. With $k = 1$, two outliers that happen to sit next to each other each get a small score, because each is the other's nearest neighbor. A larger $k$ requires a point to have $k$ close companions before its score is small, so small clumps of outliers are caught, at the price of flagging the edges of small genuine clusters. There is no validation accuracy to tune $k$ against, since there are no labels; this is the model-selection problem that [[Unsupervised Outlier Model Selection]] addresses.

### Other detector families

The decks name other detectors without explaining them. The complexity table lists COF, LOF, KDE, LOCI, and OCSVM beside kNN (p. 289), the tensor-transpilation slide lists kNNOD, ABOD, COF, LOF, LOCI, HBOS, SOD, COPOD, ECOD, FB, LSCP, MetaOD, SUOD, LODA, and PCA (p. 299), and the no-free-lunch slide pairs kNN, LOF, and iForest with intrusion detection, rare disease, and high-energy physics to make the point that no detector wins on every application (p. 357). The operator decomposition groups them by what they compute: kNN uses neighbors, LOF uses density estimation, ABOD uses cosine similarity, and PCA uses the SVD (pp. 296-299).

Synthesis: three families cover most of that list. Distance-based detectors, kNN among them, score a point by how far its neighbors are. Density-based detectors such as LOF compare a point's local density with its neighbors' densities, so a point at the edge of a sparse cluster is not flagged just because the cluster is sparse. Clustering-based detectors run a clustering algorithm first and flag the points far from every center or in tiny clusters; the [[k-Means]] score, distance to the nearest center, is the simplest case. Isolation Forest (iForest) is a tree method that isolates outliers in few random splits. None of these is in the decks beyond its name.

### Relation to kNN classification and to clustering

The kNN classifier and the kNN detector share the neighbor search, the distance function, and the hyperparameter $k$, and both pay their cost at prediction time rather than training time ([[Block 2 Slides]], pp. 181-182). They differ in what they read off the neighbors. The classifier takes a majority vote over the neighbors' labels (p. 148); the detector ignores labels and reads the distance to the neighbors ([[Block 7 Slides]], p. 290). See [[k-Nearest Neighbors]] for the classifier and [[kNN Regression]] for the version that averages the neighbors' values.

Both OD and [[Clustering]] are unsupervised tasks on inputs alone ([[Block 1 Slides]], p. 58). Clustering asks which points belong together; OD asks which points belong nowhere. The clustering deck's own hard cases include a panel of a cluster with outliers around it ([[Block 2 Slides]], p. 193), and the kNN detector is exactly a rule for finding those scattered points. On graphs, "Anomalous node detection" is one of the downstream tasks that node embeddings serve, beside node classification, link prediction, and clustering ([[Block 6 Slides]], p. 44; see [[Node Embeddings]]).

### The Block 7 research thread

Block 7 treats OD at the research level, in two optional examples (p. 272).

- **TOD** (VLDB 2023) is a tensor-based, multi-GPU OD system (p. 288). The motivation is the $O(n^2)$ or worse cost of the detectors above and their dependency on all samples (pp. 289-290). The system decomposes diverse detectors into a small set of shared tensor operators (pp. 296-299), then fits them in GPU memory with provable quantization, automatic batching, and multi-GPU support (pp. 300-310). The memory problem is concrete: the distance matrix for 200k samples in 32-bit precision takes about 160 GB against the 80 GB of an A100 (p. 300).
- **MetaOD** (NeurIPS 2021) answers a different question: given a new dataset with no labels, which detector should run on it? The best detector varies by application (p. 357), and labels for evaluation are missing (p. 359), so MetaOD meta-learns the choice from a performance matrix of historical labeled datasets against a model set (pp. 364-369). The recap reports that it picks on average the top 18% model out of 300 or more in at most a second for most datasets (p. 393). MetaOOD (2025) extends the idea to OOD detectors with LLM-generated data and model features (pp. 383-396). The full method is in [[Unsupervised Outlier Model Selection]].

## Exam Questions

**Q39.** What is an outlier in machine learning and data mining? Answer: B, a data point that differs significantly from the other observations in the dataset ([[CSCI 566 Midterm (Spring 2024)]], Q39). The definition is relational: the deck's phrase is "unusual relative to a reference dataset" ([[Block 7 Slides]], p. 355). Option A (a collection error) describes one cause of outliers, not what they are. Options C (inside the normal range) and D (the most frequent point) describe normal points.

**Q40.** When kNN is used for outlier detection, how are outliers determined? Answer: B, the outliers are the points with the lowest density of neighbors ([[CSCI 566 Midterm (Spring 2024)]], Q40). The kNN detector scores each point by the distance to its $k$-th nearest neighbor ([[Block 7 Slides]], p. 290); a large distance means few neighbors nearby, which is low local density. Option A inverts the rule, option C describes the most central points, and option D describes points that fit in with their neighbors, the opposite of an outlier.

## Related

- [[k-Nearest Neighbors]]: the classifier that shares the neighbor search, $k$, and the distance function
- [[kNN Regression]]: the third use of the same neighbor search
- [[Clustering]]: the sibling unsupervised task; its hard cases include a cluster with outliers
- [[k-Means]]: distance to the nearest center is the simplest clustering-based outlier score
- [[Unsupervised Outlier Model Selection]]: how to choose a detector when the new dataset has no labels
- [[Data Preprocessing]]: feature scaling before any distance-based method
- [[Overfitting and Underfitting]]: an overfit model fits the outliers
- [[Node Embeddings]]: anomalous node detection as a downstream task on graphs

## Sources

- [[Block 1 Slides]], pp. 4-5, 22, 53, 58
- [[Block 2 Slides]], pp. 84, 148, 150, 165, 181-182, 193
- [[Block 6 Slides]], p. 44
- [[Block 7 Slides]], pp. 272, 288-290, 296-300, 310, 355-359, 364-369, 393, 396
- [[CSCI 566 Midterm (Spring 2024)]], Q39, Q40
