---
description: "A deep learning architecture for images and video: convolutional and pooling layers extract feature maps, then a flatten step, fully connected layers, and softmax classify them."
aliases: [CNN, CNNs, ConvNet, Convolutional Neural Network, Components of CNNs, CNN Layer Types, CNN Applications]
sources: ["Topic Note - Convolutional Neural Networks (CNN)", "Lecture 3 Notes - Convolutional and Pooling Layers", "[[Block 3 Slides]]", "An Image is Worth 16x16 Words (note)", "FastVLM (note)", "Topic Note - Sequence Transduction", "Fall 2026 Reading List", "[[Block 4 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 4 Convolutional networks
---

## Definition

A CNN is a feedforward network for images and video. Convolution and pooling layers extract feature maps; a flatten step, fully connected layers, and a softmax then classify them. The pipeline dates to LeCun et al. 1998: input, convolutions, feature maps, subsampling, fully connected layers, output.

### Layer Types

Treat each layer as a function. Only two of the four are linear.

| Layer | What it does | Parameters? | Linear? |
|---|---|---|---|
| [[Convolutional Layer]] | slides learned filters over the input, stacks one activation map per filter | yes | yes (affine with bias) |
| [[Pooling Layer]] | downsamples each activation map, one depth slice at a time | no | max: no; average: yes |
| [[Fully Connected Layer]] | flattens the input and multiplies by a weight matrix | yes | yes |
| [[Softmax Layer]] | maps class scores to a probability distribution | no | no |

> [!warning] Exam trap
> Average pooling is a mean over fixed entries, so it is linear. Max pooling is not. "Pooling is nonlinear" is only true for max pooling.

Five named CNN components: convolution, pooling, fully connected layers, [[Activation Functions]], and normalization ([[Batch Normalization]]).

### Standard Architecture Pattern

$$\text{Input} \to [\text{Conv} \to \text{ReLU} \to (\text{Pool})] \times N \to \text{Flatten} \to [\text{FC} \to \text{ReLU}] \times M \to \text{FC} \to \text{Softmax}$$

- Feature extraction: repeated Conv + ReLU blocks, with pooling every block or two.
- Classification: flatten, one or more FC layers, softmax over the classes.
- Each conv filter has depth equal to the channel count of its input. Example: 3x32x32 input, 6 filters of 5x5x3 gives 6x28x28; then 10 filters of 5x5x6 gives 10x24x24.
- [[AlexNet]] follows this pattern: 224x224x3 input, 11x11 conv with stride 4, max pools, Conv Pool Conv Pool Conv Conv Conv Pool FC FC Softmax, 1000-way output.

> [!warning] Exam trap
> Stacking affine layers with no nonlinearity between them still gives one affine map. A conv layer with bias is affine, so a CNN without ReLU collapses to a single linear classifier no matter how deep it is.

### Shapes and Parameter Counts

Track the tensor shape through every layer, and keep trainable parameters separate from computed activations. Channels and spatial positions play different roles: the filter count sets the output channels, while kernel size, stride, and padding set the output height and width.

**Conv output size** (input $W_1 \times H_1 \times D_1$, $K$ filters of size $F$, stride $S$, padding $P$):

$$W_2 = \frac{W_1 - F + 2P}{S} + 1 \qquad H_2 = \frac{H_1 - F + 2P}{S} + 1 \qquad D_2 = K$$

**Conv parameter count:**

$$\text{params} = K \cdot (F \cdot F \cdot D_1 + 1)$$

**Pool output size** (no padding, no parameters):

$$W_2 = \frac{W_1 - F}{S} + 1 \qquad H_2 = \frac{H_1 - F}{S} + 1 \qquad D_2 = D_1$$

**FC parameter count** (flattened input of $n$ values, $m$ outputs):

$$\text{params} = m \cdot (n + 1)$$

| Quantity | Depends on | Does not depend on |
|---|---|---|
| conv parameters | $F$, $D_1$, $K$ | input height and width |
| conv output H and W | $F$, $S$, $P$, input H and W | $K$ |
| conv output depth | $K$ | everything else |
| FC parameters | flattened input size, output size | nothing else |

Worked example: 5 filters of 3x3 on a 3-channel input, stride 1, pad 1, applied to 32x32: output $32 \times 32 \times 5$, parameters $5 \cdot (3 \cdot 3 \cdot 3 + 1) = 140$. The same layer on a 64x64 input has the same 140 parameters.

> [!tip]
> A [[1x1 Convolution]] mixes channels at one position and reads no neighbors: output H and W are unchanged, parameters are $K \cdot (D_1 + 1)$. Row-vector ($xW$) and column-vector ($Wx$) conventions give the same parameter counts.

### Why Convolution

- Local connectivity: each output reads a small neighborhood, not the whole image, so parameters do not scale with image size.
- Weight sharing: the same kernel at every spatial position. A larger input repeats the rule with no new parameters.
- The same idea appears elsewhere: an RNN applies the same update at every time step, a GNN at every node. See [[Recurrent Neural Networks (RNN)]] and [[Graph Neural Networks]].
- This built-in bias helps at small data scale; at large pretraining scale, vision [[Transformers]] match or beat CNNs.

### Applications and Transfer Learning

| Task | Model or paper |
|---|---|
| image classification, retrieval | Krizhevsky, Sutskever, Hinton 2012 (AlexNet) |
| object detection | Fast R-CNN (Girshick 2015), Faster R-CNN (Ren et al. 2015) |
| semantic segmentation | Farabet et al. 2012 |
| image captioning | CNN + RNN (Vinyals et al. 2015; Karpathy and Fei-Fei 2015) |
| style transfer, DeepDream, Atari game AI | Gatys et al. 2016; Guo et al. 2014 |

Transfer learning with CNNs is the norm. Detectors and captioners start from a CNN pretrained on ImageNet and add task heads (for Fast R-CNN: RoI pooling, linear + softmax, box regressors). Within one detector, a stronger pretrained backbone scores higher (AlexNet < VGG-16 < ResNet-101). Training from scratch can match pretraining but takes 2 to 3 times as long. See [[Transfer Learning]].

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
- Lecture 3 Notes - Convolutional and Pooling Layers
- [[Block 3 Slides]]
- [[Block 4 Slides]]
- An Image is Worth 16x16 Words (note)
- FastVLM (note)
- Fall 2026 Reading List
- Topic Note - Sequence Transduction
- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
