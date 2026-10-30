---
description: Early stopping keeps the checkpoint with the best value of a chosen validation metric instead of the last training checkpoint; CSCI 566 tells students to wait for a pattern with a patience window and to keep the test set out of stopping decisions.
aliases: [Checkpoint selection, Best checkpoint, Patience window, Patience, Early stopping with checkpoints]
sources: ["[[Block 7 Slides]]", "[[F26-midterm-review-234p]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Neural Network Training]]

## Definition

Early stopping uses a held-out validation metric to decide when training ends and which checkpoint to keep. The deck's slide "Checkpoint Selection and Early Stopping" treats the two decisions together ([[Block 7 Slides]], p. 135).

## Explanation

### Why the last checkpoint is not always the best

In an illustrative plot over 8 epochs, training loss falls from about 1.2 to below 0.1. Validation loss reaches its lowest value, about 0.8, near epoch 4 and then rises to about 1.1 (values read from the plot). The slide says: "The best training checkpoint may not be the best held-out checkpoint." Its rule: "Select checkpoints using the chosen validation metric." ([[Block 7 Slides]], p. 134). The midterm review repeats this slide ([[F26-midterm-review-234p]], p. 138). This pattern is overfitting; see [[Overfitting and Underfitting]].

### The protocol

The slide opens with: "One noisy validation dip does not require stopping immediately." ([[Block 7 Slides]], p. 135). It gives three steps:

| Step | Rule |
| --- | --- |
| Save the best checkpoint | "Keep the best value of the selected validation metric." |
| Wait for a pattern | "A patience window can tolerate short-term noise." |
| Use a fixed protocol | "Keep the test set out of stopping decisions." |

The slide closes with: "Choose the stopping rule before inspecting test performance." ([[Block 7 Slides]], p. 135). The midterm review repeats this slide ([[F26-midterm-review-234p]], p. 139).

Synthesis: a stopping decision is a model choice. If test performance guides that choice, the test set acts as validation data and no longer gives an unbiased estimate. See Test Set Contamination and [[Model Evaluation]].

### Worked example: patience 3

The midterm review's slide "Early Stopping With Checkpoints" says: "Save the best validation checkpoint, stop after 3 epochs without improvement, and restore the saved weights." ([[F26-midterm-review-234p]], p. 140). On its illustrative loss curves over 8 epochs:

1. "Best validation: epoch 5, loss 0.45, saved".
2. "Epochs 6, 7, 8: no improvement, stop after 8 (patience 3)".
3. "Restore epoch 5, not epoch 8".

The slide ends with: "Test set: evaluate once, after all choices are fixed." (p. 140).

Synthesis: patience counts the epochs since the last improvement of the validation metric. The 3 extra epochs cost compute, but they do not change the weights that the model keeps.

### Early stopping as a regularizer

The slide "Regularization: Diagnose, Then Choose" puts early stopping in one row with dropout: "Use when they fit the architecture and validation protocol." ([[Block 7 Slides]], p. 170). The same slide says: "Compare one controlled change at a time." See [[Regularization]] and [[Dropout]].

## Related

- [[Overfitting and Underfitting]]: reading training and validation curves
- [[Regularization]]
- [[Dropout]]
- Test Set Contamination
- [[Model Evaluation]]
- Model Selection

## Sources

- [[Block 7 Slides]], pp. 134–135, 170
- [[F26-midterm-review-234p]], pp. 138–140
