---
id: con-j3y7dq
type: topic
kind: concept
description: A recurrent cell (Hochreiter and Schmidhuber, 1997) that carries a cell state for memory and a hidden state for output, and uses learned forget, input, and output gates to retain, write, and expose memory at each time step.
tags: [machine-learning]
aliases: [LSTM, Long Short Term Memory, LSTM cell, Cell state, Forget gate, Input gate, Output gate, Candidate update, LSTM gate, Retention factor, Compact state bottleneck, Fixed-size state bottleneck]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 5 Slides]]", "Topic Note - Long Short-Term Memory Networks (LSTM)", "[[F26-midterm-review-234p]]"]
up: ["[[Recurrent Neural Networks (RNN)]]"]
---

> [!concept] Concept
> 3 sources · refreshed 2026-10-19 · #machine-learning
> Up: [[Recurrent Neural Networks (RNN)]]

## Definition

The LSTM (Long Short-Term Memory) is a recurrent cell that carries two states forward. The cell state $c_t$ holds memory. The hidden state $h_t$ exposes what the model needs now ([[Block 5 Slides]], p. 116). Three learned gates decide at each step how much old memory to retain, how much new content to write, and how much memory to expose (p. 120). The deck gives it the subtitle "Memory with Learned Gates" (p. 106) and credits it to Hochreiter and Schmidhuber, *Long Short Term Memory*, Neural Computation 1997 (p. 204). The midterm review sums it up: "An LSTM uses gates to decide what to retain, what to write, and what to output" ([[F26-midterm-review-234p]], p. 146).

The user's topic note dates the LSTM from about 1997. It says the LSTM addresses part of the vanishing gradient problem of RNNs: more internal mechanisms keep early input features effective over longer sequences (Topic Note - Long Short-Term Memory Networks (LSTM)). The note does not name the gates; the slides do.

## Explanation

### Contrast with the vanilla RNN

In the vanilla RNN the state is a single hidden vector $h$ ([[Block 5 Slides]], p. 52). The character model updates it as $h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t)$ (p. 72). The LSTM must learn when to retain memory and when to update it (p. 107). It splits the state into two lanes and puts gates on each lane.

### Two states

- The cell state carries memory. The hidden state is exposed now (p. 116).
- Both states move forward when the next token arrives. The output gate maps $c_t$ to $h_t$, and $h_t$ feeds the prediction head (p. 116).
- Exposing memory for an output does not delete the cell. The cell memory also passes to the next step (p. 117).
- The cell state and the exposed hidden state have different roles (p. 221). The midterm review says: "In an LSTM, the cell state and the exposed hidden state are separate quantities" ([[F26-midterm-review-234p]], p. 146).
- The midterm review repeats these points with the same figures: the hidden state goes to the prediction head and to the next step ([[F26-midterm-review-234p]], pp. 166–167, 172).

### The gates

| Part | Symbol | Activation | What it does | Pages |
| --- | --- | --- | --- | --- |
| Forget gate | $f_t$ | sigmoid | Multiplies the old cell $c_{t-1}$; sets how much old memory to keep | 111–112, 208, 215 |
| Input gate | $i_t$ | sigmoid | Sets how much of the candidate to write into the cell | 208, 216 |
| Candidate update | $g_t$ | tanh | Supplies the content to write | 208, 216, 218 |
| Output gate | $o_t$ | sigmoid | Sets how much of the cell to reveal as $h_t$ | 117, 208, 217 |

- A gate is a learned, continuous dimmer between 0 and 1 on existing memory. Values near 1 keep most of the old cell content (p. 111).
- "Forget gate" is the historical name. The math is a retention factor that multiplies $c_{t-1}$. A high forget gate retains more; a low one retains less (p. 112).
- The forget and input gates act at the same step. Retaining old memory and writing new memory are separate decisions (p. 114).
- The forget gate $f$ and the input gate $i$ are independent gates, so they need not sum to 1 ([[F26-midterm-review-234p]], p. 168).
- p. 208 labels $g$ "Gate gate (?)". The same slide and pp. 216, 218 describe $g$ as candidate content, with $i$ setting how much of it is written.
- All gates and the candidate take the current input $x_t$ together with the previous hidden state $h_{t-1}$ (p. 121). The gate weights $W_f, W_i, W_o$ produce gate values in $[0, 1]$ (p. 119).
- In one layer, the weights are shared across time, and backpropagation through time trains each weight matrix. Shared trained weights compute context-dependent gates (p. 119).
- One time step runs in this order: retain the past and write the new candidate, which gives the updated cell; then expose part of the cell to the hidden state ([[F26-midterm-review-234p]], p. 171). "The three gates work together inside one repeated LSTM cell" ([[F26-midterm-review-234p]], p. 172).

### Equations

The deck gives (p. 205):

$$\begin{pmatrix} i \\ f \\ o \\ g \end{pmatrix} = \begin{pmatrix} \sigma \\ \sigma \\ \sigma \\ \tanh \end{pmatrix} W \begin{bmatrix} h_{t-1} \\ x_t \end{bmatrix}$$

$$c_t = f \odot c_{t-1} + i \odot g \qquad h_t = o \odot \tanh(c_t)$$

- $W$ stacks four blocks, $W_i, W_f, W_o, W_g$. Each gate applies its own block to $[h_{t-1}; x_t]$, for example $g = \tanh(W_g [h_{t-1}; x_t])$ (pp. 206–207). Written out, one block is $g = \tanh(W_{gh} h_{t-1} + W_{gx} x_t)$ (p. 205).
- $W$ has shape $4h \times 2h$. It maps the stacked $x$ and $h$ to a $4h$ vector, which splits into $i, f, o$ (sigmoid) and $g$ (tanh) (p. 208).
- The cell diagram follows the standard PyTorch LSTM equations (p. 121).

Synthesis: the $4h \times 2h$ shape assumes that the input $x_t$ has the same size $h$ as the hidden state.

### Gradient path

- The cell state has an additive path, $c_t = f_t c_{t-1} + i_t g_t$ (p. 211). Old and new information meet by addition (p. 220).
- The additive route avoids a repeated recurrent weight matrix (p. 211). Additive cell updates give a controllable gradient path (p. 204).
- Along the direct cell path the gradient multiplier is $f_t \times f_{t-1} \times \dots$. This path preserves a gradient when the forget gates stay near 1 (p. 212).
- Over 10 steps with $f = 0.9$, the direct-path multiplier is $0.9^{10} \approx 0.349$ (p. 213).
- The LSTM improves the gradient route, but retention still depends on the gates. Long memory is a learned behavior. The gates also depend on the recurrent state, not only on the direct cell path (p. 213).

Synthesis: in the vanilla RNN, the gradient passes through $W_{hh}$ and a tanh at every step, which is where the [[Vanishing Gradient Problem]] comes from. The LSTM cell path is similar to the identity path of [[Residual Connections]]: the gradient passes through a sum, scaled only by the forget gate.

### Worked example

The deck uses these values: $c_{t-1} = 2$, $f_t = 0.8$, $i_t = 0.5$, $g_t = 0.4$, $o_t = 0.75$ (p. 218).

1. Retain: $f_t c_{t-1} = 0.8 \times 2 = 1.6$ (p. 219).
2. Write: $i_t g_t = 0.5 \times 0.4 = 0.2$ (p. 220).
3. Update: $c_t = 1.6 + 0.2 = 1.8$ (p. 220).
4. Expose: $h_t = o_t \tanh(c_t) = 0.75 \times \tanh(1.8) \approx 0.710$ (p. 221).

The midterm review gives a second example for the cell update $c_{new} = f \odot c_{old} + i \odot \text{candidate}$, with $c_{old} = 4$ and candidate $= 0.5$ ([[F26-midterm-review-234p]], p. 168):

| $f$ | $i$ | $c_{new}$ |
| --- | --- | --- |
| 0.9 | 0.1 | $0.9 \times 4 + 0.1 \times 0.5 = 3.65$ |
| 0.1 | 0.6 | $0.1 \times 4 + 0.6 \times 0.5 = 0.7$ |

Then $h_{new} = o \odot \tanh(c_{new})$, so the output gate controls the exposed state separately ([[F26-midterm-review-234p]], p. 168).

Synthesis: the first gate setting keeps most of the old memory. The second setting drops most of it and writes more of the candidate.

### Teaching analogy: where does Maya live now?

The deck marks this example as a teaching analogy, with no literal neuron slots and no measured activations (p. 107). The story is "Maya lives in Boston." → "She likes tea." → "Later she moves to Seattle." For the query "Where does Maya live now?" the correct answer is Seattle (p. 107). The midterm review repeats the analogy step by step ([[F26-midterm-review-234p]], pp. 157–167).

1. The first sentence adds Boston to the memory sketch. Initial evidence sets the current context (p. 109).
2. "She likes tea" is unrelated, so Boston stays. New input should not erase unrelated memory (p. 110).
3. "Moves to" signals a change. The retain slider for Boston turns low, and Seattle becomes a candidate (p. 113). A high input gate writes Seattle (p. 114).
4. The output gate filters $\tanh(c_t)$ into $h_t$, and the prediction head predicts Seattle (p. 117).

Real memory is not a set of named slots. The city names label the sketch; real neural vectors are dense vectors in $\mathbb{R}^d$. Gates are vectors in $[0, 1]^d$, and each dimension dims on its own (p. 118). Gates softly modulate features; values near 0 retain little (p. 112).

### Limit: a compact state

A fixed-size state pair $(c_t, h_t)$ has to compress a history of any length, such as hundreds of tokens (p. 122). The midterm review names this "a compact state bottleneck": "A fixed-size state must compress the entire past" ([[F26-midterm-review-234p]], p. 173). The deck asks whether a model can keep separate vectors and read them when needed. This question leads to attention (p. 122); see [[Transformers]] and [[Recurrent State vs Growing Context]].

### Variants

The deck cites Greff et al. 2015, *LSTM: A Search Space Odyssey*, as a study of LSTM variants (p. 222). The same slide shows the MUT1, MUT2, and MUT3 updates from Jozefowicz et al. 2015, *An Empirical Exploration of Recurrent Network Architectures*. Each uses gates $z$ and $r$ and computes $h_{t+1} = \tanh(\dots) \odot z + h_t \odot (1 - z)$ (p. 222).

### Place in the course

The classroom introduction focuses on memory and gates. The deck marks the equations, gradient paths, and worked values as optional material for a deeper implementation study (p. 203).

## Related

- [[Recurrent Neural Networks (RNN)]]
- [[Backpropagation Through Time]]
- [[Recurrent State vs Growing Context]]: the fixed state against a growing KV cache
- [[Vanishing Gradient Problem]]
- [[Exploding Gradient Problem]]
- [[Gradient Clipping]]
- [[Residual Connections]]
- [[Activation Functions]]
- [[Backpropagation]]
- [[Transformers]]

## Sources

- [[Block 5 Slides]], pp. 52, 72, 106–122, 203–222. The LSTM section cites the standard LSTM in the PyTorch documentation and marks the Maya example as a teaching analogy by Y. Zhao (pp. 107–120). p. 204 also cites Colah's blog post "Understanding LSTMs" (colah.github.io/posts/2015-08-Understanding-LSTMs/).
- Topic Note - Long Short-Term Memory Networks (LSTM)
- [[F26-midterm-review-234p]], pp. 146, 157–173: the midterm review of the Block 5 LSTM slides (Block 5, slides 107–122)
- The size assumption under Equations, the comparisons under Gradient path, and the reading of the second worked example: synthesis, not from a source
