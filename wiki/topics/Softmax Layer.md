---
description: The last layer of a classification network, which maps the raw class scores (logits) to a probability distribution with sigma(z)_i = e^{z_i} / sum_j e^{z_j}.
aliases: [Softmax, Softmax Function]
sources: ["[[Block 4 Slides]]", "Lecture 3 Notes - Convolutional and Pooling Layers"]
subject: 2 Neural networks
---

## Definition

The softmax layer maps the unnormalized output of a network (logits) to a probability distribution over the predicted output classes ([[Block 4 Slides]], p. 151; Lecture 3 Notes - Convolutional and Pooling Layers). For class $i$ of $K$ classes ([[Block 4 Slides]], p. 151):

$$\sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

Here $z$ is the vector of raw class scores and $\sigma(z)_i$ is the probability of class $i$.

## Explanation

- Softmax is implemented as a neural network layer just before the output layer. It must have the same number of nodes as the output layer ([[Block 4 Slides]], p. 150).
- In [[AlexNet]], the softmax follows the last [[Fully Connected Layer|FC layer]] and gives a probability for each class. The class with the top score is the prediction (pp. 43-44).
- The softmax layer is one of the four CNN layer types, with the convolutional, pool, and FC layers (p. 46).
- It is nonlinear (p. 152; Lecture 3 Notes - Convolutional and Pooling Layers). The slides also call it the loss layer, with a reference to Lecture 1 ([[Block 4 Slides]], p. 152).

Synthesis: softmax is the loss layer because its probabilities feed the cross-entropy loss. [[Loss Functions]] has a worked example: logits $(\ln 2, 0, 0)$ give probabilities $(0.5, 0.25, 0.25)$.

## Related

- [[Convolutional Neural Networks (CNN)]]
- [[Fully Connected Layer]]
- [[Loss Functions]]
- Autoregressive Language Modeling
- [[Linear Classification]]

## Sources

- [[Block 4 Slides]], pp. 43-46, 150-152
- Lecture 3 Notes - Convolutional and Pooling Layers, § Softmax Layer, § Layer Summary
