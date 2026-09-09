# AGENTS.md

This repository provides exactly three canonical reusable workflows:

- `loops/deep-run.md`
- `loops/backlog-builder.md`
- `loops/backlog-executor.md`

## Core rule

Do not create domain-specific prompt variants. New domains, roles, products, websites, services or model names should normally use one of these three workflows with different inputs and evidence.

A new prompt file is justified only when repeated benchmark evidence shows a fundamentally different job that cannot be expressed cleanly as deep improvement, backlog construction, or backlog execution.

## Routing

Choose by the user's actual job:

### Deep Run
Use when direction, diagnosis or the next highest-leverage improvement is uncertain.

Typical shorthand:
- `run a deep loop`
- `improve this project`
- `find the next milestone`
- `audit and improve`
- `think from multiple roles and implement`

### Backlog Builder
Use when the main artifact is the GitHub backlog.

Typical shorthand:
- `fill the backlog`
- `review our issues`
- `add what is missing`
- `prioritize the backlog`
- `turn this research into GitHub work`

The expected result is an updated control plane, not implementation unless the user explicitly combines planning and execution.

### Backlog Executor
Use when a usable backlog exists and the user wants sustained implementation.

Typical shorthand:
- `work through the backlog`
- `run autonomously`
- `keep coding until the backlog is done`
- `Codex loop`
- `execute everything actionable`

The executor must continue past independently blocked issues, verify changes, keep issues synchronized and stop only when meaningful actionable work is exhausted or outside authority.

## Combination rules

Do not chain all workflows mechanically.

Use:
- `Deep Run → Backlog Builder` when deep research/strategy should become durable work;
- `Backlog Builder → Backlog Executor` when the backlog needs preparation before autonomous coding;
- `Deep Run → Backlog Builder → Backlog Executor` for a full project cycle when both direction and execution backlog are initially weak;
- `Backlog Executor` alone when backlog quality is already strong.

During Backlog Executor, create new issues only for genuine discovered defects, blockers or important follow-ups. Do not expand the backlog merely to prolong execution.

## When asked to use this library

1. Read the selected workflow and `MODEL_PROFILES.md`.
2. Inspect the target project's real context before asking for missing inputs.
3. Fill known placeholders from the repository, current conversation, issues, product, analytics, tests and other sources of truth.
4. Infer routine/reversible details; ask only when a missing answer could materially change a consequential or irreversible outcome.
5. Execute the workflow against the target project. Do not merely return prompt text unless the user asked for it.
6. Respect branch, deployment, merge, publishing and other irreversible-action constraints.
7. Preserve observable verification evidence.
8. Do not claim completion from code changes alone when user/product behavior can be checked.

## Model selection

Use `MODEL_PROFILES.md` as the current source of truth.

General defaults when available:

- Deep Run: GPT-6 Astra Medium; High for unusually hard/ambiguous/consequential work. GPT-5.6 Sol High is a strong default workhorse.
- Backlog Builder: GPT-5.6 Sol High for normal repository/product backlog work; GPT-6 Astra Medium when the backlog depends on broad research, product synthesis or very large context.
- Backlog Executor: prefer a coding-capable environment such as Codex/Work. GPT-6 Astra is preferred for the hardest long autonomous repository runs; GPT-5.6 Sol High is strong for normal execution.

Do not assume maximum reasoning effort is always superior. Benchmark model × effort × workflow.

For external agents/models (for example Kimi or future coding agents), use the same workflow text first. Add a profile only after the exact model/version and settings have been tested on comparable tasks.

## Evaluation contract

Use `BENCHMARKS.md` for prompt/model evaluation.

Evaluate each workflow on its real job:

- Deep Run: did the project measurably improve?
- Backlog Builder: did backlog quality, prioritization and executability improve without issue inflation?
- Backlog Executor: how much high-value backlog was correctly completed with verification, low regressions and accurate issue state?

When a run exposes a reusable failure mode, improve the relevant canonical workflow, model guidance or benchmark. Do not add a fourth prompt by default.
