---
description: "The CSCI 566 Block 6 slide deck by Yue Zhao on graph neural networks: graph types and tasks, applications and TDC, node embeddings, permutation invariance and equivariance, the GCN, GNNs compared with CNNs and Transformers, and LLMs combined with graphs."
---

The original is [[attachments/Block 6 Slides.pdf|Block 6 Slides.pdf]], 133 pages, an official course document saved as `Block 6 Slides.pdf` on 2026-09-28.

## Summary

The CSCI 566 deck "Block 6: Graph Neural Networks", by the instructor Yue Zhao. It has 133 PDF pages and credits Stanford CS224W and Jure Leskovec for much of the GNN material. It explains why graphs matter and why grids and sequences do not cover them, defines graph types and the node, link, and graph levels of graph tasks, and shows applications in recommenders, traffic, and drug discovery (with the Therapeutics Data Commons). It then moves from hand-built features to node embeddings, sets up permutation invariance and equivariance, and derives the graph convolutional network, its training, and its inductive use. It compares GNNs with CNNs and Transformers, and ends with a 2026 map of systems that combine LLMs and graphs. Locators are PDF page numbers.

## Structure

- pp. 1–20, why graphs, graph types, and graph ML task levels: [[Graph]].
- pp. 21–38, link-level and graph-level applications, TDC, and DrugAgent: GNN Applications, Therapeutics Data Commons.
- pp. 39–58, traditional graph ML, graph representation learning, the encoder-decoder framework, shallow encoders, and deep encoders: [[Node Embeddings]], [[Graph Neural Networks]].
- pp. 59–81, the training loop recap, graph notation, why naive methods fail, and permutation invariance and equivariance: [[Permutation Invariance and Equivariance]].
- pp. 82–110, the GCN: computation graphs, neighborhood aggregation, the update rule, synchronous updates, training, and inductive capability: [[Graph Convolutional Network]], [[Neighborhood Aggregation]], [[Graph Neural Networks]].
- pp. 111–118, GNNs compared with CNNs and with self-attention: [[Graph Neural Networks]], Attention, Causal Mask.
- pp. 119–133, LLMs and graphs: enhancer and predictor pipelines, the four system families, the GPT-3.5 case, evaluation rules, and the summary: LLMs and Graphs.
