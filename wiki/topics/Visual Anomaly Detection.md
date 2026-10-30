---
id: con-pxtr0e
type: topic
kind: concept
description: Finding defects or unusual states in images, often with no anomalous training examples, using CLIP prompts, WinCLIP, frozen DINOv2 features, or GAN-based reconstruction such as GANomaly.
tags: [machine-learning]
aliases: [zero-shot anomaly detection, industrial anomaly detection]
created: 2026-09-28T00:00:00
updated: 2026-10-19T18:32:33
refreshed: 2026-10-19T18:32:33
status: stable
sources: ["Learning Goals", "CLIP (note)", "WinCLIP (note)", "DINOv2 (note)", "Genie (note)", "Fall 2026 Reading List", "Block 8 Slides"]
---

> [!concept] Concept
> 7 sources · refreshed 2026-10-19 · #machine-learning

## Definition

Visual anomaly detection finds defects or unusual states in images, often without training examples of each anomaly. The owner has a background in condition monitoring and fire detection, and names anomaly detection on sensor images and video as a goal (Learning Goals).

## Explanation

The WinCLIP note describes detection with no anomalous training image, or with only a few normal images (WinCLIP (note)). Synthesis: labeled anomalies are rare, so methods of this kind fit the problem.

### Approaches in the vault

- **Text prompts with CLIP.** Any class that you can describe in words is a zero-shot class. Accuracy depends heavily on scale and on prompt wording (CLIP (note)). The reading list calls CLIP the foundation of nearly all zero-shot visual anomaly detection (Fall 2026 Reading List, item 4).
- **WinCLIP.** A compositional prompt ensemble describes normal and defective states. A sliding window scores local patches, so defects can be segmented and not only detected. A few-shot variant stores reference features from a few normal images. Results on MVTec-AD are strong with no anomaly supervision (WinCLIP (note)).
- **Frozen self-supervised features.** DINOv2 features carry dense spatial information, which makes patch-level anomaly scoring possible (DINOv2 (note)). The reading list calls DINOv2 embeddings a strong default backbone for anomaly detection on sensor imagery (Fall 2026 Reading List, item 3).
- **GAN-based reconstruction.** GANomaly trains on normal images only. It encodes an image, decodes it, and encodes the reconstruction again. "Disagreement between the two codes becomes the anomaly score", and "Larger disagreement between z and ẑ is evidence to investigate further" (Block 8 Slides, pp. 236, 238). The slides list AnoGAN (2017), ALAD (2018), and GANomaly (2019) as GAN-based methods. Their shared idea: "use generator & discriminator to improve distribution learning (of the normal samples)" (p. 239). See Generative Adversarial Network.

### Known weaknesses to check

- Prompts can stop describing a real defect class (WinCLIP (note)).
- Window scoring can miss small or low-contrast defects (WinCLIP (note)).
- The reading list expects WinCLIP to show where VLMs are still weak on industrial imagery (Fall 2026 Reading List, item 13).

### Open questions

- How does WinCLIP compare with a supervised detector and with a frozen DINOv2 feature-distance baseline on the same data? The WinCLIP note proposes this comparison (WinCLIP (note)). No source in the vault reports the result.
- The reading list calls Genie's latent actions from unlabeled video the most transferable idea for the owner's video of scenes that change (Fall 2026 Reading List, item 10). The Genie note asks what a learned latent action would mean for a fixed camera that watches a scene change with no agent acting (Genie (note)). No source tests this for anomaly detection.

## Related

- [[Vision Language Models (VLM)]]
- [[World Models]]
- [[Visual Token Count]]
- [[Contrastive Learning]]
- GANomaly: GAN-based anomaly detection trained on normal images

## Sources

- Learning Goals
- CLIP (note)
- WinCLIP (note)
- DINOv2 (note)
- Genie (note)
- Fall 2026 Reading List, items 3, 4, 10, 13
- Block 8 Slides, pp. 236–239: GANomaly and the GAN-based methods
