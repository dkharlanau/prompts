---
id: repository-dream
version: 1.0.0
status: experimental
---

# Repository Dream

One-shot repository maintenance: reconstruct truth, audit entropy, apply only defensible fixes, verify exact revisions, and leave the repository easier for humans and agents to understand. See [AGENTS.md](../AGENTS.md), the detailed [Repository Dream guide](../REPOSITORY_DREAM.md), and [GitHub workflow rules](../GITHUB_WORKFLOW.md).

```text
GOAL
For {{PROJECT}}, perform a complete Repository Dream cycle and achieve {{GOAL}}.

CONTEXT
{{CONTEXT}}

AUTHORITY
{{AUTHORITY}}

CONSTRAINTS
{{CONSTRAINTS}}

DONE WHEN
{{DONE_WHEN}}

WORKING CONTRACT
Run AUDIT -> CLASSIFY -> SAFE EXECUTE -> VERIFY -> INTEGRATE -> VERIFY FINAL REVISION in one pass. Do not stop at a findings report when authorized safe fixes are available. Infer routine reversible details from current repository evidence. Ask only when a consequential decision cannot be resolved safely from evidence or existing repository policy.
Do not assume a local checkout, shell, git, gh or other CLI exists. Prefer the connected GitHub/tooling surface actually available in the session. Do not waste rounds retrying unavailable tooling. Never force-push, bypass protection, expose secrets, spend money, publish a release or trigger production changes beyond the granted authority.
If the user explicitly says AUDIT/read-only/no writes, stop after evidence-backed findings and proposed changes. Otherwise this command authorizes ordinary repository-maintenance edits and normal verified integration when repository policy and available permissions allow it; deployment/release authority remains separate.

ESTABLISH TRUTH
Resolve the exact repository, default branch, current HEAD and applicable branch/ruleset policy. Explicitly read the target repository's AGENTS.md or equivalent, scoped instructions, README, CONTRIBUTING, REPO_MAP/architecture map, roadmap/status sources and relevant build/package/CI/deployment configuration. Maps route work; current source/config/workflows settle facts.
Identify canonical sources, generated/mirrored outputs, runtime code, tests/fixtures, schemas/datasets, research/provenance, workflows, public assets, migration/deprecated areas and repository-memory surfaces. Determine which files may define current priorities. Prefer one current roadmap/backlog authority rather than parallel "next steps" systems.

AUDIT ENTROPY
Search for proven local/generated residue, temporary exports, stale build artifacts, workstation-specific absolute paths, abandoned one-off outputs, obsolete compatibility files, disconnected docs, duplicated sources of truth, generated files edited as if canonical, stale examples and repository-memory contradictions.
Audit navigation: a new agent should quickly answer what owns a surface, what is generated, what to edit, what test verifies it, what not to touch and where current work lives. Prefer task -> canonical source -> coupled surfaces -> focused verification.
Audit validation and workflow orchestration. Look for giant shell chains, deterministic command lists duplicated across package scripts and CI, checks that can drift silently, overlapping workflow stages and hidden ordering dependencies. Do not consolidate workflows merely because there are many; compare triggers, permissions, environments, secrets, path filters, concurrency, artifacts, external installs and publication behavior first.

CLASSIFY BEFORE CHANGING
Classify meaningful candidates as SAFE_DELETE, SAFE_CONSOLIDATE, SAFE_REWRITE, KEEP, HISTORICAL or UNKNOWN. UNKNOWN means KEEP.
A deletion needs positive evidence: no active runtime/build/CI/package/public/migration/test dependency, no useful provenance lost, a canonical replacement when relevant, and post-change verification able to prove equivalent or better behavior. Absence of a text reference is not sufficient because convention, glob, generated and public-route dependencies may be indirect.
Treat tests, fixtures, schemas, benchmarks/results, migrations, evidence receipts, canonical datasets, research, generated public mirrors, skills, compatibility/protocol layers and deployment examples as protected by default. Never remove validation merely to reduce file count or make CI green.
Historical material may be kept but clearly labelled so it cannot override current authority.

SAFE EXECUTE
Apply low-risk memory/cleanup fixes first: remove only proven residue, update ignore rules, repair navigation, correct stale product/license/priority claims, mark historical docs, and add a small drift guard when it materially prevents recurrence.
Keep higher-risk validation/pipeline consolidation separate. Preserve exact coverage before changing orchestration. When replacing a deterministic command chain, inventory commands and order, introduce an inspectable canonical contract, add a self-test/fingerprint or equivalent drift protection, then prove the old-equivalent coverage still runs. Keep live/network/security/environment-specific boundaries explicit rather than hiding them inside a generic runner.
Do not mix repository maintenance with unrelated product features. Do not create a second roadmap, large cleanup framework, file taxonomy bureaucracy or dashboard that merely describes the repository.

GITHUB DELIVERY
For structural maintenance, prefer an isolated branch/PR unless target instructions prove a simpler publication route is safer. Base work on the exact audited HEAD. Keep changes coherent and inspect the complete diff before publication. Re-read mutable targets before writes; serialize shared writes. If HEAD moves, reconcile instead of overwriting concurrent work.
Before merge/integration, verify the exact PR/candidate head, relevant checks and mergeability. Never treat green CI for another SHA as evidence. Fix real failures rather than bypassing or deleting checks.
After integration, resolve the exact final default-branch SHA and verify push/default-branch checks again. If generated/public surfaces changed, verify deployment/publication separately; repository CI alone does not prove deployed parity.
Inspect branch protection/rulesets when possible. If important protection is missing but repository administration is unavailable, record a concrete issue with desired settings and objective closure criteria rather than simulating protection with documentation.

REPOSITORY MEMORY
Keep entry/navigation concise. Prefer README for product/human entry, AGENTS for working rules/router, REPO_MAP or an existing equivalent for task routing, and roadmap + live issues for current work. Update the existing map rather than creating a competing one. A lightweight deterministic memory check may validate required paths, repository-relative links, ignored local outputs and workstation-path leakage; it should stay smaller than the problem it prevents.

VERIFY AND STOP
Re-run the strongest applicable baseline and focused checks. Distinguish pre-existing failures from regressions. Compare generated route/artifact/schema/localization counts when structural work could affect them. Verify behavior, not only syntax or diff shape.
Stop when every actionable finding is fixed and verified, intentionally kept with evidence, left UNKNOWN because evidence is insufficient, or blocked by external/admin access and recorded with an exact next step. Do not keep deleting merely to produce more changes.

FINAL REPORT
Report previous and final default-branch SHA, PR/commit links, what was removed/consolidated/rewritten, important items intentionally kept, tests/schemas/fixtures/runtime/publication behavior affected or not affected, exact verification on PR/candidate and final SHA, deployment verification if applicable, and only real remaining debt. Distinguish changed, verified, integrated, deployed and measured impact.
```