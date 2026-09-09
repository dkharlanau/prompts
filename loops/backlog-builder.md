---
id: backlog-builder
version: 1.0.0
status: candidate
category: planning-control-plane
purpose: turn real project state into a small, prioritized, executable GitHub backlog
best_for: products and repositories where research, ideas, defects and improvements must be converted into reliable work
avoid_when: the backlog is already current, well-prioritized and execution-ready
benchmark_target: DRS-100 >= 85 plus backlog-specific quality checks
model_strategy: see MODEL_PROFILES.md
---

# Backlog Builder

## Inputs

- `{{PROJECT}}`
- `{{GOAL}}`
- `{{CONTEXT}}`
- `{{CONSTRAINTS}}`
- `{{AUTHORITY}}`
- `{{BACKLOG_SYSTEM}}`
- `{{SUCCESS_SIGNALS}}`

## Template

```text
GOAL
Build and maintain an execution-ready backlog for {{PROJECT}} that maximizes progress toward {{GOAL}}.

CONTEXT
{{CONTEXT}}

CONSTRAINTS
{{CONSTRAINTS}}

AUTHORITY
{{AUTHORITY}}

BACKLOG SYSTEM
{{BACKLOG_SYSTEM}}

SUCCESS SIGNALS
{{SUCCESS_SIGNALS}}

OPERATING PRINCIPLE
The backlog is a decision system, not an idea dump.
Fewer strong, evidence-backed tasks are better than many weak tasks.
Do not preserve an issue merely because it already exists.

LOOP

1. INSPECT REALITY
Inspect the actual repository/product, current backlog, recent changes, documentation, analytics, failures, user experience and other available sources of truth.
Do not rely on issue titles or stale documentation when the real state differs.

2. CLEAN THE EXISTING BACKLOG
Review open items and classify them as:
- READY — still valuable and executable;
- NEEDS REWRITE — valuable but vague/stale;
- DUPLICATE — overlaps another item;
- BLOCKED — depends on unavailable evidence/action;
- OBSOLETE — no longer useful;
- DONE — already satisfied by the current state.
Merge, rewrite, close or reclassify where {{AUTHORITY}} allows.

3. FIND GAPS
Identify the few highest-leverage gaps preventing {{GOAL}}.
Use only perspectives that can materially change prioritization, such as product, user, UX, growth, engineering, architecture, quality, security, data, operations or skeptic.
Distinguish FACT, OBSERVATION, INFERENCE, HYPOTHESIS and UNKNOWN.
Do not create backlog work for speculative ideas that lack a plausible path to value.

4. GENERATE CANDIDATES
Create candidate work only for meaningful gaps.
A candidate may be:
- implementation;
- bug/regression fix;
- experiment;
- research needed to unblock a decision;
- simplification/deletion;
- test/observability improvement;
- documentation only when it changes execution quality.

5. CHALLENGE CANDIDATES
For each important candidate ask:
- What outcome does it change?
- What evidence supports it?
- What happens if we do nothing?
- Is there a smaller or cheaper action?
- Is it already covered elsewhere?
- Can an execution agent verify completion objectively?
Reject weak candidates.

6. PRIORITIZE
Rank surviving work by expected outcome impact, confidence, urgency/dependency, risk reduction and implementation cost.
Prefer work that unblocks multiple downstream items or produces decision-changing evidence.
Do not let easy low-value work outrank harder high-leverage work merely because it is convenient.

7. DESIGN EXECUTABLE ISSUES
Every READY issue must contain enough information for an autonomous coding/product agent to act without reconstructing the entire conversation.
Include, as applicable:
- outcome / problem;
- why it matters;
- relevant context and evidence;
- scope and non-goals;
- dependencies;
- constraints;
- acceptance criteria;
- verification method;
- UI/user-flow expectations when relevant;
- regression risks;
- links to source artifacts.
Avoid prescribing implementation details unless the constraint is real.

8. SHAPE THE QUEUE
Make dependencies and sequencing explicit.
Keep a clear small set of highest-priority READY items.
Do not flood the executor with hundreds of undifferentiated issues.
Group or create parent/child structure only when it improves execution.

9. ADVERSARIAL REVIEW
Review the resulting backlog as:
- executor who must implement it;
- product owner protecting outcome;
- skeptic trying to delete unnecessary work.
Fix ambiguity, duplicates, missing verification and priority inversions.

10. RE-INSPECT
Compare backlog against the current product again.
If important work has no issue, add it.
If an issue no longer represents the current state, fix or close it.
Repeat until the highest-value work is represented cleanly.

STOP
Stop when:
- the top backlog is execution-ready;
- major known gaps toward {{GOAL}} are represented or explicitly rejected/blocked;
- duplicates/stale work are resolved;
- another pass is mostly generating lower-value ideas rather than improving execution quality.

Do not implement the backlog unless explicitly authorized to combine planning and execution.
```

## Expected output

A cleaned, prioritized GitHub backlog that an autonomous executor can consume directly, plus a concise summary of what was added, rewritten, merged, closed, blocked and ranked highest.
