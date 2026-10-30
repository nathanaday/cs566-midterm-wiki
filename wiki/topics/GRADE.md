---
id: doc-hte8k6
type: topic
kind: concept
description: "GRADE, in CSCI 566 Block 6, is a graph of one agent run: each action is a node, execution edges record which action came next, and dependency edges record which earlier output (a file version) a later action read, with each edge labeled by its evidence."
tags: [machine-learning/cs566-deeplearning]
aliases: [Run graph, Execution edge, Execution layer, Dependency edge, Dependency layer, Data-use edge, Recovered Dependency Layer E_D, Execution and dependency edges, File version recording, path@version, Edge evidence grades, "Observed, declared, and inferred edges", Test What the Dependency Edges Add]
created: 2026-10-05T17:31:20
updated: 2026-10-13T18:22:42
refreshed: 2026-10-13T18:22:42
status: stable
sources: ["[[Block 6 Slides Extended]]"]
up: ["[[LLMs and Graphs]]"]
---

> [!concept] Concept
> 1 source · refreshed 2026-10-13 · #machine-learning/cs566-deeplearning
> Up: [[LLMs and Graphs]]

## Definition

GRADE is the CSCI 566 example of a graph that describes the work of one agent. "An action is a node. An edge records order or data use in a run" ([[Block 6 Slides Extended]], p. 154). A run is "one sequence of actions performed while completing a task" (p. 155).

The graph answers two questions: "Which action came next? Which action supplied an input?" (p. 155). The slide's rule: "Record what happened next and which earlier output was used" (p. 155).

The deck does not expand the name GRADE. The GRADE slides carry the credit "GRADE: v33 teaching assets; local controls dated Sep 29, 2026" (pp. 155–164, 166–168).

## Explanation

### The example run

The agent task is to fix a program whose timeout setting is too short. The run trace is a log of file inspection, edits, tests, and patch submission (p. 155). The run has five actions (pp. 156–157):

| Step | Action | Output or effect |
| --- | --- | --- |
| 1 | Inspect files | Read the existing code: `project/` holds `config.py` and `runner.py`. |
| 2 | Edit config | Write `config.py` with `timeout = 60` in place of `timeout = 30`. |
| 3 | Add a test | Write `test_timeout.py`, which asserts that the timeout is 60. |
| 4 | Run tests | `pytest -q` reports `1 passed`. |
| 5 | Submit patch | The patch modifies `config.py` and adds `test_timeout.py`. |

"The trace records concrete actions and the files they use" (p. 157). A raw-trace record in the example reads: "2 writes config.py@v2; 4 reads config.py@v2" (p. 156).

### Two edge layers on the same nodes

"Both layers use the same five action nodes. Their edges answer different questions" (p. 161).

- **Execution edge.** "An execution edge joins consecutive actions in the logged run" (p. 158). The execution layer records 1 → 2 → 3 → 4 → 5 and answers "What happened next?" For example, the edge 3 → 4 tells us that running tests happened after adding the test (p. 158).
- **Dependency edge.** A dependency edge joins the action that wrote an output to a later action that read it. Step 2 writes `config.py@v2` and step 4 reads `config.py@v2`, so the graph has the edge 2 → 4 (p. 159). This edge skips step 3: "'Later' and 'uses this output' differ" (p. 159). "A dependency edge identifies a particular earlier output" (p. 161).

Read the two layers separately. In the execution layer, 2 → 3 → 4 says when the three actions occurred. In the dependency layer, 2 → 4 says that the test action read the edited config version (p. 162). The figure names the layers "Execution E_X" and "Recovered Dependency Layer E_D" (p. 161).

Two dependency graphs can have the same five actions and the same edge counts but different inputs (p. 165):

- Graph A: 2 → 4, 3 → 4, 4 → 5
- Graph B: 1 → 4, 1 → 5, 2 → 4

"An edge records which earlier output a later action uses" (p. 165).

### Why record a file version

"A file path can refer to different contents at different moments in a run" (p. 160). GRADE writes each access as `path@version` (pp. 159–160):

- Before step 2, `config.py@v1` contains `timeout = 30`.
- After step 2, `config.py@v2` contains `timeout = 60`.
- At step 4, the recorded read names v2. This links the read back to the write at step 2.

"The version tells us which earlier contents the later action read" (p. 160).

Synthesis: without the version, a read of `config.py` at step 4 could match the original file or any earlier write of it. The version gives one exact writer.

### Evidence grades for edges

"An edge should carry the evidence used to establish it" (p. 163). The slides give three grades (pp. 163–164):

| Grade | Label | How the relation is known |
| --- | --- | --- |
| Observed | O | The raw trace explicitly records the write and the later read. |
| Declared | D | Added read/write logging records the relation. |
| Inferred | I | A named rule assumes a dependency from less complete records. |

The rule: "Keep observed, declared and inferred edges distinguishable" (p. 163). The same 2 → 4 relation can have each kind of supporting record. "The edge label tells us how that relation was established" (p. 164). In the example, every O edge is an access that the log records, and "An observed read supplies evidence for the dependency edge" (p. 162).

### Test what the dependency edges add

"A graph can be informative to inspect even when its predictive gain is unresolved" (p. 166). The slide gives a controlled test (p. 166):

1. **Baseline.** Predict run success from simpler summaries, such as step counts.
2. **Add dependencies.** Use dependency information under the same evaluation setup.

The latest control result: "The current within-corpus tests do not establish a gain from edge placement" (p. 166). The slide's conclusion: "A useful representation still needs a controlled test of its added value" (p. 166).

So the predictive value of the dependency edges is unresolved in the deck. The slides do not give the size of the corpus, the model, or the scores.

Synthesis: Graphs A and B on p. 165 have the same counts, so a count baseline cannot tell them apart, but their dependency edges can. The controlled test asks whether that difference helps to predict run success. Up to the controls dated Sep 29, 2026, the answer is not established.

### Summary on the slides

"A graph makes action order and recorded data use explicit" (p. 167):

- **Representation**: actions are nodes, and order and data dependency are different edges.
- **Evidence**: record which accesses support each dependency claim.
- **Evaluation**: compare against simpler baselines and matching controls.

"Inspect the paths, keep their evidence, and test the added value" (p. 167).

### GRADE and MAMA

"GRADE describes one run. MAMA studies communication among several agents" (p. 168). In GRADE a node is one action in a run, and an edge is order or data dependency. In [[MAMA]] a node is one agent in a team, and an edge is allowed communication (p. 168). "A communication graph specifies possible paths. A run graph records what happened" (p. 175). GRADE asks: "Which earlier outputs did the recorded actions use?" (p. 175). See [[Graphs of Agents]].

Synthesis: each GRADE node is one action turn of the [[Agent Loop]], and the execution layer is the order of those turns. The dependency layer is closer to a [[Computational Graphs|computational graph]]: an edge carries the output of one node into a later node. But in GRADE the outputs are file versions, not numbers, and the edges come from a log after the run.

## Related

- [[Graphs of Agents]]: GRADE and MAMA, and what an edge means across Block 6
- [[MAMA]]: a communication graph of several agents, in contrast to the run graph of one agent
- [[Agent Loop]]: the loop whose actions become GRADE nodes
- [[ReAct]]: the Thought, Action, Observation pattern that produces such runs
- [[Graph]]: nodes, edges, and the choice of representation
- [[Computational Graphs]]: a different graph whose edges also carry outputs forward
- [[Model Evaluation]]: baselines and controls for any claim of a gain

## Sources

- [[Block 6 Slides Extended]], pp. 154–168, 175
