# Prompts

A deliberately small library for **deep autonomous AI runs** on real products, services, websites, repositories and systems.

The repository has one canonical prompt:

## [Deep Run](loops/deep-run.md)

`inspect → baseline → independent perspectives → bottleneck → alternatives → red team → experiment gate → execute → verify → independent evaluation → entropy check → learn → repeat`

Deep Run intentionally absorbs the useful parts of self-interview/council, Best-of-N, adversarial review, experimentation, evaluator-optimizer and repository gardening. Those are phases of one strong loop, not separate prompt variants.

## When to use it

Use Deep Run when the task deserves substantial reasoning and a complete pass rather than a quick answer:

- improve a product or service;
- find the next high-leverage milestone;
- improve discovery, acquisition, activation or retention;
- deeply audit and improve a website;
- solve a difficult repository/software problem;
- reconsider architecture or product direction;
- research a problem and turn findings into verified changes;
- review a mature project for simplification, regressions and new opportunities.

Do **not** force Deep Run onto a small deterministic edit or simple factual question.

## Where to use it

- **ChatGPT Work / Codex** — preferred for long repository-level execution with files, code, tools and tests.
- **ChatGPT with GitHub/web tools** — strong for product/repository audits, research, GitHub changes and scoped implementation.
- **API/custom harness** — use the same canonical prompt; configure the model/effort separately rather than cloning the prompt.

See [MODEL_PROFILES.md](MODEL_PROFILES.md) for current model and reasoning recommendations.

## Current model guidance

| Configuration | Recommended use |
|---|---|
| **GPT-6 Astra — Medium** | Preferred starting point for hardest end-to-end Deep Runs |
| **GPT-6 Astra — High** | Very difficult/ambiguous/consequential multi-domain run |
| **GPT-5.6 Sol — High** | Default full Deep Run workhorse |
| **GPT-5.6 Sol — Extra High** | Especially difficult one-off run when available |
| **GPT-5.6 Luna — Think** | Bounded sub-work/pre-scan; not preferred as sole final judge when stronger models exist |

As of 2026-09-09, official OpenAI sources checked for this repository do not list a model called `Solana`; see `MODEL_PROFILES.md` for handling that name.

## How to invoke

Minimal invocation:

```text
Use the canonical Deep Run from dkharlanau/prompts.
Project: <project/repository>.
Outcome: <real outcome>.
Constraints: <important constraints>.
Authority: <what may be changed>.
Run it to completion and verify the resulting state.
```

If the agent already has project context, do not duplicate it. The prompt explicitly tells the agent to inspect the real sources of truth.

Example:

```text
Use Prompts/Deep Run on Ptichi.
Outcome: materially improve qualified organic discovery and first user value.
Authority: inspect and modify the current development branch, create/update issues, run checks; do not deploy.
```

## Repository contract

This repository is intentionally resistant to prompt proliferation.

Do not add a new prompt because the domain changed. Improve `deep-run.md` when a generally useful failure pattern is discovered. Add a model-specific adapter only when benchmark evidence shows that the same canonical prompt needs different execution guidance for that model.

Files:

- `loops/deep-run.md` — canonical reusable prompt.
- `MODEL_PROFILES.md` — model selection, reasoning effort, adapters and model-refresh policy.
- `BENCHMARKS.md` — Deep Run quality and model×effort evaluation protocol.
- `RESEARCH.md` — research/evidence basis.
- `catalog.yaml` — machine-readable metadata.
- `AGENTS.md` — instructions for agents using this repository.

## Template variables

- `{{PROJECT}}`
- `{{OUTCOME}}`
- `{{TARGET}}`
- `{{CONTEXT}}`
- `{{CONSTRAINTS}}`
- `{{AUTHORITY}}`
- `{{SUCCESS_EVIDENCE}}`
- `{{STOP_CONDITION}}`

The default principle is: **one strong loop, real evidence, real execution, independent re-evaluation, repeat only while marginal value remains high.**
