---
id: con-n38v95
type: topic
kind: concept
description: The subset of ML that makes multi-layer neural networks feasible; CSCI 566 describes it as non-linear, hierarchical, and often end-to-end, and traces it through three turning points from 1980 to 2012.
tags:
  - machine-learning/cs566-deeplearning
aliases:
  - DL
created: 2026-09-28T00:00:00
updated: 2026-10-19T18:32:33
refreshed: 2026-10-19T18:32:33
status: stable
sources:
  - "[[Block 1 Slides]]"
  - "[[Block 3 Slides]]"
  - "Lecture 1"
  - "CSCI 566 Syllabus"
  - "CSCI 566 Reading List"
  - "Block 8 Slides"
up:
  - "[[CS566-DeepLearning]]"
  - "[[Machine Learning]]"
---

> [!concept] Concept
> 6 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[CS566-DeepLearning]] · [[Machine Learning]]

## Definition

Deep learning is a "Subset of ML which make the computation of multi-layer neural network feasible". ML is in turn a subset of AI ([[Block 1 Slides]], p. 65).

Both sources name three properties and say later classes will explain them (Lecture 1, § Deep Learning; [[Block 1 Slides]], p. 66):

- Non-linear, which gives high capacity
- Hierarchical
- End-to-end learning (the slides say "(Often)")

## Explanation

### Why deep networks for function approximation

The slides use these properties to argue that deep networks are a good choice for $f$ when the goal is to approximate an unknown function $f^*$. "Given certain conditions, a deep neural net can approximate any f(x)" ([[Block 1 Slides]], pp. 226–228). [[Block 3 Slides]] repeats the argument (pp. 8–9). See [[Function Approximation]].

### Brain analogy

Deep learning "may be motivated by" the human brain. A figure credited to Simon Thorpe times visual processing from the retina (20–40 ms) to the finger muscle (180–260 ms) ([[Block 1 Slides]], p. 67; again in [[Block 3 Slides]], p. 17). The next slide limits the analogy: biological neurons have many types, dendrites compute non-linear functions, and synapses are complex dynamical systems. "These are good motivations, while the actual relationship is weak" ([[Block 3 Slides]], p. 18). See [[Neural Networks]].

### Classical ML vs. deep learning

[[Block 3 Slides]] (p. 11) draws two pipelines under the label "Better Representations":

- Classical ML: input → feature extraction by a person → classification → output.
- Deep learning: input → one network that does feature extraction and classification → output.

Synthesis: this is a picture of the "hierarchical" and "end-to-end" properties.

### Three turning points

| # | Turning point | Evidence on the slide | Citation |
| --- | --- | --- | --- |
| 1 | Hierarchical visual features | local features composed into a hierarchy; the idea predates 2012 | Fukushima, Neocognitron, Biological Cybernetics 1980 |
| 2 | Backprop trains a convolutional system | 1% error, about 9% reject rate on handwritten digits | LeCun et al., NeurIPS 1989 |
| 3 | Data and GPUs cross a threshold | 1.2M training images, 2 × GTX 580, 60M parameters; 15.3% vs. 26.2% top-5 error | Krizhevsky et al., NeurIPS 2012 ([[AlexNet]]) |

Source: [[Block 1 Slides]], pp. 69–71.

### Why non-linearity

A linear classifier cannot separate some point sets in $(x, y)$. After a feature transform such as $f(x,y) = (r(x,y), \theta(x,y))$, a linear classifier can separate them ([[Block 1 Slides]], p. 343). The slides show a linear model as one unit inside a multi-layer network (pp. 237, 347). See [[Linear Separability]].

A network gets its non-linearity from an [[Activation Functions|activation function]] such as ReLU, $\max(0, z)$. Without it, $f = W_2 \max(0, W_1 x)$ becomes $f = W_2 W_1 x = W_3 x$: "We end up with a linear classifier again!" ([[Block 3 Slides]], pp. 65–66).

### Place in the course

The CSCI 566 Syllabus gives deep learning most of the term:

- Week 3: neural network basics: perceptron, gradient descent, forward propagation
- Week 4: backpropagation, vanishing gradients, activation functions
- Week 5: convolutional neural networks
- Week 6: RNN and LSTM, graph neural networks
- Week 7: training dynamics, transfer learning
- Week 8: generative AI: GAN and VAE; see Generative Models and the Block 8 deck "Generative Models: GAN, VAE, and Beyond" (Block 8 Slides, p. 1)
- Week 9: attention, decoding, mixture of experts

The CSCI 566 Reading List names the *Deep Learning* textbook by Goodfellow.

The notes date CNNs to 1998 and say many meaningful changes in ML come from data and compute, not new core algorithms (Lecture 1, § Background Topics). The slides also list "ConvNet (1998)" among research milestones ([[Block 1 Slides]], p. 28), and they add two earlier turning points (1980 and 1989).

Synthesis: turning points 1 and 2 are ideas in architecture and training. Only turning point 3 is about data and hardware. After 2012, [[Scaling Laws]] made the effect of scale measurable.

## Related

- [[Neural Networks]]
- [[Machine Learning Task Types]]
- [[Function Approximation]]
- [[Linear Separability]]
- [[Activation Functions]]
- [[Backpropagation]]
- [[Convolutional Neural Networks (CNN)]]
- [[Scaling Laws]]
- [[Evolution of Machine Learning]]
- [[Autoregressive Language Modeling]]
- [[AlexNet]]

## Sources

- Lecture 1, § Deep Learning and § Background Topics
- [[Block 1 Slides]], pp. 28, 65–71, 226–228, 237, 343, 347
- [[Block 3 Slides]], pp. 8–11, 17–18, 65–66
- CSCI 566 Syllabus, schedule
- CSCI 566 Reading List
- Block 8 Slides, p. 1
