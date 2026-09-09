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

## Prepare the repository, not just the prompt

Start with [AGENTS.md](AGENTS.md) and [REPO_MAP.md](REPO_MAP.md) for this library. The map routes a task to its source files, coupled changes, real checks and resume location. Do not read every supporting guide on every run.

[REPOSITORY_SETUP.md](REPOSITORY_SETUP.md) explains how to prepare another repository for ChatGPT app + GitHub work: explicit entry-point loading, a small task map, canonical versus generated sources, executable checks, readable CI evidence and resumable state. Reuse existing conventions; no extra manifest or fourth command is required.

```text
Prompts Deep Run EXECUTE на <project>. Подготовь репозиторий для работы из ChatGPT через GitHub по REPOSITORY_SETUP.md. Сохрани ограничения на push и deploy.
```

This request applies to the named target only. Normal feature runs consume its map rather than reorganize the repository. A file named AGENTS.md does not itself configure the ChatGPT app or grant tools access.

The [prompt-only CI workflow](.github/workflows/prompts-check.yml) runs the existing structural check on main pushes, PRs and manual dispatch. It prints the checked revision and diagnostics to logs and a summary. One job, no site tests, model calls, dependency installation or deployment; actual run status must still be inspected.

## ChatGPT Deep Run

Deep Run now has a conditional ChatGPT execution adapter; Codex keeps its own runtime behavior.

In ChatGPT, the default objective is **verified useful progress per repository-tool round-trip**. The run maintains a compact evidence map (HEAD, relevant paths/SHAs, issues, workflow/deploy triggers, last published/verified SHA), searches to discover unknown paths and then switches to exact reads. High reasoning effort should reach a decision threshold and execute rather than repeatedly reopen the architecture.

For coherent multi-file changes, a write-capable ChatGPT surface should prefer a staged candidate Git commit: build the tree/commit without moving the branch, inspect the candidate diff, recheck HEAD, then fast-forward `main` with `force=false`. This reduces half-published multi-file states without requiring a branch/PR for every low-risk change.

For long work, prefer one existing issue checkpoint. If no issue/state artifact exists but real commits are already being made, a coherent commit body may carry a compact fallback cursor:

```text
Agent-Run: <stable-goal-key>
Agent-Next: <one executable next action>
Agent-Verify: <exact SHA/check status or explicit gap>
```

This is not a heartbeat commit and does not expose chain-of-thought. On resume, ChatGPT resolves current HEAD, finds the latest checkpoint, compares changes since the recorded SHA, and continues the unfinished action instead of re-auditing the repository.

Detailed rules are in [CHATGPT_DEEP_RUN.md](CHATGPT_DEEP_RUN.md).

## Website work: one command, stack-aware execution

[WEBSITE_STACKS.md](WEBSITE_STACKS.md) adds a conditional adapter for static sites on GitHub Pages, Next.js static export, and Next.js runtime deployments. Pages is a host, not an alternative to the Next.js framework. The assistant resolves the actual version, router, rendering mode, host/prefix and real checks from source; you do not need a separate prompt for each combination.

The guide routes a change through its source/data/template/checks, preserves generated-output and client/server boundaries, and separates production-build, route and browser evidence. It requires version-matched documentation and keeps preview publication subject to the existing deploy restrictions. It does not install a new stack, testing service or deployment pipeline.

The normal commands stay unchanged. An explicit website request can be:

```text
Prompts Deep Run EXECUTE на <project>. Определи стек по репозиторию и примени WEBSITE_STACKS.md. Сохрани текущий режим сборки и ограничения на push и deploy.
```

Only the applicable sections are loaded. No website fixtures or target-project configuration are stored in this prompt library.

## Templates

[Deep Run](loops/deep-run.md) and [Backlog Executor](loops/backlog-executor.md) are self-contained once filled. The agent entry point is [AGENTS.md](AGENTS.md).

The templates retain deep diagnosis, alternative hypotheses, skeptical review, experiments and iteration, but activate these only when they can affect the decision. They require real capability checks, preserve concurrent work and distinguish a branch fix from merged code, deployment and measured impact. A simulated user is not customer research; a green build is not proof of a useful product.

## GitHub working defaults

**Main-first, not main-at-any-cost.** When implementation publication is authorized, prefer small verified batches on the actual default branch. Keep explicit branch/no-push/no-deploy restrictions and protection intact. Reuse a permitted work branch when necessary; do not create one per microtask.

**One coherent change, one publication.** Prefer atomic multi-file commits over one commit per file. Check for concurrent changes and read back writes. After a timeout, establish whether the operation already succeeded before retrying.

**Checkpoints before the session ends.** For multi-batch work, keep one compact checkpoint from early in the run and update it after coherent batches and before lengthy/risky steps. Do not create issues or commits solely for heartbeat state.

**Lean CI, not disabled CI.** Existing CI can serve as remote verification when ChatGPT has no shell. Optimize validation only when observed friction justifies it and workflow edits are authorized: validation-only concurrency, separation from deployment, an always-reporting fast gate, path-aware expensive jobs, measured caches and justified matrix reduction. Do not toggle workflows off until the chat ends, blanket-apply `[skip ci]`, remove useful tests or treat skipped checks as passed verification.

Operational recipes are in [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md). These are prompt rules, not an installed scheduler or automatic recovery service.

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

Use `--spec -` for standard input. Rendering writes only prompt text to standard output; it does not call a model, read projects, write to GitHub or change permissions. Unknown/missing fields and unresolved placeholders fail instead of silently producing an incomplete prompt. Do not commit private run specifications.

## Supporting files

[MODEL_PROFILES.md](MODEL_PROFILES.md) separates environment capabilities from model choices. [RESEARCH.md](RESEARCH.md) records source-to-design decisions. Keep the repository project-neutral: do not add target-project datasets, fixtures, benchmark cases or generated run prompts containing private project context.

Keep exactly three commands unless repeated real use shows a genuinely different job that cannot fit the existing workflows.
