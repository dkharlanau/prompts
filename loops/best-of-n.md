---
id: best-of-n
version: 0.1.0
status: candidate
category: decision
pattern: parallelization + tournament evaluation
best_for: important choices where several fundamentally different solutions are plausible
avoid_when: the solution space is narrow or the task is deterministic
benchmark_target: PLS-100 >= 85
research_basis: [anthropic-effective-agents]
---

# Best-of-N Tournament Loop

## Inputs

- `{{PROBLEM}}`
- `{{CONTEXT}}`
- `{{CONSTRAINTS}}`
- `{{N}}`
- `{{EVALUATION_CRITERIA}}`
- `{{AUTHORITY}}`
- `{{SUCCESS_EVIDENCE}}`

## Template

```text
PROBLEM
{{PROBLEM}}

CONTEXT
{{CONTEXT}}

CONSTRAINTS
{{CONSTRAINTS}}

LOOP

1. GENERATE
Create {{N}} fundamentally different solutions independently. Different solutions must rely on different hypotheses or trade-offs, not cosmetic variations.

2. NORMALIZE
Describe every candidate using the same compact structure:
- core hypothesis;
- mechanism;
- expected upside;
- evidence;
- main risk;
- cost;
- easiest falsification test.

3. EVALUATE
Evaluate candidates only against {{EVALUATION_CRITERIA}}. Do not preserve a candidate merely because it was generated first or described persuasively.

4. ATTACK THE LEADERS
For the top candidates, identify failure modes, unsupported assumptions and cheaper substitutes.

5. SELECT
Choose the strongest surviving candidate, or choose experiment/defer/no-change if none is sufficiently supported.

6. TEST OR EXECUTE
Within {{AUTHORITY}}, run the smallest meaningful test or implementation that can produce {{SUCCESS_EVIDENCE}}.

7. RE-RANK
Use the resulting evidence to rerank the surviving options. Generate a new candidate only if the evidence reveals a genuinely new direction.

STOP
Stop when a candidate meets the success threshold, all candidates fail, or additional rounds are unlikely to alter the ranking.
```

## Expected output

A ranked decision set with explicit evidence and a tested winner rather than a single unchallenged first idea.
