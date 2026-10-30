---
id: con-f0cr58
type: topic
kind: concept
description: A training method that pulls matched pairs together and pushes mismatched pairs apart in a shared embedding space; CLIP applies it to image-text pairs with a symmetric cross-entropy over the batch similarity matrix.
tags: [machine-learning]
aliases: [Contrastive Objective, contrastive loss, CLIP loss, symmetric contrastive loss, image-text contrastive loss, joint embedding space, sigmoid loss, SigLIP loss, sigmoid image-text pairing]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: ["CLIP (note)", "CSCI 566 Syllabus", "DINOv2 (note)", "V-JEPA 2 (note)", "[[Block 4 Slides]]"]
---

> [!concept] Concept
> 5 sources · refreshed 2026-09-28 · #machine-learning

## Definition

Contrastive learning trains a model to tell correct pairs from incorrect pairs ([[Block 4 Slides]], p. 238). For images and text, it learns a joint embedding space in which an image and the text that describes it lie close together. Training reduces the distance between correct image-text pairs and increases the distance between incorrect pairs ([[Block 4 Slides]], p. 240). The CLIP note gives the same description (CLIP (note), § Summary).

## Explanation

### The CLIP loss

[[CLIP]] takes a batch of N image-text pairs. It encodes the images to I1..IN and the captions to T1..TN, and scores every image against every caption with Ii·Tj. The result is an N x N matrix. The matching pairs lie on the diagonal, and every other cell in the batch is a negative ([[Block 4 Slides]], pp. 244-245, 247). The logits are cosine similarity times a learned scale exp(t) ([[Block 4 Slides]], p. 248).

The loss is symmetric:

- **Row loss (image to caption).** A softmax over each row, so each row sums to 1, then cross-entropy against the matching caption ([[Block 4 Slides]], p. 249).
- **Column loss (caption to image).** A softmax over each column, so each column sums to 1, then cross-entropy against the matching image ([[Block 4 Slides]], p. 250).
- **Total.** L = (L_row + L_col) / 2 ([[Block 4 Slides]], p. 251).

So CLIP learns retrieval in both directions ([[Block 4 Slides]], pp. 245-246, 251). Synthesis: each row and each column is a [[Loss Functions|cross-entropy]] classification. The correct class is the matching partner, and the other classes are the rest of the batch.

**Toy example** ([[Block 4 Slides]], pp. 248-251, citing Radford et al., ICML 2021, Fig. 3). The toy uses a scale of 5 in place of exp(t); for example, a cosine of 0.8 gives 0.8 x 5 = 4.0.

| Logits | "a cat" | "a dog" |
|---|---|---|
| cat image | 4.0 | 1.0 |
| dog image | 0.5 | 4.5 |

- Row softmax: cat .953 / .047, dog .018 / .982. Mean cross-entropy .0334 ([[Block 4 Slides]], p. 249).
- Column softmax: "a cat" .971 / .029, "a dog" .029 / .971. Mean cross-entropy .0298 ([[Block 4 Slides]], p. 250).
- Total loss: (.0334 + .0298) / 2 = .0316 ([[Block 4 Slides]], p. 251).

### Why contrastive, not caption prediction

In the CLIP study, a contrastive objective learned zero-shot ImageNet accuracy more efficiently than objectives that predict the caption. After 400M images processed, bag-of-words contrastive (CLIP) reached about 40%, bag-of-words prediction about 27%, and a Transformer language model about 16% ([[Block 4 Slides]], p. 259). The slides limit the comparison to these objectives, models, and data, and note that image-caption pairs still supply supervision ([[Block 4 Slides]], p. 259).

### Sigmoid pairing (SigLIP 2)

SigLIP 2 (Tschannen et al., 2025) uses sigmoid image-text pairing: one binary decision per cell of the matrix ([[Block 4 Slides]], p. 278). A matching pair such as (cat, "a cat") gets target y = 1, and a non-matching pair such as (cat, "a dog") gets y = 0 ([[Block 4 Slides]], p. 278). The probabilities in a row need not sum to 1: a logit of 2 in two cells of a row gives σ(2) = .881 in each ([[Block 4 Slides]], p. 279). For a negative pair, the loss pushes its logit down ([[Block 4 Slides]], p. 279).

Synthesis: in the softmax loss, the cells of a row compete for one unit of probability. In the sigmoid loss, the model scores each cell on its own.

### Where the course goes next

The slides say the course covers contrastive learning in more depth later ([[Block 4 Slides]], p. 238). The syllabus lists self-supervised learning for week 11 (Nov 9) (CSCI 566 Syllabus), and the Block 4 slides also place self-supervised objectives in week 11 ([[Block 4 Slides]], p. 230).

Open question:

- How does contrastive learning compare with the self-supervised methods in DINOv2 (note) and V-JEPA 2 (note)? The CLIP note lists DINOv2 under "Compare with" (CLIP (note), § Related).

## Related

- [[CLIP]]
- [[Vision Language Models (VLM)]]
- [[Visual Anomaly Detection]]
- [[Loss Functions]]
- [[Pretrained Visual Encoders]]

## Sources

- [[Block 4 Slides]], pp. 238-251, 259, 278-279
- CLIP (note) (pre-reading summary, not the paper)
- CSCI 566 Syllabus
- DINOv2 (note), V-JEPA 2 (note): named for comparison only
