---
description: A CNN layer that slides a set of learned filters over an input volume, computes one dot product plus bias at each position, and stacks the resulting activation maps; its weights are shared across locations.
aliases: [Convolution Layer, Conv Layer, Kernel, Feature Map, Weight Sharing, Padding]
sources: ["[[Block 4 Slides]]", "Lecture 3 Notes - Convolutional and Pooling Layers", "[[F26-midterm-review-234p]]"]
subject: 4 Convolutional networks
---

## Definition

A convolutional layer slides a set of learned filters (kernels) over an input volume and computes one dot product plus bias, $w^T x + b$, at each position. Each filter produces one activation map; the layer stacks the maps into the output volume. The same weights serve every location, so the layer keeps spatial structure and shares parameters.

### Shapes

A filter spans the full input depth: a 32x32x3 image takes a 5x5x3 filter, a 75-dim dot product per position. Six such filters give a 6x28x28 output.

| Tensor | Shape |
|---|---|
| Input | $N \times C_{in} \times H \times W$ |
| Filters | $C_{out} \times C_{in} \times F \times F$ |
| Bias | $C_{out}$ |
| Output | $N \times C_{out} \times H' \times W'$ |

Hyperparameters: $K$ filters (so $C_{out} = K$), filter size $F$, stride $S$, zero padding $P$. Common choices: $K$ a power of 2 (32, 64, 128, 512) and $(F, S, P)$ one of (3, 1, 1), (5, 1, 2), (5, 2, fit), (1, 1, 0).

- One filter makes one output channel. Changing $K$ alone changes only the depth of the output.
- Height and width depend only on $F$, $S$, and $P$.
- A 1x1 filter mixes channels at one site and reads no spatial neighbours; see 1x1 Convolution.

### Output Size

**Output size.** For a $W_1 \times H_1 \times C$ input, the output is $W_2 \times H_2 \times K$ with

$$W_2 = \frac{W_1 - F + 2P}{S} + 1 \qquad H_2 = \frac{H_1 - F + 2P}{S} + 1$$

Example: $W_1 = 7$, $F = 3$, $P = 0$. Stride 1 gives $(7 - 3)/1 + 1 = 5$; stride 2 gives 3; stride 3 gives $4/3 + 1$, not a whole number, so the filter does not fit.

**"Same" padding.** Stride 1 with $P = (F - 1)/2$ keeps the spatial size:

$$P = \frac{F - 1}{2} \quad\Rightarrow\quad W_2 = W_1 \qquad (F = 3 \to P = 1,\; F = 5 \to P = 2,\; F = 7 \to P = 3)$$

**"Valid" padding.** No padding, so the filter only visits positions where it fits fully:

$$P = 0 \quad\Rightarrow\quad W_2 = \frac{W_1 - F}{S} + 1 \qquad (S = 1 \to W_2 = W_1 - F + 1)$$

Padding can also make a stride fit that otherwise would not.

> [!tip]
> The midterm review writes the same formula as $(n + 2p - k)/s + 1$ with lowercase $n$ for a spatial length; there uppercase $N$ is batch size. Block 4 uses $N$ for the side length. Read each formula in its own notation, and check that the division is exact.

### Parameter Count

**Parameters.** Each filter has $F \cdot F \cdot C_{in}$ weights and one bias:

$$\text{params} = K \,(F^2 C_{in} + 1) = F^2 C_{in} K \text{ weights} + K \text{ biases}$$

A larger input reuses the same parameters at more positions.

| Kernel ($C_{in} = 3$, $K = 2$) | Parameters | What it reads |
|---|---|---|
| 1x1 | 8 | channels at one site |
| 3x3 | 56 | 9 spatial sites |
| 5x5 | 152 | 25 spatial sites |

Six 5x5 filters on 3 channels: $25 \cdot 3 \cdot 6 + 6 = 456$.

> [!tip]
> Input size, batch size, and stride never enter the parameter count.

### Receptive Field

**Receptive field.** The input region one output unit sees. One layer sees $F \times F$. Stacking layers grows it; with $r_0 = 1$ and strides $S_i$,

$$r_l = r_{l-1} + (F_l - 1) \prod_{i=1}^{l-1} S_i$$

With stride 1 throughout, $L$ stacked $F \times F$ layers see $1 + L(F - 1)$: three 3x3 layers see 7x7, the span of one 7x7 layer, with fewer parameters ($27 C^2$ versus $49 C^2$ per $C$ channels) and extra nonlinearities between them.

### Weight Sharing and Layer Types

For a 200x200 image and 40k hidden units:

| Layer | Connections | Parameters |
|---|---|---|
| [[Fully Connected Layer]] | each unit to every pixel | about 2B |
| Locally connected | each unit to its own 10x10 patch, own weights | 4M = 40k x 100 |
| Convolutional | local patches, weights shared across units | $100 \cdot K$ |

- A locally connected layer keeps locality but not sharing, so it learns location-specific features. It suits registered inputs, at the cost of many parameters and overfitting.
- Sharing the local weights across all positions turns a locally connected layer into a convolutional layer; the parameter count then depends on $F$ and $K$, not on the number of hidden units.
- CNNs, [[Recurrent Neural Networks (RNN)]], and [[Graph Neural Networks]] all reuse one set of weights: the same kernel at every position, the same update at every time step, the same update at every node. A larger compatible input adds no parameters. Parameters are fixed at inference; attention weights in [[Transformers]] depend on the input.

### Properties

- Translation (shift) equivariant: shifting the input shifts the output. Stride, padding, and boundaries can break this. See [[Pooling Layer]] for equivariance versus invariance.
- Linear: a CNN puts an activation such as ReLU between convolutional layers; see [[Activation Functions]].
- Respects spatial hierarchy and uses parameters efficiently; typical for images and time series.
- First-layer filters are local templates, often oriented edges and opposing colours, unlike the whole-image templates of a linear classifier.
- No layer type wins every task; vision transformers match or beat convolution at large pretraining scale.

> [!tip]
> A convolutional layer alone is linear. Two stacked convolutions without a nonlinearity collapse to one linear map.

## Related

- [[Convolutional Neural Networks (CNN)]]
- 1x1 Convolution
- Depthwise Separable Convolution
- [[Pooling Layer]]
- [[Fully Connected Layer]]
- [[Softmax Layer]]
- [[Activation Functions]]
- [[Transformers]]
- [[Recurrent Neural Networks (RNN)]]: the same update at every time step
- [[Graph Neural Networks]]: the same update at every node

## Sources

- [[Block 4 Slides]]
- Lecture 3 Notes - Convolutional and Pooling Layers
- [[F26-midterm-review-234p]]
