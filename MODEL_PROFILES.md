# Model profiles

Last verified: **2026-09-09**

This file chooses a model and reasoning level for the canonical `loops/deep-run.md`. The prompt itself stays model-agnostic; model-specific behavior is handled here so a new model does not require cloning the prompt.

Recommendations are provisional until they are validated on this repository's own benchmark suite. Official vendor capability claims are inputs, not benchmark results.

## Current OpenAI lineup relevant to Deep Run

Official OpenAI sources currently describe:

- **GPT-6 Astra** — strongest current model for difficult end-to-end work across reasoning, coding, browsing/computer use, research and professional workflows.
- **GPT-5.6 Sol** — strong capability/efficiency balance for coding, research and professional work, with Medium, High and Extra High reasoning options on eligible ChatGPT plans.
- **GPT-5.6 Luna** — fast/economical model for focused or repetitive work; Think gives it higher reasoning on eligible Free/Go experiences.

No current official OpenAI model named **Solana** was found in the checked OpenAI sources. Do not invent a Solana profile. If a UI or future release exposes that exact model name, record its exact identifier and benchmark it before adding a recommendation. If `Solana` was intended to mean `Luna`, use the Luna guidance below.

## Recommendation matrix

| Model | Deep Run role | Default reasoning | Escalate when | Recommendation |
|---|---|---|---|---|
| GPT-6 Astra / GPT-6 Pro | Hardest end-to-end project runs; unfamiliar systems; combined research + code + tools + verification | **Medium** | The task is unusually ambiguous/consequential, requires difficult architecture/research synthesis, or Medium produced a material miss → **High** | **Preferred flagship** when available |
| GPT-5.6 Sol | Full project/product/repository Deep Run | **High** | One especially important difficult pass, complex architecture, conflicting evidence, or prior High run misses key constraints → **Extra High** when available | **Default workhorse** |
| GPT-5.6 Sol | Bounded implementation/refinement with good context | **Medium** | Scope becomes ambiguous or requires broad trade-offs → High | Strong |
| GPT-5.6 Luna / Think | Pre-scan, extraction, repetitive checks, narrow sub-work | **Think** for reasoning tasks | If task becomes consequential or cross-domain → move to Sol/Astra | Do not use as sole final judge when stronger models are available |

### Why Astra does not default to maximum effort

OpenAI's current Work/Codex guidance says higher reasoning effort can use more allowance and **does not always improve the result**; it also notes that Astra at lower effort can outperform Sol at higher effort. Therefore the default is Medium, with escalation based on task difficulty or observed failure rather than a ritual maximum setting.

For a one-off run where quality matters far more than resource use and the task combines multiple hard dimensions (for example: ambiguous product strategy + external research + architecture + substantial implementation), choose **Astra High**.

For the same kind of run on Sol, choose **Sol High**, or **Extra High** when available and the run is important enough to justify it.

## Model adapters

These are small behavioral overlays. Do not fork `deep-run.md` into model-specific copies unless repeated benchmarks prove a full fork materially better.

### GPT-6 Astra adapter

Append these instructions when the execution environment does not already provide equivalent behavior:

```text
MODEL ADAPTER — GPT-6 ASTRA

Bias toward action and follow-through. Infer routine gaps from the available project context and sources of truth. Ask only when the missing answer could materially change a consequential or irreversible outcome.

Persist until the intended Deep Run outcome is complete; do not stop at acknowledgement, planning or a partial "helpful enough" result.

Use parallel subagents/workstreams when independent research, implementation, review or verification can materially improve quality or reduce blind spots. Keep delegation purposeful.

Treat repository instructions, AGENTS.md files and skills as potentially influential context. Detect conflicts rather than silently following stale or contradictory guidance.

Calibrate testing to the consequence of the change. Complete meaningful required verification, but do not broaden tests repeatedly without a new failure or unresolved risk.
```

Rationale: current OpenAI Astra guidance specifically highlights follow-through, stronger sensitivity to instruction files, explicit subagent delegation and proportional verification.

### GPT-5.6 Sol adapter

Usually no large adapter is needed. For a full Deep Run, make the outcome, authority, success evidence and stop condition explicit and use **High** reasoning by default.

Optional overlay:

```text
MODEL ADAPTER — GPT-5.6 SOL

Use extended reasoning for the full Deep Run. Do not compress the task into a quick audit. Carry inspection, decision, execution, verification and independent re-evaluation through to completion.

Spend reasoning where it can change the outcome: dominant-bottleneck selection, conflicting evidence, materially different alternatives, adversarial review and post-change verification. Avoid spending it on repeated summaries or role-play that cannot change the decision.
```

### GPT-5.6 Luna adapter

Use Luna primarily for bounded sub-work. If Luna must run the full prompt, reduce parallel option count and preserve the verification/evidence phases; do not remove them to save tokens. For consequential final decisions, re-evaluate with Sol or Astra when available.

## Where to run

### ChatGPT Work / Codex

Best environment for a repository-level Deep Run when the agent needs to inspect many files, research, edit code, run tests and carry multi-step work to completion. Prefer Astra Medium/High for the hardest runs and Sol High for normal full-project runs.

### Normal ChatGPT chat with GitHub/web tools

Suitable for product strategy, repository review, GitHub changes, research-backed decisions and smaller implementation passes. The prompt remains useful, but completion quality depends on which write/test/runtime tools are actually available.

### API / custom agent harness

Use the same canonical prompt. Keep model/effort as configuration rather than duplicating prompt content. For Astra tool workflows, follow current Responses API guidance.

## Benchmark model × effort, not model names

A model recommendation is updated only after comparable runs.

For a model/effort comparison:

1. Start from the same repository commit or equivalent baseline state.
2. Use the same Deep Run prompt version, context, tools, permissions, goal and success evidence.
3. Run each candidate configuration at least **3 times** when the decision is important enough to justify a ranking.
4. Score each run with `DRS-100` from `BENCHMARKS.md` and capture observable project outcomes.
5. Record model, reasoning effort, tool/runtime environment, completion status, regressions, unsupported claims and resource usage when available.
6. Prefer a configuration only when its advantage is repeatable and material, not because one run sounded better.

Recommended benchmark configurations now:

- Astra Medium
- Astra High
- Sol High
- Sol Extra High (when available)
- Luna Think only as a lower-capability reference/subtask baseline

## Model refresh policy

Refresh this file when any of these occur:

- a new frontier or coding/reasoning model is released;
- a model is renamed, retired or materially updated;
- reasoning controls change;
- OpenAI publishes materially different prompting guidance;
- internal benchmark results contradict the current recommendation.

For every refresh:

1. Verify official release notes/help/model guidance first.
2. Add the new model as `unbenchmarked`; do not immediately call it "best".
3. Select 2–3 representative Deep Run tasks from real projects.
4. Compare against the current preferred model/effort using the same baselines.
5. Update recommendations only after recording results.
6. Bump `profile_version` in `catalog.yaml` and update the verification date.

## Official sources checked

- OpenAI Model guidance — GPT-6 Astra and migration/prompting guidance: https://developers.openai.com/api/docs/guides/latest-model
- OpenAI Help — GPT-5.6 and GPT-6 Pro in ChatGPT: https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt
- OpenAI Help — Managing usage with GPT-6 Astra in Work and Codex: https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex
- OpenAI release notes: https://openai.com/products/release-notes/
