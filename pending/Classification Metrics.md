---
id: con-qhxhxg
type: topic
kind: concept
description: Accuracy, precision, recall, F1, specificity, ROC-AUC, and PR-AUC for binary classifiers, computed from the confusion matrix; how the decision threshold trades precision against recall; and why accuracy and ROC-AUC can look strong while positives are missed or false alarms are high when positives are rare.
tags: [machine-learning/cs566-deeplearning]
aliases: [Accuracy, Precision, Recall, True positive rate, TPR, Sensitivity, F1 score, F1, AUC-ROC, ROC-AUC, ROC curve, Area under the ROC curve, PR-AUC, ROC-AUC under class imbalance, When ROC Hides False Alarms, Report both ROC-AUC and PR-AUC when positives are rare, Safety guardrail classifier, Guardrail classifier, Specificity, Confusion matrix, TP / FP / FN / TN counts, Classification threshold, Decision threshold, Flagging threshold, Accuracy on imbalanced data, Accuracy paradox, Class imbalance]
created: 2026-09-28T00:00:00
updated: 2026-10-19T17:48:15
refreshed: 2026-10-19T17:48:15
status: stable
sources: ["[[Block 2 Slides]]", "[[F26-midterm-review-234p]]"]
up: ["[[Model Evaluation]]"]
---

> [!concept] Concept
> 2 sources · refreshed 2026-10-19 · #machine-learning/cs566-deeplearning
> Up: [[Model Evaluation]]

## Definition

Classification metrics compare a classifier's predictions $\hat{y}$ with the true labels $y$. The slides define these for binary classification ([[Block 2 Slides]], p. 137; repeated in [[F26-midterm-review-234p]], p. 21):

| Metric | Formula | Code |
| --- | --- | --- |
| Accuracy | # correct predictions / # examples | `sum(y == y_hat) / y.size` |
| Precision | # TP / # (TP + FP) | `sum((y_hat == 1) & (y == 1)) / sum(y_hat == 1)` |
| Recall | # TP / # positive examples | `sum((y_hat == 1) & (y == 1)) / sum(y == 1)` |
| F1 | $2pr / (p + r)$ | |

The slide warns: "Be careful of division by 0" (p. 137). Precision divides by the number of positive predictions, and recall divides by the number of positive examples. Either count can be zero.

The metrics come from four counts, the confusion matrix. The midterm review names them for a defect flagger, where positive means defective and predicted positive means flagged for inspection ([[F26-midterm-review-234p]], p. 22):

| Actual \ Prediction | Flagged (+) | Passed (−) |
| --- | --- | --- |
| Defective (+) | TP: caught | FN: missed |
| Good (−) | FP: false alarm | TN: correctly passed |

Precision and recall have the same numerator, TP, but different denominators. Precision divides by the flagged parts (TP + FP). Recall divides by the defective parts (TP + FN) (p. 22).

## Explanation

### Accuracy on imbalanced data

The midterm review uses fabricated inspection data: 1,000 parts, of which 20 are defective (positive) and 980 are good (negative) ([[F26-midterm-review-234p]], p. 20). A rule that always predicts good never flags a part:

- Accuracy: 980 / 1,000 = 98%.
- Defects caught: 0 / 20, so recall = 0%.
- "Precision is undefined because no part is flagged, and 0/0 has no value." (p. 20)

This is the division by 0 that the Block 2 slide warns about.

### Worked counts

The same 1,000 parts with a flagger that works give TP 16, FP 24, FN 4, and TN 956 ([[F26-midterm-review-234p]], p. 22):

- Precision = 16 / (16 + 24) = 40%: of 40 flagged parts, 16 are defective.
- Recall = 16 / (16 + 4) = 80%: of 20 defective parts, 16 are caught.

Synthesis, not from the deck: accuracy for these counts is (16 + 956) / 1,000 = 97.2%. That is lower than the 98% of the rule that flags nothing, but this flagger catches 16 defects.

### Moving the threshold

A part is flagged when its defect score is at least the threshold. The deck constructs these counts for illustration ([[F26-midterm-review-234p]], p. 23):

| Threshold | Flagged | True / false alarms | Precision | Recall | Missed defects |
| --- | --- | --- | --- | --- | --- |
| 0.2 (lower) | 80 | 19 / 61 | 23.75% | 95% | 1 |
| 0.8 (higher) | 12 | 9 / 3 | 75% | 45% | 11 |

"Lowering the threshold can add both true and false alarms; recall cannot fall, but precision can move either way." (p. 23)

Synthesis: a lower threshold only adds flags. TP cannot fall, and the recall denominator (all positives) does not change. Precision depends on the mix of the added flags. The ROC curve below traces this trade-off over all thresholds.

### Which metric leads threshold selection

The review asks: a factory flags rare defects. A missed defect ships to a customer, and a false alarm triggers one manual review. Which metric should lead threshold selection ([[F26-midterm-review-234p]], pp. 24–25)? The answer is D, recall, while tracking precision: "recall tracks the costly misses, and precision shows the review workload" (p. 25). The deck rejects the other choices (p. 25):

- Accuracy: "with rare defects, accuracy can stay high even when many defects are missed."
- Precision: "precision limits false alarms, the cheaper error here, and can tolerate misses."
- Specificity: it "counts good parts and can be high while defects slip through."

Synthesis, not from the deck: specificity is the usual name for TN / (TN + FP), the share of negatives correctly passed. It equals 1 − FPR. For the p. 22 counts it is 956 / 980 ≈ 97.6%, while 4 defects are missed.

The ChatGPT Agent guardrail below makes the same choice: a threshold with at least 0.95 recall, with lower precision accepted.

### ROC curve and AUC

Choose a decision threshold $\theta$. Predict positive if the output $o \geq \theta$, else negative. The ROC curve plots TPR against FPR over all thresholds ([[Block 2 Slides]], p. 138):

- TPR = # true positive predictions / # positive examples (the same quantity as recall)
- FPR = # false positive predictions / # negative examples

AUC-ROC measures how well the model separates the two classes. It lies in $[0, 1]$ (p. 138). Ideal separation gives AUC = 1, partial overlap about 0.7, and distributions that do not separate give 0.5 (p. 138). Chance is 0.50 (p. 139).

### When ROC hides false alarms

The slides give an example with rare positives ([[Block 2 Slides]], p. 139):

- 10,000 scored cases, 1% positive, with positives ranked 10, 20, …, 1000.
- A cut at the top 1,000 gives recall 1.00 but precision only 0.10.
- ROC gives that cut an FPR of 0.091, because the 900 false alarms sit among 9,900 negatives.
- ROC-AUC reads 0.954. PR-AUC reads 0.098, against a chance line of 0.01.

Chance for ROC-AUC is 0.50. Chance for PR-AUC is the positive rate. The slide's rule: "Report both here" (p. 139).

Synthesis: FPR divides false alarms by the count of negatives. When negatives are many, a large number of false alarms still gives a small FPR. Precision divides by the count of positive predictions, so it shows those false alarms.

### Case: safety guardrails

A guardrail is a thresholded classifier ([[Block 2 Slides]], p. 212). It makes one binary decision per exchange: pass, or escalate for a closer look (p. 140).

- **Constitutional Classifiers++**: in a one-month shadow run on live traffic (January 2026), 5.5% of exchanges escalated and 0.05% were finally flagged. That is a 1-in-2000 positive rate (p. 140).
- **ChatGPT Agent**: in July 2025 its first-stage classifier reported recall 0.960, precision 0.737, and F1 0.834. OpenAI says it picked a threshold with at least 0.95 recall and accepted the lower precision (p. 140).
- **PromptGuard 2 86M** reports 97.5% recall at a 1% false positive rate (p. 212).

At a 1-in-2000 positive rate, accuracy and ROC-AUC stay comfortable, while the false alarms decide whether the system can ship (p. 140). Neither the ChatGPT Agent report nor the Constitutional Classifiers++ report gives a PR curve on one labeled production sample. Attack tests and ordinary traffic are different datasets and do not combine into one confusion matrix (p. 140).

## Related

- [[Model Evaluation]]: loss against other metrics, and how to select models
- [[Loss Functions]]: accuracy is one minus the mean 0/1 loss, and the 0/1 loss gives no gradient for training
- [[Agent Loop]]: model routing as cost-sensitive classification, where "The threshold is the design"
- [[Deployment Failure Modes]]: false refusal is a false alarm of a guardrail
- [[Shortcut Learning]]
- [[LLM Trustworthiness]]

## Sources

- [[Block 2 Slides]], pp. 137–140, 212
- [[F26-midterm-review-234p]], pp. 20–25
