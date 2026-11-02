---
description: A convolution with a 1x1 kernel that forms a learned combination of the channels at each position without reading neighboring positions, often used to shrink the channel count before a costlier layer.
aliases: [1×1 Convolution, 1x1 Conv, Pointwise Convolution, 1x1 Bottleneck]
sources: ["[[F26-midterm-review-234p]]"]
subject: 4 Convolutional networks
---

## Definition

A 1x1 convolution is a dense convolution with a 1x1 kernel. At each position it forms a learned linear combination of the input channels and never reads neighboring positions.

### Computation

**Output of filter $k$ at position $(i, j)$.**

$$
y_k(i, j) = \sum_{c=1}^{C_{in}} w_{k,c} \, x_c(i, j) + b_k
$$

The same weights apply at every position. Each output reads only its own position.

**Quick check.** Weights $(1, 2)$, bias $-1$, channels $(2, 5)$ at one site:
$1 \cdot 2 + 2 \cdot 5 - 1 = 11$.

### Shapes and Parameters

**Shape.** $H \times W \times C_{in} \to H \times W \times C_{out}$ with stride 1 and padding 0. Spatial size is unchanged: $(H + 0 - 1)/1 + 1 = H$.

**Parameter count for $C_{out}$ filters of size $k \times k$.**

$$
\text{params} = C_{out} \,(k^2 C_{in} + 1)
$$

| Kernel, 3 in, 2 out | Parameters |
|---|---|
| 1x1 | 8 |
| 3x3 | 56 |
| 5x5 | 152 |

See [[Convolutional Layer]] for the general count.

### Bottleneck: Shrink Channels First

Example: 8x8x64 map through 16 filters of 1x1x64 gives 8x8x16.

| Path from 64 to 32 channels | Parameters |
|---|---|
| Direct 3x3: 64 to 32 | 18,464 |
| 1x1: 64 to 16, then 3x3: 16 to 32 | 1,040 + 4,640 = 5,680 |

The bottleneck path uses about 31% of the parameters of the direct path.

> [!tip]
> Fewer parameters does not mean the same function. The two paths can represent different functions.

> [!tip]
> A 1x1 convolution changes only the channel count. If a question asks for the output height or width, copy the input.

## Related

- [[Convolutional Layer]]
- Depthwise Separable Convolution: its pointwise step is a 1x1 convolution
- [[ResNet]]: bottleneck blocks project down and back up with 1x1 convolutions
- HyDRa: a 1x1 Channel-to-Height convolution
- [[Convolutional Neural Networks (CNN)]]

## Sources

- [[F26-midterm-review-234p]]
