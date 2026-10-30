---
description: kNN regression predicts a continuous target as the mean, or distance-weighted mean, of the k nearest training points' values; it learns no parameters and pays its whole cost at prediction time, like the kNN classifier.
aliases: [k-Nearest Neighbors Regression, Nearest Neighbor Regression]
sources: ["[[Block 2 Slides]]", "[[F26-midterm-review-234p]]", "[[CSCI 566 Midterm (Spring 2024)]]"]
---

## Definition

kNN regression is [[k-Nearest Neighbors]] with a continuous target. The classifier returns `majority_vote(S)` over the set S of the k training points nearest to the query ([[Block 2 Slides]], p. 148). The regressor keeps the same S and returns the mean of the neighbors' target values. Synthesis: the decks teach kNN as a classifier only. The regression form appears once by name, as the method CARROT uses to route requests, "kNN classification and kNN regression over cost" ([[Block 2 Slides]], p. 212), with no definition.

## Explanation

### The prediction rule

Synthesis: the decks do not state the rule. With S the k nearest neighbors of $x'$ under the distance $d$ and $y^{(i)}$ their target values,

$$\hat{y}(x') = \frac{1}{k} \sum_{i \in S} y^{(i)}$$

The distance-weighted variant gives nearer neighbors more say, through weights $w_i$ that fall with distance, for example $w_i = 1 / d(x', x^{(i)})$:

$$\hat{y}(x') = \frac{\sum_{i \in S} w_i \, y^{(i)}}{\sum_{i \in S} w_i}$$

The deck has one distance-weighted neighbor rule, in kNN-LM: the retrieved neighbors form a distribution over targets with $p(k_i) \propto \exp(-d_i)$ ([[Block 2 Slides]], p. 176). That is the same weighting with softmax weights and a categorical target.

Synthesis: the median of the neighbors' values is a robust alternative when a few targets sit far from the rest. Every outlying neighbor moves the mean; the median ignores it.

### Zero learned parameters

`train(D)` stores the dataset D and nothing else ([[Block 2 Slides]], p. 148). Nearest neighbor "Requires no training!" (p. 147). The regressor changes only what `h(x')` returns, so it learns nothing either. k and the distance are hyperparameters, "choices about the algorithms themselves" (p. 165), and no step fits them to D.

### Cost at prediction time

"State where the cost lives: prediction, not training" ([[Block 2 Slides]], p. 182). kNN stores all the data, $O(ND)$, and finding the k closest points in D dimensions costs $O(ND + N \log k)$ (p. 181). Synthesis: the regressor runs the same search and then averages k numbers, so its prediction cost matches the classifier's.

### Choosing k

k sets the model capacity: "Small k leads to overfitting and large k leads to underfitting" ([[Block 2 Slides]], p. 180). Synthesis: in regression the same trade shows up in the fitted curve. At k = 1 the prediction jumps to each training value, a step function with high variance. At k = N every input gets the global mean, a flat line with high bias. Validation picks k between the two, as the review says for the classifier: "choose k by validation results" ([[F26-midterm-review-234p]], p. 26).

## Exam Questions

**Q51.** How does kNN handle regression? Answer A: by the mean of the nearest neighbors' values ([[CSCI 566 Midterm (Spring 2024)]], Q51). A majority vote (B) needs discrete labels. Copying the single nearest value (C) is 1-NN, which discards $k - 1$ neighbors. Gradient descent (D) has nothing to update, since kNN has no parameters.

**Q32.** 100 instances, 64 features each, a 3-NN classifier: how many parameters are learned? Answer 0 ([[CSCI 566 Midterm (Spring 2024)]], Q32). Training stores D ([[Block 2 Slides]], p. 148); N = 100, D = 64, and k = 3 describe the data and the hyperparameter, and none is learned. The same answer holds for a 3-NN regressor.

**Q34.** 100 billion training images of shape (3, 224, 224), ten classes; which trained model is least efficient at labeling a new image: 10-NN, [[AlexNet]], [[ResNet]]-50, or a 100-layer MLP with halving widths? Answer A, the 10-NN classifier ([[CSCI 566 Midterm (Spring 2024)]], Q34). Synthesis: each network costs one fixed forward pass per image, whatever the training-set size. 10-NN compares the new image with all $N = 10^{11}$ stored images in $D = 3 \times 224 \times 224 = 150{,}528$ dimensions, about $1.5 \times 10^{16}$ operations for one label, by the $O(ND + N \log k)$ count on p. 181.

## Related

- [[k-Nearest Neighbors]]: the classifier this topic extends
- [[Overfitting and Underfitting]]: what k trades off
- [[Model Evaluation]]: validation data to choose k
- [[Loss Functions]]: squared error, the loss a mean prediction minimizes
- [[Outlier Detection]]: the kNN-distance detector, another use of the same neighbor search

## Sources

- [[Block 2 Slides]], pp. 147-148, 165, 176, 180-182, 212
- [[F26-midterm-review-234p]], p. 26
- [[CSCI 566 Midterm (Spring 2024)]], Q32, Q34, Q51
