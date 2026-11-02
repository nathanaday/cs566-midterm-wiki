---
description: "A deep learning architecture for images and video: convolutional and pooling layers extract feature maps, then a flatten step, fully connected layers, and softmax classify them."
aliases: [CNN, CNNs, ConvNet, Convolutional Neural Network]
sources: ["Topic Note - Convolutional Neural Networks (CNN)", "Lecture 3 Notes - Convolutional and Pooling Layers", "[[Block 3 Slides]]", "An Image is Worth 16x16 Words (note)", "FastVLM (note)", "Topic Note - Sequence Transduction", "Fall 2026 Reading List", "[[Block 4 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 4 Convolutional networks
---

### Layer Types

| Layer                                   | What it does                                                                | Parameters? | Linear?                                 |
| --------------------------------------- | --------------------------------------------------------------------------- | ----------- | --------------------------------------- |
| [[Convolutional Layer]]                 | slides learned filters over the input, stacks one activation map per filter | yes         | yes (affine with bias)                  |
| [[Pooling Layer]]                       | downsamples each activation map, one depth slice at a time                  | no          | max: no; average: yes                   |
| [[Fully Connected Layer]]               | flattens the input and multiplies by a weight matrix                        | yes         | yes                                     |
| [[Activation Functions]]                | Applies elementwise nonlinearity to each activation                         | no          | no                                      |
| Normalization ([[Batch Normalization]]) | Rescale activations to a controlled mean and variance                       | yes         | yes (affine per channel; fixed at eval) |
| [[Softmax Layer]]                       | maps class scores to a probability distribution                             | no          | no                                      |


> [!tip]
> Average pooling is a mean over fixed entries, so it is linear. Max pooling is not. "Pooling is nonlinear" is only true for max pooling.


### Standard Architecture Pattern

$$\text{Input} \to [\text{Conv} \to \text{ReLU} \to (\text{Pool})] \times N \to \text{Flatten} \to [\text{FC} \to \text{ReLU}] \times M \to \text{FC} \to \text{Softmax}$$

- **Feature extraction**: repeated Conv + ReLU blocks, with pooling every block or two.
- **Classification**: flatten, one or more FC layers, softmax over the classes.

### Shapes and Parameter Counts

- Each filter is a small weight tensor of size $F$ by $F$ by $C_{in}$ . Sliding one filter over the input produces one 2D activation map.
- The **filter count sets the output channels**, while **kernel size, stride, and padding set the output height and width**.

**Parameter Count**
$$\text{params} = K \cdot (F \cdot F \cdot D_1 + 1)= F^2 D_{1} K \text{ weights} + K \text{ biases}$$

>[!tip] If the question says no bias, drop the K biases term (which is 1 for 1x1)

| Kernel ($D_{1} = 3$, $K = 2$) | Parameters | What it reads        |
| ----------------------------- | ---------- | -------------------- |
| 1x1                           | 8          | channels at one site |
| 3x3                           | 56         | 9 spatial sites      |
| 5x5                           | 152        | 25 spatial sites     |

**FC parameter count** (flattened input of $n$ values, $m$ outputs):

$$\text{params} = m \cdot (n + 1)$$

**Conv output size** (input $W_1 \times H_1 \times D_1$, $K$ filters of size $F$, stride $S$, padding $P$):

$$W_2 = \frac{W_1 - F + 2P}{S} + 1 \qquad H_2 = \frac{H_1 - F + 2P}{S} + 1 \qquad D_2 = K$$

| Input       | K (num filters) | F (filter size) | Output      |
| ----------- | --------------- | --------------- | ----------- |
| `32, 32, 3` | `6`             | `5, 5`          | `28, 28, 6` |


**Pool output size** (no padding, no parameters):

$$W_2 = \frac{W_1 - F}{S} + 1 \qquad H_2 = \frac{H_1 - F}{S} + 1 \qquad D_2 = D_1$$


**"Same" padding.** Stride 1 with $P = (F - 1)/2$ keeps the spatial size:

$$P = \frac{F - 1}{2} \quad\Rightarrow\quad W_2 = W_1 \qquad (F = 3 \to P = 1,\; F = 5 \to P = 2,\; F = 7 \to P = 3)$$

**"Valid" padding.** No padding, so the filter only visits positions where it fits fully:

$$P = 0 \quad\Rightarrow\quad W_2 = \frac{W_1 - F}{S} + 1 \qquad (S = 1 \to W_2 = W_1 - F + 1)$$

| Quantity | Depends on | Does not depend on |
|---|---|---|
| conv parameters | $F$, $D_1$, $K$ | input height and width |
| conv output H and W | $F$, $S$, $P$, input H and W | $K$ |
| conv output depth | $K$ | everything else |
| FC parameters | flattened input size, output size | nothing else |

> [!tip]
> A [[1x1 Convolution]] mixes channels at one position and reads no neighbors: output H and W are unchanged, parameters are $K \cdot (D_1 + 1)$. 



### Why Convolution

- Local connectivity: each output reads a small neighborhood, not the whole image, so parameters do not scale with image size.
- Weight sharing: the same kernel at every spatial position. A larger input repeats the rule with no new parameters.
- The same idea appears elsewhere: an RNN applies the same update at every time step, a GNN at every node. See [[Recurrent Neural Networks (RNN)]] and [[Graph Neural Networks]].
- This built-in bias helps at small data scale; at large pretraining scale, vision [[Transformers]] match or beat CNNs.

## Related

- [[Convolutional Layer]]
- 1x1 Convolution
- [[Pooling Layer]]
- [[Fully Connected Layer]]
- [[Softmax Layer]]
- [[Transformers]]
- Visual Token Count
- [[Recurrent Neural Networks (RNN)]]
- [[Graph Neural Networks]]: the same weights at every node
- [[AlexNet]]
- [[Neural Networks]]
- [[Activation Functions]]
- [[Batch Normalization]]
- [[Overfitting and Underfitting]]
- [[Residual Connections]]
- [[Transfer Learning]]: pretrained CNN backbones are the norm
- Image Captioning
- ImageNet Large Scale Visual Recognition Challenge: ImageNet as the pretraining source

## Sources

- Topic Note - Convolutional Neural Networks (CNN)
- Lecture 3 Notes - Convolutional and Pooling Layers
- [[Block 3 Slides]]
- [[Block 4 Slides]]
- An Image is Worth 16x16 Words (note)
- FastVLM (note)
- Fall 2026 Reading List
- Topic Note - Sequence Transduction
- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
