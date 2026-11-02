---
description: A deep learning model for graph data that computes one embedding per node through layers of neighborhood aggregation with shared weights, read by a head matched to the node, pair, or graph output; this page also covers graphs as data, the GCN update rule, training, the CNN special case, and the directed, attention, and autoencoder variants.
aliases: [GNN, GNNs, Graph Neural Network, GCN, Graph Convolutional Network, Message Passing]
sources: ["[[Block 6 Slides]]", "[[Block 6 Slides Extended]]", "[[Block 5 Slides]]", "[[F26-midterm-review-234p]]", "[[CSCI 566 Midterm (Spring 2024)]]"]
subject: 7 Graphs
---

## Definition

A graph neural network (GNN) is a deep node encoder: a stack of layers that update each node's embedding from its own embedding and its neighbors', with one set of weights shared by every node. A head then reads the embeddings per node, per node pair, or per graph. The basic form, which averages the neighbors, is the graph convolutional network (GCN); variants differ in the aggregation step.

A plain MLP on the rows of $[A \,\|\, X]$ fails: $O(|V|)$ parameters, no transfer across graph sizes, and sensitivity to node order.

### Message Passing

Each layer runs **aggregate**, then **update**, at every node at once.

**Aggregation must be permutation invariant.** AGG treats $N(v)$ as a set: a sum, mean, max, or attention-weighted sum gives the same $m_v$ in any neighbor order. Concatenation, a recurrent pass over the list, or a weight tied to "the first neighbor" breaks this.

- Computation graph: each node's own $K$-level tree, target at the top, input features at the leaves.
- Reach: a layer-$k$ embedding sees nodes up to $k$ hops away; information moves one edge per layer.
- Schedule: read layer $k$, write layer $k+1$ for all nodes. An in-place update depends on node order.

> [!tip]
> Weight sharing alone does not make a GNN; a shared per-node MLP shares weights too. The GNN update reads the neighbors.

### Invariance, Shared Weights, and Depth

- Per node, the encoder is **permutation invariant**; over all nodes, **permutation equivariant**: permute the feature rows and $A$ together, and the output rows permute the same way. 
- All nodes share $W_k$ and $B_k$ per layer, as a CNN shares one kernel across positions and an RNN one update across time steps. Parameter count depends on width and depth, so a trained GNN runs inductively on unseen graphs whose features have the same meaning and width.
- A CNN is a GNN with a fixed neighbor count and order: a 3x3 filter learns one $W_l^u$ per offset $u$; graph neighbors have no order. 
- Node (row) order may change when $A$ moves with it; feature (column) order may not, since each column carries the meaning the weights learned.

**Over-smoothing.** Each layer averages a node with its neighbors, so after many layers the embeddings of all nodes in a connected region converge toward one vector. Depth trades reach for distinctness and compute; a few layers is the usual choice.

> [!tip]
> Running on a new graph and predicting well on it are separate checks: the model computes an output without retraining, but accuracy still needs evaluation.

### Task Level and Readout

The encoder outputs $H$ with one row $z_v$ per node; the head turns the rows into the task output. Choose the output before the model.

| Level | Head | Output | Task |
| --- | --- | --- | --- |
| Node | shared MLP on $z_v$ | one label per node | node classification |
| Edge (pair) | $z_u^\top z_v$ or MLP on $[z_u \,\|\, z_v]$ | link probability | link prediction |
| Graph | readout, then MLP | one label per graph | graph classification or regression |

**Readout.**
$$z_G = \text{READOUT}\big(\{\, z_v : v \in V \,\}\big), \quad \text{a sum, mean, or max over nodes}$$

The readout must be permutation invariant so the graph label does not depend on node order. Layers and head train together by [[Backpropagation]] and SGD ([[Gradient Descent]]) on a loss over the labeled nodes, pairs, or graphs ([[Loss Functions]]); with no labels, the graph structure is the supervision, as in the autoencoder below.

### Variants

| Variant | Aggregator | Distinction |
| --- | --- | --- |
| GCN | normalized mean of neighbors | weights fixed by the graph, $1/\sqrt{d_u d_v}$ |
| GAT | attention-weighted sum | learned weight per pair, recomputed per input; multi-head |
| Directed or relational GCN | one $W_k^r$ per direction or edge type | in- and out-edges, or relations, get separate weights |
| GAE | GCN encoder, dot-product decoder | same layers, different loss: reconstruct $A$ |

**GAT weights.**
$$e_{vu} = \text{LeakyReLU}\big(a^\top [W h_v \,\|\, W h_u]\big), \quad \alpha_{vu} = \frac{\exp e_{vu}}{\sum_{w \in N(v)} \exp e_{vw}}, \quad h_v' = \sigma\Big(\sum_{u \in N(v)} \alpha_{vu} W h_u\Big)$$

Invariance holds because the score reads only the pair and the softmax runs over $N(v)$. Projection weights are fixed at inference; $\alpha$ is recomputed per input. See [[Transformers]].

**Directed edges.** Symmetrize $A \leftarrow \max(A, A^\top)$ and lose direction; or aggregate in-neighbors with $W_k^{in}$ and out-neighbors with $W_k^{out}$; or use one $W_k^r$ per relation $r \in R$. Keeping only the out-neighbors is not a standard method.

**Graph autoencoder.**
$$Z = \text{GCN}(X, A), \qquad \hat{A} = \sigma(Z Z^\top), \qquad \hat{A}_{uv} = \sigma(z_u^\top z_v)$$

The loss is binary cross-entropy between $\hat{A}$ and $A$ with non-edges down-weighted or sampled. It is unsupervised, scores unseen pairs for link prediction, and reuses the dot-product decoder of [[Node Embeddings]]; VGAE adds a Gaussian prior and a KL term.

> [!tip]
> A GNN does not predict the next state of a graph. Link prediction scores one pair at a time; graph generation is a separate graph-level task.

## Related

- [[Permutation Invariance and Equivariance]]: invariance and equivariance as matrices
- [[Node Embeddings]]: the shallow encoders GNNs replace, and the GAE decoder
- [[Convolutional Neural Networks (CNN)]]: the special GNN on a grid
- [[Convolutional Layer]]: one weight per spatial offset
- [[Pooling Layer]]: the grid form of the readout
- [[Recurrent Neural Networks (RNN)]]: the same weights at every time step
- [[Transformers]]: attention as input-dependent mixing weights
- [[Activation Functions]]: $\sigma$, for example ReLU
- [[Loss Functions]]: cross-entropy on labels, or on the adjacency in a GAE
- [[Gradient Descent]]
- [[Backpropagation]]
- Road Delay GNN Example: the toy values layer by layer

## Sources

- [[Block 6 Slides]]
- [[Block 6 Slides Extended]]
- [[Block 5 Slides]]
- [[F26-midterm-review-234p]]
- [[CSCI 566 Midterm (Spring 2024)]]
