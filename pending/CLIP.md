---
id: ent-asc9cn
type: topic
kind: entity
description: OpenAI's image-text model (Radford et al., ICML 2021) that trains an image encoder and a text encoder with a contrastive loss on 400M internet image-text pairs, so it can classify images zero-shot from text prompts.
tags: [machine-learning]
aliases: [Contrastive Language-Image Pre-training, Learning Transferable Visual Models From Natural Language Supervision, Radford et al. 2021, CLIP paper, CLIP ViT-L, CLIP-ViT, CLIP-ResNet]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: ["[[Block 4 Slides]]", "CLIP (note)"]
---

> [!entity] Entity
> 2 sources · refreshed 2026-09-28 · #machine-learning

## What it is

CLIP is an image-text model from OpenAI. Its paper is by Radford, Kim, Hallacy, Ramesh, Goh, Agarwal, Sastry, Askell, Mishkin, Clark, Krueger, and Sutskever, at ICML 2021 ([[Block 4 Slides]], p. 236). CLIP trains vision models from natural language descriptions instead of fixed class labels ([[Block 4 Slides]], p. 237). The goal is a general-purpose vision model that learns concepts directly from text, which enables zero-shot learning ([[Block 4 Slides]], p. 237).

## Facts

### Training

- **Data.** 400M image-text pairs from the internet, not a labeled dataset ([[Block 4 Slides]], pp. 237, 260).
- **Encoders.** The image encoder is ResNet-based or ViT-based. The text encoder is a Transformer, similar to GPT-2 ([[Block 4 Slides]], pp. 257, 260). See [[Vision Transformer (ViT)]].
- **Recipe.** Batch size 32,768, 32 epochs, cosine learning rate decay ([[Block 4 Slides]], p. 260).
- **Objective.** [[Contrastive Learning|Contrastive]]. For a batch of N pairs, CLIP encodes the captions to T1..TN and the images to I1..IN, and scores every pair with Ii·Tj. The N x N matrix has the matching pairs on the diagonal; every other cell is a negative ([[Block 4 Slides]], pp. 242-245). The logits are cosine similarity times a learned scale exp(t) ([[Block 4 Slides]], p. 248). The loss averages a cross-entropy over the rows (image to caption) and over the columns (caption to image) ([[Block 4 Slides]], pp. 249-251). [[Contrastive Learning]] works through the slides' toy example.

### Why a contrastive objective

The slides compare objectives by zero-shot ImageNet accuracy after 400M images processed. A bag-of-words contrastive objective (CLIP) reaches about 40%, bag-of-words prediction about 27%, and a Transformer language model that predicts the caption about 16% ([[Block 4 Slides]], p. 259). Contrastive training is about 4x more efficient than bag-of-words prediction, which is about 3x more efficient than the Transformer language model ([[Block 4 Slides]], p. 259). The slides limit this result to these objectives, models, and data, and note that image-caption pairs still supply supervision ([[Block 4 Slides]], p. 259).

### Zero-shot classification

1. Put each class name (plane, car, dog, ..., bird) into a prompt template such as "A photo of a {object}." ([[Block 4 Slides]], pp. 252-253).
2. Encode each prompt with the text encoder to get T1..TN ([[Block 4 Slides]], p. 254).
3. Encode the image to get I1. Compute I1·T1 ... I1·TN and pick the label with the highest score, for example "A photo of a dog." ([[Block 4 Slides]], pp. 255-257).

CLIP needs no training on the target categories ([[Block 4 Slides]], p. 245). It only ranks the text candidates that you supply, such as "a cat", "a dog", "a bicycle" ([[Block 4 Slides]], p. 274). For free-form answers, see [[Vision Language Models (VLM)]]. The CLIP note says any class that you can describe in words becomes a zero-shot class (CLIP (note), § Summary).

Prompt wording changes accuracy. Compared with contextless class names, prompt engineering and ensembling add about 5 points of average score at RN50x16 (75.3 GFLOPs) ([[Block 4 Slides]], p. 268). RN101 with prompts (9.9 GFLOPs) matches RN50x4 with bare class names (21.5 GFLOPs), about a 4x efficiency gain ([[Block 4 Slides]], p. 268). The CLIP note also says accuracy depends heavily on prompt wording (CLIP (note), § Summary).

### Results

- **Linear probe.** Averaged over 27 datasets, CLIP-ViT models (B/32 to L/14@336px, about 85%) score above EfficientNet-NoisyStudent, BiT, SimCLRv2, BYOL, MoCo, ViT (ImageNet-21k), and ResNet at comparable forward-pass GFLOPs ([[Block 4 Slides]], p. 263). See [[Pretrained Visual Encoders]] for the method.
- **Transfer against ImageNet score.** CLIP models lie near the y = x line. Other models, for example EfficientNet-NoisyStudent, have transfer scores well below their ImageNet scores (linear probe average over 26 datasets) ([[Block 4 Slides]], p. 264).
- **Zero-shot against a supervised baseline.** Zero-shot CLIP matches a fully supervised linear-probe ResNet-50 across the evaluation suite ([[Block 4 Slides]], p. 266). It gains most on StanfordCars (+28.9), Country211 (+23.2), and Food101 (+22.5). It loses most on EuroSAT (-37.1), KITTI Distance (-34.0), and PatchCamelyon (-19.5). On ImageNet it is +1.9 and on MNIST -10.0 ([[Block 4 Slides]], p. 266).
- **Zero-shot against few-shot.** Zero-shot CLIP, at an average score of about 62%, is as good as 4-shot linear-probe CLIP and 16-shot BiT-M ([[Block 4 Slides]], p. 267).

### Robustness to distribution shift

On ImageNet, CLIP ViT-L and an ImageNet-trained ResNet101 both score 76.2%. On shifted versions of ImageNet, CLIP keeps far more accuracy ([[Block 4 Slides]], p. 258):

| Test set | ResNet101 | CLIP ViT-L |
|---|---|---|
| ImageNet | 76.2% | 76.2% |
| ImageNet V2 | 64.3% | 70.1% |
| ImageNet Rendition | 37.7% | 88.9% |
| ObjectNet | 32.6% | 72.3% |
| ImageNet Sketch | 25.2% | 60.2% |
| ImageNet Adversarial | 2.7% | 77.1% |

The slides also use 7 natural distribution shift datasets from Taori et al.: ImageNetV2, ImageNet-A, ImageNet-R, ImageNet Sketch, ObjectNet, ImageNet Vid, and Youtube-BB ([[Block 4 Slides]], p. 270). An ideal robust model lies on y = x, where shift accuracy equals ImageNet accuracy. Zero-shot CLIP lies much closer to this line than standard ImageNet training or existing robustness techniques ([[Block 4 Slides]], p. 270).

### Limitations

The slides list these ([[Block 4 Slides]], p. 272):

- Zero-shot performance is well below the state of the art on some tasks.
- It is weak on abstract tasks such as counting.
- It is poor on out-of-distribution data such as MNIST.
- It is open to adversarial attacks.
- Methodology concerns: the choice of datasets in the evaluation suite, and the use of large validation sets for prompt engineering.
- It shows social biases.

### Code

The openai/CLIP GitHub repository has a PyTorch implementation, a Colab notebook, references for zero-shot prediction and linear probes, the YFCC100M dataset, and released models ([[Block 4 Slides]], p. 273). Its README says CLIP matches the original ResNet50 on ImageNet zero-shot without any of the 1.28M labeled examples ([[Block 4 Slides]], p. 273).

## Related

- [[Contrastive Learning]]
- [[Vision Language Models (VLM)]]
- [[Vision Transformer (ViT)]]
- [[Pretrained Visual Encoders]]
- [[Visual Anomaly Detection]]

## Sources

- [[Block 4 Slides]], pp. 236-274 (CSCI 566 lecture on CLIP)
- CLIP (note) (pre-reading summary, not the paper)
