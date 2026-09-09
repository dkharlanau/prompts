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

## GitHub working defaults

**Main-first, not main-at-any-cost.** When implementation publication is authorized, prefer small verified batches on the actual default branch. Keep explicit branch/no-push/no-deploy restrictions and protection intact. Reuse a permitted work branch when necessary; do not create one per microtask.

**One coherent change, one publication.** Prefer atomic multi-file commits over one commit per file. Check for concurrent changes and read back writes. After a timeout, establish whether the operation already succeeded before retrying.

**Checkpoints before the session ends.** For multi-batch work, keep one compact checkpoint from early in the run, update it after coherent batches and before lengthy/risky steps. Prefer an editable comment in an existing relevant issue, checking issue-triggered automation; avoid heartbeat commits. Record confirmed SHA, done/pending work, checks and next action. Resume from live state, not a fresh full audit:

```text
Prompts Backlog Executor на <project>. Продолжи с последнего checkpoint.
```

**Lean CI, not disabled CI.** Batch commits and run relevant checks. Optimize validation concurrency and expensive-job selection only when authorized. Do not toggle workflows off until the chat ends, blanket-apply `[skip ci]`, remove useful tests or treat skipped checks as passed verification. A no-deploy restriction includes automatic previews.

Operational recipes and a checkpoint format are in [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md). These are prompt rules, not an installed scheduler or repository-wide configuration change. They support a later resumed session, not automatic recovery from a crashed chat. Essential rules stay inside both copyable templates.

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
