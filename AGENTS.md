# AGENTS.md

This repository is a compact library of reusable agent loops.

## Core rule

Do not grow the repository by adding domain-specific prompt variants. Add a new prompt only when it introduces a genuinely different loop, decision pattern or feedback mechanism.

## When asked to use this library

1. Read `README.md` and inspect the available loop metadata.
2. Select the **simplest loop that matches the current goal**.
3. Fill placeholders from the target project's real context. Do not ask for values that can be resolved by inspecting the target repository, product, issues, analytics or prior project context.
4. Execute the instantiated prompt against the target project; do not merely return the filled template unless the user asked for the prompt itself.
5. Respect the target project's authority and deployment constraints.
6. When useful, compose loops deliberately rather than merging them into a giant prompt. Example: `council` for decision discovery → `experiment` for uncertainty → `evaluator-optimizer` for refinement.
7. Do not claim a benchmark result unless the benchmark was actually run and observable evidence was recorded.

## Selection guide

- Continuous project improvement → `autonomous-improvement`
- Ambiguous decision requiring multiple perspectives → `council`
- Several plausible directions → `best-of-n`
- Expensive or suspicious proposal → `adversarial-decision`
- Existing artifact needs measurable refinement → `evaluator-optimizer`
- Decision blocked by uncertainty → `experiment`
- Acquisition/activation/return journey → `discovery-to-value`
- Repository drift/duplication/stale knowledge → `repository-gardening`

## Prompt authoring contract

Every loop file should remain generic and contain:

- YAML metadata;
- explicit inputs/placeholders;
- a repeatable feedback loop;
- verification;
- stop condition;
- expected output.

Prefer outcome-driven language. Avoid model-specific tricks unless evidence shows they are necessary.

## Evaluation

Use `BENCHMARKS.md` for internal evaluation. New loops start as `experimental` or `candidate`; promote to `stable` only after recorded cross-domain evaluation.

Use `RESEARCH.md` for research provenance. Research should explain why a pattern is plausible, not be used as decorative authority.
