# Model and environment profiles

Official guidance checked: **2026-09-12**. Local model rankings: **unbenchmarked**.

Choose the execution environment before the model. A capable model with repository tools but no shell/runtime cannot provide the same evidence as a coding checkout. Prompt text cannot change the active model, reasoning setting, sandbox, subscription or tools.

## Capability-first routing

| Available environment | Useful work | Evidence boundary |
|---|---|---|
| ChatGPT with repository read tools | Inspect, search, diagnose, maintain permitted issue context | Do not claim committed code or runtime verification |
| ChatGPT with repository write tools | Inspect, edit permitted GitHub state, stage/publish coherent commits, inspect CI when exposed | A remote write is not a local draft; no shell/browser claims unless those tools actually ran |
| ChatGPT with local execution/browser tools | Direct implementation plus relevant runtime/UI verification | Check network, dependencies, write scope and runtime availability |
| Codex with checkout, shell and tests | Sustained implementation and executable verification | Check actual issue/browser/network access rather than assuming it |
| Agents API with managed Codex harness | Durable programmatic agent sessions, hosted or connected sandboxes, tools/MCP integration, streamed progress and recovery | **Public beta and unbenchmarked here**; inspect sandbox/network/tool permissions and required actions before treating it as equivalent to a local Codex checkout |
| Read-only session | Diagnosis, grounded proposals and unapplied patches | No claim of committed changes or updated issues |

The same Deep Run command can route across these environments, but its runtime adapter is conditional. When it is actually running in ChatGPT, use [CHATGPT_DEEP_RUN.md](CHATGPT_DEEP_RUN.md). Do not impose that adapter on Codex merely because GitHub is involved.

OpenAI currently documents ChatGPT GitHub retrieval as on-demand rather than a guaranteed synchronized repository index, and says capabilities can vary by product surface. Therefore discover unknown paths with search, then use exact current reads and inspect the active tool permissions before assuming writes. A GitHub connection label is not proof of write access.

## Current Work / Codex environment facts

OpenAI's Work/Codex guidance was updated on **2026-09-10** and materially changes environment selection details relevant to long autonomous runs:

- GPT-6 Pro, powered by GPT-6 Astra, is available in ChatGPT for Pro $100, Pro $200, Business and Enterprise; Plus includes GPT-6 Astra in Work and Codex as rollout permits.
- Astra in Codex requires **Codex CLI 0.153.0 or newer**. The latest ChatGPT Desktop app is also required for current Astra availability in desktop Work/Codex surfaces.
- Work is designed for longer multi-step work and finished deliverables; Codex remains the software-development surface for repository, terminal, test and debugging work.
- Work can run in the cloud on web/mobile and in supported desktop configurations. Codex remains a separate desktop experience; supported remote Codex chats can be accessed from mobile, but Codex is not itself selectable on web/mobile.
- Workspace administrators can set the starting model, reasoning level, speed and Fast Mode availability for Work & Codex independently from ordinary Chat defaults.

Treat these as environment capabilities, **not** as evidence that Astra is the best configuration for Deep Run or Backlog Executor. Exact model × reasoning × environment choices remain unbenchmarked until compared on authorized real tasks.

## Agents API candidate environment

OpenAI released the **Agents API in public beta on 2026-09-10**. It is materially relevant to long autonomous execution because it provides a managed Codex harness with:

- durable sessions that can continue across turns;
- managed session orchestration, context compaction and recovery;
- streamed progress/events;
- OpenAI-hosted sandboxes or a connected external/supported sandbox;
- custom tools and MCP integration;
- reusable agent/session configuration through the API.

For this library, treat the Agents API as an **unbenchmarked candidate execution environment**, not a new workflow and not a preferred default. The strongest fit to test first is sustained `backlog-executor` work or API-driven Deep Run EXECUTE where durable state and recovery matter.

Before adopting it as a default, compare it against the current Codex/Work path on equivalent authorized repository tasks. Record at minimum: verified work completed, recovery after interruption/compaction, issue-state accuracy, regressions, UI/runtime verification coverage, human intervention required, and total resource/latency cost when observable.

Do not assume a managed session has the same filesystem, network, browser, GitHub write, secret or approval capabilities as another Codex surface. Inspect the actual session environment and required actions.

For API/custom-harness use, OpenAI currently documents GPT-6 Astra reasoning efforts `low`, `medium`, `high`, `xhigh`, and `max`. The Responses API also supports long-running controls such as async tool calling, mid-turn steering and changing reasoning effort during a conversation. These are candidate execution controls, not defaults for this library; benchmark them before adopting a workflow-specific recommendation.

## Reasoning effort

Retain **Sol High/Extra High** or other user-requested higher reasoning configurations when they are actually available and appropriate. The template does not claim a measured winner.

Higher reasoning effort should be spent where uncertainty or consequence justifies it: establishing the dominant constraint, comparing materially different options, finding a strong counterargument, defining a reversal condition, and reviewing the candidate change. Once the decision threshold is met, execute. More reasoning effort is not a reason to re-read unchanged files, manufacture roles, generate fixed idea quotas or reopen settled architecture without contradictory evidence.

Escalate effort for observed reasoning failures or unusually ambiguous/high-consequence work. Verify exact model/configuration controls in the actual surface before depending on them.

## Long work and delegation

Use real subagents only for bounded tasks with clear ownership and integration. Do not let multiple writers compete over the same files. A self-review is not an independent evaluation.

Conversation compaction, persistence and scheduling depend on the runtime. Deep Run's checkpoint supports evidence-based resumption; it neither schedules work nor guarantees automatic restart. In ChatGPT, prefer durable checkpoints that cost no extra branch/PR overhead: one existing issue comment, an existing state artifact, or commit trailers attached to an already-needed coherent commit.

Managed Agents sessions change the runtime trade-off because the API can preserve session state and recover/compact managed context. That may reduce the value of manual checkpoint scaffolding for API-driven runs, but do not remove workflow checkpoints until real project runs show equivalent or better recovery and traceability.

## Refresh rule

When official guidance or an actual failure changes the decision: verify the current primary source, propose the smallest prompt/configuration change, compare before/after on authorized real tasks, and retain it only with useful evidence. Keep target-project evaluation evidence in that project, not this prompt library; see [RESEARCH.md](RESEARCH.md).

Sources:
- [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903)
- [Current model guidance](https://developers.openai.com/api/docs/guides/latest-model)
- [GPT-6 Astra model](https://developers.openai.com/api/docs/models/gpt-6-astra)
- [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275/)
- [OpenAI release notes](https://openai.com/products/release-notes/)
- [Agents API reference](https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions)
- [Codex best practices](https://developers.openai.com/codex/learn/best-practices)
- [Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)
