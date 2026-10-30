---
id: con-rwnkm3
type: topic
kind: concept
description: The CSCI 566 grouping of ML tasks (supervised, unsupervised, reinforcement, semi-supervised, active), the few-shot, one-shot, and zero-shot settings for target data, and the task-experience-performance frame for a base model, an assistant, and an agent system.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Types of Learning
  - ML Tasks
  - Supervised and unsupervised learning
  - Task, Experience, Performance
  - Few-shot learning
  - One-shot learning
  - Zero-shot learning
  - Zero-Shot Learning With Semantic Labels
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
  - "Lecture 1"
  - "CSCI 566 Syllabus"
  - "[[Block 7 Slides]]"
up:
  - "[[Deep Learning]]"
---

> [!concept] Concept
> 5 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Deep Learning]]

## Definition

ML is the "Design and Analysis of algorithms that improve their performance at some task with experience" ([[Block 1 Slides]], p. 50, based on CMU 10701). The slides draw it as data (experience) → learning algorithm → knowledge (performance on task) (pp. 49–51).

The lecture groups ML tasks as follows (Lecture 1, § Broad ML Tasks; [[Block 1 Slides]], p. 53):

- **Supervised learning** learns from pairs of inputs and labels.
  - Classification: discrete labels, for example a news article → "Sports".
  - Regression: continuous labels, for example market information → a share price of "$24.50" (p. 54).
- **Unsupervised learning** learns from untagged or unlabeled data.
  - Density estimation, clustering, and dimensionality reduction.
  - Self-supervised learning, which the lecture notes and the Week 1 slides both list under this heading.
- **Reinforcement learning**
- **Semi-supervised learning**
- **Active learning**

Neither the lecture notes nor the Week 1 slides define active learning.

## Explanation

### Types by how much of Y is in the training data

A later slide gives a shorter list ([[Block 1 Slides]], p. 222; repeated in [[Block 3 Slides]], p. 7):

| Type | Training data |
| --- | --- |
| Supervised | desired output $Y$ in training data |
| Unsupervised | $Y$ not in training data |
| Weakly or semi-supervised | some of $Y$ in training data |
| Reinforcement | rewards based on a set of actions |

### Few-shot, one-shot, and zero-shot learning

These terms tell how many labelled examples of the target task the model gets. The Block 7 deck uses them in transfer learning, where the model first learns from source data ([[Block 7 Slides]], pp. 212, 225). See [[Transfer Learning]].

| Term | Labelled target examples | Page |
| --- | --- | --- |
| Few-shot | "a few examples" | p. 212 |
| One-shot | "one per class/task" | p. 212 |
| Zero-shot | none; the target classes are not in the training data | p. 225 |

- **Few-shot and one-shot.** The note "Few-shot: a few examples. One-shot: one per class/task." is on the model fine-tuning slide. On that slide, the source data $(x^s, y^s)$ is "A large amount" and the target data $(x^t, y^t)$ is "Very little". The slide warns: "only limited target data, so be careful about overfitting" ([[Block 7 Slides]], p. 212). See [[Fine-Tuning]] and [[Overfitting and Underfitting]].
- **Zero-shot.** Source data $(x^s, y^s)$ is the training data and target data $(x^t)$ is the testing data, and the two are "Different tasks". The example trains on cat and dog images and tests on alpaca images. "Unseen classes need semantic descriptions shared with known classes." Example: "alpaca = woolly coat, long neck, hooves." ([[Block 7 Slides]], p. 225)
- In the deck's transfer-learning grid, zero-shot learning fills the cell for labelled source data and unlabeled target data. [[Domain-Adversarial Training]] shares that cell ([[Block 7 Slides]], p. 224). The two differ in the task: domain-adversarial training keeps the same task, and only the data does not match ([[Block 7 Slides]], p. 220).

Other uses of these terms in the vault:

- [[CLIP]] gives the semantic description as a text prompt, so it can classify images zero-shot. [[Visual Anomaly Detection]] uses CLIP and WinCLIP in this way.
- Synthesis: few-shot prompting puts a few examples in the model's input and does not change the weights ([[In-Context Learning]]). The deck's few-shot setting instead fine-tunes the weights on the few target examples ([[Block 7 Slides]], p. 212).
- Few-shot clustering in [[Clustering]] is a different use of "few-shot": an LLM expands a few user examples into clustering constraints.

### Formal statements

- Supervised: given $X \in \mathcal{X}$, predict $Y \in \mathcal{Y}$. That is, construct a prediction rule $f: \mathcal{X} \to \mathcal{Y}$ ([[Block 1 Slides]], p. 54).
- Unsupervised, aka "learning without a teacher": given $X \in \mathcal{X}$, learn $f(X)$ (p. 55). Supervised learning maps observations to outcomes, such as transactions → fraud; unsupervised learning explores observations without outcomes (p. 56). Examples: the bias of a coin, the distribution of words in text (Shakespeare), and clusters of similar images (p. 57).
- Uses of unsupervised learning: outlier and out-of-distribution detection, model and data compression, and clustering (p. 58).

### Task, experience, and performance

- **Task**: the problem the learning algorithm must solve, such as image recognition, language translation, or game playing. It defines the scope of the problem (p. 52).
- **Experience**: the observed data. It is labeled data for supervised learning, rewards for reinforcement learning, and raw data for unsupervised learning. Its quality and quantity can change the learning outcome (p. 59).
- Experience is not test data. The example learns the stage of protein crystallization from six labeled images (crystal, needle, tree, empty), then asks about a new image (pp. 60–61, credited to CMU 10601).
- **Performance**: how well the algorithm does the task. For classification, the usual metrics are accuracy, precision, recall, and F1. It is evaluated on a test set or with cross-validation to assess generalization (p. 62). See [[Model Evaluation]].

### By system level

| Level | Task | Experience | Performance |
| --- | --- | --- | --- |
| Base model | predict tokens | broad token sequences | held-out loss / perplexity |
| Assistant | follow user intent | demonstrations + preferences | helpfulness / safety / preference evals |
| Agent system | reach goal in environment | prompt + observations from tools during run | correct end state + repeatability |

The table is in both the lecture notes and the Week 1 slides. The slides title it "One AI Product, Three Task-Experience-Performance Triples" and synthesize it from Brown et al. (NeurIPS 2020), Ouyang et al. (NeurIPS 2022), and Yao et al. (ICLR 2025) (Lecture 1, § Broad ML Tasks; [[Block 1 Slides]], p. 64).

Synthesis: the task-experience-performance definition is the common definition of learning credited to Tom Mitchell. Neither the lecture notes nor the slides name him.

Synthesis: each level is judged in a different way. A base model is judged by held-out loss. An agent system is judged by whether it reaches the correct end state each time. [[What Counts as Solved]] follows this change in the unit of evaluation.

The CSCI 566 Syllabus covers classical ML (decision trees, kNN, clustering) and model metrics in week 2, self-supervised learning in week 11, and reinforcement learning in week 12.

## Related

- [[Deep Learning]]
- [[Function Approximation]]: every task as a function $f(X) \to Y$
- [[Model Evaluation]]
- [[What Counts as Solved]]
- [[Autoregressive Language Modeling]]: the base-model level
- [[Post-Training]]: the assistant level
- [[Agent Loop]]: the agent-system level
- [[Transfer Learning]]: the setting of few-shot and zero-shot learning
- [[Fine-Tuning]]: training on a few labelled target examples
- [[Domain-Adversarial Training]]: the other method for unlabeled target data
- [[CLIP]]: zero-shot classification from text prompts
- [[In-Context Learning]]: few-shot prompting without weight updates

## Sources

- Lecture 1, § Broad ML Tasks
- [[Block 1 Slides]], pp. 49–64, 222
- [[Block 3 Slides]], p. 7
- CSCI 566 Syllabus, schedule
- [[Block 7 Slides]], pp. 212, 220, 224-225
