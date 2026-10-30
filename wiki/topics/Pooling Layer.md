---
description: A CNN layer with no learned parameters that downsamples each activation map on its own, most often by max pooling, so the width and height shrink and the depth stays the same.
aliases: [Pool Layer, Pooling, Max Pooling, Max Pool, Average Pooling, Mean Pooling, L2-norm Pooling, Global Average Pooling, GAP]
sources: ["[[Block 4 Slides]]", "Lecture 3 Notes - Convolutional and Pooling Layers", "[[F26-midterm-review-234p]]"]
---

## Definition

A pooling layer makes representations smaller and easier to manage. It operates on each activation map independently ([[Block 4 Slides]], p. 133; Lecture 3 Notes - Convolutional and Pooling Layers). It maps an $M \times N \times P$ input to an $m \times n \times P$ output, so only the spatial size shrinks ([[Block 4 Slides]], pp. 138, 141). Example: a 224x224x64 volume becomes 112x112x64 (p. 133).

## Explanation

### Types

- **Max pooling** takes the maximum of each window. It is the most common type ([[Block 4 Slides]], p. 145).
- **Average (mean) pooling** takes the average of each window (p. 145; Lecture 3 Notes - Convolutional and Pooling Layers).
- **L2-norm pooling** is a third type ([[Block 4 Slides]], p. 145). The lecture did not go into detail (Lecture 3 Notes - Convolutional and Pooling Layers).

To choose a type, find a representation of a region that works for the task; max and mean are common choices (Lecture 3 Notes - Convolutional and Pooling Layers).

### Max pooling

Max pooling with 2x2 filters and stride 2 on one 4x4 depth slice ([[Block 4 Slides]], p. 134; [[F26-midterm-review-234p]], p. 75):

$$\begin{bmatrix} 1 & 1 & 2 & 4 \\ 5 & 6 & 7 & 8 \\ 3 & 2 & 1 & 0 \\ 1 & 2 & 3 & 4 \end{bmatrix} \rightarrow \begin{bmatrix} 6 & 8 \\ 3 & 4 \end{bmatrix}$$

A 3x3 max pool with stride 2 on a 5x5 input gives the 2x2 output `[8, 7]`, `[8, 9]` ([[Block 4 Slides]], pp. 138-143). Each input depth slice gives one output slice (p. 144).

Max pooling has no learnable parameters and gives some invariance to small shifts (p. 135; [[F26-midterm-review-234p]], p. 76). It is nonlinear ([[Block 4 Slides]], p. 152; Lecture 3 Notes - Convolutional and Pooling Layers). It still loses information, because it is a form of compression (Lecture 3 Notes - Convolutional and Pooling Layers).

### Linearity

"Additivity is a necessary test of linearity: a linear map must pass it" ([[F26-midterm-review-234p]], p. 77). Linearity requires $f(u + v) = f(u) + f(v)$. Max pooling fails the test (p. 77):

- u = (2, 0) and v = (0, 3).
- max(u) + max(v) = 2 + 3 = 5.
- max(u + v) = max(2, 3) = 3.

"A mean over fixed entries is linear, and neither max nor mean pooling has trainable parameters" (p. 77).

Synthesis: the linearity of a pooling layer depends on its type. The "nonlinear" label for pooling in [[Convolutional Neural Networks (CNN)]] holds for max pooling, not for average pooling.

### Output size and parameters

For a $W_1 \times H_1 \times C$ input, a pooling layer has two hyperparameters: the spatial extent $F$ and the stride $S$. The output is $W_2 \times H_2 \times C$, where ([[Block 4 Slides]], p. 148; Lecture 3 Notes - Convolutional and Pooling Layers):

$$W_2 = \frac{W_1 - F}{S} + 1 \qquad H_2 = \frac{H_1 - F}{S} + 1$$

A pooling layer has 0 parameters, so it has nothing to learn ([[Block 4 Slides]], p. 148; slide credit CS 231N). It reduces the number of parameters in the layers after it (p. 146). This reduces model complexity and overfitting (p. 147; Lecture 3 Notes - Convolutional and Pooling Layers).

### Shifts: equivariance and invariance

An equivariant output tracks a shift of the input. An invariant output erases it. Pooling guarantees neither ([[Block 4 Slides]], p. 137).

The deck tests this with 2x2 max pooling, stride 2, no padding. A one-pixel right shift of the input changed the output from `[9, 0], [0, 8]` to `[0, 9], [0, 8]` The top row moved and the bottom row did not, so the output is not one uniform shift (pp. 136-137). Pooling lowers resolution and gives only limited tolerance to local shifts (p. 137; Lecture 3 Notes - Convolutional and Pooling Layers).

Synthesis: p. 135 says max pooling gives "some" invariance to small shifts, and p. 137 says it guarantees none. The two slides do not conflict. The tolerance is real for some shifts but not for all.

### Global average pooling

ResNet puts a global average pooling layer after its last conv layer. Its only FC layer is FC 1000, to the output classes ([[Block 4 Slides]], p. 214).

## Related

- [[Convolutional Neural Networks (CNN)]]
- [[Convolutional Layer]]
- [[Fully Connected Layer]]
- [[Overfitting and Underfitting]]
- [[Residual Connections]]

## Sources

- [[Block 4 Slides]], pp. 133-148, 152, 214
- Lecture 3 Notes - Convolutional and Pooling Layers, § Pooling Layer, § Layer Summary
- [[F26-midterm-review-234p]], pp. 75-77
