# GitHub working protocol

For ChatGPT connectors and coding environments. Apply to authorized GitHub work, not as permission to change every repository. Essential rules are already inside both canonical templates. For conversation-first execution, also use [CHATGPT_DEEP_RUN.md](CHATGPT_DEEP_RUN.md). Read only the relevant recipes; keep project-specific state in the target project, not this library.

## 1. Main-first without branch sprawl

Resolve the actual repository, default branch, current HEAD, project instructions, protection and publication triggers. Use `main` only when it is the correct branch. Default authorized low-risk implementation to small coherent verified commits on that branch. BACKLOG stays issue-only.

Explicit branch/no-push/no-merge/no-deploy restrictions override this preference. A connector's file edit commits remotely; it is not a local draft. A branch push can create a preview, while a main push can publish production. Do not use a branch or a CI skip token as an assumed no-deploy switch. When publication effects cannot be established under a no-deploy restriction, keep an unapplied/local patch.

Reuse the existing permitted work branch when work is risky, incompletely verified, overlapping another writer, or governed by PR requirements. Do not force a switch to main, create branches per microtask, automatically merge unfinished work, remove protection or delete other branches. Parallel reviewers may inspect separate concerns; use one coordinated writer for a shared branch. An issue comment is an advisory ownership signal, not a lock.

No shell does not mean no useful work. It does mean that local tests have not run. Publish only changes whose risk fits the available evidence; hand off high-risk edits when the required verification environment is missing. If your main batch causes a regression, repair it or make a targeted revert commit preserving later work before publishing unrelated changes.

## 2. Atomic publication, not a commit per file

Use a supported multi-file commit capability. When Git data tools are available:

1. Read target HEAD and its commit's tree SHA. Fetch affected source at that snapshot; inspect the complete relevant content before replacing a file.
2. Prepare only intended file entries on the **existing base tree**. Preserve unrelated paths, modes and concurrent edits. Omitting the base tree can remove unrelated files from the resulting commit.
3. Create one tree and one commit parented to the observed HEAD. Before moving the ref, fetch/compare this candidate when the environment supports it. This is a useful staging barrier for ChatGPT, but the unreferenced candidate is not published, CI-verified or a durable checkpoint.
4. Re-read target HEAD. If it moved, reconcile on the new base and repeat affected verification. Update the ref with `force=false`. A non-fast-forward rejection requires reconciliation, not a forced retry.
5. Read back the branch/commit and changed paths. Record the actual published SHA; inspect validation for that SHA.

Blobs/trees/a commit created without a ref update are not publication and not a reliable permanent checkpoint by themselves. Local preparation or a staged Git object must never be reported as "in main".

If only per-file writes exist, use current blob SHAs, serialize mutations and keep each intermediate state compatible. If that cannot be done safely, use an authorized isolated branch or provide a patch. Do not approximate an atomic update by leaving main half-migrated. Prefer one meaningful commit per coherent batch, not one giant unverified commit for the entire session.

See the official [tree](https://docs.github.com/en/rest/git/trees) and [reference](https://docs.github.com/en/rest/git/refs) APIs.

## 3. Checkpoint early; resume from evidence

For multi-batch work, save a first checkpoint once the goal, scope and next action are known. Update after each completed coherent batch, after a useful finding in a long investigation, and before costly/risky operations. Do not wait until a crash seems imminent. No timer, automatic restart or final save is guaranteed by prompt text.

Prefer **one editable checkpoint comment in an existing relevant issue**, found by issue ID and a stable marker such as `<!-- prompts-checkpoint:goal-key -->`. Read it before updating and edit only your own checkpoint content. Check issue/comment/label-triggered automation; a comment is not universally side-effect-free. Do not create a new issue or comment per step.

If there is no suitable issue, reuse an authorized state artifact. A small `.agent/checkpoint.md` is an option only if appropriate to the project; include its updates with real changes, not heartbeat commits. In ChatGPT, when no such artifact exists but coherent commits are already necessary, a compact commit-body fallback is allowed:

```text
Agent-Run: <stable-goal-key>
Agent-Next: <one executable next action>
Agent-Verify: <exact SHA/check status or explicit gap>
```

Do not create checkpoint-only commits. Do not overwrite durable `AGENTS.md` instructions with session logs. If remote writes are prohibited, use a local handoff or the chat response and disclose that another session may not have access to it. Never put credentials, private data or unnecessary reasoning transcripts in public notes.

Suggested compact issue/state-artifact format; fill from observed state, not predictions:

```text
Goal / mode / stable run key:
Repository / branch:
Authority / restrictions, including push and deploy:
Base SHA / last confirmed published SHA:
Done: issue IDs, paths and result:
Checks: command or run URL, tested SHA, result / not run:
Pending: remaining acceptance or issue IDs:
In-flight mutation: intended operation, target and expected effect, or none:
Blocker / failed attempt worth not repeating:
Next action: one executable step:
Updated at: observed timestamp and timezone:
```

Read back a checkpoint before saying it was saved. "Published" and "verified" are different fields in practice; never advance either on a queued request or predicted result. When a checkpoint is included in a commit, record only information knowable at commit creation; later exact-SHA verification belongs in the next checkpoint or external state.

On resume, load the applicable prompt and checkpoint, inspect current HEAD/diff, linked issues and exact-SHA checks. Reconcile changes since the recorded SHA, including an operation that succeeded after its response timed out. Continue the next unfinished action without duplicating issues, commits or the entire audit. Newer user restrictions take precedence. Start a fresh diagnosis only when evidence invalidates the saved plan.

## 4. Lean CI that remains safe after an interrupted chat

Default: **leave CI enabled**. Do not temporarily disable workflows "until this session finishes"; interruption can leave the repository unprotected. Do not remove useful tests to reduce runtime or hide a failure.

When CI tuning is in scope, first establish the concrete bottleneck from triggers, required checks, recent runs, duration/duplication or failure evidence. A Deep Run may treat a minimal validation-loop improvement as supporting implementation work when repository workflow edits are within its authority and the change does not cross deployment/security boundaries. Do not redesign CI speculatively.

Prefer, in order:

- coherent batched commits, fewer duplicate triggers, and relevant checks before publication;
- cancellation of superseded **validation-only** runs on the same workflow/ref:

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

- separation of cancellable validation from deployment/migration when currently mixed and the project can preserve its release guarantees;
- a small always-reporting required gate, with expensive work selected by relevant changes and an aggregate result that fails on relevant failures/cancellations;
- measured dependency caching, justified matrix reduction and expensive optional/full suites on an explicit manual or appropriate scheduled path.

Do not apply validation cancellation to deployment or migration blindly. Avoid blanket `[skip ci]`/`[no ci]` commit messages. Skipping an entire required workflow by paths, branches or commit text can leave its check pending. Prefer job-level selection inside an always-reporting workflow when required checks exist. See [workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency), [workflow skipping](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs), and [job conditions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-jobs-with-conditions).

For each published batch, match workflow, event and **head SHA**, not the latest green run on the branch. Some connector helpers return only subsets of runs; use the best available exact-SHA evidence and state gaps. No run, pending, skipped and cancelled are not verified. If checks are still running, record links, do useful independent work and avoid tight polling or piling dependent unverified code onto main.

## 5. Fewer calls, safer retries, cleaner issues

Discover tool capabilities once; use their actual schemas. Read repository structure and targeted files at a known SHA, then reuse unchanged evidence. Use source search for discovery, not as the authoritative current file. Re-read mutable targets before writes and after ambiguous results. Do not repeatedly fetch the whole repository, backlog or unchanged logs.

Use stable issue/PR IDs and search existing open/closed work before creating anything. Update existing acceptance criteria and your checkpoint rather than generating parallel task systems. Add labels without erasing unrelated labels; preserve other authors' issue text. Close only when the recorded acceptance boundary is met, not merely because a commit exists.

After a write timeout, inspect the exact target/ref/recent issue or comment before retrying: the write may already have succeeded. If the result remains ambiguous, checkpoint it and stop that mutation rather than create duplicates. Distinguish permission/protection failures from transient transport failures. Do not turn a 403 into permission-bypass attempts.

Respect retry/reset headers and bounded backoff. Serialize write operations; avoid bursts and unnecessary parallel REST calls. If a rate limit exceeds the usable session, preserve the handoff instead of promising to resume later. See [GitHub REST best practices](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api).

## Applying these defaults

No fourth command or new required input is needed. Put resolved branch/publication policy in AUTHORITY, runtime/CI boundaries in CONSTRAINTS and DONE_WHEN, and checkpoint location in CONTEXT. Keep every copied run prompt self-contained. These defaults reduce avoidable work; they do not replace project-specific judgment or demonstrate measured speed/reliability gains.
