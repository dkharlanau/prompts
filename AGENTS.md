# Agent entry point

This library has **three user commands, two canonical templates**. Do not create prompt copies by project, role or model.

| User intent | Command | Template |
|---|---|---|
| Analyze, fill, clean or prioritize work | Deep Run BACKLOG | `loops/deep-run.md`, BACKLOG |
| Diagnose and improve the project now | Deep Run EXECUTE | `loops/deep-run.md`, EXECUTE |
| Implement the existing actionable queue | Backlog Executor | `loops/backlog-executor.md` |

Default ordinary "deep loop / improve" requests to EXECUTE; explicit backlog-only requests to BACKLOG. Do not restore a standalone Backlog Fill/Builder. Use BACKLOG then Executor only when a real handoff is needed. A small deterministic edit needs no full loop.

## When the user invokes Prompts

1. Read the selected canonical template from the current repository, noting its version/ref. Read target-project instructions and inspect the actual target repository/issues. This library is not automatically loaded into every ChatGPT conversation. Use available connectors; do not pretend a remembered template is the current file.
2. Resolve project aliases from evidence. Do not guess a repository from a brand name. Fill PROJECT, GOAL, CONTEXT, AUTHORITY, CONSTRAINTS and DONE_WHEN yourself from the request, trusted project context and live state. Include only context that changes the task: target user, source paths, baseline/ref, relevant issue scope and known blockers. Mark decision-changing unknowns; never invent measurements, issue IDs or test commands.
3. Separate intended outcome from permission. Carry forward all applicable restrictions, including no-push and no-deploy. Specify allowed file/issue/branch operations and the completion boundary. If branch policy is absent, prefer isolated work; do not infer merge, release, spending or destructive-action permission. Account for preview deployments before remote writes.
4. Produce a self-contained run prompt with no unresolved placeholders and only the selected mode. The optional renderer performs this mechanical step; it does not discover project context or grant permission. In ordinary chat, assemble the same text directly.
5. When asked to run, act through the available tools, not merely return the prompt. When asked only to prepare a prompt, return the filled prompt without executing it. Proceed with safe independent work rather than repeatedly asking for routine details.

Consult [MODEL_PROFILES.md](MODEL_PROFILES.md) when selecting a runtime/model; do not prepend the entire library to every task. A model name in a prompt does not switch the current model or create Codex/subagents. Keep reports concise, factual and in the user's language.

## Maintaining this repository

Run `python3 scripts/prompts.py check` and `python3 -m unittest discover -s tests -v` after changes. Keep links, catalog versions and input fields consistent. Keep both templates independently usable outside this checkout. Do not add generated run prompts containing private project context to this public repository.

For a reusable failure, improve the relevant template and add an evaluation case. Preserve conditional reasoning rather than fixed role/iteration quotas. Consult [BENCHMARKS.md](BENCHMARKS.md) for behavioral evidence; static checks do not prove agent performance. Promote versions only with recorded real-run results. The source rationale is in [RESEARCH.md](RESEARCH.md).
