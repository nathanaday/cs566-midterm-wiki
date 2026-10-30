---
id: doc-sk9hey
type: topic
kind: concept
description: AutoML (automated machine learning) automates the choice of algorithms and hyperparameters, so a search loop finds an "optimal" model in a large model space; CSCI 566 sorts it into hyperparameter tuning or algorithm selection, meta learning, and neural architecture search.
tags: [machine-learning/cs566-deeplearning]
aliases: [Automated ML, Automated machine learning, Neural architecture search, NAS, Model search, Algorithm search]
created: 2026-10-12T16:58:10
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 7 Slides]]"]
up: ["[[Model Selection]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Model Selection]]

## Definition

"The key of AutoML is to automate the selection process of algorithms and hyperparameters" ([[Block 7 Slides]], p. 316). The deck also says: "AutoML helps us to find an 'optimal' model in large model space" ([[Block 7 Slides]], pp. 320–322).

## Explanation

### Models are algorithms plus hyperparameters

The deck says that the key elements in ML pipelines are (i) algorithms and (ii) hyperparameters ([[Block 7 Slides]], p. 314). It puts algorithms into three groups ([[Block 7 Slides]], p. 314):

1. Data preprocessing algorithms, for example dimensionality reduction like PCA.
2. Classical ML algorithms, for example kNN, logistic regression, and random forests.
3. Modern ML algorithms (deep learning), for example RNN, LSTM, and CNN.

After you choose an algorithm, you must choose its hyperparameters. Examples are the number of principal components for PCA, the number of nearest neighbors for kNN, the number of base trees for random forests, and the learning rate and dropout rate for deep learning ([[Block 7 Slides]], p. 315).

Hyperparameters are "specific settings of a selected algorithm". "Models are the combination of algorithms and hyperparameters", for example {Decision tree, tree_depth=5} and {kNN, n_neighbors=10} ([[Block 7 Slides]], p. 319).

### The search loop

AutoML automates repeated modeling decisions in a loop ([[Block 7 Slides]], p. 312):

1. Propose a configuration.
2. Train and evaluate it.
3. Use the results to choose the next trial.

The slide adds: "The search still needs a trustworthy evaluation protocol" ([[Block 7 Slides]], p. 312). For the flower classifier, you could try different learning rates, regularizers, and model choices. Each trial chooses a setting, trains the model, and measures validation performance. "AutoML organizes this repeated search" ([[Block 7 Slides]], p. 313). See [[Flower Classifier Running Example]].

A diagram shows the same loop at a higher level. A task goes into "meta-level learning and optimization", which "chooses architecture and hyperparameters" and produces models. The performance of the models goes back into the meta-level step ([[Block 7 Slides]], p. 316).

In hyperparameter optimization for the flower classifier, training data fits each candidate. Validation data compares candidates "under the same metric and budget". Test data evaluates the selected procedure after tuning ends. "The test score remains outside the search loop" ([[Block 7 Slides]], p. 326). See [[Test Set Contamination]].

### Three situations

| Situation | What varies | Example models | Locator |
|---|---|---|---|
| 1: reduced to hyperparameter search | Same algorithm; search for the best hyperparameters | {Decision tree, tree_depth=3}, {Decision tree, tree_depth=5}, {Decision tree, tree_depth=10} | p. 320 |
| 2: reduced to algorithm search | Different algorithms with their default hyperparameters; search for the best model ("merely algorithm") | {Decision tree, default hyperparameters}, {kNN, default hyperparameters}, {Logistic regression, default hyperparameters} | p. 321 |
| 3: both | Different algorithms with varying hyperparameters; search for the best model and its algorithm(s) | {Decision tree, tree_depth=5}, {Decision tree, tree_depth=10}, {kNN, n_neighbors=5}, {kNN, n_neighbors=10} | p. 322 |

All rows cite [[Block 7 Slides]].

### Algorithm choice as a hyperparameter

"Most of the methods introduced in this lecture can be used for model search, although they may be put under hyperparameter search or algorithm search" ([[Block 7 Slides]], p. 323). "The selection of algorithms (kNN, Decision Tree, etc.) can also be viewed as a 'hyperparameter' of the ML pipeline" ([[Block 7 Slides]], p. 323). When a person selects the algorithm and tunes only its hyperparameters, human knowledge (priors) fixes the algorithm and restricts the search space ([[Block 7 Slides]], p. 323).

The deck gives two reasons to do hyperparameter search only ([[Block 7 Slides]], pp. 323–324):

1. The search space is smaller, so the optimization is easier.
2. The difference between algorithms can be large. If the search includes the algorithm choice, "the search process will be less smooth", especially for learning-based algorithms.

A figure compares a "smooth(er) objective" surface with a "nonsmooth objective" surface ([[Block 7 Slides]], p. 324).

### Three buckets

The slide says that deep learning may have more flexible architectures than classical ML models, so "people typically categorize AutoML into *three* buckets" ([[Block 7 Slides]], p. 316):

1. HP tuning and/or algorithm selection for a single dataset. The slide marks this bucket "(covered in this lecture)".
2. Meta learning (learning to learn): "generalize to many different datasets".
3. Neural architecture search, which "may be considered as a subarea/combination of 1&2".

Open point: the slide says only bucket 1 is covered, but the same deck later teaches meta learning ("Part 2", p. 352) and neural architecture search ("P3", p. 398) ([[Block 7 Slides]]). This topic does not resolve the difference.

For bucket 1 with one dataset and one algorithm, the deck recommends random and grid search "if cheap evaluation is possible", and Bayesian optimization "if evaluation is expensive, and the optimization is restricted" ([[Block 7 Slides]], p. 325). See [[Model Selection]] and Bayesian Optimization.

### What AutoML automates, and what people still define

"An automated search still follows a task and evaluation protocol" ([[Block 7 Slides]], p. 317). A modeling system can automate three kinds of choices ([[Block 7 Slides]], p. 317):

| Choice | What the system does |
|---|---|
| Preprocessing choices | Compare suitable transformations within the pipeline. |
| Model and training choices | Search architectures or training hyperparameters. |
| Resource allocation | Decide which trials deserve more compute. |

"People still define the task, data boundaries and success metric" ([[Block 7 Slides]], p. 317).

### Search budget

"A Search Budget Is Part of the Problem" ([[Block 7 Slides]], p. 332). The example assumes compute for ten full training runs. You can use it in two ways:

- Evaluate fewer candidates fully. You get more evidence about each one, but you explore fewer settings.
- Screen more candidates briefly. You explore more broadly, but "early rankings may be misleading".

"Cheap early evaluations can guide a later, longer evaluation" ([[Block 7 Slides]], p. 332).

### Cost, and ensembles as an alternative

The deck warns that "AutoML is not necessarily superior to human selection" ([[Block 7 Slides]], p. 318):

- Human selection of algorithm and hyperparameters is based on "prior knowledge" and "historical information" of the problem.
- Software and hardware limits, "especially the cost", can make AutoML impossible. "AutoML is often costly to run."

The alternative on the same slide is ensemble learning, which the slide calls stable and robust. If you do not know how to select the algorithms and hyperparameters, you can build multiple models at random with different hyperparameters and combine them, for example by taking the average. The drawback: "building many diversified models may be slow for prediction" ([[Block 7 Slides]], p. 318).

### Meta learning

The slide says there are "generally two 'definitions'" of meta-learning. The deep learning definition (Lilian Weng's 2018 post) is not covered. The classical goal is to "learn a general model that can select model for arbitrary datasets" ([[Block 7 Slides]], p. 352).

Meta-learning splits whole tasks, not only samples. Historical datasets teach how dataset properties relate to model performance. Model selection is then tested on a new, unseen dataset, and its hidden evaluation labels stay outside the selector. "Later X_test means a new dataset at the task level" ([[Block 7 Slides]], p. 353).

"Meta-learning helps select ML models for new tasks by prior experience" ([[Block 7 Slides]], p. 360). In the example, historical tasks have labeled dog images, so their model performance can be evaluated. The new task has wolf images without labels, so performance cannot be evaluated. Dogs and wolves are similar, so the method uses the best dog model for wolves ([[Block 7 Slides]], p. 361). "Meta-learning helps new tasks by transferring from similar prior tasks": it identifies similar datasets and transfers the best model(s) ([[Block 7 Slides]], p. 362). It does not transfer from dissimilar tasks, such as fish to wolves, because "The best model(s) differ" ([[Block 7 Slides]], p. 363). The deck applies this to outlier detection; see [[Unsupervised Outlier Model Selection]] and [[MetaOD]].

### Neural architecture search

MetaOD and MetaOOD showed how to choose a model for a new dataset. Architecture choices (layer count, widths, connections) define one candidate network. The next step is to "search the architecture as another model configuration" ([[Block 7 Slides]], p. 397).

"Neural nets may be considered as a computational graph, and most of time it is sequential" ([[Block 7 Slides]], p. 398). Neural architecture search (NAS) tries to decide ([[Block 7 Slides]], p. 398):

1. The number of layers.
2. The types of layers: dense, conv, pooling.
3. The hyperparameters of the layers.
4. Branching, joins, and skips.

"HPO methods can search architecture choices." The strategies are "random, evolution, RL and gradient-based search" ([[Block 7 Slides]], p. 398).

### Comparing searches, and NAS benchmarks

"Compare searches under matched tasks, search spaces and compute budgets" ([[Block 7 Slides]], p. 399). The slide lists ([[Block 7 Slides]], p. 399):

| Item | What the slide says |
|---|---|
| Search-space coverage | "A benchmark measures a defined set of candidate architectures." |
| NAS-Bench-101 | "A public benchmark for reproducible architecture-search experiments." |
| NAS-Bench-201 | "Extends benchmarking to multiple datasets and richer diagnostics." |

"A benchmark result has limits set by its evaluation conditions" ([[Block 7 Slides]], p. 399).

Synthesis: a search result is valid only for its task, search space, budget, and evaluation protocol. Compare two searches only when those four match.

## Related

- [[Model Selection]]: choosing a model family and its hyperparameters by hand
- Bayesian Optimization: bucket 1 when evaluation is expensive
- [[Unsupervised Outlier Model Selection]]: meta learning for model selection without labels
- [[MetaOD]]: a meta-learning model selector
- [[Flower Classifier Running Example]]
- [[Test Set Contamination]]: why the test score stays outside the search loop
- [[k-Nearest Neighbors]]: an example algorithm, with n_neighbors as its hyperparameter

## Sources

- [[Block 7 Slides]], pp. 312–326, 332, 352–353, 360–363, 397–399
