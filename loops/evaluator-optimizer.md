---
id: evaluator-optimizer
version: 0.1.0
status: candidate
category: quality
pattern: evaluator-optimizer + self-refinement
best_for: improving an existing artifact when quality can be scored against explicit criteria
avoid_when: there is no meaningful rubric or feedback cannot change the output
benchmark_target: PLS-100 >= 85
research_basis: [anthropic-effective-agents, self-refine, openai-evals]
---

# Evaluator–Optimizer Loop

## Inputs

- `{{ARTIFACT_OR_TASK}}`
- `{{GOAL}}`
- `{{RUBRIC}}`
- `{{TARGET_SCORE}}`
- `{{CONSTRAINTS}}`
- `{{AUTHORITY}}`
- `{{MAX_ITERATIONS}}`

## Template

```text
GOAL
Improve {{ARTIFACT_OR_TASK}} toward {{GOAL}}.

RUBRIC
{{RUBRIC}}

TARGET
{{TARGET_SCORE}}

CONSTRAINTS
{{CONSTRAINTS}}

LOOP

1. BASELINE
Inspect the current artifact or produce the smallest viable first version. Score it against every rubric dimension and preserve the baseline scores.

2. EVALUATE
Act as an independent evaluator. Identify the few defects that most limit the total outcome. Support each critique with observable evidence from the artifact or environment.

3. PRIORITIZE
Rank defects by expected score gain relative to cost and regression risk. Do not optimize low-value details while a major defect remains.

4. OPTIMIZE
Within {{AUTHORITY}}, make the smallest coherent changes that address the highest-value defects.

5. RE-EVALUATE
Score the new version using the same rubric. Compare delta against baseline and check for regressions in dimensions that were already strong.

6. REFLECT
If improvement was weak, diagnose whether the problem was the proposed fix, the underlying hypothesis or the rubric itself. Update the next action accordingly.

7. REPEAT
Continue from the new state, not from the original plan.

STOP
Stop when the target score is reached, {{MAX_ITERATIONS}} is reached, or expected marginal improvement is too small relative to cost/risk. Do not inflate scores to satisfy the stop condition.
```

## Expected output

A before/after scorecard, concrete artifact changes, remaining defects and evidence that each iteration improved or failed to improve the target outcome.
