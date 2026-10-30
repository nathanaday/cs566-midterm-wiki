---
description: Three ways a GNN departs from the basic mean-aggregation GCN, which the sample midterm tests and the decks only touch: edge direction in the update rule, attention weights on the neighbors (GAT), and an unsupervised graph autoencoder that reconstructs the adjacency.
aliases: [Graph Attention Network, GAT, Graph Autoencoder, GAE, Directed Graphs in GNNs, Attention-Weighted Aggregation, Edge Direction in GNNs, Link Reconstruction]
sources: ["[[Block 6 Slides]]", "[[Block 6 Slides Extended]]", "[[F26-midterm-review-234p]]", "[[CSCI 566 Midterm (Spring 2024)]]"]
subject: 7 Graphs
---

## Definition

The GCN of the slides updates a node from the plain mean of its neighbors with two shared matrices, $W_k$ for the neighbor mean and $B_k$ for the node itself ([[Block 6 Slides]], pp. 89, 98). The slides say that GNN approaches differ mainly in what goes in the aggregation box ([[Block 6 Slides]], p. 87). This page covers three variants that the sample midterm asks about: how the update treats a directed edge, how an attention weight replaces the uniform $1/|N(v)|$, and how an autoencoder trains the encoder from the graph structure alone, with no labels.

The decks cover these three variants unevenly. Edge direction appears as a property of the data and in the causal attention mask. Attention appears as a weighted sum over tokens in Block 5 and in the last part of Block 6, with one bridge slide that compares it to a GNN neighborhood. The decks do not name the graph attention network or the graph autoencoder. The sections below mark everything beyond the slides with "Synthesis:".

## Explanation

### The Baseline Update

The rule from [[Block 6 Slides]] (p. 89), with $h_v^{(0)} = x_v$ and $z_v = h_v^{(K)}$:

$$h_v^{(k+1)} = \sigma\left(W_k \sum_{u \in N(v)} \frac{h_u^{(k)}}{|N(v)|} + B_k h_v^{(k)}\right)$$

Three features of this rule matter for what follows. Every neighbor gets the same weight, $1/|N(v)|$. The neighbor set $N(v)$ comes from a binary adjacency matrix that the deck assumes undirected ([[Block 6 Slides]], pp. 45, 63). The matrices $W_k$ and $B_k$ are the only trainable parameters, and the slides say we "can feed these embeddings into any loss function and run SGD to train the weight parameters" (p. 98). [[Neighborhood Aggregation]] covers the computation graph and the layer-by-layer trace; [[Permutation Invariance and Equivariance]] covers why a sum or mean over neighbors is the right kind of aggregator.

### Directed Edges

The decks define directed graphs as data. An undirected link is "symmetrical, reciprocal", and a directed link has a direction; the same slide lists weights, properties, types, and attributes as further considerations on an edge ([[Block 6 Slides]], p. 15; [[Block 6 Slides Extended]], p. 22). A heterogeneous graph $G = (V, E, R, T)$ adds relation types $r \in R$ to the edges, with examples such as (fulvestrant, Treats, Breast Neoplasms) in a biomedical knowledge graph ([[Block 6 Slides]], pp. 12-13; [[Block 6 Slides Extended]], p. 20). See [[Graph]]. The GNN part of the decks never says what the update rule does with a direction. The one directional construction they show is the causal attention mask: "The causal mask makes the allowed interactions directional" ([[Block 6 Slides]], p. 118; [[Block 6 Slides Extended]], p. 125), where a token reads earlier positions and the future is masked.

Synthesis: a directed edge $u \to v$ splits the neighborhood of $v$ into in-neighbors $N_{in}(v)$ (edges that arrive at $v$) and out-neighbors $N_{out}(v)$ (edges that leave $v$). The common ways to put this in the update rule are:

1. **Treat the graph as undirected.** Symmetrize the adjacency, $A \leftarrow \max(A, A^\top)$, and run the baseline rule. The direction is lost, and the method works whenever the direction is not informative for the task.
2. **One weight matrix per direction.** Aggregate the in-neighbors with $W_k^{in}$ and the out-neighbors with $W_k^{out}$, then add the two sums to the self term. The model can then learn that a citation received and a citation given mean different things.
3. **More flexible weights.** Give each edge type or relation its own matrix, $W_k^{r}$ for $r \in R$, which is the heterogeneous graph of p. 12 taken into the update. A relational GCN (Schlichtkrull et al. 2018) does this, with a shared basis across relations when $|R|$ is large. Edge features or edge weights can also scale each message.

Synthesis: aggregating from one direction only is a choice a model can make. Message passing along the edge direction, so that $v$ reads its in-neighbors, is a natural default for a flow or a citation graph. What is not a standard method is to discard the in-edges and keep only the information of the out-neighbors. The sample exam uses this as its distractor (Q16 below).

### Attention-Weighted Aggregation

The decks define attention as a weighted sum: "Given a set of vector values, and a vector query, attention is a technique to compute a weighted sum of the values, dependent on the query" ([[Block 6 Slides]], p. 116). The extended deck adds the mechanics: compare a query with the allowed keys to get weights, then mix the corresponding values ([[Block 6 Slides Extended]], p. 123). The midterm review works a toy case, prefix values 1, 5, 9 with weights 0.2, 0.3, 0.5 giving a context of 6.2, and states the rule that matters here: "Projection parameters are learned and fixed at inference; attention weights are recomputed for each input" ([[F26-midterm-review-234p]], p. 182; also p. 233).

One slide bridges the two worlds. A road GNN reads the connected road segments; self-attention reads the token positions the mask allows. Both restrict information flow. The difference is the weighting: "Attention learns input-dependent mixing weights" ([[Block 6 Slides Extended]], p. 121). The review deck also lists "Transform or weight the messages" as one of the parts of the update that can learn ([[F26-midterm-review-234p]], p. 206; [[Block 6 Slides Extended]], p. 90). This is as far as the decks go.

Synthesis: the graph attention network (GAT, Veličković et al. 2018) replaces the uniform $1/|N(v)|$ with a learned weight per (node, neighbor) pair:

$$e_{vu} = \text{LeakyReLU}\left(a^\top [W h_v \,\|\, W h_u]\right), \qquad \alpha_{vu} = \frac{\exp(e_{vu})}{\sum_{w \in N(v)} \exp(e_{vw})}, \qquad h_v' = \sigma\left(\sum_{u \in N(v)} \alpha_{vu} W h_u\right)$$

The score $e_{vu}$ depends only on the two embeddings $h_v$ and $h_u$; the softmax normalizes the scores over the neighbors of $v$; the output is a weighted sum. Several heads run in parallel and their outputs are concatenated or averaged, as in a Transformer. A distance-based weighting is the same design with a fixed score, for example $e_{vu} = -\lVert h_v - h_u \rVert^2$ or a dot product $h_v^\top h_u$, in place of the learned $a$.

Synthesis: why this keeps permutation invariance. The slides say that summation is a permutation-invariant aggregation ([[Block 6 Slides]], p. 89), and that a mean or a sum treats the neighbors as a set ([[Block 6 Slides Extended]], p. 92; [[F26-midterm-review-234p]], p. 208). A weight $\alpha_{vu}$ that is a function of the pair $(h_v, h_u)$ travels with its neighbor. Relabel the neighbors from B, C to C, B and the terms $\alpha_{vB} h_B$ and $\alpha_{vC} h_C$ swap places inside a sum, which does not care about the order. The softmax denominator is itself a sum over the same set, so it does not change either. The argument needs two conditions:

- The score must depend on the pair of embeddings, or on the pair plus edge features, and never on the position of the neighbor in the list. A weight that goes to "the first neighbor" or that decays with the neighbor's index breaks invariance, in the same way the slot weights $y = 1 \cdot \text{slot}_1 + 2 \cdot \text{slot}_2$ do on [[Block 6 Slides]], p. 79.
- The combination after the weighting must be symmetric: a sum, a mean, or a max. A concatenation or a recurrent pass over the weighted messages depends on the order again.

Any distance function of the two embeddings satisfies the first condition, so the choice of distance does not threaten invariance. What threatens it is a score or a combiner that reads the order.

### Graph Autoencoders

The decks supply both halves of a graph autoencoder and never put them together under that name. The first half is the encoder-decoder framework for [[Node Embeddings]]: an encoder $\text{ENC}(v) = z_v$ maps each node to a $d$-dimensional vector, and the decoder is the dot product $z_v^\top z_u$, whose value should approximate the similarity of $u$ and $v$ in the original network ([[Block 6 Slides]], pp. 46, 49). The objective maximizes $z_v^\top z_u$ for node pairs that are similar (p. 53). The slides call this "unsupervised/self-supervised": it uses no node labels and no node features, and the embeddings are task independent (p. 55). The simplest similarity asks whether two nodes are linked (p. 54).

The second half is the deep encoder. A GNN is $\text{ENC}(v)$ as "multiple layers of non-linear transformations based on graph structure", and the slide adds: "All these deep encoders can be combined with node similarity functions defined earlier" (p. 56). The training slides give the unsupervised setting one line: "No node label available. Use the graph structure as the supervision!" ([[Block 6 Slides]], p. 99; [[Block 6 Slides Extended]], p. 100). Model design step (2) is to define a loss function on the embeddings (p. 102), and the lecture outline promises a "Simple example for unsupervised and supervised training" (p. 62). The supervised example is the cross-entropy node classifier on p. 101; the deck shows no unsupervised example.

Synthesis: a graph autoencoder (GAE, Kipf and Welling 2016) is exactly that combination. The encoder is a GCN, $Z = \text{GCN}(X, A)$, so it uses node features and shares weights across nodes, unlike the shallow lookup of p. 50. The decoder reconstructs the adjacency from the embeddings:

$$\hat{A} = \sigma(Z Z^\top), \qquad \hat{A}_{uv} = \sigma(z_u^\top z_v)$$

The loss is the binary cross-entropy between $\hat{A}$ and $A$ over node pairs, with the missing edges down-weighted or sampled because most pairs of a sparse graph are not linked. Training needs no labels: the graph itself is the target, which is what p. 99 means by structure as supervision. The variational form (VGAE) puts a Gaussian over $Z$ and adds a KL term. The embeddings serve link prediction directly, since $\hat{A}_{uv}$ is a score for an unseen pair, and they serve node classification or clustering after the fact, the way the task list on p. 44 says.

Synthesis: a GAE is a GNN variant by training objective, not by architecture. The same GCN layers run inside it. What changes is the decoder and the loss, from a classifier head with labels to a dot-product decoder with the adjacency.

## Exam Questions

**Q16.** Which of these is not a common method for handling directed graphs in a GNN: treat them as undirected; use different weight matrices for incoming and outgoing edges; use the information of the out-degree nodes only; allow more flexible weight matrices? Answer: C ([[CSCI 566 Midterm (Spring 2024)]], Q16). Options A, B, and D are the three methods of the Directed Edges section: symmetrize, one matrix per direction, and per-relation or edge-conditioned matrices. Option C discards the in-edges, which is half the structure of the graph, and no standard model is defined that way. The decks give only the data side of this question ([[Block 6 Slides]], pp. 12-15); the modeling options are synthesis.

**Q17.** Which best describes a graph autoencoder: a network for unsupervised learning on graph data; a GNN variant for regression; a model that predicts the next node in a sequence; a GNN that uses only convolutional layers? Answer: A ([[CSCI 566 Midterm (Spring 2024)]], Q17). An autoencoder reconstructs its input, here the adjacency, so it trains without labels; that is the "Use the graph structure as the supervision!" setting of [[Block 6 Slides]], p. 99. Option B names a supervised task. Option C describes a sequence model. Option D describes the encoder of a GAE and not the autoencoder itself; the GCN layers are shared with the supervised model, and the decoder and loss are what make it an autoencoder.

**Q48.** A GNN computes $h_v^{(k+1)} = f(\text{AGGREGATE}(h_{u_1}^{(k)}, \ldots, h_{u_n}^{(k)}, h_v^{(k)}), h_v^{(k)})$ over $\{u_1, \ldots, u_n\} = N(v)$. Suppose AGGREGATE should weigh each neighbor's embedding by its distance to the embedding of the current node, $h_v^{(k)}$. Can such a function be implemented while preserving permutation invariance: yes; no; yes, but only for some distance functions; yes, but only for some graphs? The key reads "A or C" ([[CSCI 566 Midterm (Spring 2024)]], Q48). Both readings are defensible, and they differ on what "distance function" is allowed to mean.

- Reading A: any distance $d(h_v, h_u)$ is a function of the pair, so the weight $w_u = g(d(h_v, h_u))$ attaches to neighbor $u$ wherever $u$ sits in the list. The weighted sum $\sum_u w_u h_u$, or the softmax-normalized version, is the same under any reordering, by the same argument that makes the plain mean invariant ([[Block 6 Slides]], p. 89; [[F26-midterm-review-234p]], p. 208). On this reading the answer is yes without conditions, and it is the GAT design.
- Reading C: the grader admits "distance functions" that read something beyond the two embeddings, for example the index of the neighbor in the list or a rank among the neighbors. Those functions break invariance, so the claim holds only for distances that are functions of the pair. On this reading the condition is on the distance, and C is the careful answer.

Option B is wrong under either reading. Option D is wrong because the argument never uses the shape of the graph: it holds for every $N(v)$. For the exam, state the condition (the weight must depend only on the pair of embeddings, followed by a symmetric combiner) and pick A; if an option lets you say "yes, provided the distance depends only on the embeddings", that option is C.

## Related

- [[Graph Neural Networks]]: the parent; the deep encoder that each variant keeps
- [[Neighborhood Aggregation]]: the box these variants change
- [[Permutation Invariance and Equivariance]]: why a pair-wise weight followed by a sum stays invariant, and the slot-weight counterexample
- [[Node Embeddings]]: the encoder-decoder framework and the dot-product decoder that the GAE reuses
- [[Graph]]: directed, heterogeneous, and bipartite graphs as data; link prediction as a task
- [[Loss Functions]]: cross-entropy, on labels in the supervised case and on the adjacency in the GAE
- [[Convolutional Neural Networks (CNN)]]: the fixed-neighbor special case that can learn a different weight per neighbor position ([[Block 6 Slides]], p. 114)

## Sources

- [[Block 6 Slides]], pp. 12-15 (directed and heterogeneous graphs as data), 44-56 (encoder-decoder framework, shallow embeddings, unsupervised objective, deep encoders), 62, 79, 87-89, 98-102 (update rule, parameters, supervised and unsupervised training), 114, 116, 118
- [[Block 6 Slides Extended]], pp. 20, 22, 90, 92, 100, 121, 123, 125
- [[F26-midterm-review-234p]], pp. 182, 206, 208, 233: attention as an input-dependent weighted mix, and the parts of a GNN update that can learn
- [[CSCI 566 Midterm (Spring 2024)]], Q16, Q17, Q48
