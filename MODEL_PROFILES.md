# Model and environment profiles

Official guidance checked: **2026-09-09**. Local model rankings: **unbenchmarked**.

Choose the execution environment before the model. A capable model with no repository/runtime access cannot provide the same evidence as a coding environment. Prompt text cannot change the active model, reasoning setting, sandbox, subscription, or available tools.

## Capability-first routing

| Available environment | Useful work | Evidence boundary |
|---|---|---|
| ChatGPT with repository read/write connectors | Inspect, maintain issues, edit permitted files, review diffs | Do not claim local tests/browser checks unless tools actually ran them |
| ChatGPT with local execution/browser tools | Direct implementation and relevant runtime/UI verification | Check network, dependencies, write scope and runtime availability |
| Codex with checkout, shell and tests | Sustained implementation; executable verification | Check actual issue/browser/network access rather than assuming it |
| Read-only session | Diagnosis, grounded proposals and unapplied patches | No claim of committed changes or updated issues |

Use all three commands in any environment that can satisfy their requirements. Backlog Executor is not a promise that ChatGPT launches Codex. If the runtime cannot do the next step, use available safe alternatives or produce a precise handoff.

## Starting configurations, not measured winners

The current OpenAI model guide describes GPT-6 Astra for difficult multi-step work. Its guidance calls out follow-through, instruction sensitivity, delegation and risk-proportionate testing. Those behavior controls are already in the canonical templates; no extra repeated adapter is needed.

Retain **Astra Medium/High** and **Sol High**, where actually offered, as user-preferred configurations to compare. Honor a requested available configuration; otherwise use the active capable model and report any material limitation. Escalate effort for observed reasoning failures or unusually ambiguous/high-consequence work, not merely to make a run longer. Verify exact model IDs and effort controls in the actual surface before configuring them.

No claim is made that one setting wins for BACKLOG, EXECUTE or Executor. Codex/Work is an environment, not a single immutable model. External agents use the same templates; record their exact model/version and tools before comparing outcomes.

## Long work and delegation

Use real subagents only for bounded tasks with clear ownership and integration: for example, inspect a separate subsystem or test an acceptance case. Do not let multiple writers compete over the same files. A self-review is not an independent evaluation.

Compaction, persistence and scheduling depend on the runtime. The template's checkpoint supports resumption; it neither schedules work nor guarantees background execution. Do not promise unavailable automation or fabricate cost/token measurements.

## Refresh rule

When official guidance or an actual failure changes the decision: verify the current primary source, propose the smallest prompt/configuration change, compare before/after on authorized real tasks, and retain it only with useful evidence. Keep target-project evaluation evidence in that project, not this prompt library; see [RESEARCH.md](RESEARCH.md). Do not copy a vendor's entire agent system prompt into a task prompt.

Sources:
- [Current model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [Codex best practices](https://developers.openai.com/codex/learn/best-practices)
- [Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)
