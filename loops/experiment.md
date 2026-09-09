---
id: experiment
version: 0.1.0
status: candidate
category: learning
pattern: hypothesis-test-learn
best_for: product, growth, UX or technical uncertainty that can be reduced with observable evidence
avoid_when: the answer is already available from existing evidence or the proposed test cannot change a decision
benchmark_target: PLS-100 >= 85
research_basis: [openai-evals, reflexion]
---

# Experiment Loop

## Inputs

- `{{QUESTION}}`
- `{{GOAL}}`
- `{{CURRENT_EVIDENCE}}`
- `{{CONSTRAINTS}}`
- `{{AUTHORITY}}`
- `{{DECISION_THRESHOLD}}`

## Template

```text
QUESTION
{{QUESTION}}

GOAL
{{GOAL}}

CURRENT EVIDENCE
{{CURRENT_EVIDENCE}}

CONSTRAINTS
{{CONSTRAINTS}}

LOOP

1. HYPOTHESIS
State the decision-relevant hypothesis precisely. State what evidence would falsify it.

2. UNCERTAINTY
Identify which unknown actually blocks the decision. Ignore interesting questions that would not alter the next action.

3. TEST
Design the smallest, cheapest, safest experiment capable of reducing that uncertainty. Define the metric, comparison and decision threshold before observing results.

4. EXECUTE
Within {{AUTHORITY}}, run the test using the closest available real-world conditions. Do not replace observable evidence with simulated confidence when real evidence is accessible.

5. READ
Separate result from interpretation. Record unexpected behavior and evidence quality.

6. DECIDE
Choose: ADOPT, ITERATE, REJECT, or GATHER EXTERNAL EVIDENCE. Explain what changed relative to the prior belief.

7. LEARN
Preserve the hypothesis, test, result, decision and reusable failure mode so later runs do not repeat the same uncertainty.

8. NEXT LOOP
If uncertainty still blocks {{GOAL}}, formulate the next smallest decision-changing experiment from the new evidence.

STOP
Stop when {{DECISION_THRESHOLD}} is met, the hypothesis is rejected, or further experimentation has lower expected value than making the reversible decision.
```

## Expected output

A compact evidence trail from hypothesis to decision, with explicit falsification criteria and no experimentation for its own sake.
