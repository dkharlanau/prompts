# Prompts

A compact library of reusable **agent loops** for improving products, services, software and repositories.

This repository intentionally avoids large collections of one-shot prompts. A prompt belongs here only if it defines a repeatable loop with an explicit goal, feedback, verification and stop condition.

## How to use

1. Pick a loop from the catalog below.
2. Fill the placeholders such as `{{PROJECT}}`, `{{GOAL}}`, `{{CONTEXT}}`, `{{CONSTRAINTS}}`, `{{METRICS}}` and `{{AUTHORITY}}`.
3. Give the agent access to the real system of record when possible: repository, product, analytics, issues, tests and current user experience.
4. Run the loop until its stop condition is reached, not until the first plan is produced.
5. Record outcomes and failures so the next run starts with better evidence.

You can also invoke a template by reference, for example:

> Use `loops/autonomous-improvement.md` for `<project>`. Goal: `<outcome>`. Constraints: `<constraints>`.

## Core loops

| Loop | Best for | Core pattern |
|---|---|---|
| [Autonomous Improvement](loops/autonomous-improvement.md) | General project development | inspect → prioritize → execute → verify → learn |
| [Council](loops/council.md) | Ambiguous product/strategy decisions | independent perspectives → conflict → synthesis |
| [Best-of-N Tournament](loops/best-of-n.md) | Important choices with multiple viable directions | parallel alternatives → blind evaluation → winner |
| [Adversarial Decision](loops/adversarial-decision.md) | Avoiding weak ideas and feature inflation | proposal → attack → evidence test → decision |
| [Evaluator–Optimizer](loops/evaluator-optimizer.md) | Raising quality of an existing output | build → score → critique → improve |
| [Experiment](loops/experiment.md) | Product/growth hypotheses | hypothesis → smallest test → evidence → decision |
| [Discovery-to-Value](loops/discovery-to-value.md) | Products/services that need acquisition and activation | intent → discovery → value → return loop |
| [Repository Gardening](loops/repository-gardening.md) | Long-lived agent-developed repositories | detect entropy → simplify → verify → repeat |

## Quality standard

Every stable loop should have:

- a concrete outcome rather than an activity goal;
- inputs and authority boundaries;
- an explicit iterative feedback mechanism;
- independent evaluation where useful;
- verification against the real artifact or environment;
- a stop condition;
- a way to preserve learning between runs;
- low dependence on project-specific wording.

See [BENCHMARKS.md](BENCHMARKS.md) for the internal evaluation rubric and [RESEARCH.md](RESEARCH.md) for the research basis.

## Template variables

Common placeholders:

- `{{PROJECT}}` — product, service, repository or system.
- `{{GOAL}}` — measurable desired outcome.
- `{{CONTEXT}}` — only context that materially affects decisions.
- `{{TARGET}}` — user, customer, system or audience.
- `{{CONSTRAINTS}}` — limits and non-goals.
- `{{AUTHORITY}}` — what the agent may inspect/change without asking.
- `{{METRICS}}` — evidence used to judge success.
- `{{STOP_CONDITION}}` — when further looping has low expected value.

## Design principle

Prefer a small number of strong composable loops over a large prompt catalog. New templates should introduce a genuinely different decision or feedback pattern, not merely rename an existing prompt for another domain.
