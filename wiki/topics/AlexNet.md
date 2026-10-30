---
id: ent-n5p03c
type: topic
kind: entity
description: The 8-layer convolutional network of Krizhevsky et al. that won ILSVRC 2012 as the first CNN-based winner, which CSCI 566 uses as the case study of methods, data, and compute coming together.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - Krizhevsky et al. 2012
  - ImageNet Classification with Deep Convolutional Neural Networks
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: contested
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
  - "Lecture 1"
  - "[[Block 4 Slides]]"
  - "[[Block 7 Slides]]"
up:
  - "[[Convolutional Neural Networks (CNN)]]"
  - "[[Deep Learning]]"
---

> [!entity] Contested · Entity
> 5 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Convolutional Neural Networks (CNN)]] · [[Deep Learning]]

## What it is

AlexNet is the convolutional network from Krizhevsky et al., "ImageNet Classification with Deep Convolutional Neural Networks", NeurIPS 2012 ([[Block 1 Slides]], pp. 40, 71; [[Block 4 Slides]], p. 29). Alex Krizhevsky designed it with Ilya Sutskever and Geoffrey Hinton ([[Block 4 Slides]], p. 22). It has 8 layers and won ILSVRC 2012. It was the first CNN-based winner of the challenge ([[Block 4 Slides]], p. 182; see [[ImageNet Large Scale Visual Recognition Challenge]]).

The sources give two top-5 error rates:

- [[Block 1 Slides]]: 15.3% top-5 error on ImageNet. The second-place entry had 26.2% (pp. 40, 71).
- [[Block 4 Slides]]: 16.4 top-5 error in the chart of ILSVRC winners (pp. 181-182).

The slides do not explain the difference. General background, not from a course source: the paper reports 16.4% for an average of five CNNs, and 15.3% when it adds two CNNs pretrained on extra ImageNet data.

## Facts

### Architecture

- **Layer stack.** 11x11 conv with 96 filters, pool, 5x5 conv 256, pool, 3x3 conv 384, 3x3 conv 384, 3x3 conv 256, pool, FC 4096, FC 4096, FC 1000, softmax ([[Block 4 Slides]], pp. 184, 199). Synthesis: five conv layers and three FC layers give the 8 layers.
- **Input and first layer.** The input is 224x224x3. The first layer uses 11x11 filters with stride 4 and gives 55x55 maps, 48 per stream. Later maps are 27x27 and 13x13, with 128 and 192 channels per stream ([[Block 4 Slides]], pp. 22, 29, 163).
- **Two streams.** The diagram splits the network into two parallel streams, with cross-connections at some layers. Each stream has two dense layers of 2048 units ([[Block 4 Slides]], pp. 22, 29, 41-42, 163). Synthesis: two streams of 48 maps and of 2048 units match the 96 filters and the FC 4096 layers on p. 184.
- **ReLU.** The detailed layer order is Image, Conv, Pool, ReLU, Conv, Pool, ReLU, Conv, ReLU, Conv, ReLU, Conv, Pool, ReLU, FC, ReLU, FC, ReLU, Softmax ([[Block 4 Slides]], p. 163). Architecture figures usually omit ReLU (pp. 164-165).
- **Output.** The last dense layer gives 1000 values. The softmax turns them into class probabilities, and the class with the highest probability is the prediction ([[Block 4 Slides]], pp. 43-44, 163). The deck shows top-5 labels for ImageNet images, such as mite, container ship, motor scooter, and leopard (pp. 24, 31).
- **Learned filters.** The first-layer filters show oriented edges and opposing colors. This slide gives 64 filters, each 3x11x11 ([[Block 4 Slides]], p. 89). [[Block 7 Slides]] gives the same shape, "64 x 3 x 11 x 11" (p. 195). The count differs from the 96 filters on [[Block 4 Slides]], p. 184. Neither deck explains the difference.

### Course framing

- **Three pillars.** The lecture uses AlexNet (2012) as a case study credited to CMU 15-884 by Tianqi Chen ([[Block 1 Slides]], p. 35):
  - Methods: SGD, dropout, ConvNet, initialization
  - Data: ImageNet, 1M labeled images
  - Compute: two GTX 580 GPUs, six days
- **Turning point 3.** A later slide gives 1.2M training images, 2 × GTX 580, and 60M parameters. It says "Architecture, ImageNet data, and efficient GPU convolution mattered together" and calls the result "threshold crossed" ([[Block 1 Slides]], p. 71). The two image counts (1M and 1.2M) differ; the slides do not explain the difference.
- **Systems view.** With today's frameworks (PyTorch, TensorFlow, MXNet) on data and compute, a researcher writes about 100 lines of Python and trains in a few hours ([[Block 1 Slides]], pp. 36–37).
- **A scoped claim.** "A strong result inherits the scope of its task, distribution, and metric." The AlexNet claim holds inside all three ([[Block 1 Slides]], p. 75).
- **Architecture diagram.** [[Block 3 Slides]] shows the AlexNet architecture as the example of a convolutional neural network (p. 31).
- **ReLU.** [[Block 3 Slides]] cites Krizhevsky et al., 2012 for ReLU: it "Reached 25% train error in ~1/6 the iterations of tanh (CIFAR-10)" (p. 258). See [[Activation Functions]].
- **Start of the current wave.** Lecture 1 say many people believe the momentum of the current AI wave started in 2012 with AlexNet (§ Background Topics).

### Transfer learning evidence

[[Block 7 Slides]] uses AlexNet in its "Transfer Learning with CNNs" slides (pp. 195-200). See [[Transfer Learning]].

- **First-layer filters.** The slide marks the first layer of the AlexNet diagram and shows its filters, "64 x 3 x 11 x 11", as a grid of edge, color, and texture patterns (p. 195).
- **Nearest neighbors in feature space.** The slide marks a late dense layer of the AlexNet diagram (2048 units per stream). It shows "L2 Nearest neighbors in feature space" for five test images: a flower, an elephant, a ship, a jack-o'-lantern, and a dog. Each row of neighbors shows the same kind of object as its test image (p. 196). Synthesis: the two streams of 2048 units form one 4096-wide FC layer. On CIFAR-10, neighbors by pixel distance often come from other classes (see [[k-Nearest Neighbors]]). Distance in the learned feature space finds images with the same content.
- **DeCAF.** pp. 197-200 cite Donahue et al., "DeCAF: A Deep Convolutional Activation Feature for Generic Visual Recognition", ICML 2014, and Razavian et al., "CNN Features Off-the-Shelf: An Astounding Baseline for Recognition", CVPR Workshops 2014. The chart on p. 199, from DeCAF, reports:

| Method | Score |
|---|---|
| DPD (Zhang et al., 2013) | 50.98 |
| POOF (Berg & Belhumeur, 2013) | 56.78 |
| AlexNet FC6 + logistic regression | 58.75 |
| AlexNet FC6 + DPD | 64.96 |

  The slide labels the two AlexNet bars "Finetuned from AlexNet" (p. 199). The chart does not name the metric or the dataset. The bar names (FC6 features with a classifier on top) and the "Finetuned" label do not clearly agree. The slide does not say which one applies.
- **The diagram is not AlexNet.** Synthesis: the network that pp. 197-200 draw (blocks of Conv-64, Conv-128, Conv-256, and Conv-512, then FC-4096, FC-4096, FC-1000) is VGG-style. The chart beside it reports AlexNet features.
- **Detection backbone.** On the MSCOCO object detection chart, Fast R-CNN scores 15 with AlexNet and 19 with VGG-16 (p. 208). See [[Convolutional Neural Networks (CNN)]].

### Before AlexNet

[[Block 4 Slides]] traces CNNs back to studies of the visual cortex:

- **Hubel and Wiesel (1959).** They recorded signals from the visual area of the brain with an electrode while they showed oriented bars and other stimuli. The goal was to learn how the system builds complex representations from simple stimulus features (p. 16).
- **Topographic mapping.** Nearby cells in the cortex represent nearby regions of the visual field. The layout of the retina maps directly to the layout of visual areas V1, V2, V3, hV4, and VO1 (p. 18).
- **Cell hierarchy.** Retinal ganglion cells feed LGN and V1 simple cells. Simple cells respond to light orientation. Complex cells respond to orientation and movement. Hypercomplex cells respond to movement with an end point (p. 19).
- **Brain inspiration.** The slide title says deep learning "may" be motivated by the human brain. It shows the visual pathway with timings, from the retina (20-40 ms) through V1 (edges, corners), V4 (feature groups), and AIT (80-100 ms; faces, objects) to a finger muscle (180-260 ms) (p. 20).
- **Neocognitron (Fukushima).** A "sandwich" architecture that alternates simple and complex cell layers. Simple cells have modifiable parameters; complex cells perform pooling. The slide labels it 1980 and cites a 1982 publication (p. 17).
- **LeNet (LeCun et al., NIPS 1989).** A handwritten digit recognizer. A 32x32 input goes through C1 (6@28x28), S2 (6@14x14), C3 (16@10x10), S4 (16@5x5), C5 (120 units), F6 (84 units), and an output of 10. It alternates convolution and subsampling, then uses full connections (p. 21).
- After AlexNet, the deck shows [[VGGNet]] (p. 23).

## Related

- [[Deep Learning]]: the third turning point
- [[Evolution of Machine Learning]]: first node of the capability track
- [[What Counts as Solved]]: example of a scoped claim
- [[ImageNet Large Scale Visual Recognition Challenge]]: the 2012 win
- [[VGGNet]]
- [[ResNet]]
- [[Convolutional Neural Networks (CNN)]]
- [[Activation Functions]]
- [[Transfer Learning]]: AlexNet features as the course example
- [[k-Nearest Neighbors]]: nearest neighbors by pixel distance, in contrast to feature space

## Sources

- [[Block 1 Slides]], pp. 35–37, 40, 71, 75
- [[Block 3 Slides]], pp. 31, 258
- Lecture 1, § Background Topics
- [[Block 4 Slides]], pp. 16-24, 29, 31, 41-44, 89, 163-165, 181-184, 199
- [[Block 7 Slides]], pp. 195-200, 208
- The explanation of 16.4% against 15.3% is general background with no course source.
