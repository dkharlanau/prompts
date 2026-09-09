# Prompts

A deliberately small library of **three canonical agent workflows** for building and improving real products and repositories.

The library covers the full lifecycle without prompt proliferation:

```text
UNDERSTAND / IMPROVE
Deep Run
    ↓
PLAN / CONTROL
Backlog Builder
    ↓
BUILD / VERIFY
Backlog Executor
    ↺
new evidence, defects and blockers feed the backlog
```

These prompts are complementary, not variants of one another.

## 1. Deep Run

[`loops/deep-run.md`](loops/deep-run.md)

Use when the main question is:

> What should materially improve in this product/project, and can the agent carry the best improvement through evidence, implementation and verification?

Core pattern:

`inspect → baseline → independent perspectives → bottleneck → alternatives → red team → experiment gate → execute → verify → independent evaluation → learn → repeat`

Best for:
- product/website/repository improvement;
- difficult strategy or architecture work;
- discovery/growth/value audits;
- research that should turn into verified changes;
- periodic deep reconsideration of a mature project.

Avoid for small deterministic edits.

## 2. Backlog Builder

[`loops/backlog-builder.md`](loops/backlog-builder.md)

Use when the main question is:

> What work should exist in GitHub, in what order, with enough context and verification criteria for an autonomous agent to execute it well?

Core pattern:

`inspect reality → clean backlog → find gaps → challenge candidates → prioritize → write executable issues → adversarial review → repeat`

Best for:
- filling or refreshing a GitHub backlog;
- converting research/product audits into issues;
- merging duplicates and closing stale/obsolete tasks;
- defining dependencies, acceptance criteria and verification;
- preparing a repository for long autonomous execution.

The backlog is treated as a **control plane**, not an idea dump.

## 3. Backlog Executor

[`loops/backlog-executor.md`](loops/backlog-executor.md)

Use when the backlog already exists and the goal is:

> Keep implementing the highest-value actionable work autonomously until no justified executable backlog remains.

Core pattern:

`sync → triage → select → implement → tests → product/UI verification → independent review → update issues → regression checkpoint → continue`

Best for:
- Codex or another coding/product agent with repository access;
- long autonomous implementation sessions;
- working through many GitHub issues without stopping after one task;
- user-facing work where UI must be inspected after implementation;
- sessions that should continue past blocked issues and periodically check regressions.

Do not use it against a low-quality backlog; run Backlog Builder first.

## Which prompt should I use?

| Situation | Prompt |
|---|---|
| "Think deeply and improve this project" | **Deep Run** |
| "Audit/fill/review/prioritize our GitHub backlog" | **Backlog Builder** |
| "Take the backlog and keep building until actionable work is exhausted" | **Backlog Executor** |
| Backlog is messy, then needs implementation | **Backlog Builder → Backlog Executor** |
| Product direction is uncertain before backlog work | **Deep Run → Backlog Builder → Backlog Executor** |

Do not automatically run all three. Start at the stage where the real uncertainty or bottleneck exists.

## Model guidance

See [`MODEL_PROFILES.md`](MODEL_PROFILES.md). Model selection and reasoning effort are configuration, not reasons to duplicate prompt files.

Current high-level guidance:

| Workflow | Strong default |
|---|---|
| Deep Run | **GPT-6 Astra Medium/High** for hardest end-to-end work; **GPT-5.6 Sol High** as strong workhorse |
| Backlog Builder | **GPT-5.6 Sol High** or **GPT-6 Astra Medium** when broad product/research context must be synthesized |
| Backlog Executor | **Codex/Work with GPT-6 Astra** for hardest long autonomous runs; **GPT-5.6 Sol High** for normal repository execution |
| External coding agents | Use the same Backlog Executor; benchmark the exact model/settings before adding recommendations |

## Minimal invocation examples

```text
Use Prompts/Deep Run on <project>.
Outcome: <real outcome>.
Authority: <what may be changed>.
Run through implementation and verification.
```

```text
Use Prompts/Backlog Builder on <project>.
Goal: <project outcome>.
Review and update the actual GitHub backlog directly.
```

```text
Use Prompts/Backlog Executor on <project>.
Goal: <project outcome>.
Work from the current GitHub backlog and continue autonomously until no justified actionable work remains.
Do not deploy unless explicitly authorized.
```

## Repository contract

The target size is **three canonical prompts**.

Do not add a new file because a new domain, role, feature type or model appears. Improve one of these three when a reusable failure mode is discovered. Add a fourth workflow only if repeated benchmark evidence shows that the job cannot be expressed cleanly as Deep Run, Backlog Builder or Backlog Executor.

Files:
- `loops/deep-run.md` — deep product/project improvement loop;
- `loops/backlog-builder.md` — backlog creation, cleanup and prioritization loop;
- `loops/backlog-executor.md` — long autonomous implementation loop;
- `MODEL_PROFILES.md` — model/effort guidance and adapters;
- `BENCHMARKS.md` — evaluation protocols;
- `RESEARCH.md` — research basis;
- `catalog.yaml` — machine-readable metadata;
- `AGENTS.md` — routing and execution rules.

Default principle: **deep thinking when direction is uncertain; a clean backlog when work must be coordinated; relentless verified execution when the backlog is ready.**
