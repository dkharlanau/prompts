---
id: deep-run
version: 1.1.0
status: candidate
category: universal
pattern: inspect + council + tournament + adversarial review + experiment gate + backlog-or-execute + evaluator-optimizer + reflection
best_for: deep autonomous analysis that either turns findings into a high-quality backlog or immediately improves the real project
avoid_when: a small deterministic edit, simple factual question, or an irreversible action that still requires explicit approval
benchmark_target: DRS-100 >= 85 across at least 3 materially different domains
model_guidance: ../MODEL_PROFILES.md
research_basis: [anthropic-effective-agents, openai-model-guidance, openai-harness-engineering, openai-evals, self-refine, reflexion]
---

# Deep Run

One canonical prompt for substantial project work with two output modes:

- **BACKLOG** — think deeply, inspect the real project, challenge assumptions, then create/clean/prioritize an execution-ready backlog. Do not implement product changes unless explicitly authorized beyond backlog work.
- **EXECUTE** — think deeply, choose the highest-leverage action, implement it in the real project, verify it, learn, and continue while marginal value remains high.

The reasoning core is intentionally shared. Backlog work should not use a shallower analysis than direct implementation.

## Use when

Use this prompt when the goal is consequential enough to justify a full autonomous pass: improving a product, finding the next milestone, increasing acquisition or activation, redesigning an experience, resolving a difficult technical problem, reviewing architecture, improving a repository, validating a strategy, turning research into execution-ready work, or turning research directly into verified changes.

Do not use it for a tiny deterministic edit or a question that can be answered reliably in one step.

## Modes

Set `{{MODE}}` to exactly one of:

- `BACKLOG` — the main artifact is the backlog/control plane.
- `EXECUTE` — the main artifact is a changed and verified project state.

If mode is omitted, infer it from the user's request. If still ambiguous, default to `EXECUTE` for ordinary "deep run / improve the project" requests and `BACKLOG` for "fill/review/prioritize the backlog" requests.

## Inputs

- `{{MODE}}` — `BACKLOG` or `EXECUTE`.
- `{{PROJECT}}` — product, service, repository, website, workflow or system.
- `{{OUTCOME}}` — the real outcome to improve; avoid activity goals.
- `{{TARGET}}` — user, customer, system, audience or stakeholder affected by the outcome.
- `{{CONTEXT}}` — only context that materially changes decisions. Inspect sources of truth instead of duplicating discoverable context here.
- `{{CONSTRAINTS}}` — non-goals, limits, deployment restrictions, budget or compatibility constraints.
- `{{AUTHORITY}}` — what may be inspected, changed, committed, tested, published or changed in GitHub without further approval.
- `{{SUCCESS_EVIDENCE}}` — observable evidence that would demonstrate improvement.
- `{{STOP_CONDITION}}` — optional explicit stopping rule. If omitted, use the built-in marginal-value rule.

## Canonical template

```text
DEEP RUN

MODE
{{MODE}}

PROJECT
{{PROJECT}}

OUTCOME
{{OUTCOME}}

TARGET
{{TARGET}}

CONTEXT
{{CONTEXT}}

CONSTRAINTS
{{CONSTRAINTS}}

AUTHORITY
{{AUTHORITY}}

SUCCESS EVIDENCE
{{SUCCESS_EVIDENCE}}

MISSION
Deeply improve the quality of decisions and work for {{PROJECT}} toward {{OUTCOME}}.

If MODE=BACKLOG, finish with a cleaned, prioritized, execution-ready control plane that represents the highest-value justified work.
If MODE=EXECUTE, carry the strongest justified work through implementation and verification in the real project.

Do not optimize for number of ideas, files, features, pages, issues, commits, tokens saved, or visible activity. Optimize for the stated outcome.

Use substantial reasoning and available tools when they can materially improve the result. Do not stop at a shallow audit, recommendation list, or generic plan. Do not create work merely to satisfy this prompt.

OPERATING RULES

- Treat the real product, repository, data, analytics, tests, current UI, GitHub state and external evidence as stronger sources than stale documentation or intended behavior.
- Distinguish FACT, OBSERVATION, INFERENCE, HYPOTHESIS and UNKNOWN whenever the distinction could change a decision.
- Prefer evidence over confidence and outcomes over activity.
- Prefer simplification, deletion, consolidation and reuse when they achieve the outcome better than adding features.
- Preserve useful existing behavior and project constraints.
- Infer routine missing details from available context and sources of truth. Ask only when a missing answer is consequential, irreversible, or genuinely cannot be resolved from available evidence.
- If independent work can materially improve quality or speed, use parallel roles/subagents/workstreams. Do not create role-play theatre: every perspective must be capable of changing the decision.
- Re-evaluate from the changed project/backlog state after every meaningful iteration. Do not mechanically continue the original plan.
- Keep GitHub state synchronized with reality when AUTHORITY permits.

SHARED DEEP-REASONING LOOP

1. INSPECT REALITY
Inspect the current state deeply enough to understand how the system actually behaves. Depending on the task, inspect code, product/UI, documentation, open/closed issues, recent changes, tests, analytics, user journeys, datasets, search/discovery state, competitors, research and external constraints.

Create a compact evidence map:
- what is known;
- what is observed directly;
- what is inferred;
- what is uncertain;
- which unknowns could change the next action.

2. ESTABLISH A BASELINE
Define the current state against SUCCESS EVIDENCE before changing the project or backlog. Use real metrics when available. When direct metrics are unavailable, define explicit observable proxies or a rubric that can be applied consistently before and after.

3. INDEPENDENT PERSPECTIVES
Infer the smallest set of perspectives that could materially change the outcome. Examples include target user, product owner, domain expert, growth/search specialist, UX designer, architect, engineer, data analyst, operator, buyer, competitor and skeptic.

Have relevant perspectives analyze independently before synthesis. Each should state:
- strongest finding;
- decisive evidence;
- biggest risk or missed opportunity;
- preferred action;
- what evidence would change its mind.

Do not force consensus. Preserve meaningful disagreement.

4. FIND THE DOMINANT BOTTLENECK
Identify the single highest-leverage constraint currently preventing OUTCOME. Separate symptoms from causes. Explicitly compare it with plausible competing bottlenecks and explain why it dominates now.

5. GENERATE MATERIAL ALTERNATIVES
For the dominant bottleneck, generate 3–7 materially different responses when the solution space is genuinely open. Alternatives must use different mechanisms or hypotheses, not cosmetic variations.

Include, when legitimate:
- improve existing behavior;
- simplify or remove something;
- change positioning or flow;
- use existing data/capability differently;
- run an experiment;
- defer or do nothing.

Normalize candidates by mechanism, expected upside, evidence, uncertainty, cost, risk, reversibility and easiest falsification test.

6. RED TEAM THE LEADERS
Attack the strongest candidates as if they are wrong.

Run a pre-mortem: assume the chosen direction was implemented and failed. Identify the most plausible causes.

Audit decisive claims as FACT / OBSERVATION / INFERENCE / HYPOTHESIS / UNKNOWN. Look for cheaper substitutes, hidden dependencies, second-order effects, feature inflation and reasons the target user may not care.

7. DECIDE
Choose the action or work package with the strongest expected outcome relative to evidence, uncertainty, cost, risk, reversibility and strategic compounding.

Do not use fake precision. If uncertainty is decision-changing, say so.

Valid decisions include IMPLEMENT, EXPERIMENT, SIMPLIFY/DELETE, RESEARCH TO UNBLOCK, DEFER and NO CHANGE.

8. EXPERIMENT GATE
Before committing to costly work, ask whether one unresolved uncertainty could reverse the decision.

If yes and it can be tested cheaply, define the smallest falsifiable test first:
- hypothesis;
- falsification evidence;
- metric/comparison;
- decision threshold.

Run it within AUTHORITY when doing so is allowed in the chosen MODE. Do not substitute internal simulation for accessible real evidence.

If no decision-changing uncertainty remains, continue to the selected MODE.

MODE BRANCH — BACKLOG

9B. AUDIT THE EXISTING BACKLOG
Treat the backlog as a control plane, not an idea dump. Review existing open work against the real current state and classify relevant items as:
- READY — still valuable and executable;
- NEEDS REWRITE — valuable but vague/stale;
- DUPLICATE — overlaps another item;
- BLOCKED — depends on unavailable evidence/action;
- OBSOLETE — no longer useful;
- DONE — already satisfied by the current state.

Merge, rewrite, close or reclassify where AUTHORITY allows.

10B. MAP DEEP-RUN FINDINGS TO WORK
Translate only justified findings into candidate work. Candidate work may be implementation, bug/regression fix, experiment, research needed to unblock a decision, simplification/deletion, test/observability improvement, or documentation only when it changes execution quality.

For each important candidate ask:
- What outcome does it change?
- What evidence supports it?
- What happens if we do nothing?
- Is there a smaller or cheaper action?
- Is it already covered elsewhere?
- Can an execution agent verify completion objectively?

Reject weak candidates.

11B. PRIORITIZE AND SHAPE THE QUEUE
Rank surviving work by expected outcome impact, confidence, urgency/dependency, risk reduction and implementation cost.

Prefer work that removes the dominant bottleneck, unblocks multiple downstream items, produces decision-changing evidence or prevents significant regressions.

Do not let easy low-value work outrank harder high-leverage work merely because it is convenient. Do not flood the executor with hundreds of undifferentiated issues.

12B. WRITE EXECUTION-READY ISSUES
Every READY issue must contain enough information for an autonomous coding/product agent to act without reconstructing the originating conversation.

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

13B. ADVERSARIAL BACKLOG REVIEW
Review the resulting backlog from three perspectives:
- executor who must implement it;
- product owner protecting OUTCOME;
- skeptic trying to delete unnecessary work.

Fix ambiguity, duplicates, missing verification, missing dependencies and priority inversions.

14B. VERIFY THE CONTROL PLANE
Re-inspect the backlog against the real project.

Check that:
- the highest-value known work is represented;
- stale/done/duplicate work is not masquerading as future work;
- the top READY issues are genuinely executable;
- important blockers are explicit;
- issue volume did not increase merely because more ideas were generated;
- the queue still reflects the dominant bottleneck and OUTCOME.

15B. REPEAT FROM REALITY
Run another shared-analysis/backlog iteration only if it is likely to materially improve prioritization or executability. Do not keep inventing lower-value issues after the meaningful gaps are represented.

BACKLOG STOP
Stop when the highest-value backlog is execution-ready, major known gaps are represented or explicitly rejected/blocked, stale work is resolved, and another pass mostly generates lower-value ideas.

Do not implement product changes in BACKLOG mode unless the user explicitly extends AUTHORITY beyond backlog/control-plane changes.

MODE BRANCH — EXECUTE

9E. EXECUTE
Within AUTHORITY, make the smallest coherent set of changes capable of materially improving OUTCOME.

Carry work through implementation. For software/repositories, edit the real files and run appropriate checks. For products/services, improve the real user-facing artifact or operational system. For strategy/research, produce the decision artifact and update the system of record when appropriate.

Do not expand scope merely because additional work is possible. If new information invalidates the plan, revise the plan.

When useful, create/update GitHub issues for durable follow-up work discovered during execution, but do not turn EXECUTE mode into backlog-filling activity.

10E. VERIFY THE RESULT
Verify the changed state, not the intention.

Use the checks relevant to this project, such as:
- build/tests/static checks;
- real UI or workflow inspection;
- target-user journey replay;
- accessibility/performance;
- data correctness;
- search/discovery behavior;
- conversion/activation signals;
- architectural invariants;
- regression checks;
- external evidence or source validation.

Calibrate verification to the consequence of the change. Do not manufacture tests that merely mirror the implementation.

11E. INDEPENDENT EVALUATION
Evaluate the result from scratch against the same baseline and SUCCESS EVIDENCE. The evaluator must not defend the implementation because effort was spent on it.

Report:
- before;
- after;
- delta;
- strongest remaining defect;
- regressions or new complexity;
- confidence and evidence quality.

If improvement is weak or negative, diagnose whether the implementation, hypothesis, bottleneck choice or evaluation method was wrong. Correct it rather than inflating the score.

12E. ENTROPY CHECK
Inspect whether the iteration introduced avoidable complexity: duplicated concepts, stale docs, dead files, unnecessary abstractions, overlapping issues, inconsistent patterns, content cannibalization or maintenance burden.

Remove or consolidate entropy when doing so is safe and clearly improves the system.

13E. LEARN
Preserve only durable learning that should affect later runs:
- validated/rejected hypotheses;
- decisions and why they changed;
- useful measurements;
- failure modes;
- new constraints;
- reusable project rules.

Do not create documentation for ephemeral reasoning.

14E. REPEAT FROM REALITY
Re-inspect the changed state and identify the new dominant bottleneck.

Run another iteration only if its expected marginal value is meaningful. A new iteration may choose a different mechanism, perspective or hypothesis from the previous one.

EXECUTE STOP
Stop when OUTCOME is sufficiently supported by SUCCESS EVIDENCE, when another iteration has low expected marginal value, when progress requires external evidence that is not currently accessible, or when the next consequential action is outside AUTHORITY.

GLOBAL STOP
If {{STOP_CONDITION}} is supplied, respect it as an additional condition in either mode.

FINAL REPORT
Keep the final report compact relative to the work performed.

For BACKLOG mode state:
- what was added, rewritten, merged, closed or blocked;
- highest-priority READY work and why;
- important rejected assumptions/ideas;
- remaining uncertainty or blocker.

For EXECUTE mode state:
- what materially changed;
- evidence of improvement or failure;
- important decisions/rejected assumptions;
- remaining uncertainty or blocker;
- next highest-leverage action, only if one remains.
```

## Expected result

- **BACKLOG mode:** a cleaned, prioritized, execution-ready backlog grounded in deep project analysis.
- **EXECUTE mode:** a real, verified project change or decision with an evidence trail.

Both modes use the same deep reasoning core so backlog quality and direct implementation are driven by the same view of reality.