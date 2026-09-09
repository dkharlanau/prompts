---
id: council
version: 0.1.0
status: candidate
category: decision
pattern: parallelization + adversarial synthesis
best_for: ambiguous product, strategy or architecture decisions with competing perspectives
avoid_when: evidence already points to a clear low-risk action
benchmark_target: PLS-100 >= 85
research_basis: [anthropic-effective-agents]
---

# Council Loop

## Inputs

- `{{PROJECT}}`
- `{{QUESTION}}`
- `{{ROLES}}`
- `{{CONTEXT}}`
- `{{CONSTRAINTS}}`
- `{{DECISION_CRITERIA}}`
- `{{AUTHORITY}}`

## Template

```text
QUESTION
For {{PROJECT}}, decide: {{QUESTION}}

CONTEXT
{{CONTEXT}}

CONSTRAINTS
{{CONSTRAINTS}}

COUNCIL
{{ROLES}}

If roles are not supplied, infer only the few perspectives that can materially change the decision.

LOOP

1. INSPECT
Inspect the current state and available evidence before role analysis.

2. INDEPENDENT VIEWS
Each role analyzes independently and states:
- strongest finding;
- strongest evidence;
- biggest uncertainty;
- preferred action;
- what would change its mind.
Do not allow early consensus.

3. CONFLICT
Find disagreements that imply different actions. Cross-examine the evidence and assumptions behind them.

4. OPTIONS
Produce a small set of materially different choices. Include a simpler/no-change option when legitimate.

5. DECIDE
Evaluate options only against {{DECISION_CRITERIA}}. Separate confidence from preference.

6. ACT
Within {{AUTHORITY}}, implement or test the selected reversible action when execution is justified.

7. RECONVENE
After new evidence or a state change, rerun only the roles whose conclusions could materially change. Compare their new positions with the previous round.

STOP
Stop when one option is sufficiently supported for the decision's stakes, or when the remaining uncertainty requires external evidence rather than more internal debate.
```

## Expected output

A decision trace containing disagreements, decisive evidence, selected action, confidence, unresolved uncertainty and post-action review.
