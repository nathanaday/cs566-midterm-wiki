---
description: A sequence model built only from attention and feed-forward layers, with no recurrence or convolution; decoder-only variants such as GPT predict the next word, and encoder-only variants such as BERT are pretrained as masked language models.
aliases: [Transformer, Decoder-only Transformer, GPT-style Transformer, Text-generating Transformer, Autoregressive Transformer, Transformer block, Transformer layer, Transformer LM, Encoder-only Transformer, Masked language model, Masked language modeling, MLM, MLM pretraining, BERT, BERT-Base, BERT-Large]
sources: ["Attention Is All You Need (note)", "Topic Note - Transformers", "Topic Note - Sequence Transduction", "An Image is Worth 16x16 Words (note)", "Fall 2026 Reading List", "[[Block 3 Slides]]", "[[Block 5 Slides]]", "[[Block 6 Slides]]", "[[Block 6 Slides Extended]]", "[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
---

## Definition

The Attention note says the Transformer is a sequence model built only from attention and feed-forward layers. It removes recurrence and convolution entirely (Attention Is All You Need (note)). The Transformers note dates it to about 2017. It says the model does not track hidden states the way RNNs and LSTMs do. At each step it looks over the whole sequence and finds associations between each step and the rest of the sequence (Topic Note - Transformers).

Block 6 calls the Transformer one of the most popular architectures, with strong results on many sequence modeling tasks. It names self-attention as the key component ([[Block 6 Slides]], p. 115; [[Block 6 Slides Extended]], p. 122).

## Explanation

### Mechanics

- **Parallel training.** Scaled dot-product attention lets every position read every other position in one step, so training runs in parallel across the sequence instead of stepping through it (Attention Is All You Need (note)). Block 5 makes the same contrast. An RNN updates its state one step at a time (h1 -> h2 -> h3 -> h4), so each step waits for the previous state. A Transformer processes positions in parallel as batched matrix operations on a GPU ([[Block 5 Slides]], p. 151).
- **Multi-head attention** is the same attention operation run in parallel on lower-dimensional projections. The note points to Section 3 of the paper and the Q/K/V matrix shapes as the part to study (Attention Is All You Need (note)).
- **Shared parts.** Multi-head attention, positional encodings, and the residual plus layer-norm block are the parts that every model on the Fall 2026 Reading List reuses (Attention Is All You Need (note); Fall 2026 Reading List, item 1).

### Decoder-only text generation

Block 5 builds a decoder-only, GPT-style Transformer that continues "The dog chased the ball. It ...". It cites Vaswani et al. (2017) and Radford et al. (2019) ([[Block 5 Slides]], pp. 129–150). The midterm review repeats slides 129–149 of this sequence as its pp. 175–194, and it labels each page with its Block 5 slide number ([[F26-midterm-review-234p]], pp. 175–194). The whole model is ([[Block 5 Slides]], p. 149; [[F26-midterm-review-234p]], p. 194):

Tokens + position -> Transformer block x L -> Prediction head -> Next token

The opening slide follows one path: token + position, then attention reads context, then the MLP processes features, then the prediction of the next token. Attention and the MLP repeat in several layers ([[Block 5 Slides]], p. 129; [[F26-midterm-review-234p]], p. 175). The deck names four pieces to remember: position tracks word order, attention mixes context, the MLP transforms each vector, and the prediction head scores the next token ([[Block 5 Slides]], p. 150).

The midterm review sums up two rules of the model. Weights are shared across positions within a layer, while different layers have distinct weights. In training, all target positions are known; in generation, each step sees only the generated prefix ([[F26-midterm-review-234p]], p. 174).

**Token vectors.** Each token begins as a learned vector of feature values ([[Block 5 Slides]], p. 130; [[F26-midterm-review-234p]], p. 176). Multiplication of a one-hot vector by a weight matrix picks out one column of the matrix, and models put an embedding layer between the input and the hidden layer ([[Block 5 Slides]], p. 78). Token vectors alone do not give word order: "dog bites man" and "man bites dog" use the same words ([[Block 5 Slides]], p. 131; [[F26-midterm-review-234p]], p. 177). See Tokenization.

**Position.** The model adds a position vector to each token vector, so the input keeps word order ([[Block 5 Slides]], p. 132; [[F26-midterm-review-234p]], p. 178). See Positional Encoding.

**Attention.** Attention reads context from other positions ([[Block 5 Slides]], p. 129). In a text generator, a Causal Mask limits each position to itself and earlier tokens ([[Block 5 Slides]], pp. 137–138; [[F26-midterm-review-234p]], pp. 183–184). Our reading: the phrase "every position reads every other position" holds for unmasked attention. In the decoder, each position reads only its allowed prefix.

Position, the causal mask, and the attention weights answer three separate questions: where a token is, which tokens are visible, and how much each token contributes ([[Block 5 Slides]], p. 139; [[F26-midterm-review-234p]], p. 185).

**Token MLP.** After attention gathers context, a position-wise MLP learns new combinations of the features: Linear, then a nonlinearity, then Linear ([[Block 5 Slides]], p. 141; [[F26-midterm-review-234p]], p. 187). It is a familiar feedforward network applied to one position, and its output is another feature vector for that token (same pages). The layer uses the same MLP weights at every position: "A shared MLP transforms each contextualized vector separately" ([[Block 5 Slides]], p. 142; [[F26-midterm-review-234p]], p. 188). "Attention gathers context; the MLP learns new feature combinations" ([[Block 5 Slides]], p. 141; [[F26-midterm-review-234p]], p. 187).

**Transformer block.** One block maps input vectors through causal attention, then the token MLP, to output vectors. Attention exchanges information across positions, and the MLP transforms the features within each position ([[Block 5 Slides]], p. 143; [[F26-midterm-review-234p]], p. 189). That slide leaves out the residual connections and LayerNorm for clarity ([[F26-midterm-review-234p]], p. 189). The full block is causal multi-head attention, then "+ input -> LayerNorm", then the MLP at each position, then "+ input -> LayerNorm" ([[Block 5 Slides]], p. 149; [[F26-midterm-review-234p]], p. 194). The shortcuts ([[Residual Connections]]) and the normalization help train the stack (same pages).

**Stacking.** A deeper model stacks L blocks. Later blocks work on features that earlier blocks already processed ([[Block 5 Slides]], p. 144). One attention layer can already read the whole allowed prefix; more blocks add learned processing steps at the cost of extra computation (p. 144). Each block has its own attention and MLP weights: same architecture, different weights, one jointly trained model ([[Block 5 Slides]], p. 145; [[F26-midterm-review-234p]], p. 190). "Depth counts blocks; generation length counts tokens" (same pages).

**Prediction head.** The prediction head turns the final transformed vector into scores for the next word ([[Block 5 Slides]], p. 146; [[F26-midterm-review-234p]], p. 191). Generation then follows Autoregressive Language Modeling.

**The Block 7 recall.** Block 7 calls the same model a "Transformer LM" ([[Block 7 Slides]], p. 241). Each layer has four sublayers: attention, a feed-forward neural network, layer normalization, and residual connections. "Each hidden vector looks back at the hidden vectors of the current and previous timesteps in the previous layer." "The language model part is just like an RNN-LM": at each position t, the figure shows a distribution p(w_t | h_t) over words (p. 241). See [[Recurrent Neural Networks (RNN)]] and [[Layer Normalization]].

### Encoder-only Transformers and masked language modeling

Block 7 sets an encoder-only Transformer next to the decoder-only model ([[Block 7 Slides]], p. 242). Each layer has four sublayers: non-causal attention, a feed-forward neural network, layer normalization, and residual connections. Each hidden vector looks at the hidden vectors of all timesteps in the previous layer (p. 242).

Synthesis: the two variants use the same layer. The difference is the mask. The decoder applies a Causal Mask, and the encoder applies none. So in the encoder, the phrase "every position reads every other position" holds.

**Masked language model (MLM) pretraining.** The encoder uses its distribution over words for MLM pretraining (p. 242). The slide gives the objective in two steps: "Rather than trying to predict the next word from the previous ones…" "…mask out a word (or a few words) and predict the missing words from the remaining ones" (p. 242). In the figure, the input is [CLS] [MASK] cat sat. The output at the masked position is p(w1 | h2), its target is "The", and the objective is J = log p(w1 | w2, w3) (p. 242).

Open point: the slide does not define its indices. It calls the masked word w1 but reads it from h2, the second position after [CLS]. The context words w2 and w3 are probably "cat" and "sat", but the slide does not say so.

Synthesis: next-word prediction (Autoregressive Language Modeling) uses only the words to the left. MLM predicts a masked word from the words on both sides. That is why the encoder needs non-causal attention.

**BERT.** "BERT popularized this encoder-only Transformer architecture and style of pretraining" ([[Block 7 Slides]], p. 242). BERT-Base has 110 million parameters, and BERT-Large has 340 million. A slide on the intrinsic dimension of fine-tuning (Aghajanyan et al., 2020) gives these numbers (p. 259). The deck uses BERT-Large as the pretrained model in its adapter results. The baseline fine-tunes only the top K layers of BERT-Large (pp. 246–248). See [[Adapters]] and [[Fine-Tuning]].

Open point: the text on pp. 246–248 names BERT-Large on all three pages. Only the plot on p. 246 has the label BERT_LARGE (GLUE). The plots on p. 247 (MNLI_m) and p. 248 (CoLA) have the label BERT_BASE.

Block 3 notes that BERT uses GELU; see Activation choice below.

### Scaling training

Parallel positions plus adjustable width and depth support large training runs ([[Block 5 Slides]], p. 151). Block 5 shows two ways to spread training over GPUs (p. 152):

- **Data parallelism**, for more data. Copy the model to each GPU, split the examples into batches, and synchronize the gradients so every copy gets the same update. The method also applies to other architectures. The slide cites the PyTorch DDP tutorial.
- **Model parallelism**, for a bigger model. Split large computations across GPUs as matrix shards, then combine the results. The slide cites Shoeybi et al. (2019), Megatron-LM.

Both methods need communication between GPUs (p. 152).

### Model sizes

Block 7 recalls a comparison of some large language models (LLMs) ([[Block 7 Slides]], p. 254):

| Model | Creators | Year | Training tokens | Parameters |
| --- | --- | --- | --- | --- |
| GPT-2 | OpenAI | 2019 | ~10 billion (40Gb) | 1.5 billion |
| GPT-3 (cf. ChatGPT) | OpenAI | 2020 | 300 billion | 175 billion |
| PaLM | Google | 2022 | 780 billion | 540 billion |
| Chinchilla | DeepMind | 2022 | 1.4 trillion | 70 billion |
| LaMDA (cf. Bard) | Google | 2022 | 1.56 trillion | 137 billion |
| LLaMA | Meta | 2023 | 1.4 trillion | 65 billion |
| LLaMA-2 | Meta | 2023 | 2 trillion | 70 billion |
| GPT-4 | OpenAI | 2023 | ? | Not disclosed |
| Gemini (Ultra) | Google | 2023 | ? | Not disclosed |
| Llama 3.1 | Meta | 2024 | 15 trillion | 405 billion |

Synthesis: size grows on two axes, parameters and training tokens. Chinchilla has 70 billion parameters, fewer than half of GPT-3's 175 billion. But it trains on about 4.7 times as many tokens (1.4 trillion against 300 billion). See Scaling Laws.

### Self-attention as a graph

Block 6 reads self-attention as a graph over tokens. The first version says every token attends to all other tokens through matrix calculation ([[Block 6 Slides]], p. 115). The extended version says each token attends to the allowed positions, and a causal mask excludes future tokens ([[Block 6 Slides Extended]], p. 122). Unmasked attention is a complete token graph. The causal mask makes the edges directional, so a query reads only its own and earlier positions ([[Block 6 Slides]], pp. 117–118; [[Block 6 Slides Extended]], pp. 124–125). The extended deck also compares the attention mask with a GNN neighborhood: both restrict information flow, but attention learns input-dependent mixing weights ([[Block 6 Slides Extended]], p. 121). See Attention and [[Graph Neural Networks]].

### Sequence transduction

The paper opens by contrasting itself with the dominant sequence transduction models, which use recurrent or convolutional networks with an encoder and a decoder (Topic Note - Sequence Transduction). A sequence transduction model converts one sequence into another; classification outputs one label instead. The encoder compresses the input into an internal representation, and the decoder generates the output one piece at a time (Topic Note - Sequence Transduction).

### Images as tokens

The ViT note says ViT cuts an image into fixed-size patches and treats each patch as a token, with no convolutions. With enough pre-training data it matches or beats CNNs (An Image is Worth 16x16 Words (note)). The reading list says VLMs, world models, and video models all inherit this tokenization (Fall 2026 Reading List, item 2).

**Token count is cost.** Patch size sets token count, and token count sets cost and latency (An Image is Worth 16x16 Words (note)). See Visual Token Count.

### Activation choice

BERT (Devlin et al., NAACL 2019) and GPT-3 (Brown et al., NeurIPS 2020) use GELU, not ReLU. Neither runs an ablation against ReLU; the comparison is in the Hendrycks and Gimpel preprint ([[Block 3 Slides]], pp. 81–82). The slides say GELU is smooth everywhere, and that Transformers rely on stable gradient flow; smoothness is not shown to be the cause of the gains (p. 80). A paper in the same deck argues for bringing ReLU back into LLMs for activation sparsity (pp. 83–84); see [[Activation Sparsity]].

## Related

- Attention
- Causal Mask: the one difference between the decoder-only and encoder-only layers
- Positional Encoding
- Autoregressive Language Modeling: the decoder's objective; MLM is the encoder's alternative
- Teacher Forcing: training scores all positions in one pass
- Tokenization
- [[Recurrent Neural Networks (RNN)]]
- [[Convolutional Neural Networks (CNN)]]
- [[Graph Neural Networks]]
- Vision Language Models (VLM)
- Visual Token Count
- KV Cache: reuse of attention keys and values during decoding
- [[Residual Connections]]
- [[Layer Normalization]]
- [[Activation Functions]]
- [[Activation Sparsity]]
- Scaling Laws: model size against training tokens
- [[Transfer Learning]]
- [[Fine-Tuning]]
- [[Adapters]]: Block 7 tests adapters on BERT
- LLMs and Graphs

## Sources

- Attention Is All You Need (note)
- Topic Note - Transformers
- Topic Note - Sequence Transduction
- An Image is Worth 16x16 Words (note)
- Fall 2026 Reading List, items 1–2
- [[Block 3 Slides]], pp. 80–84
- [[Block 5 Slides]], pp. 78, 129–152
- [[Block 6 Slides]], pp. 115–118
- [[Block 6 Slides Extended]], pp. 121–125
- [[Block 7 Slides]], pp. 241–242, 246–248, 254, 259
- [[F26-midterm-review-234p]], pp. 174–194: the midterm recap of the Block 5 text-generating Transformer
