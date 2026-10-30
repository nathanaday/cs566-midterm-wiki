---
id: con-hx89ym
type: topic
kind: concept
description: A graph is data made of nodes and the edges between them, and it records which objects can exchange information. CSCI 566 covers directed, bipartite, and heterogeneous graphs, the choice of nodes, edges, and features, and the node, link, community, and graph levels of graph ML tasks.
tags: [machine-learning/cs566-deeplearning]
aliases: [Graphs, Network, Relational graph, Machine learning on graphs, Graph ML, Graph ML task levels, Graph machine learning task levels, Heterogeneous graph, Bipartite graph, Knowledge graph, Directed graph, Undirected graph, Link prediction, Node classification, Graph-level prediction, Graph representation, "Nodes, edges, and features", Node-level network structure, Graph notation]
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

The slides call graphs "a general language to describe and analyze entities with relations/interactions" ([[Block 6 Slides]], p. 3). A graph has nodes (also called vertices, the set $V$ or $N$) and edges (also called links, the set $E$).

The extended deck opens the block with a shorter statement: "A graph describes which objects can exchange information" ([[Block 6 Slides Extended]], p. 5). The same slide names three uses of graphs in the block (p. 5):

- graph representation: choose the objects, the connections, and the input features
- [[Graph Neural Networks|graph neural network]]: learn predictions by combining neighboring information
- graphs of agents: study communication paths and execution dependencies

The same abstract graph can describe different domains. Actors linked by movies, people linked by relationships, and proteins linked by interactions all give one graph with $|N| = 4$ and $|E| = 4$ ([[Block 6 Slides]], p. 11).

This page is about graphs as data. A computational graph is a different use of the word: it records the operations of a calculation so that backpropagation can run on it.

On this page, a bare page number refers to [[Block 6 Slides]]. Claims from the extended deck name [[Block 6 Slides Extended]].

## Explanation

### Notation

The GNN part of the slides uses this setup for a graph $G$ (p. 63):

- $V$ is the vertex set.
- $A$ is the adjacency matrix, assumed binary.
- $X \in \mathbb{R}^{|V| \times m}$ is a matrix of node features.
- $v$ is a node in $V$, and $N(v)$ is the set of neighbors of $v$.

Node features depend on the domain. In social networks, they can be a user profile or a user image. In biological networks, they can be gene expression profiles or gene function information. If a dataset has no node features, use indicator vectors (a one-hot encoding of each node) or a vector of constant 1s (p. 63).

### Nodes, edges, and features

The extended deck gives nodes, edges, and features different jobs. It uses a small road graph with four road segments ([[Block 6 Slides Extended]], p. 18):

| Part | Job | In the road graph |
| --- | --- | --- |
| Node | one object | one road segment, such as A |
| Edge | one direct connection | A-B, A-C, or C-D |
| Feature | an observed value on the object | current load: A = 1, B = 2, C = 4, D = 8 |

"The feature describes the road; the edge describes its connection" (p. 18). The deck defines a feature as "an observed value we give the model before it predicts" (p. 15). Other possible inputs for a road are current speed, road capacity, and time of day (p. 15).

Synthesis: the feature is a row of the node-feature matrix $X$ in the notation above, and the edges fill the adjacency matrix $A$.

### Why graphs

Many kinds of data are graphs ([[Block 6 Slides]], pp. 4-6):

- event graphs, computer networks, disease pathways, food webs, particle networks, and underground networks (p. 4)
- social, economic, communication, and citation networks, the Internet, and networks of neurons (p. 5)
- knowledge graphs, regulatory networks, scene graphs, code graphs, molecules, and 3D shapes (p. 6)

Complex domains have a rich relational structure. A relational graph can represent this structure, and models can use it when they model the relationships explicitly. The main question of the lecture is: "how do we take advantage of relational structure for better prediction?" (p. 7).

The modern deep learning toolbox is designed for simple sequences and grids: [[Convolutional Neural Networks (CNN)|CNNs]] for images, and [[Recurrent Neural Networks (RNN)|RNNs]] and LSTMs for text and speech (pp. 8, 59). The slides give three reasons why networks are harder (p. 60):

- They have arbitrary size and complex topology, with no spatial locality as in a grid.
- They have no fixed node ordering or reference point.
- They are often dynamic and have multimodal features.

[[Graph Neural Networks]] are the course's answer to these problems.

### Choosing a representation

To build a graph, decide what the nodes are and what the edges are. The slides say that the choice of representation for a domain or problem "determines our ability to use networks successfully" (p. 14):

- In some cases, there is one unambiguous representation.
- In other cases, the representation is "by no means unique".
- The way you assign links determines the questions you can study.

The extended deck adds the input features to this choice: a graph representation chooses the objects, the connections, and the input features ([[Block 6 Slides Extended]], p. 5). One graph can hold different kinds of objects. In its example, an agent, a tool, and a document are nodes, with the edges Agent -calls-> Tool -reads-> Document. The deck concludes: "The node type and edge meaning belong to the representation" (p. 19).

### Kinds of graph

**Undirected and directed.** An undirected graph has symmetrical, reciprocal links. A directed graph has links with a direction. Other things to consider are weights, properties, types, and attributes (p. 15). In the extended deck's undirected example, node B has a self-loop and two edges connect C and D ([[Block 6 Slides Extended]], p. 22). So an edge can start and end at one node, and two nodes can have more than one edge between them.

**Bipartite.** The nodes divide into two disjoint sets $U$ and $V$, and every link connects a node in $U$ to a node in $V$. So $U$ and $V$ are independent sets (p. 16). Examples: authors to papers (they authored), actors to movies (they appeared in), users to movies (they rated), and recipes to ingredients (they contain) (p. 16).

**Heterogeneous.** A heterogeneous graph is $G = (V, E, R, T)$ (p. 12):

- nodes with node types: $v_i \in V$, with type $T(v_i)$
- edges with relation types: $(v_i, r, v_j) \in E$
- relation types: $r \in R$
- nodes and edges can have attributes or features

Many graphs are heterogeneous (p. 13). In a biomedical knowledge graph, the node types are Drug, Disease, Adverse event, Protein, and Pathways. Examples are the node Migraine, the edge (fulvestrant, Treats, Breast Neoplasms), the node type Protein, and the relation type Causes. In an academic graph, examples are the node ICML, the edge (GraphSAGE, NeurIPS), the node type Author, and the relation type pubYear (p. 13). The agent, tool, and document graph in the extended deck is also heterogeneous: it has three node types and two edge meanings ([[Block 6 Slides Extended]], p. 19).

**Knowledge graph.** The slides list knowledge graphs as one kind of graph data. Their example links actors, characters, films, and genres (p. 6). The biomedical knowledge graph on p. 13 is their example of a heterogeneous graph.

### Task levels

Graph tasks work at four levels (p. 17):

| Level | Prediction target | Examples in the slides |
| --- | --- | --- |
| Node | one node | node classification: predict the type of a node (pp. 19, 58) |
| Edge (link) | a pair of nodes | link prediction (pp. 21-24) |
| Community (subgraph) | a group of nodes | community detection: find densely linked clusters of nodes (p. 58) |
| Graph | the whole graph or a subgraph | graph-level prediction and graph generation (pp. 17, 25) |

The review slide names three main tasks: node-level, link-level, and graph-level prediction (p. 18). The "Tasks on networks" slide adds network similarity, which asks how similar two (sub)networks are (p. 58).

**Link prediction.** Predict new, missing, or unknown links from the existing links. At test time, rank the node pairs that have no link, then predict the top $K$ pairs (p. 21). The slides give two examples:

- Recommender systems: the nodes are users and items, and the edges are user-item interactions. The goal is to recommend items that users might like (p. 22). PinSage learns node embeddings so that two cake pins are closer than a cake and a sweater (p. 23).
- A biomedical graph of drugs and proteins, with interactions as edges. A query asks how likely Simvastatin and Ciprofloxacin, taken together, are to break down muscle tissue (p. 24).

**Graph-level prediction.** Make a prediction for an entire graph or a subgraph (p. 25). The slides give traffic prediction and drug discovery as examples (pp. 26-30).

### Node-level structure features

Node-level features describe the structure and position of a node in the network (p. 20):

- node degree
- node importance and position, for example the number of shortest paths that pass through the node, or the average shortest path length to other nodes
- the substructures around the node

### Traditional ML on graphs

The traditional pipeline has four steps: input graph, structured features, learning algorithm, prediction. A person designs the node-level, edge-level, and graph-level features by hand (feature engineering). A model such as an SVM or a neural network then maps the features to labels (p. 40).

[[Node Embeddings|Graph representation learning]] replaces the hand-designed features with learned features (p. 41).

Synthesis: this graph task list is a different axis from Machine Learning Task Types. That page groups tasks by how much of the label $Y$ the training data holds. This page groups tasks by which part of the graph gets the prediction. For example, node classification is usually supervised, and learning [[Node Embeddings]] is self-supervised.

## Related

- [[Node Embeddings]]: learned features for nodes, in place of feature engineering
- Road Delay GNN Example: the road graph of the extended deck, with its nodes, edges, and features
- Graphs of Agents: graphs whose nodes are agents or agent actions, and what an edge means
- [[Graph Neural Networks]]: deep encoders that work on graph structure
- GNN Applications: link prediction and graph-level prediction in use
- [[Permutation Invariance and Equivariance]]: why a model on $A$ and $X$ must not depend on the node order
- Machine Learning Task Types: tasks grouped by supervision, not by graph level
- Computational Graphs: a different kind of graph, used for backpropagation
- [[Convolutional Neural Networks (CNN)]]: the grid case that GNNs generalize
- [[Recurrent Neural Networks (RNN)]]: the sequence case

## Sources

- [[Block 6 Slides]], pp. 3-8, 11-25, 40-41, 58-60, 63
- [[Block 6 Slides Extended]], pp. 5, 15, 18, 19, 22: new claims (the exchange-of-information definition, the three uses of graphs, the definition of a feature, the jobs of nodes, edges, and features, node types and edge meanings in the representation, and the self-loop and multi-edge example). The deck repeats the other claims on this page at these pages: pp. 6-10 (definition, data types, relational structure), p. 17 (common language), pp. 20-23 (heterogeneous graphs, representation, directed and bipartite graphs), pp. 26-27 (task levels), pp. 29-31 (node classification, node-level structure, link prediction), pp. 32-34 (link prediction examples), p. 35 (graph-level prediction), p. 63 (notation).
