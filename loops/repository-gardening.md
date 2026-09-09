---
id: repository-gardening
version: 0.1.0
status: candidate
category: engineering
pattern: inspect-simplify-verify-repeat
best_for: repositories that accumulate agent-generated code, docs, issues, experiments or architectural drift
avoid_when: the repository is small, fresh and has no meaningful entropy
benchmark_target: PLS-100 >= 85
research_basis: [openai-harness-engineering]
---

# Repository Gardening Loop

## Inputs

- `{{REPOSITORY}}`
- `{{GOAL}}`
- `{{CONSTRAINTS}}`
- `{{AUTHORITY}}`
- `{{QUALITY_SIGNALS}}`

## Template

```text
REPOSITORY
{{REPOSITORY}}

GOAL
Reduce entropy while preserving or improving {{GOAL}}.

CONSTRAINTS
{{CONSTRAINTS}}

LOOP

1. INSPECT
Inspect code, documentation, tests, issues, dependencies, generated artifacts and recent changes. Treat actual behavior as stronger evidence than stale prose.

2. FIND ENTROPY
Identify:
- duplicated concepts or implementations;
- stale or contradictory documentation;
- abandoned experiments;
- obsolete issues or plans;
- dead files/dependencies;
- architectural boundary violations;
- inconsistent patterns;
- unnecessary abstractions;
- complexity introduced without current value.

3. PRIORITIZE
Rank cleanup by expected reduction in maintenance cost, agent confusion and regression risk. Prefer deleting or consolidating before rewriting.

4. CLEAN
Within {{AUTHORITY}}, make a small coherent cleanup batch. Do not combine unrelated feature development with gardening unless required to preserve behavior.

5. VERIFY
Run relevant tests/build/checks and inspect {{QUALITY_SIGNALS}}. Confirm useful behavior was not lost.

6. COMPARE
State what became simpler, smaller, clearer or more mechanically verifiable. If entropy merely moved elsewhere, treat the iteration as failed.

7. RECORD
Update the system of record only where the cleanup changed a durable rule or removed stale knowledge.

8. REPEAT
Re-scan the changed repository and choose the next highest-value entropy source.

STOP
Stop when remaining cleanup has low expected value, requires product decisions outside {{AUTHORITY}}, or would create more churn than clarity.
```

## Expected output

A smaller or clearer verified repository state, with explicit removed entropy and no hidden feature expansion.
