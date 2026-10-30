---
id: con-cmg7jw
type: topic
kind: concept
description: Test set contamination, a form of data leakage, happens when test items or items close to them reach a model's training, preprocessing, or selection; CSCI 566 cites a 2024 audit with 1% to 45% benchmark contamination and tells students to make every choice on validation data and keep the final test private.
tags: [machine-learning/cs566-deeplearning]
aliases: [Benchmark contamination, Data contamination, Test set leakage, Keep the final test set private, Data leakage]
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

The old rule: "A final test item must be unseen, and used once" ([[Block 2 Slides]], p. 99). Test set contamination breaks this rule. The test items, or items close to them, appear in the data the model trained on.

Synthesis: contamination is one form of data leakage. In data leakage, information from evaluation data enters training, preprocessing, or model selection.

## Explanation

### Evidence on the slide

The slide "When the Test Set Was Seen" gives three findings ([[Block 2 Slides]], p. 99):

- **Contamination is common.** A 2024 audit of over 15 models across six multiple-choice QA benchmarks showed contamination from 1% to 45%.
- **It does not always inflate scores.** Contaminated subsets showed boosts of up to 14% on C-Eval and 7% on HellaSwag, but only a minimal increase on MMLU.
- **Patching the benchmark does not fix it.** Across 10 models, 5 benchmarks, and 20 mitigation strategies, none balanced fidelity against contamination resistance.

### The rule

"So use validation or cross-validation for every choice you make, and keep the final test private. Rewording a leaked question is not a reset" ([[Block 2 Slides]], p. 99).

In practice:

- Make every modeling choice, including hyperparameters in [[Model Selection]], on validation data or with cross-validation.
- Use the final test set once, at the end.
- Treat a leaked test item as seen, even after you reword it.

### Data leakage in a training pipeline

Block 7 shows more ways that evaluation data can reach the model:

- **Preprocessing statistics.** If you scale the data, derive the scale parameters (for example, the mean and standard deviation for standardization) from the training data, and then use them to scale the test data. "This prevents data leakage and ensures that the model's performance is evaluated on the same terms as it was trained." ([[Block 7 Slides]], p. 40). See [[Fit Preprocessing on Training Data Only]] and [[Data Preprocessing]].
- **Near-duplicates across splits.** "Keep near-duplicate photos in the same split." (p. 17)
- **Selection.** "Trying many settings also uses information from the validation set." Choose with validation data, then "Evaluate once on held-out test data" (p. 190). "The test score remains outside the search loop." (p. 326)
- **Stopping.** "Keep the test set out of stopping decisions." "Choose the stopping rule before inspecting test performance." (p. 135)

The deck uses the term "data leakage" only for the preprocessing case (p. 40). Synthesis: the other cases have the same effect. Information from evaluation data reaches training or a choice, and the evaluation score then overstates how well the model does on new data. [[Model Evaluation]] gives the full split and selection rules.

### Why it matters

Synthesis: test error estimates the true error only when the test items are new to the model ([[Model Evaluation]]). A contaminated test set measures part of the training fit, so it can hide [[Overfitting and Underfitting|overfitting]]. The previous slide makes a related point: memorization of training strings is a different failure from overfitting, and validation error alone does not show it ([[Block 2 Slides]], p. 98).

## Related

- [[Model Evaluation]]
- [[Model Selection]]
- [[Fit Preprocessing on Training Data Only]]
- [[Data Preprocessing]]
- [[Overfitting and Underfitting]]: memorization is not overfitting
- [[What Counts as Solved]]

## Sources

- [[Block 2 Slides]], pp. 98–99
- [[Block 7 Slides]], pp. 17, 40, 135, 190, 326
