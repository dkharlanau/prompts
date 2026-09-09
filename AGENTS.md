# AGENTS.md

This repository provides exactly two canonical reusable workflows:

- `loops/deep-run.md`
- `loops/backlog-executor.md`

Deep Run has two modes:
- `BACKLOG` — deep analysis whose output is a cleaned, prioritized, execution-ready backlog.
- `EXECUTE` — deep analysis whose output is a changed and verified project state.

## Core rule

Do not create domain-specific prompt variants. New domains, roles, products, websites, services or model names should normally use one of these two workflows with different inputs and evidence.

A new prompt file is justified only when repeated benchmark evidence shows a fundamentally different job that cannot be expressed cleanly as Deep Run BACKLOG, Deep Run EXECUTE, or Backlog Executor.

## Routing

Choose by the user's actual job.

### Deep Run — EXECUTE
Use when direction, diagnosis or the next highest-leverage improvement is uncertain and the agent should implement justified changes now.

Typical shorthand:
- `run a deep loop`
- `improve this project`
- `find the next milestone and do it`
- `audit and improve`
- `think from multiple roles and implement`

Default ordinary Deep Run requests to EXECUTE unless backlog-only intent is clear.

### Deep Run — BACKLOG
Use when direction/diagnosis still requires deep reasoning, but the desired durable output is the GitHub backlog rather than immediate product implementation.

Typical shorthand:
- `fill the backlog`
- `review our issues`
- `add what is missing`
- `prioritize the backlog`
- `turn this research into GitHub work`
- `prepare work for Codex/Kimi`

The expected result is an updated control plane. Do not implement product changes unless the user explicitly extends authority.

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

Do not chain workflows mechanically.

Use:
- `Deep Run BACKLOG → Backlog Executor` when analysis should prepare durable work for Codex/Kimi/another coding agent;
- `Deep Run EXECUTE` alone when ChatGPT/Work has enough authority/tools to make the best changes immediately;
- `Backlog Executor` alone when backlog quality and direction are already strong.

During Deep Run EXECUTE, create/update issues only for durable follow-up work when useful; do not convert execution into backlog inflation.

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

- Deep Run EXECUTE: GPT-6 Astra Medium; High for unusually hard/ambiguous/consequential work. GPT-5.6 Sol High is a strong default workhorse.
- Deep Run BACKLOG: GPT-5.6 Sol High for normal repository/product backlog reasoning; GPT-6 Astra Medium when the backlog depends on broad research, product synthesis or very large context.
- Backlog Executor: prefer a coding-capable environment such as Codex/Work. GPT-6 Astra is preferred for the hardest long autonomous repository runs; GPT-5.6 Sol High is strong for normal execution.

Do not assume maximum reasoning effort is always superior. Benchmark model × effort × workflow/mode.

For external agents/models (for example Kimi or future coding agents), use Backlog Executor first. Add a profile only after the exact model/version and settings have been tested on comparable tasks.

## Evaluation contract

Use `BENCHMARKS.md` for prompt/model evaluation.

Evaluate each job on its real outcome:

- Deep Run EXECUTE: did the project measurably improve?
- Deep Run BACKLOG: did backlog quality, prioritization and executability improve without issue inflation?
- Backlog Executor: how much high-value backlog was correctly completed with verification, low regressions and accurate issue state?

When a run exposes a reusable failure mode, improve the relevant canonical workflow, model guidance or benchmark. Do not add another prompt by default.
