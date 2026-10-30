---
description: "The two properties a function on a graph needs because the nodes have no fixed order: an invariant function gives the same graph output for every node order, and an equivariant function reorders its node outputs with the nodes."
aliases: [Permutation Invariance, Permutation Equivariance, Permutation-Invariant Function, Permutation-Equivariant Function, Permutation Invariant, Permutation Equivariant, Order Plan, Node Ordering, Graph Readout, Symmetric Readout, Node Renumbering, Whole-Graph Pooling, Shared Node MLP, Node Reordering, Node Permutation, Graph Relabeling, Graph Pooling]
sources: ["[[Block 6 Slides]]", "[[Block 6 Slides Extended]]", "[[F26-midterm-review-234p]]"]
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Graph Neural Networks]]

## Definition

A graph has no canonical order of its nodes ([[Block 6 Slides]], p. 67). Node numbering is arbitrary ([[Block 6 Slides Extended]], p. 66). Permutation invariance and permutation equivariance state how a function on a graph must behave when the node order changes ([[Block 6 Slides]], p. 77):

- **Permutation invariance** applies at the graph level. Permute the input, and the output stays the same.
- **Permutation equivariance** applies at the node level. Permute the input, and the output permutes the same way.

The required property depends on what the model outputs. A model with one output per node needs equivariance: the output rows follow the reordering. A model with one output per graph needs invariance: the graph output stays the same. In both cases the graph is the same. Only its storage order changed, and its connections stay intact ([[Block 6 Slides Extended]], p. 71; [[F26-midterm-review-234p]], p. 231).

## Explanation

Bare page numbers in this section refer to [[Block 6 Slides]]. Claims from [[Block 6 Slides Extended]] name it. [[F26-midterm-review-234p]] is the midterm review deck. It repeats many slides of the extended deck and adds review examples, and its citations give the review page.

### Setup

A graph $G = (A, X)$ has a vertex set $V$, a binary adjacency matrix $A$, and a node feature matrix $X \in \mathbb{R}^{|V| \times m}$. Each node has an $m$-dimensional feature vector. $N(v)$ is the set of neighbors of node $v$ (pp. 63, 72). See [[Graph]].

### Adjacency matrix and feature matrix

A row of the adjacency matrix tells which neighbors one node can read. The matrix and the drawing describe the same graph ([[Block 6 Slides Extended]], p. 54). The adjacency matrix says who is connected, and $X$ records the node inputs. The rows of $X$ follow the same node order as the rows of $A$ ([[Block 6 Slides Extended]], p. 55). Road Delay GNN Example gives both matrices for four roads.

### Keep A and X aligned

When you renumber the nodes, reorder $A$ and $X$ together. Node identity must stay aligned across the graph rows and the feature rows ([[Block 6 Slides Extended]], p. 55).

The midterm review shows this for the four roads ([[F26-midterm-review-234p]], p. 222). The adjacency matrix $M$ has $M[i, j] = M[j, i] = 1$ when roads $i$ and $j$ share an edge. In order A, B, C, D, the feature rows of $X$ are 1, 2, 4, 8. In order D, B, A, C, they are 8, 2, 1, 4, and the rows and the columns of $M$ move in the same way:

$$M_{ABCD} = \begin{bmatrix} 0 & 1 & 1 & 0 \\ 1 & 0 & 0 & 0 \\ 1 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix} \qquad M_{DBAC} = \begin{bmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 \end{bmatrix}$$

"Reorder the feature rows and both matrix axes together to keep the same graph" ([[F26-midterm-review-234p]], p. 222).

Synthesis: this is why a permutation acts on the pair as $(PAP^\top, PX)$, with the same $P$ in both terms. If you reorder only one of them, row $i$ of $X$ no longer describes the node that row $i$ of $A$ connects, and the input describes a different graph.

### Order plans

The slides call one choice of node order an order plan. Two order plans of the same graph give different node feature matrices $X_1, X_2$ and different adjacency matrices $A_1, A_2$ (pp. 68-69). A graph with $|V|$ nodes has $|V|!$ order plans (p. 72). Under a reordering, the graph output must stay the same, and the node outputs must reorder with the nodes (p. 70).

A permutation matrix $P$ shuffles the node order, for example $(A, B, C) \to (B, C, A)$ (p. 72). It maps $X$ to $PX$ and $A$ to $PAP^\top$ (pp. 72, 76).

The extended deck shows a reordering with a six-node sketch in two orders. Colors track the objects, and letters are temporary storage labels. The gold object changes its label from A to E, and its links stay intact: the same colored node keeps the same neighbors ([[Block 6 Slides Extended]], p. 67, from the Stanford CS224W diagrams; [[F26-midterm-review-234p]], p. 227). A reordering of the input rows changes only the storage order ([[Block 6 Slides Extended]], p. 71; [[F26-midterm-review-234p]], p. 231).

### Permutation invariance

Let $f$ map a graph to one vector in $\mathbb{R}^d$. It must give the same vector for any two order plans: $f(A_1, X_1) = f(A_2, X_2)$ (pp. 71-72). Definition, for $f: \mathbb{R}^{|V| \times m} \times \mathbb{R}^{|V| \times |V|} \to \mathbb{R}^d$ (p. 72):

$$f(A, X) = f(PAP^\top, PX) \quad \text{for any permutation } P$$

Example: $f(A, X) = \mathbf{1}^\top X$ is invariant, because $\mathbf{1}^\top P X = \mathbf{1}^\top X$ (p. 77).

Example task: is the whole graph connected? The answer is Yes under both orders of the six-node sketch. Renumbering leaves the whole-graph answer unchanged ([[Block 6 Slides Extended]], p. 68; [[F26-midterm-review-234p]], p. 228).

### Permutation equivariance

Let $f$ map each node to a $d$-dimensional embedding, which gives a matrix in $\mathbb{R}^{|V| \times d}$ (p. 73). The output vector of a node at the same position in the graph must stay the same for any order plan (pp. 74-76). Definition, for $f: \mathbb{R}^{|V| \times m} \times \mathbb{R}^{|V| \times |V|} \to \mathbb{R}^{|V| \times d}$ (p. 76):

$$P f(A, X) = f(PAP^\top, PX) \quad \text{for any permutation } P$$

Examples (p. 77):

- $f(A, X) = X$ is equivariant: $f(PAP^\top, PX) = PX = P f(A, X)$.
- $f(A, X) = AX$ is equivariant: $PAP^\top PX = PAX = P f(A, X)$.

Synthesis: the second example uses $P^\top P = I$, which holds for every permutation matrix.

In the six-node sketch, the gold object keeps its output vector, and the vector moves from row A to row E. The vector of the green object moves from row C to row D. Equivariance keeps the output of every node attached to that node ([[Block 6 Slides Extended]], pp. 69-70; [[F26-midterm-review-234p]], pp. 229-230).

### A counterexample: weights per slot

Take the graph-level predictor $y = 1 \cdot \text{slot}_1 + 2 \cdot \text{slot}_2$. Order A, B with values $[1, 3]$ gives $y = 7$. Order B, A with values $[3, 1]$ gives $y = 5$. Different slot weights make the graph output depend on the node numbering (p. 79). The extended deck gives the same example with other values. Order A, B stores $[1, 2]$ and scores $1 \cdot 1 + 2 \cdot 2 = 5$. Order B, A stores $[2, 1]$ and scores $1 \cdot 2 + 2 \cdot 1 = 4$ ([[Block 6 Slides Extended]], p. 72).

Synthesis: the naive approach that feeds adjacency rows into a deep network is sensitive to node ordering (p. 64) for the same reason. Each input position gets its own weights.

### Shared node MLP

Apply the same function $f$ to each node on its own. Order A, B gives $[f(1), f(3)]$, and order B, A gives $[f(3), f(1)]$, so the map is equivariant (p. 80). The rows reorder correctly, but no node reads its neighbors. A shared node MLP combined with neighbor aggregation gives a graph-aware update (p. 80).

An MLP is a small feedforward [[Neural Networks|neural network]], and a shared node MLP uses the same one for every node. With the shared function $f(x) = 2x$, rows $[1, 2]$ give $[2, 4]$, and rows $[2, 1]$ give $[4, 2]$. Node A gets the same result wherever its row is stored ([[Block 6 Slides Extended]], p. 73). A shared rule can also read neighbors. At road A (load 1, neighbors B = 2 and C = 4), the mean of 2 and 4 is 3 in either listing order ([[Block 6 Slides Extended]], p. 74).

### In a graph neural network

A GNN consists of multiple permutation-equivariant and permutation-invariant functions: a stack of equivariant layers, then an invariant layer for a single graph output (p. 78, after Bronstein, ICLR 2021 keynote). The extended deck shows two permutation-equivariant node-update layers that feed a permutation-invariant graph readout ([[Block 6 Slides Extended]], p. 115; [[F26-midterm-review-234p]], p. 218). The review slide puts it in one line: "Equivariant node layers. Invariant graph pooling." ([[F26-midterm-review-234p]], p. 218).

- **One node's embedding is invariant.** In a GCN, the weights are shared across neighbors, and the average of the neighbors' previous-layer embeddings is permutation invariant (p. 94). Summation is also a permutation-invariant aggregation (p. 89; [[Block 6 Slides Extended]], p. 84). Worked case: road A reads the mean 3 whether its neighbors are listed B, C or C, B, so its toy update is $0.5 \cdot 1 + 0.5 \cdot 3 = 2$ in both cases. A mean or a sum treats the neighbors as a set ([[Block 6 Slides Extended]], p. 92; [[F26-midterm-review-234p]], p. 208).
- **All embeddings together are equivariant.** The rows of the input features and the output embeddings are aligned. Each node's computation is invariant. So after a permutation, a node's row moves, but its embedding stays the same (pp. 95-96). Worked case: the layer-1 outputs in file order A, B, C, D are 2, 1.5, 4.25, 6. In file order D, B, A, C they are 6, 1.5, 2, 4.25. Road A keeps output 2 after its row moves ([[Block 6 Slides Extended]], p. 93; [[F26-midterm-review-234p]], p. 209).
- **Node outputs:** each node embedding passes through a shared head to its own label. Reordering the node inputs reorders the node outputs (p. 108; [[Block 6 Slides Extended]], p. 112). See Head (machine learning).
- **Graph outputs:** a symmetric readout pools the node embeddings with sum or mean. It gives the same graph output after the nodes are reordered (p. 109; [[Block 6 Slides Extended]], p. 113; [[F26-midterm-review-234p]], p. 216). Worked case: the sum of the layer-1 values is $2 + 1.5 + 4.25 + 6 = 13.75$ in order A, B, C, D and in order D, B, A, C. The same set of node vectors gives the same pooled result ([[Block 6 Slides Extended]], p. 94; [[F26-midterm-review-234p]], p. 210).

Node tasks keep one output per node. Graph tasks pool the node vectors into one graph vector. The output task decides whether the model keeps or pools the node vectors ([[Block 6 Slides Extended]], pp. 94, 114; [[F26-midterm-review-234p]], pp. 210, 217).

### State what is reordered

Invariance and equivariance answer different questions. Always state what is reordered and what the output represents ([[Block 6 Slides Extended]], p. 95; [[F26-midterm-review-234p]], p. 211):

| Operation | Reordering | Required behavior |
|---|---|---|
| Neighbor mean at A | B, C → C, B | Same aggregate |
| All node outputs | A, B, C, D → D, B, A, C | Rows move together |
| Whole-graph pooling | A, B, C, D → D, B, A, C | Same graph vector |

A reordering of the file keeps the same physical prediction ([[Block 6 Slides Extended]], p. 95; [[F26-midterm-review-234p]], p. 211).

### A reordering does not change the graph

An added edge is different from a change of file order. In the road example, a new A–D edge changes the neighbor mean of A from 3 to about 4.67, and the toy update for A from 2 to about 2.83. A graph model can respond to changed connections ([[Block 6 Slides Extended]], p. 96).

Synthesis: invariance and equivariance constrain the output only under a relabeling of the same graph. They say nothing about a graph with different edges.

### Contrast with CNN shifts

CNNs use fixed spatial offsets on a grid, and arbitrary pixel permutations do not preserve these offsets (p. 114). Synthesis: the invariance and equivariance discussed for CNN pooling concern shifts of an image on its grid, not reorderings of nodes; see [[Pooling Layer]].

The midterm review shows the difference with a worked case ([[F26-midterm-review-234p]], p. 232). The pooling step is a global max: after convolution, keep the largest value over all spatial positions in each channel. A 5x5 input holds two adjacent ones. With a 3x3 all-ones kernel (stride 1, zero padding 1), one window covers both ones, so its sum is 2. Rearrange the input pixels so the two ones are 3 rows and 3 columns apart. Then every window sum is at most 1, and the global max changes from 2 to 1. A 1x1 convolution followed by a global max gives the same pooled vector, because "The earlier 1 x 1 shared map only moves its outputs when positions move." The slide concludes: "Reordering graph features with adjacency keeps the same graph; moving pixels changes neighborhoods."

Synthesis: the 1x1 convolution is the grid form of the shared node MLP. It reads no neighbors, so it is equivariant under any pixel permutation, and a global max over its outputs is invariant. A 3x3 kernel reads fixed spatial offsets ([[Convolutional Layer]]), and a pixel permutation changes which values sit at those offsets. A node reordering also moves the adjacency, so each node keeps the same neighbors.

## Related

- [[Graph Neural Networks]]
- [[Graph Convolutional Network]]
- [[Neighborhood Aggregation]]
- [[Graph]]
- Road Delay GNN Example: the worked numbers for neighbor order, node order, and graph readout
- Head (machine learning): the shared node head and the graph head after the readout
- [[Neural Networks]]: the MLP that a shared node MLP applies
- [[Pooling Layer]]: shift invariance and equivariance on grids
- [[Convolutional Layer]]: the fixed spatial offsets that a pixel permutation breaks
- [[Convolutional Neural Networks (CNN)]]

## Sources

- [[Block 6 Slides]], pp. 63-81, 89, 94-96, 108-109, 114
- [[Block 6 Slides Extended]], pp. 54-55, 66-74, 84, 92-96, 112-115
- [[F26-midterm-review-234p]], pp. 208-211, 216-218, 222, 227-232
