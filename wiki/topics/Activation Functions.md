---
description: The non-linear function a neural network applies to each unit's weighted sum, such as sigmoid, tanh, ReLU, Leaky ReLU, PReLU, Maxout, ELU, or GELU, without which stacked layers collapse to one linear map.
aliases: [Activation Function, Nonlinearity, Nonlinear Activation, ReLU, Rectified Linear Unit, Sigmoid, Logistic Function, tanh, Leaky ReLU, PReLU, Parametric ReLU, Parametric Rectifier, ELU, Exponential Linear Unit, Maxout, Activation Saturation, Saturated Neurons]
sources: ["[[Block 3 Slides]]", "CSCI 566 Syllabus", "Sep 14 Lecture Account", "[[Block 4 Slides]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 2 Neural networks
---

## Definition

A layer computes $h = f(Wx + b)$. 
- inputs $w_i x_i$ sum in the cell body
- $f(\sum_i w_i x_i + b)$ is the output on the axon ([[Block 3 Slides]], p. 239).

## Explanation

### Why a network needs one

Without $f$, two layers collapse into one linear layer:

$$W_2(W_1 x + b_1) + b_2 = (W_2 W_1)x + (W_2 b_1 + b_2)$$

So a stack of linear layers still draws only a linear boundary. Without non-linearity "the neural network would essentially become a linear regression model, incapable of handling complex data patterns"

$Y = H(G(F(X)))$ becomes $Y = (HGF)(X)$. 

"Without nonlinear activation, multiple layers are reduced to one matrix multiplication" (p. 153). "Nonlinearity makes a neural network deeper and more expressive" (p. 154).

### Common functions


![[graph.png]]


![[a6c898f4-42b7-4f81-a3ff-b46cf0a50e3e_Frame+1000001937.png.avif]]


| Function | Formula | Output range | Derivative |
| --- | --- | --- | --- |
| Sigmoid | $\sigma(x) = \dfrac{1}{1 + e^{-x}}$ | $(0, 1)$ | $\sigma(x)(1 - \sigma(x))$, at most 0.25 |
| tanh | $\tanh(x)$ | $(-1, 1)$ | $1 - \tanh^2(x)$, at most 1 |
| ReLU | $\max(0, x)$ | $[0, \infty)$ | 1 if $x > 0$, 0 if $x < 0$ |
| Leaky ReLU | $\max(0.1x, x)$ | $(-\infty, \infty)$ | 0.1 if $x < 0$, 1 if $x > 0$ |
| Maxout | $\max(w_1^T x + b_1,\ w_2^T x + b_2)$ | depends on the weights | from the larger piece |
| ELU | $x$ if $x \geq 0$; $\alpha(e^x - 1)$ if $x < 0$ | $(-\alpha, \infty)$ | 1 if $x > 0$; $\alpha e^x$ if $x < 0$ |

### Saturation

A unit saturates when its input falls in a flat region of the activation, where the local derivative is near 0. "The local derivative tells us how much gradient passes through this gate" 

| Input $x$ | Sigmoid output | Local derivative |
| --- | --- | --- |
| −10 | ≈ 0.000045 | ≈ 0.000045 |
| 0 | 0.50 | 0.25 |
| 10 | ≈ 0.999955 | ≈ 0.000045 |

"Near saturation, very little gradient passes backward" (p. 48). "A saturated sigmoid passes a very small gradient, making upstream updates slow" (p. 49). 

Synthesis: saturation is one cause of the [[Vanishing Gradient Problem]]. The sigmoid derivative is at most 0.25, so each sigmoid layer multiplies the backward gradient by at most 0.25. [[Dying ReLU]] is a related failure: a ReLU unit whose inputs are all negative passes no gradient.

### Sigmoid

- "squashes numbers to range (0,1)"
- "similar to step functions, but differentiable"
- Use it "in the output layer for binary classification tasks", when outputs must be probabilities

**Problems**

1. **Saturated neurons shrink the gradients.*
2. **Outputs are not zero-centered.** If the input $x$ to a neuron is always positive, $\partial L / \partial w = \sigma(\sum_i w_i x_i + b)(1 - \sigma(\sum_i w_i x_i + b))\, x \times \text{upstream gradient}$. The local sigmoid gradient is always positive, so the sign of the gradient for all $w_i$ is the sign of the upstream gradient ([[Block 3 Slides]], pp. 251-255). All weights move in the same direction, and the path to the optimum zig-zags (p. 256).
3. **"exp() is a bit compute expensive"** (p. 257).

### tanh

- tanh "is similar but outputs values between -1 and 1, making it zero-centered and thus, in some cases, more efficient than sigmoid" 
- $\tanh(x) = 2\sigma(2x) - 1$, its maximum gradient is 1, and it still saturates for large $|x|$.

### ReLU

- ReLU "outputs the input directly if positive, otherwise, it will output zero"
- Use it "in most hidden layers, as it helps with the vanishing gradient problem and speeds up training. Good default choice for deep neural networks" (p. 77)
- It "does not saturate (in +region)", is "very computationally efficient"
- "Converges much faster than sigmoid/tanh in practice (e.g. 6x)" 
- Its output is not zero-centered;  it still loses the gradient when $x < 0$ 
- It "can suffer from 'dying ReLU' problem, where neurons can become inactive on all current training examples" 
- "ReLU has no trainable parameters" Synthesis: PReLU, below, adds one, $\alpha$.

Why ReLU still learns with no negative response:

- **Sparse activation:** some neurons output 0. "Realizing a speedup from that sparsity requires kernels that exploit it; effects on regularization are empirical." See [[Activation Sparsity]].
- **Non-saturation** for positive inputs, unlike sigmoid or tanh.
- **Enhancement of positive features:** the learned weights can emphasize positive features.
- **Collaboration in multilayer networks:** many layers of ReLU units together can abstract features that one unit cannot.

### Leaky ReLU, PReLU, and ELU

- **Leaky ReLU** allows "a small, non-zero gradient when the unit is not active", to combat dying ReLU (p. 78). It "performs about the same as ReLU in the cited experiments" and is "less prone to 'dying'" (p. 264). "The performance gain over ReLU can be inconsistent" (p. 78).
- **PReLU**: $f(x) = \max(\alpha x, x)$, with backprop into the parameter $\alpha$ (p. 265).
- **ELU**: non-saturating for $x > 0$, closer to zero-mean outputs, and a negative saturation regime that "adds some robustness to noise" compared with Leaky ReLU. Its computation requires exp() (p. 266).

### Maxout

- Maxout takes the larger of two linear functions of the input: $\max(w_1^T x + b_1,\ w_2^T x + b_2)$  
- Synthesis: ReLU is the special case $w_1 = 0$, $b_1 = 0$, so Maxout does not have a zero-gradient region. The cost is a second set of weights for each unit.


### GELU and transformers

- BERT (Devlin et al., NAACL 2019) and GPT-3 (Brown et al., NeurIPS 2020) use GELU; GELU "is smooth everywhere and has a Gaussian CDF weighting of the input" 
- GELU "has a soft threshold", so neurons "have a chance of recovering instead of being stuck at zero output" (p. 82). A 2024 paper argues for ReLU in LLMs again; see [[Activation Sparsity]].

### Practice

"Use ReLU. Be careful with your learning rates. Try out Leaky ReLU / Maxout / ELU to squeeze out some marginal gains. Don't default to sigmoid or tanh in hidden layers" ([[Block 3 Slides]], p. 267).

| Layer | Common choice (p. 55) |
| --- | --- |
| CNN / MLP hidden layers | "ReLU-family activations are common starting points." |
| Transformer hidden layers | "GELU or gated SiLU variants are common choices." |
| Outputs and gates | "Sigmoid or tanh can still have specific roles." |


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
