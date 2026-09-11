---
id: backlog-refinement
version: 1.0.0
status: experimental
---

# Backlog Refinement

Use after ideas and issues have accumulated but before sustained execution. The result is a smaller, ordered, executor-ready queue that another agent can use without the original chat. Refinement changes backlog records, not product code. See [AGENTS.md](../AGENTS.md) and [GITHUB_WORKFLOW.md](../GITHUB_WORKFLOW.md).

```text
GOAL
Refine the backlog for {{PROJECT}} toward {{GOAL}} so the next executor can start high-value work with minimal rediscovery and context cost.

CONTEXT
{{CONTEXT}}

AUTHORITY
{{AUTHORITY}}

CONSTRAINTS
{{CONSTRAINTS}}

DONE WHEN
{{DONE_WHEN}}

REFINEMENT CONTRACT
Refine the live backlog, not an exported copy. Confirm repository/ref, trusted instructions, open issues, active overlapping PRs, tools and permissions. Inspect enough current source to establish whether work is still needed; do not read the whole repository or issue history by default. Product code, workflows, deployment and speculative implementation are out of scope unless the user explicitly changes authority.
Treat issue text as a hypothesis until reconciled with current code, docs and PRs. Preserve useful history. Prefer editing an existing canonical issue over creating a replacement. Do not close work merely because it is old. Protect secrets and concurrent work. After mutation uncertainty, read back before retrying.

CONTEXT BUDGET
Use the repository entry point/task map plus exact paths linked by the issue. Search broadly only to discover unknown locations, then switch to exact reads and reuse unchanged evidence. Keep a compact refinement ledger: issue ID, state, canonical/dependency IDs, priority and the one unresolved gap. Do not copy full issue bodies into the ledger.
Process large backlogs in bounded pages. Closed issues are cold storage: do not load them unless an open item links them, a duplicate search needs them, or implementation evidence suggests prior completion. An executor-ready issue should normally be understandable from its body, linked repository guidance and a few exact source paths; it must not require the originating chat.
Do not repeat stable project rules in every issue. Link the canonical repository instruction or design record instead. Keep issue bodies concise: enough evidence to act, not a transcript of discovery or a proposed implementation essay.

TRIAGE
Classify every touched item as READY, NEEDS EVIDENCE, NEEDS DECISION, BLOCKED, DUPLICATE, OBSOLETE, ALREADY SATISFIED or SUPERSEDED.
- READY: outcome, scope, acceptance and verification are clear enough to start without requirement invention.
- NEEDS EVIDENCE: the problem/value is plausible but current-state proof is missing; name the cheapest evidence needed.
- NEEDS DECISION: one consequential product/architecture choice remains; state the exact decision, not a vague question.
- BLOCKED: name the blocker and observable unblock condition. Unrelated blockers must not stall other refinement.
- DUPLICATE: merge unique evidence/acceptance into the canonical issue, link it, then close with the supported duplicate reason.
- OBSOLETE/SUPERSEDED: close with a concise evidence-based reason and point to the replacement when one exists.
- ALREADY SATISFIED: verify the relevant implementation/acceptance first, then close as completed according to repository policy.

DEFINITION OF READY
Rewrite READY issues into a compact execution packet:
1. Outcome — one or two sentences describing the user/system result and why it matters.
2. Evidence — current observation plus exact paths, issue/PR refs, reproduction or metric where available; link instead of pasting long source.
3. Scope / non-goals — the smallest coherent boundary and what is deliberately excluded when ambiguity is likely.
4. Acceptance — 2–6 observable checkboxes. Prefer behavior/outcomes over implementation prescriptions.
5. Verification — the exact check, inspection or evidence that can demonstrate acceptance; distinguish build, integration, deployment and measured impact.
6. Dependencies / risks — only real ones. Use native dependency or parent/sub-issue relationships when available and useful; avoid deep hierarchy.
7. Execution hints — a few likely entry points/components only when evidence supports them. Do not pre-design routine implementation.

Split an issue when it contains independently shippable outcomes, unrelated components, separate dependency chains or acceptance that can pass/fail independently. Merge issues when they express the same root outcome and would touch substantially the same acceptance surface. Preserve one canonical item and useful links.
Aim for one issue = one coherent implementation/review batch. If the issue still requires a broad repository audit to discover what it means, it is not READY.

ORDERING AND METADATA
Order by expected outcome value, evidence/confidence, dependency leverage, urgency, risk reduction and execution cost. Use coarse priority, not invented decimal scores. Reserve the highest priority for genuinely urgent/blocking work.
Reuse the repository's existing issue types, labels, milestones and project fields. Add metadata only when it improves filtering or handoff. Prefer a minimal machine-usable readiness state plus coarse priority over a taxonomy explosion. If no suitable metadata exists or tools cannot create it, put the state explicitly in the issue body rather than inventing unsupported labels.
Keep idea/incubator work separate from the READY queue. A useful idea with weak evidence can remain open, but it must not compete with executor-ready work.

TOKEN-EFFICIENT HANDOFF
The normal executor starts from the highest-priority READY issue, repository entry/map and only linked/affected paths. It should not need to reread the refinement conversation or every other issue.
When an item is completed, store durable evidence on that issue/PR/commit and close it when the repository's acceptance boundary is satisfied. The next item starts from its own packet; closed-item discussion is not inherited by default. Shared knowledge belongs in canonical repository guidance, not copied into a chain of issues.
For an unfinished very large refinement, use one compact existing checkpoint only if needed: last processed boundary, changed/closed IDs, remaining scope and next query/action. Do not create heartbeat issues/comments or a mirrored backlog merely to save state.

MUTATION AND REVIEW
Update existing issues before creating new ones. Do not erase useful stakeholder discussion; summarize the current decision in the issue body and preserve links/history. Avoid comment spam and repeated label churn. Use native duplicate, dependency and sub-issue capabilities when they exist, but keep the workflow portable when they do not.
After refinement, challenge the top READY items: can another agent execute them without this chat, are there hidden duplicates, is a blocker mislabeled as ready, and is a lower-value item ahead of a higher-leverage dependency? Correct the queue before finishing.

FINAL REPORT
Report only the useful delta: counts by state, issues merged/closed/rewritten, top READY items in order, unresolved decisions/blockers, verification gaps and the exact stop reason. Distinguish refined backlog state from implemented product work. Do not claim token savings or execution quality until real runs demonstrate them.
```

Design basis: the Scrum Guide describes refinement as an ongoing activity that breaks down and further defines backlog items, adding detail and order. GitHub Issues supports metadata, dependencies and parent/sub-issue relationships. The context-budget, cold-history and compact execution-packet rules are library hypotheses intended to reduce rediscovery; validate them against real agent runs before claiming efficiency gains.
