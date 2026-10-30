---
id: ent-h0f0r4
type: topic
kind: entity
description: The annual ImageNet image classification competition (2010 to 2017), whose winning top-5 error fell from 28.2% to 2.3% as depth grew to 152 layers; its ImageNet data is also the usual pretraining source for CNN backbones.
tags: [machine-learning/cs566-deeplearning, dataset]
aliases: [ILSVRC, ImageNet Challenge, ILSVRC 2015, ImageNet, Rethinking ImageNet Pre-training]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 4 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Convolutional Neural Networks (CNN)]]"]
---

> [!entity] Entity
> 3 sources · refreshed 2026-10-19 · #dataset · #machine-learning/cs566-deeplearning
> Up: [[Convolutional Neural Networks (CNN)]]

## What it is

The ImageNet Large Scale Visual Recognition Challenge (ILSVRC) is an annual image classification competition on ImageNet. [[Block 4 Slides]] charts the top-5 error and depth of its entries from 2010 to 2017 (pp. 181, 222). The chart comes from the Stanford cs231n lecture slides (p. 181).

ImageNet, the dataset of the challenge, is also the usual source for pretraining CNN backbones ([[Block 7 Slides]], pp. 197-198, 206). This topic also covers ImageNet in that role.

## Facts

### Entries by year

From pp. 181 and 222:

| Year | Entry | Top-5 error | Depth |
|---|---|---|---|
| 2010 | Lin et al. | 28.2 | shallow |
| 2011 | Sanchez & Perronnin | 25.8 | shallow |
| 2012 | Krizhevsky et al. ([[AlexNet]]) | 16.4 | 8 layers |
| 2013 | Zeiler & Fergus (ZFNet) | 11.7 | 8 layers |
| 2014 | Simonyan & Zisserman ([[VGGNet]]) | 7.3 | 19 layers |
| 2014 | Szegedy et al. (GoogLeNet) | 6.7 | 22 layers |
| 2015 | He et al. ([[ResNet]]) | 3.6 | 152 layers |
| 2016 | Shao et al. | 3 | 152 layers |
| 2017 | Hu et al. (SENet) | 2.3 | 152 layers |

Human top-5 error is 5.1 (Russakovsky et al.) (p. 181). This is one trained human annotator on 1500 images (p. 220).

VGG placed 2nd in 2014 classification and 1st in localization (p. 199). The exact ResNet figure is 3.57% (p. 201). [[Block 1 Slides]] gives 15.3% for AlexNet, not 16.4 (see [[AlexNet]]).

### Eras

- **2012: first CNN winner.** AlexNet was the first CNN-based winner (p. 182).
- **2014: "Deeper Networks".** The deck marks VGG and GoogLeNet with this label (p. 183).
- **2015-2017: "Revolution of Depth".** Depth grew from 22 layers (GoogLeNet) to 152 (ResNet), and top-5 error fell from 6.7 to 3.6. ResNet, Shao et al., and SENet all used 152 layers, and error fell to 3 and then 2.3, below the human 5.1 (p. 200).

### After 2017

- The official 2017 workshop called it the last ImageNet Challenge competition (p. 228).
- The site said its three tracks would move to Kaggle. Kaggle's localization challenge ran from 2018 to 2020. ImageNet keeps the historical data and an evaluation server (p. 228).
- Reported ImageNet numbers now differ in pretraining data, resolution, and augmentation (p. 228). Synthesis: two numbers compare fairly only under the same setup; see [[What Counts as Solved]].

### Accuracy against cost

Canziani, Paszke, and Culurciello (2017) plot top-1 ImageNet accuracy against operations and parameter count (p. 221):

- Inception-v4 has the highest accuracy, near 80%. AlexNet has the lowest, near 55%.
- VGG-16 and VGG-19 use the most operations and parameters, but reach only about 71%.
- ENet and GoogLeNet reach about 68-69% with very few operations and parameters.

### ImageNet as the pretraining source

[[Block 7 Slides]] uses ImageNet as the source task in transfer learning. See [[Transfer Learning]] and [[Fine-Tuning]].

- **Step 1 of the recipe.** Step 1 is "Train on Imagenet". The network ends in FC-4096, FC-4096, and FC-1000 (p. 197). For step 2, a small dataset with C classes, FC-1000 becomes FC-C. The slide says "Reinitialize this and train" for FC-C and "Freeze these" for the rest (p. 198). [[F26-midterm-review-234p]] repeats this slide. It shows a VGG-style stack of Conv-64 to Conv-512 layers with max pooling below the three FC layers (p. 143).
- **Pretrained backbones are the norm.** Fast R-CNN detection and CNN + RNN captioning both use a "CNN pretrained on ImageNet" ([[Block 7 Slides]], p. 206). See [[Convolutional Neural Networks (CNN)]] and [[Image Captioning]].
- **Rethinking ImageNet Pre-training.** He et al., "Rethinking ImageNet Pre-training", ICCV 2019, is the deck's "Evidence: object detection, ICCV 2019" (p. 209). The slide states:
  - "Training from scratch can work just as well as training from a pretrained ImageNet model for object detection"
  - "But it takes 2-3x as long to train."
  - "They also find that collecting more data is better than finetuning on a related task"
- **The plot.** Its title is "bbox AP: R50-FPN, GN". It compares "random init" with "w/ pre-train" (p. 209). My reading of the plot, not text on the slide: at the dashed line marked "typical fine-tuning schedule", the pretrained curve is ahead. With longer schedules, both curves reach about 41 bbox AP.

Synthesis: in this detection setting, ImageNet pretraining saves training time. It does not raise the final score.

## Related

- [[AlexNet]]
- [[VGGNet]]
- [[ResNet]]
- [[Convolutional Neural Networks (CNN)]]
- [[What Counts as Solved]]
- [[Transfer Learning]]: ImageNet is the usual source task
- [[Fine-Tuning]]
- [[Image Captioning]]

## Sources

- [[Block 4 Slides]], pp. 181-184, 199-201, 220-222, 228
- [[Block 7 Slides]], pp. 197-198, 206, 209
- [[F26-midterm-review-234p]], p. 143
