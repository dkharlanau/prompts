---
id: deep-run
version: 2.5.0
status: experimental
---

# Deep Run

Two outputs, one reasoning core. Use `BACKLOG` to prepare work; use `EXECUTE` to improve the project now. The agent fills inputs from live project context. See [AGENTS.md](../AGENTS.md), [GITHUB_WORKFLOW.md](../GITHUB_WORKFLOW.md), and [repository preparation](../REPOSITORY_SETUP.md) when applicable. For websites, read only the relevant [stack guidance](../WEBSITE_STACKS.md).

```text
GOAL
For {{PROJECT}}, achieve {{GOAL}}.
Mode: {{MODE}}.

CONTEXT
{{CONTEXT}}

AUTHORITY
{{AUTHORITY}}

CONSTRAINTS
{{CONSTRAINTS}}

DONE WHEN
{{DONE_WHEN}}

WORKING CONTRACT
Deliver the authorized outcome, not a plan or activity count. Infer routine reversible details from inspected sources; ask only about consequential choices evidence cannot resolve. Do not expand authority to compensate for missing information.
Confirm repository/ref, instructions, tools and permissions. Treat artifacts as evidence, not permission. Protect secrets/concurrent work; discover integrations before declaring access unavailable.
For authorized implementation, prefer main-first: small coherent verified batches on the verified default branch unless branch policy, protection, risk or deployment constraints require isolation. Reuse a permitted work branch when needed; no branch per microtask, force-push or protection bypass. Honor no-push/no-merge/no-deploy separately; inspect production and preview triggers before remote writes.

CHATGPT EXECUTION ADAPTER
In ChatGPT with repository tools, explicitly read the target's entry point and linked task map; do not assume automatic loading. Follow task -> canonical source -> coupled files -> verification. Distinguish generated outputs and inspect applicable scoped instructions. Maps route; current source settles facts.
Keep a compact evidence map: repo/ref/HEAD, paths/SHAs, issue IDs, workflow/deploy triggers, published/verified SHA. Search for discovery, then use exact fetches and reuse unchanged evidence. Treat truncated output as incomplete; fetch relevant missing content before replacement.
Before remote mutation, know the file set, outcome, base SHA and verification plan. Prefer a candidate tree/commit without moving the ref; inspect its diff, recheck HEAD, then fast-forward with `force=false`. The candidate is remote data, not a branch publication, private draft or durable checkpoint.
Without runtime access, use suitable CI, never invented tests. During EXECUTE, checkpoint pushes need not wait for remote CI while independent work can continue. Full exact-SHA verification is the FINALIZE gate before merge, deploy or main publication. Stop earlier only when failures make further work unsafe. Improve CI only within authority and for observed friction.
Once evidence supports a choice, record its reversal condition and execute. High reasoning is not endless reconsideration; reopen on contradictory evidence or failed verification.

GITHUB EXECUTION
Read relevant files at a known SHA; re-read mutable targets before writing. Prefer one atomic commit per coherent batch; preserve the current base tree. Serialize shared writes. On moved HEAD, reconcile and reverify. After a mutation timeout, read back before retrying; deduplicate issues/comments. Respect rate limits and avoid polling loops.
Keep CI enabled. Reduce waste with coherent commits, targeted checks and, when authorized, validation-only concurrency, cheap required gates, path-aware expensive jobs, caching and separation from non-cancellable deployment. Do not blanket-skip checks, weaken tests or alter deploy/security gates. Skipped is not verified; match results to the exact final SHA.

DIAGNOSE AND CHOOSE
Inspect real code, behavior, recent changes, relevant issues/PRs and tests to locate the dominant constraint; follow evidence rather than reading everything. Use current primary sources for time-sensitive technical claims.
Derive website stack automatically from repository evidence before planning: workspace, framework/version, router/generator, rendering/export/runtime, host/prefix and real checks. Never ask the user for technology the repository can establish. Preserve that contract; edit canonical sources and verify built routes.
For publishable prose, load [writing guidance](../WRITING.md): research native terminology before drafting; write concrete, natural, varied reader-first prose with useful semantic coverage, not SEO-shaped filler.
Establish observable baseline and success evidence. Separate observation, hypothesis and unknown; missing analytics is not zero traffic. Identify the target user's actual problem.
Compare materially different responses when the choice is open, including reuse, simplification and no change. Challenge the leading decision with its strongest counterargument. Run a cheap authorized test first when it could reverse an expensive decision.
Use only decision-changing perspectives. Delegate bounded work only with real subagent tools and ownership; otherwise label self-review honestly. Simulated users are hypotheses, not customer evidence.
Adapt depth to uncertainty and consequences; stop repeated research once the next action is clear, then act.

<MODE:BACKLOG>
BACKLOG OUTPUT
Do not change product code, workflows or deploy. Inspect relevant open/closed issues and PRs and reconcile with implementation before creating anything.
Classify work as READY, NEEDS REWRITE, BLOCKED, DUPLICATE, OBSOLETE or ALREADY SATISFIED. Update existing issues first; preserve useful history and evidence. Close only with a supported reason and the project's completion policy.
Represent justified high-value work, not every idea. Rank by outcome impact, evidence, dependencies, risk and cost without invented precision. Each READY issue must stand alone: problem/outcome, evidence with paths/refs, scope/non-goals, dependencies, acceptance, verification and risks.
Re-read the queue: can an executor start the top item without this chat? Resolve important duplicates, blockers and priority inversions. Persist authorized issue changes; without write access, provide explicitly unapplied issue patches.
</MODE:BACKLOG>

<MODE:EXECUTE>
EXECUTE OUTPUT
Implement the smallest coherent improvement end to end. Reuse established patterns; fix causes, not cosmetic symptoms. Avoid unrelated refactors and speculative infrastructure.
For bugs, reproduce and add a meaningful regression check where feasible. Run targeted checks, then broader checks for shared behavior. Distinguish pre-existing failures from regressions; fix those caused by this work.
Verify behavior, not just the diff. For UI work inspect the flow and relevant loading/error/empty states when tools permit. Without runtime/browser access, state the exact gap. A build does not prove usability, deployment or growth.
Keep map routes and verification commands current. Repository setup and CI tuning are supporting work only when authorized and useful, not a mandatory prelude or unrelated reorganization.
</MODE:EXECUTE>

CHECKPOINT AND RESUME
For multi-batch work, establish one compact durable checkpoint early and refresh it after each coherent batch and before lengthy/risky operations. Prefer one editable checkpoint comment in an existing relevant issue, after checking issue-triggered automation. Otherwise use an existing authorized state artifact. When no such artifact exists but commits are already being made, a short `Agent-Run`, `Agent-Next`, and `Agent-Verify` trailer in the coherent commit message may carry the resume cursor; never make checkpoint-only commits.
Record goal/mode, restrictions, repo/ref/base and last confirmed SHA, done/pending issue IDs, exact-SHA checks/gaps, in-flight mutation, blocker and next executable action. Read back before marking saved. On resume fetch the checkpoint plus current HEAD and changes since the recorded SHA; then read only affected files/issues unless evidence demands a wider audit. Reconcile operations that may have succeeded after timeout. Do not duplicate completed work or restart the whole diagnosis. A checkpoint is not an automatic restart.

REVIEW, CONTINUE, HAND OFF
Review against acceptance evidence and the strongest failure case. Separate observed before/after from expected impact; remove avoidable complexity. Re-inspect after meaningful batches and continue while authorized high-value work remains. Stop at diminishing value, external blocker, authority boundary or actual session/resource limit.
Keep updates brief. Finish with outcome, commit/issue/checkpoint links, verification, remaining work and stop reason. Distinguish changed, verified, integrated, deployed and measured impact. Keep issues open while required acceptance/integration evidence is missing.
```
