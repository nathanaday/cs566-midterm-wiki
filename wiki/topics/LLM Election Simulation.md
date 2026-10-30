---
id: doc-gcgfrn
type: topic
kind: concept
description: "The presenters' study in CSCI 566 Block 7, shown as an optional research example: LLMs get demographic personas and vote, the votes are summed into state-level U.S. election results, and the results are checked for accuracy (WAE, WMSE), systematic bias (BM), stereotypes, and hyper-accuracy distortion."
tags: [machine-learning/cs566-deeplearning]
aliases: [A Large-Scale Simulation on LLMs for Decision-Making in Political Science, LLMs for Human Behavior Simulation, LLM persona simulation, LLM voting simulation, "Voting simulation pipelines (V1, V2, V3)", Multi-Step Reasoning with Ideology Inference, Bias Metric (BM), WAE, WMSE, Hyper-accuracy distortion, Stereotype over-amplification, ANES, Ballotpedia]
created: 2026-10-12T16:58:10
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 7 Slides]]"]
up: ["[[Large Language Models]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[Large Language Models]]

## Definition

LLM Election Simulation is the study "A Large-Scale Simulation on LLMs for Decision-Making in Political Science". The slides call it "Our work" ([[Block 7 Slides]], p. 273). The study gives a large language model (LLM) a demographic persona and asks it to vote. Then it sums the votes of all personas into state-level U.S. presidential election results (pp. 277, 279).

The Block 7 deck presents the study as an optional research example. Its "Optional Research Examples" slide lists "LLM behavior: A research example of how adaptation changes behavior" and says "These sections can be taught separately from the core workflow" ([[Block 7 Slides]], p. 272). The slides do not list the authors of the study.

## Explanation

### LLMs for human behavior simulation

The general idea: "Give LLMs a specific persona –Let LLMs simulate the corresponding behaviours" ([[Block 7 Slides]], p. 275). The slide names three related studies (p. 275):

- Public opinion: confirmation bias (Chuang et al., 2024).
- Economics: utility theory (Xie et al., 2024).
- Social psychology: collaboration (Zhang et al., 2024).

### Why a voting task

The inspiration is a question: given a persona, can LLMs "Vote like Real Human"? ([[Block 7 Slides]], p. 276). The slide gives two reasons to choose the voting simulation task (p. 276):

1. It is a complex decision-making task, with demographic, ideological, spatial, and external factors.
2. It is easy to evaluate, because state- and county-level election results are public.

The slide names two difficulties (p. 276):

1. "LLMs' Bias from Pretrain Corpus (Feng et al, 2023)". A chart places many language models (BERT, RoBERTa, GPT-2 to GPT-4, LLaMA, Alpaca, and others) on a left-right and authoritarian-libertarian grid.
2. "Lack of Voter-level Data / shifting political context".

The research questions (p. 276):

- RQ1: How can LLMs be used to simulate human decision-making in political science?
- RQ2: How do different LLMs perform, and how robust are their election simulations?
- RQ3: What limitations arise when using LLMs to model political decision-making?

### Data and models

- **ANES** ("Public ANES (real human samples)"): demographic information, political ideology, and voting records from human respondents ([[Block 7 Slides]], pp. 277, 280). The slide shows the ANES Data Center web page (p. 277).
- **1:1 synthetic data**: synthetic personas. A figure covers the rest of this line on the slide (p. 277).
- **LLMs**: GPT-4o, Llama3.1-70B, Qwen-72B, DeepSeek-V3 (p. 277).
- **Time range**: two lines that start "Evaluation Within pretr…" and "Test Beyond pretrain co…". A figure covers the rest of both lines (p. 277).

### Pipelines V1, V2, V3

Each pipeline runs once for each persona. The state-level simulation sums the results of all personas ([[Block 7 Slides]], pp. 277, 279). The diagram names the versions "Demographic-only Prompting", "Single-step Prompting with Time-based Information", and "Multi-step Reasoning with Contextual Information" (p. 277).

- **V1: direct prompt on each persona.** The LLM gets a specific persona and votes "in one single prompt (Argyle et al., 2023)" (p. 278). The persona holds age, gender, ethnicity, marital status, household size, presence of children, education level, occupation, individual income, family income, and place of residence. The prompt gives the current year and asks: "As of today, will you vote for the Democratic Party (Joe Biden), the Republican Party (Donald Trump), or do you have no preference?" The options are Democratic, Republican, and No Preference (p. 278).
- **V2: with time-sensitive information.** V2 uses the V1 direct prompt and adds "timely info" from **Ballotpedia**: campaign agendas, key policy positions, and candidates' biographies (p. 278).
- **V3: multi-step reasoning with ideology inference.** V3 breaks the thinking chain into multiple steps. An intermediate step generates the persona's political ideology (p. 279). The diagram flow (p. 279):
  1. Inputs: a temporary policy position and an individual demographic persona.
  2. Prompt: "When it comes to politics, you would describe yourself as ...". The LLM answers "When it comes to politics, I would describe myself as ...". This is the political ideology inference.
  3. The ideology and the persona form an extended persona. The candidates' information is added.
  4. The LLM completes "As of today, I will vote for ...".

The theoretical background of V3 is "A significant increase of polarization" and the link "Political Ideology <-> Party Identification" (Levendusky, 2009; Abramowitz and Saunders, 2008; Bornschier et al., 2021) (p. 279). The slide reports a "Significant Improvement" in voting behavior simulation, in both public benchmark validation and state-level simulations (p. 279). The diagrams mark the V1 result "Biden Win Ohio 2020" as wrong and the V3 result "Trump Win Ohio 2020" as correct (pp. 277, 279).

### Results on ANES

The chart reports the ratio P(s) = R / (R + D), where R and D are the Republican and Democratic votes ([[Block 7 Slides]], p. 280).

| Pipeline | ANES 2016 | ANES 2020 |
|---|---|---|
| Ground truth | 0.477 | 0.412 |
| V1 (vanilla) | 63.25% | 30.14% |
| V2 | 66.38% | 10.02% |
| V3, real ideology | 46.84% | 46.78% |
| V3, LLM-generated ideology | 48.34% | (not shown) |

The slide says "LLM on Generated Ideology performs almost same as on Real Ideology" and "2020's variables is partially missing" (p. 280). It gives "4,270 / 8,280 samples" and does not say which number belongs to which year (p. 280).

### Results on synthetic data: 2020

The 2020 simulation uses "1/1000 of total population ~ 330,000 personas" ([[Block 7 Slides]], p. 281). The slide claims (p. 281):

- "V3 Simulate in all 'red' and 'blue' states accurately".
- V3 "correctly predicted in 9 out of 11 swing and tipping point states", "with only minor deviations in North Carolina (NC) and Arizona (AZ)".

GPT-4o simulation of the 2020 U.S. election (p. 281):

| Metric | V1 (%) | V2 (%) | V3 (%) |
|---|---|---|---|
| WAE | 22.78 | 14.97 | 5.24 |
| WMSE | 5.46 | 2.34 | 0.37 |
| Bias Metric (BM) | -22.78 | -14.97 | 0.34 |

State-level results (a subset), as R / (R + D) in percent (p. 281):

| State | 2020 result | V1 | V2 | V3 |
|---|---|---|---|---|
| OH | 54.08 | 30.78 | 39.18 | 56.13 |
| WI | 49.68 | 24.26 | 37.26 | 45.51 |
| FL | 51.69 | 30.49 | 39.70 | 53.51 |
| IL | 41.34 | 12.20 | 21.67 | 36.09 |

### Results on synthetic data: 2024

The slide warns: "2024 evaluation period. Model-specific training cutoffs and data leakage need separate checks" ([[Block 7 Slides]], p. 282). It runs a cross-pipeline and cross-model evaluation. It says the GPT-4o V3 pipeline does better than the others (V1 and V2 under the same LLM) (p. 282).

Multi-LLM simulation of the 2024 U.S. election (pp. 282, 284):

| Metric | GPT-4o V1 | GPT-4o V2 | GPT-4o V3 | LLaMA3-70B V1 | LLaMA3-70B V2 | LLaMA3-70B V3 | Qwen-72B V3 | DeepSeek-V3 V3 | Zhang et al., 2024 |
|---|---|---|---|---|---|---|---|---|---|
| WAE | 21.35 | 25.96 | 3.49 | 19.97 | 10.23 | 6.88 | 10.66 | 14.57 | 4.70 |
| WMSE | 4.83 | 6.89 | 0.22 | 4.15 | 1.42 | 0.68 | 1.47 | 2.43 | 0.30 |
| BM | -21.35 | -25.96 | -2.95 | -19.97 | -10.23 | -5.44 | -9.47 | -14.57 | 1.26 |

### Metrics: WAE, WMSE, and the Bias Metric

- **WAE and WMSE**: "smaller the number, more accurate the simulation" ([[Block 7 Slides]], p. 281). The slides do not expand the names or give the formulas.
- **Bias Metric (BM)**: "A metric which quantifies systematic bias by measuring whether simulated personas consistently favor one party over the other". BM > 0 means Republican-leaning. BM < 0 means Democratic-leaning (p. 284). The slide gives equation (A6) (p. 284):

$$\mathrm{BM} = \frac{\sum_{s \in S} E(s) \cdot (P(s) - R(s))}{\sum_{s \in S} E(s)}$$

The slides do not define $S$, $E(s)$, or $R(s)$. The ANES chart labels $P(s)$ as the ratio R / (R + D) (p. 280).

### Beyond accuracy

**Systematic bias.** In 2020, GPT-4o V1 and V2 lean Democratic (BM -22.78 and -14.97), and V3 is near zero (0.34). In 2024, every LLM pipeline has a negative BM, from -2.95 (GPT-4o V3) to -25.96 (GPT-4o V2). Only the Zhang et al., 2024 baseline is positive (1.26) ([[Block 7 Slides]], p. 284).

**Stereotypes: "Over-amplification of Demographic Voting Patterns".** The slide compares the "Vote Preference Diff (%)" of each demographic group in GPT-4o V1, V2, and V3 with a human sample from Pew 2020 ([[Block 7 Slides]], p. 285). The V3 and Pew values, read from the bar charts:

| Group | GPT-4o V3 | Human sample (Pew) |
|---|---|---|
| Male | -47.6 | -2.0 |
| Female | 45.6 | 11.1 |
| White | -20.0 | -12.2 |
| Hispanic | 34.1 | 21.6 |
| Black | 72.7 | 84.0 |
| Asian | 89.5 | 44.0 |
| 65+ | -15.6 | -4.0 |
| 50-64 | -17.1 | -6.0 |
| 30-49 | 19.8 | 12.0 |
| 18-29 | 11.6 | 24.0 |
| Some college or less | -10.7 | -8.0 |
| College grad+ | 71.6 | 24.0 |
| High school or less | -31.8 | -15.0 |
| Some college | 15.0 | -1.0 |
| College graduate | 67.0 | 14.0 |
| Postgraduate | 81.7 | 35.0 |

The slide quotes: "Large language models that replace human participants can harmfully misportray and flatten identity groups" (wang et al., 2025) (p. 285).

**Hyper-accuracy distortion: "Overestimation of ideological influence".** A logistic regression predicts the voting outcome from political ideology ([[Block 7 Slides]], p. 286). The chart plots voting preference (Democrat to Republican) against political ideology (Liberal, Moderate, Conservative). The curve for the human sample (ANES dataset) is flatter: "human decision making process is more complex & dynamic". The curves for the GPT-4o simulations of 2020 and 2024 are much steeper. The slide says the "LLM oversimplified this decision-making process – like a shortcut" (p. 286).

### Reducing political bias: theory-grounded prompts

The discussion returns to RQ3 under the heading "Discussion : How to fulfilling the gap" ([[Block 7 Slides]], p. 283). The slide "How to reduce political bias of LLM (agents)?" adds two prompts to the pipeline (p. 287):

- **Social Identity Theory**, attached to the individual synthetic persona: "As [a young, suburban moderate voter] in [Pennsylvania], you are part of a community that includes both Republican and Democratic supporters. How do social interactions shape your decision?"
- **Information Processing Theory**, attached to the ideology step: "Recently, the [candidate] from [party] have initiated [policy issue]. How does this affect your stance?"

In this diagram, the ideology step is a "Conservative-liberal Spectrum" (p. 287). The goal: "Improve realism by aligning synthetic personas with real-world voter concerns." The next step: "Experiment with the new reasoning framework on sample personas from swing states" (p. 287). The slide gives no results for this framework.

### Points the slides leave open

These notes are synthesis, not claims from the slides.

- The slides name the Llama model "Llama3.1-70B" on p. 277 and "LLaMA3-70B" in the 2024 tables (pp. 282, 284).
- The slide titled "2024 U.S. Election Simulation" also repeats the 2020 table (p. 282).
- The stereotype table does not fit "over-amplification" in every row. For Black voters (72.7 against 84.0) and voters aged 18-29 (11.6 against 24.0), the V3 value is smaller than the human value (p. 285). The slide does not say which party a positive "Vote Preference Diff" favors.
- In many columns, BM is the negative of WAE: GPT-4o V1 and V2 in both years, LLaMA3-70B V1 and V2, and DeepSeek-V3 V3 (pp. 281, 282, 284). The slides do not explain this.
- The deck lists the study as an example of "how adaptation changes behavior" (p. 272). The pipelines on the slides change only the prompt. The slides show no change to model weights (pp. 277–279, 287).

## Related

- [[In-Context Learning]]: the pipelines change LLM behavior through the prompt only.
- [[Chain-of-Thought Prompting]]: V3 also splits the decision into intermediate steps.
- [[Test Set Contamination]]: the 2024 slide asks for checks on training cutoffs and data leakage.
- [[TrustLLM]]: another CSCI 566 example of measuring LLM behavior beyond accuracy.
- [[TOD]]: the other optional research example in Block 7.
- [[Transfer Learning]]: the core Block 7 workflow that these examples follow.
- [[Updating LLMs]]: ways to change LLM behavior after pretraining.

## Sources

- [[Block 7 Slides]], pp. 272–287
