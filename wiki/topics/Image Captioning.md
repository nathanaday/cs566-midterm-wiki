---
id: con-ddn7wb
type: topic
kind: concept
description: The task of generating a sentence that describes an image, one word at a time; the classic model feeds CNN image features into the first hidden state of an RNN language model.
tags: [machine-learning/cs566-deeplearning]
aliases: [CNN-RNN Image Captioning, CNN + RNN captioning, Image captioning with CNN + RNN]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 5 Slides]]", "[[Block 7 Slides]]"]
up: ["[[Recurrent Neural Networks (RNN)]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Recurrent Neural Networks (RNN)]]

## Definition

Image captioning maps one image to a sequence of words. It is a one-to-many task ([[Block 5 Slides]], p. 23). The model generates the description one word at a time, for example "A person throws a frisbee" (p. 123).

## Explanation

### Output length varies

In the worked example, one image gives "A big house" in three steps. A second image gives "A car on a tree" in five steps ([[Block 5 Slides]], pp. 33–34).

### CNN encoder, RNN decoder

The deck builds a captioning model from a CNN and an RNN ([[Block 5 Slides]], pp. 154–166):

1. A [[Convolutional Neural Networks (CNN)|CNN]] of Conv, Pool, and FC layers processes the image. The last FC layer and the softmax are removed (pp. 155–156, 161–166).
2. The output of the remaining FC layer feeds into the first RNN hidden state $h_1$. The first input $x_0$ is a zero vector (pp. 157–158, 161–166).
3. Each hidden state $h_t$ produces an output $y_t$, a word. $h_1$ gives the first word, "I" (pp. 159–160).
4. The generated word becomes the next input. For example, $y_2$ is fed back as $x_2$ (pp. 160, 163).
5. The example caption "I look better than Tom Cruise ." takes seven steps ($h_1$ to $h_7$). The last output is a period token that ends the sentence (p. 166).

The slides cite Mao et al. (Multimodal RNNs), Karpathy and Fei-Fei (Deep Visual-Semantic Alignments), Vinyals et al. (Show and Tell), Donahue et al. (Long-term Recurrent Convolutional Networks), and Chen and Zitnick (p. 154).

Synthesis: steps 3 and 4 are the generation loop of [[Autoregressive Language Modeling]], with the image in the first hidden state.

### Pretrained parts

[[Block 7 Slides]] uses the CNN + RNN captioning model as evidence that "Transfer learning with CNNs is pervasive… (it's the norm, not an exception)" (pp. 205-207). Its figure comes from Karpathy and Fei-Fei, "Deep Visual-Semantic Alignments for Generating Image Descriptions", CVPR 2015 (p. 205). See [[Transfer Learning]].

- The CNN is a "CNN pretrained on ImageNet" (p. 206). See [[ImageNet Large Scale Visual Recognition Challenge]].
- The word vectors at the RNN inputs are "pretrained with word2vec" (p. 207).
- In this figure, the CNN output enters the hidden state through a weight $W_{hi}$. The inputs are START, "straw", and "hat". The outputs are "straw", "hat", and END (p. 205).

The slides do not say whether the pretrained parts stay frozen or are fine-tuned on captions. This figure starts with a START token, but [[Block 5 Slides]] uses a zero vector as $x_0$ (pp. 157–158). The two decks use different figures, and neither explains the difference.

### Successes and failures

- Good captions: "A cat sitting on a suitcase on the floor", "A dog is running in the grass with a frisbee", "Two giraffes standing in a grassy field", "A man riding a dirt bike on a dirt track" ([[Block 5 Slides]], p. 167).
- Failures (p. 168):

| Image | Caption |
| --- | --- |
| a woman in a fur coat | A woman is holding a cat in her hand |
| a spider web | A bird is perched on a tree branch |
| a person doing a handstand | A woman standing on a beach holding a surfboard |
| a person holding a phone | A person holding a computer mouse on a desk |
| a player diving to catch a ball | A man in a baseball uniform throwing a ball |

A fluent caption can still be wrong. "Feedback into the model explains generation, not correctness" (p. 82).

### One pooled vector is a bottleneck

- "Each next word can draw on different image regions" ([[Block 5 Slides]], p. 123). The slide cites Xu et al. (2015) for the attention mechanism.
- With one pooled feature vector, the decoder state (c, h) must predict the next word from one summary. "One pooled summary forces the entire scene into one vector" (p. 124).
- A separate vector for each region avoids this: "Separate region vectors avoid forcing all parts together" (p. 125).

Synthesis: this is the same fixed-state limit as in [[Sequence to Sequence]]. Modern systems read many visual tokens instead; see [[Vision Language Models (VLM)]].

## Related

- [[Recurrent Neural Networks (RNN)]]
- [[Convolutional Neural Networks (CNN)]]
- [[Autoregressive Language Modeling]]
- [[Sequence to Sequence]]
- [[Question Answering]]: visual question answering uses the same CNN features
- [[Vision Language Models (VLM)]]
- [[CLIP]]
- [[Transfer Learning]]: the CNN and the word vectors are both pretrained

## Sources

- [[Block 5 Slides]], pp. 23, 33–34, 82, 123–125, 154–168
- [[Block 7 Slides]], pp. 205-207
