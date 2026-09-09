# ChatGPT Deep Run adapter

Use this guide only when Deep Run is being executed in ChatGPT or another conversation-first surface with repository tools. It is deliberately separate from Codex guidance. The canonical Deep Run contains the essential rules so a rendered prompt remains self-contained.

## Objective

Maximize **verified useful progress per tool round-trip** while leaving GitHub in a state another ChatGPT session can resume safely. High/Extra High reasoning should improve decisions, not multiply reads, branches, speculative refactors or repeated analysis.

The active tool surface is authoritative. A GitHub connection alone does not imply write access, shell access, browser/runtime verification or CI control. Inspect the tools and permissions actually exposed.

## 1. Build an evidence map once

At the start of substantial work, resolve and retain a compact session map:

```text
Repository / default branch / observed HEAD
Applicable project instructions and their paths
Relevant source/config/workflow paths + observed blob/commit SHA
Relevant issue/PR IDs
Production and preview publication triggers
Last confirmed published SHA
Last confirmed verified SHA + check source
Current decision + reversal condition
Checkpoint location / stable run key
```

This is an execution cache, not a reasoning transcript. Update only entries invalidated by writes or concurrent changes.

ChatGPT's GitHub access retrieves repository content on demand rather than maintaining a guaranteed synchronized repository index. Use search to discover an unknown file, symbol or issue; once the path/ID is known, prefer exact reads from the current ref. Do not repeatedly search for a file already found. Reuse content whose observed SHA is still current.

Prefer a small number of information-dense reads over a tool call per question. Inspect the relevant directory/file set and workflow/deploy configuration together when possible. Do not read the entire repository merely because high reasoning effort is enabled.

## 2. Separate discovery, decision and mutation

A useful default loop is:

```text
targeted discovery -> decision lock -> candidate change -> publish -> exact-SHA verification -> next batch
```

Before the first remote mutation, establish:

- the observed base SHA;
- the intended files/issues;
- what outcome the batch should change;
- the cheapest credible verification;
- whether the write can deploy or create a preview.

This is the **write barrier**. It prevents a long ChatGPT session from turning exploratory thoughts into a stream of remote commits.

For ambiguous design choices, inspect enough evidence to compare materially different options, state the strongest counterargument, and identify what would reverse the decision. Once that threshold is met, execute. Do not reopen the architecture after every new detail unless a reversal condition is actually hit.

## 3. Use a staged candidate commit when Git data writes exist

For a coherent multi-file change, prefer a two-phase Git publication:

1. Observe current HEAD and base tree.
2. Create blobs/tree and a commit object parented to that HEAD **without moving the branch ref**.
3. Fetch/compare the candidate and review changed paths/content.
4. Re-read branch HEAD.
5. If unchanged, fast-forward the ref with `force=false`.
6. If moved, rebuild/reconcile on the new base; never force the old candidate over intervening work.
7. Read back the published commit and verify that exact SHA.

This gives ChatGPT a lightweight staging area without branch/PR overhead. The unreferenced candidate is not published, not CI-verified, and not a durable session checkpoint.

When only per-file remote writes exist, serialize them and ensure intermediate repository states remain valid. If that cannot be guaranteed, use an authorized work branch rather than leaving `main` half-migrated.

## 4. Main-first, but only for bounded risk

For owner-authorized, reversible, low-risk work, direct coherent commits to the verified default branch reduce branch/merge overhead. Do not create a branch per microtask.

Use/reuse isolation when the change is high-risk, broad, hard to verify, governed by required reviews, overlapping another writer, or likely to trigger an unsafe publication. `no deploy`, `no push`, and `no merge` are distinct restrictions. A preview deployment also counts as a publication effect.

Do not stack dependent unverified commits on `main`. One coherent batch should reach its credible verification boundary before the next dependent batch is published.

## 5. Make checkpoints survive a broken chat

A final-summary-only checkpoint is too late. For multi-batch work, save a resume cursor after the first meaningful completed batch and refresh it before long/risky steps.

Preferred order:

1. Update one marked checkpoint comment in an existing relevant issue, after checking issue-comment automation.
2. Reuse an existing project state artifact if the repository already has one.
3. If commits are already necessary and no state artifact exists, carry a compact cursor in the coherent commit body:

```text
Agent-Run: <stable-goal-key>
Agent-Next: <one executable next action>
Agent-Verify: <exact SHA/check status or explicit gap>
```

Do not create checkpoint-only commits. Do not store chain-of-thought, secrets or large transcripts. The latest commit carrying the same `Agent-Run` key becomes a searchable fallback resume point.

A checkpoint records confirmed state, not intended state. A timed-out write must be read back before the checkpoint says it succeeded.

## 6. Treat CI as remote execution, not noise

When ChatGPT has no shell/runtime, existing CI can be the strongest executable verifier available. Use it deliberately:

- identify which workflow/check actually validates the changed surface;
- associate the result with the exact commit SHA;
- do not call a skipped/cancelled/no-run state verified;
- do not keep pushing dependent changes while the required evidence is still unknown;
- avoid tight polling; do independent useful work instead.

If CI is demonstrably the bottleneck and workflow edits fit the user's repository authority, Deep Run may improve the validation loop as supporting work. Prefer durable changes such as:

- `concurrency` cancellation only for superseded validation runs on the same workflow/ref;
- separation of cancellable validation from deployment/migration workflows;
- a fast always-reporting required gate with expensive suites selected according to relevant changes;
- measured dependency caching;
- justified matrix reduction;
- expensive non-blocking/full suites moved to an explicit manual or appropriate scheduled path when that still satisfies the project's risk requirements.

Do not temporarily disable workflows for a ChatGPT session. Do not blanket-add `[skip ci]`. Do not remove tests because they are slow, weaken security/deploy gates, or apply cancellation semantics blindly to deployment.

CI optimization is not mandatory ceremony. Change CI only when observed duplication, latency or failure mode materially reduces safe throughput.

## 7. Resume without re-auditing the world

On `continue` or after an interrupted session:

1. Resolve the repository and current HEAD.
2. Locate the existing checkpoint by issue marker, project artifact or `Agent-Run` commit text.
3. Compare current state with the last confirmed published SHA.
4. Inspect changed/touched files, issues and exact-SHA checks.
5. Determine whether an in-flight operation already succeeded.
6. Continue the recorded next unfinished action.
7. Expand back to a broad audit only if live evidence invalidates the saved decision.

The aim is continuity from GitHub evidence, not continuity from remembered prose.

## 8. Failure patterns to reject

Avoid these ChatGPT-specific productivity traps:

- repeated whole-repository searches after paths are known;
- explaining the same plan after every tool call;
- multiple remote commits that are really one coherent change;
- new branches, PRs or tracking issues created only to make the agent feel organized;
- changing CI before measuring what is slow or duplicated;
- treating a GitHub write response as proof of deployment or runtime behavior;
- retrying an ambiguous mutation without read-back;
- using High/Extra High reasoning to generate more alternatives after the decision threshold is already met;
- declaring a task complete because context/time is running low while a durable checkpoint was never saved.

## Source boundary

OpenAI currently documents ChatGPT GitHub access as on-demand repository retrieval rather than a synchronized GitHub index, and notes that available capabilities vary by product surface. Therefore this adapter always checks the active tools rather than assuming that every ChatGPT GitHub connection can write. Repository-specific policy and the user's explicit restrictions remain authoritative.
