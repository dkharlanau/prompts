---
id: autonomous-improvement
version: 0.1.0
status: candidate
category: general
pattern: orchestrator-workers + evaluator-optimizer + reflection
best_for: continuous improvement of a product, service, repository or system
avoid_when: the task is a small deterministic edit with a clear solution
benchmark_target: PLS-100 >= 85
research_basis: [anthropic-effective-agents, openai-harness-engineering, reflexion]
---

# Autonomous Improvement Loop

## Inputs

- `{{PROJECT}}`
- `{{GOAL}}`
- `{{CONTEXT}}`
- `{{CONSTRAINTS}}`
- `{{AUTHORITY}}`
- `{{METRICS}}`
- `{{STOP_CONDITION}}`

## Template

```text
GOAL
Improve {{PROJECT}} toward {{GOAL}}.

CONTEXT
{{CONTEXT}}

CONSTRAINTS
{{CONSTRAINTS}}

AUTHORITY
{{AUTHORITY}}

SUCCESS EVIDENCE
{{METRICS}}

LOOP

1. INSPECT
Inspect the real current state and relevant sources of truth. Do not assume documentation matches reality.

2. BOTTLENECK
Identify the single highest-leverage constraint preventing the goal. Distinguish facts, observations, hypotheses and unknowns.

3. OPTIONS
Generate materially different responses to that bottleneck, including simplification, deletion, experimentation and doing nothing.

4. SELECT
Choose the option with the best expected outcome relative to evidence, risk, cost and reversibility.

5. EXECUTE
Within {{AUTHORITY}}, make the smallest coherent change capable of producing meaningful progress. Do not stop at a plan when safe execution is authorized.

6. VERIFY
Test the resulting state against {{METRICS}} and inspect the real artifact or environment. Check for regressions and unintended complexity.

7. CRITIQUE
Independently identify what remains weak, unsupported or worse than before.

8. LEARN
Preserve reusable findings, decisions and failures in the project's system of record when appropriate.

9. REPEAT
Re-inspect the changed state and identify the new highest-leverage bottleneck. Do not mechanically continue the previous plan.

STOP
Stop when {{STOP_CONDITION}}, when the goal is satisfied, or when another iteration has low expected marginal value. Report remaining uncertainty explicitly.
```

## Expected output

A changed and verified state, plus concise evidence of what improved, what did not, and the next unresolved bottleneck.
