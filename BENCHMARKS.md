# Prompt Loop Benchmarks

The repository uses a small internal benchmark so templates are judged by behavior, not by how sophisticated they sound.

This is **not** an external scientific benchmark. It is a repository-level eval protocol inspired by established agent/evaluation work.

## PromptLoop Score (PLS-100)

Score each dimension from 0–5, then apply the weight.

| Dimension | Weight | 5/5 means |
|---|---:|---|
| Outcome alignment | 20 | The loop optimizes a concrete outcome and resists activity/feature inflation. |
| Feedback-loop quality | 20 | Results are evaluated and materially influence the next iteration. |
| Verification | 15 | Claims are checked against real artifacts, tests, users, data or other observable evidence. |
| Decision quality | 15 | Alternatives, uncertainty and trade-offs are handled explicitly. |
| Actionability | 10 | The loop can move from analysis to safe execution and verification. |
| Evidence discipline | 10 | Facts, observations, hypotheses and unknowns are not silently mixed. |
| Portability | 5 | The template remains useful across unrelated projects with only placeholder substitution. |
| Efficiency | 5 | It avoids redundant roles, repeated analysis and uncontrolled looping. |

`PLS-100 = Σ (dimension_score / 5 × weight)`

## Stability levels

- **experimental** — concept exists but has not passed the internal suite.
- **candidate** — PLS ≥ 75 on at least two domains.
- **stable** — PLS ≥ 85 on at least three materially different domains, with no critical failure.

Suggested test domains:

1. software repository improvement;
2. user-facing product/service improvement;
3. research/growth/strategy task.

## Critical failures

A prompt cannot be stable if a normal run tends to:

- stop after producing a plan when execution was safe and authorized;
- fabricate evidence or treat assumptions as facts;
- loop without a meaningful state change;
- create work primarily to satisfy the prompt rather than the goal;
- ignore explicit constraints or authority boundaries;
- declare success without verification;
- generate duplicate work on repeated runs.

## Loop benchmark protocol

For every candidate template:

1. Run a **one-shot baseline** using only `{{GOAL}}`, `{{CONTEXT}}` and `{{CONSTRAINTS}}`.
2. Run the loop template on the same task.
3. Compare both against the same rubric and observable outcome.
4. Run the template again from the resulting state.
5. Measure whether iteration two discovers new high-value work or merely repeats iteration one.
6. Record failure modes and revise the template if necessary.

## Useful quantitative measures

Depending on domain, attach real metrics rather than inventing a universal score:

- tests passed / issue resolved;
- task completion rate;
- error or regression count;
- time-to-first-value;
- conversion or activation;
- search visibility / qualified discovery;
- human preference or expert score;
- number of unsupported claims;
- cost, latency or number of model/tool calls;
- delta between baseline and post-loop outcome.

## Benchmark record

Store results in this form when a loop is materially evaluated:

```yaml
prompt_id: <id>
prompt_version: <version>
date: <yyyy-mm-dd>
domain: <software|product|service|research|other>
model: <model>
baseline:
  score: <0-100>
loop:
  score: <0-100>
iterations: <n>
observable_outcome: <result>
failures: []
notes: <short notes>
```

The benchmark itself should evolve when real failures expose gaps in the rubric.
