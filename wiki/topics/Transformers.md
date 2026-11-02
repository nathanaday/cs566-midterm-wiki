---
description: A sequence model built only from attention and feed-forward layers, with no recurrence or convolution; decoder-only variants such as GPT predict the next word, and encoder-only variants such as BERT are pretrained as masked language models.
aliases: [Transformer, Transformer block, Decoder-only Transformer, Encoder-only Transformer, BERT, Masked language model]
sources: ["Attention Is All You Need (note)", "Topic Note - Transformers", "Topic Note - Sequence Transduction", "An Image is Worth 16x16 Words (note)", "Fall 2026 Reading List", "[[Block 3 Slides]]", "[[Block 5 Slides]]", "[[Block 6 Slides]]", "[[Block 6 Slides Extended]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
subject: 6 Sequence models
---

## Definition

A Transformer is a sequence model built from attention and position-wise feed-forward layers only, with no recurrence or convolution. Every position reads every allowed position in one matrix step, so training runs in parallel over the sequence instead of stepping through it like an [[Recurrent Neural Networks (RNN)]]. The decoder-only variant (GPT) predicts the next token under a Causal Mask; the encoder-only variant (BERT) uses no mask and is pretrained as a masked language model.

## Explanation

### Scaled Dot-Product Attention

Each input row $x_i \in \mathbb{R}^{d_{\text{model}}}$ (token vector plus position vector) is projected three ways with learned matrices: queries $Q = XW_Q$, keys $K = XW_K$, values $V = XW_V$.

**Attention.**
$$
\operatorname{Attention}(Q, K, V) = \operatorname{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right) V
$$

- Row $i$ of $QK^{\top}$ scores how well query $i$ matches every key. The softmax turns the row into weights that sum to one, and the output is the weighted sum of the values.
- Why $\sqrt{d_k}$: if the entries of $q$ and $k$ have unit variance, their dot product has variance $d_k$. Large scores push the softmax into saturation, where gradients vanish. Dividing by $\sqrt{d_k}$ restores unit variance.
- Self-attention: $Q$, $K$, $V$ all come from the same sequence. Cross-attention: $Q$ from the decoder, $K$ and $V$ from the encoder output.

**Shapes through one head**, for a sequence of $n$ tokens:

| Tensor | Shape | Note |
| --- | --- | --- |
| $X$ | $n \times d_{\text{model}}$ | input |
| $W_Q, W_K$ | $d_{\text{model}} \times d_k$ | learned |
| $W_V$ | $d_{\text{model}} \times d_v$ | learned |
| $Q, K$ | $n \times d_k$ | |
| $V$ | $n \times d_v$ | |
| $QK^{\top}$ | $n \times n$ | one score per (query, key) pair |
| softmax rows | $n \times n$ | each row sums to 1 |
| head output | $n \times d_v$ | |

**Multi-head attention.** Run $h$ heads in parallel on lower-dimensional projections, concatenate, and mix with $W_O$:

$$
\operatorname{MultiHead}(X) = \operatorname{Concat}(\text{head}_1, \ldots, \text{head}_h)\, W_O, \qquad \text{head}_i = \operatorname{Attention}(XW_Q^{(i)}, XW_K^{(i)}, XW_V^{(i)})
$$

With $d_k = d_v = d_{\text{model}}/h$, the concatenation is $n \times d_{\text{model}}$ and $W_O$ is $d_{\text{model}} \times d_{\text{model}}$, so $h$ heads cost about the same as one full-width head. The original paper uses $d_{\text{model}} = 512$, $h = 8$, $d_k = 64$.

**Complexity.** Per layer, self-attention costs $O(n^2 d)$ time and $O(n^2)$ memory for the score matrix, with $O(1)$ sequential steps and a path of length 1 between any two positions. An RNN layer costs $O(n d^2)$ but takes $n$ sequential steps. The quadratic term dominates on long sequences; for ViT, patch size sets token count, and token count sets cost (Visual Token Count).

### Positional Encoding

Attention is permutation invariant: "dog bites man" and "man bites dog" give the same bag of token vectors. The model adds a position vector to each token embedding before the first block.

**Sinusoidal encoding.**
$$
PE_{(pos,\, 2i)} = \sin\!\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right), \qquad
PE_{(pos,\, 2i+1)} = \cos\!\left(\frac{pos}{10000^{2i/d_{\text{model}}}}\right)
$$

Learned position embeddings (GPT, BERT) work as well at fixed lengths. See Positional Encoding and Tokenization.

### Block Layout

Every block has two sublayers, each wrapped as $\text{LayerNorm}(x + \text{Sublayer}(x))$. The feed-forward sublayer is one MLP applied to each position separately with shared weights.

| Block | Sublayers in order | Mask |
| --- | --- | --- |
| Encoder | self-attention, add & norm, FFN, add & norm | none |
| Decoder (encoder-decoder) | masked self-attention, add & norm, cross-attention, add & norm, FFN, add & norm | causal on self-attention |
| Decoder-only (GPT) | masked self-attention, add & norm, FFN, add & norm | causal |
| Encoder-only (BERT) | self-attention, add & norm, FFN, add & norm | none |

- BERT and GPT-3 use GELU in the FFN instead of ReLU 

> [!tip]
> Depth counts blocks; generation length counts tokens. One attention layer already reads the whole allowed prefix; more blocks add processing steps, not reach.

### Masking in the Decoder

The causal mask adds $-\infty$ to every score $s_{ij}$ with $j > i$ before the softmax, so those weights become exactly zero and position $i$ reads only itself and earlier positions. Position, mask, and attention weights answer three separate questions: where a token is, which tokens are visible, and how much each contributes.

- Training: all target positions are known, so one pass scores every position at once (Teacher Forcing).
- Generation: each step sees only the generated prefix (Autoregressive Language Modeling); a KV Cache reuses past keys and values.
- Padding mask: the same trick hides padded positions in a batch, in encoder or decoder.
- Graph view: unmasked self-attention is a complete graph over tokens with input-dependent edge weights; the causal mask makes the edges directional ([[Graph Neural Networks]]).

> [!tip]
> The causal mask is the only difference between the decoder-only and encoder-only layers. Masked language modeling (BERT) hides a token and predicts it from both sides, so it needs unmasked attention; next-token prediction (GPT) uses left context only. The MLM [MASK] token and the causal attention mask are different things.


## Related

- Attention
- Causal Mask: decoder-only vs encoder-only layers
- Positional Encoding
- Autoregressive Language Modeling: the decoder's objective; MLM is the encoder's
- Teacher Forcing
- Tokenization
- [[Recurrent Neural Networks (RNN)]]
- [[Convolutional Neural Networks (CNN)]]
- [[Graph Neural Networks]]
- Vision Language Models (VLM)
- Visual Token Count
- KV Cache
- [[Residual Connections]]
- [[Layer Normalization]]
- [[Activation Functions]]
- [[Activation Sparsity]]
- Scaling Laws
- [[Transfer Learning]]
- [[Fine-Tuning]]
- [[Adapters]]
- LLMs and Graphs

## Sources

- Attention Is All You Need (note)
- Topic Note - Transformers
- Topic Note - Sequence Transduction
- An Image is Worth 16x16 Words (note)
- Fall 2026 Reading List
- [[Block 3 Slides]]
- [[Block 5 Slides]]
- [[Block 6 Slides]]
- [[Block 6 Slides Extended]]
- [[Block 7 Slides]]
- [[F26-midterm-review-234p]]
