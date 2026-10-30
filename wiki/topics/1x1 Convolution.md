---
id: doc-mxad45
type: topic
kind: concept
description: A convolution with a 1x1 kernel that forms a learned combination of the channels at each position without reading neighboring positions, often used to shrink the channel count before a costlier layer.
tags: [machine-learning/cs566-deeplearning]
aliases: [1×1 Convolution, 1x1 Conv, Pointwise Convolution, 1x1 Bottleneck]
created: 2026-10-19T17:47:21
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[F26-midterm-review-234p]]"]
up: ["[[Convolutional Layer]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Convolutional Layer]]

## Definition

A 1x1 convolution is a standard dense convolution with a 1x1 kernel ([[F26-midterm-review-234p]], pp. 70-71). "The 1×1 filter never reads neighboring positions; it only forms a learned combination of the channels stacked at one spot" (p. 71).

## Explanation

### Worked example

Take a 1x1 convolution with 2 input channels, 1 output channel, weights (1, 2), and bias −1. Here x1 and x2 are the channel entries at one position ([[F26-midterm-review-234p]], p. 71):

| Position | Channels (x1, x2) | Computation | Output |
|---|---|---|---|
| 1 | (2, 5) | 1×2 + 2×5 − 1 | 11 |
| 2 | (4, 1) | 1×4 + 2×1 − 1 | 5 |

The same weights apply at every position, and each output reads only its own position.

### Parameters

Each 1x1 filter has one weight per input channel and one bias. With 3 input channels and 2 filters, a 1x1 kernel has 8 parameters, against 56 for a 3x3 kernel and 152 for a 5x5 kernel. The 1x1 kernel reads the "channels at one site" ([[F26-midterm-review-234p]], p. 70). See [[Convolutional Layer]] for the general count.

### Shrinking channels first

An 8x8x64 feature map (H x W x C) passes through 16 filters of size 1x1x64, with stride 1 and padding 0. The output is 8x8x16: 64 features become 16 per site ([[F26-midterm-review-234p]], p. 72).

The review compares two paths from 64 to 32 channels, with biases included (p. 72):

| Path to 32 channels | Parameters |
|---|---|
| Direct 3x3: 64 → 32 | 18,464 |
| 1x1: 64 → 16, then 3x3: 16 → 32 | 1,040 + 4,640 = 5,680 |

"Fewer parameters; the two paths can represent different functions" (p. 72).

Synthesis: the 1x1 path uses about 31% of the parameters of the direct path (5,680 / 18,464). The 1x1 step keeps the 8x8 spatial size, because (8 + 0 − 1)/1 + 1 = 8.

## Related

- [[Convolutional Layer]]
- [[Depthwise Separable Convolution]]: its pointwise step is a 1x1 convolution that mixes the channels
- [[ResNet]]: its bottleneck block uses 1x1 convolutions to project down and back up
- HyDRa: a 1x1 Channel-to-Height convolution for occupancy
- [[Convolutional Neural Networks (CNN)]]

## Sources

- [[F26-midterm-review-234p]], pp. 70-72
