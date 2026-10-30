---
description: How many leaves and how much depth a decision tree can have as a function of the number of attributes k and the number of training samples N, for binary attributes (2^k leaves, depth k) and for continuous attributes (N leaves, depth N-1), and why those sizes matter for overfitting, stopping, and pruning.
aliases: [Maximum depth of a decision tree, Maximum number of leaves, Decision tree depth, Decision tree capacity, Tree size, Tree size bounds]
sources: ["[[Block 2 Slides]]", "[[F26-midterm-review-234p]]", "[[CSCI 566 Midterm (Spring 2024)]]"]
subject: 1 Foundations and classical machine learning
---

## Definition

The size of a decision tree is its number of leaves and its depth. The sample midterm defines depth as "the maximum number of nodes between the root and any of the leaf nodes (including the leaf, not the root)" ([[CSCI 566 Midterm (Spring 2024)]], Q27), so a decision stump has depth 1. With $k$ binary attributes, a tree has at most $2^k$ leaves and depth at most $k$. With continuous attributes and $N$ training samples, a tree has at most $N$ leaves and depth at most $N - 1$. The decks give the facts these bounds rest on, and this topic derives the bounds from them.

## Explanation

[[Decision Trees]] covers how a tree is learned, when it stops, and how it is pruned. This topic asks a narrower question: how big can the tree get? The answer depends on whether an attribute can be reused on a path from the root to a leaf.

### What the Decks Say

The decks do not state a leaf count or a depth bound. They give three facts that fix the bounds:

1. Stopping condition 2 stops a branch when it has "Already split on all features". In the loan example, the 5-year node (4 safe / 3 risky) stops for this reason: Credit, Income, and Term have all been tested on its path ([[Block 2 Slides]], p. 65).
2. For a continuous feature, the tree splits at a threshold, and "For threshold splits, same feature can be used multiple times". The example splits on $x[1]$ at $-0.07$ and again at $-1.66$ on the same path ([[Block 2 Slides]], pp. 74–76).
3. "The tree size can be controlled by the number of levels", shown with scikit-learn's `DecisionTreeRegressor(max_depth=n)` ([[Block 2 Slides]], p. 91; repeated in [[F26-midterm-review-234p]], p. 15).

Fact 1 bounds a tree on discrete attributes by $k$. Fact 2 removes that bound, so a tree on continuous attributes is limited by the data instead. Fact 3 says depth is the knob the course uses to control size.

### Binary Attributes

Synthesis: with binary attributes, a test on an attribute sends every sample with value 0 one way and every sample with value 1 the other way. Testing the same attribute again lower on that path separates nothing, since all samples in the node already share that value. Each attribute therefore appears at most once on any root-to-leaf path, which is what stopping condition 2 enforces ([[Block 2 Slides]], p. 65).

A path can hold at most $k$ tests, one per attribute. Under the exam's definition of depth, a path with $k$ internal nodes and one leaf has $k - 1$ internal nodes below the root plus the leaf, so its depth is $k$. The maximum depth is $k$, written $O(k)$ on the exam.

The leaf count follows from the depth. Each test has two outcomes, so a complete tree with $k$ levels of tests has $2^k$ leaves. No tree on $k$ binary attributes can have more, because every leaf sits at the end of a distinct path and there are only $2^k$ distinct assignments of values to the $k$ attributes.

Synthesis: a leaf that holds no training sample is never created by the greedy learner, so the leaf count is also at most $N$. The exam sets $k \ll N$ and asks for the bound in terms of the attributes, so $2^k$ is the intended answer. For the loan data, $k = 3$ gives at most 8 leaves and depth 3. The learned tree has 6 leaves and depth 3 ([[Block 2 Slides]], p. 62), under both bounds.

### Continuous Attributes

Synthesis: a threshold split on a continuous attribute can be placed between any two distinct values, so one attribute supports many splits on one path ([[Block 2 Slides]], p. 76). The number of attributes no longer limits the tree. What limits it is the data: a split is only useful if it separates at least one sample from the rest, so every internal node has at least one sample on each side, and every leaf holds at least one sample.

With $N$ samples and one sample per leaf, the tree has at most $N$ leaves. Every leaf is then pure, and training error is zero.

The deepest tree is a chain. The root peels one sample off into a leaf and sends the other $N - 1$ down. The next node peels off one more, and so on, until the last internal node splits the final two samples into two leaves. That chain has $N - 1$ internal nodes. The longest path has $N - 2$ internal nodes below the root plus the leaf, so its depth is $N - 1$. Check: with $N = 2$, the root splits the two samples and the depth is 1.

Synthesis: a single continuous attribute with $N$ distinct values is enough to build this chain, so the bounds hold for $k = 1$. More attributes add choices of split, and they do not add size.

### Why the Bounds Matter

The bounds explain why a tree overfits. A tree on continuous data can grow until it has one leaf per training sample, with zero training error and a boundary shaped around every point. The slides show this directly: the depth 10 boundary on the 2-D example carves small rectangles around single points, where depth 1 and depth 2 draw one or three straight cuts ([[Block 2 Slides]], p. 77). The Mitchell figure plots accuracy against tree size: training accuracy keeps rising with the number of nodes, and test accuracy peaks and then falls ([[Block 2 Slides]], p. 86; repeated in [[F26-midterm-review-234p]], p. 13). The `max_depth` plot tells the same story with depth on the x-axis: training error falls steadily, validation error is lowest near depth 10 and rises after it ([[Block 2 Slides]], p. 91; [[F26-midterm-review-234p]], p. 15). See [[Overfitting and Underfitting]].

Every control the slides list for tree overfitting is a control on size ([[Block 2 Slides]], p. 96):

1. Do not grow the tree beyond some maximum depth.
2. Do not split if the splitting criterion is below a threshold.
3. Stop growing when the split is not statistically significant.
4. Grow the entire tree, then prune.

The first three are stopping conditions that keep the tree below its maximum size. Pruning lets the tree reach full size on the training set, then removes the splits that do not reduce validation error, one at a time, until no removal helps ([[Block 2 Slides]], p. 97). The result is a smaller and shallower tree.

Synthesis: the bounds also show why a single deep tree has high variance. A tree with $N$ leaves encodes the training sample exactly, so a different sample gives a different tree ([[Block 2 Slides]], p. 106). The slides note that `max_depth` sets each tree's capacity, and adding more trees to a forest does not overfit the way deeper trees do ([[Block 2 Slides]], p. 108).

### Counting Capacity: Trees Beside Networks

The exam asks the same kind of question of every model: how large is it, in terms of what? For a [[Fully Connected Layer]] the answer is a parameter count from the layer widths ([[CSCI 566 Midterm (Spring 2024)]], Q24, Q43). For a [[Convolutional Layer]] it is the kernel shape times the number of filters, plus biases (Q4, Q33). For [[k-Nearest Neighbors]] the answer is zero: the model stores the data and learns nothing (Q32). For a tree the answer is a size that depends on the attributes and on the data (Q27 to Q30).

The slides frame this as model complexity: "The number of learnable parameters" and "The value range for those parameters", with the warning that "It's hard to compare between different types of ML models", "E.g. trees vs neural network" ([[Block 2 Slides]], p. 89). The hyperparameters that set complexity differ by family: "Trees: #trees, maximal depths" against "Neural networks: architecture, depth (#layers), width (#hidden units), regularizations" ([[Block 2 Slides]], p. 94).

Synthesis: a network's parameter count is fixed before training by its architecture. A tree's size is fixed only by an upper bound, and the learner decides the actual size from the data. A tree on continuous attributes can grow with $N$, as kNN's memory does, where a network's size stays put as $N$ grows. The slides name VC dimension as the more precise measure of complexity ([[Block 2 Slides]], p. 89); see [[VC Dimension]] and [[Parameterization of a Hypothesis Class]].

## Exam Questions

The four size questions share one setup: $N$ samples, each with $k$ attributes, $k \ll N$, and depth defined as the maximum number of nodes between the root and a leaf, including the leaf and excluding the root ([[CSCI 566 Midterm (Spring 2024)]], Q27).

**Q27.** With binary attributes, what is the maximal number of leaf nodes? Options: $2^k$, $NK$, $2NK - 1$, $N^k - 1$. Answer: A, $2^k$ ([[CSCI 566 Midterm (Spring 2024)]], Q27).
Each attribute is tested at most once on a path, so a path holds at most $k$ binary tests, and a complete tree with $k$ levels has $2^k$ leaves. The other options grow with $N$, and the attribute values cap the tree before the sample count does.

**Q28.** For the same binary-valued data, what is the maximum possible depth? Options: $O(k)$, $O(k - 1)$, $O(\log k)$, $O(\log(k + N))$. Answer: A, $O(k)$ ([[CSCI 566 Midterm (Spring 2024)]], Q28).
A path uses each attribute at most once, so it has at most $k$ tests, and under the exam's definition the depth of that path is $k$. $O(k - 1)$ and $O(k)$ describe the same growth, and the exam's key picks A; write $k$ and pick the option that names it.

**Q29.** With continuous attributes, what is the maximum number of leaf nodes? Options: $2^{k-1}$, $NK^2$, $K$, $N$. Answer: D, $N$ ([[CSCI 566 Midterm (Spring 2024)]], Q29).
A threshold split can reuse an attribute, so $k$ no longer limits the tree. Each leaf holds at least one sample, so the tree stops at one leaf per sample.

**Q30.** With continuous attributes, what is the maximal possible depth? Options: $NK^2$, $K$, $N - 1$, $2^{k-1}$. Answer: C, $N - 1$ ([[CSCI 566 Midterm (Spring 2024)]], Q30).
The deepest tree is a chain that peels one sample off at each node. The chain has $N - 1$ internal nodes, and the exam's depth counts the nodes below the root plus the leaf, which gives $N - 1$. Check with $N = 2$: one split, depth 1.

Two more questions use the same ideas.

**Q6.** What is the primary purpose of pruning? Answer: A, to reduce the depth of the tree and prevent overfitting ([[CSCI 566 Midterm (Spring 2024)]], Q6).
Pruning removes splits after the full tree is grown ([[Block 2 Slides]], p. 97). A tree has no weights to penalize, so L2 regularization (option B) does not apply, and a smaller tree is a side effect, with overfitting as the reason.

**Q14.** Which is a disadvantage of decision trees? Answer: C, trees are prone to overfit ([[CSCI 566 Midterm (Spring 2024)]], Q14).
A tree can grow to one leaf per sample and fit the training set exactly. Options A and B contradict the slides: a non-ML person can read a tree, and prediction is a walk from root to leaf, which is cheap next to kNN's search over all stored samples ([[Block 2 Slides]], p. 101).

## Related

- [[Decision Trees]]: the parent topic, with the learning algorithm, stopping conditions, and pruning this topic builds on
- [[Overfitting and Underfitting]]: tree size is the complexity axis of the error curves
- [[VC Dimension]]: the slides' more precise measure of model complexity
- [[Parameterization of a Hypothesis Class]]: how the form of a model fixes what it can fit
- [[k-Nearest Neighbors]]: the other model whose size follows the data instead of a fixed parameter count
- [[Fully Connected Layer]] and [[Convolutional Layer]]: the parameter counts the exam asks for beside tree sizes
- [[Linear Separability]]: deep trees fit data that no linear boundary separates, such as XOR
- [[Model Evaluation]]: the validation error that pruning minimizes

## Sources

- [[Block 2 Slides]], pp. 62, 65, 74–77, 86, 89, 91, 94, 96–97, 101, 106, 108
- [[F26-midterm-review-234p]], pp. 13, 15, which repeat Block 2 slides 86 and 91
- [[CSCI 566 Midterm (Spring 2024)]], Q6, Q14, Q27–Q30, with the parameter-count questions Q4, Q24, Q32, Q33, Q43 for contrast
