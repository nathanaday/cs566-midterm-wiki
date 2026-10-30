---
id: con-kc4dvj
type: topic
kind: concept
description: A recurrent model carries one fixed-width state through time, while attention keeps a per-layer KV cache that grows with the history; sequence architectures sit on a spectrum between these two ends.
tags: [machine-learning/cs566-deeplearning]
aliases: [Fixed State vs. Growing History, Compress or Re-read, Compress vs. Re-read, Fixed-Width State, Stronger Recurrence, Modern Recurrence]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 5 Slides]]"]
up: ["[[Recurrent Neural Networks (RNN)]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Recurrent Neural Networks (RNN)]]

## Definition

The Block 5 deck compares two ways for a model to hold the past while it decodes ([[Block 5 Slides]], pp. 224–226):

- **Recurrent state:** one state flows through the cells, starting from $h_0$. The sequence gets longer, but "the carried state width stays fixed" (p. 225).
- **Per-layer KV cache:** each layer stores a key (K) and a value (V) for each processed token (p. 224). The history "adds slots each row", so the cache at $t=8$ is larger than the cache at $t=2$ (p. 226).

The deck adds: "Memory scaling differs; model quality is a separate question" (p. 226).

## Explanation

The deck marks pp. 223–230 as "optional extensions to the introductory examples", to return to "after learning how attention reads context" ([[Block 5 Slides]], p. 223).

### The compress-or-re-read spectrum

The deck places four model families on one line, from "compressed state" to "direct access to more tokens" ([[Block 5 Slides]], p. 227):

| Position | Family | What the deck says |
|---|---|---|
| Compressed end | RNN | Constant-size decode state |
| | SSM (state space model) | Constant-size decode state |
| Middle | Hybrid (HYB) | Periodic attention access |
| Direct-access end | Attention (ATTN) | Direct access to more tokens |

"Efficiency comes from what the model stores and can revisit" (p. 227). The deck does not define the SSM further. It only places the SSM beside the RNN.

### Two design paths for modern recurrence

The deck names two paths ([[Block 5 Slides]], p. 228):

| Path | Idea | Examples in the deck |
|---|---|---|
| Stronger recurrence | "richer state updates without full history" | xLSTM scaling study; Mamba-3: "complex + MIMO" |
| Hybrid layers | "fixed-state layers plus periodic direct access" | Qwen3-Next: "3:1 mix"; Kimi Linear: "KDA + MLA" |

The deck gives one line for each model. It warns: "Mechanisms are documented; benchmark claims remain source-specific" (p. 228). This page adds no detail about these models beyond those lines. [[Hybrid Recurrent-Attention Models]] covers the hybrid path.

### RNN and LSTM in 2026

The deck puts "STATE" at the center of four points ([[Block 5 Slides]], p. 230):

- **Foundation:** shared parameters and gated credit paths.
- **Current niche:** streaming ASR and low-latency decode.
- **Modern return:** xLSTM and SSMs strengthen recurrence.
- **Hybrid path:** mostly state, plus selective attention.

Its rule for comparing architectures: "Ask what state is stored, what can be revisited, and at what cost" (p. 230).

### Synthesis

This part is not from the deck. The [[KV Cache]] page records that caching "does not make history free" ([[Block 3 Slides]], p. 58). A recurrent state is the other end of that trade: its memory stays bounded as the sequence grows. The deck leaves open whether that bound costs model quality (p. 226).

## Related

- [[KV Cache]]: the growing history at the attention end
- [[Transformers]]
- [[Recurrent Neural Networks (RNN)]]: the fixed state at the compressed end
- [[Long Short-Term Memory]]
- [[Hybrid Recurrent-Attention Models]]: the middle of the spectrum
- [[Autoregressive Language Modeling]]

## Sources

- [[Block 5 Slides]], pp. 223–230
