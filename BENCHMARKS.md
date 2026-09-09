# Workflow Benchmarks

This repository evaluates three canonical workflows against the job each one is supposed to do.

The goal is not to reward sophisticated-sounding reasoning. The benchmark asks whether the workflow improves a real project/control plane and whether autonomous execution actually completes verified work.

These are internal repository eval protocols, not external scientific benchmarks.

# 1. DRS-100 — Deep Run Score

Score each dimension 0–5 and apply the weight.

| Dimension | Weight | 5/5 means |
|---|---:|---|
| Outcome improvement | 25 | The run materially improves the stated outcome or prevents a bad change with decisive evidence. |
| Evidence & verification | 20 | Claims are grounded and the changed state is meaningfully verified. |
| Bottleneck & decision quality | 15 | The dominant constraint, alternatives, uncertainty and trade-offs are handled well. |
| Execution completeness | 15 | Authorized work reaches a coherent changed state rather than stopping at a plan. |
| Independent re-evaluation | 10 | The result is judged from scratch and weak work is not defended. |
| Learning & iteration | 5 | New evidence changes later decisions and durable learning is preserved. |
| Regression & entropy control | 5 | Regressions, duplication and avoidable complexity are checked. |
| Reasoning efficiency | 5 | Heavy reasoning is spent on decision-changing work. |

`DRS-100 = Σ (score / 5 × weight)`

# 2. BQS-100 — Backlog Quality Score

Use for `backlog-builder.md`.

| Dimension | Weight | 5/5 means |
|---|---:|---|
| Outcome alignment | 20 | Top backlog work clearly contributes to the project goal rather than activity volume. |
| Priority quality | 20 | High-leverage, dependency-unblocking work ranks above easy low-value work. |
| Executability | 20 | READY issues contain enough context, scope, acceptance criteria and verification for an autonomous executor. |
| Evidence & traceability | 15 | Important tasks are supported by observable project evidence; hypotheses/unknowns are explicit. |
| Backlog hygiene | 10 | Duplicates, stale, obsolete and already-done issues are correctly merged/closed/reclassified. |
| Dependency & queue design | 10 | Dependencies, blockers and a clear actionable queue are represented accurately. |
| Inflation control | 5 | The builder resists speculative issue generation and keeps the backlog compact enough to guide execution. |

`BQS-100 = Σ (score / 5 × weight)`

Useful secondary measures:
- percentage of READY issues an executor can start without reconstructing missing context;
- duplicate/stale issue rate before vs after;
- number of high-priority issues later invalidated as unnecessary;
- number of important discovered gaps that had no issue;
- executor clarification/rework rate caused by issue quality.

# 3. BES-100 — Backlog Execution Score

Use for `backlog-executor.md`.

| Dimension | Weight | 5/5 means |
|---|---:|---|
| Verified completion | 25 | High-value READY work is actually completed with observable verification. |
| Acceptance correctness | 20 | Implementations satisfy intended outcomes and acceptance criteria, not merely issue wording. |
| Regression control | 15 | Targeted and periodic broader checks catch/fix regressions caused by execution. |
| Control-plane integrity | 10 | GitHub issue state accurately reflects repository/product reality. |
| Autonomous continuation | 10 | The agent continues across multiple independent issues and does not stop at the first blocker/batch. |
| Product/UI verification | 10 | User-facing changes are inspected in the resulting experience when tooling permits. |
| Scope & architecture discipline | 5 | Work avoids speculative features, unrelated refactors and unnecessary abstraction. |
| Blocker handling | 5 | Blocked/human-decision work is recorded accurately while independent READY work continues. |

`BES-100 = Σ (score / 5 × weight)`

Useful secondary measures:
- verified issues completed / READY issues attempted;
- issues incorrectly marked complete;
- regressions per completed issue/batch;
- blocked issue handling accuracy;
- autonomous issues completed before human intervention;
- user-facing changes with actual UI verification;
- unnecessary files/dependencies/abstractions introduced;
- re-open rate after executor completion.

# Status levels

For each workflow separately:

- **experimental** — structure exists but has not passed representative real runs.
- **candidate** — score ≥75 in at least two materially different real tasks with no critical failure.
- **stable** — score ≥85 across at least three materially different tasks/domains, with repeatable performance and no recurring critical failure.

A correct `NO CHANGE`, issue closure, rejection or BLOCKED classification can score highly when evidence supports it.

# Critical failures

## Deep Run

Cannot be stable if it materially tends to:
- stop at audit/plan when safe execution was authorized;
- fabricate evidence or silently turn hypotheses into facts;
- optimize files/features/commits rather than outcome;
- declare improvement without verifying changed state;
- loop without meaningful state/evidence change.

## Backlog Builder

Cannot be stable if it materially tends to:
- create issue volume as a proxy for project progress;
- duplicate existing work;
- preserve obviously stale/obsolete work;
- assign priority without evidence or dependencies;
- produce READY issues whose outcome/acceptance/verification is too vague for autonomous execution;
- convert every idea or unknown into an implementation task.

## Backlog Executor

Cannot be stable if it materially tends to:
- stop after one issue/batch while independent READY work remains;
- mark issues done without satisfying acceptance criteria;
- treat a green build as sufficient verification for user-facing changes when UI inspection is available;
- ignore failing tests/regressions caused by its changes;
- blindly implement stale/obsolete issue text;
- stop the entire run because one issue is blocked;
- create large unrelated refactors/features while executing scoped backlog;
- leave GitHub issue state inconsistent with actual work.

# Canonical evaluation protocol

For any workflow/model comparison:

1. Freeze a meaningful baseline repository/product/backlog state.
2. Define the workflow goal, constraints, authority and observable success evidence before the run.
3. Use the same workflow version and equivalent tool/permission context for compared configurations.
4. Change only the model/reasoning/environment unless the experiment explicitly tests an adapter or tool difference.
5. Run important configurations at least **3 times** when practical.
6. Score using DRS-100, BQS-100 or BES-100 as appropriate.
7. Record project-native outcomes and critical failures in addition to the score.
8. Prefer a configuration only when the advantage is repeatable and materially useful.

# End-to-end lifecycle benchmark

Periodically benchmark the full system, not only isolated prompts:

```text
Deep Run → Backlog Builder → Backlog Executor
```

Start from a real project state with imperfect direction/backlog.
Measure:

- whether Deep Run discovers a genuinely high-value direction;
- whether Backlog Builder converts that evidence into a clean executable queue;
- whether Backlog Executor completes the queue correctly and continues autonomously;
- how much rework/clarification is needed between stages;
- whether the final product state is materially better than the initial state;
- whether issue count/complexity grew without proportional value.

The ideal lifecycle has **low handoff loss**: evidence and intent survive the transition from discovery → backlog → execution.

# Model × environment benchmark

For autonomous work, benchmark:

`workflow × model × reasoning effort × execution environment`

Environment matters because repository access, shell/runtime, tests, browser/UI inspection, GitHub issue tools, branch isolation and persistence can materially affect outcomes.

Current OpenAI configurations worth testing when available:

- Deep Run — GPT-6 Astra Medium / High;
- Deep Run — GPT-5.6 Sol High / Extra High;
- Backlog Builder — GPT-5.6 Sol High vs GPT-6 Astra Medium;
- Backlog Executor — Codex/Work + GPT-6 Astra Medium/High;
- Backlog Executor — Codex/Work + GPT-5.6 Sol High/Extra High.

External agents/models should use the same baseline tasks and workflow text before any vendor-specific adapter is introduced.

# Representative real-project suite

Maintain at least:

1. **Product/growth** — e.g. discovery → first value → continuation in an existing product.
2. **Website/service** — real user-facing site with search, UX and UI verification.
3. **Software/repository** — non-trivial technical backlog with dependencies/tests.

Prefer projects with real history, constraints, existing issues and measurable artifacts.

# Benchmark record

```yaml
workflow_id: <deep-run|backlog-builder|backlog-executor>
workflow_version: <version>
profile_version: <version>
date: <yyyy-mm-dd>
project: <project>
baseline_ref: <commit/snapshot/date>
goal: <desired outcome>
model: <exact model label/id>
reasoning_effort: <setting>
environment: <chatgpt|work|codex|api|external-agent|other>
run_number: <n>
score_type: <DRS-100|BQS-100|BES-100>
score: <0-100>
observable_outcome: <before/after result>
completion: <complete|partial|blocked|failed>
regressions: []
incorrect_state_changes: []
resource_usage: <if available>
critical_failures: []
notes: <short evidence-based notes>
```

# Promotion rule

A workflow version, model profile or adapter becomes preferred only when its advantage is visible in comparable real outcomes across repeated runs.

The benchmark itself should evolve when actual failures expose blind spots.
