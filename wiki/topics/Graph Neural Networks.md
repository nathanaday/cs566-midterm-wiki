---
id: con-cw1hzm
type: topic
kind: concept
description: A deep learning model for graph data that computes node embeddings through layers of neighborhood aggregation with shared weights, built from permutation-equivariant layers and an invariant readout, with a prediction head matched to the node, pair, or graph output; a CNN is a special case.
tags: [machine-learning]
aliases: [GNN, GNNs, Graph Neural Network, Graph Deep Learning, Deep Learning for Graphs, Deep Graph Encoders, GNN Training, Graph Network, Inductive GNN Inference]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 6 Slides]]", "[[Block 5 Slides]]", "[[Block 6 Slides Extended]]", "What a GNN Outputs", "[[F26-midterm-review-234p]]"]
up: ["[[Neural Networks]]", "[[Machine Learning]]"]
---

> [!concept] Concept
> 5 sources · refreshed 2026-10-19 · #machine-learning
> Up: [[Neural Networks]] · [[Machine Learning]]

## Definition

A graph neural network (GNN) is a deep learning model for data in the form of a graph. Block 6 of CSCI 566 covers GNNs ([[Block 6 Slides]], p. 2). The extended deck states the job in one line: a GNN learns predictions by combining neighboring information ([[Block 6 Slides Extended]], p. 5). A GNN is a deep node encoder: ENC(v) is "multiple layers of non-linear transformations based on graph structure" (p. 56). Each layer takes the previous layer's embeddings as input, and aggregates the neighbor embeddings and the node's own embedding (p. 133).

The midterm review sums up the model in one line: "Graph networks update node features using edges, then read out predictions per node or per graph." The inputs are the edges that connect nodes and the feature stored at each node. Each layer updates node features by combining information from neighbors. The outputs are one prediction per node or one pooled prediction for the whole graph ([[F26-midterm-review-234p]], p. 197).

The learned object is one function with shared weights. Each node runs it on its own features and its neighbors' vectors. The inputs change from node to node, but the learned weights are shared ([[Block 6 Slides Extended]], p. 61).

After Bronstein's ICLR 2021 keynote, the slides describe a GNN as a stack of permutation-equivariant layers, followed by a permutation-invariant layer that gives one output for the graph (p. 78). The extended deck repeats this: equivariant node layers, then invariant graph pooling ([[Block 6 Slides Extended]], p. 115; [[F26-midterm-review-234p]], p. 218). See [[Permutation Invariance and Equivariance]].

## Explanation

### From input to prediction

The extended deck shows a GNN as the middle stage of a pipeline. Graph and node features go in, the GNN gives node embeddings, and the embeddings give task predictions ([[Block 6 Slides Extended]], p. 48). "The graph gives the model structure. The task gives it a learning goal." ([[Block 6 Slides Extended]], p. 48). An embedding is a numeric vector that the prediction head uses ([[Block 6 Slides Extended]], p. 48). Its hidden coordinates need not have a fixed human meaning. The task trains the encoder to produce useful vectors ([[Block 6 Slides Extended]], p. 56).

The extended deck follows one small road network. The task is to predict whether road A will be delayed in the next 5 minutes, from the current traffic loads and the road connections ([[Block 6 Slides Extended]], p. 13). Road A has load 1. Alone, A sees only 1. With its neighbors, A also sees B = 2 and C = 4. A GNN lets A use its own input and the nearby inputs ([[Block 6 Slides Extended]], p. 16). A shared node MLP applies the same function to each road's own features. A GNN at road A also reads the neighbor inputs, and the mean of 2 and 4 is 3 in either listing order ([[Block 6 Slides Extended]], p. 74; [[F26-midterm-review-234p]], p. 199). For the adjacency and feature matrices of this example, see [[Permutation Invariance and Equivariance]]; for the values layer by layer, see [[Road Delay GNN Example]].

The values at layer 0 are observed inputs. After an update, the number at a node is a hidden value that the model uses: layer 1 and later hold computed hidden values, not observed inputs ([[F26-midterm-review-234p]], p. 201).

Synthesis: weight sharing alone does not make a GNN. A shared node MLP also shares its weights. The difference is that the GNN update also reads the neighbors.

### Why graphs need their own model

The deep learning toolbox is designed for simple sequences and grids: CNNs for images, and RNNs for text and speech (p. 59). The extended deck puts it in two lines: "CNNs use grids. Token order matters." ([[Block 6 Slides Extended]], p. 11). Networks are harder (pp. 10, 60; [[Block 6 Slides Extended]], p. 12):

- They have arbitrary size and complex topology, with no spatial locality as grids have.
- They have no fixed node ordering or reference point.
- They are often dynamic and have multimodal features.

A naive approach joins the adjacency matrix and the node features, and feeds each row into a deep neural net. It has three problems (p. 64; [[Block 6 Slides Extended]], p. 64):

- It needs $O(|V|)$ parameters (p. 64). The extended deck states this problem as an input width that grows with the graph size ([[Block 6 Slides Extended]], p. 64).
- It does not apply to graphs of a different size.
- It is sensitive to node ordering.

The goal is to generalize convolution beyond simple lattices (p. 65; [[Block 6 Slides Extended]], p. 65). The extended deck also names a second goal: use node features and attributes, such as text and images ([[Block 6 Slides Extended]], p. 65). But real-world graphs have no fixed notion of locality or sliding window, and their node numbering is arbitrary (p. 66). In the words of the extended deck, graphs have neighborhoods but no fixed grid-shaped window ([[Block 6 Slides Extended]], p. 66).

### Architecture

The example architecture stacks graph convolutions, an activation function, regularization such as dropout, and more graph convolutions (p. 57; [[Block 6 Slides Extended]], p. 62). The output is node embeddings. Subgraphs and whole graphs can also be embedded (p. 57; [[Block 6 Slides Extended]], p. 62). These deep encoders can be combined with the node similarity functions of the shallow encoders (p. 56; see [[Node Embeddings]]).

Each node computes its embedding along its own computation graph, a tree of neighbor aggregations; see [[Neighborhood Aggregation]]. [[Graph Convolutional Network]] gives the basic update rule.

### Tasks and the prediction head

GNNs can solve node classification, link prediction, community detection, and network similarity (p. 58). Node classification assigns labels to the unlabeled nodes of a partly labeled graph (p. 19). Example: classify a drug node in a drug-drug interaction network as safe or toxic (p. 100).

The prediction head is the output stage on top of the GNN. For road A, a shared classifier converts the node vector $h_A$ into low and high risk scores. A training label supplies the loss for a labeled node ([[Block 6 Slides Extended]], p. 99). The loss trains the GNN and the prediction head together ([[Block 6 Slides Extended]], p. 25), when both are trainable ([[Block 6 Slides Extended]], p. 99).

The required output tells where to attach the prediction head ([[Block 6 Slides Extended]], p. 28):

- **Node output:** predict the delay risk for road A ([[Block 6 Slides Extended]], p. 28). Each node embedding passes through a shared head to its own label (p. 108; [[Block 6 Slides Extended]], p. 112). Reordering the node inputs reorders the node outputs ([[Block 6 Slides Extended]], p. 112). A GNN gives one hidden vector per node, and the output rows follow the input rows ([[F26-midterm-review-234p]], p. 209).
- **Pair or edge output:** predict whether two objects have a relationship ([[Block 6 Slides Extended]], p. 28).
- **Whole-graph output:** predict a label for the complete network ([[Block 6 Slides Extended]], p. 28). A readout pools the node embeddings with sum or mean into one graph label (p. 109; [[Block 6 Slides Extended]], p. 113). A symmetric readout gives the same graph output after reordering ([[Block 6 Slides Extended]], p. 113).

Node tasks keep one output per node. Graph tasks pool the node vectors. The output task decides which of the two the model does ([[Block 6 Slides Extended]], p. 114; [[F26-midterm-review-234p]], p. 217). The review draws the full pipeline: graph and node features, then GNN layers 1, 2, and so on, then either node heads that give labels A, B, and so on, or a pool and a graph head that give one graph label ([[F26-midterm-review-234p]], p. 217).

The extended deck applies this to the [[Therapeutics Data Commons]] problems. It groups them by required output: one molecule, a drug-protein pair, or a generated molecule ([[Block 6 Slides Extended]], p. 45). "Our GNN head must match the scientific question." ([[Block 6 Slides Extended]], p. 45). A molecule property pools the atom vectors, then predicts one property. A drug-protein interaction combines the drug vector and the protein vector, then predicts the interaction. Road delay passes the vector of road A through a prediction head ([[Block 6 Slides Extended]], p. 46).

#### Choose the output first

The extended deck gives one design rule: "Choose the output before choosing the model." ([[Block 6 Slides Extended]], p. 28). The required output (node, pair or edge, or whole graph) tells where the prediction head attaches ([[Block 6 Slides Extended]], p. 28).

Synthesis: decide the output level of a graph task before the architecture. The output level decides whether the model keeps the node vectors, combines pairs of vectors, or pools all of them.

### What a GNN outputs

The GNN itself outputs one embedding per node: a matrix $H$ with $|V|$ rows and $d$ columns, one row $h_u$ for each node $u$. The graph structure stays the same. With $k$ layers, each row holds information about the node's features and its neighborhood out to $k$ hops (What a GNN Outputs). This fits the deck's pipeline, in which the GNN gives node embeddings and the embeddings give task predictions ([[Block 6 Slides Extended]], p. 48).

No step turns the output back into a graph. The prediction head gives a label, a probability, or a number (What a GNN Outputs). For a pair output, one choice of head scores two node vectors, for example with the dot product $h_u^\top h_v$, read as the probability that an edge exists (What a GNN Outputs). The shallow encoders of [[Node Embeddings]] use the same dot product as their decoder ([[Block 6 Slides]], p. 49).

A GNN does not, in general, predict the future state of a graph (What a GNN Outputs). Two tasks come close:

- Link prediction predicts new, missing, or unknown links (p. 21). It changes the graph one pair of nodes at a time (What a GNN Outputs).
- A forecasting task predicts a future value at a node. The road example predicts whether road A will be delayed in the next 5 minutes ([[Block 6 Slides Extended]], p. 13). That is a node-level prediction.

Graph generation is a separate graph-level task; see [[Graph]].

Synthesis: "what does a GNN output?" has two answers. The encoder outputs node vectors. The full model, encoder and head together, outputs the task prediction. A GNN is the graph version of the convolutional layers of a CNN: a learned feature extractor that a head reads (What a GNN Outputs).

### Training

A GNN is one choice of the function $f_\Theta$ in the usual objective $\min_\Theta \mathcal{L}(y, f_\Theta(x))$, trained with minibatches, backpropagation, and SGD (p. 61; see [[Gradient Descent]] and [[Backpropagation]]). To train a GNN, define a loss function on the embeddings (p. 97). Any loss works, and SGD trains the weight parameters (p. 98). A node embedding $z_v$ is a function of the input graph (p. 99). [[Graph Convolutional Network]] gives the details of the training step.

- **Supervised:** minimize $\mathcal{L}(y, f_\Theta(z_v))$, where $y$ is the node label. Use L2 if $y$ is a real number, or cross-entropy if $y$ is categorical (p. 99; see [[Loss Functions]]). For binary node classification (p. 101):

$$\mathcal{L} = -\sum_{v \in V} \Big[ y_v \log \sigma(z_v^\top \theta) + (1 - y_v) \log\big(1 - \sigma(z_v^\top \theta)\big) \Big]$$

  Here $z_v$ is the encoder output, $\theta$ holds the classification weights, and $y_v$ is the node class label (p. 101).
- **Unsupervised:** no node label exists, so the graph structure is the supervision (p. 99).

### Model design in four steps

1. Define a neighborhood aggregation function (p. 102).
2. Define a loss function on the embeddings (p. 102).
3. Train on a set of nodes, which is a batch of compute graphs (p. 103).
4. Generate embeddings for nodes as needed, also for nodes the model never trained on (p. 104).

### Inductive capability

All nodes share the same aggregation parameters (p. 105). The parameter count depends on the width and depth, not on $|V|$, so the parameters work on new nodes (p. 105). A model trained on one graph can embed an unseen graph. Example: train on a protein interaction graph of organism A, then embed new data about organism B (p. 106). Reddit, YouTube, and Google Scholar meet new nodes all the time: train on a snapshot, then embed each new node when it arrives (p. 107).

The midterm review states the condition: "Shared per-node updates with a mean or sum over neighbors respect node reordering and apply to new graphs with compatible features." ([[F26-midterm-review-234p]], p. 197). Its slide title is "Inductive Means Applying the Learned Rule to Unseen Nodes". Training fits the encoder, and inference computes outputs for new compatible inputs. In the training city, the road inputs, the links, and the observed delay labels fit the weights. In a new city, the model keeps the weights and computes vectors from the new road inputs and links. To check generalization, test the accuracy, the feature units, the edge meanings, and the traffic conditions. "Computing an output and predicting accurately are separate checks." ([[F26-midterm-review-234p]], p. 215). The review shows the same update rule on an unseen 3-road graph: it "Runs without retraining, but accuracy must be evaluated; outputs are not probabilities" ([[F26-midterm-review-234p]], p. 219). [[Road Delay GNN Example]] holds the numbers.

Synthesis: shared parameters remove two problems of the naive approach. The parameter count no longer grows with $|V|$, and the model accepts graphs of other sizes. A compatible input lets the model compute an output, but only an evaluation on the new graph shows whether the output is accurate.

### GNN and CNN

Each architecture shares parameters over a structure: a CNN over spatial offsets, an RNN over the previous state, and a GNN over graph neighbors ([[Block 5 Slides]], p. 4).

The extended deck calls this the same reuse idea. A CNN encoder reuses learned filters at many pixels and on new images. A GNN encoder reuses learned update weights at many nodes and on new graphs. In both, the new inputs must have the expected feature meanings and widths ([[Block 6 Slides Extended]], p. 111).

A CNN layer with a 3x3 filter updates pixel $v$ from itself and its 8 neighbor pixels, with one weight matrix for each position (pp. 111-112; [[Block 6 Slides Extended]], pp. 118-119):

$$h_v^{(l+1)} = \sigma\Big(\sum_{u \in N(v)} W_l^u h_u^{(l)} + B_l h_v^{(l)}\Big)$$

The GNN update uses one $W_l$ for all neighbors (p. 112; [[Block 6 Slides Extended]], p. 119):

$$h_v^{(l+1)} = \sigma\Big(W_l \sum_{u \in N(v)} \frac{h_u^{(l)}}{|N(v)|} + B_l h_v^{(l)}\Big)$$

A CNN can learn a different $W_l^u$ for each neighbor, because it can order the 9 pixels by their offset from the center, from $(-1,-1)$ to $(1,1)$ (p. 113; [[Block 6 Slides Extended]], p. 120). So a CNN is a special GNN with a fixed neighbor size and ordering, and a predefined filter size (p. 114). A GNN processes arbitrary graphs in which each node can have a different degree (p. 114). Arbitrary pixel permutations do not preserve the fixed offsets of a CNN (p. 114). The summary repeats that a GNN is a general architecture and a CNN is a special GNN (p. 133).

### Place in the field

"Graph neural network" was the fourth most frequent keyword at ICLR 2023, after reinforcement learning, deep learning, and representation learning. The slides call GNNs a hot subfield of ML (p. 9). The summary names GNN plus LLMs as a new direction (p. 133).

## Related

- [[Graph]]: vertices, edges, and the adjacency matrix
- [[Node Embeddings]]: the shallow encoders that GNNs replace with deep encoders
- [[Neighborhood Aggregation]]: the per-node computation graph and the aggregation step
- [[Graph Convolutional Network]]: the basic GNN update rule and its training
- [[Permutation Invariance and Equivariance]]: the road-delay example as matrices
- [[Road Delay GNN Example]]: the running toy example, layer by layer and on an unseen graph
- [[GNN Applications]]
- [[Therapeutics Data Commons]]: problems grouped by required output
- [[Convolutional Neural Networks (CNN)]]: a special GNN on a grid
- [[Recurrent Neural Networks (RNN)]]
- [[Transformers]]
- [[Loss Functions]]
- [[Gradient Descent]]
- [[Backpropagation]]

## Sources

- [[Block 6 Slides]], pp. 2, 9-10, 19, 21, 49, 56-66, 78, 97-114, 133
- [[Block 6 Slides Extended]], pp. 5, 11-13, 16, 25, 28, 45-46, 48, 56, 61-62, 64-66, 74, 99, 111-115, 118-120
- [[Block 5 Slides]], p. 4
- What a GNN Outputs: a saved study answer on what a GNN outputs and what it does not predict
- [[F26-midterm-review-234p]], pp. 197, 199, 201, 209, 215, 217-219: the midterm review of GNNs

A page number without a source name refers to [[Block 6 Slides]].
