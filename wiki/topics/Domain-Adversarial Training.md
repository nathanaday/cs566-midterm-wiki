---
id: doc-cd3q3x
type: topic
kind: concept
description: "A transfer method for one task with labelled source data and unlabeled, mismatched target data: a feature extractor, a label predictor, and a domain classifier, joined by a gradient reversal layer, train features that predict labels but cannot be told apart by domain."
tags: [machine-learning/cs566-deeplearning]
aliases: [Domain-adversarial training, DANN, Domain-Adversarial Training of Neural Networks, Gradient reversal layer, GRL, Domain shift, Domain change, Domain mismatch, MNIST-M, MNIST to MNIST-M]
created: 2026-10-12T16:58:10
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 7 Slides]]"]
up: ["[[Transfer Learning]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Transfer Learning]]

## Definition

Domain-adversarial training is a transfer-learning method for one task and two kinds of data: labelled source data, and unlabeled target data that does not match it ([[Block 7 Slides]], pp. 219-220). Its goal: "Make features useful for labels and difficult to separate by domain." ([[Block 7 Slides]], p. 221)

## Explanation

### The setting

- Source data $(x^s, y^s)$ is the training data. Target data $(x^t)$ is the testing data. The slide marks the pair "Same task, mismatch" ([[Block 7 Slides]], p. 220).
- Example: MNIST is the source, "with label". MNIST-M is the target, "without label" ([[Block 7 Slides]], p. 220). The slide shows MNIST as white digits on black, and MNIST-M as colored digits on colored image patches.
- The deck's transfer-learning overview is a grid of source data (labelled or unlabeled) against target data (labelled or unlabeled). Domain-adversarial training fills the cell for labelled source data and unlabeled target data, and zero-shot learning shares that cell. Fine-tuning and multitask learning fill the cell for labelled source data and labelled target data ([[Block 7 Slides]], pp. 219, 224). The grid is credited to Hung-yi Lee at NTU. Its first version warns: "different terminology in different literature" ([[Block 7 Slides]], p. 211).
- Domain-adversarial training and zero-shot learning differ in the task. In domain-adversarial training, the task stays the same and only the data does not match (p. 220). In zero-shot learning, the source and target are "Different tasks" ([[Block 7 Slides]], p. 225). See [[Machine Learning Task Types]].

### Domain shift

Domain shift is the mismatch between the source data and the target data. The slide title is "Transfer Can Fail When the Domain Changes": "A model trained on everyday photos may miss specialized visual features." ([[Block 7 Slides]], p. 215)

| Source and target | What may happen |
| --- | --- |
| Similar | "Some shapes, textures and object parts may transfer usefully." |
| Different | "Microscopy or unusual sensors may need different representations." |

The slide's advice: "Check target-domain performance before trusting reuse." ([[Block 7 Slides]], p. 215)

### The network

The network has three parts. "This is a big network, but different parts have different goals." ([[Block 7 Slides]], pp. 221-222)

| Part | Goal |
| --- | --- |
| Feature extractor | "Maximize label classification accuracy + minimize domain classification accuracy" (p. 222) |
| Label predictor | "Maximize label classification accuracy" (p. 221) |
| Domain classifier | "Maximize domain classification accuracy" (p. 221) |

The feature extractor must "Confuse domains while preserving labels" ([[Block 7 Slides]], p. 221). The next slide puts it this way: "Not only cheat the domain classifier, but satisfying label classifier at the same time" ([[Block 7 Slides]], p. 222).

### Gradient reversal layer

A gradient reversal layer sits between the features $f$ and the domain classifier. The slide shows these gradients ([[Block 7 Slides]], p. 223):

- The label predictor $\theta_y$ gets $\partial L_y / \partial \theta_y$ from the label loss $L_y$.
- The domain classifier $\theta_d$ gets $\partial L_d / \partial \theta_d$ from the domain loss $L_d$.
- The feature extractor $\theta_f$ gets $\partial L_y / \partial \theta_f$ from the label loss. It gets $-\lambda \, \partial L_d / \partial \theta_f$ from the domain loss, through the gradient reversal layer.

The slide does not define $\lambda$ or say how to set it. The slide states the result: "Domain classifier fails in the end. It should struggle …… do not know if it from source or target" ([[Block 7 Slides]], p. 223).

Synthesis (not in the deck): the domain classifier learns to lower $L_d$, and the reversed gradient pushes the feature extractor to raise $L_d$. Because the layer only flips the sign, ordinary [[Backpropagation]] trains all three parts in one backward pass. The title of the first paper below, "Unsupervised Domain Adaptation by Backpropagation", names this idea.

### Papers

The slide cites two papers ([[Block 7 Slides]], p. 223):

- Yaroslav Ganin, Victor Lempitsky, "Unsupervised Domain Adaptation by Backpropagation", ICML 2015.
- Hana Ajakan, Pascal Germain, Hugo Larochelle, François Laviolette, Mario Marchand, "Domain-Adversarial Training of Neural Networks", JMLR 2016.

Open point: the slide's author list for the JMLR 2016 paper starts with Ajakan. Check the full author list in the paper before you cite it.

## Related

- [[Transfer Learning]]: the overview grid of source and target data
- [[Fine-Tuning]]: the method when the target data has labels
- [[Multitask Learning]]: the other method for labelled source data and labelled target data
- [[Machine Learning Task Types]]: zero-shot learning, the other method for unlabeled target data
- [[Backpropagation]]

## Sources

- [[Block 7 Slides]], pp. 211, 215, 219-225
