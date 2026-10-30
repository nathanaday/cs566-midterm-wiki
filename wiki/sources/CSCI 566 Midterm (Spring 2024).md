---
description: "The CSCI 566 midterm exam from Spring 2024 (10 pages, 50 questions plus 6 bonus, answers marked): a sample of what the exam tests, mapped question by question onto the topics of this wiki to rank them by relevance and to show where the wiki had to grow."
aliases: [Spring 2024 Midterm, Sample Midterm]
---

The original is [[attachments/CSCI 566 Midterm (Spring 2024).pdf|CSCI 566 Midterm (Spring 2024).pdf]], 10 pages, an official course document saved as `midterm.pdf` on 2026-10-29.

## Summary

A past CSCI 566 midterm, from Spring 2024, with the answers marked in red. The exam has 50 questions and 6 bonus questions of equal weight, half a point each, in 112 minutes. It is open book and open notes with no electronic devices. Only the answer sheet on page 1 is graded.

The exam is a sample, not the Fall 2026 exam. Two differences from the [[F26-midterm-review-234p]] deck matter when reading the counts below. The 2024 exam asks nothing about attention, Transformers, the LSTM, language models, or agents, while the 2026 review deck spends two of its seven sections there. The 2024 exam also leans harder on graph neural networks and classical ML than the review deck does: 10 questions on graphs and 13 on decision trees, kNN, k-means, and outliers.

Most questions are short recall or a one-line calculation. The calculations are parameter counts for dense and convolutional layers, the output of a tiny linear network, convolution output shapes, and decision tree size bounds.

## Structure

- p. 1, instructions and the answer sheet: [[_index|CSCI 566 Midterm Wiki]].
- p. 2, Q1 to Q8, generalization gap, layer cost, zero initialization, the 1x1 filter, exploding gradients, tree pruning, NaN weights in an RNN, and L2 in GNNs: [[Overfitting and Underfitting]], [[Regularization]], [[Pooling Layer]], [[Weight Initialization]], [[Convolutional Layer]], [[Exploding Gradient Problem]], [[Gradient Clipping]], [[Decision Trees]], [[Recurrent Neural Networks (RNN)]], [[Graph Neural Networks]].
- p. 3, Q9 to Q15, aggregation in GNNs, pooling, why ReLU is nonlinear, a linear-network calculation, tree weaknesses, and graphs of varying size: [[Neighborhood Aggregation]], [[Pooling Layer]], [[Activation Functions]], [[Fundamentals of Deep Learning Nonlinear Activation]], [[Forward Propagation]], [[Decision Trees]], [[Graph Neural Networks]].
- p. 4, Q16 to Q22, directed graphs, graph autoencoders, what counts as regularization, reading activation plots, and preprocessing statistics: [[Graph]], [[Regularization]], [[Activation Functions]], [[Fit Preprocessing on Training Data Only]].
- p. 5, Q23 to Q27, BatchNorm modes, dense parameter growth, RNN facts, the LeNet-5 kernel shape, and the first tree-size bound: [[Batch Normalization]], [[Fully Connected Layer]], [[Recurrent Neural Networks (RNN)]], [[Convolutional Layer]], [[Decision Trees]].
- p. 6, Q28 to Q36, tree-size bounds, linear and nonlinear layers, kNN and conv parameter counts, inference cost, Lasso against Ridge, and the single-neuron gradient step: [[Decision Trees]], [[k-Nearest Neighbors]], [[Convolutional Layer]], [[AlexNet]], [[ResNet]], [[Regularization]], [[Gradient Descent]].
- p. 7, Q37 to Q42, two model-parameterization puzzles, outliers, kNN outlier detection, a circular classifier, and zero training error: [[Function Approximation]], [[Linear Classification]], [[k-Nearest Neighbors]], [[Linear Separability]], [[Model Evaluation]].
- p. 8, Q43 to Q48, MLP parameters, an MLP with no activations, 0/1 loss under backprop, shuffle invariance of a 1x1 conv with global pooling, permutation-invariant functions, and a GNN aggregation design: [[Fully Connected Layer]], [[Loss Functions]], [[Pooling Layer]], [[Permutation Invariance and Equivariance]], [[Neighborhood Aggregation]].
- p. 9, Q49 to Q54, centroids, k-means initialization, kNN regression, residual connections, gradient clipping, and why gradients vanish in deep nets: [[k-Means]], [[Clustering]], [[k-Nearest Neighbors]], [[Residual Connections]], [[Gradient Clipping]], [[Vanishing Gradient Problem]], [[Backpropagation]].
- p. 10, Q55 and Q56, what deep means for a CNN, and the grade curve: [[Convolutional Neural Networks (CNN)]], [[_index|CSCI 566 Midterm Wiki]].

## Question Map

Each row links the topics a student would open to answer the question. The last link in a row is often a topic written for that question; the Gaps section below says why.

| Q | Question | Answer | Topics |
|---|---|---|---|
| 1 | Least common fix for a 100% train / 46% test gap | B | [[Overfitting and Underfitting]], [[Regularization]], [[Batch Normalization]], [[Activation Functions]] |
| 2 | Fastest CNN layer by FLOPs | B | [[Pooling Layer]], [[Convolutional Layer]], [[Batch Normalization]], [[Activation Functions]] |
| 3 | Weights after training from an all-zero start | A | [[Weight Initialization]] |
| 4 | Parameters in one 1x1 filter on a 64x64x3 input, no bias | 3 | [[Convolutional Layer]], [[1x1 Convolution]] |
| 5 | Standard fix for exploding gradients | D | [[Exploding Gradient Problem]], [[Gradient Clipping]] |
| 6 | Purpose of pruning a decision tree | A | [[Decision Trees]], [[Overfitting and Underfitting]] |
| 7 | RNN weights become NaN | B | [[Recurrent Neural Networks (RNN)]], [[Exploding Gradient Problem]] |
| 8 | Does L2 regularization work in GNNs | B | [[Graph Neural Networks]], [[Regularization]] |
| 9 | Purpose of the GNN aggregation function | A | [[Neighborhood Aggregation]], [[Graph Neural Networks]] |
| 10 | Are pooling layers necessary | C | [[Pooling Layer]], [[Convolutional Neural Networks (CNN)]] |
| 11 | Why ReLU counts as nonlinear | C | [[Activation Functions]], [[Fundamentals of Deep Learning Nonlinear Activation]] |
| 12 | Why layers need a nonlinearity | C | [[Fundamentals of Deep Learning Nonlinear Activation]], [[Neural Networks]] |
| 13 | Output of a 3-neuron linear layer | B | [[Forward Propagation]], [[Perceptron]] |
| 14 | Disadvantage of decision trees | C | [[Decision Trees]], [[Overfitting and Underfitting]] |
| 15 | How a GNN handles graphs of different sizes | B | [[Graph Neural Networks]] |
| 16 | Not a method for directed graphs in GNNs | C | [[Graph]], [[Graph Neural Networks]], [[Graph Neural Network Variants]] |
| 17 | What a graph autoencoder is | A | [[Graph Neural Networks]], [[Graph Neural Network Variants]] |
| 18 | Not a regularization technique | C | [[Regularization]], [[Weight Initialization]], [[Data Augmentation]] |
| 19 | Pick the sigmoid curve | E | [[Activation Functions]] |
| 20 | Pick the ELU curve | C | [[Activation Functions]] |
| 21 | Properties that matter in an activation | A | [[Activation Functions]] |
| 22 | Which split to compute preprocessing statistics on | B | [[Fit Preprocessing on Training Data Only]], [[Data Preprocessing]] |
| 23 | BatchNorm at train and test time | A | [[Batch Normalization]], [[Switch the Model to Evaluation Mode When Evaluating]] |
| 24 | Parameter growth when hidden widths double | C | [[Fully Connected Layer]], [[Neural Networks]] |
| 25 | False statement about RNNs | A | [[Recurrent Neural Networks (RNN)]], [[Vanishing Gradient Problem]], [[Exploding Gradient Problem]] |
| 26 | Kernel shape of LeNet C1 from input and output shapes | (3,5,5,4) | [[Convolutional Layer]], [[Convolutional Neural Networks (CNN)]] |
| 27 | Max leaves, binary attributes | A | [[Decision Trees]], [[Decision Tree Size Bounds]] |
| 28 | Max depth, binary attributes | A | [[Decision Trees]], [[Decision Tree Size Bounds]] |
| 29 | Max leaves, continuous attributes | D | [[Decision Trees]], [[Decision Tree Size Bounds]] |
| 30 | Max depth, continuous attributes | C | [[Decision Trees]], [[Decision Tree Size Bounds]] |
| 31 | Which layer is not linear | C | [[Activation Functions]], [[Pooling Layer]], [[Convolutional Layer]], [[Batch Normalization]] |
| 32 | Parameters learned by 3-NN | 0 | [[k-Nearest Neighbors]] |
| 33 | Parameters in a conv layer with bias | 39 | [[Convolutional Layer]] |
| 34 | Least efficient model at inference | A | [[k-Nearest Neighbors]], [[AlexNet]], [[ResNet]] |
| 35 | Ridge or Lasso for feature selection | B | [[Regularization]], [[L1 Regularization and Feature Selection]] |
| 36 | Gradient update of a single linear neuron | A | [[Gradient Descent]], [[Loss Functions]], [[Perceptron]] |
| 37 | y = w^2 x against y = wx | B | [[Function Approximation]], [[Linear Classification]], [[Parameterization of a Hypothesis Class]] |
| 38 | y = tan(w) x + wx against y = wx | D | [[Function Approximation]], [[Linear Classification]], [[Parameterization of a Hypothesis Class]] |
| 39 | Definition of an outlier | B | [[Unsupervised Outlier Model Selection]], [[Outlier Detection]] |
| 40 | How kNN flags outliers | B | [[k-Nearest Neighbors]], [[Outlier Detection]] |
| 41 | Points a circular classifier cannot fit | C | [[Overfitting and Underfitting]], [[Linear Separability]], [[VC Dimension]] |
| 42 | What zero training error implies | D | [[Overfitting and Underfitting]], [[Model Evaluation]] |
| 43 | Parameters of a 4-8-2 MLP | A | [[Fully Connected Layer]], [[Neural Networks]] |
| 44 | What an MLP without activations can fit | A | [[Fundamentals of Deep Learning Nonlinear Activation]], [[Linear Classification]] |
| 45 | Backprop with 0/1 loss | B | [[Loss Functions]], [[Gradient Descent]] |
| 46 | 1x1 conv plus global max pool under pixel shuffling | B | [[Pooling Layer]], [[Convolutional Layer]], [[Permutation Invariance and Equivariance]], [[1x1 Convolution]] |
| 47 | Which function is permutation invariant | C | [[Permutation Invariance and Equivariance]] |
| 48 | Distance-weighted aggregation and invariance | A or C | [[Neighborhood Aggregation]], [[Permutation Invariance and Equivariance]], [[Node Embeddings]], [[Graph Neural Network Variants]] |
| 49 | Meaning of centroid | A | [[k-Means]], [[Clustering]] |
| 50 | Poor k-means initialization | B | [[k-Means]], [[k-Means Initialization and Local Minima]] |
| 51 | kNN for regression | A | [[k-Nearest Neighbors]], [[kNN Regression]] |
| 52 | How residual connections help gradients | A | [[Residual Connections]], [[ResNet]], [[Vanishing Gradient Problem]] |
| 53 | Gradient clipping and vanishing gradients | D | [[Gradient Clipping]], [[Vanishing Gradient Problem]] |
| 54 | Why vanishing gradients hit deep nets | C | [[Vanishing Gradient Problem]], [[Backpropagation]] |
| 55 | What deep means for a CNN | C | [[Convolutional Neural Networks (CNN)]], [[Deep Learning]] |
| 56 | Course logistics: grade curve | C | [[_index|CSCI 566 Midterm Wiki]] |

## Relevance

The count is the number of questions whose row links the topic. It measures how often the 2024 exam touched the topic, not how hard the questions were. Topics with no row are listed at the end as plain text, so the graph keeps them at a distance from this page.

**Core, five or more questions.**

| Topic | Questions |
|---|---|
| [[Activation Functions]] | 7 |
| [[Convolutional Layer]] | 6 |
| [[Decision Trees]] | 6 |
| [[Overfitting and Underfitting]] | 5 |
| [[Graph Neural Networks]] | 5 |

**Supporting, two to four questions.**

| Topic | Questions |
|---|---|
| [[Regularization]] | 4 |
| [[Batch Normalization]] | 4 |
| [[Pooling Layer]] | 4 |
| [[Vanishing Gradient Problem]] | 4 |
| [[k-Nearest Neighbors]] | 4 |
| [[Exploding Gradient Problem]] | 3 |
| [[Convolutional Neural Networks (CNN)]] | 3 |
| [[Fundamentals of Deep Learning Nonlinear Activation]] | 3 |
| [[Neural Networks]] | 3 |
| [[Linear Classification]] | 3 |
| [[Permutation Invariance and Equivariance]] | 3 |
| [[Weight Initialization]] | 2 |
| [[Gradient Clipping]] | 2 |
| [[Recurrent Neural Networks (RNN)]] | 2 |
| [[Neighborhood Aggregation]] | 2 |
| [[Perceptron]] | 2 |
| [[Fully Connected Layer]] | 2 |
| [[ResNet]] | 2 |
| [[Gradient Descent]] | 2 |
| [[Loss Functions]] | 2 |
| [[Function Approximation]] | 2 |
| [[k-Means]] | 2 |

**Touched once.** [[Forward Propagation]], [[Graph]], [[Data Augmentation]], [[Fit Preprocessing on Training Data Only]], [[Data Preprocessing]], [[Switch the Model to Evaluation Mode When Evaluating]], [[AlexNet]], [[Unsupervised Outlier Model Selection]], [[Linear Separability]], [[Model Evaluation]], [[Node Embeddings]], [[Clustering]], [[Residual Connections]], [[Backpropagation]], [[Deep Learning]], [[_index|CSCI 566 Midterm Wiki]].

**Not touched by this exam.** Sixteen topics in this wiki have no question in the 2024 exam: Activation Sparsity, Adapters, Dropout, Dying ReLU, Early Stopping, Fine-Tuning, Gradient-Based Optimizers, Graph Convolutional Network, Layer Normalization, LoRA, Neural Network Training, Optimization, Parameter-Efficient Fine-Tuning, Softmax Layer, Transfer Learning, Transformers. They are left unlinked here so the graph keeps them at a distance from this page. They are where the wiki is wider than this exam: Fall 2026 material the 2024 exam predates, such as Transformers and the fine-tuning family, plus training details such as dropout, early stopping, and normalization.

## Gaps

Questions the slide-based topics answered only partly or not at all, listed by how much the exam leaned on each. Each gap now has a topic, named at the start of its entry. The entries keep the original finding so the reason for each topic stays on record.

- **1x1 convolution**, now [[1x1 Convolution]] (Q4, Q46). Two questions count parameters of, or reason about, a 1x1 filter, and the Convolutional Layer page treats it only in passing.
- **Decision tree size bounds**, now [[Decision Tree Size Bounds]] (Q27 to Q30, four questions). [[Decision Trees]] covers learning, stopping, and pruning, but not the maximum number of leaves or the maximum depth as a function of the number of attributes k and samples N, for binary and for continuous attributes. The exam spends four questions on exactly that.
- **Outlier detection basics**, now [[Outlier Detection]] (Q39, Q40). The only outlier page from the slides, [[Unsupervised Outlier Model Selection]], is a Block 7 research example, as are MetaOD and TOD. Nothing defined an outlier or explains the kNN-distance detector, where points with few close neighbors are flagged.
- **Parameterization of a hypothesis class**, now [[Parameterization of a Hypothesis Class]] (Q37, Q38). Why y = w²x can only fit non-negative slopes while y = tan(w)x + wx fits any slope. [[Function Approximation]] and [[Linear Classification]] do not discuss how the parameterization constrains the reachable functions.
- **Graph autoencoder**, now in [[Graph Neural Network Variants]] (Q17). Autoencoders belong to Block 8, which the midterm does not cover, and no graph page mentioned the unsupervised variant.
- **Directed graphs inside a GNN**, now in [[Graph Neural Network Variants]] (Q16). [[Graph]] defines directed graphs as data, but no page covers the modeling options the question lists: treating edges as undirected, separate weight matrices for in-edges and out-edges, or more flexible weights.
- **Attention-weighted neighbor aggregation**, now in [[Graph Neural Network Variants]] (Q48). [[Neighborhood Aggregation]] and [[Permutation Invariance and Equivariance]] give the invariance argument, but no page covered aggregators that weight neighbors by a learned or distance-based score, the graph attention network. The exam's own answer key hedges between A and C.
- **L1 sparsity and feature selection**, now [[L1 Regularization and Feature Selection]] (Q35). [[Regularization]] lists L1, Lasso, and Ridge as aliases and gives the L1 penalty formula, but does not state that the L1 penalty drives weights to exactly zero and so selects features.
- **k-means local minima**, now [[k-Means Initialization and Local Minima]] (Q50). [[k-Means]] lists initialization as step one but does not say the algorithm converges to a local minimum that depends on it. [[Optimization]] mentions local minima in general.
- **kNN regression**, now [[kNN Regression]] (Q51). [[k-Nearest Neighbors]] covers classification by majority vote only. The regression form averages the neighbors' values.
- **VC dimension**, now [[VC Dimension]] (Q41). One sentence in [[Overfitting and Underfitting]]. The question needs the shattering argument for a circular boundary in the plane.

## Sources

- The exam itself, `midterm.pdf`, 10 pages, with the instructor's answer key marked in red.
