---
id: con-2zny14
type: topic
kind: concept
description: A layer that flattens its input to a vector and multiplies it by a learned weight matrix, so every output connects to every input; CNNs use it near the output because it costs too many parameters on raw images.
tags: [machine-learning/cs566-deeplearning]
aliases: [FC Layer, FC, Dense Layer]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 4 Slides]]", "Lecture 3 Notes - Convolutional and Pooling Layers"]
up: ["[[Convolutional Neural Networks (CNN)]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Convolutional Neural Networks (CNN)]]

## Definition

A fully connected (FC) layer maps an $M \times N \times P$ input to a $Q \times 1$ output ([[Block 4 Slides]], p. 50). It stretches the input into a vector $x$ of size $(M \cdot N \cdot P) \times 1$ (p. 51). The output is $Wx$, where $W$ is a $Q \times (M \cdot N \cdot P)$ matrix (pp. 52-53). The layer learns $W$ (p. 54).

The name comes from the connections: each hidden unit connects to every input pixel (pp. 55-56), and every neuron connects to every neuron in the previous layer (p. 128).

## Explanation

### Cost on images

A 200x200 image with 40k hidden units needs about 2B parameters in an FC layer ([[Block 4 Slides]], pp. 57-61). So many parameters waste resources, and there are not enough training samples to learn them (pp. 60-61). Spatial correlation in images is local, so full connectivity is not necessary (p. 61; slide credit Marc'Aurelio Ranzato). The notes make the same point: FC layers are not parameter efficient, and convolutional layers use parameters better (Lecture 3 Notes - Convolutional and Pooling Layers).

Flattening also destroys the spatial structure of the image. The deck's example is a 2-layer network, $f = W_2 \max(0, W_1 x)$: a 32x32x3 image becomes a 3072-dim input $x$, then a 100-unit hidden layer, then 10 class scores ([[Block 4 Slides]], p. 62).

See [[Convolutional Layer]] for how the deck moves from FC to locally connected to convolutional layers.

### Where it fits

- FC layers are often used toward the end of a network, to make decisions from features that earlier layers extract ([[Block 4 Slides]], p. 128).
- They are parameter-heavy and do not account for spatial hierarchy, which makes them less suitable for image recognition (p. 128).
- They can be effective for tasks that need a holistic view, where spatial relationships matter less, especially in the output layer (p. 131).
- In [[AlexNet]], a [[Softmax Layer|softmax]] follows the last FC layer (pp. 43-44). ResNet has only one FC layer, FC 1000, after global average pooling (p. 214).

The FC layer is linear ([[Block 4 Slides]], p. 152; Lecture 3 Notes - Convolutional and Pooling Layers).

A network built only from FC layers and activation functions is a fully connected network or MLP; see [[Neural Networks]].

## Related

- [[Neural Networks]]
- [[Convolutional Layer]]
- [[Convolutional Neural Networks (CNN)]]
- [[Softmax Layer]]
- [[Linear Classification]]

## Sources

- [[Block 4 Slides]], pp. 43-44, 50-62, 128, 131, 152, 214
- Lecture 3 Notes - Convolutional and Pooling Layers, § Convolutional Layer, § Layer Summary
