---
description: A sequence model that applies one recurrence h_t = f_W(h_{t-1}, x_t) at every time step, so it carries a hidden state forward and reuses the same weights at every step.
aliases: [RNN, Recurrent Neural Network, Vanilla RNN, LSTM, GRU, Gated Recurrent Unit]
sources: ["Topic Note - Recurrent Neural Networks (RNN)", "Topic Note - Long Short-Term Memory Networks (LSTM)", "Topic Note - Sequence Transduction", "Topic Note - Transformers", "Attention Is All You Need (note)", "World Models, Ha & Schmidhuber (note)", "DreamerV3 (note)", "Fall 2026 Reading List", "[[Block 3 Slides]]", "[[Block 5 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 6 Sequence models
---

## Definition

An RNN reads a sequence one step at a time. At each step it combines the previous hidden state with the current input through one function $f_W$, and the same weights serve every step. The hidden state is the model's memory of everything it has read so far.

### Parameter Sharing Across Time

- One $\theta$ for every step, so the parameter count stays fixed as the sequence grows and the model accepts inputs of any length.
- Shared weights do not mean shared states: $h_t$ differs at each step because $x_t$ and $h_{t-1}$ differ.

| Model | Shares parameters over |
| --- | --- |
| CNN | space (one filter at every offset) |
| RNN | time (one update at every step) |
| GNN | graph neighbors |

### Sequence Task Shapes

| Shape | Input | Output | Example |
| --- | --- | --- | --- |
| One to many | one $x$ at step 1 | $y_t$ at every step | image captioning |
| Many to one | $x_1 \dots x_T$ | one $y$ from $h_T$ | action class from video |
| Many to many, delayed | $x_1 \dots x_T$, then decode | $y_1 \dots y_{T'}$ | video captioning, translation |
| Many to many, aligned | $x_t$ at every step | $y_t$ and $L_t$ at every step | frame-level video labels |

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

> [!tip]
> The LSTM eases vanishing gradients. It does not stop exploding gradients, so clipping still applies.

### GRU

**GRU update.** Two gates and no separate cell.
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
