# AGENTS.md

This repository provides one canonical reusable workflow: `loops/deep-run.md`.

## Core rule

Do not create domain-specific prompt variants. Product, service, website, repository, growth, architecture and research work should use the same Deep Run with different inputs and evidence.

A new prompt file is justified only if repeated benchmark evidence shows a fundamentally different workflow is required and cannot be expressed as an optional Deep Run phase. The default response to a new failure pattern is to improve `deep-run.md`, not to add another prompt.

## When asked to use this library

1. Read `loops/deep-run.md` and `MODEL_PROFILES.md`.
2. Inspect the target project's real context before asking for missing inputs.
3. Fill known placeholders from the target repository, current conversation, issues, product, analytics, tests and other sources of truth.
4. Infer only routine details. Ask only for consequential/irreversible information that cannot be resolved from available context.
5. Execute the instantiated Deep Run against the target project. Do not merely return the filled prompt unless the user explicitly asks for prompt text.
6. Carry the loop through implementation and verification when authority/tools permit. Do not stop after analysis or planning.
7. Respect deployment, merge, publishing and other irreversible-action constraints from the target project/user.
8. Preserve the same success evidence across before/after evaluation.
9. Stop when marginal value becomes low, the goal is met, external evidence is required, or the next consequential action is outside authority.

## Model selection

Use `MODEL_PROFILES.md` as the current source of truth.

Default order for a substantial Deep Run when available:

1. GPT-6 Astra Medium for hardest end-to-end work.
2. GPT-6 Astra High when the task is unusually difficult, ambiguous or consequential, or Medium materially underperformed.
3. GPT-5.6 Sol High as the default full-run workhorse.
4. GPT-5.6 Sol Extra High for especially difficult one-off runs when available.
5. GPT-5.6 Luna/Think for bounded sub-work or lower-capability baseline, not as the preferred sole final evaluator when stronger models are available.

Do not assume that maximum reasoning effort is always superior. Prefer benchmarked model×effort combinations.

If the user names a model not recognized in current verified profiles, check current official model documentation before inventing behavior or mapping names.

## How to interpret user shorthand

Examples:

- `Use Prompts for Ptichi and run deep` → instantiate and execute `deep-run.md` with Ptichi's current project context.
- `Pick the best prompt for this repo` → use Deep Run unless the task is too small to justify it.
- `Run another loop` → re-run Deep Run from the project's changed current state, not from the previous plan.
- `Use the Astra version` → use the same Deep Run plus the Astra adapter from `MODEL_PROFILES.md`.
- `Use Sol` → use the same Deep Run plus the Sol guidance from `MODEL_PROFILES.md`.

## Evaluation contract

Use `BENCHMARKS.md` when evaluating the prompt or a model profile.

Never claim that a model, reasoning effort or prompt version is better because it sounds stronger or because vendor documentation says it is more capable. Record comparable runs against observable outcomes.

When a real run exposes a reusable failure mode, decide whether to:

- improve the canonical prompt;
- improve model guidance;
- improve the benchmark;
- or leave it project-specific.

Do not preserve ephemeral reasoning as repository documentation.
