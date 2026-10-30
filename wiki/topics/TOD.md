---
id: doc-spzb1b
type: topic
kind: entity
description: TOD is a tensor-based, multi-GPU outlier detection system (VLDB'23, Zhao, Chen, Jia) that turns diverse outlier detection algorithms into shared tensor operators and fits them in GPU memory with provable quantization, automatic batching, and multi-GPU support.
tags: [machine-learning/cs566-deeplearning, tool]
aliases: ["TOD: A Tensor-based, Multi-GPU OD System", Tensor-based Outlier Detection System, Tensor Transpilation Interface, Tensor transpilation, Provable quantization, (1 + ε)-property, (1+epsilon)-property]
created: 2026-10-12T16:58:10
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 7 Slides]]"]
up: ["[[Unsupervised Outlier Model Selection]]"]
---

> [!entity] Entity
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning · #tool
> Up: [[Unsupervised Outlier Model Selection]]

## What it is

TOD is "A Tensor-based, Multi-GPU OD System", published at VLDB'23 by Zhao, Chen, and Jia. The deck shows it under the heading "Building ML Systems for Scalable Learning" ([[Block 7 Slides]], p. 288). The slides call it the "1st Tensor-based GPU Outlier Detection System" (p. 291). OD means outlier detection.

TOD acts as a "transpiler" or "translator". On one side are diverse OD algorithms. On the other side are the learning systems that run neural nets on GPUs (p. 294). It has two parts. A tensor transpilation interface breaks each OD algorithm into a small set of shared tensor operators. Operator optimizations then make those operators fit in GPU memory (pp. 298-310).

Synthesis: the slide underlines "Zhao" in the author list (p. 288). Yue Zhao, the course instructor, lists a GitHub repository `pytod` (GPU-accelerated outlier detection). That is probably the code for TOD, but the Block 7 deck does not name the repository.

## Facts

### The problem: OD cost and data dependency

OD algorithms have high time and space complexity: "O(n^2) or higher" (p. 289).

| Algorithm | Time | Space |
| --- | --- | --- |
| kNN | $O(n^2)$ | $O(n^2)$ |
| COF | $O(n^3)$ | $O(n^2)$ |
| LOF | $O(n^2)$ | $O(n^2)$ |
| KDE | $O(n^3)$ | $O(n^2)$ |
| LOCI | $O(n^2)$ | $O(n^2)$ |
| OCSVM | $O(n^3)$ | $O(n^2)$ |

Source: [[Block 7 Slides]], p. 289.

Many OD algorithms also have a data dependency. For example, kNN outlier detection uses the distance to the k-th nearest neighbor as the outlier score. To compute pairwise distances, it needs "all samples" (p. 290; see [[k-Nearest Neighbors]]). Because of this dependency, OD algorithms do not run as "batches of tensor algebra" the way neural nets do (p. 294).

### The opportunity with GPUs

1. Deep neural networks succeeded as hardware improved. The slides give two examples: visual object recognition on ImageNet (2012) and AlphaFold protein structure prediction (2021) (p. 291; see [[ImageNet Large Scale Visual Recognition Challenge]]). Tensor operations (addition, product, convolution) give fast computation (p. 292).
2. Learning systems are mature. The slides name MXNet, DL4J, ONNX, PyTorch, TensorFlow, and PaddlePaddle, with "Deep optimization & Neural nets on GPUs" (p. 293).

The slides list two limits of existing OD GPU systems. Each implements only "*one* (family of) OD algorithm(s)", and none has deep optimization. In contrast, TOD (1) supports diverse OD algorithms through tensor transpilation and (2) uses GPUs and optimized GPU systems (p. 295).

### Challenge 1 and Solution 1: the tensor transpilation interface

The first challenge is to represent OD as tensor operations. TOD decomposes each OD algorithm into functional operators, and decomposes those into basic tensor operators (p. 296):

- ABOD → kNN and cosine similarity → topk, cdist, and basic OPs.
- LOF → nwr and density estimation → cdist, basic OPs, SVD, and histogram.

The slides make two notes. OD algorithms are decomposable as basic tensor operators for GPUs. The tensor operators are shared across algorithms, for example cdist (p. 297). Solution 1 is to "decompose *complex* and *diverse* OD algorithms into a small set of: *shared* basic tensor operators" (p. 298).

The interface has three layers (p. 299):

| Layer | Members |
| --- | --- |
| Outlier detection algorithms | kNNOD, ABOD, COF, LOF, LOCI, HBOS, SOD, COPOD, ECOD, FB, LSCP, MetaOD, SUOD, LODA, PCA, ... |
| Basic functional operators | kNN, shared neighbors, neighbors within range, cosine similarity, dimension reduction, density estimation |
| Basic tensor operators | cdist, topk, intersect, SVD, feature sampler, histogram, aggregation |

The slides give two advantages. Advantage 1: "lower implementation and optimization effort". Advantage 2: "extends to new fields and algorithms" (p. 299).

Synthesis: the slides do not define "nwr" on p. 296. It is probably "neighbors within range" from the functional-operator layer on p. 299. The algorithm list on p. 299 includes [[MetaOD]], the model-selection method from [[Unsupervised Outlier Model Selection]].

### Challenge 2: GPU memory

GPU memory is limited. An NVIDIA A100 has 80 GB of device memory. OD operators are costly: a distance matrix for 200k samples in 32-bit needs about 160 GB (p. 300).

Synthesis: the number checks out. $200{,}000^2 \times 4$ bytes $= 1.6 \times 10^{11}$ bytes, which is 160 GB, twice the memory of one A100.

### Solution 2: optimizations on basic operators

The slides list three optimizations (pp. 301, 310):

1. **Provable quantization:** "use lower precision, verify the result, recompute if needed" (p. 301).
2. **Automatic batching:** "split large operations into smaller ones" (p. 310).
3. **Multi-GPU support:** "deploy small batches onto multiple GPUs" (p. 310).

Together, automatic batching and multi-GPU support give "Divide and conquer with multi-GPUs". A large operation splits into batches. Each batch goes to a GPU (GPU 1, GPU 2, ...). A result-aggregation step then combines the outputs (p. 310).

### Provable quantization

Quantization saves memory but can change the result. In the slide's example, a 2×2 block in float16 (16×4 = 64 bits) is quantized to int8 (8×4 = 32 bits). This saves 50% of storage. The float16 sum is 34.2138 and the int8 sum is 33, which the slide calls a "4% difference" (p. 302).

The proposal asks: "For select operators, can we quantize them *without* accuracy change?" (p. 303). The slides give an example with $a = [1.011, 1.011]$ and the question $sum(a) > 2$, whose correct answer is yes (p. 304):

- Quantize to 2 decimals: $sum([1.01, 1.01]) = 2.02 > 2$. The result is correct.
- Quantize to 1 decimal: $sum([1.0, 1.0]) = 2$. The result is wrong "due to the large rounding error".

"The key is to quantify the rounding error in lower precisions!" (p. 304).

**The (1 + ε)-property.** The slides credit this error bound to Lee et al., 2018. It quantifies floating-point operation error at a precision α (for example, 64-bit), where x and y are floating-point numbers and the operator $*$ is one of $\{+, -, \times, /\}$. With proper conditions,

$$x \circledast y = (x * y)(1 + \delta), \quad |\delta| \le \epsilon$$

Here δ is the error in the operation between x and y, and ε bounds it. ε "is a constant that solely depends on the precision level α" (p. 305).

For selected operators, TOD uses the bound $x \circledast y = (x * y)(1 + \epsilon)$ and replaces δ by ε for the maximum error. TOD then asks whether the maximum low-precision error can change the output of the operator. If it cannot, "Quantization accuracy is provable" (p. 306).

The method has three steps (p. 307):

1. **Input quantization:** quantize the inputs to lower precision.
2. **Low-precision evaluation:** run the operator on the lower-precision inputs.
3. **Exactness verification:** verify accuracy with the (1 + ε)-property. If needed, fix the result by calculating again in higher precision.

The slides give two reasons why this suits OD operators. They often output ranks, indexes, and similar values, not floating-point numbers. They are mostly calculation-based, with "no *iterative* error propagation" (p. 308).

Synthesis and open points:

- The slides do not define $\circledast$. It reads as the computed floating-point result of $*$.
- With $|\delta| \le \epsilon$, the error can go in either direction. Writing $(1 + \epsilon)$ shows only the size of the worst case.
- In the p. 302 example, $(34.2138 - 33) / 34.2138 \approx 3.5\%$. The slide rounds this to 4%.
- Some example values, such as 18.4123, have more digits than float16 holds. The example is an illustration, not an exact float16 calculation.
- The deck gives no full reference for Lee et al., 2018.
- The deck reports no speedup or accuracy results for TOD.

## Related

- [[Unsupervised Outlier Model Selection]]: the same deck's work on choosing an OD model without labels
- [[MetaOD]]: one of the OD algorithms in TOD's top layer (p. 299)
- Yue Zhao: the course instructor, whose pinned repositories include `pytod`
- [[k-Nearest Neighbors]]: kNN distance is the slides' example of OD data dependency
- [[Evolution of Machine Learning]]: the compute and systems tracks that TOD builds on
- [[ImageNet Large Scale Visual Recognition Challenge]]
- [[Visual Anomaly Detection]]: anomaly detection on images, a neighbor task

## Sources

- [[Block 7 Slides]], pp. 288-310
