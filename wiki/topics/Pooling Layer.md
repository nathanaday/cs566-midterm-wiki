---
description: A CNN layer with no learned parameters that downsamples each activation map on its own, most often by max pooling, so the width and height shrink and the depth stays the same.
aliases: [Pool Layer, Pooling, Max Pooling, Average Pooling, Global Average Pooling, GAP]
sources: ["[[Block 4 Slides]]", "Lecture 3 Notes - Convolutional and Pooling Layers", "[[F26-midterm-review-234p]]"]
subject: 4 Convolutional networks
---

## Definition

A pooling layer downsamples each activation map. It has no learnable parameters. 

Pooling **tolerates small local shifts** but guarantees neither equivariance (output tracks the shift) nor invariance (output erases the shift): a one-pixel shift into a 2x2, stride 2 max pool moved one output row and left the other in place.

**Global average pooling (GAP)** averages each map to one number, so the output is $1 \times 1 \times C$. ResNet puts GAP after its last conv layer, then a single FC 1000 layer

### Output Size

Hyperparameters: window size $F$ and stride $S$. Input $W_1 \times H_1 \times C$, output $W_2 \times H_2 \times C$.

**Output size.**

$$W_2 = \frac{W_1 - F}{S} + 1 \qquad H_2 = \frac{H_1 - F}{S} + 1$$

- Common setting: $F = 2$, $S = 2$, which halves width and height.
- Smaller maps mean fewer parameters in later layers, which helps against [[Overfitting and Underfitting]].

> [!tip]
> Depth never changes; one output slice per input slice.

### Max vs Average Pooling

| | Max pooling | Average pooling |
|---|---|---|
| Output per window | largest value | mean of the values |
| Linear | no | yes |
| Parameters | 0 | 0 |
| Backward pass | gradient to the argmax only | gradient split evenly, $1/F^2$ each |
| Typical use | most common choice | global average pooling before the classifier |
A linear map must satisfy $f(u + v) = f(u) + f(v)$. Max fails: with $u = (2, 0)$ and $v = (0, 3)$, $\max(u) + \max(v) = 5$ but $\max(u + v) = 3$. A mean over fixed entries passes, so average pooling is linear.


**Max pooling, 2x2 window, stride 2.**

$$\begin{bmatrix} 1 & 1 & 2 & 4 \\ 5 & 6 & 7 & 8 \\ 3 & 2 & 1 & 0 \\ 1 & 2 & 3 & 4 \end{bmatrix} \rightarrow \begin{bmatrix} 6 & 8 \\ 3 & 4 \end{bmatrix}$$

## Related

- [[Convolutional Neural Networks (CNN)]]
- [[Convolutional Layer]]
- [[Fully Connected Layer]]
- [[Overfitting and Underfitting]]
- [[Residual Connections]]

## Sources

- [[Block 4 Slides]]
- Lecture 3 Notes - Convolutional and Pooling Layers
- [[F26-midterm-review-234p]]
