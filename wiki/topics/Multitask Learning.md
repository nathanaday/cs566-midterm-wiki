---
id: doc-pppde5
type: topic
kind: concept
description: Multitask learning trains one neural network for several tasks that share some layers, for example one speech recognizer whose shared hidden layers serve five languages and lower the Mandarin error rate.
tags: [machine-learning/cs566-deeplearning]
aliases: [Multi-task learning, Multitask learning, Multilingual speech recognition, Multitask Learning - Multilingual]
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

Multitask learning trains one neural network for several tasks, and the tasks share some layers ([[Block 7 Slides]], p. 216). "The multi-layer structure makes NN suitable for multitask learning." ([[Block 7 Slides]], p. 216)

## Explanation

### Place in transfer learning

In the deck's transfer-learning grid, multitask learning and fine-tuning fill the cell for labelled source data and labelled target data ([[Block 7 Slides]], pp. 214, 224). See [[Transfer Learning]].

Synthesis (not in the deck): fine-tuning trains on the source data first and on the target data next. Multitask learning trains on the tasks together, so the data of each task shapes the shared layers.

### Two layouts

The slide draws two networks for Task A and Task B ([[Block 7 Slides]], p. 216):

1. One input feature goes through shared layers. The network then splits into layers for Task A and layers for Task B.
2. Each task has its own input feature and its own first layers. Both feed a shared middle layer. The network then splits into layers for each task.

### Example: multilingual speech recognition

- Shared hidden layers read acoustic features. Separate output layers give the states of French, German, Spanish, Italian, and Mandarin. The slide's reason: "Human languages share some common characteristics." ([[Block 7 Slides]], p. 217)
- A similar idea in translation: Daxiang Dong, Hua Wu, Wei He, Dianhai Yu, and Haifeng Wang, "Multi-task learning for multiple language translation", ACL 2015 ([[Block 7 Slides]], p. 217).
- A chart plots the Mandarin character error rate against the hours of Mandarin training data, on a log scale. At each plotted point, the "With European Language" curve is below the "Mandarin only" curve ([[Block 7 Slides]], p. 218).

These are approximate values, read from the chart ([[Block 7 Slides]], p. 218):

| Hours of Mandarin data (about) | Mandarin only | With European language |
| --- | --- | --- |
| 3 | 45 | 35.5 |
| 9 | 40 | 34 |
| 35 | 31.5 | 28.5 |
| 140 | 29 | 26.5 |

- From these readings, the gap is largest when there is the least Mandarin data.
- The chart also has a red horizontal line near a character error rate of 27.5. The slide does not explain it.
- The chart's source: Huang, Jui-Ting, et al., "Cross-language knowledge transfer using multilingual deep neural network with shared hidden layers", ICASSP 2013 ([[Block 7 Slides]], p. 218).

## Related

- [[Transfer Learning]]: the overview grid of source and target data
- [[Fine-Tuning]]: the other method for labelled source data and labelled target data
- [[Domain-Adversarial Training]]: the method when the target data has no labels
- [[Machine Learning Task Types]]

## Sources

- [[Block 7 Slides]], pp. 214, 216-218, 224
