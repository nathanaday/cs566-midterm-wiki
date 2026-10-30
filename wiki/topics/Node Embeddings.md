---
id: con-p4trfx
type: topic
kind: concept
description: A node embedding is a learned low-dimensional vector for a graph node that a prediction head uses; a shallow embedding lookup stores one vector per node ID (DeepWalk, node2vec), while a GNN encoder computes the vector from the node's features and neighbors, so it can also embed new nodes and new graphs with compatible inputs.
tags: [machine-learning/cs566-deeplearning]
aliases: [Node embedding, Graph representation learning, Representation learning on graphs, Encoder-decoder framework, Shallow encoding, Shallow encoder, Shallow embedding, Embedding lookup, Lookup matrix Z, GNN encoder, Embedding space, Node similarity, DeepWalk, node2vec, Traditional ML for graphs, Feature engineering for graphs, Inductive capability of GNNs]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 6 Slides]]", "[[Block 6 Slides Extended]]"]
up: ["[[Graph Neural Networks]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Graph Neural Networks]]

## Definition

A node embedding is a vector $z_u \in \mathbb{R}^d$ for a node $u$ of a [[Graph]]. The goal is "efficient task-independent feature learning for machine learning with graphs": learn a map $f: u \to \mathbb{R}^d$ from each node to its feature representation, or embedding ([[Block 6 Slides]], p. 43).

The extended revision of the deck states the goal another way: "Learn node vectors useful for a chosen graph task" ([[Block 6 Slides Extended]], p. 52). In that deck, an embedding is a numeric vector that the prediction head uses (p. 48).

The embedding space must reflect the graph. Similar nodes in the network must get similar embeddings, for example two nodes that an edge connects ([[Block 6 Slides]], p. 44). The extended deck says that the training objective decides which nodes have similar vectors. For example, an edge-based objective can bring connected nodes closer ([[Block 6 Slides Extended]], p. 53).

## Explanation

### Graph representation learning

Traditional ML on graphs needs a person to design node, edge, and graph-level features for each task ([[Block 6 Slides]], p. 40; [[Block 6 Slides Extended]], p. 49). A model then maps the features to labels. The extended deck names an SVM or a neural network as examples of this model ([[Block 6 Slides Extended]], p. 49). Graph representation learning "alleviates the need to do feature engineering every single time": the model learns the features, and a learning algorithm then uses them for the downstream prediction task ([[Block 6 Slides]], p. 41; [[Block 6 Slides Extended]], p. 50).

The slides compare this change to the change from classical ML to deep learning. Classical ML extracts features by hand, then classifies. [[Deep Learning]] learns feature extraction and classification together ([[Block 6 Slides]], p. 42; [[Block 6 Slides Extended]], p. 51).

Embeddings encode network information. Many downstream tasks can use them: node classification, link prediction, graph classification, anomalous node detection, and clustering ([[Block 6 Slides]], p. 44; [[Block 6 Slides Extended]], p. 53). See [[Graph]] for these tasks.

### What an embedding holds

The extended deck shows the pipeline from inputs to a prediction with its road-delay example. The inputs $x_A$ of road A and its neighbor context go into the encoder. The encoder gives a learned vector $h_A$, for example $[0.2, 0.8]$, and a prediction head uses $h_A$ to predict delay risk ([[Block 6 Slides Extended]], p. 56). After the neighborhood updates, each node has a vector $h$ (p. 56).

- The hidden coordinates need not have a fixed human meaning (p. 56).
- The task trains the encoder to produce useful vectors (p. 56).
- An encoder maps nodes $u$ and $v$ to $z_u$ and $z_v$ in the embedding space. The training task decides what makes two vectors useful (p. 57).

### Setup

The original deck assumes an undirected graph $G$ with vertex set $V$ and a binary adjacency matrix $A$. For simplicity, the method uses no node features or other information ([[Block 6 Slides]], p. 45).

### Encoder-decoder framework

The goal is to encode nodes so that similarity in the embedding space, for example a dot product, approximates similarity in the graph ([[Block 6 Slides]], p. 46):

$$\text{similarity}(u, v) \approx z_v^T z_u$$

Both the similarity function and the encoder must be defined (p. 47). Learning takes four steps (p. 48):

1. An encoder maps nodes to embeddings.
2. A node similarity function measures similarity in the original network.
3. A decoder DEC maps embeddings to a similarity score.
4. Optimize the encoder parameters so that $\text{similarity}(u, v) \approx z_v^T z_u$.

The two key parts are (p. 49):

- **Encoder:** $\text{ENC}(v) = z_v$ maps each node in the input graph to a $d$-dimensional embedding.
- **Similarity function:** it says how relationships in the vector space map to relationships in the original network. The decoder is the dot product between node embeddings, $z_v^T z_u$.

### Shallow encoding

The simplest encoder is an embedding lookup ([[Block 6 Slides]], p. 50):

$$\text{ENC}(v) = z_v = Z \cdot v$$

- $Z \in \mathbb{R}^{d \times |V|}$ is the matrix that training learns. Each column is the embedding of one node.
- $v \in \mathbb{I}^{|V|}$ is an indicator vector: all zeros, except a one in the column for node $v$.

$Z$ has one column for each node. The number of rows is the embedding dimension (p. 51). Each node gets its own embedding vector, so training optimizes the embedding of each node directly. The slides name DeepWalk and node2vec as methods of this kind (p. 52) but do not describe them.

In summary (p. 53): the shallow encoder is an embedding lookup, and the parameters to optimize are $Z$, which holds $z_u$ for every node $u \in V$. The decoder is based on node similarity. The objective is to maximize $z_v^T z_u$ for node pairs $(u, v)$ that are similar.

$Z \cdot v$ with a one-hot $v$ selects one column of $Z$. So the number of parameters grows with the number of nodes. The extended deck states the consequence: "A lookup needs an entry for every node ID" ([[Block 6 Slides Extended]], p. 60).

### Node similarity

The key choice among methods is how they define node similarity ([[Block 6 Slides]], p. 54). Should two nodes have similar embeddings if they:

- are linked?
- share neighbors?
- have similar "structural roles"?

### Properties of these embeddings

This way of learning node embeddings is unsupervised or self-supervised ([[Block 6 Slides]], p. 55):

- It does not use node labels.
- It does not use node features.
- It estimates the coordinates of each node directly, so that some aspect of the network structure is preserved.

The embeddings are task-independent. They are not trained for one task, and any task can use them (p. 55).

Synthesis: the two goal statements in the Definition fit two kinds of encoder. Task independence describes these shallow, unsupervised embeddings. The extended deck's goal, vectors useful for a chosen task, describes an encoder that a task trains (see What an embedding holds).

### Lookup versus GNN encoder

The extended deck compares two ways to give a node a vector, because a numeric vector for each road must exist before a prediction ([[Block 6 Slides Extended]], p. 58):

| Method | How it gets the vector |
| --- | --- |
| Embedding lookup | Use a node ID to fetch its learned vector from a table. |
| GNN encoder | Use the node's current features and neighbors to compute a vector. |

Source: [[Block 6 Slides Extended]], p. 58. The reason for the comparison: a new road has features, but it may have no row in the ID table (p. 58). "A lookup stores a vector. An encoder computes a vector" (p. 58).

The deck's example uses illustrative numbers. Training has learned one vector for each of roads A, B, C, and D, for example A $\to [0.2, 0.8]$ and B $\to [0.5, 0.1]$. A newly added road E has no trained table entry yet (p. 59). In the lookup matrix $Z$, one column stores the vector for one node ID, and the column height is the vector width (p. 60).

A GNN learns a function with shared weights and uses it at every road. Road E's features and its neighbor vectors go through the same learned GNN update, and the result is a computed vector for E. The inputs change from road to road, but the learned weights are shared (p. 61). How each layer shares its weights is described in [[Neighborhood Aggregation]] and [[Graph Convolutional Network]].

### New nodes and new graphs

"Inductive" means that the encoder applies its learned rule to nodes it did not see in training ([[Block 6 Slides Extended]], p. 110). The weights depend on the feature width, not on the road IDs. So the learned matrices can process E when E and its neighbors supply vectors of the width that the encoder expects (pp. 107, 109).

Training fits the encoder. Inference computes outputs for new compatible inputs (p. 110):

| Stage | What happens |
| --- | --- |
| Training city | Use the road inputs, the links, and the observed delay labels to fit the weights. |
| New city | Keep the weights. Compute vectors from the new city's road inputs and links. |
| Check generalization | Check test accuracy, feature units, edge meanings, and traffic conditions. |

Source: [[Block 6 Slides Extended]], p. 110. The slide's conclusion: "Computing an output and predicting accurately are separate checks" (p. 110).

The deck calls this the same reuse idea as in a CNN ([[Block 6 Slides Extended]], p. 111). A trained image filter can scan a new image, and a trained GNN update can visit new nodes. A [[Convolutional Neural Networks (CNN)|CNN]] encoder reuses learned filters at many pixels and on new images. A GNN encoder reuses learned update weights at many nodes and on new graphs. Both have the same requirement: the new inputs must have the expected feature meanings and widths. "The learned operation is reusable across compatible inputs" (p. 111).

The original deck gives other examples of this capability: a protein interaction graph of a new organism, and new nodes on Reddit, YouTube, and Google Scholar. See [[Graph Neural Networks]].

Synthesis: a matching width is enough for the computation to run, but it does not show that the output is correct. Suppose that a new city records a feature in other units, or uses edges with another meaning. The encoder then still returns a vector of the right width, but the vector can be wrong. That is why the deck lists feature units and edge meanings next to test accuracy. A different distribution of traffic conditions is a generalization risk of the same kind; see [[Overfitting and Underfitting]].

### Deep encoders

The original deck then replaces the lookup with a deep encoder based on [[Graph Neural Networks]] ([[Block 6 Slides]], pp. 53, 56):

$$\text{ENC}(v) = \text{multiple layers of non-linear transformations based on graph structure}$$

These deep encoders can use the same node similarity functions ([[Block 6 Slides]], p. 56). They output node embeddings, and they can also embed subgraphs and whole graphs ([[Block 6 Slides]], p. 57; [[Block 6 Slides Extended]], p. 62). Unlike the shallow method, GNNs aim to use node features or attributes such as text and images ([[Block 6 Slides]], p. 65).

Synthesis: the decoder objective resembles Contrastive Learning. Both pull the embeddings of similar pairs together in a shared space. The slides do not make this comparison.

## Related

- [[Graph]]: graph types, task levels, and the traditional feature-engineering pipeline
- [[Graph Neural Networks]]: the deep encoders, and more examples of inductive use
- [[Neighborhood Aggregation]]: the shared update that a GNN encoder runs at each node
- [[Graph Convolutional Network]]: the basic update rule and its shared weights
- [[Convolutional Neural Networks (CNN)]]: the same reuse of learned weights on new inputs
- [[Overfitting and Underfitting]]: generalization to new data
- [[Deep Learning]]: learned features in place of hand-designed ones
- Contrastive Learning
- Machine Learning Task Types: self-supervised learning

## Sources

- [[Block 6 Slides]], pp. 40-57, 65
- [[Block 6 Slides Extended]], pp. 48-53, 56-62, 107, 109-111
