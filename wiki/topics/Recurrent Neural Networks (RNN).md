---
description: A sequence model that applies one recurrence h_t = f_W(h_{t-1}, x_t) at every time step, so it carries a hidden state forward and reuses the same weights at every step.
aliases: [RNN, GRU, Gated Recurrent Unit, Recurrent Neural Network, Vanilla RNN, Many-to-many RNN, Weight sharing across time steps, RNN applications, Parameter sharing across time, RNN parameter sharing]
sources: ["Topic Note - Recurrent Neural Networks (RNN)", "Topic Note - Long Short-Term Memory Networks (LSTM)", "Topic Note - Sequence Transduction", "Topic Note - Transformers", "Attention Is All You Need (note)", "World Models, Ha & Schmidhuber (note)", "DreamerV3 (note)", "Fall 2026 Reading List", "[[Block 3 Slides]]", "[[Block 5 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 6 Sequence models
---

## Definition

An RNN reads a sequence one step at a time. At each step it combines the previous hidden state with the current input through one function $f_W$, and the same weights serve every step. The hidden state is the model's memory of everything it has read so far.

### Vanilla RNN

**Recurrence.**

$$h_t = f_W(h_{t-1}, x_t)$$

**Vanilla update and output.**

$$h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t), \qquad y_t = W_{hy} h_t$$

- Stacked form: $h_t = \tanh(W [h_{t-1}; x_t])$ with $W = [W_{hh} \;\; W_{xh}]$.
- $W_{xh}$ (also written $U$) reads the input, $W_{hh}$ (also $W$) carries the state, $W_{hy}$ (also $V$) emits the output.
- [[Activation Functions|tanh]] keeps the state in $(-1, 1)$.
- Unrolled, the network is a chain of identical $f_W$ blocks fed by one $W$; a many-to-many graph has a loss $L_t$ at every step and $L = \sum_t L_t$.

### Parameter Sharing Across Time

- One $\theta$ for every step, so the parameter count stays fixed as the sequence grows and the model accepts inputs of any length.
- Shared weights do not mean shared states: $h_t$ differs at each step because $x_t$ and $h_{t-1}$ differ.
- Scalar check, $h_t = 0.5\,h_{t-1} + x_t$ with $h_0 = 0$ and inputs $2, -1, 3$: states $2, 0, 3$. The coefficient 0.5 never changes.

| Model | Shares parameters over |
| --- | --- |
| CNN | space (one filter at every offset) |
| RNN | time (one update at every step) |
| GNN | graph neighbors |

See [[Convolutional Layer]] for the spatial case.

### Sequence Task Shapes

| Shape | Input | Output | Example |
| --- | --- | --- | --- |
| One to many | one $x$ at step 1 | $y_t$ at every step | image captioning |
| Many to one | $x_1 \dots x_T$ | one $y$ from $h_T$ | action class from video |
| Many to many, delayed | $x_1 \dots x_T$, then decode | $y_1 \dots y_{T'}$ | video captioning, translation |
| Many to many, aligned | $x_t$ at every step | $y_t$ and $L_t$ at every step | frame-level video labels |

- Many to one encodes a sequence into one vector; one to many decodes a sequence from one vector.
- In one to many, later steps take a zero vector or the previous output as input.
- The delayed shape is the encoder-decoder design: the encoder compresses the input, the decoder emits one token at a time (sequence transduction).

### Backpropagation Through Time

**Total gradient.** Forward through the whole sequence, then backward. Per-step gradients sum because $W$ is shared.

$$\frac{\partial L}{\partial W} = \sum_{t=1}^{T} \frac{\partial L_t}{\partial W}$$

**One step back.**

$$\frac{\partial h_t}{\partial h_{t-1}} = \tanh'(W_{hh} h_{t-1} + W_{xh} x_t)\, W_{hh}$$

**Last loss to first step.** The gradient passes through every step on the way.

$$\frac{\partial L_T}{\partial W} = \frac{\partial L_T}{\partial h_T} \Big( \prod_{t=2}^{T} \tanh'(W_{hh} h_{t-1} + W_{xh} x_t) \Big) W_{hh}^{T-1} \frac{\partial h_1}{\partial W}$$

### Vanishing and Exploding Gradients

| Cause | Effect | Remedy |
| --- | --- | --- |
| $\tanh' \le 1$ at every step | product shrinks, gradient vanishes | gated architecture (LSTM, GRU) |
| largest singular value of $W_{hh}$ below 1 | $W_{hh}^{T-1}$ shrinks, gradient vanishes | gated architecture |
| largest singular value of $W_{hh}$ above 1 | $W_{hh}^{T-1}$ grows, gradient explodes | [[Gradient Clipping]] |

- Vanishing: early inputs stop affecting late outputs, so long dependencies never train. See [[Vanishing Gradient Problem]].
- Exploding: at a steep cliff of the loss surface an unclipped step shoots off; clipping bounds the step. See [[Exploding Gradient Problem]].
- Any deep network can vanish, but the vanilla RNN multiplies by the same $W_{hh}$ at every step, so sequence length acts as depth.

> [!warning] Exam trap
> Clipping treats exploding gradients only. It does nothing for vanishing gradients; those need gates.

> [!tip]
> One hidden vector must hold distant context, local detail, and the next output at once, so each new word dilutes older facts. This is the case for a separate cell state.

### LSTM

**Gates and cell update.** $\sigma$ is the sigmoid and $\odot$ the elementwise product.

$$\begin{aligned} f_t &= \sigma(W_f [h_{t-1}; x_t] + b_f) \\ i_t &= \sigma(W_i [h_{t-1}; x_t] + b_i) \\ o_t &= \sigma(W_o [h_{t-1}; x_t] + b_o) \\ \tilde{c}_t &= \tanh(W_c [h_{t-1}; x_t] + b_c) \\ c_t &= f_t \odot c_{t-1} + i_t \odot \tilde{c}_t \\ h_t &= o_t \odot \tanh(c_t) \end{aligned}$$

| Gate | Range | Controls |
| --- | --- | --- |
| Forget $f_t$ | $(0, 1)$ | how much of $c_{t-1}$ to keep |
| Input $i_t$ | $(0, 1)$ | how much of the candidate $\tilde{c}_t$ to write |
| Output $o_t$ | $(0, 1)$ | how much of $c_t$ to expose as $h_t$ |

- The cell $c_t$ is the long-term memory; $h_t$ is the working output.
- The gradient along $c_t$ passes through elementwise $f_t$ only, with no repeated $W_{hh}$ multiply and no $\tanh'$, so it survives far longer. With $f_t \approx 1$ the cell is an additive path, like a residual connection.
- The vanilla update $h_t = \tanh(W [h_{t-1}; x_t])$ is the LSTM with no gates and no cell.

> [!warning] Exam trap
> The LSTM eases vanishing gradients. It does not stop exploding gradients, so clipping still applies.

### GRU

**GRU update.** Two gates and no separate cell.

$$\begin{aligned} r_t &= \sigma(W_{xr} x_t + W_{hr} h_{t-1} + b_r) \\ z_t &= \sigma(W_{xz} x_t + W_{hz} h_{t-1} + b_z) \\ \tilde{h}_t &= \tanh(W_{xh} x_t + W_{hh} (r_t \odot h_{t-1}) + b_h) \\ h_t &= z_t \odot h_{t-1} + (1 - z_t) \odot \tilde{h}_t \end{aligned}$$

- Reset gate $r_t$: how much of $h_{t-1}$ enters the candidate.
- Update gate $z_t$: near 1 keeps $h_{t-1}$, near 0 takes $\tilde{h}_t$.
- Further variants from the same architecture search: MUT1 to MUT3.

### Beyond the Vanilla Cell

- Bidirectional RNN: join a forward state (left context) with a backward state (right context); it needs the whole input in advance.
- Applications: captioning, question answering, VQA, speech recognition, action recognition, parsing, translation.
- The Transformer drops recurrence; every position reads every other position in one step, so training runs in parallel. See [[Transformers]].
- In 2026 the niche is streaming ASR and low-latency decoding; recurrence returns in xLSTM, SSMs, and state-plus-attention hybrids.
- World models still use them: the MDN-RNN of Ha and Schmidhuber predicts the next latent; the DreamerV3 RSSM pairs a deterministic recurrent state with a stochastic one.

## Related

- Backpropagation Through Time
- Long Short-Term Memory
- [[Transformers]]
- World Models
- [[Convolutional Neural Networks (CNN)]]
- [[Convolutional Layer]]: parameter sharing across space
- Computational Graphs
- [[Backpropagation]]
- [[Vanishing Gradient Problem]]
- [[Exploding Gradient Problem]]
- [[Gradient Clipping]]

## Sources

- Topic Note - Recurrent Neural Networks (RNN)
- Topic Note - Long Short-Term Memory Networks (LSTM)
- Topic Note - Sequence Transduction
- Topic Note - Transformers
- Attention Is All You Need (note)
- World Models, Ha & Schmidhuber (note)
- DreamerV3 (note)
- Fall 2026 Reading List
- [[Block 3 Slides]]
- [[Block 5 Slides]]
- [[F26-midterm-review-234p]]
