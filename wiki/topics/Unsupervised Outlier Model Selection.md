---
description: Unsupervised outlier model selection picks an outlier or out-of-distribution detector for a new dataset that has no labels, by meta-learning from historical labeled datasets; CSCI 566 Block 7 teaches it through MetaOD and MetaOOD.
aliases: [Unsupervised OD model selection, UOMS, Unsupervised model selection, Meta-learning for model selection, OD/OOD model selection]
sources: ["[[Block 7 Slides]]"]
subject: 1 Foundations and classical machine learning
---

## Definition

Unsupervised outlier model selection chooses a detector for a new dataset that has no labels. The Block 7 deck defines the terms in one table ([[Block 7 Slides]], p. 355):

| Term | Definition on the slide |
|---|---|
| Outlier detection (OD) | "Find observations unusual relative to a reference dataset." |
| Out-of-distribution (OOD) | "Identify inputs outside the reference distribution." |
| Model selection here | "Choose a detector for a new dataset without its labels." |

The same slide says: "Historical labeled tasks can teach this selection rule" (p. 355). The deck names the problem unsupervised OD model selection (UOMS) and marks it "[New]": "Given a new input dataset with no labels, select an OD model" ([[Block 7 Slides]], p. 364).

## Explanation

### The best detector varies: no free lunch

The slide title is "The *Best* Algorithm Varies by Applications". The slide states: "No free lunch theorem: no learning algorithm always outperforms." One side shows OD algorithms: kNN, LOF, and iForest. The other side shows applications: intrusion detection, rare disease, and high-energy physics. A question mark sits between the two sides ([[Block 7 Slides]], p. 357). Synthesis: no single detector is a safe default, so each new dataset needs a selection step.

### Without labels, evaluation-based search fails

Supervised model selection uses the ground truth y to evaluate each candidate. The slide lists "grid & random search by evaluation" and "bandit-based algorithm by evaluation". Its figure also shows Bayesian search, and labels all three "Model evaluation w/ labels" ([[Block 7 Slides]], p. 358). The next slide adds: "For unsupervised ML, there is no labels for evaluation" (p. 359). Synthesis: the search methods in Model Selection and Bayesian Optimization need a score for each trial, and an unlabeled OD dataset cannot supply that score.

### Meta-learning for model selection

The deck says meta-learning "focuses on learning to learn" and that it has two "definitions". One belongs to the deep learning context, and the lecture does not cover it. The other, "more classical" goal is to "learn a general model that can select model for arbitrary datasets" ([[Block 7 Slides]], p. 352). Meta-learning splits whole tasks, not samples. Historical datasets teach "how dataset properties relate to model performance". A new dataset tests model selection on an unseen task, and "Its hidden evaluation labels stay outside the selector." From this point, X_test means a new dataset at the task level (p. 353).

The deck explains the idea with images ([[Block 7 Slides]], pp. 360-363):

1. "Meta-learning helps select ML models for new tasks by prior experience." The question: "How to select a good ML model for wolf images without evaluation?" (p. 360)
2. We have dog images and labels, so we can evaluate models on them. We know the best model for dog images. "Dogs and wolves are similar → use the same model for wolves." The historical task "Can evaluate"; the new task "Cannot evaluate". The arrow between them reads "Transfer the best model(s)" (p. 361).
3. "Meta-learning helps new tasks by transferring from similar prior tasks." The first step is to "Identify similar datasets" (p. 362).
4. When fish images are the historical task, the slide crosses out the transfer to wolves: "Do not transfer the model from dissimilar datasets/tasks." The reason: "The best model(s) differ" (p. 363).

UOMS via meta-learning, marked "[1st time]", uses "prior knowledge to facilitate model selection on the new dataset". "The key is to measure dataset/task similarity" ([[Block 7 Slides]], p. 364).

### Problem formulation

The deck states the problem in two steps ([[Block 7 Slides]], pp. 365-369):

1. **Training on historical datasets.** A meta-train database holds n datasets: D_train = {D_1, D_2, ..., D_n}, where D_i = (X_i, y_i) (p. 365). A predefined OD model set holds m models: ℳ = {M_1, M_2, ..., M_m} (p. 366). Pairing the n datasets with the m models "(by evaluation)" gives the performance matrix P ∈ ℝ^(n×m) (p. 367). Each entry is one model's performance on one dataset. In the slide's example, M_1 on D_2 scores 0.5 ("Model 1's perf. on dataset 2") (p. 368).
2. **Model selection.** A new dataset D_test = (X_test, Ø) has no labels. The task is to select the model from ℳ with the highest performance (p. 368). Meta-learning transfers the knowledge in P to model selection on X_test (p. 369).

MetaOD solves this problem. It factorizes P and predicts the embedding of the new dataset. Its successor, MetaOOD, replaces handcrafted meta-features with LLM embeddings; see MetaOD, § MetaOOD.

The recap lists three steps of the "1st OD/OOD Model Selection Framework": (1) the problem formulation of UOMS by meta-learning, (2) data embedding and OD meta-features, and (3) language embeddings for datasets and models ([[Block 7 Slides]], pp. 393-395). The title on p. 393 says "OD/OOD". The titles on pp. 394-395 say only "OD".

### Automated OD/OOD algorithms

The deck closes the part with a summary table ([[Block 7 Slides]], p. 396). Here "yes" is a check mark on the slide, and "no" is a blank cell.

| Work | Year | Algorithm selection | HPO, continuous | HPO, discrete | Meta-learning | Training-free at test time |
|---|---|---|---|---|---|---|
| IPM | 2021 | yes | yes | yes | no | no |
| MetaOD | 2021 | yes | no | yes | yes | yes |
| ELECT | 2022 | yes | no | yes | yes | no |
| HPOD | 2022 | N/A | yes | yes | yes | no |
| ADGym | 2023 | yes | yes | yes | yes | yes |
| Hyper | 2024 | N/A | yes | yes | yes | yes |
| MetaOOD | 2025 | yes | no | no | yes | yes |

The table gives no authors or venues for IPM, ELECT, HPOD, ADGym, and Hyper. Synthesis: in this table, only ADGym has a check in every column.

### Model selection by LLMs

The outline names "Model Selection by LLMs" as the third section of the part: "Leverage LLMs in model selection", with MetaOOD (ICLR 2025) and AD-LLM (preprint) ([[Block 7 Slides]], p. 354). The deck covers MetaOOD on pp. 383-392. A later slide says "MetaOD and MetaOOD illustrated choosing a model for a new dataset", and its footnote says "AD-LLM case: Block 10" (p. 397).

## Related

- MetaOD: the method that solves UOMS, and its successor MetaOOD
- Model Selection: model selection when labels are available
- AutoML
- [[Transfer Learning]] (synthesis: meta-learning here transfers the best models from similar datasets)
- Machine Learning Task Types: lists outlier and out-of-distribution detection as uses of unsupervised learning
- Visual Anomaly Detection: outlier detection on images
- [[k-Nearest Neighbors]]: the slide lists kNN as an OD algorithm (p. 357)
- Yue Zhao: the instructor, author of MetaOD, MetaOOD, and the PyOD library

## Sources

- [[Block 7 Slides]], pp. 352-355, 357-369, 393-397
