---
description: "The Spring 2024 midterm transcribed question by question with the answer key held out, for timed practice. The marked original is the PDF; the mapping onto topics is the source note."
aliases: [Blank Midterm, Practice Midterm]
---

The questions below are verbatim from [[attachments/CSCI 566 Midterm (Spring 2024).pdf|CSCI 566 Midterm (Spring 2024).pdf]] with the red answer marks removed. The answer key and the mapping onto wiki topics live in [[CSCI 566 Midterm (Spring 2024)]]. Four questions depend on figures that live only in the PDF; each has a placeholder naming the page.

# CSCI 566 Midterm – Spring 2024

This exam contains 50+6 bonus questions with equal weights (each worth ½ point of your total grade). Please only provide your answer in the answer sheet below. We will only collect and grade the first page and not consider the information on other pages. Please make sure your answer is readable.

## Question 1

After training a neural network, you observe a large gap between the training accuracy (100%) and the test accuracy (46%). Which of the following methods is least common to reduce this gap?

- a. L2 regularization
- b. Replace Tanh by Sigmoid activation
- c. Reduce the size of the neural networks
- d. Adding batch normalization

## Question 2

You are benchmarking runtimes for layers commonly encountered in CNNs. Which of the following would you expect to be the fastest (in terms of floating point operations)?

- a. Conv layer (convolution operation + bias addition)
- b. Max pooling
- c. Sigmoid activation
- d. Batch Normalization

## Question 3

Consider a neural network model with parameters initialized with zeros. $w^{[1]}$ denotes the weight matrix of the first layer. You forward propagate a batch of examples, then backpropagate the gradients and update the parameters. Which of the following statements is true?

- a. Entries of $w^{[1]}$ may be positive or negative
- b. Entries of $w^{[1]}$ are all negative
- c. Entries of $w^{[1]}$ are all positive due to the gradient direction in the initial batches
- d. Entries of $w^{[1]}$ are all zeros

## Question 4

If your input image is 64x64x3 (i.e., 3 channels), how many parameters are there in single 1x1 convolution filters without bias?

Answer: ____

## Question 5

Which of the below is typical approach to solve the exploding gradient problem?

- a. Use SGD optimization with small batch sizes
- b. Oversample minority classes
- a. Increase the batch size to reduce overfitting
- b. Resize gradient by their norm to a predefined threshold

## Question 6

What is the primary purpose of pruning in decision trees?

- a. To reduce the depth of the tree and prevent overfitting
- b. To optimize the tree's parameters by L2 regularization and prevent overfitting
- c. To handle missing data
- d. To improve the tree's interpretability by using a smaller tree

## Question 7

You are training an RNN and find that all the weights and parameters are taking on the value NaN (not a number). Which of the following is the most likely cause?

- a. Vanishing gradient problem
- b. Exploding gradient problem
- c. ReLU activation function $g(\cdot)$ used to compute $g(z)$, where $z$ is too large
- d. Sigmoid activation function $g(\cdot)$ used to compute $g(z)$, where $z$ is too large

## Question 8

Will the general neural network regularization techniques like L2 work in Graph Neural Networks (GNNs)?

- a. No. Due to the unique spatial relationship, L2 will push GNN weights to near-zero values, which causes a phenomenon called over-smoothing
- b. Yes. GNNs are still learning the network weights as a type of neural networks
- c. No. L2 is not feasible for GNN since the squared loss will cause gradient error in aggregation
- d. Yes. However, in practice, people most likely rely on early stopping to control GNN complexity but not L2 regularization

## Question 9

What is the primary purpose of the aggregation function in Graph Neural Networks (GNNs)?

- a. Combine information from a node's neighbors to update the node's representation
- b. To reduce the dimensionality of node features before processing
- c. To classify the nodes into different categories based on their features
- d. To predict the presence or absence of edges between nodes in a graph.

## Question 10

Are pooling layers necessary in a convolutional neural network (CNN)?

- a. Yes. Without pooling layers, the spatial correlation will not be kept
- b. Yes. Without pooling layers, CNN will likely face the issue of vanishing gradient problems
- c. No. It is primarily for reducing dimensionality and preventing overfitting
- d. No. It is primarily for amplifying the non-linearity in CNN

## Question 11

Why is the Rectified Linear Unit (ReLU) activation function considered non-linear?

- a. Because it can only output positive values
- b. Because it outputs the same value as its input
- c. Because it introduces a point of non-linearity at zero, where the function changes slope
- d. Because it is a piecewise function with two linear segments

## Question 12

In the context of neural networks, why is nonlinearity an essential component within the layers of the network?

- a. Nonlinearity allows neural networks to compute only linearly separable functions, simplifying calculations
- b. Nonlinearity enables neural networks to make decisions and binary classifications more efficiently
- c. Nonlinearity allows neural networks to learn and model complex patterns and relationships within the data that cannot be represented with linear models
- d. Nonlinearity is primarily used to speed up the training process by reducing the number of required iterations

## Question 13

Consider a simple feedforward neural network model, also known as a multi-layer perceptron (MLP), consisting of a single layer with three neurons. Each neuron receives an input and applies a weight to it. For this scenario, the inputs to the three neurons are 1, 2, and 3, respectively. Correspondingly, the weights applied by the neurons are 4, 5, and 6. After the weighted inputs are summed, a linear activation function is applied to the result. This activation function multiplies the sum by a constant value of 3. What is the final output of the network based on these parameters?

- a. 32
- b. 96
- c. 643
- d. 9

## Question 14

Choose a disadvantage of decision trees among the following.

- a. Decision trees lack interpretability and are not suited for high-stakes applications
- b. Decision trees are costly to run in comparison to kNN
- c. Decision trees are prone to overfit
- d. All of the above

## Question 15

How does a GNN typically handle varying sizes and structures of input graphs?

- a. By padding smaller graphs to match the largest one in the dataset
- b. By utilizing a fixed number of parameters that are shared across different parts of the graph
- c. By employing a variable number of layers depending on the size of the graph
- d. By transforming all graphs to a fixed size before processing

## Question 16

What is NOT a common method for handling directed graphs in GNNs?

- a. Treat them as undirected graphs
- b. Use different weight matrices for incoming and outgoing edges
- c. Use the information of the out-degree nodes only
- d. Allow more flexible weight matrices

## Question 17

Which of the following best describes a Graph Autoencoder?

- a. A network designed for unsupervised learning on graph data
- b. A GNN variant used for regression tasks
- c. A model that predicts the next node in a sequence
- d. A GNN that only uses convolutional layers

## Question 18

Which of the following is not a regularization technique?

- a. Model pruning
- b. L2 norm regularization
- c. Random weight initialization
- d. Data augmentation

## Question 19

> [!figure] See the original PDF, page 4: five activation function plots labelled A through E.

Based on the above figure, which is a sigmoid function?

Answer: ____

## Question 20

> [!figure] See the original PDF, page 4: the same five activation function plots labelled A through E.

Based on the above figure, which is an Exponential Linear Unit (ELU) function?

Answer: ____

## Question 21

For all these non-linear activation functions, which are the primary properties that affect their usages in neural networks?

- a. The value range and the rate of response, e.g., the slope
- b. The value range only
- c. The ability to handle probability outputs
- d. The ability to handle probability outputs and the rate of response, e.g., the slope

## Question 22

When computing statistics for data preprocessing (for example, a mean of features), which set of data should be used to compute?

- a. Training dataset only to avoid data leakage
- b. Validation dataset only to avoid overfitting on the training dataset
- c. Training and validation datasets together since both are used for training
- d. Training, validation, and test datasets altogether since we need as much data as possible to approximate statistics

## Question 23

Which of the following statements about batch normalization is true?

- a. During the training time, batch normalization will use the mean and variance of the current mini-batch.
- b. During the test time, batch normalization will use the mean and variance of the current mini-batch.
- c. When batch size is set to the size of the entire dataset, batch normalization on input is equivalent to performing L1 normalization on input.
- d. When batch size is set to the size of the entire dataset, batch normalization on input is equivalent to performing L2 normalization on input.

## Question 24

You have a fully connected neural network with input layer ($i$), 2 hidden layers ($h_1$ and $h_2$) and 1 output layer ($\sigma$). Dimensions of the layers are $i = 10$; $h_1 = 20$; $h_2 = 20$; $\sigma = 10$. Assume fully connected layers do not have biases. You decided to double the number of hidden units in every hidden layer. How many times will it increase the number of parameters of the network?

- a. 1 (the same number of parameters)
- b. 2
- c. 3
- d. 6

## Question 25

Which of the following statements about Recurrent Neural Networks (RNNs) is not true?

- a. RNNs suffer from the vanishing gradient problem but not the exploding gradient problem
- b. RNNs can produce a sequence of outputs
- c. RNNs can deal with variable-length inputs
- d. RNNs are usually difficult to train due to the vanishing gradient problem

## Question 26

> [!figure] See the original PDF, page 5: a LeNet-5 variant diagram with layers C1, P1, C2, P2, F1, F2, F3 and shapes (32, 32, 3), (28, 28, 4), (14, 14, 4), (10, 10, 4), (5, 5, 4), (10), (10), (4).

Consider a variant of LeNet-5 (C1, P1, C2, P2, F1, F2, F3) shown here and answer the corresponding questions. Convolution layers and fully connected layers have weights and biases. Here, this LeNet takes a color image of size (32, 32, 3) as input and outputs a prediction vector of probabilities for 4 classes.

For the first convolutional layer, we observe that the shape of input data is (32, 32, 3) and the shape of output data is (28, 28, 4). Assuming there is no spatial padding for this layer and stride is 1, what is the size of C1's convolutional kernel? The size of a kernel is represented in the form of (input channel, kernel height, kernel width, and output channel). The answer should be four numbers in the parenthesis.

Answer: ( ____ , ____ , ____ , ____ )

## Question 27

Assume we are trying to learn a decision tree. Our input data consists of $N$ samples, each with $k$ attributes ($k \ll N$). We define the depth of a tree as the maximum number of nodes between the root and any of the leaf nodes (including the leaf, not the root).

If all attributes are binary, what is the maximal number of leaf (decision) nodes that we can have in a decision tree for this? (choose the closest one if your answer is slightly off).

- a. $2^k$
- b. $NK$
- c. $2NK - 1$
- d. $N^k - 1$

## Question 28

For the same binary-valued tree, what is the maximum possible depth of a decision tree for this data?

- a. $O(k)$.
- b. $O(k - 1)$
- c. $O(\log k)$
- d. $O(\log(k + N))$

## Question 29

If all attributes are continuous, what is the maximum number of leaf nodes that we can have in a decision tree for this data?

- a. $2^{k-1}$
- b. $NK^2$
- c. $K$
- d. $N$

## Question 30

If all attributes are continuous, what is the maximal possible depth for a decision tree for this? (choose the closest one if your answer is slightly off).

- a. $NK^2$
- b. $K$
- c. $N - 1$
- d. $2^{k-1}$

## Question 31

Which of the following layers is not linear activation functions?

- a. Convolutional layer
- b. Pooling layer
- c. ReLU layer
- d. Batch normalization Layer

## Question 32

There are 100 data instances, each of which is a 64 dimension/feature vector. To have a 3 nearest neighbor classifier on the data, the number of parameters to learn is __.

Answer: ____

## Question 33

In a convolutional layer with 3 filters, each with the size (3, 2, 2) representing C, H, W, the number of parameters in this layer including biases is ____.

Answer: ____

## Question 34

Ss For a 10-way classification task, there are 100 billion images in the training set, each with the size (C, H, W) = (3, 224, 224). After training each of the following models on the task, when a new image comes, which one would be the least efficient to infer the label of the new image?

- a. 10 nearest neighbor classifier
- b. AlexNet
- c. ResNet-50
- d. An MLP with 100 layers, where each layer is in half the size of the previous layer, and the minimum size is 16

## Question 35

Comparing Ridge regression and Lasso regression, which one(s) can help feature selection?

- a. Ridge regression (L2)
- b. Lasso regression (L1)
- c. Both
- d. Neither

## Question 36

Suppose you have a single neuron with a linear activation function $g()$ as above and input $\mathbf{x} = x_0, \ldots, x_n$ and weights $\mathbf{W} = W_0, \ldots, W_n$. Here is the squared error function ($(y - \mathbf{W}^T \mathbf{x})^2$) for this input and the true output is a scalar $y$, what is the weight update rule for the neuron based on gradient given the learning rate is $\lambda$?

- a. $W_i \leftarrow W_i + \lambda 2 x_i (y - \mathbf{W}^T \mathbf{x})$
- b. $W_i \leftarrow W_i + \lambda 2 x_i (y - \mathbf{W}^T \mathbf{x}) + \|\mathbf{W}\|^2$
- c. $W_i \leftarrow W_i + \lambda x_i (y - \mathbf{W}^T \mathbf{x}) + \|\mathbf{W}\|^2$
- d. $W_i \leftarrow W_i + \lambda x_i$

## Question 37

For linear regression models, assume we only observe a single input for each output (that is, a set of {x, y} pairs). We would like to compare the following two models on our input dataset (for each one we split into training and testing set to evaluate the learned model). Assume we have an unlimited amount of data:

$$A: y = w^2 x$$
$$B: y = wx$$

Which of the following is correct (chose the answer that **best** describes the outcome):

- a. There are datasets for which A would perform better than B
- b. There are datasets for which B would perform better than A
- c. Both 1 and 2 are correct.
- d. They would perform equally well on all datasets.

## Question 38

Note that model A now has a new form. Again we assume unlimited data. Which of the following is correct (chose the answer that **best** describes the outcome):

$$A: y = \tan(w)\, x + wx$$
$$B: y = wx$$

- a. There are datasets for which A would perform better than B
- b. There are datasets for which B would perform better than A
- c. Both 1 and 2 are correct.
- d. They would perform equally well on all datasets.

## Question 39

What is an outlier within the context of machine learning and data mining?

- a. An error in data collection
- b. A data point that differs significantly from other observations in the dataset
- c. A data point that lies within the normal range of the distribution
- d. A data point that is the most frequent in the dataset

## Question 40

When using the k-nearest neighbors (k-NN) algorithm for outlier detection, how are outliers determined?

- a. Outliers are the points with the highest density of neighbors
- b. Outliers are the points with the lowest density of neighbors
- c. Outliers are the points that are closest to the center of the dataset
- d. Outliers are the points that are most similar to the k-nearest neighbors

## Question 41

Consider a binary classification problem (2 possible classes) on a 2D plane (2 inputs) with a circular decision boundary ($(x_1 - a)^2 + (x_2 - b)^2 < r^2 \rightarrow y = 0$; otherwise, $y = 1$; $a, b, r$ are learnable parameters). What is the minimum number of distinct points required to make perfect prediction impossible for this classifier?

- a. 2
- b. 3
- c. 4
- d. 8

## Question 42

Consider a supervised learning problem with MSE loss. If the training error is 0, which of the following is true?

- a. Test error will always be 0
- b. True error on any given data will always be 0
- c. Both (A) and (B)
- d. Neither (A) nor (B)

## Question 43

Consider an MLP with one hidden layer of size 8, 4 inputs, and 2 outputs. How many learnable parameters does this network have? (ignore the bias term; assume activation functions don't have parameters)?

- a. 48
- b. 40
- c. 24
- d. 8

## Question 44

Consider an MLP with one hidden layer, 2 inputs, and 1 output, but no activation after the hidden or the output layer. Which of the following functions can it predict accurately (assuming there is enough data and hidden neurons available for convergence)?

- a. $y = x$
- b. $y = |x|$
- c. $y = x^2$
- d. Both (A) and (B)

## Question 45

Consider a binary classification problem (2 possible classes) with 0/1 loss (loss = 0 if the prediction is correct, loss = 1 otherwise). Can backpropagation + SGD (let us assume magically it is differentiable) be used to train a neural network for this problem?

- a. Yes, regardless of the output activations or the NN architecture
- b. No, regardless of the output activations or the NN architecture
- c. Yes, but only for some output activations (regardless of the NN architecture)
- d. Yes, but only for certain NN architectures and output activation functions

## Question 46

Consider an $8 \times 8$ input image passed through a CNN with a $1 \times 1$ filter and stride of 1. Assume that the convolution operation is followed by an $8 \times 8$ max pool operation. Will output change if pixels in the input image are shuffled without changing the CNN weights?

- a. Yes
- b. No
- c. Depends on the shuffling
- d. Depends on the weights

## Question 47

Which of the following functions are permutation invariant ($x_1, x_2, x_3$ are inputs)?

- a. $f(x) = x_1 + 2x_2 + x_3$
- b. $f(x) = \text{average}(x_1, 2x_2, x_3)$
- c. $f(x) = \max(\text{relu}(x_1), \text{relu}(x_2), \text{relu}(x_3))$
- d. None of above

## Question 48

Consider a GNN with the following functions for calculating node embeddings $z_v$ of node $v$:

$$h_v^{(0)} = x_v$$
$$h_v^{(k+1)} = f\left(\text{AGGREGATE}\left(h_{u_1}^{(k)}, h_{u_2}^{(k)}, \ldots, h_{u_n}^{(k)}, h_v^{(k)}\right), h_v^{(k)}\right) \quad \{u_1, u_2, \ldots, u_n\} \in N(v)$$
$$z_v = h_v^{(K)}$$

Assume you are solving a problem for which the neighborhood aggregation (AGGREGATE function above) should weigh the neighbors' embeddings ($h_{u_i}^{(k)}$) based on their distance to the embedding of the current node ($h_v^{(k)}$). Is it possible to implement such a function while preserving permutation invariance?

- a. Yes
- b. No
- c. Yes, but only for some distance functions
- d. Yes, but only for some graphs

## Question 49

In the context of clustering, what does the term "centroid" refer to?

- a. The center point of a cluster in k-Means clustering.
- b. The largest point in a dataset.
- c. The average distance between clusters.
- d. The initial point selected at random in hierarchical clustering.

## Question 50

When using the k-means algorithm, if the initial centroids are chosen poorly, which of the following may occur?

- a. The algorithm will not run
- b. The algorithm may converge to a local minimum
- c. The number of clusters will automatically increase
- d. The algorithm will switch to a hierarchical approach

## Question 51

How does the K-nearest neighbors (KNN) algorithm typically handle regression problems?

- a. By calculating the mean value of the nearest neighbors' labels/values
- b. By taking a majority vote among the labels/values of the nearest neighbors
- c. By treating it as a classification problem and use the value from the most similar neighbor
- d. By using gradient descent to minimize the distance between neighbors

## Question 52

The introduction of residual connections in neural networks, as seen in ResNet architectures, helps mitigate the vanishing gradient problem. How do these connections work?

- a. By allowing gradients to flow through additional paths, bypassing non-linear transformations.
- b. By reducing the depth of the network, thereby shortening the gradient propagation path.
- c. By adding a constant to the gradients at each layer.
- d. By forcing all layers to learn an identity function, making the network effectively shallower.

## Question 53

How can gradient clipping help in addressing the vanishing gradient problem?

- a. It makes the gradients larger when they are too small.
- b. It prevents gradients from becoming too large, which may be used for vanishing gradients with caution.
- c. It helps by normalizing the gradients to a specific range to ensure they neither vanish nor explode.
- d. Gradient clipping is not a method used for addressing vanishing gradients.

## Question 54

Why does the vanishing gradient problem primarily affect deep networks?

- a. Because shallow networks do not use gradient-based learning algorithms
- b. Because deep networks have more parameters and thus higher computational complexity
- c. Because in deep networks, the multiple layers can cause the gradients to become very small, exponentially fast as they are propagated backward through each layer
- d. Because deep networks are more prone to overfitting which inherently causes vanishing gradients

## Question 55

When a CNN is described as being "deep," this refers to which of the following?

- a. The number of filters in the convolutional layers.
- b. The size of the filters in the convolutional layers.
- c. The number of convolutional layers in the network.
- d. The amount of pooling layers in the network.

## Question 56

Did the instructor mentioned there could be curve for the grade?

- a. No. It is clearly stated that there is no curve
- b. No. But there might be random grade bump
- c. Yes. It depends on the final score distribution
- d. Yes. There will be a curve no matter of the score distribution
