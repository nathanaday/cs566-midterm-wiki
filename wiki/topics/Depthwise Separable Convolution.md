---
id: con-mqw48e
type: topic
kind: concept
description: A factorization of a standard convolution into a per-channel depthwise convolution and a 1x1 pointwise convolution, which cuts parameters and multiply-accumulates about 8x in the course example; MobileNets are built from it.
tags: [machine-learning/cs566-deeplearning]
aliases: [Depthwise Separable Conv, Depthwise + Pointwise Convolution, MobileNets Block]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 4 Slides]]"]
up: ["[[Convolutional Neural Networks (CNN)]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Convolutional Neural Networks (CNN)]]

## Definition

A depthwise separable convolution splits a standard convolution into two steps ([[Block 4 Slides]], pp. 224-226):

1. A depthwise convolution filters each input channel on its own (groups = C).
2. A 1x1 pointwise convolution mixes the channels.

MobileNets replace standard convolutions with this block (p. 224).

## Explanation

### Cost

For a 3x3 conv from C to C channels on an H x W map, a standard layer costs 9C^2HW. The MobileNets block (3x3 depthwise, then 1x1 pointwise) costs 9CHW + C^2HW ([[Block 4 Slides]], p. 224). Synthesis: the ratio is 1/C + 1/9, so the saving nears 9x when C is large.

### Worked example

C_in = 64, C_out = 128, K = 3, H = W = 56. Each output channel has one bias, and the MAC counts exclude bias (p. 225):

| Layer | Parameters | MACs |
|---|---|---|
| Standard conv | 73,856 | 231,211,008 |
| Depthwise part | 640 | 1,806,336 |
| Pointwise part | 8,320 | 25,690,112 |
| Separable total | 8,960 | 27,496,448 |

The separable version has 8.24x fewer parameters and 8.41x fewer MACs (p. 225). The output stays 56x56x128 and the receptive field stays 3x3 (p. 226).

### Trade-offs

From p. 226:

- Per-channel filtering followed by 1x1 mixing cannot represent every coupling that a full convolution can.
- At matched parameters, the factorization often costs some accuracy. More width or depth can recover it.
- Fewer MACs may not run faster. Kernels, memory bandwidth, and hardware decide the speed. FasterNet (CVPR 2023) measures this gap.

### MobileNets

MobileNets (Howard et al., 2017) are efficient CNNs for mobile applications. They are much more efficient than standard CNNs, with little loss in accuracy. Follow-up work includes MobileNetV2 (Sandler et al., 2018) and ShuffleNet (Zhang et al., CVPR 2018) ([[Block 4 Slides]], p. 224). A MobileNet can also replace VGG16 as the backbone of an SSD detector (p. 166).

## Related

- [[Convolutional Neural Networks (CNN)]]
- [[VGGNet]]: the SSD backbone that MobileNet can replace
- [[ResNet]]: its bottleneck block also uses 1x1 convs to cut cost

## Sources

- [[Block 4 Slides]], pp. 166, 224-226
