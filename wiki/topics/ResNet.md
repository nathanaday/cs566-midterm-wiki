---
id: ent-zkq1tw
type: topic
kind: entity
description: The residual network family of He et al. (2015), 18 to 152 layers deep, whose 152-layer model won ILSVRC 2015 classification with 3.57% top-5 error.
tags: [machine-learning/cs566-deeplearning]
aliases: [Residual Network, Residual Networks, ResNet-18, ResNet-34, ResNet-50, ResNet-101, ResNet-152, He et al. 2015, Deep Residual Learning for Image Recognition]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 4 Slides]]", "[[Block 7 Slides]]"]
up: ["[[Convolutional Neural Networks (CNN)]]"]
---

> [!entity] Entity
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Convolutional Neural Networks (CNN)]]

## What it is

ResNet is a family of very deep CNNs built by stacking residual blocks ([[Block 4 Slides]], pp. 201, 211; see [[Residual Connections]]). Every ResNet slide in the deck cites He et al., 2015 (pp. 201-220). A 152-layer ResNet won ILSVRC 2015 classification with 3.57% top-5 error (p. 201). The deck marks ResNet as the start of the "Revolution of Depth" (p. 200).

## Facts

### Results

- **ILSVRC 2015.** 3.57% top-5 error (p. 201). The charts round this to 3.6 (pp. 181, 220). One trained human annotator had 5.1% top-5 error on 1500 images (Russakovsky 2014) (p. 220).
- **All five main tracks.** MSRA took 1st place in all five main tracks at ILSVRC and COCO 2015 (p. 219):
  - ImageNet classification, with 152-layer nets
  - ImageNet detection, 16% better than 2nd
  - ImageNet localization, 27% better than 2nd
  - COCO detection, 11% better than 2nd
  - COCO segmentation, 12% better than 2nd
- **No degradation.** ResNet trains very deep networks without degradation: 152 layers on ImageNet and 1202 on CIFAR. Deeper networks now reach lower training error, as expected (p. 219). See [[Residual Connections]] for the degradation problem.

### Architecture

- **Stem.** A 7x7 conv with 64 filters and stride 2, then a pool (p. 213).
- **Body.** Stacked residual blocks. Each block has two 3x3 conv layers (p. 211).
- **Stages.** The network periodically doubles the number of filters and downsamples with stride 2 (/2 in each spatial dimension). For example, a "3x3 conv, 128 filters, /2 spatially with stride 2" follows the 64-filter layers. The slide says this halves the activation volume (p. 212). Synthesis: twice the channels on a quarter of the spatial positions gives half the values.
- **Head.** A global average pooling layer follows the last conv layer. The only FC layer is FC 1000 to the output classes (p. 214). In theory, a ResNet can train on input images of variable size (p. 214). Synthesis: global average pooling removes the dependence on the spatial size.
- **Depths.** 18, 34, 50, 101, or 152 layers for ImageNet (p. 215).

### Bottleneck block

ResNet-50 and deeper use a "bottleneck" block to improve efficiency (p. 216). The example block takes a 28x28x256 input (pp. 216-217):

1. 1x1 conv, 64 filters, then BN and ReLU. This projects to 28x28x64.
2. 3x3 conv, 64 filters, then BN and ReLU. The 3x3 conv operates over only 64 feature maps.
3. 1x1 conv, 256 filters. This projects back to 28x28x256.
4. Add the shortcut.

Synthesis: the costly 3x3 conv runs on 64 channels instead of 256.

### Training recipe

From p. 218:

- [[Batch Normalization]] after every conv layer
- He (Kaiming) initialization; see [[Weight Initialization]]
- SGD with momentum 0.9
- Learning rate 0.1, divided by 10 when validation error plateaus
- Mini-batch size 256
- Weight decay 1e-4
- No dropout

### Later block design

The creators of ResNet later reordered the block as BN, ReLU, conv, BN, ReLU, conv, then the identity add, for a more direct information path and better performance (p. 223). See [[Residual Connections]].

### Author

The Block 7 deck has a slide titled "Kaiming Initialization". It shows a photo and two bullets: "MIT Professor" and "Author of ResNet (covered in this our CNN lecture), Faster R-CNN, and more" ([[Block 7 Slides]], p. 80). The slide does not give the person's full name. Two slides earlier, the slide "Weight Initialization: Kaiming / MSRA Initialization" cites He et al, "Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification", ICCV 2015 (p. 78).

Synthesis: the given name "Kaiming" on p. 80 and the surname "He" in the p. 78 citation together name Kaiming He. This agrees with the "He et al., 2015" citation on every ResNet slide in [[Block 4 Slides]] (pp. 201-220) and with "He (Kaiming) initialization" in the training recipe (p. 218). The wiki's [[Convolutional Neural Networks (CNN)]] topic lists He among the Faster R-CNN authors (Ren, He, Girshick, Sun, 2015). The slides never state the full name, so this identity is an inference.

## Related

- [[Residual Connections]]: the residual block, the degradation problem, and the gradient argument
- [[Batch Normalization]]
- [[Weight Initialization]]: He (Kaiming) initialization, named for the author of ResNet
- ImageNet Large Scale Visual Recognition Challenge
- VGGNet
- [[AlexNet]]
- [[Vanishing Gradient Problem]]
- [[Convolutional Neural Networks (CNN)]]

## Sources

- [[Block 4 Slides]], pp. 181, 200-220, 223
- [[Block 7 Slides]], pp. 78, 80
