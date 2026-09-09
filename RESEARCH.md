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

The design hypothesis is that a shorter, capability-aware contract preserves decision quality while reducing mode confusion and unsupported completion claims. It must be tested on actual task traces, not inferred from the number of safety phrases or passing renderer tests. Keep failed runs as evaluation cases and revise only what the evidence implicates.
