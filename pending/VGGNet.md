---
id: ent-4cd67b
type: topic
kind: entity
description: The CNN of Simonyan and Zisserman (2014) that stacks only 3x3 convolutions and 2x2 max pooling to 16 or 19 layers; it placed 2nd in classification and 1st in localization at ILSVRC 2014 with 7.3% top-5 error.
tags: [machine-learning/cs566-deeplearning]
aliases: [VGG, VGG16, VGG19, VGG-16, VGG-19, Simonyan and Zisserman 2014]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 4 Slides]]"]
up: ["[[Convolutional Neural Networks (CNN)]]"]
---

> [!entity] Entity
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Convolutional Neural Networks (CNN)]]

## What it is

VGGNet is the CNN of Simonyan and Zisserman (2014). Its design idea is small filters and deeper networks: 16 to 19 layers, compared with 8 for [[AlexNet]] ([[Block 4 Slides]], p. 184). It uses only 3x3 conv with stride 1 and pad 1, and 2x2 max pool with stride 2 (p. 184). Top-5 error fell from 11.7% (ZFNet, ILSVRC 2013) to 7.3% with VGG in ILSVRC 2014 (p. 184). VGG placed 2nd in classification and 1st in localization that year (p. 199).

## Facts

### Layer stack

- **VGG16.** 2x conv-64, pool, 2x conv-128, pool, 3x conv-256, pool, 3x conv-512, pool, 3x conv-512, pool, then FC 4096, FC 4096, FC 1000, and softmax (pp. 184, 195). The history diagram shows the same five conv blocks, each ending in max pooling (p. 23).
- **VGG19.** Four conv layers in each of the 256 and 512 stages (p. 184).
- **Layer names.** conv1-1 to conv5-3, then fc6, fc7, and fc8 (p. 198).

### Why small filters

- **Same receptive field.** Three stacked 3x3 conv layers with stride 1 have the same effective receptive field as one 7x7 layer (pp. 186, 192). The slides trace one unit in A3 back through A2 (3x3) and A1 (5x5) to a 7x7 region of the input (pp. 187-192).
- **More non-linearity.** The stack is deeper and has more non-linearities (p. 193).
- **Fewer parameters.** With C channels per layer, three 3x3 layers have 3*(3^2 C^2) parameters, against 7^2 C^2 for one 7x7 layer (p. 193). Synthesis: 27C^2 against 49C^2, about 45% fewer.
- **Convergence.** The slides state that stacked 3x3 filters converge better (p. 193).
- **Feature hierarchy.** Early layers learn simple edges and deeper layers learn complex patterns. This can be more effective for complex objects (p. 194).

### Memory and parameters (VGG16)

- **Memory.** About 24M values * 4 bytes, roughly 96MB per image, for the forward pass only. The backward pass roughly doubles it (pp. 196-197).
- **Parameters.** 138M in total, not counting biases (pp. 195-196).
- **Where the memory is.** Most memory is in the early conv layers. Each conv-64 layer at 224x224x64 stores 3.2M values (p. 197).
- **Where the parameters are.** Most parameters are in the late FC layers. The first FC layer has 7*7*512*4096 = 102,760,448. The other two have 4096*4096 = 16,777,216 and 4096*1000 = 4,096,000. Each conv-512 layer with 512 input channels has 2,359,296 (pp. 195, 197).
- **Cost against accuracy.** In the Canziani et al. (2017) comparison, VGG-16 and VGG-19 use the most operations (about 31 and 39 G-Ops) and have the most parameters, but reach only about 71% top-1 (p. 221).

### Practical notes

From p. 199:

- The training procedure is similar to Krizhevsky 2012. VGG does not use Local Response Normalisation (LRN).
- Use VGG16 or VGG19. VGG19 is only slightly better and uses more memory.
- Ensembles give the best results.
- FC7 features generalize well to other tasks.

VGG16 also serves as a detection backbone. In the SSD figure, a 300x300x3 input goes through VGG16 Conv0 to Conv5_3. 3x3 detection heads on several feature maps feed the detections, then non-maximum suppression (p. 166).

## Related

- [[AlexNet]]
- [[ResNet]]
- [[ImageNet Large Scale Visual Recognition Challenge]]
- [[Depthwise Separable Convolution]]
- [[Convolutional Neural Networks (CNN)]]

## Sources

- [[Block 4 Slides]], pp. 23, 166, 184-199, 221
