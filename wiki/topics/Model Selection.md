---
id: con-cn8342
type: topic
kind: concept
description: Model selection picks a model family and its hyperparameters so that model complexity matches data complexity; CSCI 566 chooses hyperparameters on validation data with a seven-step loop and keeps the test score outside the search.
tags: [machine-learning/cs566-deeplearning]
aliases: [Hyperparameter selection, Hyperparameter tuning, Choosing hyperparameters, Hyperparameter optimization, HPO, Hyperparameter search, HP search, HP tuning]
created: 2026-09-28T00:00:00
updated: 2026-10-13T18:22:47
refreshed: 2026-10-13T18:22:47
status: stable
sources: ["[[Block 2 Slides]]", "[[Block 7 Slides]]"]
up: ["[[Model Evaluation]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Model Evaluation]]

## Definition

"Model selection: match model and data complexities" ([[Block 2 Slides]], p. 95).

Block 7 separates two kinds of values: "Hyperparameters: usually set beforehand" and "Parameters: learnable, e.g., model weights" ([[Block 7 Slides]], p. 173). Training learns the parameters. Model selection chooses the hyperparameters.

## Explanation

### Pick a model family, then its hyperparameters

The Block 2 slide gives two steps ([[Block 2 Slides]], p. 94, credited to Stanford CS 329P):

1. Pick a model with a proper complexity for your data. Minimize the generalization error, and also consider business metrics.
2. Pick a model family, then select proper hyperparameters:
   - Trees: number of trees, maximal depth.
   - Neural networks: architecture, depth (number of layers), width (number of hidden units), and regularizations.

### Choose by validation

The Block 7 summary splits the work in two ([[Block 7 Slides]], p. 189):

- To improve training error, use [[Gradient-Based Optimizers]] and [[Learning Rate Schedules]].
- To improve generalization, "choosing by validation", use [[Regularization]] and choose the hyperparameters.

For the [[Flower Classifier Running Example|flower classifier]], each data split has one role ([[Block 7 Slides]], p. 326):

| Split | Role |
| --- | --- |
| Training data | "Fit each candidate model with its proposed learning rate and weight decay." |
| Validation data | "Compare candidate settings under the same metric and budget." |
| Test data | "Evaluate the selected procedure after tuning is complete." |

"The test score remains outside the search loop" (p. 326).

### The seven-step procedure for neural networks

[[Block 7 Slides]] builds this list one step per slide (pp. 174–179, 186):

1. **Check initial loss** (p. 174). Turn off weight decay. Sanity check the loss at initialization. "For uniform class probabilities: loss = ln(C); three classes give ≈1.10."
2. **Overfit a small sample** (p. 175). Try to train to 100% training accuracy on a small sample of training data (~5-10 minibatches). Adjust the architecture, the learning rate, and the [[Weight Initialization|weight initialization]]. To diagnose:
   - The loss does not go down: the learning rate is too low, or the initialization is bad.
   - The loss explodes to Inf or NaN: the learning rate is too high, or the initialization is bad.
3. **Find a learning rate that makes the loss go down** (p. 176). Use the architecture from step 2 and all the training data. Turn on small weight decay. Find a learning rate that makes the loss drop significantly within ~100 iterations. "Good learning rates to try: 1e-1, 1e-2, 1e-3, 1e-4."
4. **Coarse grid, train for ~1-5 epochs** (p. 177). Choose a few values of learning rate and weight decay around what worked in step 3. Train a few models for ~1-5 epochs. "Good weight decay to try: 1e-4, 1e-5, 0."
5. **Refine grid, train longer** (p. 178). Pick the best models from step 4. Train them for longer (~10-20 epochs) without learning rate decay.
6. **Look at loss and accuracy curves** (p. 179). See the next section.
7. **"GOTO step 5"** (p. 186). Steps 5 and 6 repeat as a loop.

Points in the slides that are not consistent:

- Step 2 has two names. p. 175 calls it "Fit a tiny sample as a debugging check". pp. 176–179 and p. 186 call it "Overfit a small sample".
- p. 176 lists "Good learning rates to try". p. 187 shows the same four values (0.0001, 0.001, 0.01, 0.1) and says: "These values illustrate spacing, not a universal recommendation."

Synthesis: steps 1 and 2 are debugging checks. They find setup errors before the search spends compute. Steps 3 to 7 are the search.

### Read the curves (step 6)

Three example curves of training and validation accuracy against time ([[Block 7 Slides]], pp. 180–182):

- Both curves still rise: "Validation accuracy still improves: a longer run may help" (p. 180).
- Training accuracy rises while validation accuracy falls: "A large gap can suggest overfitting. Check the split, labels and regularization" (p. 181). See [[Overfitting and Underfitting]] and [[Early Stopping]].
- The curves stay close together: "Both accuracies low: possible underfitting. A small gap alone is inconclusive" (p. 182).

More advice from the slides:

- "Losses may be noisy, use a scatter plot and also plot moving average to see trends better" (p. 183).
- "You can plot all your loss curves for different HPs on a single plot" (p. 184).
- "Don't look at accuracy or loss curves for too long!" (p. 185).

### Search strategies

- **Search across scales** ([[Block 7 Slides]], p. 187). "A broad first pass checks orders of magnitude." "Find a useful region, then search more closely." "A fixed compute budget makes comparisons meaningful."
- **Random search vs. grid search** (p. 188, citing Bergstra and Bengio, 2012, "Random Search for Hyper-Parameter Optimization"). The slide draws nine trials in a grid layout and nine in a random layout, over one important and one unimportant parameter. Synthesis: with the same number of trials, the random layout tries more distinct values of the important parameter.
- **Choosing a method** (p. 325). Choosing hyperparameters for one dataset and one algorithm is "the most common case we encounter in our daily work". Use random and grid search "if cheap evaluation is possible". Use Bayesian Optimization "if evaluation is expensive, and the optimization is restricted".
- **The basic loop** (p. 333). "For the same classifier and split, try settings and measure validation accuracy." Pick the config with the highest accuracy. "Fitting on the data is expensive!"

### Hyperparameter tuning inside AutoML

[[AutoML]] groups its work in three buckets. The first is "HP tuning and/or algorithm selection: for a single dataset" ([[Block 7 Slides]], p. 316). Situation 1 keeps one algorithm and searches its hyperparameters, for example a decision tree with tree_depth 3, 5, or 10 (p. 320).

An automated search proposes a configuration, trains and evaluates it, and uses the results to choose the next trial. "The search still needs a trustworthy evaluation protocol" (p. 312). "An automated search still follows a task and evaluation protocol." "People still define the task, data boundaries and success metric" (p. 317).

### Not the same as HyperTuning

Hyperparameter tuning searches settings such as learning rate, weight decay, or LoRA rank. The [[HyperTuning]] method uses a trained hypernetwork to generate adaptation parameters from task demonstrations. The slide's rule: "Separate choosing settings from generating model parameters" ([[Block 7 Slides]], p. 264).

### Example

For a decision tree, `max_depth` sets the model complexity. On house sales data, training error keeps falling as `max_depth` grows, while validation error is lowest near depth 10 ([[Block 2 Slides]], p. 91). Synthesis: model selection picks the depth near that minimum.

### Why it matters

Too little complexity underfits and too much overfits; see [[Overfitting and Underfitting]]. Complex models such as deep networks need more data before they beat a simple linear model ([[Block 2 Slides]], p. 93). Each selection step uses held-out data, so the choices must come from validation data, not the final test set ([[Test Set Contamination]]). Block 7 states the same rule: "The test score remains outside the search loop" ([[Block 7 Slides]], p. 326).

To know which change caused a result, compare runs that differ in one factor. See [[Change One Factor per Experiment]].

## Related

- [[Overfitting and Underfitting]]: model complexity and data complexity
- [[Regularization]]: a hyperparameter for neural networks
- [[Model Evaluation]]
- [[Test Set Contamination]]
- [[Neural Networks]]
- [[Change One Factor per Experiment]]: the rule for controlled comparisons
- [[Gradient-Based Optimizers]], [[Learning Rate Schedules]], [[Weight Initialization]]
- [[Early Stopping]]
- [[AutoML]], Bayesian Optimization
- [[HyperTuning]]: a different method with a similar name
- [[Flower Classifier Running Example]]

## Sources

- [[Block 2 Slides]], pp. 91, 93–95
- [[Block 7 Slides]], pp. 173–189, 264, 312, 316–317, 320, 325–326, 333
