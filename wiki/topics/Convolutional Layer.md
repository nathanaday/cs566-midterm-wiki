---
id: con-jyf2ak
type: topic
kind: concept
description: A CNN layer that slides a set of learned filters over an input volume, computes one dot product plus bias at each position, and stacks the resulting activation maps; its weights are shared across locations.
tags: [machine-learning/cs566-deeplearning]
aliases: [Convolution Layer, Conv Layer, CONV layer, Conv, Locally Connected Layer, Weight Sharing, Parameter Sharing, Shared Weights, Convolution Filter, Kernel, Activation Map, Feature Map, Stride, Zero Padding, Padding, Standard Dense 2D Convolution, Convolution Output Size, Counting Convolution Parameters]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 4 Slides]]", "Lecture 3 Notes - Convolutional and Pooling Layers", "[[F26-midterm-review-234p]]"]
up: ["[[Convolutional Neural Networks (CNN)]]"]
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Convolutional Neural Networks (CNN)]]

## Definition

A convolutional layer applies a set of learned filters (kernels) to an input volume. Each filter slides over the input and computes one dot product at each position. The layer keeps the spatial structure of the input and uses the same parameters at every location ([[Block 4 Slides]], pp. 67-70; [[F26-midterm-review-234p]], pp. 51-53).

## Explanation

### Filters and activation maps

The layer keeps the shape of a 32x32x3 image: height 32, width 32, depth 3 (p. 69). The slides name the three axes of a volume width, height, and depth (p. 106).

A filter always extends the full depth of its input, so a 32x32x3 image takes a 5x5x3 filter (p. 71). At each position the output is one number: the dot product of the filter with a 5x5x3 chunk of the image, plus a bias. This is a 75-dimensional dot product, $w^T x + b$ (p. 72).

One 5x5x3 filter slid over all positions of a 32x32x3 image gives a 28x28x1 activation map (p. 77). A second filter gives a second map of the same size (p. 78). Six filters give six maps, and the layer stacks them into a 6x28x28 output (p. 79). The weights of this layer are a 6x3x5x5 filter tensor and a 6-dim bias vector (pp. 79-80). The same output is a 28x28 grid with a 6-dim vector at each point (p. 81).

The general shapes (p. 83):

| Tensor | Shape |
|---|---|
| Input | $N \times C_{in} \times H \times W$ |
| Filters | $C_{out} \times C_{in} \times K_w \times K_h$ |
| Bias | $C_{out}$ |
| Output | $N \times C_{out} \times H' \times W'$ |

For a batch of 2 images, a 2x3x32x32 input and the same 6x3x5x5 filters give a 2x6x28x28 output (p. 82).

[[F26-midterm-review-234p]] repeats these Block 4 slides, from the 5x5x3 filter to the general shapes (pp. 53-66).

Each output location comes from one window of the input. In the figures, a 3x3 window moves one position at a time over a 6x6 grid and fills a 4x4 output map ([[Block 4 Slides]], pp. 90-105).

First-layer filters are local image templates. They often learn oriented edges and opposing colors. The deck contrasts them with the one template per class of a linear classifier and the bank of whole-image templates of an MLP (pp. 87-89).

### Filter count and output channels

One filter makes one output channel ([[F26-midterm-review-234p]], p. 74). The review checks this with a 3x3 layer, stride 1 and padding 1, on an 8x8x64 input (H x W x C). Only the filter count changes, from 16 to 24 (pp. 73-74):

- The output channels become 24.
- The output height and width stay 8x8. Height and width depend on kernel, stride, and padding, and none of these changed.
- Each filter keeps its 3x3x64 shape. In standard convolution every filter spans all input channels, here still 64 (p. 74).

### Stride

The stride is the distance the filter moves at each step ([[Block 4 Slides]], pp. 107-108). [[F26-midterm-review-234p]] calls it the "step between window starts" (p. 67). A larger stride compresses more and gives a smaller output (Lecture 3 Notes - Convolutional and Pooling Layers). On a 7x7 input with a 3x3 filter ([[Block 4 Slides]], pp. 109-118):

| Stride | Output |
|---|---|
| 1 | 5x5 |
| 2 | 3x3 |
| 3 | does not fit |

The notes give the same stride-3 example, and say that zero padding can make a stride fit (Lecture 3 Notes - Convolutional and Pooling Layers).

Synthesis: the formula below gives (7 - 3)/3 + 1 = 2.33 for stride 3, which is not a whole number.

### Zero padding

In practice it is common to pad the border of the input with zeros ([[Block 4 Slides]], p. 121). Padding 2 adds two rings of zeros to a 5x5 input and makes it 9x9 (pp. 119-120). A 7x7 input with a 3x3 filter, stride 1, and a 1-pixel pad gives a 7x7 output (p. 122).

CONV layers often use stride 1, FxF filters, and padding $(F-1)/2$. This keeps the spatial size: F = 3 pads 1, F = 5 pads 2, F = 7 pads 3 (p. 123). The review's example agrees: a 3x3 convolution with stride 1 and padding 1 keeps an 8x8x64 input at 8x8 ([[F26-midterm-review-234p]], pp. 73-74).

### Hyperparameters and output size

A convolutional layer has four hyperparameters ([[Block 4 Slides]], p. 125; Lecture 3 Notes - Convolutional and Pooling Layers):

| Symbol | Hyperparameter |
|---|---|
| $K$ | number of filters |
| $F$ | filter size |
| $S$ | stride |
| $P$ | zero padding |

For a $W_1 \times H_1 \times C$ input, the output is $W_2 \times H_2 \times K$, where ([[Block 4 Slides]], p. 125; Lecture 3 Notes - Convolutional and Pooling Layers):

$$W_2 = \frac{W_1 - F + 2P}{S} + 1 \qquad H_2 = \frac{H_1 - F + 2P}{S} + 1$$

The slides also write it for one side of size $N$: $(N + 2P - F)/\text{stride} + 1$ ([[Block 4 Slides]], p. 122). The notes mark this calculation as a testable concept (Lecture 3 Notes - Convolutional and Pooling Layers).

[[F26-midterm-review-234p]] writes one row of a convolution with four lowercase symbols (p. 67):

| Symbol | Meaning |
|---|---|
| $n$ | input width before padding |
| $p$ | zero cells added on each side |
| $k$ | window width |
| $s$ | step between window starts |

"Lowercase n is a spatial length, while uppercase N often denotes batch size" (p. 67). The output width is $(n + 2p - k)/s + 1$ (p. 68). Example: with n = 9, p = 1, k = 3, and s = 2, the padded indices run 0 to 10, and windows start at 0, 2, 4, 6, and 8. This gives 5 outputs: (9 + 2 - 3)/2 + 1 = 4 moves plus the first window (p. 68).

Synthesis: this is the formula above with $n = W_1$, $k = F$, $p = P$, and $s = S$. Block 4 uses $N$ for the side size (p. 122), but the review uses $N$ for batch size. Read each formula with its own notation.

The layer has $F^2 C K$ weights and $K$ biases ([[Block 4 Slides]], p. 125). Synthesis: the 6x3x5x5 example above has 450 weights and 6 biases.

Common settings: $K$ is a power of 2 (32, 64, 128, 512), and (F, S, P) is (3, 1, 1), (5, 1, 2), (5, 2, whatever fits), or (1, 1, 0) (p. 126).

### Parameter count

Each filter has $k \times k \times C_{in}$ weights and one bias. Two 3x3 filters over 3 input channels use 2 x (27 + 1) = 56 parameters, "regardless of input size". "A larger input image reuses the same 56 parameters at more positions" ([[F26-midterm-review-234p]], p. 69).

For a standard dense 2D convolution with 3 input channels, 2 filters, one bias per filter, stride 1, and padding that keeps the spatial size (p. 70):

| Kernel size | Parameters | What it reads |
|---|---|---|
| 1x1 | 8 | channels at one site |
| 3x3 | 56 | 9 spatial sites |
| 5x5 | 152 | 25 spatial sites |

Going from 2 to 4 filters doubles the output channels, with the same spatial span (p. 70). The 1x1 kernel mixes only the channels at one position; see 1x1 Convolution.

Synthesis: these counts match the Block 4 count of $F^2 C K$ weights plus $K$ biases. For F = 3, C = 3, and K = 2, that is 54 + 2 = 56.

### From fully connected to convolutional

The deck builds the convolutional layer in steps, for a 200x200 image and 40k hidden units ([[Block 4 Slides]], pp. 57-67; slide credit Marc'Aurelio Ranzato):

| Layer | Connections | Parameters |
|---|---|---|
| [[Fully Connected Layer]] | each hidden unit to every pixel | about 2B (pp. 57-61) |
| Locally connected | each hidden unit to a 10x10 patch, with its own weights | 4M = 40k x 100 (pp. 63-65) |
| Convolutional | local patches, with all local weights shared | not given |

A **locally connected layer** keeps spatial relations like a convolutional layer, but it does not share weights across locations. It can learn different features at different locations. The cost is many parameters, which makes the network prone to overfitting and expensive to compute (p. 129). It is good when images are registered, so that parts show up at the same locations (p. 65), and when the exact location of features matters and the input has a consistent structure (p. 131).

**Weight sharing** is the last step: share all local weights across the hidden units, and the locally connected layer becomes a convolutional layer (pp. 66-67).

Synthesis: with shared weights, the parameter count depends on the filter size and the number of filters, not on the number of hidden units. One 10x10 filter has 100 weights.

[[F26-midterm-review-234p]] restates the property: a convolutional layer shares the same parameters across different locations, and these parameters are learned kernels (pp. 51-52). Its last slide puts CNNs beside RNNs and GNNs: "CNNs, RNNs, and GNNs reuse one set of weights many times, so uses do not add parameters" (p. 233). A CNN uses the same kernel at every spatial position, an RNN the same update at every time step, and a GNN the same update at every node. "A larger compatible input repeats the rule with no new parameters." "Parameters are fixed at inference; attention weights depend on input." (p. 233). See [[Recurrent Neural Networks (RNN)]] and [[Graph Neural Networks]].

### Properties

- Convolutional layers respect the spatial hierarchy of the data, use parameters efficiently because of weight sharing, and are translation equivariant. They are typically used for images or time series ([[Block 4 Slides]], p. 130).
- Convolution is shift-equivariant, but stride, padding, and boundaries can break that (p. 137). See [[Pooling Layer]] for the difference between equivariance and invariance.
- The convolutional layer is linear ([[Block 4 Slides]], p. 152; Lecture 3 Notes - Convolutional and Pooling Layers). A CNN puts an activation function such as ReLU between convolutional layers ([[Block 4 Slides]], p. 86).
- Which layer type is best cannot be answered for all tasks. For images, convolutional layers encode locality and weight sharing cheaply, but vision transformers match or beat them at large pretraining scale (p. 131).

## Related

- [[Convolutional Neural Networks (CNN)]]
- 1x1 Convolution
- [[Depthwise Separable Convolution]]
- [[Pooling Layer]]
- [[Fully Connected Layer]]
- [[Softmax Layer]]
- [[Activation Functions]]
- [[Transformers]]
- [[Recurrent Neural Networks (RNN)]]: the same update at every time step
- [[Graph Neural Networks]]: the same update at every node

## Sources

- [[Block 4 Slides]], pp. 57-72, 77-126, 129-131, 137, 152
- Lecture 3 Notes - Convolutional and Pooling Layers, § Convolutional Layer, § Layer Summary
- [[F26-midterm-review-234p]], pp. 51-74, 233
