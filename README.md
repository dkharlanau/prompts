# Prompts

Three commands for real development through ChatGPT or Codex. Two maintained templates, no collection of near-duplicates.

| Command | Job | Durable result |
|---|---|---|
| **Deep Run BACKLOG** | Find what is worth doing | Clean, prioritized issues an executor can use without the original chat |
| **Deep Run EXECUTE** | Find the best justified improvement and make it | Changed artifacts with verification and an honest completion status |
| **Backlog Executor** | Work through an existing usable queue | Implemented, reviewed work; accurate issues; continued progress past unrelated blockers |

## Everyday use

```text
Prompts Deep Run BACKLOG на <project>. Цель — <outcome>.
```

```text
Prompts Deep Run EXECUTE на <project>. Работай глубоко.
```

```text
Prompts Backlog Executor на <project>. Разбирай весь actionable backlog.
```

The assistant reads this repository, resolves the actual project, fills context and constraints, then executes. You do not need to fill six fields yourself. Existing no-push, branch and deployment restrictions remain in force. Specifying a model or environment requests that configuration; text cannot switch the active model or start an unavailable agent.

Use EXECUTE when direction is uncertain and changes are wanted now. Use BACKLOG when the output should be issues, not product edits. Use Executor when useful work is already defined. Do not chain workflows automatically or use a deep loop for a one-line deterministic fix.

## Templates

[Deep Run](loops/deep-run.md) and [Backlog Executor](loops/backlog-executor.md) are self-contained once filled. The agent entry point is [AGENTS.md](AGENTS.md).

The templates retain deep diagnosis, alternative hypotheses, skeptical review, experiments and iteration, but activate these only when they can affect the decision. They require real capability checks, preserve concurrent work and distinguish a branch fix from merged code, deployment and measured impact. A simulated user is not customer research; a green build is not proof of a useful product.

For long work, the agent checkpoints repo/ref/SHA, constraints, issue state, verification and the next action. This supports a later resumed session; it is not background scheduling.

## Optional local renderer

Python 3.10+, standard library only. The agent supplies a UTF-8 JSON run specification with six non-empty string fields:

```json
{
  "PROJECT": "owner/repository (verified target)",
  "GOAL": "Fix the reproduced first-value failure",
  "CONTEXT": "Use the verified branch/ref and linked reproduction; inspect current state",
  "AUTHORITY": "Edit and verify in the existing work branch; no push, merge or deploy",
  "CONSTRAINTS": "Preserve existing work and public API behavior",
  "DONE_WHEN": "The reproduction passes, relevant regressions are checked, and remaining gaps are reported"
}
```

```sh
python3 scripts/prompts.py render deep-execute --spec /tmp/run.json
python3 scripts/prompts.py render deep-backlog --spec /tmp/run.json
python3 scripts/prompts.py render backlog-executor --spec /tmp/run.json
python3 scripts/prompts.py check
```

Use `--spec -` for standard input. Rendering writes only prompt text to standard output; it does not call a model, read your projects, write to GitHub or change permissions. The Deep Run renderer strips the unused mode. Unknown/missing fields and unresolved placeholders fail instead of silently producing an incomplete prompt. Do not commit private run specifications.

## Supporting files

[MODEL_PROFILES.md](MODEL_PROFILES.md) separates environment capabilities from model choices. [RESEARCH.md](RESEARCH.md) records source-to-design decisions. Keep the repository project-neutral: do not add target-project datasets, fixtures, benchmark cases or generated run prompts containing private project context.

Keep exactly three commands unless repeated real use shows a genuinely different job that cannot fit the existing workflows.
