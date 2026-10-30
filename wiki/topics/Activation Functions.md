---
description: The non-linear function a neural network applies to each unit's weighted sum, such as sigmoid, tanh, ReLU, Leaky ReLU, PReLU, Maxout, ELU, or GELU, without which stacked layers collapse to one linear map.
aliases: [Activation Function, Nonlinearity, Nonlinear Activation, ReLU, Rectified Linear Unit, Sigmoid, Logistic Function, tanh, Leaky ReLU, PReLU, Parametric ReLU, Parametric Rectifier, ELU, Exponential Linear Unit, Maxout, Activation Saturation, Saturated Neurons]
sources: ["[[Block 3 Slides]]", "CSCI 566 Syllabus", "Sep 14 Lecture Account", "[[Block 4 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 2 Neural networks
---

## Definition

An activation function $f$ is a non-linear function that a neural network applies to each unit's weighted sum. A layer computes $h = f(Wx + b)$. The slides draw the analogy to a neuron: inputs $w_i x_i$ sum in the cell body, and $f(\sum_i w_i x_i + b)$ is the output on the axon ([[Block 3 Slides]], p. 239).

The slides' answer to "What is an activation function?": "a mathematical function applied to the output of a neuron or layer of neurons, transforming the input signal into an output signal. It's used for introducing non-linear properties to the network" (p. 88).

The [[F26-midterm-review-234p]] repeats the framing from Stanford CS 231n: in the 2-layer network $f = W_2 \max(0, W_1 x)$, "The function max(0, z) is called the activation function" (p. 43).

[[Block 7 Slides]] recaps the subject as "Activation Functions (Recap Note 3)" under "Training Neural Networks" (p. 42), and repeats the neuron figure with $f(\sum_i w_i x_i + b)$ on the output axon (p. 44).

The CSCI 566 Syllabus schedules activation functions in week 4 (Sep 21), with backpropagation and vanishing gradients.

## Explanation

### Why a network needs one

Without $f$, two layers collapse into one linear layer:

$$W_2(W_1 x + b_1) + b_2 = (W_2 W_1)x + (W_2 b_1 + b_2)$$

So a stack of linear layers still draws only a linear boundary. The slides make the same argument with $f = W_2 \max(0, W_1 x)$: without the max, "we end up with a linear classifier again!" ([[Block 3 Slides]], pp. 65-66). Without non-linearity "the neural network would essentially become a linear regression model, incapable of handling complex data patterns" (p. 88). See [[Neural Networks]], [[Deep Learning]], and [[Linear Separability]].

[[Block 4 Slides]] repeats the argument with three layers $F$, $G$, $H$: $Y = H(G(F(X)))$ becomes $Y = (HGF)(X)$. "Without nonlinear activation, multiple layers are reduced to one matrix multiplication" (p. 153). "Nonlinearity makes a neural network deeper and more expressive" (p. 154).

[[Block 7 Slides]] puts it briefly: "Two linear layers without a nonlinearity are still one linear map." "The activation lets stacked layers model nonlinear patterns" (p. 43).

The midterm review repeats the argument with the same collapse formula and the result "We end up with a linear classifier again!" ([[F26-midterm-review-234p]], pp. 42-44). [[Fundamentals of Deep Learning Nonlinear Activation]] works the argument step by step.

### Common functions

The slides list six functions ([[Block 3 Slides]], pp. 75, 240). [[Block 4 Slides]] shows the same six in its recap, with a figure from Stanford CS231n (pp. 155, 159, 161). [[Block 7 Slides]] shows them again (p. 45). The midterm review compares three of them: sigmoid, tanh, and ReLU ([[F26-midterm-review-234p]], pp. 49-50).

| Function | Formula | Output range | Derivative |
| --- | --- | --- | --- |
| Sigmoid | $\sigma(x) = \dfrac{1}{1 + e^{-x}}$ | $(0, 1)$ | $\sigma(x)(1 - \sigma(x))$, at most 0.25 |
| tanh | $\tanh(x)$ | $(-1, 1)$ | $1 - \tanh^2(x)$, at most 1 |
| ReLU | $\max(0, x)$ | $[0, \infty)$ | 1 if $x > 0$, 0 if $x < 0$ |
| Leaky ReLU | $\max(0.1x, x)$ | $(-\infty, \infty)$ | 0.1 if $x < 0$, 1 if $x > 0$ |
| Maxout | $\max(w_1^T x + b_1,\ w_2^T x + b_2)$ | depends on the weights | from the larger piece |
| ELU | $x$ if $x \geq 0$; $\alpha(e^x - 1)$ if $x < 0$ | $(-\alpha, \infty)$ | 1 if $x > 0$; $\alpha e^x$ if $x < 0$ |

The formulas are from the slides; the range and derivative columns are synthesis. The sigmoid derivative is on [[Block 3 Slides]], p. 243, and on [[Block 7 Slides]], p. 47. The slides give more than one slope for Leaky ReLU: $\max(0.1x, x)$ on [[Block 3 Slides]], pp. 75, 78, and 240, on [[Block 4 Slides]], pp. 155 and 161, and on [[Block 7 Slides]], p. 45; $\max(0.01x, x)$ on [[Block 3 Slides]], pp. 264-265, and on [[Block 7 Slides]], pp. 52-53; and the general form $\max(\alpha x, x)$ on [[Block 4 Slides]], p. 162. The ELU plot in [[Block 4 Slides]] levels off near $-2$ for negative inputs (pp. 161-162). [[Block 7 Slides]] splits ELU at $x \geq 0$ / $x < 0$ on p. 45, and at $x > 0$ / $x \leq 0$ on p. 54, with "Alpha default = 1". Synthesis: the two splits agree, because $\alpha(e^0 - 1) = 0$.

### Saturation

A unit saturates when its input falls in a flat region of the activation, where the local derivative is near 0. "The local derivative tells us how much gradient passes through this gate" ([[Block 7 Slides]], p. 48). For the sigmoid gate, $\partial L / \partial x = (\partial \sigma / \partial x)(\partial L / \partial \sigma)$, with $\partial \sigma(x) / \partial x = \sigma(x)(1 - \sigma(x))$ (p. 47). The deck's table (p. 48):

| Input $x$ | Sigmoid output | Local derivative |
| --- | --- | --- |
| −10 | ≈ 0.000045 | ≈ 0.000045 |
| 0 | 0.50 | 0.25 |
| 10 | ≈ 0.999955 | ≈ 0.000045 |

"Near saturation, very little gradient passes backward" (p. 48). "A saturated sigmoid passes a very small gradient, making upstream updates slow" (p. 49). The value agrees with "about 4.5e-5" on [[Block 3 Slides]], p. 249, and on [[F26-midterm-review-234p]], p. 100.

ReLU "does not saturate (in +region)" ([[Block 7 Slides]], p. 51). Leaky ReLU "does not saturate" (p. 52). ELU keeps a "negative saturation regime" (p. 54).

Synthesis: saturation is one cause of the [[Vanishing Gradient Problem]]. The sigmoid derivative is at most 0.25, so each sigmoid layer multiplies the backward gradient by at most 0.25. [[Dying ReLU]] is a related failure: a ReLU unit whose inputs are all negative passes no gradient.

### Sigmoid

Sigmoid "squashes numbers to range [0,1]" and was "historically popular since they have nice interpretation as a saturating 'firing rate' of a neuron" ([[Block 3 Slides]], p. 241; repeated in [[Block 7 Slides]], p. 46). It is "similar to step functions, but differentiable" ([[Block 4 Slides]], p. 157). Use it "in the output layer for binary classification tasks", when outputs must be probabilities ([[Block 3 Slides]], p. 76).

The midterm review gives the full slide. Sigmoid "squashes the input values into a range between 0 and 1. It's historically been used for binary classification." Use it "When you need probabilities as outputs, since its output can be interpreted as a probability." Its limitations: "Prone to vanishing gradient problem (discussed later). Outputs are not zero-centered" ([[F26-midterm-review-234p]], p. 49).

[[Block 3 Slides]] names three problems (pp. 242, 250, 257; [[Block 7 Slides]], p. 50):

1. **Saturated neurons shrink the gradients.** At $x = -10$, $\sigma(x) \approx 0$ and the local gradient is $0(1 - 0) = 0$. At $x = 10$ it is $1(1 - 1) = 0$ ([[Block 3 Slides]], pp. 244-248). "Then the gradients flowing back are tiny (about 4.5e-5 here) and the weights barely move" (p. 249). [[Block 4 Slides]] states it briefly: sigmoid is "easily saturated (no gradients)" (p. 157). Block 7 writes "Saturated neurons 'kill' the gradients" (p. 50). This is part of the [[Vanishing Gradient Problem]] ([[Block 3 Slides]], p. 76; [[Block 4 Slides]], p. 158). The midterm review repeats the sigmoid gate, with a plot of $\sigma(x)(1 - \sigma(x))$ that peaks at $x = 0$ and falls toward 0 for large $\lvert x \rvert$ ([[F26-midterm-review-234p]], pp. 98-100). See the Saturation section above.
2. **Outputs are not zero-centered.** If the input $x$ to a neuron is always positive, $\partial L / \partial w = \sigma(\sum_i w_i x_i + b)(1 - \sigma(\sum_i w_i x_i + b))\, x \times \text{upstream gradient}$. The local sigmoid gradient is always positive, so the sign of the gradient for all $w_i$ is the sign of the upstream gradient ([[Block 3 Slides]], pp. 251-255). All weights move in the same direction, and the path to the optimum zig-zags (p. 256).
3. **"exp() is a bit compute expensive"** (p. 257).

### tanh

tanh "is similar but outputs values between -1 and 1, making it zero-centered and thus, in some cases, more efficient than sigmoid" ([[Block 3 Slides]], p. 90). [[Block 7 Slides]] plots it from −1 to 1 (p. 45). The [[Batch Normalization]] example network in [[Block 4 Slides]] repeats the order FC, BN, tanh (p. 174). Synthesis: $\tanh(x) = 2\sigma(2x) - 1$, its maximum gradient is 1, and it still saturates for large $|x|$.

### ReLU

ReLU "outputs the input directly if positive, otherwise, it will output zero" ([[Block 3 Slides]], p. 77). From the slides:

- Use it "in most hidden layers, as it helps with the vanishing gradient problem and speeds up training. Good default choice for deep neural networks" (p. 77). "ReLU is a good default choice for most problems" (p. 75).
- It "does not saturate (in +region)", is "very computationally efficient", and "reached 25% train error in ~1/6 the iterations of tanh (CIFAR-10)" [Krizhevsky et al., 2012] (p. 258). [[Block 4 Slides]] lists the same points: it prevents gradient vanishing when $x > 0$, and it is computationally efficient. It adds that ReLU is "biologically plausible" (p. 160).
- [[Block 7 Slides]] repeats the first two points and states the speed result as "Converges much faster than sigmoid/tanh in practice (e.g. 6x)" [Krizhevsky et al., 2012] (p. 51). Block 3 compares ReLU with tanh only; Block 7 names both sigmoid and tanh.
- Its output is not zero-centered ([[Block 3 Slides]], p. 259), and its gradient is 0 for $x < 0$ (p. 260). [[Block 4 Slides]] puts it as: it still loses the gradient when $x < 0$ (p. 160).
- It "can suffer from 'dying ReLU' problem, where neurons can become inactive on all current training examples" ([[Block 3 Slides]], p. 77). See [[Dying ReLU]].
- The midterm review repeats the description, the advice on when to use it, and the dying ReLU limitation of [[Block 3 Slides]], p. 77 ([[F26-midterm-review-234p]], p. 50).
- "ReLU has no trainable parameters" ([[F26-midterm-review-234p]], p. 41). Synthesis: PReLU, below, adds one, $\alpha$.
- In the review's 2-2-1 example (see [[Forward Propagation]]), both pre-activations are positive, $z_1 = 1.5$ and $z_2 = 1$, so ReLU$' = 1$ and $\delta_i = \partial L / \partial z_i$ equals $\partial L / \partial h_i$: $\delta = (-2, +1)$ ([[F26-midterm-review-234p]], p. 91). A negative pre-activation, $z = -1.2$, gives $a = 0$ and $da/dz = 0$ (p. 97). See [[Dying ReLU]].

Synthesis: ReLU has no derivative at $x = 0$; implementations use 0 or 1 there. The slides note ReLU "is not differentiable at zero" ([[Block 3 Slides]], p. 80).

Why ReLU still learns with no negative response ([[Block 3 Slides]], pp. 262-263):

- **Sparse activation:** some neurons output 0. "Realizing a speedup from that sparsity requires kernels that exploit it; effects on regularization are empirical." See [[Activation Sparsity]].
- **Non-saturation** for positive inputs, unlike sigmoid or tanh.
- **Enhancement of positive features:** the learned weights can emphasize positive features.
- **Collaboration in multilayer networks:** many layers of ReLU units together can abstract features that one unit cannot.

**ReLU and initialization.** "ReLU removes negative inputs, changing the signal scale." With weights drawn as `np.random.randn(Din, Dout) / np.sqrt(Din)` in a six-layer ReLU network, the activations shrink layer by layer: the mean falls from 0.39 to 0.07 and the std from 0.58 to 0.10. "Signal scale shrinks here" ([[Block 7 Slides]], p. 77, credited to CS231n). Kaiming / MSRA initialization uses std $= \sqrt{2 / D_{in}}$. The activations then stay "nicely scaled for all layers" (p. 78, citing He et al., ICCV 2015). "He scaling is a common starting point for ReLU layers" (p. 79). Synthesis: the $1/\sqrt{D_{in}}$ scale on p. 77 is the Xavier scale. See [[Weight Initialization]].

### Leaky ReLU, PReLU, and ELU

From [[Block 3 Slides]], pp. 78, 264-266:

- **Leaky ReLU** [Maas et al., 2013] allows "a small, non-zero gradient when the unit is not active", to combat dying ReLU (p. 78). It "performs about the same as ReLU in the cited experiments" and is "less prone to 'dying'" (p. 264). "The performance gain over ReLU can be inconsistent" (p. 78).
- **PReLU** [He et al., 2015]: $f(x) = \max(\alpha x, x)$, with backprop into the parameter $\alpha$ (p. 265).
- **ELU** [Clevert et al., 2015]: non-saturating for $x > 0$, closer to zero-mean outputs, and a negative saturation regime that "adds some robustness to noise" compared with Leaky ReLU. Its computation requires exp() (p. 266).

[[Block 4 Slides]] shows Leaky ReLU as $\max(\alpha x, x)$ next to ELU on one slide (p. 162).

[[Block 7 Slides]] covers the same three (pp. 52-54):

- **Leaky ReLU**, $f(x) = \max(0.01x, x)$: it "does not saturate", is computationally efficient, and "A small negative slope preserves a local gradient path" (p. 52). The slide cites "[Mass et al., 2013]" and [He et al., 2015]; this topic writes Maas, as above.
- **Parametric Rectifier (PReLU)**, $f(x) = \max(\alpha x, x)$, with "backprop into α (parameter)". "Leaky fixes α; PReLU learns α." "Negative inputs pass a gradient" (p. 53).
- **Exponential Linear Units (ELU)** [Clevert et al., 2015]: $f(x) = x$ if $x > 0$, $\alpha(\exp(x) - 1)$ if $x \leq 0$, with "Alpha default = 1". It has "All benefits of ReLU" and "Closer to zero mean outputs". Its negative saturation regime "compared with Leaky ReLU adds some robustness to noise". "Computation requires exp()" (p. 54).

### Maxout

Maxout takes the larger of two linear functions of the input: $\max(w_1^T x + b_1,\ w_2^T x + b_2)$ ([[Block 3 Slides]], pp. 75, 240; [[Block 4 Slides]], pp. 155, 161; [[Block 7 Slides]], p. 45). Synthesis: ReLU is the special case $w_1 = 0$, $b_1 = 0$, so Maxout does not have a zero-gradient region. The cost is a second set of weights for each unit.

### In convolutional networks

[[Block 4 Slides]] names the activation function as one of five components of a CNN, with convolution layers, pooling layers, fully-connected layers, and normalization (pp. 167, 178). A ConvNet is "a sequence of Convolution Layers, interspersed with activation functions": each CONV layer is followed by a ReLU (p. 86, credited to CS231n). [[AlexNet]] applies ReLU after its conv and FC layers, but diagrams "typically omit ReLU for the visualization" (pp. 163-165). See [[Convolutional Neural Networks (CNN)]].

### GELU and transformers

BERT (Devlin et al., NAACL 2019) and GPT-3 (Brown et al., NeurIPS 2020) use GELU. ReLU has a hard cutoff on the negative side; GELU "is smooth everywhere and has a Gaussian CDF weighting of the input" ([[Block 3 Slides]], p. 80). Hendrycks and Gimpel (arXiv 2016) report gains on the tasks they tested, but "smoothness is not shown to be the cause" (p. 80). Neither BERT nor GPT-3 runs an ablation against ReLU (p. 81). GELU "has a soft threshold", so neurons "have a chance of recovering instead of being stuck at zero output" (p. 82). A 2024 paper argues for ReLU in LLMs again; see [[Activation Sparsity]].

[[Block 7 Slides]] names "GELU or gated SiLU variants" as common choices for Transformer hidden layers (p. 55). The deck does not define SiLU. [[Activation Sparsity]] records that Llama 7B uses SiLU.

### Practice

"Use ReLU. Be careful with your learning rates. Try out Leaky ReLU / Maxout / ELU to squeeze out some marginal gains. Don't default to sigmoid or tanh in hidden layers" ([[Block 3 Slides]], p. 267).

[[Block 7 Slides]] makes the choice depend on the layer: "Choose an activation that fits the role of the layer" (p. 55).

| Layer | Common choice (p. 55) |
| --- | --- |
| CNN / MLP hidden layers | "ReLU-family activations are common starting points." |
| Transformer hidden layers | "GELU or gated SiLU variants are common choices." |
| Outputs and gates | "Sigmoid or tanh can still have specific roles." |

"Compare activation choices using validation results" (p. 52). "Match initialization to the activation and architecture" (p. 55); see [[Weight Initialization]]. Synthesis: this agrees with Block 3. ReLU is the default for hidden layers, and sigmoid or tanh stay at outputs and gates.

The Sep 14 lecture named appropriate activation functions, with batch normalization, as the two fixes for the vanishing gradient problem (Sep 14 Lecture Account, § Vanishing gradients). The slides list the same two fixes on p. 232.

The slides pose interview questions (pp. 87-92, 268-269):

- What an activation function is, and a comparison of sigmoid, tanh, and ReLU (pp. 87-90).
- The dying ReLU problem and its fix (pp. 91-92). See [[Dying ReLU]].
- What limits gradient-based training? The [[Vanishing Gradient Problem]], the [[Exploding Gradient Problem]], dependence on data and initialization, non-convex optimization, and the compute cost of backpropagation for large networks (pp. 268-269).

Synthesis: the saturation of sigmoid and tanh connects to vanishing gradients. ReLU keeps a gradient of 1 for positive inputs, which is one reason it is a good default. Sigmoid is still common as the output of a binary classifier.

## Related

- [[Neural Networks]]
- [[Fundamentals of Deep Learning Nonlinear Activation]]
- [[Deep Learning]]
- [[Linear Separability]]
- [[Perceptron]]: uses the step function $\text{sign}$
- [[Backpropagation]]: the sigmoid derivative in a worked example
- [[Forward Propagation]]: the 2-2-1 ReLU example
- Computational Graphs
- [[Gradient Descent]]
- [[Dying ReLU]]
- [[Activation Sparsity]]
- [[Batch Normalization]]
- [[Weight Initialization]]: He scaling for ReLU layers
- [[Vanishing Gradient Problem]]
- [[Exploding Gradient Problem]]
- [[Convolutional Neural Networks (CNN)]]
- [[AlexNet]]
- [[Transformers]]

## Sources

- [[Block 3 Slides]], pp. 65-66, 75-92, 232, 239-269
- [[Block 4 Slides]], pp. 86, 153-165, 167, 174, 178. The recap figures are credited to Stanford CS231n.
- CSCI 566 Syllabus, schedule, week 4
- Sep 14 Lecture Account, § Vanishing gradients
- [[Block 7 Slides]], pp. 42-55, 77-79
- [[F26-midterm-review-234p]], pp. 41-44, 49-50, 91, 97-100
