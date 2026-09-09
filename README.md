# Prompts

A deliberately small library of **two canonical agent workflows** for building and improving real products and repositories.

```text
DEEP RUN
  ├─ BACKLOG mode  → deeply analyze → create/clean/prioritize execution-ready work
  └─ EXECUTE mode  → deeply analyze → implement → verify → repeat

BACKLOG EXECUTOR
  → consume the current actionable backlog autonomously until useful work is exhausted
```

The library intentionally avoids prompt proliferation.

## 1. Deep Run

[`loops/deep-run.md`](loops/deep-run.md)

Deep Run is the reasoning workflow. It has two modes.

### Deep Run — BACKLOG

Use when the main question is:

> What should materially improve in this project, and what should the actual GitHub backlog contain so an autonomous executor can do it well?

Core pattern:

`inspect → baseline → independent perspectives → bottleneck → alternatives → red team → experiment gate → audit backlog → map findings to work → prioritize → write executable issues → adversarial review`

Best for:
- filling or refreshing a GitHub backlog;
- converting research/product audits into durable issues;
- cleaning duplicates, stale work and already-completed tasks;
- defining dependencies, acceptance criteria and verification;
- preparing a repository for long autonomous execution.

The backlog is a control plane, not an idea dump.

### Deep Run — EXECUTE

Use when the main question is:

> What should materially improve in this product/project, and can the agent implement and verify the best improvement now?

Core pattern:

`inspect → baseline → independent perspectives → bottleneck → alternatives → red team → experiment gate → execute → verify → independent evaluation → entropy check → learn → repeat`

Best for:
- product/website/repository improvement;
- difficult strategy or architecture work;
- discovery/growth/value audits;
- research that should turn directly into verified changes;
- periodic deep reconsideration of a mature project.

Default to EXECUTE for ordinary requests such as "run a deep loop" or "improve this project". Use BACKLOG when the user explicitly wants issues/backlog rather than immediate product changes.

## 2. Backlog Executor

[`loops/backlog-executor.md`](loops/backlog-executor.md)

Use when the backlog already exists and the goal is:

> Keep implementing the highest-value actionable work autonomously until no justified executable backlog remains.

Core pattern:

`sync → triage → select → implement → tests → product/UI verification → independent review → update issues → regression checkpoint → continue`

Best for:
- Codex, Work, Kimi or another coding/product agent with repository access;
- long autonomous implementation sessions;
- working through many GitHub issues without stopping after one task;
- user-facing work where UI must be inspected after implementation;
- sessions that should continue past blocked issues and periodically check regressions.

Do not use it blindly against a poor backlog. Run Deep Run in BACKLOG mode first when backlog quality is uncertain.

## Which workflow should I use?

| Situation | Workflow |
|---|---|
| "Think deeply and improve this project now" | **Deep Run — EXECUTE** |
| "Audit/fill/review/prioritize our GitHub backlog" | **Deep Run — BACKLOG** |
| "Take the backlog and keep building until actionable work is exhausted" | **Backlog Executor** |
| Backlog is messy, then needs long autonomous implementation | **Deep Run BACKLOG → Backlog Executor** |
| Direction is uncertain but ChatGPT can safely implement | **Deep Run EXECUTE** |
| Direction is uncertain and work should be handed to Codex/Kimi later | **Deep Run BACKLOG → Backlog Executor** |

Do not mechanically chain both workflows. Start where the real uncertainty exists.

## Model guidance

See [`MODEL_PROFILES.md`](MODEL_PROFILES.md). Model selection and reasoning effort are configuration, not reasons to duplicate prompt files.

Current high-level guidance:

| Workflow | Strong default |
|---|---|
| Deep Run — EXECUTE | **GPT-6 Astra Medium/High** for hardest end-to-end work; **GPT-5.6 Sol High** as strong workhorse |
| Deep Run — BACKLOG | **GPT-5.6 Sol High** or **GPT-6 Astra Medium** when broad product/research context must be synthesized |
| Backlog Executor | **Codex/Work with GPT-6 Astra** for hardest long autonomous runs; **GPT-5.6 Sol High** for normal repository execution |
| External coding agents | Use the same Backlog Executor; benchmark the exact model/version/settings before adding recommendations |

## Minimal invocation examples

```text
Use Prompts/Deep Run on <project> in EXECUTE mode.
Outcome: <real outcome>.
Authority: <what may be changed>.
Run through implementation and verification.
```

```text
Use Prompts/Deep Run on <project> in BACKLOG mode.
Outcome: <real project outcome>.
Deeply inspect the project and update the actual GitHub backlog directly.
Do not implement product changes.
```

```text
Use Prompts/Backlog Executor on <project>.
Goal: <project outcome>.
Work from the current GitHub backlog and continue autonomously until no justified actionable work remains.
Do not deploy unless explicitly authorized.
```

## Repository contract

The target size is **two canonical prompts**.

Do not add a new file because a new domain, role, feature type or model appears. Improve Deep Run or Backlog Executor when a reusable failure mode is discovered. Add a third workflow only if repeated benchmark evidence shows that the job cannot be expressed cleanly as one of the two Deep Run modes or Backlog Executor.

Files:
- `loops/deep-run.md` — deep reasoning with BACKLOG and EXECUTE modes;
- `loops/backlog-executor.md` — long autonomous backlog implementation loop;
- `MODEL_PROFILES.md` — model/effort guidance and adapters;
- `BENCHMARKS.md` — evaluation protocols;
- `RESEARCH.md` — research basis;
- `catalog.yaml` — machine-readable metadata;
- `AGENTS.md` — routing and execution rules.

Default principle: **one deep reasoning loop with two outputs, plus one relentless verified executor for sustained backlog work.**