---
id: doc-e78e0j
type: topic
kind: concept
description: "Weight initialization sets the starting values of a network's weights: random starts break the symmetry between hidden units, and a scale such as small random numbers, Xavier (std = 1/sqrt(Din)), or He/Kaiming (std = sqrt(2/Din)) keeps activations and gradients usable across layers."
tags: [machine-learning/cs566-deeplearning]
aliases: [Initialization, Weight W Initialization, Xavier initialization, Glorot initialization, He initialization, Kaiming initialization, MSRA initialization, He scaling, Xavier scaling, Zero initialization, Small random number initialization, Hidden-unit symmetry, Symmetry breaking]
created: 2026-10-12T16:58:10
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Neural Network Training]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Neural Network Training]]

## Definition

Weight initialization is the choice of a network's starting weights. "Initialization sets the starting scale of weights" ([[Block 7 Slides]], p. 83). "Initialization gives optimization a usable starting point" (p. 62).

The slides list three options (p. 60, slide credit CS 231N):

- Small random numbers
- Xavier
- He / Kaiming: "ReLU-aware scale"

The midterm review repeats this list ([[F26-midterm-review-234p]], p. 114). It puts initialization among the choices that "shape how training behaves", together with normalization, regularization, and frozen layers (p. 112).

## Explanation

### Why the scale matters

The slide "Signals Must Survive Many Layers" says: "Before useful learning begins, check the scale of activations" (p. 62). It gives three cases:

| Scale | Effect (p. 62) |
|---|---|
| Too small | "Signals or gradients can shrink across depth." |
| Too large | "Signals or gradients can grow or saturate." |
| A suitable scale | "Xavier / He rules account for layer size and activation." |

"Good scaling can reduce shrinking or growing signals across layers" (p. 83). See [[Vanishing Gradient Problem]] and [[Exploding Gradient Problem]].

### Zero initialization and hidden-unit symmetry

The section opens with a convolution weight that maps X to Y and asks: "If all weights are 0?" (p. 57, slide credit CS 231N).

The slide "Why Identical Hidden Units Stay Identical" supposes "two hidden units start with exactly the same parameters" (p. 58):

- Same start: "Same inputs and parameters produce the same outputs."
- Same update: "Under symmetric connections, they receive the same gradients."
- "Different random starts let hidden units learn different features."

The midterm review repeats this slide ([[F26-midterm-review-234p]], p. 113) and states the rule in one line: "Identical starts keep symmetric hidden units identical under deterministic updates; random starts break symmetry" (p. 112).

The slide "Zero Initialization and Hidden-Unit Symmetry" considers "several hidden units with identical incoming and outgoing connections". "They can remain identical through subsequent updates" (p. 59). For other parameter roles: "Zero biases can be valid. LoRA also uses a zero factor with a nonzero random factor" (p. 59, citing Hu et al., LoRA, ICLR 2022). The slide concludes: "Initialization must account for the parameter's role" (p. 59).

A worked example: "Two identical hidden units receive equal gradients, so one SGD step keeps them doing the same computation" ([[F26-midterm-review-234p]], p. 115).

- Two hidden units compute $h = w x$ with $x = 2$ and $w_1 = w_2 = 0.4$, so $h_1 = h_2 = 0.8$.
- $dL/dh = 1$ for each unit, so $dL/dw = 2$ for each.
- SGD with rate 0.1: $0.4 - 0.1 \times 2 = 0.2$. Both weights become 0.2, and $h_1 = h_2 = 0.4$.
- A different start, $w_1 = 0.3$ and $w_2 = 0.7$, gives $h_1 = 0.6$ and $h_2 = 1.4$: "different computations".

Synthesis, not a slide statement: all-zero weights are one case of identical units. Every unit in the layer starts the same, so gradient descent cannot make them different. A zero bias does not cause this problem when the weights are random, because the random weights already make the units different.

General background, not from a course source: in the LoRA paper, $A$ starts as random Gaussian values and $B$ starts at zero. Thus $BA = 0$, and the adapted layer starts equal to the frozen layer (see [[LoRA]]). The slide does not say which factor is zero.

### The activation-statistics experiment

The slides use one experiment for each scheme (pp. 63-78, slide credit CS 231N). The experiment is a "Forward pass for a 6-layer net with hidden size 4096": `dims = [4096] * 7`, a batch of 16 random inputs `x = np.random.randn(16, dims[0])`, and one weight matrix `W` of shape `(Din, Dout)` for each layer (p. 63). The slides plot each layer's activations and print the mean and std.

| Scheme and activation | Pages | Std, layers 1-6 | Mean, layers 1-6 |
|---|---|---|---|
| Small random (0.01), tanh | 64-65 | 0.49, 0.29, 0.18, 0.11, 0.07, 0.05 | 0.00 at every layer |
| Xavier, tanh | 67 | 0.63, 0.49, 0.41, 0.36, 0.32, 0.30 | 0.00 at every layer |
| Xavier, ReLU | 77 | 0.58, 0.41, 0.30, 0.21, 0.15, 0.10 | 0.39, 0.28, 0.20, 0.14, 0.10, 0.07 |
| He / Kaiming, ReLU | 78 | 0.83, 0.83, 0.83, 0.81, 0.81, 0.81 | 0.57, 0.57, 0.56, 0.55, 0.55, 0.55 |

(The slides print the tanh means as 0.00 or -0.00.)

### Small random numbers

"Sample from a gaussian distribution with 0 mean and given standard deviation (such as 0.01)" (p. 61):

```python
W = 0.01 * np.random.randn(Din, Dout)
```

"A fixed scale such as 0.01 can shrink signals in a deep network" (p. 61). In the experiment with tanh, "All activations tend to zero for deeper network layers" (p. 65). The slide asks "What do the gradients dL/dW look like?" and answers: "Tiny gradients; slow updates" (p. 65).

### Xavier (Glorot) initialization

"Set the variance according to # of input neurons". "Intuition: balance signal scales across layers" (p. 66):

$$\mathrm{Var}(W) = \frac{1}{n_{in}}$$

```python
W = np.random.randn(Din, Dout) / np.sqrt(Din)   # std = 1/sqrt(Din)
```

With tanh, the slide calls the result "'Just right': Activations are nicely scaled for all layers!" (p. 67). "For conv layers, Din is filter_size² * input_channels" (p. 68; see [[Convolutional Layer]]). The slides cite Glorot and Bengio, "Understanding the difficulty of training deep feedforward neural networks", AISTAT 2010 (pp. 67-75; the slides spell the venue "AISTAT").

The derivation (pp. 69-75):

1. Let $y = x_1 w_1 + x_2 w_2 + \dots + x_{D_{in}} w_{D_{in}}$.
2. Assume $\mathrm{Var}(x_1) = \mathrm{Var}(x_2) = \dots = \mathrm{Var}(x_{D_{in}})$.
3. We want $\mathrm{Var}(y) = \mathrm{Var}(x_i)$.
4. $\mathrm{Var}(y) = D_{in}\,\mathrm{Var}(x_i w_i)$ if all $x_i, w_i$ are iid (p. 73).
5. $\mathrm{Var}(y) = D_{in}\,\mathrm{Var}(x_i)\,\mathrm{Var}(w_i)$ if all $x_i, w_i$ are also zero mean (p. 74).
6. "So, Var(y) = Var(x_i) only when Var(w_i) = 1/Din" (p. 75).

Xavier / Glorot "Balances input and output signal scales" and is "A common choice for tanh-like layers" (p. 82). For "Other feed-forward layers", "Xavier scaling can be appropriate" (p. 81).

With ReLU, Xavier scaling is not enough. "ReLU removes negative inputs, changing the signal scale." "Signal scale shrinks here" (p. 77). See the table above.

### He (Kaiming, MSRA) initialization

The "ReLU correction" doubles the variance (p. 78):

$$\text{std} = \sqrt{2 / D_{in}}$$

```python
W = np.random.randn(Din, Dout) * np.sqrt(2/Din)
```

With ReLU, the slide again calls the result "'Just right': Activations are nicely scaled for all layers!" (p. 78). It cites He et al., "Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification", ICCV 2015 (p. 78).

"ReLU removes negative activations, changing the signal's second moment" (p. 79). The slide draws the chain "Layer size" → "Activation-aware initial scale" → "A usable starting signal". "He scaling is a common starting point for ReLU layers" (p. 79). He / Kaiming "Accounts for ReLU removing negative values" and is "A common choice for ReLU layers" (p. 82).

The slides introduce Kaiming He as "MIT Professor" and "Author of ResNet (covered in this our CNN lecture), Faster R-CNN, and more" (p. 80). See [[ResNet]].

General background, not from a course source: if a pre-activation is symmetric about zero, ReLU keeps about half of its second moment. The factor 2 restores that half.

### Rules for choosing an initialization

The slides state these rules:

1. "Match initialization to the activation and architecture" (p. 55). The same slide chooses activations by layer role: ReLU-family for CNN / MLP hidden layers, GELU or gated SiLU for Transformer hidden layers, and sigmoid or tanh for outputs and gates (see [[Activation Functions]]).
2. "Initialization must account for the parameter's role" (p. 59). Weights need random starts that differ. Zero biases can be valid.
3. "Use the model or library initialization intended for that architecture" (p. 81):
   - ReLU-family layer: "He / Kaiming scaling is a common choice."
   - Other feed-forward layers: "Xavier scaling can be appropriate."
   - Pretrained backbone: "Start from its learned weights when transferring." See [[Transfer Learning]] and Pretrained Visual Encoders.
4. "Changing an activation may require changing initialization" (p. 81). "The activation affects the suitable weight scale" (p. 82). "Choose a starting scale that matches the layer width and activation" (p. 82).
5. "Before useful learning begins, check the scale of activations" (p. 62).

### Limits

The slide "Initialization Helps Gradient Flow" (p. 83) puts initialization next to two other factors:

- Architecture: "Depth, activations and residual paths also matter." See [[Residual Connections]] and [[Batch Normalization]].
- Training: "Inspect actual loss and gradient behavior."

"A suitable initialization helps without guaranteeing convergence" (p. 83).

### Open points in the slides

- Page 82 says Xavier "Balances input and output signal scales". But the formula and the derivation use only the number of inputs: $\mathrm{Var}(W) = 1/n_{in}$ (p. 66) and $\mathrm{Var}(w_i) = 1/D_{in}$ (p. 75). The slides give no form that uses the number of outputs.
- Pages 61 and 66 write $W \sim \mathcal{N}(\mu, \sigma^2)$, but the text and the code use mean 0.
- Page 75 labels the final step "[Assume all x_i, w_i are iid]". The step before it (p. 74) needs zero mean as well. The derivation uses both assumptions.
- With Xavier and tanh, the std still falls from 0.63 to 0.30 across six layers (p. 67), and the slide calls this "Just right". The slides do not say how much decay is acceptable.

## Related

- [[Activation Functions]]: the activation sets the suitable scale
- [[Vanishing Gradient Problem]]
- [[Exploding Gradient Problem]]
- [[Batch Normalization]]
- [[Residual Connections]]
- [[ResNet]]
- [[Convolutional Layer]]
- [[LoRA]]: starts one factor at zero
- [[Dying ReLU]]: a different failure in which ReLU units stop learning
- [[Transfer Learning]]
- Pretrained Visual Encoders
- [[Optimization]]
- [[Gradient Descent]]: the SGD step in the symmetry example

## Sources

- [[Block 7 Slides]], pp. 55, 57-83
- [[F26-midterm-review-234p]], pp. 112-115, the midterm review's recap of symmetry breaking and the initialization options
- The LoRA factor detail, the factor-2 explanation, and the syntheses are general background, not from a course source.
