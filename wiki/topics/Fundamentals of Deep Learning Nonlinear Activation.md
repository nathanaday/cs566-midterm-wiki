---
description: "Why a neural network needs a nonlinear activation, built up from one neuron: stacked linear layers collapse to one ax + b, and each ReLU neuron adds one bend whose place its bias sets and whose size its outgoing weight sets."
aliases: [Why nonlinear activation, Nonlinear Activation Fundamentals, ReLU bends, Stacked Affine Layers Collapse, Need for Nonlinearity]
sources: ["Nonlinear activation from a Socratic session", "[[F26-midterm-review-234p]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Activation Functions]]

## Definition

A nonlinear activation is the step between layers that is not "multiply and add." Without it, any number of layers simplifies to one linear function. With it, each neuron can put a bend in the function the network computes (Nonlinear activation from a Socratic session). [[Activation Functions]] lists the common choices.

## Explanation

### One neuron

A neuron has one weight for each input, plus one bias $b$. It computes a dot product and adds the bias:

$$z = w \cdot x + b$$

Example: $x = [2, -1, 3]$ and $w = [0.5, 1, -1]$ give $w \cdot x = 1 - 1 - 3 = -3$. One neuron gives one number.

### One layer is a matrix and a bias vector

In a [[Fully Connected Layer]], every neuron sees the full input vector. Each neuron has its own weights and its own bias. Stack the weight vectors as rows to get $W$, and the biases to get $b$. For 3 inputs and 4 neurons:

| Part | Shape | Meaning |
| --- | --- | --- |
| $W$ | $[4, 3]$ | one row for each neuron (out by in) |
| $b$ | $[4]$ | one bias for each neuron |
| $z = Wx + b$ | $[4]$ | one output for each neuron |

Neuron $i$ is row $i$ of $W$ with entry $i$ of $b$. The "set of nodes" picture and the "matrix plus bias vector" picture are the same thing. PyTorch `nn.Linear(3, 4)` stores its weight as $[4, 3]$ and computes `x @ W.T + b` for a row vector `x`.

### Stacked linear layers collapse

Layer 2 takes the output of layer 1 as its input. The layers are chained, not added:

$$z_1 = 3x + 1, \qquad z_2 = 2z_1 + 5 = 2(3x + 1) + 5 = 6x + 7$$

The result has the form $ax + b$, the same form as one layer. Each layer substitutes a degree-1 expression into another, so the degree never rises above 1. A stack of 100 linear layers still simplifies to one $ax + b$. With matrices:

$$W_2(W_1 x + b_1) + b_2 = (W_2 W_1)x + (W_2 b_1 + b_2)$$

Without a nonlinear step, depth adds nothing. This is the same limit that [[Linear Separability]] shows for classifiers.

The CSCI 566 midterm review states the same result: "Without a nonlinearity between them, two affine layers are equivalent to a single affine layer." From $h = W_1 x + b_1$ and $y = W_2 h + b_2$, it gets $y = (W_2 W_1)x + (W_2 b_1 + b_2)$. "The combined weight is W2W1 and the combined bias is W2b1 + b2." Its scalar example: $h = 3x + 2$ and $y = 2h - 1$ give $y = 6x + 3$ ([[F26-midterm-review-234p]], p. 42).

The review then applies the result to a 2-layer network with no biases. Without the activation, $f = W_2 \max(0, W_1 x)$ becomes $f = W_2 W_1 x$. With $W_3 = W_2 W_1 \in \mathbb{R}^{C \times H}$, this is $f = W_3 x$: "We end up with a linear classifier again!" "Neural networks need this non linearity!!" (p. 44, credited to Stanford CS 231n).

### Linear and nonlinear

- **Linear:** the output has the form $ax + b$. The plot is a straight line, or a flat plane for many inputs. A change in $x$ gives the same change in output everywhere.
- **Nonlinear:** any other function. The plot curves or bends at some point.

Mathematicians call $ax + b$ *affine* and keep *linear* for $ax$. Machine learning uses *linear* for both. The midterm review uses *affine* for $Wx + b$: "Stacking affine layers without a nonlinearity still gives one affine map" ([[F26-midterm-review-234p]], p. 37).

Any nonlinear step between layers stops the collapse; a polynomial would also work. The common choice is ReLU:

$$\text{ReLU}(z) = \max(0, z)$$

It sets negative values to 0 and passes positive values unchanged: two straight pieces with one bend at 0.

### Worked example: two ReLU neurons

One hidden layer with 2 neurons, then a linear output:

$$h_1 = \text{ReLU}(x), \quad h_2 = \text{ReLU}(x - 1), \quad y = h_1 - 2h_2$$

| $x$ | $h_1$ | $h_2$ | $y$ |
| --- | --- | --- | --- |
| −1 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 0 |
| 3 | 3 | 2 | −1 |

| Segment | −1→0 | 0→1 | 1→2 | 2→3 |
| --- | --- | --- | --- | --- |
| Slope | 0 | +1 | −1 | −1 |

The slope changes at $x = 0$ and at $x = 1$. The plot is flat, then rises, then falls. No $ax + b$ makes this shape.

- $h_1$ makes the bend at $x = 0$. $h_2$ makes the bend at $x = 1$.
- The $-1$ inside $h_2$ is its bias. It puts the bend at $x = 1$. $\text{ReLU}(x - 5)$ bends at $x = 5$.
- At $x = 1$ the slope changes from $+1$ to $-1$, a change of $-2$. That is the output weight on $h_2$.

### The picture of one layer

- Each ReLU neuron adds **one bend**.
- Its **bias** decides **where** the bend is.
- The **weight after it** decides **how much the slope changes** at that bend.
- More neurons give more bends. With enough bends, the network can follow almost any curve. This result is the **universal approximation theorem**. See [[Function Approximation]].

Without the activation function, every bend disappears and the network is one $ax + b$ again.

### Next: who picks the numbers

In a real network, nobody sets the biases and weights by hand. The network starts with random values and fits data. [[Gradient Descent]] finds the values.

## Related

- [[Activation Functions]]
- [[Linear Separability]]
- [[Fully Connected Layer]]
- [[Neural Networks]]
- [[Forward Propagation]]
- [[Function Approximation]]
- [[Gradient Descent]]

## Sources

- Nonlinear activation from a Socratic session
- [[F26-midterm-review-234p]], pp. 37, 42, 44
