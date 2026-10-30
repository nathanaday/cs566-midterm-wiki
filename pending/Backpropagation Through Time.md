---
id: con-gks021
type: topic
kind: concept
description: "Backpropagation through an RNN unrolled over time: forward through the sequence to compute the loss, then backward through it; the truncated form backpropagates only within chunks while the hidden state still carries forward."
tags: [machine-learning/cs566-deeplearning]
aliases: [BPTT, Full BPTT, Truncated BPTT, TBPTT, Truncated Backpropagation Through Time, Detaching the hidden state, detach(h)]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 5 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Recurrent Neural Networks (RNN)]]", "[[Backpropagation]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Recurrent Neural Networks (RNN)]] · [[Backpropagation]]

## Definition

Backpropagation through time (BPTT) is [[Backpropagation]] on a [[Recurrent Neural Networks (RNN)|recurrent network]] unrolled over its time steps. "Forward through entire sequence to compute loss, then backward through entire sequence to compute gradient" ([[Block 5 Slides]], p. 86).

## Explanation

### The gradient over time

The RNN uses the same $W$ at every step, so $W$ gets a gradient from every step's loss (p. 97):

$$\frac{\partial L}{\partial W} = \sum_{t=1}^{T} \frac{\partial L_t}{\partial W}$$

In a vanilla RNN, the gradient from the last loss passes back through every step (pp. 98–101):

$$\frac{\partial L_T}{\partial W} = \frac{\partial L_T}{\partial h_T} \Big( \prod_{t=2}^{T} \tanh'(W_{hh} h_{t-1} + W_{xh} x_t) \Big) W_{hh}^{T-1} \frac{\partial h_1}{\partial W}$$

The product of $\tanh'$ terms and the power $W_{hh}^{T-1}$ cause the [[Vanishing Gradient Problem]] and the [[Exploding Gradient Problem]] (pp. 101–105).

### Full BPTT is expensive

Full BPTT must save intermediate activations across the whole sequence. "A longer backward path needs more memory before an update" (p. 87; the midterm review repeats this slide, [[F26-midterm-review-234p]], p. 152). Synthesis: this is the memory cost of [[Backpropagation]], which grows here with sequence length.

### Truncated BPTT

"Run forward and backward through chunks of the sequence instead of whole sequence" (p. 89). "Carry hidden states forward in time forever, but only backpropagate for some smaller number of steps" (pp. 90–91).

The slides show eight steps split into non-overlapping chunks: losses 1–3, 4–6, and 7–8. For each chunk: sum or average its losses, backpropagate, and update $\theta$. "The targets stay the same; the gradient history is truncated" (p. 88; also [[F26-midterm-review-234p]], p. 153). The slides cite Sutskever (2013) for truncated BPTT (pp. 87–88).

### Carry the state, stop the gradient

At a chunk boundary, the next chunk starts with the same state value as the last hidden state of the previous chunk. "Forward memory can cross the boundary" (p. 92; also [[F26-midterm-review-234p]], p. 154).

The gradient does not cross. In the slides' schematic, $\text{detach}(h_2)$ stops the gradient from the chunk-2 loss at the boundary, so it does not flow into chunk 1. "The backpropagation horizon is shorter than the forward history" (p. 93; also [[F26-midterm-review-234p]], p. 155).

### Detaching the hidden state

The midterm review states the rule: "Detaching the state keeps its values as memory but stops gradients from flowing further back" ([[F26-midterm-review-234p]], p. 146). It works one chunk boundary with numbers ([[F26-midterm-review-234p]], p. 156):

- Chunk 1 ends with $h_2 = 4$.
- Chunk 2 has $x_3 = 1$ and the coefficient $a = 0.5$. It computes $h_3 = 0.5 \times 4 + 1 = 3$ from the detached value 4.
- Forward: the value 4 crosses the boundary. Backward: the gradient from the chunk-2 loss stops at the boundary and does not go into chunk 1.
- "a still gets gradients from chunk 2".

Synthesis: chunk 2 uses the shared coefficient $a$ to compute $h_3$, so $a$ still gets a gradient. Detach cuts only the path back through $h_2$ into chunk 1.

Synthesis: in PyTorch, `h.detach()` returns a tensor with the same value but no link to the graph that made it. The loop below is general background, not from the slides:

```python
h = h0
for chunk in chunks:
    h = h.detach()          # keep the value, cut the gradient
    loss = 0
    for x_t, y_t in chunk:
        h = rnn_cell(x_t, h)
        loss = loss + criterion(readout(h), y_t)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

Synthesis: a truncated gradient cannot directly tie a loss to an input more than one chunk back. The forward state can still carry that input's effect.

## Related

- [[Recurrent Neural Networks (RNN)]]
- [[Backpropagation]]
- [[Computational Graphs]]
- [[Vanishing Gradient Problem]]
- [[Exploding Gradient Problem]]
- [[Gradient Clipping]]
- [[Long Short-Term Memory]]

## Sources

- [[Block 5 Slides]], pp. 86–105. Pp. 87–88 cite Sutskever (2013). Pp. 94–105 cite Bengio et al. (1994) and Pascanu et al. (2013).
- [[F26-midterm-review-234p]], pp. 146, 152–156: the midterm review of Block 5 (Block 5, slides 87–93), with the worked detach example on p. 156
- The PyTorch loop and the note on `h.detach()`: general background, not from a course source
