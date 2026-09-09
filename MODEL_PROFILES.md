# Model and environment profiles

Official guidance checked: **2026-09-09**. Local model rankings: **unbenchmarked**.

Choose the execution environment before the model. A capable model with repository tools but no shell/runtime cannot provide the same evidence as a coding checkout. Prompt text cannot change the active model, reasoning setting, sandbox, subscription or tools.

## Capability-first routing

| Available environment | Useful work | Evidence boundary |
|---|---|---|
| ChatGPT with repository read tools | Inspect, search, diagnose, maintain permitted issue context | Do not claim committed code or runtime verification |
| ChatGPT with repository write tools | Inspect, edit permitted GitHub state, stage/publish coherent commits, inspect CI when exposed | A remote write is not a local draft; no shell/browser claims unless those tools actually ran |
| ChatGPT with local execution/browser tools | Direct implementation plus relevant runtime/UI verification | Check network, dependencies, write scope and runtime availability |
| Codex with checkout, shell and tests | Sustained implementation and executable verification | Check actual issue/browser/network access rather than assuming it |
| Read-only session | Diagnosis, grounded proposals and unapplied patches | No claim of committed changes or updated issues |

The same Deep Run command can route across these environments, but its runtime adapter is conditional. When it is actually running in ChatGPT, use [CHATGPT_DEEP_RUN.md](CHATGPT_DEEP_RUN.md). Do not impose that adapter on Codex merely because GitHub is involved.

OpenAI currently documents ChatGPT GitHub retrieval as on-demand rather than a guaranteed synchronized repository index, and says capabilities can vary by product surface. Therefore discover unknown paths with search, then use exact current reads and inspect the active tool permissions before assuming writes. A GitHub connection label is not proof of write access.

## Reasoning effort

Retain **Sol High/Extra High** or other user-requested higher reasoning configurations when they are actually available and appropriate. The template does not claim a measured winner.

Higher reasoning effort should be spent where uncertainty or consequence justifies it: establishing the dominant constraint, comparing materially different options, finding a strong counterargument, defining a reversal condition, and reviewing the candidate change. Once the decision threshold is met, execute. More reasoning effort is not a reason to re-read unchanged files, manufacture roles, generate fixed idea quotas or reopen settled architecture without contradictory evidence.

Escalate effort for observed reasoning failures or unusually ambiguous/high-consequence work. Verify exact model/configuration controls in the actual surface before depending on them.

## Long work and delegation

Use real subagents only for bounded tasks with clear ownership and integration. Do not let multiple writers compete over the same files. A self-review is not an independent evaluation.

Conversation compaction, persistence and scheduling depend on the runtime. Deep Run's checkpoint supports evidence-based resumption; it neither schedules work nor guarantees automatic restart. In ChatGPT, prefer durable checkpoints that cost no extra branch/PR overhead: one existing issue comment, an existing state artifact, or commit trailers attached to an already-needed coherent commit.

## Refresh rule

When official guidance or an actual failure changes the decision: verify the current primary source, propose the smallest prompt/configuration change, compare before/after on authorized real tasks, and retain it only with useful evidence. Keep target-project evaluation evidence in that project, not this prompt library; see [RESEARCH.md](RESEARCH.md).

Sources:
- [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903)
- [Current model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [Codex best practices](https://developers.openai.com/codex/learn/best-practices)
- [Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)
