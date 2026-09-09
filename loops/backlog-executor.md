---
id: backlog-executor
version: 1.0.0
status: candidate
category: autonomous-execution
purpose: consume an existing GitHub backlog and deliver verified changes until no actionable high-value work remains
best_for: Codex, Kimi or other coding/product agents with repository and issue access
avoid_when: backlog quality is poor, authority is unclear, or changes require frequent irreversible human decisions
benchmark_target: DRS-100 >= 85 plus execution-specific checks
model_strategy: see MODEL_PROFILES.md
---

# Backlog Executor

## Inputs

- `{{PROJECT}}`
- `{{GOAL}}`
- `{{CONTEXT}}`
- `{{CONSTRAINTS}}`
- `{{AUTHORITY}}`
- `{{BACKLOG_SYSTEM}}`
- `{{WORKING_BRANCH_OR_POLICY}}`
- `{{VERIFICATION}}`
- `{{STOP_CONDITION}}`

## Template

```text
GOAL
Autonomously execute the actionable backlog for {{PROJECT}} toward {{GOAL}} until no justified executable work remains under the current authority.

CONTEXT
{{CONTEXT}}

CONSTRAINTS
{{CONSTRAINTS}}

AUTHORITY
{{AUTHORITY}}

BACKLOG SYSTEM
{{BACKLOG_SYSTEM}}

WORKING POLICY
{{WORKING_BRANCH_OR_POLICY}}

VERIFICATION
{{VERIFICATION}}

OPERATING PRINCIPLE
Deliver verified product progress, not issue throughput.
An issue is not complete because code was written. It is complete only when its intended outcome and acceptance criteria are satisfied and regressions are checked.

EXECUTION LOOP

1. SYNC STATE
Inspect the current repository, branch, open backlog, recent commits, tests/build status, documentation and relevant product state before selecting work.
Resolve obvious mismatch between issue text and reality before implementation.

2. TRIAGE ACTIONABLE WORK
Classify relevant open issues:
- READY;
- BLOCKED;
- STALE/OBSOLETE;
- DUPLICATE;
- ALREADY DONE;
- NEEDS HUMAN DECISION.
Update backlog state when {{AUTHORITY}} allows.
Do not blindly implement stale issues.

3. SELECT NEXT WORK
Choose the highest-leverage READY item, considering:
- priority and user/product impact;
- dependencies;
- whether it unblocks other work;
- regression risk;
- ability to verify completion.
Batch items only when they are tightly coupled and safer to verify together.

4. RECONSTRUCT INTENT
Before editing, understand:
- desired outcome;
- current behavior;
- acceptance criteria;
- relevant architecture and conventions;
- likely regression surface.
Inspect source files rather than guessing.
If the issue is underspecified but the intended reversible outcome can be inferred safely, proceed using the smallest reasonable assumption and record it.

5. IMPLEMENT
Make the smallest coherent change that fully satisfies the item.
Preserve established architecture and product behavior unless the issue requires changing them.
Do not add speculative abstractions, unrelated cleanup or extra features.

6. VERIFY LOCALLY
Run the strongest relevant checks available, such as:
- targeted tests;
- broader regression tests;
- type/lint/static checks;
- build;
- runtime checks;
- data/schema validation;
- accessibility/performance checks when material.
Fix failures caused by the change before moving on.

7. VERIFY THE PRODUCT
For user-facing work, inspect the actual resulting interface or flow when tools permit.
Check desktop/mobile or relevant states, interaction path, loading/error/empty states, visual regressions, accessibility and whether the intended user outcome is actually visible.
Do not treat a successful build as sufficient UI verification.

8. INDEPENDENT REVIEW
Review the completed change from scratch as a skeptical senior reviewer.
Ask:
- Does it satisfy the issue outcome, not just its wording?
- What could regress?
- Did complexity increase unnecessarily?
- Are tests meaningful rather than merely passing?
- Is any claim of completion unsupported?
Correct material defects before closing the item.

9. UPDATE CONTROL PLANE
When verified:
- update/close the issue appropriately;
- record concise implementation and verification evidence;
- update durable documentation only when behavior/contracts changed;
- create a new issue only for a genuine newly discovered defect, blocker or high-value follow-up that should not be fixed safely in the current scope.
Do not generate backlog merely to keep the loop alive.

10. REGRESSION CHECKPOINT
After a coherent batch of changes, run a wider lightweight regression pass across the affected product/repository.
Inspect recent changes together for interaction bugs, duplicated solutions, inconsistent UI/architecture and accumulating entropy.
Repair regressions caused by the batch within {{AUTHORITY}}.

11. CONTINUE FROM NEW STATE
Re-read the backlog and repository after each completed batch.
Priorities may have changed because dependencies were removed, issues became obsolete, or new evidence appeared.
Select the next highest-value actionable item rather than following an old static sequence mechanically.

12. PERIODIC GARDENING
During long sessions, occasionally remove small execution-generated entropy directly related to the work: dead code, stale temporary notes, duplicate helpers, obsolete issue text or broken tests.
Do not turn execution into an unrelated refactor campaign.

BLOCKING RULE
Do not stop the entire run because one issue is blocked.
Mark/record the blocker and continue with independent READY work.
Escalate only when:
- no meaningful READY work remains;
- a consequential irreversible decision requires human preference;
- permissions/external dependencies prevent further safe execution;
- the environment cannot verify changes sufficiently.

STOP
Stop only when {{STOP_CONDITION}} or when all remaining backlog is blocked, obsolete, low-value, outside authority or genuinely requires human input.
Do not stop merely because one task, milestone or planned batch is complete.

FINAL STATE
Report:
- completed and verified issues;
- issues closed as obsolete/duplicate/already-done;
- remaining blockers/human decisions;
- verification performed;
- regressions found/fixed;
- current repository/product state;
- whether meaningful actionable backlog remains.
```

## Expected output

A sequence of implemented, reviewed and verified backlog items with the GitHub control plane kept synchronized, continuing autonomously until no justified actionable work remains.
