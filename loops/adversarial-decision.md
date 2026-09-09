---
id: adversarial-decision
version: 0.1.0
status: candidate
category: decision
pattern: red-team + pre-mortem + evidence gate
best_for: major features, pivots, investments, architecture choices and other costly proposals
avoid_when: the change is trivial, reversible and already well-evidenced
benchmark_target: PLS-100 >= 85
research_basis: [anthropic-effective-agents]
---

# Adversarial Decision Loop

## Inputs

- `{{PROPOSAL}}`
- `{{GOAL}}`
- `{{CONTEXT}}`
- `{{CONSTRAINTS}}`
- `{{EVIDENCE}}`
- `{{AUTHORITY}}`
- `{{SUCCESS_EVIDENCE}}`

## Template

```text
PROPOSAL
{{PROPOSAL}}

GOAL
{{GOAL}}

CONTEXT
{{CONTEXT}}

CONSTRAINTS
{{CONSTRAINTS}}

LOOP

1. ATTACK
Assume the proposal is wrong. Find the strongest reasons it should not be built or adopted.

2. PRE-MORTEM
Assume the proposal was implemented and later failed. Identify the most plausible causal explanations.

3. EVIDENCE AUDIT
For every decisive claim label it as FACT, OBSERVATION, INFERENCE, HYPOTHESIS or UNKNOWN. Compare against {{EVIDENCE}}.

4. SUBSTITUTE
Find the cheapest simpler action that could achieve the same goal or resolve the same uncertainty.

5. DECIDE
Choose exactly one: BUILD, EXPERIMENT, DEFER, DELETE/REJECT. Base the decision on expected value, evidence, risk, reversibility and cost.

6. ACT
Within {{AUTHORITY}}, perform the chosen safe action when possible. If EXPERIMENT, design the smallest falsifiable test.

7. SECOND ATTACK
Evaluate the resulting evidence or implementation from scratch. Ask whether the original justification still survives.

8. UPDATE
Revise the decision if evidence changed. Do not defend the original proposal for consistency.

STOP
Stop when the decision is robust enough for its stakes or when new external evidence is required. Do not continue debating without a plausible path to changing the decision.
```

## Expected output

A falsifiable decision with explicit evidence, rejected assumptions, cheaper alternatives and a post-action recheck.
