---
id: con-0znvdc
type: topic
kind: concept
description: A model built from layers of simple units, each a weighted sum followed by a non-linear activation function, with much more representational power than a linear classifier.
tags: [machine-learning/cs566-deeplearning]
aliases: [Fully Connected Network, Multi-Layer Perceptron, MLP, Neural Network Data Shape]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 3 Slides]]", "Lecture 3", "[[Block 4 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[CS566-DeepLearning]]", "[[Machine Learning]]"]
---

> [!concept] Concept
> 4 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[CS566-DeepLearning]] · [[Machine Learning]]

## Definition

A neural network is "a set of neurons (atomic functions) connected in a non-linear way" ([[Block 3 Slides]], p. 28).

One artificial neuron multiplies inputs $x_1, \dots, x_n$ and a constant input of 1 by weights $w_1, \dots, w_n$ and $w_0$, then sums them (p. 27). A linear neuron outputs the sum. A logistic neuron passes the sum through the sigmoid: a "different way for activation; no longer a linear one" (p. 29, modified from an HKUST slide).

"Neural network" is a broad term. The slides say these models are "more accurately called 'fully-connected networks' or sometimes 'multi-layer perceptrons' (MLP)" (p. 62). A network with one hidden layer is a "2-layer" or "1-hidden-layer" net. A network with two hidden layers is a "3-layer" or "2-hidden-layer" net (p. 93, credited to Stanford CS231n).

"(Fully-connected) Neural Networks are stacks of linear functions and nonlinear activation functions; they have much more representational power than linear classifiers" (p. 207).

## Explanation

### Layer formulas

The formulas start from the linear score $f = Wx$ ([[Linear Classification]]):

- 2-layer network: $f = W_2 \max(0, W_1 x)$, with $x \in \mathbb{R}^D$, $W_1 \in \mathbb{R}^{H \times D}$, $W_2 \in \mathbb{R}^{C \times H}$ ([[Block 3 Slides]], p. 62).
- 3-layer network: $f = W_3 \max(0, W_2 \max(0, W_1 x))$, with $W_1 \in \mathbb{R}^{H_1 \times D}$, $W_2 \in \mathbb{R}^{H_2 \times H_1}$, $W_3 \in \mathbb{R}^{C \times H_2}$ (p. 63, credited to CS231n).
- "In practice we will usually add a learnable bias $b$ at each layer as well" (pp. 62-63).

A 3-layer example in NumPy with sigmoid activations: $h_1 = \sigma(W_1 x + b_1)$ (4×1), $h_2 = \sigma(W_2 h_1 + b_2)$ (4×1), $\text{out} = W_3 h_2 + b_3$ (1×1), for a random 3×1 input (p. 94, credited to CS231n). [[Forward Propagation]] evaluates these formulas in order.

### Data shapes

The layer sizes set the weight shapes. A 28×28 image gives 784 input features. A first hidden layer of 128 neurons needs $W_1$ of shape 784×128: $[1 \times 784] \cdot [784 \times 128] = [1 \times 128]$. A second 128-neuron layer needs $W_2$ of shape 128×128 ([[Block 3 Slides]], pp. 59-61). The midterm review repeats this example ([[F26-midterm-review-234p]], pp. 38-40).

The user's lecture notes give the rule: the weight matrix dimensions are the number of features × the number of neurons, "e.g. 784 x 128 if we have 784 features and 128 neurons" (Lecture 3, § Neural Network Data Shape).

Synthesis: these slides multiply a row vector by $W$ ($xW$). The layer formulas above multiply $W$ by a column vector ($Wx$). Both give the same outputs. [[Block 3 Slides]] does not mention the change. The midterm review does: "Some source slides use row vectors xW; new formulas here use column vectors Wx, and parameter counts are the same" ([[F26-midterm-review-234p]], p. 37).

### Counting parameters

The trainable parameters of a dense network are the entries of its weight matrices and its bias vectors. The midterm review counts them for a network with widths 2, 3, and 1, with column vectors ($Wx + b$) ([[F26-midterm-review-234p]], p. 41):

| Part | Shape | Parameters |
| --- | --- | --- |
| $W_1$ | 3 × 2 | 6 |
| $b_1$ | 3 | 3 |
| $W_2$ | 1 × 3 | 3 |
| $b_2$ | 1 | 1 |
| Total | | 13 |

"Inputs and activations are recomputed per example, and ReLU has no trainable parameters" (p. 41). The review puts this count under forward computation: "Track tensor shapes through each layer, and separate trainable parameters from computed activations" (p. 37). See [[Forward Propagation]].

Synthesis: a dense layer from $n$ inputs to $m$ outputs, with a bias, has $mn + m$ parameters. If each layer has a bias, the 784-to-128 layer above has $784 \times 128 + 128 = 100{,}480$ parameters, and the 128-to-128 layer has $128 \times 128 + 128 = 16{,}512$. A row-vector layer ($xW$) has the same count. [[Fully Connected Layer]] shows why this count becomes too large for raw images.

### Hierarchical computation

Each layer's output is the next layer's input. On [[Block 3 Slides]], p. 64, an input of 3072 features goes through a 100-unit hidden layer to 10 scores: "Input features compressed from 3072 to 10" (credited to CS231n). Synthesis: 3072 = 32×32×3, the size of a CIFAR-10 image.

### Why the max operator matters

[[Block 3 Slides]] calls $\max(0, z)$ "the activation function" (p. 65). Without it, $f = W_2 \max(0, W_1 x)$ becomes $f = W_2 W_1 x$. $W_3 = W_2 W_1$ is one matrix, so "we end up with a linear classifier again!" and "Neural networks need this non linearity!!" (p. 66, credited to CS231n). The midterm review repeats both slides ([[F26-midterm-review-234p]], pp. 43-44). See [[Activation Functions]], [[Fundamentals of Deep Learning Nonlinear Activation]], [[Deep Learning]], and [[Linear Separability]].

### What an MLP learns from images

[[Block 4 Slides]] compares what models learn from images (pp. 87-88, credited to CS231n). A linear classifier learns "one template per class" (p. 87). An MLP learns a "bank of whole-image templates" (p. 88). The slides use this contrast to lead into what convolutional filters learn; see [[Convolutional Neural Networks (CNN)]]. Synthesis: each first-layer unit connects to every pixel, so its weights form a template the size of the whole image.

### Model families

[[Block 4 Slides]] groups neural network models into feedforward networks (CNNs, ...), recurrent networks (RNNs, ...), memory networks, and others (p. 8). See [[Convolutional Neural Networks (CNN)]] and [[Recurrent Neural Networks (RNN)]].

### From one unit to a network

Each unit of a network represents a "neuron" ([[Block 3 Slides]], p. 24). The linear model $Wx + b$ from [[Linear Classification]] is "a unit used in deep neural networks too" (pp. 25-26). A [[Perceptron]], $\text{sign}(Wx + b)$, "itself can only address linearly separable problem; but connecting them together makes a huge difference" (p. 27).

### Brain analogy and its limits

The slides say deep learning "may be motivated by human brain" (p. 17). They show neuron anatomy and a chain of neurons, each one's output feeding the next (pp. 19-23). They then limit the analogy. Biological neurons have many types, dendrites can do complex non-linear computation, and synapses are "not a single weight but a complex non-linear dynamical system". "These are good motivations, while the actual relationship is weak" (p. 18, citing London and Hausser, "Dendritic Computation"). "Artificial Neurons are inspired by biological neurons. They are NOT exactly the same" (p. 30).

### Why deep

The slides show [[AlexNet]] (Krizhevsky et al., NIPS 2012) and GoogLeNet (Szegedy et al., "Going deeper with convolutions", CVPR 2015) as deep examples (pp. 31-32; see [[Convolutional Neural Networks (CNN)]]). They compare a shallow network (one hidden layer) with a deep one (two densely connected hidden layers) (p. 33). A network has two passes: "Inference (forward pass)" and "Learning (backward)" (p. 35).

### Capacity and regularization

On one dataset, 3, 6, and 20 hidden neurons draw more and more complex decision boundaries: "more neurons = more capacity" (p. 95). "Larger Model Capacity May Overfit – Need to Regularize them": the slides show the regularized loss $L(W) = \frac{1}{N}\sum_i L_i(f(x_i, W), y_i) + \lambda R(W)$ with $\lambda \in \{0.001, 0.01, 0.1\}$, and the larger $\lambda$ gives a smoother boundary (p. 96). See [[Regularization]] and [[Overfitting and Underfitting]].

## Related

- [[Forward Propagation]]
- [[Backpropagation]]
- [[Activation Functions]]
- [[Fundamentals of Deep Learning Nonlinear Activation]]
- [[Fully Connected Layer]]: the parameter cost of a dense layer on images
- [[Perceptron]]
- [[Linear Classification]]
- [[Linear Separability]]
- [[Deep Learning]]
- [[Regularization]]
- [[Overfitting and Underfitting]]
- [[Convolutional Neural Networks (CNN)]]
- [[Recurrent Neural Networks (RNN)]]
- [[AlexNet]]

## Sources

- [[Block 3 Slides]], pp. 17-35, 59-66, 93-96, 207
- [[Block 4 Slides]], pp. 8, 87-88
- Lecture 3, § Neural Network Data Shape
- [[F26-midterm-review-234p]], pp. 37-44
