---
id: doc-gdf7sa
type: topic
kind: concept
description: "The CSCI 566 Block 6 running example: a graph neural network predicts whether road A will be delayed in the next 5 minutes from the load indices of four connected roads A, B, C, D, with a fixed 0.5/0.5 mean-aggregation update traced through two layers and applied without retraining to an unseen 3-road graph."
tags: [machine-learning/cs566-deeplearning]
aliases: [Road A Delay-Risk Example, Delay Risk on Road A, Road Network Example, Load Index, Toy Mean-Aggregation Example, 0.5/0.5 Toy Update, Toy Road Network, Road Network Graph Task, Toy Mean-Aggregation Update]
created: 2026-10-05T17:31:20
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 6 Slides Extended]]", "[[F26-midterm-review-234p]]"]
up: ["[[GNN Applications]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[GNN Applications]]

## Definition

The road delay example is the running toy problem of the extended Block 6 deck. A graph neural network must predict whether road A will be delayed in the next 5 minutes. The model inputs are the current traffic on four road segments A, B, C, D and the connections between them ([[Block 6 Slides Extended]], p. 13). The deck marks the example as a course schematic: the numbers are illustrative, and the sources are in the speaker notes (pp. 13-18). The midterm review deck uses the same toy road network to show which numbers are inputs and which outputs a model must return ([[F26-midterm-review-234p]], p. 198).

## Explanation

### The road graph

A connects to B and to C, and C connects to D (p. 13). In the graph, a node is one road segment, an edge is one direct connection (A–B, A–C, C–D), and a feature is the current load: A = 1, B = 2, C = 4, D = 8. The feature describes the road, and the edge describes its connection (p. 18). The midterm review gives the same nodes, edges, and loads ([[F26-midterm-review-234p]], p. 198).

### Load index

For this toy example, the load index is the number of vehicles counted in the last 5 minutes divided by 10 (p. 14):

| Road | Observed vehicles | Input load index |
|---|---|---|
| A | 10 | 1 |
| B | 20 | 2 |
| C | 40 | 4 |
| D | 80 | 8 |

### Inputs and target

A feature is an observed value that the model gets before it predicts. Road A has load 1 in the current 5-minute window. The prediction asks whether travel on A will take longer than its usual travel time. Current speed, road capacity, and time of day are possible extra inputs (p. 15).

The midterm review states the role of each number: "These unitless load indices are input features; the labels are the delay risk classes." A node head predicts one delay risk class per road. A graph head pools to one city label ([[F26-midterm-review-234p]], p. 198).

A alone sees load 1. With its neighbors, A also sees B = 2 and C = 4: A is lightly loaded now, but the roads connected to it carry more traffic. A GNN lets A use its own input and the inputs near it (p. 16). The review puts it as a contrast: a shared node MLP applies the same function to each road's own features, but a GNN at road A also reads the neighbor inputs B = 2 and C = 4. "One shared update combines each node with its neighbors." ([[F26-midterm-review-234p]], p. 199).

The model uses a current snapshot to predict the following 5 minutes. The loads and road links of the current window are the model inputs. The training label is Yes or No: does travel time in the next 5 minutes exceed the usual time? Training pairs the earlier inputs with the later observed label (p. 24). The pipeline is current loads and road links, then the GNN and a head, then a predicted delay probability. The historical label gives a loss, and the loss updates the shared weights of both the GNN and the prediction head (p. 25). The head reads the learned vector of A, for example $h_A = [0.2, 0.8]$ (p. 56), and a shared classifier turns it into low-risk and high-risk scores (p. 99).

### The matrices

In node order A, B, C, D, the adjacency matrix is (p. 54):

|   | A | B | C | D |
|---|---|---|---|---|
| A | 0 | 1 | 1 | 0 |
| B | 1 | 0 | 0 | 0 |
| C | 1 | 0 | 0 | 1 |
| D | 0 | 0 | 1 | 0 |

A row tells which neighbors one road can read. The feature matrix is $X = [1, 2, 4, 8]^\top$, with one feature per road; a real road node can have several input features (p. 55). When the nodes are renumbered, $A$ and $X$ must be reordered together (p. 55); see [[Permutation Invariance and Equivariance]].

### The 0.5/0.5 toy update

The deck uses a fixed update so that every number can be followed (p. 85; [[F26-midterm-review-234p]], p. 201):

$$h_v^{k+1} = 0.5\, h_v^k + 0.5\, \mathrm{mean}\{h_u^k : u \text{ is a neighbor of } v\}$$

This is a toy mean-aggregation update with fixed weights, not the exact normalized GCN rule (p. 86; [[F26-midterm-review-234p]], pp. 202-205). Layer 0 holds the observed load indices. From layer 1 on, the values are hidden values that the model uses, not vehicle counts (p. 85; [[F26-midterm-review-234p]], p. 201).

| Road | Neighbors | Layer 0 | Layer 1 | Layer 2 |
|---|---|---|---|---|
| A | B, C | 1 | 2 | 2.4375 |
| B | A | 2 | 1.5 | 1.75 |
| C | A, D | 4 | 4.25 | 4.125 |
| D | C | 8 | 6 | 5.125 |

The values are from pp. 86-88 and from [[F26-midterm-review-234p]], pp. 202-204. The deck works two of them: $A^1 = 0.5 \cdot 1 + 0.5 \cdot (2 + 4)/2 = 2$ (p. 86; [[F26-midterm-review-234p]], p. 202) and $A^2 = 0.5 \cdot 2 + 0.5 \cdot (1.5 + 4.25)/2 = 2.4375$ (p. 88; [[F26-midterm-review-234p]], p. 204). Synthesis: the other values follow from the same rule, for example $C^1 = 0.5 \cdot 4 + 0.5 \cdot (1 + 8)/2 = 4.25$ and $D^1 = 0.5 \cdot 8 + 0.5 \cdot 4 = 6$.

Every new value uses only the previous layer (p. 87; [[F26-midterm-review-234p]], p. 203). Information moves one graph edge per layer. At layer 1, A reads B and C. At layer 2, D can contribute to A through C (pp. 88, 91; [[F26-midterm-review-234p]], pp. 204, 207).

### Synchronous updates

Each layer reads layer $k$ and writes layer $k+1$. An in-place update in the order A, then B, would give $B^1 = 2$ instead of 1.5. Node numbering does not define an update schedule (p. 89; [[F26-midterm-review-234p]], p. 205). Synthesis: the only neighbor of B is A. In place, B reads the new value of A (2) instead of its layer-0 value (1), so $B^1 = 0.5 \cdot 2 + 0.5 \cdot 2 = 2$. See [[Graph Convolutional Network]].

### From fixed weights to learned weights

The 0.5/0.5 example shows information flow with fixed weights. A trained layer transforms or weights the neighbor messages, combines them with the current vector of the node, and reuses the same update rule at every node. Training learns these shared transforms from the prediction loss (p. 90; [[F26-midterm-review-234p]], p. 206). At one GNN layer, every road uses the same learned matrices: $W_{self}$ transforms the vector of the node, and $W_{neighbor}$ transforms the neighbor mean. The weights depend on the feature width, not on the road IDs (pp. 107-108). So a new road E can run the same update: its neighbor vectors $[1, 0]$ and $[5, 2]$ give the mean $[3, 1]$, and its own vector is $[3, 1]$ (p. 109). A model trained on one city can compute outputs for a new city with the same weights. Accurate prediction there is a separate check (p. 110; [[F26-midterm-review-234p]], p. 215). The review names what to check: test accuracy, feature units, edge meanings, and traffic conditions ([[F26-midterm-review-234p]], p. 215).

### An unseen graph

The midterm review runs the update on a graph that the model did not see: a triangle of three roads U, V, W with loads U = 6, V = 1, W = 3. The slide says that "the same two learned weights" update nodes in the 4-road graph and in the unseen 3-road graph. It writes the rule with the input loads as $h_v = 0.5\, x_v + 0.5\, \mathrm{mean}(\text{neighbor } x)$ ([[F26-midterm-review-234p]], p. 219):

| Graph | Node | Neighbor mean | Output |
|---|---|---|---|
| Old graph (A–B, A–C, C–D) | A | mean(2, 4) = 3 | 0.5 × 1 + 0.5 × 3 = 2 |
| Unseen triangle (U–V, U–W, V–W) | U | mean(1, 3) = 2 | 0.5 × 6 + 0.5 × 2 = 4 |

The feature is a unitless load index, one per road. The rule "Runs without retraining, but accuracy must be evaluated; outputs are not probabilities" ([[F26-midterm-review-234p]], p. 219). See [[Graph Neural Networks]] for inductive use in general.

### Node order

The example also shows the order properties of a GNN (pp. 92-95):

- **Neighbor order:** A reads the values 2, 4 or 4, 2. The mean is 3 either way, and the update of A is 2 in both cases (p. 92; [[F26-midterm-review-234p]], pp. 199, 208).
- **Node outputs:** a GNN gives one hidden vector per road, and the output rows follow the input rows ([[F26-midterm-review-234p]], p. 209). The layer-1 outputs in file order A, B, C, D are 2, 1.5, 4.25, 6. In file order D, B, A, C they are 6, 1.5, 2, 4.25. Road A keeps output 2 after its row moves (p. 93; [[F26-midterm-review-234p]], p. 209).
- **Graph readout:** the sum of the layer-1 values is 13.75 in both orders (p. 94).

### An added A–D edge

An added edge between A and D is different from a change of file order. A also reads D = 8, so the neighbor mean of A becomes about 4.67, and the toy update for A changes from 2 to about 2.83. A graph model can respond to changed connections (p. 96).

### Depth

One or two layers use nearby graph context. More layers reach more distant nodes, but the node vectors can become less distinct, and compute increases. The deck says to choose depth from the task and the validation results (p. 116).

## Related

- [[Permutation Invariance and Equivariance]]: the order properties that the example checks
- [[Neighborhood Aggregation]]: the step that the toy update simplifies
- [[Graph Convolutional Network]]: the full update rule, synchronous layers, and shared weights
- [[Graph Neural Networks]]: inductive use on new nodes and new graphs
- [[Graph]]: nodes, edges, and the adjacency matrix
- [[Node Embeddings]]: a lookup table has no row for a new road E (pp. 58-59)
- [[GNN Applications]]: ETA prediction on real road graphs in Google Maps

## Sources

- [[Block 6 Slides Extended]], pp. 13-18, 24-25, 54-56, 74, 85-96, 99, 107-110, 116
- [[F26-midterm-review-234p]], pp. 198-209, 215, 219: the midterm review of the road example

A page number without a source name refers to [[Block 6 Slides Extended]].
