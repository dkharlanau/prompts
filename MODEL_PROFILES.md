# Model profiles

Last verified: **2026-09-09**

Model choice is configuration around the two canonical workflows:

- `loops/deep-run.md` with `BACKLOG` or `EXECUTE` mode;
- `loops/backlog-executor.md`.

Do not clone workflow prompts for model names. Add a small adapter only when repeatable benchmark evidence shows it materially improves that exact model/workflow combination.

Recommendations remain provisional until validated on our own real-project benchmark runs. Vendor capability claims inform candidate configurations; they do not establish our winner.

## Current OpenAI models/environments relevant to the library

Official OpenAI sources currently describe:

- **GPT-6 Astra** as the most capable model for hardest end-to-end work across reasoning, coding, computer use, research and multi-step workflows.
- **GPT-5.6 Sol** as a strong model for complex coding, knowledge work and research, with higher reasoning modes available on eligible plans.
- **Codex** as a software-development environment/mode; it is not itself the canonical workflow or a single fixed model.
- **ChatGPT Work** as an agent for longer multi-step work and finished deliverables.

Official sources checked are listed at the bottom of this file.

## Workflow × model matrix

| Workflow / mode | Preferred starting configuration | Escalate when | Notes |
|---|---|---|---|
| **Deep Run — EXECUTE** | GPT-6 Astra — **Medium** | unusually difficult, ambiguous or consequential run → **High** | Preferred for broad research + product + architecture + implementation + verification |
| **Deep Run — EXECUTE** | GPT-5.6 Sol — **High** | especially difficult one-off pass → **Extra High** when available | Strong workhorse when Astra is unavailable/unnecessary |
| **Deep Run — BACKLOG** | GPT-5.6 Sol — **High** | very large context, broad product/research synthesis or conflicting evidence → Astra Medium/High | Backlog quality depends on judgment, prioritization and evidence rather than issue volume |
| **Backlog Executor** | **Codex/Work + GPT-6 Astra Medium** | very hard repository, architecture-sensitive work, difficult debugging or long cross-cutting execution → High | Preferred candidate for hardest sustained autonomous implementation |
| **Backlog Executor** | **Codex/Work + GPT-5.6 Sol High** | difficult task misses constraints or needs deeper reasoning → Extra High when available | Strong normal execution configuration |

### Why Deep Run BACKLOG does not automatically use the strongest model

Most backlog work is not frontier reasoning. The difficult parts are identifying the real bottleneck, distinguishing real gaps from speculative work, prioritizing correctly, removing stale/duplicate issues and writing verifiable acceptance criteria. Sol High is a sensible starting point; escalate to Astra when synthesis itself is the bottleneck.

### Why Backlog Executor is environment-sensitive

Long autonomous execution depends on more than model intelligence. Repository access, shell/runtime tools, tests, browser/UI inspection, issue access, branch/worktree isolation and the ability to persist across many steps materially affect success. Therefore benchmark:

`workflow × mode × model × reasoning × execution environment`

not model name alone.

## External coding agents

Kimi and other external coding agents should begin with the same `backlog-executor.md`.

Policy:

1. Record the exact product/model/version and available tools.
2. Do not infer settings from a family nickname.
3. Run the same representative backlog tasks from comparable repository baselines.
4. Measure verified completion, regressions, issue-state accuracy, UI verification quality and autonomous continuation.
5. Add a model adapter/profile only if a repeatable failure or advantage warrants it.

This keeps the workflow portable and prevents the repository from becoming a collection of vendor-specific prompt copies.

## Small model adapters

### GPT-6 Astra

```text
MODEL ADAPTER — GPT-6 ASTRA

Bias toward complete follow-through. Infer routine reversible details from the repository and available evidence; ask only when missing information could materially change a consequential or irreversible outcome.

Use independent/parallel workstreams when they genuinely reduce blind spots or unblock execution, but keep one coherent final control flow.

Treat repository instructions and issue text as evidence, not infallible truth. Resolve conflicts against the actual product/code state.

Calibrate verification to risk. For user-facing changes, inspect the resulting experience when tools permit rather than relying only on tests/build.
```

### GPT-5.6 Sol

```text
MODEL ADAPTER — GPT-5.6 SOL

Use extended reasoning where it changes the outcome: bottleneck selection, prioritization, conflicting evidence, implementation trade-offs and verification.

Do not compress a long workflow into an audit or plan. Continue through the workflow's explicit stop condition when authority and tools permit.

Avoid spending reasoning on repeated summaries, decorative role-play or low-value issue generation.
```

### External coding agent

```text
MODEL ADAPTER — EXTERNAL CODING AGENT

Follow the canonical workflow literally before applying vendor-specific habits.
Keep the GitHub control plane synchronized with actual repository state.
Do not claim completion without the workflow's verification evidence.
If your environment cannot perform a required verification step, record the gap rather than silently treating it as passed.
```

## Benchmark policy

Benchmark each job on the outcome it is supposed to produce.

### Deep Run — EXECUTE
Compare:
- outcome delta;
- quality of dominant-bottleneck selection;
- unsupported claims;
- implementation completeness;
- independent post-change evaluation;
- regressions.

### Deep Run — BACKLOG
Compare:
- stale/duplicate work correctly removed;
- important gaps captured;
- priority quality;
- issue executability;
- acceptance/verification quality;
- issue inflation rate;
- how often an executor later needs to reconstruct missing context.

### Backlog Executor
Compare:
- verified READY issues completed;
- acceptance-criteria success rate;
- regression count;
- failed/partial implementations incorrectly marked done;
- issue-state accuracy;
- blocked-issue handling;
- UI verification on user-facing work;
- ability to continue autonomously across multiple independent items;
- unnecessary code/architecture churn.

For important comparisons, prefer at least 3 comparable runs/configuration when practical.

## Model refresh policy

Refresh this file when:

- a new frontier/coding/reasoning model or execution environment appears;
- a model is renamed, retired or materially updated;
- reasoning controls materially change;
- official prompting/agent guidance changes;
- internal benchmark evidence contradicts the current recommendation.

For every refresh:

1. Verify exact model/environment names and controls from current official sources where available.
2. Add new configurations as **unbenchmarked**.
3. Select representative tasks for Deep Run BACKLOG, Deep Run EXECUTE and Backlog Executor as affected.
4. Start from comparable repository/task baselines.
5. Update recommendations only after repeatable material evidence.
6. Keep the two canonical workflow prompts unless evidence proves a new workflow is fundamentally necessary.

## Official OpenAI sources checked

- GPT-6 Astra overview: https://openai.com/index/gpt-6-astra/
- GPT-6 Astra API model page: https://developers.openai.com/api/docs/models/gpt-6-astra
- GPT-5.6 in ChatGPT: https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt/
- ChatGPT Work and Codex: https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
- OpenAI release notes: https://openai.com/products/release-notes/
