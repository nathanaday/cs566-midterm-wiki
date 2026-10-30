---
description: "A deep learning architecture for images and video: convolutional and pooling layers extract feature maps, then a flatten step, fully connected layers, and softmax classify them."
aliases: [CNN, CNNs, ConvNet, Convolutional Neural Network, Components of CNNs, CNN Layer Types, CNN Applications]
sources: ["Topic Note - Convolutional Neural Networks (CNN)", "Lecture 3 Notes - Convolutional and Pooling Layers", "[[Block 3 Slides]]", "An Image is Worth 16x16 Words (note)", "FastVLM (note)", "Topic Note - Sequence Transduction", "Fall 2026 Reading List", "[[Block 4 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
---

> [!concept] Concept
> 10 sources · refreshed 2026-10-19 · #machine-learning
> Up: [[Neural Networks]] · Machine Learning

## Definition

A CNN is a classic deep learning architecture for computer vision, in use from about 1980 on (Topic Note - Convolutional Neural Networks (CNN)). The note describes the flow like this: the network can split an image into channels, and passes it through convolutional layers. At the end, a fully connected layer flattens the data and feeds an output layer, usually a classifier (Topic Note - Convolutional Neural Networks (CNN)).

[[Block 3 Slides]] introduces CNNs as the model "for images and videos". It asks: "For a 1024x1080 picture – how many features does it have?" Its diagram shows three stages of convolution + ReLU with pooling (feature extraction), then a flatten layer, a fully connected layer, and a softmax output that gives a probability distribution over classes (p. 270).

[[Block 4 Slides]] calls CNNs a type of feedforward network (p. 8). Its pipeline, from LeCun et al. 1998, is: input, convolutions, image maps, subsampling, and so on, then fully connected layers and the output (p. 14).

## Explanation

### Layers

The deck names four CNN layer types and frames each layer as a function ("Layer = Function") ([[Block 4 Slides]], pp. 46-47, 132, 149):

| Layer | What it does | Linear? |
|---|---|---|
| [[Convolutional Layer]] | slides learned filters over the input and stacks the activation maps | linear |
| [[Pooling Layer]] | downsamples each activation map; no parameters | max pooling is nonlinear |
| [[Fully Connected Layer]] | flattens the input and multiplies it by a weight matrix | linear |
| [[Softmax Layer]] | maps class scores to probabilities | nonlinear |

The linearity column is from Lecture 3 Notes - Convolutional and Pooling Layers and [[Block 4 Slides]], p. 152. Both say only two of the four layers are linear. [[F26-midterm-review-234p]] adds that a mean over fixed entries is linear, so average pooling is linear while max pooling is not (p. 77). See [[Pooling Layer]].

A later slide lists five components of a CNN: convolution layers, pooling layers, fully connected layers, the activation function, and normalization ([[Block 4 Slides]], p. 167). See [[Activation Functions]] and [[Batch Normalization]]. The deck then asks how to put these components together, which leads into CNN architectures (p. 178).

### Stacking convolutional layers

A ConvNet is a sequence of convolution layers with activation functions such as ReLU between them ([[Block 4 Slides]], pp. 84-86). Example: a 3x32x32 input passes through 6 filters of 5x5x3 to give 6x28x28, then 10 filters of 5x5x6 to give 10x24x24 (p. 85). The filter depth of each layer equals the channel count of its input (p. 85).

[[F26-midterm-review-234p]] states the rule behind the activation functions: "Stacking affine layers without a nonlinearity still gives one affine map" (p. 37). Synthesis: a convolutional layer with a bias is affine, so without the activation functions the stack would collapse to one affine map. See [[Activation Functions]].

### Shapes and parameter counts

[[F26-midterm-review-234p]] says: "Tracking shapes and counting parameters makes each forward layer concrete." Track tensor shapes through each layer, and separate trainable parameters from computed activations (p. 37). "In CNNs, channels and spatial positions play different roles in counting and in computation" (p. 37). The review's examples (pp. 69-74):

- The parameter count of a convolutional layer depends on kernel size, input channels, and filter count, not on the input's height and width. A larger input reuses the same parameters at more positions (p. 69). See [[Convolutional Layer]].
- The filter count sets the output channels. Kernel, stride, and padding set the output height and width (p. 74).
- A 1x1 Convolution mixes the channels at one position and reads no neighboring positions (p. 71).

Some source slides use row vectors $xW$. The review's new formulas use column vectors $Wx$, and the parameter counts are the same (p. 37).

### Image classification

Image classification maps a whole image to one label, for example a photo of a car to "Car" ([[Block 4 Slides]], p. 287). The deck's pipeline is Image, Conv, Pool, Conv, Pool, Conv, Conv, Conv, Pool, FC, FC, Softmax. Its diagram shows a 224x224x3 input, a first 11x11 convolution with stride 4, max pooling layers, two dense layers of 2048 units per branch, and a 1000-way output (p. 288).

Synthesis: this pipeline and diagram match [[AlexNet]].

### Applications

[[Block 4 Slides]] shows CNNs used for:

- image classification and image retrieval (Krizhevsky, Sutskever, and Hinton, 2012; p. 24)
- object detection with Faster R-CNN (Ren, He, Girshick, Sun, 2015) and semantic segmentation (Farabet et al., 2012; p. 25)
- game AI on Atari frames (Guo et al., 2014) and neural style transfer (Gatys et al., CVPR 2016 and 2017; p. 26)
- image captioning (Vinyals et al., 2015; Karpathy and Fei-Fei, 2015; p. 27)
- Inceptionism (DeepDream) images from Google Research, and style transfer images by Justin Johnson (p. 28)

Slide credit for pp. 26-28 goes to CS 231N. A later slide adds object segmentation, image resolution, human pose detection, and action classification (p. 286).

### Transfer learning with CNNs

[[Block 7 Slides]] says "Transfer learning with CNNs is pervasive… (it's the norm, not an exception)" (pp. 205-207). See [[Transfer Learning]]. Its examples:

- **Object detection with Fast R-CNN** (Girshick, "Fast R-CNN", ICCV 2015; p. 205). A ConvNet is "applied to entire image". An external proposal algorithm (for example, selective search) gives regions, and RoI pooling reads features for each region. FC layers feed a linear + softmax proposal classifier and linear bounding-box regressors. The loss is "Log loss + smooth L1 loss" (p. 205). The ConvNet is a "CNN pretrained on ImageNet" (p. 206).
- **Image captioning with CNN + RNN** (Karpathy and Fei-Fei, CVPR 2015; p. 205). The CNN is pretrained on ImageNet (p. 206), and the word vectors are "pretrained with word2vec" (p. 207). See Image Captioning.
- **Architecture matters.** "Object detection on MSCOCO" (Girshick, "The Generalized R-CNN Framework for Object Detection", ICCV 2017 Tutorial; p. 208):

| Detector (backbone) | Score |
|---|---|
| DPM (Pre DL) | 5 |
| Fast R-CNN (AlexNet) | 15 |
| Fast R-CNN (VGG-16) | 19 |
| Faster R-CNN (VGG-16) | 29 |
| Faster R-CNN (ResNet-50) | 36 |
| Faster R-CNN (ResNet-101) | 39 |
| Mask R-CNN FPN (ResNet-101) | 46 |

  The chart does not name the metric on its y-axis.
- **Pretraining against training from scratch.** He et al., "Rethinking ImageNet Pre-training" (ICCV 2019), finds that detection from scratch can match ImageNet pretraining but takes 2-3x as long to train (p. 209). See ImageNet Large Scale Visual Recognition Challenge for the details.

Synthesis: within one detector, a stronger pretrained backbone gives a higher score. The score goes from 15 to 19 for Fast R-CNN (AlexNet to VGG-16), and from 29 to 39 for Faster R-CNN (VGG-16 to ResNet-101).

### Architectures in the slides

[[Block 3 Slides]] shows two architectures with no discussion: [[AlexNet]] (Krizhevsky et al., "ImageNet Classification with Deep Convolutional Neural Networks", NIPS 2012; p. 31) and GoogLeNet (Szegedy et al., "Going deeper with convolutions", CVPR 2015; p. 32).

### Beyond image grids

The input structure sets what a network must model ([[Block 4 Slides]], p. 311):

- Images: local neighborhoods lie on a fixed grid.
- Sequences: past information must persist across ordered observations.
- Graphs: neighborhoods follow edges, not image coordinates.

The deck introduces RNNs for sequences and GNNs for graphs as the topics after CNNs (pp. 311-312). See [[Recurrent Neural Networks (RNN)]].

The three share one idea. A CNN uses the same kernel at every spatial position, an RNN the same update at every time step, and a GNN the same update at every node. "A larger compatible input repeats the rule with no new parameters" ([[F26-midterm-review-234p]], p. 233). See [[Convolutional Layer]] and [[Graph Neural Networks]].

### Why CNNs still matter

- **Built-in bias.** The ViT note says ViT matches or beats CNNs with enough pre-training data. This shows that the inductive bias of convolution helps at small scale but is optional at large scale (An Image is Worth 16x16 Words (note)). [[Block 4 Slides]] makes the same point: convolutional layers encode locality and weight sharing cheaply, but vision transformers match or beat them at large pretraining scale, so no layer type is best for all tasks (p. 131).
- **Back in edge encoders.** The FastVLM note says FastVLM uses FastViTHD, a hybrid convolution-transformer encoder that emits far fewer visual tokens at high resolution (FastVLM (note)). The reading list calls it a hybrid CNN-ViT encoder that cuts time-to-first-token (Fall 2026 Reading List, item 12).
- **Earlier sequence transduction.** Before the Transformer, sequence transduction required RNNs or CNNs (Topic Note - Sequence Transduction).

Synthesis: ViT drops convolution when data is plentiful, and FastVLM brings it back to reduce latency. The two answer different constraints (accuracy at scale versus time-to-first-token), so they do not contradict each other.

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
- Lecture 3 Notes - Convolutional and Pooling Layers, § Layer Summary
- [[Block 3 Slides]], pp. 31–32, 270
- [[Block 4 Slides]], pp. 8, 14, 24-28, 46-47, 84-86, 131-132, 149, 152, 167, 178, 286-288, 311-312
- An Image is Worth 16x16 Words (note)
- FastVLM (note)
- Fall 2026 Reading List, item 12
- Topic Note - Sequence Transduction
- [[Block 7 Slides]], pp. 205-209
- [[F26-midterm-review-234p]], pp. 37, 69-74, 77, 233
