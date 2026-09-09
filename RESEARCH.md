# Research and design decisions

Sources checked **2026-09-09**. These sources support mechanisms, not a claim that this library is the strongest prompt system or guarantees product success. Current official pages can change; recheck before a model/configuration refresh.

| Primary source | Relevant guidance | Library decision |
|---|---|---|
| [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model) | Explicit follow-through, instruction hygiene, purposeful delegation and proportionate verification | Infer routine details, act within authority, condition review depth on risk |
| [Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) | End-to-end work, preservation of existing edits, meaningful implementation and avoiding unproductive repetition | Inspect live state, protect concurrent work, verify and checkpoint rather than simulate endless progress |
| [Codex best practices](https://developers.openai.com/codex/learn/best-practices) | Clear goals/context/constraints/completion, practical repository guidance and testing | Six filled inputs, short task-specific context, executable checks |
| [AGENTS.md guidance](https://developers.openai.com/codex/guides/agents-md) | Repository-scoped instructions and explicit discovery of applicable guidance | Use this library as a router; inspect the target's applicable instructions rather than copying the whole library |
| [Harness engineering](https://openai.com/index/harness-engineering/) | Inspectable repository knowledge, feedback loops and manageable instruction structure | Two templates, progressive reading, durable evidence instead of accumulating process documents |
| [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Task-specific evaluation, representative cases, explicit criteria and evaluation of changes | Frozen baselines, critical failures, held-out cases and separation of structural checks from model performance |

## Why v2 changes the previous design

At baseline `cfd120d893ed7a049402b3a36bc4464d6df24878`, the library already had strong outcome-first reasoning, backlog deduplication and continued execution. The main weaknesses found by repository review were:

- A long staged Deep Run risked making every task pay for councils, tournaments and repeated analysis. v2 keeps those mechanisms conditional instead of prescribing a fixed number of alternatives or roles.
- Agent-filled inputs had no mechanical completeness check. The optional renderer validates fields and removes the unused mode; it does not replace real context discovery.
- Generic issue closure did not clearly distinguish a branch result from the required integration/release boundary. v2 requires that distinction.
- Capability gaps, concurrent edits, repeated no-progress attempts and interrupted sessions needed concrete handling. v2 adds targeted rules without requiring a particular agent product.
- Templates were marked candidate although the published candidate standard requires recorded real-run scores. v2 remains experimental pending that evidence.

## Deliberately not added

No mandatory multi-agent council, hidden-reasoning transcript, domain prompt clones, invented "best model" ranking, background scheduler, paid benchmark runner or self-awarded quality score. No claim that shorter text alone is better.

The design hypothesis is that a shorter, capability-aware contract preserves decision quality while reducing mode confusion and unsupported completion claims. It must be tested on actual task traces, not inferred from the number of safety phrases or passing renderer tests. Keep failed-run evidence with the target project and revise only what the evidence implicates.

## GitHub execution update: templates v2.1

Baseline: `b3841804e49f46ee291e3cb62669c0cb1381c85a`. The owner requested lower branch/merge overhead and more recoverable ChatGPT-to-GitHub work. Main-first is this library's operating preference for authorized low-risk implementation, not a universal GitHub recommendation or permission to bypass repository policy.

The update replaces end-of-session-only recovery with early per-batch checkpoints, prefers atomic publication, reconciles ambiguous writes before retries, and reduces CI waste without leaving workflows disabled. Essential rules are embedded in both templates; optional recipes live in [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md). No new command, site fixture, benchmark workflow or background service is introduced. Existing template word budgets remain unchanged.

| Primary source checked 2026-09-09 | Mechanism | Design consequence |
|---|---|---|
| [Git trees](https://docs.github.com/en/rest/git/trees) and [references](https://docs.github.com/en/rest/git/refs) | Multiple file entries can share a tree/commit; a non-forced ref update requires a fast-forward | Preserve the current base tree, publish coherent batches atomically, reconcile moved HEAD instead of forcing |
| [REST API best practices](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api) | Avoid excessive polling/concurrent calls, handle rate limits, reuse conditional reads | Targeted SHA-based reads, serialized writes, bounded retries and explicit mutation read-back |
| [Workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency) | A concurrency group can cancel superseded running validation | Scope cancellation to the same validation workflow/ref; do not copy it blindly to deployment |
| [Skip workflow runs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs) and [job conditions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-jobs-with-conditions) | Skipped workflows may leave required checks pending; job-level skip has different status semantics | No blanket skip tokens; preserve an always-reporting required gate and distinguish skipped from actual verification |

Checkpoint cadence and main-first are design choices, not measured performance results. A saved note cannot restart ChatGPT, guarantee recovery of an unsaved edit or prove a test passed. Validate the behavior on actual authorized tasks; structural checks alone cannot establish reliability gains.
