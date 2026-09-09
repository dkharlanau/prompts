# Agent entry point

This library has **three user commands, two canonical templates**. Do not create prompt copies by project, role, model or runtime.

| User intent | Command | Template |
|---|---|---|
| Analyze, fill, clean or prioritize work | Deep Run BACKLOG | `loops/deep-run.md`, BACKLOG |
| Diagnose and improve the project now | Deep Run EXECUTE | `loops/deep-run.md`, EXECUTE |
| Implement the existing actionable queue | Backlog Executor | `loops/backlog-executor.md` |

Default ordinary "deep loop / improve" requests to EXECUTE; explicit backlog-only requests to BACKLOG. Do not restore a standalone Backlog Fill/Builder. Use BACKLOG then Executor only when a real handoff is needed. A small deterministic edit needs no full loop.

## When the user invokes Prompts

1. Read the selected canonical template from the current repository, noting version/ref. Read target-project instructions and inspect the actual target repository/issues. This library is not automatically loaded into every conversation. If Deep Run is executing in ChatGPT rather than a coding checkout, apply the relevant [ChatGPT Deep Run adapter](CHATGPT_DEEP_RUN.md). Use available connectors; do not pretend a remembered template is the current file.
2. Resolve project aliases from evidence. Do not guess a repository from a brand name. Fill PROJECT, GOAL, CONTEXT, AUTHORITY, CONSTRAINTS and DONE_WHEN yourself from the request, trusted project context and live state. Include only context that changes the task: target user, source paths, baseline/ref, relevant issue scope and known blockers. Mark decision-changing unknowns; never invent measurements, issue IDs or verification commands.
3. Separate intended outcome from permission. Carry forward all restrictions, including no-push and no-deploy. Specify allowed file/issue/branch operations and completion boundary. If branch policy is absent and implementation writes are authorized, prefer small coherent verified commits to the verified default branch (main-first). Existing branch instructions, protection, risk and production/preview deployment constraints take precedence. Reuse a permitted work branch when isolation is needed; do not infer release, spending, destructive-action or protection-bypass permission.
4. Produce a self-contained run prompt with no unresolved placeholders and only the selected mode. Resolve runtime behavior, branch/publication policy, CI verification and checkpoint destination within the existing six fields; no extra questionnaire. The optional renderer performs the mechanical step; it does not discover context or grant permission.
5. When asked to run, act through the available tools, not merely return the prompt. When asked only to prepare a prompt, return the filled prompt without executing it. Proceed with safe independent work rather than repeatedly asking for routine details.

## ChatGPT + GitHub runs

The Deep Run template contains the essential ChatGPT adapter. Use [CHATGPT_DEEP_RUN.md](CHATGPT_DEEP_RUN.md) for the detailed execution recipe and [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md) for GitHub/CI mechanics. Do not apply the ChatGPT adapter to Codex merely because the target is GitHub-hosted.

In ChatGPT, optimize verified progress per connector round-trip: keep a compact SHA-based evidence map, search only for discovery, reuse exact paths/IDs, batch independent reads, establish a write barrier before remote mutations, and use a staged candidate Git commit when supported. High reasoning effort is not a reason to keep reopening a decision after its reversal condition is known.

Default to atomic coherent commits, early incremental checkpoints and CI left enabled. A GitHub connector file edit is already a remote publication, not a local draft. BACKLOG remains issue-only; main-first never converts it into implementation. When no issue/state artifact exists, a coherent commit may carry `Agent-Run`, `Agent-Next`, and `Agent-Verify` trailers as the durable resume cursor; never create a checkpoint-only commit.

On "continue/resume", locate the existing goal/checkpoint and reconcile it with live HEAD, changes since the last confirmed SHA and exact-SHA checks before doing another audit. No duplicate tracking issues, heartbeat commits or public reasoning transcripts.

Consult [MODEL_PROFILES.md](MODEL_PROFILES.md) when selecting a runtime/model; do not prepend the entire library to every task. A model name in a prompt does not switch the current model or create Codex/subagents. Keep reports concise, factual and in the user's language.

## Maintaining this repository

Run `python3 scripts/prompts.py check` after changes. Keep links, catalog versions and input fields consistent. Keep both templates independently usable outside this checkout. Do not add generated run prompts containing private project context to this public repository.

For a reusable failure, improve the relevant canonical template or runtime adapter rather than adding a project-specific prompt, fixture, benchmark or test case. Preserve conditional reasoning rather than fixed role/iteration quotas. Keep this repository project-neutral and focused on prompt design. The source rationale is in [RESEARCH.md](RESEARCH.md).
