---
description: The front page of this wiki. Built for the CSCI 566 midterm, Fall 2026.
aliases:
  - CS566-DeepLearning
  - "CSCI 566: Deep Learning and its Applications"
  - Start Here
---

## Topics by Subject

Every topic, grouped by subject. Open a row to read the page.

```base
filters:
  and:
    - file.inFolder("wiki/topics")
views:
  - type: table
    name: Topics by subject
    groupBy:
      property: subject
      direction: ASC
    order:
      - file.name
      - description
    sort:
      - property: file.name
        direction: ASC
```


## Sources

- The lecture decks: [[Block 1 Slides]], [[Block 2 Slides]], [[Block 3 Slides]], [[Block 4 Slides]], [[Block 5 Slides]], [[Block 6 Slides]] and its longer revision [[Block 6 Slides Extended]], and [[Block 7 Slides]].
- The review deck: [[F26-midterm-review-234p]], the instructor's walk through Blocks 1 to 7 with worked examples and check questions.
- The sample exam: [[CSCI 566 Midterm (Spring 2024)]], with the answer key, mapped onto the topics.

