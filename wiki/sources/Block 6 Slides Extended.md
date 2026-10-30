---
id: doc-w2d1w4
type: source
description: "The extended CSCI 566 Block 6 deck on graph neural networks by Yue Zhao (176 pages, Oct 4, 2026): it follows one road network through graph basics, GNN training, invariance, and depth, then adds drug-discovery tasks with TDC, attention as a graph, LLM enhancer and predictor routes, a worked GraphRAG example, and graphs of agents (GRADE, MAMA)."
tags: [machine-learning/cs566-deeplearning]
aliases: []
created: 2026-10-05T17:16:58
updated: 2026-10-05T17:36:06
refreshed: 2026-10-05T17:36:06
authority: official
status: absorbed
file: "[[internal/wiki/originals/178b26a7c05bf0d6.pdf]]"
media: pdf
sha256: 178b26a7c05bf0d69bb4be512c2723f1209841211722bf814c1b7ead9cf54df3
origin: ingest
locator: Block 6 Slides Extended.pdf
measure: 176 pages
captured: 2026-10-05T17:16:58
---

> [!source] PDF · 176 pages · official
> Captured 2026-10-05 from `Block 6 Slides Extended.pdf` (ingest) · absorbed by 2026-10-05 Ingest the extended CS566 Block 6 slides

![[internal/wiki/originals/178b26a7c05bf0d6.pdf]]

## Summary

The CSCI 566 deck "Block 6: Graph Neural Networks", by the instructor Yue Zhao, in a longer revision with 176 PDF pages. The file name in the course repository says "225p", but the PDF has 176 pages. The deck credits prior USC CSCI 566 materials and Stanford CS224W, and thanks Jure Leskovec for the GNN materials (p. 1). It replaces [[Block 6 Slides]] (133 pages, made on 2026-09-23). This deck was made on 2026-10-04.

Pages 2–3 are course updates dated Oct 4: Assignment 1 is out and due Oct 26, and the TAs release proposal feedback in 1–2 days. The deck then follows one small road network through the GNN material. The task is to predict whether road A will be delayed in the next 5 minutes, and the deck traces every number of a fixed 0.5/0.5 update through two layers. Most GNN slides of the first version come back, often reworded around this example. The new material:

- a section on graph tasks in drug discovery, built on TDC
- an embedding lookup compared with a GNN encoder
- weight sharing and inductive use on a new road and a new city
- the choice of depth
- self-attention seen as a graph with a mask
- a worked paper-classification example of the LLM as enhancer and as predictor
- a worked GraphRAG example with failure modes
- two graphs of agents: GRADE, a run graph, and MAMA, a communication graph with a privacy-leakage result

The text of this deck does not hold some slides of the first version: the four LLM-graph system families, the GPT-3.5 Cora and Pubmed case study, the formal permutation-matrix definitions, the ICLR 2023 keyword statistic, and the Reddit and YouTube examples of inductive use. The topics keep those claims with their citations to [[Block 6 Slides]]. Locators are PDF page numbers.

## Structure

- pp. 1–5, title, the Oct 4 course updates, and the plan of the block: [[CS566-DeepLearning]], [[Graphs of Agents]].
- pp. 6–23, why graphs, the road example, nodes, edges, and features, heterogeneous, directed, and bipartite graphs, and the choice of representation: [[Graph]], [[Road Delay GNN Example]].
- pp. 24–40, training on the road example, graph task levels, where the prediction head attaches, and applications (PinSage, polypharmacy, Google Maps ETA, antibiotic discovery): [[Graph Neural Networks]], [[GNN Applications]].
- pp. 41–46, graph tasks in drug discovery and TDC: the GNN head must match the scientific question: [[GNN Applications]], [[Therapeutics Data Commons]].
- pp. 47–62, traditional graph ML, representation learning, node embeddings, the adjacency and feature matrices, and an embedding lookup compared with a GNN encoder: [[Node Embeddings]], [[Permutation Invariance and Equivariance]].
- pp. 63–80, notation, the naive approach, node ordering, invariance and equivariance, the shared node MLP, message passing, and computation graphs: [[Permutation Invariance and Equivariance]], [[Neighborhood Aggregation]], [[Graph Convolutional Network]].
- pp. 81–100, the deep encoder update rule, the 0.5/0.5 toy update, synchronous updates, pooling, an added edge, the prediction head, and training: [[Graph Convolutional Network]], [[Neighborhood Aggregation]], [[Road Delay GNN Example]].
- pp. 101–120, supervised training, model design, weight sharing, inductive use, readout, depth, and GNNs compared with CNNs: [[Graph Convolutional Network]], [[Node Embeddings]], [[Graph Neural Networks]].
- pp. 121–125, self-attention as a token graph and the causal mask: [[Attention]], [[Causal Mask]], [[Transformers]].
- pp. 126–134, paper classification with the LLM as enhancer or as predictor, and matched comparisons: [[LLMs and Graphs]].
- pp. 135–153, retrieval-augmented generation and a worked GraphRAG example with failure modes and tests: [[Retrieval-Augmented Generation]], [[GraphRAG]].
- pp. 154–168, what an edge means, and GRADE run graphs: [[Graphs of Agents]], [[GRADE]].
- pp. 168–176, MAMA communication topology and leakage, the closing comparison, and the pointer to Block 7: [[MAMA]], [[Graphs of Agents]].
