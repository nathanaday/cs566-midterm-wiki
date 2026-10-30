---
description: A sequence model that applies one recurrence h_t = f_W(h_{t-1}, x_t) at every time step, so it carries a hidden state forward and reuses the same weights at every step.
aliases: [RNN, GRU, Gated Recurrent Unit, Recurrent Neural Network, Vanilla RNN, Many-to-many RNN, Weight sharing across time steps, RNN applications, Parameter sharing across time, RNN parameter sharing]
sources: ["Topic Note - Recurrent Neural Networks (RNN)", "Topic Note - Long Short-Term Memory Networks (LSTM)", "Topic Note - Sequence Transduction", "Topic Note - Transformers", "Attention Is All You Need (note)", "World Models, Ha & Schmidhuber (note)", "DreamerV3 (note)", "Fall 2026 Reading List", "[[Block 3 Slides]]", "[[Block 5 Slides]]", "[[F26-midterm-review-234p]]"]
---

## Definition

A typical neural network receives all input features at once and produces one output. An RNN receives each feature of the input at a different time step. At each step it receives both the output of the last step and the next input feature (Topic Note - Recurrent Neural Networks (RNN)). The note dates the architecture from about 1986 and says it is most common in NLP.

[[Block 5 Slides]] gives the general form: "We can process a sequence of vectors x by applying a recurrence formula at every time step" (p. 43):

$$h_t = f_W(h_{t-1}, x_t)$$

Here $h_t$ is the new state, $h_{t-1}$ the old state, $x_t$ the input vector at some time step, and $f_W$ some function with parameters $W$ (pp. 44–48). The same function with the same parameters runs at every time step (p. 49). The move from $h_t$ to $h_{t+1}$, $f(h_t; \theta)$, is itself a neural network (pp. 29–30). A feedforward network sends its signal in one direction. A recurrent network has cycles in its connections (p. 27).

[[Block 3 Slides]] introduces RNNs as the model "for sequences", for data with a time dependency such as stock prices (pp. 270–271). The diagram unrolls one hidden state $h$ into steps $h_{t-4} \to \dots \to h_t$. Each step takes input $x_t$ through weight $U$, passes the state forward through the same weight $W$, and emits output $y$ through weight $V$ (p. 271).

## Explanation

### Why sequences need recurrence

[[Block 5 Slides]] starts from speech recognition. A function $f(X)$ maps each audio window to one character, giving T, H, E, S, O for "THE SOUND OF" (pp. 6–11). The outputs of neighboring windows are independent. Groups of windows are also independent, so the model cannot use context across words (pp. 14–15).

Other sequential tasks in the deck are handwriting recognition, machine translation (p. 16), image captioning, constituency parsing (p. 17), and video action detection (p. 18, citing Yeung et al., CVPR 2017). The captioning pipeline pairs a vision deep CNN with a language-generating RNN (p. 17).

A sequence model must handle inputs of different lengths, such as "a big house" (3 tokens) and "a car on a road" (5 tokens). Earlier words can affect later predictions. "We need a computation that can continue as the sequence grows" (p. 20).

### Vanilla RNN

The vanilla RNN makes $f_W$ concrete ([[Block 5 Slides]], pp. 51–53):

$$h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t), \qquad y_t = W_{hy} h_t$$

The state is a single "hidden" vector $h$ (p. 52). If you stack $h_{t-1}$ and $x_t$, the update becomes $h_t = \tanh(W [h_{t-1}; x_t])$ (pp. 94, 205). Synthesis: $W$ is $W_{hh}$ and $W_{xh}$ placed side by side.

Recall [[Activation Functions|tanh]] is a nonlinear activation.

### Parameter sharing

The deck asks what goes wrong with a separate network for each step, $\theta_1, \theta_2, \theta_3$ (pp. 31, 36). Each new position then needs another trained network, and the parameter count grows with sequence length (p. 37). An RNN uses one update rule $f_\theta$ for any number of steps. The weights stay the same, while the input and the previous state change (p. 38). Sharing $\theta$ does not make the hidden states or the predictions identical (p. 40). The unrolled graph shows the same rule: "Re-use the same weight matrix at every time-step" (p. 57).

[[F26-midterm-review-234p]] repeats these points in its Block 5 review: "Recurrent networks carry a state across time steps using the same weights at every step" (p. 146), and "An RNN reuses a learned transition across time" (p. 148). The review adds a worked example with scalar values and no nonlinearity (p. 151). The rule $h_t = 0.5 \times h_{t-1} + x_t$ updates a state from sensor readings, starting from $h_0 = 0$:

| Step | Input $x_t$ | Update | State $h_t$ |
| --- | --- | --- | --- |
| 1 | 2 | $0.5 \times 0 + 2$ | 2 |
| 2 | −1 | $0.5 \times 2 + (-1)$ | 0 |
| 3 | 3 | $0.5 \times 0 + 3$ | 3 |

The stored coefficient 0.5 is the same at every step, while the input and the carried state change ([[F26-midterm-review-234p]], p. 151).

The deck puts this in a wider pattern (pp. 4, 40):

| Model | Shares parameters over |
| --- | --- |
| CNN | spatial offsets (one filter reused across space) |
| RNN | the previous state (one update reused across time) |
| GNN | graph neighbors |

The common pattern is shared parameters, then structured computation, then task-specific outputs. "Keep parameter sharing; change which information can interact" (p. 4). See [[Convolutional Layer]] for the CNN case. The midterm review states the contrast in two lines: "CNN: reuse a filter across space. RNN: reuse an update across time" ([[F26-midterm-review-234p]], p. 150).

### Computational graph

Unrolled over time, the RNN is a chain of $f_W$ blocks. $h_0$ and $x_1$ enter $f_W$ to give $h_1$. Then $h_1$ and $x_2$ give $h_2$, and so on to $h_T$ ([[Block 5 Slides]], pp. 54–56). One $W$ feeds every block (p. 57). In the many-to-many graph, each $h_t$ emits an output $y_t$. Each $y_t$ has its own loss $L_t$, computed against the true value, and the losses sum into one total loss $L$ (pp. 58–61). The slides credit these graphs to the Stanford CS231n lecture slides (pp. 42–69). See Computational Graphs.

### Input and output configurations

| Configuration | Graph | Example |
| --- | --- | --- |
| One to many | one input $x$ at the first step; an output $y_t$ at every step (p. 64) | image captioning: an image to a sequence of words (p. 23) |
| Many to one | inputs $x_1 \dots x_T$; one output $y$ from $h_T$ (p. 62), or in a variant from all hidden states (p. 63) | action prediction: video frames to an action class (p. 24) |
| Many to many, outputs after the inputs | the input sequence first, then the output sequence | video captioning: video frames to a caption (p. 25) |
| Many to many, one output per input | an output $y_t$ and a loss $L_t$ at every step (pp. 58–60) | video classification on frame level (p. 26) |

Source: [[Block 5 Slides]]; the diagrams on pp. 22–26 come from Stanford CS231n.

Many to one encodes the input sequence in a single vector (p. 68). One to many produces an output sequence from a single input vector (p. 69). For the later steps of one to many, the slides show two inputs: zero vectors, or the previous output (pp. 65–67). With the second option, the output of the previous step enters the next step with the recurrent hidden state (p. 67).

### Training and gradient flow

An RNN trains with Backpropagation Through Time: forward through the sequence to compute the loss, then backward through it to compute the gradient ([[Block 5 Slides]], p. 86). The total gradient is the sum of the per-step gradients (p. 97):

$$\frac{\partial L}{\partial W} = \sum_{t=1}^{T} \frac{\partial L_t}{\partial W}$$

One step back from $h_t$ to $h_{t-1}$ multiplies by $W_{hh}^T$ (p. 95):

$$\frac{\partial h_t}{\partial h_{t-1}} = \tanh'(W_{hh} h_{t-1} + W_{xh} x_t)\, W_{hh}$$

So the gradient from the last loss back to $W$ passes through every step (pp. 98–101):

$$\frac{\partial L_T}{\partial W} = \frac{\partial L_T}{\partial h_T} \Big( \prod_{t=2}^{T} \tanh'(W_{hh} h_{t-1} + W_{xh} x_t) \Big) W_{hh}^{T-1} \frac{\partial h_1}{\partial W}$$

The slides cite Bengio et al., "Learning long-term dependencies with gradient descent is difficult" (IEEE Transactions on Neural Networks, 1994), and Pascanu et al., "On the difficulty of training recurrent neural networks" (ICML 2013) (pp. 94–105).

### Gradient problems

- **Vanishing gradients.** Outputs early in the sequence have less and less effect on later time steps (Topic Note - Recurrent Neural Networks (RNN)). The problem "can occur in any type of deep neural network. However, it is more prominently discussed in the architecture with sequential data" ([[Block 3 Slides]], p. 225). In the vanilla RNN, $\tanh' \le 1$ at every step, so the product of $\tanh'$ terms makes the gradient vanish ([[Block 5 Slides]], p. 101). With no non-linearity, the gradient is $\frac{\partial L_T}{\partial h_T} W_{hh}^{T-1} \frac{\partial h_1}{\partial W}$, and it vanishes when the largest singular value of $W_{hh}$ is less than 1 (pp. 102–103). The slides' remedy is to change the RNN architecture (p. 105). See [[Vanishing Gradient Problem]].
- **Exploding gradients.** With no non-linearity, gradients can explode when the largest singular value of $W_{hh}$ is greater than 1. The fix is [[Gradient Clipping]] ([[Block 5 Slides]], pp. 103–104). [[Block 3 Slides]] shows clipping on the loss surface of a simple RNN whose hidden state is a scalar. Without clipping, gradient descent takes two very big steps at a steep "cliff" and shoots off; with clipping, the steps are smaller (p. 236). See [[Exploding Gradient Problem]].

### One hidden state for everything

A standard RNN uses a single recurrent hidden state $h_t$ to remember earlier context, remember local detail, and predict the next output ([[Block 5 Slides]], p. 108). One vector mixes distant context and immediate detail, so intervening words can dilute or displace earlier facts (p. 108). The midterm review repeats the slide: "A single hidden state mixes memory and immediate output" ([[F26-midterm-review-234p]], p. 158).

### LSTM and GRU

The LSTM (from about 1997) addresses part of the vanishing gradient problem in RNNs. It adds internal mechanisms that keep earlier input features effective over longer sequences (Topic Note - Long Short-Term Memory Networks (LSTM)). [[Block 5 Slides]] gives the LSTM equations and shows the vanilla update $h_t = \tanh(W [h_{t-1}; x_t])$ beside them for contrast (p. 205). See Long Short-Term Memory.

The slides list the GRU under "Other variants", from Cho et al. 2014, "Learning phrase representations using RNN encoder-decoder for statistical machine translation" ([[Block 5 Slides]], p. 222):

$$\begin{aligned} r_t &= \sigma(W_{xr} x_t + W_{hr} h_{t-1} + b_r) \\ z_t &= \sigma(W_{xz} x_t + W_{hz} h_{t-1} + b_z) \\ \tilde{h}_t &= \tanh(W_{xh} x_t + W_{hh} (r_t \odot h_{t-1}) + b_h) \\ h_t &= z_t \odot h_{t-1} + (1 - z_t) \odot \tilde{h}_t \end{aligned}$$

The same slide cites Greff et al. 2015, "LSTM: A Search Space Odyssey", and Jozefowicz et al. 2015, "An Empirical Exploration of Recurrent Network Architectures", with three more variants, MUT1 to MUT3 (p. 222).

Synthesis: $r_t$ is the reset gate and $z_t$ the update gate. When $z_t$ is near 1, the unit keeps its old state $h_{t-1}$. When $z_t$ is near 0, it takes the candidate $\tilde{h}_t$.

### Bidirectional RNN

To read "bank" in "She sat on the bank of the river.", the model joins a forward RNN state (left context) and a backward RNN state (right context). Both directions help when the full input is already available ([[Block 5 Slides]], p. 231). The slide marks this topic as optional and points to the PyTorch LSTM documentation (p. 231).

### Applications

The deck lists image captioning, image captioning with attention, question answering, visual question answering, speech recognition, action recognition in videos, text parsing, and machine translation ([[Block 5 Slides]], p. 153).

### Sequence transduction

Transduction is converting one thing into another, for example language translation or speech to text. A sequence transduction model converts one sequence into another; classification takes a sequence but outputs one label (Topic Note - Sequence Transduction). Before the Transformer, RNNs or CNNs did this work in an encoder-decoder design. The encoder reads the whole input and compresses it into an internal representation. The decoder generates the output sequence one piece at a time (Topic Note - Sequence Transduction).

### Replacement by the Transformer

The Transformers note says a model does not need to track hidden states the way RNNs and LSTMs do. At each step, it looks over the whole sequence instead (Topic Note - Transformers). The Attention note says the Transformer removes recurrence, and attention lets every position read every other position in one step, so training runs in parallel (Attention Is All You Need (note)).

### RNNs in 2026

[[Block 5 Slides]] gives a timeline (p. 199):

- 2014–17: CNN + RNN models for captioning and QA.
- 2018–24: the Transformer and VLMs as the common interface.
- 2025–26: recurrent and hybrid models with fixed-state decoding.

"Keep the mechanisms; update the deployment framing" (p. 199). Four design questions stay the same across generations: state (what persists across steps), shared rule (the same parameters at many positions), conditioning (which evidence changes the output), and interface (how one module feeds another). "Architecture names change faster than these design questions" (p. 200).

The slides sum up RNNs and LSTMs in 2026 as shared parameters plus gated credit paths. Their current niche is streaming ASR and low-latency decoding. Recurrence returns through xLSTM, SSMs, and hybrids of mostly state plus selective attention (p. 230).

### Still used in world models

- The note on Ha & Schmidhuber says an MDN-RNN predicts the next latent from the current latent and the action. Because the RNN can roll futures forward alone, the controller trains inside imagined rollouts (World Models, Ha & Schmidhuber (note)). The reading list calls this recurrent network the part that predicts the next latent state (Fall 2026 Reading List, item 7).
- The DreamerV3 note says its Recurrent State Space Model (RSSM) splits each state into a deterministic recurrent part and a stochastic part (DreamerV3 (note)).

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
- Fall 2026 Reading List, item 7
- [[Block 3 Slides]], pp. 225, 236, 270–271
- [[Block 5 Slides]], pp. 4–69, 86–108, 153, 199–200, 205, 222, 230–231. The slides credit the RNN diagrams on pp. 22–69 to Stanford CS231n.
- [[F26-midterm-review-234p]], pp. 146–151, 158: the midterm review of Block 5 (Block 5, slides 37–40, 108)
