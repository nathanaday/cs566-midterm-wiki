---
description: "The CSCI 566 Midterm Review deck by Yue Zhao, Fall 2026 (234 PDF pages): core material of Blocks 1-7 traced through small worked examples and check questions, in seven sections: evaluation and classical ML, forward computation and CNNs, losses and gradients, reliable training and transfer, recurrent memory, attention and Transformers, and graphs."
---

> [!source] PDF · 234 pages · official
> Captured 2026-10-19 from `F26-midterm-review-234p.pdf` (ingest) · absorbed by 2026-10-19 Ingest the CS566 midterm review

![[internal/wiki/originals/ba0a06b4dbe8c5d8.pdf]]

## Summary

The CSCI 566 "Midterm Review" deck by the instructor Yue Zhao, Fall 2026. It covers "Core material from Blocks 1-7, traced through small worked examples" (p. 1). The file name in the course repository says "234p", and the PDF has 234 pages. Each page carries the counter "Review N / 234", which matches the PDF page number. Many pages are copies of lecture slides and name their origin in the header (for example "Block 7, slide 34"). The other pages are new review slides: worked examples and check questions with graded answers.

The deck gives two study routes (p. 3). The class follows a 112-page core route ("PowerPoint: Midterm Core Review") through selected and new slides. The full deck keeps every step for self-study. The last slide gives three study rules (p. 234):

- "Trace each example by hand, then check shapes and parameter counts at every layer."
- "Read loss, optimizer, and normalization conventions from their definitions before computing."
- "Note when training and evaluation modes differ and what makes a model compatible with new inputs."

Notes on reading the deck:

- Most numbers are illustrative course values, for example the 1,000-part defect flagger (pp. 20-25), the 120 flower photos from 24 plants (pp. 5-6), and the four-road graph (pp. 198-219).
- The slides credit Stanford CS 229, CS 231n, CS 224W, and CS 329P, CMU 10601, and Marc'Aurelio Ranzato for some figures.
- The review repeats some lecture slides with small text changes. For example, its copy of the k-means slide reads "Repeat 2.+3." where the Block 2 copy reads "Repeat 1.+2." (p. 34).

## Structure

- pp. 1-3, title, the seven sections, and the core route: [[CS566-DeepLearning]], Yue Zhao.
- pp. 4-9, Evaluation: the three data splits, a split by plant, the choice between two trees, preprocessing fitted on training data, and a check question on the jobs of the splits: [[Model Evaluation]], [[Fit Preprocessing on Training Data Only]].
- pp. 10-19, decision trees, overfitting and underfitting, model complexity, bias and variance, and ensemble averaging: [[Decision Trees]], [[Overfitting and Underfitting]], Tree Ensembles.
- pp. 20-25, accuracy on imbalanced data, precision, recall, F1, the confusion matrix, the decision threshold, and a check question on metric choice: Classification Metrics.
- pp. 26-36, k-nearest neighbors, distance functions, clustering, and k-means: [[k-Nearest Neighbors]], [[Clustering]], [[k-Means]].
- pp. 37-50, Forward computation: tensor shapes, the MLP shape example, counting dense parameters, the collapse of stacked affine layers, the 2-2-1 ReLU network, and activation functions: [[Forward Propagation]], [[Neural Networks]], [[Activation Functions]].
- pp. 51-77, CNNs: the convolutional layer, activation maps, batched shapes, output size, parameter counts, the 1x1 convolution, a filter-count check, and pooling: [[Convolutional Neural Networks (CNN)]], [[Convolutional Layer]], 1x1 Convolution, [[Pooling Layer]].
- pp. 78-100, Losses and gradients: the 0/1 loss, squared loss and its slope, the chain rule, backpropagation on the 2-2-1 network, one gradient-descent step, a dead ReLU, and the sigmoid gate: [[Loss Functions]], [[Backpropagation]], [[Gradient Descent]], [[Dying ReLU]], [[Vanishing Gradient Problem]].
- pp. 101-111, residual connections, gradient clipping, the gradient-descent update, SGD, and momentum: [[Residual Connections]], [[Gradient Clipping]], [[Gradient-Based Optimizers]].
- pp. 112-120, Reliable training: initialization, symmetry breaking, and batch normalization: [[Weight Initialization]], [[Batch Normalization]].
- pp. 121-140, BatchNorm in evaluation mode, weight penalties, dropout and inverted dropout, data augmentation, loss curves, and early stopping: [[Switch the Model to Evaluation Mode When Evaluating]], [[Regularization]], [[Dropout]], [[Data Augmentation]], [[Early Stopping]].
- pp. 141-145, transfer learning: a frozen backbone, a new head, fine-tuning, and the CNN transfer recipe: [[Transfer Learning]], [[Fine-Tuning]], Flower Classifier Running Example, ImageNet Large Scale Visual Recognition Challenge.
- pp. 146-156, Recurrent memory: parameter sharing across time, full and truncated BPTT, and detaching the hidden state: [[Recurrent Neural Networks (RNN)]], Backpropagation Through Time.
- pp. 157-173, the LSTM: the Maya analogy, the three gates, the cell and hidden states, the cell update, and the fixed-size state bottleneck: Long Short-Term Memory.
- pp. 174-196, Attention and Transformers: token and position vectors, attention weights, the causal mask, the token MLP, the Transformer block, generation, parallel training, and a check question on position and the mask: Attention, Positional Encoding, Causal Mask, [[Transformers]], Autoregressive Language Modeling, Teacher Forcing.
- pp. 197-219, Graphs: the road network, message passing, the toy mean update, synchronous layers, depth, invariance and equivariance, readout, prediction heads, shared weights, and inductive use: [[Graph Neural Networks]], Road Delay GNN Example, [[Neighborhood Aggregation]], [[Permutation Invariance and Equivariance]], Head (machine learning), [[Graph Convolutional Network]].
- pp. 220-233, the feature-order question, node reordering with the adjacency matrix, k-hop reach, pixel against node reordering, and weight sharing in CNNs, RNNs, and GNNs: [[Graph Convolutional Network]], [[Permutation Invariance and Equivariance]], [[Neighborhood Aggregation]].
- p. 234, how to study these ideas.
