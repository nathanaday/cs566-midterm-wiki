---
id: ent-mcds4s
type: topic
kind: entity
description: TypeSafe AI's proprietary model, released in early access in September 2026, that answers typed questions about a block of state with calibrated probabilities instead of generating text.
tags: [machine-learning, tool]
aliases: [Jev (AI model), TypeSafe Jev]
created: 2026-09-28T00:00:00
updated: 2026-09-28T00:00:00
refreshed: 2026-09-28T00:00:00
status: stable
sources: ["Jev (AI model) - Wikipedia"]
---

> [!entity] Entity
> 1 source · refreshed 2026-09-28 · #machine-learning · #tool

## What it is

Jev is a proprietary AI model from TypeSafe AI, a San Francisco company founded in 2024. Unlike a large language model, Jev does not generate natural-language text. It returns typed values with probability estimates and confidence scores, and its output is meant for other software to consume, not for a person to read. TypeSafe calls it the first of a class of models it names "System One models" (Jev (AI model) - Wikipedia, intro).

The only source is a Wikipedia article, clipped with a publication date of 2026-09-19. Most technical facts in it come from TypeSafe. This page marks them as vendor claims.

## Facts

### Release and company

- Jev entered limited early access on 15 September 2026, with a US$40 million seed round led by DCVC (Jev (AI model) - Wikipedia, intro).
- *Forbes* reported that the round valued TypeSafe at US$200 million. Jev was in development in stealth for about two years before the announcement (§ Background).
- Diogo Almeida, Erik Gafni, and Sasha Sheng founded TypeSafe in 2024. Almeida, the chief executive, spent about four years at OpenAI on RLHF, InstructGPT, ChatGPT, and GPT-4, and left in 2024 (§ Background).
- The company positions Jev as a reliable model for automation and software, and as a response to overconfidence in existing models. The article quotes *Forbes*: "We've been optimizing for humans and we're super human at pleasing humans." The article attributes the quote to Almeida only by context. Almeida told *TechCrunch* that conversational models were "lightning in a bottle" but not useful, and describes that disappointment as the origin of the project (§ Background).

### Request and answer design

A request holds a block of *state* (a string, a JSON object, or an array of text) and one or more typed *questions*. The model evaluates every question against the state in a single parallel pass and returns structured answers, not plain text (Jev (AI model) - Wikipedia, § Design & architecture).

Jev has three question types, also called primitives:

| Primitive | Purpose | Returns |
|---|---|---|
| Choice | Select one option from a defined set | Selected option, per-option probabilities, confidence |
| Score | Rate the state against ordered levels | Score, per-level probabilities, confidence |
| Noul | Evaluate a yes/no statement | Probability between 0 and 1 |

The caller defines the answers in advance, so the model cannot return a value outside the supplied schema. Vendor claim: TypeSafe presents this as the end of hallucination and type errors (§ Design & architecture).

### Training

- TypeSafe has not published Jev's architecture, weights, or a technical paper (§ Design & architecture).
- Vendor claim: the model is transformer-based and trained only on synthetic data.
- Vendor claim: the training method is Reinforcement Learning for Calibrated Decisions (RLCD). RLCD optimizes the model's probabilities against outcomes, not against the preferences of human raters.
- Outside observers suggest that Jev may be built on an open-weight LLM.

### Performance claims

All figures are vendor claims, from TypeSafe (Jev (AI model) - Wikipedia, § Performance claims):

- End-to-end response times of 70 to 500 milliseconds.
- 40 to 200 times faster and 40 to 400 times cheaper than frontier LLMs on comparable tasks.
- Peak figures of 193.6 times faster and 444.6 times cheaper, on TypeSafe's own workflows.

The stated caveats, from TypeSafe's own technical notes: members of its model-capabilities team created the workflows; the company acknowledges possible bias; and it says the reported gains are likely at the high end of real-world results. The source reports no independent measurement.

### Name

The name comes from William Stanley Jevons, the 19th-century English economist. His Jevons paradox says that more efficient use of a resource can increase its consumption. Almeida has said the name reflects his expectation that cheaper machine intelligence will lead to far wider deployment (Jev (AI model) - Wikipedia, § Name).

## Related

- [[Post-Training]]: RLCD contrasts with RLHF, which optimizes against human rater preference.
- [[World Models]]: the world-model topic note uses "System 1" for LLM-based agents that map state to action. No source says whether TypeSafe's "System One models" uses the term in the same sense (synthesis).

## Sources

- Jev (AI model) - Wikipedia
