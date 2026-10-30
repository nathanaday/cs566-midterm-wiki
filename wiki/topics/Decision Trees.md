---
id: con-w3epjy
type: topic
kind: concept
description: A classical ML classifier that tests one feature at each node and predicts the majority class at a leaf. CSCI 566 teaches greedy learning with decision stumps, the choice of splitting criteria, stopping conditions, and pruning to control overfitting.
tags: [machine-learning/cs566-deeplearning]
aliases: [Decision tree, DT, Decision tree classifier, Decision tree learning, Greedy decision tree learning, Decision stump, Decision tree splitting criteria, Gini gain, Information gain, Decision tree stopping conditions, Decision tree pruning, Reduced-error pruning]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 2 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Classical Machine Learning]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Classical Machine Learning]]

## Definition

A decision tree is a classifier that sends an input through a tree of feature tests. Each test picks a branch, and the leaf at the end gives the predicted class ([[Block 2 Slides]], pp. 36–38). Decision trees are the first topic in the Classical ML Algorithms section of CSCI 566, and the slides credit the material to Stanford CS 229 ([[Block 2 Slides]], pp. 30–60).

## Explanation

### The loan example

The running example decides if a loan is safe or risky ([[Block 2 Slides]], p. 31). The features are:

- Credit history: excellent, fair, or poor (did the person pay previous loans on time?).
- Income, for example $80K per year.
- Term: 3 or 5 years (how soon the loan must be repaid).
- Personal info, such as age, reason for the loan, and marital status.

([[Block 2 Slides]], pp. 32–35)

The classifier takes a loan application $x_i$ and outputs $\hat{y}_i = +1$ (Safe) or $-1$ (Risky) ([[Block 2 Slides]], p. 36). The training table has $N = 40$ loans with three features: Credit (excellent/fair/poor), Term (3/5 years), and Income (high/low). Of these, 22 loans are safe and 18 are risky ([[Block 2 Slides]], pp. 42–43).

### Prediction

To score an application, follow the path from the root to a leaf. In the example tree, excellent credit gives Safe. Fair credit tests Term (3 years Risky, 5 years Safe). Poor credit tests Income: low gives Risky, and high tests Term (3 years Risky, 5 years Safe) ([[Block 2 Slides]], p. 37; repeated in [[F26-midterm-review-234p]], p. 10). So $x_i$ = (Credit = poor, Income = high, Term = 5 years) gives $\hat{y}_i$ = Safe ([[Block 2 Slides]], p. 38; repeated in [[F26-midterm-review-234p]], p. 11).

The slides name three kinds of node ([[Block 2 Slides]], pp. 44–46, 59):

- The **root node** holds all $N$ examples. Its compact notation shows the count of each class (22 safe, 18 risky).
- An **intermediate node** holds the subset of data with one feature value after a split.
- A **leaf node** needs no more splits, for example when all its data has one class.

At each node, the prediction $\hat{y}$ is the majority class of the data in that node ([[Block 2 Slides]], p. 47).

### The learning problem

Given $N$ training observations $(x_i, y_i)$, learning optimizes a quality metric on the training data to produce a tree $T(X)$ ([[Block 2 Slides]], p. 39). The quality metric is classification error, the fraction of mistakes:

$$\text{error} = \frac{\#\,\text{incorrect predictions}}{\#\,\text{examples}}$$

The best value is 0.0 and the worst is 1.0 ([[Block 2 Slides]], p. 40). For the general use of error rates on test sets, see [[Model Evaluation]].

The number of possible trees grows exponentially, so exact learning is hard. Learning the smallest decision tree is NP-hard (Hyafil & Rivest '76) ([[Block 2 Slides]], p. 41). The course therefore uses a greedy algorithm.

### Decision stumps

A decision stump is a tree with one level: one split from the root into child nodes ([[Block 2 Slides]], p. 45). A split on Credit turns the root (22/18) into excellent (9/0), fair (9/4), and poor (4/14). With majority prediction, this stump predicts excellent → Safe, fair → Safe, poor → Risky ([[Block 2 Slides]], pp. 45, 47). To learn a stump, find the "best" feature to split on ([[Block 2 Slides]], p. 48).

### Choosing a split

The slides rate a split by the classification error of its stump ([[Block 2 Slides]], p. 50):

1. At each node, set $\hat{y}$ to the majority class.
2. Calculate the classification error of predicting $\hat{y}$ for that data.

([[Block 2 Slides]], p. 51)

Worked example:

| Choice | Mistakes | Error |
|---|---|---|
| No split (predict Safe at root) | 18 | 0.45 |
| Split on Credit | 0 + 4 + 4 | 0.2 |
| Split on Term (3 yrs 16/4 → Safe, 5 yrs 6/14 → Risky) | 4 + 6 | 0.25 |

([[Block 2 Slides]], pp. 51–55)

Credit wins over Term ([[Block 2 Slides]], p. 56). The general procedure: for a node $M$, split its data on each feature $h_i(x)$, compute the classification error of each split, and choose the feature $h^*(x)$ with the lowest error ([[Block 2 Slides]], p. 57).

### Greedy recursive learning

Tree learning is recursive stump learning. After the first split, build a new stump on each child subset ([[Block 2 Slides]], p. 60). The loop is: pick the best feature to split on, learn a stump with that split, then recurse on each leaf of the stump ([[Block 2 Slides]], p. 63). Written as steps:

1. Start with an empty tree.
2. Select the feature split with the lowest classification error.
3. For each split: if there is nothing more to do, make predictions (the stopping conditions).
4. Otherwise, go to step 2 and recurse on this split.

([[Block 2 Slides]], p. 66)

In the loan example, fair credit (9/4) splits on Term into 3 years (0/4, Risky) and 5 years (9/0, Safe). Poor credit (4/14) splits on Income: low (0/9) is Risky, and high (4/5) is still mixed, so the algorithm builds another stump on it ([[Block 2 Slides]], p. 61). That node splits on Term: 3 years (0/2) is Risky and 5 years (4/3) is Safe ([[Block 2 Slides]], p. 62).

The tree is built greedily and never revisits a split ([[Block 2 Slides]], p. 114).

### Stopping conditions

1. All data in the node has the same $y$ value ([[Block 2 Slides]], p. 64).
2. The node has already been split on all possible features. The 5-year node (4 safe / 3 risky) in the loan example stops for this reason ([[Block 2 Slides]], p. 65).
3. Proposed: stop if no split reduces the classification error ([[Block 2 Slides]], p. 67). The slides do not recommend this condition ([[Block 2 Slides]], p. 72).

The XOR data set shows why condition 3 fails. Take $y = x[1] \text{ xor } x[2]$ with 2 True and 2 False points. The root has error 0.5 ([[Block 2 Slides]], p. 68). A split on $x[1]$ gives children with 1 True / 1 False each, so the error stays 0.5. A split on $x[2]$ also gives $(1+1)/(2+2) = 0.5$ ([[Block 2 Slides]], pp. 69–70). With condition 3, the tree is only the root, which predicts True with error 0.5 ([[Block 2 Slides]], p. 71). Without it, the tree splits on $x[1]$ and then on $x[2]$ in each branch. Every leaf is pure, and the tree classifies all the data correctly ([[Block 2 Slides]], p. 72).

### Continuous features and decision boundaries

For a continuous feature, the tree splits at a threshold. On 2-D data (root 17 negative / 14 positive), a depth-1 split at $x[1] < -0.07$ gives 13/3, and $x[1] \ge -0.07$ gives 4/11 ([[Block 2 Slides]], p. 74). At depth 2, the left branch splits on $x[1]$ again at −1.66, and the right branch splits on $x[2]$ at 1.55 ([[Block 2 Slides]], p. 75). With threshold splits, a path can use the same feature more than once ([[Block 2 Slides]], p. 76).

A deeper tree gives a more complex decision boundary. The slides show depth 1, 2, and 10 on the same data ([[Block 2 Slides]], p. 77). Tree boundaries are axis-aligned rectangles. Logistic regression with degree 1, 2, and 6 features gives smooth curves instead ([[Block 2 Slides]], p. 78).

### Splitting criteria

Classification error is one way to rate a split. Buntine & Niblett (1992) compared four criteria (random, Gini, mutual information, and Marshall) on 12 data sets: hypo, breast, tumor, lymph, LED, mush, votes, votes1, iris, glass, xd6, and pole. The slides credit this material to CMU 10601 ([[Block 2 Slides]], pp. 79, 81). Four sets are medical diagnosis sets. For example, hypo has 4 classes, 29 attributes, 1000 training and 2772 test examples ([[Block 2 Slides]], p. 79). Information gain is another name for mutual information ([[Block 2 Slides]], p. 80).

The slides' takeaway: Gini gain and mutual information are statistically indistinguishable in error on pruned trees ([[Block 2 Slides]], pp. 80–81).

| Data set | Gini | Info. gain | Random |
|---|---|---|---|
| hypo | 1.01 ± 0.29 | 0.95 ± 0.22 | 7.44 ± 0.53 |
| mush | 1.44 ± 0.47 | 1.44 ± 0.47 | — |
| xd6 | 22.14 ± 3.23 | 22.17 ± 3.36 | — |

(Error on pruned trees, [[Block 2 Slides]], p. 80)

A second table gives the average difference in error between Gini and each other rule, with the significance from a two-tailed paired t-test. Gini vs. random differs by 6.43 on hypo. Gini vs. info gain differs by −0.06 on hypo and 0.00 on mush ([[Block 2 Slides]], p. 81). Random splitting gives clearly higher error on most data sets ([[Block 2 Slides]], p. 80).

### Overfitting control

A single deep tree has high variance: its predictions change a lot when the training sample changes ([[Block 2 Slides]], p. 106). See [[Tree Ensembles]] for how averaging many trees reduces it.

A figure from Tom Mitchell, credited to CMU 10601, plots accuracy against tree size. Accuracy on training data keeps rising to about 0.86 near 90 nodes. Accuracy on test data peaks near 0.75 and falls to about 0.69 ([[Block 2 Slides]], p. 86; repeated in [[F26-midterm-review-234p]], p. 13; values read from the plot).

"The tree size can be controlled by the number of levels." The slides show this with scikit-learn's `DecisionTreeRegressor(max_depth=n)` on house sales data. Train error falls steadily with depth (to about 0.03 at depth 50). Validation error is lowest near depth 10 (about 0.25) and then rises a little. Small depth is labeled underfitting and large depth overfitting ([[Block 2 Slides]], p. 91; repeated in [[F26-midterm-review-234p]], p. 15). See [[Overfitting and Underfitting]].

The slides list four ways to control overfitting ([[Block 2 Slides]], p. 96):

- Do not grow the tree past a maximum depth.
- Do not split if the splitting criterion (for example mutual information) is below a threshold.
- Stop growing when the split is not statistically significant.
- Grow the entire tree, then prune.

Reduced-error pruning works as follows ([[Block 2 Slides]], p. 97):

1. Split the data into a training set and a validation set.
2. Grow the full tree on the training set.
3. For each split, compare the validation error with and without it. Remove the split that most decreases validation error. Stop if no removal improves validation error; otherwise repeat.

### Uses

Decision trees are one of the most popular classification methods in practice. A non-ML person can understand the learned tree, and the method is efficient in computation and memory. Trees apply to classification, regression, and density estimation ([[Block 2 Slides]], p. 101). Application areas include medicine, molecular biology, text classification, manufacturing, astronomy, and agriculture ([[Block 2 Slides]], p. 102).

The summary slide lists the learning outcomes: define a decision tree classifier, interpret its output, learn it with a greedy algorithm, traverse it for majority-class predictions, handle continuous and discrete features, and control overfitting and underfitting ([[Block 2 Slides]], p. 103).

Synthesis: unlike [[Linear Classification]], a tree does not use the form $Wx + b$. Its axis-aligned boundaries can separate data that is not linearly separable, such as XOR (see [[Linear Separability]]). The cost is high variance, which depth limits and pruning reduce.

## Related

- [[Decision Tree Size Bounds]]: the maximum leaves and depth as a function of attributes and samples
- [[Tree Ensembles]]: averaging many trees to lower the variance of a single tree
- [[Linear Classification]]
- [[Linear Separability]]
- [[Model Evaluation]]
- [[Overfitting and Underfitting]]
- [[Function Approximation]]

## Sources

- [[Block 2 Slides]], pp. 30–114
- [[F26-midterm-review-234p]], pp. 10–11, 13, 15, which repeat Block 2 slides 37, 38, 86, and 91
