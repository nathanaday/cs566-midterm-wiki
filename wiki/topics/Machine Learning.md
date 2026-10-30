---
id: are-kbdt2s
type: topic
kind: overview
description: "Machine learning and machine perception: the concepts, models, and papers that the courses and the self-study notes share, such as transformers, vision-language models, world models, and vision-language-action models."
tags: []
aliases: [ML, Machine Perception]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: []
defines: machine-learning
---

> [!overview] The page of #machine-learning
> 0 sources · refreshed 2026-09-28

## Summary

Machine learning and machine perception: the concepts, models, and papers that the courses and the self-study notes share, such as transformers, vision-language models, world models, and vision-language-action models.

## Context

General machine learning knowledge: concepts, model families, and paper notes. It holds the self-study notes on machine perception and decision making, and every concept that more than one course or project uses.

Course material lives in the child areas, such as [[CS566-DeepLearning]].

## Main threads

The self-study notes follow the owner's interests: world models, vision-language models, and machines that reason about and act in their surroundings. With a background in condition monitoring and fire detection, the owner wants to analyze sensor data, including images and video, for anomaly detection and safety suggestions, on fleets of edge sensors (Learning Goals, § Interests). A main goal is to read industry papers comfortably (Learning Goals, § Papers).

1. **Reading path.** Fall 2026 Reading List orders 13 papers and 4 optional companions: the Transformer and ViT, then vision backbones and VLMs, then world models, then VLAs, edge VLMs, and anomaly detection.
2. **[[World Models]].** A world model predicts the outcomes of actions, so a system can plan by search (Topic Note - World Models, § About). The line runs from Ha & Schmidhuber to DreamerV3 (Fall 2026 Reading List, items 7–8). The sources disagree on the prediction target: the core Cosmos models are video predictors (Topic Note - NVIDIA COSMOS, § About), while the V-JEPA 2 and LeCun notes argue for prediction in representation space (V-JEPA 2 (note), § Summary; A Path Towards Autonomous Machine Intelligence (note), § What To Read For). See also [[NVIDIA Cosmos]] and [[World Action Models]].
3. **[[Vision Language Models (VLM)]] and [[Visual Token Count]].** The reading list calls visual token count, not parameter count, the real constraint on edge multimodal work (Fall 2026 Reading List, item 12). The FastVLM note says time-to-first-token is mostly encoder latency plus prefill over visual tokens (FastVLM (note), § Summary), and the SmolVLM note puts the savings in token compression, not in a smaller language model alone (SmolVLM (note), § Summary).
4. **[[Visual Anomaly Detection]].** The reading list calls CLIP the foundation of nearly all zero-shot visual anomaly detection (Fall 2026 Reading List, item 4). WinCLIP scores patches with CLIP prompts and a sliding window (WinCLIP (note), § Summary), and frozen DINOv2 features carry the dense spatial information that patch-level scoring needs (DINOv2 (note), § What To Read For).
5. **[[Vision Language Action Models]].** Actions become tokens that a language model outputs: RT-2 writes actions as text strings (RT-2 (note), § Summary), and OpenVLA bins each action dimension into 256 tokens (OpenVLA (note), § Summary). The Sep 21 guest lecture adds that lighting has a large effect on VLA policy training (Guest Lecture 9-21 Notes (part 1)).

Foundations: [[Transformers]], [[Recurrent Neural Networks (RNN)]], [[Convolutional Neural Networks (CNN)]]. Also here: [[Jev]], a model that returns typed values with probabilities instead of text (Jev (AI model) - Wikipedia).

## Gaps

- Claims about papers rest on pre-reading summaries. No paper is in the vault, and every paper note was unread at capture.
- Topic notes that were empty or one line long were not captured: VAE, VLM, VLA, World Action Models, NeRF, Skills, and Subagents.
- The Jev claims come from one Wikipedia clip and are mostly the company's own.
- Open threads: ITL EFD physics-informed fire-risk detection and Write up Physical AI and Physics Informed AI.

## Map

```base
filters:
  and:
    - file.inFolder("tool/source-core/documents")
    - 'file.hasTag("machine-learning", "machine-learning/cs566-deeplearning", "machine-learning/cs566-deeplearning/cs566-course", "machine-learning/cs566-deeplearning/cs566-project", "machine-learning/cs566-deeplearning/cs566-project/autonomous-vehicle-sandbox", "machine-learning/cs566-deeplearning/cs566-project/kqiao-cs566-project-repo")'
views:
  - type: table
    name: Map
    groupBy:
      property: type
      direction: ASC
    order:
      - file.name
      - description
      - status
      - refreshed
```
