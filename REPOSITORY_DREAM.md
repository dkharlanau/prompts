# Repository Dream

Repository Dream is the detailed maintenance guide behind the canonical [Repository Dream workflow](loops/repository-dream.md) and the user command `Prompts Repository Dream на <project>`.

The command is intentionally one-shot by default: **audit first, then apply only defensible repository-maintenance fixes, verify exact revisions, integrate through the repository's normal GitHub path, and verify the final default-branch revision**. An explicit `AUDIT`, `read-only`, `ничего не менять` or equivalent restriction turns the same workflow into analysis-only mode.

Examples:

```text
Prompts Repository Dream на <project>.
```

```text
Prompts Repository Dream на <project>. Проверь структуру, лишние файлы, validation/pipeline entropy и навигацию для агентов; исправь всё безопасное за один проход.
```

```text
Prompts Repository Dream на <project>. AUDIT only — ничего не меняй.
```

## Goal

Treat the repository as a long-lived software and knowledge system that periodically needs to:

- remove proven dead weight;
- consolidate duplicated or obsolete implementation;
- preserve valuable tests, evidence, history and operational safeguards;
- refresh navigation for humans and AI agents;
- reduce context required to understand and modify the project;
- detect structural entropy before it becomes permanent;
- leave the repository easier to reason about than before.

This is not a "delete as many files as possible" task. Optimize for comprehension cost, maintenance cost, agent navigation speed, architectural coherence, safety, reproducibility and regression resistance. A larger repository with clear ownership is preferable to a smaller repository that lost useful tests, provenance or operational knowledge.

## Operating cycle

Use:

`DISCOVER -> AUDIT -> CLASSIFY -> SAFE EXECUTE -> VERIFY -> INTEGRATE -> VERIFY FINAL REVISION`

Do not begin with deletion and do not stop at a findings report when safe authorized fixes are available.

## 1. Establish repository truth

Work against the actual current repository and default-branch HEAD. Do not rely on remembered architecture, old reports, stale maps, previous agent conclusions or commit messages alone.

Before changing anything:

- resolve exact repository, default branch and HEAD;
- explicitly read applicable `AGENTS.md`, `README.md`, `CONTRIBUTING.md` and linked task map;
- inspect package/build configuration, CI/workflows and deployment configuration relevant to the task;
- inspect repository-specific instructions and scoped guidance;
- determine canonical versus generated sources;
- inspect branch protection/rulesets when the available GitHub surface can read them.

Do not assume a local checkout or CLI exists. Prefer the connected GitHub toolchain and adapt execution to the capabilities actually available in the current session. Do not waste rounds retrying unavailable CLI tooling.

Maps are navigation, not proof. Current source/config/workflows settle discoverable facts.

## 2. Build a repository inventory

Reconstruct the actual repository topology. Identify at minimum:

- canonical source directories;
- generated/mirrored directories;
- runtime/application code;
- build/generator/post-processing code;
- validation/check code;
- tests and fixtures;
- schemas and datasets;
- documentation and research/provenance material;
- deployment/workflow/configuration files;
- AI/agent instructions;
- public assets and integrations;
- deprecated, archived or migration-only areas;
- repository-memory surfaces: README, AGENTS, REPO_MAP, roadmap, status/checkpoint docs and live issues.

Determine which sources may define current priorities. Avoid parallel roadmap systems where README, status docs and historical milestone docs all claim to be "next work".

Look for unusually large or duplicated scripts, stale reports, abandoned experiments, obsolete generated artifacts committed to Git, one-off migration/repair scripts, disconnected documentation, checks for removed features, repeated pipeline stages, overlapping transformations and stale agent instructions.

File age alone is not evidence of obsolescence.

## 3. Reconstruct dependencies before judging files

For every cleanup candidate, inspect whether it is referenced by imports, dynamic imports, package scripts, build scripts, CI, deployment, tests, schemas, generators, documentation, integrations, runtime configuration, public URLs, generated artifacts, localization/Search pipelines or agent workflows.

Consider indirect and convention-based dependencies: glob loading, filesystem discovery, dynamic path construction, GitHub Actions references and generated-data consumers. A file is not dead merely because ordinary text search finds no import.

## 4. Classify before changing

Place meaningful candidates into one of these classes:

- `SAFE_DELETE` — positive evidence proves the artifact is no longer required;
- `SAFE_CONSOLIDATE` — useful behavior remains but ownership/implementation is unnecessarily fragmented;
- `SAFE_REWRITE` — navigation/docs/metadata can be corrected without changing product semantics;
- `KEEP` — actively needed or useful safety/context;
- `HISTORICAL` — useful provenance that must no longer appear to define current priorities;
- `UNKNOWN` — evidence is insufficient.

`UNKNOWN` means KEEP.

## 5. Protect tests and evidence

Tests, checks, fixtures, schemas and validation code are safety infrastructure. Never delete them merely because they are large, old, similar to another test or absent from the default context.

A test/check becomes a deletion candidate only when the protected behavior itself is proven removed or exactly superseded and equivalent protection exists elsewhere. Prefer reorganizing or documenting useful coverage over deleting it.

Apply an especially high deletion threshold to schemas, migrations, lock files, CI/deploy/security files, licences, citation/provenance records, canonical datasets, public compatibility contracts, localization source-of-truth data, research, benchmark evidence and reproducibility material.

Do not rewrite Git history as part of Repository Dream. History compaction is a separate destructive operation requiring explicit authorization. Deleting a file from current HEAD does not remove it from historical repository size.

## 6. Safe deletion gate

Delete only with positive evidence. Require all applicable conditions:

1. no active dependency requires the artifact;
2. no build, CI or deployment path requires it;
3. no package/export/public interface depends on it;
4. no migration or compatibility contract depends on it;
5. no useful validation, provenance or historical evidence is lost;
6. it is reproducible, obsolete, superseded or genuinely unreachable;
7. baseline behavior is known;
8. post-change verification can demonstrate equivalent or better behavior.

If an applicable condition cannot be established, keep the artifact. Do not delete to improve file-count metrics.

## 7. Detect architectural and validation entropy

Do not limit the pass to dead files. Look for complexity created by repeated incremental fixes, especially:

- the same postprocessor running several times;
- generators that repair output from earlier generators;
- `finalize`, `repair`, `ensure` and `reconcile` layers stacking indefinitely;
- giant serial validation commands;
- deterministic command lists duplicated between package scripts and CI;
- overlapping checks whose ownership is unclear;
- scripts whose order is critical but undocumented;
- one new script for every isolated fix;
- repeated output mutation long after canonical generation;
- duplicated sources of truth.

Before removing a repeated stage, determine why it repeats. It may compensate for later-generated output. Preserve behavior first; simplify phase ordering only after proving equivalence.

When consolidating validation, inventory the old command set and order first. Prefer an inspectable canonical validation contract plus a lightweight self-test/fingerprint or equivalent drift guard. Keep live/network/security/environment-specific boundaries explicit in CI: external SDK installation, credentials, live-site dogfood, deployment checks, reusable Actions and release/publication gates should not disappear into a generic runner merely to make YAML shorter.

Do not merge workflows merely because there are many. Compare triggers, path filters, permissions, secrets, environments, concurrency, artifacts and publication side effects before claiming equivalence.

## 8. Refresh repository memory

The repository should route a new agent from "I have a task" to "these are the few sources/checks I need" quickly.

Prefer a small hierarchy when it fits the target:

- `README.md` — product/human entry point;
- `AGENTS.md` — compact agent rules and task router;
- `REPO_MAP.md` or existing equivalent — current architecture/navigation map;
- roadmap + live issues — current priorities;
- domain documentation — loaded only when relevant;
- historical milestone docs — provenance, clearly marked historical.

Do not create `REPO_MAP.md` when an equivalent canonical map already exists; improve that source instead. Avoid documentation duplication.

A compact map should use task-oriented routing such as:

`task -> canonical source -> coupled surface -> focused verification`

Where justified, add a lightweight deterministic memory check for required paths, repository-relative links, ignored local-output paths and workstation-specific absolute paths. Do not build a maintenance framework heavier than the problem.

## 9. Change strategy

Before risky structural work, establish the strongest available baseline using the target repository's own verification contract. Record what already fails. Do not attribute pre-existing failures to cleanup.

Separate risk when useful:

1. navigation/memory refresh and proven residue cleanup;
2. validation/pipeline consolidation;
3. workflow consolidation only when strong evidence supports it.

Do not mix unrelated product features into Repository Dream. Never weaken validation merely to make cleanup pass.

For structural maintenance prefer branch/PR-first delivery unless repository instructions prove a simpler route is safer. Use [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md) for concurrency, publication, exact-SHA verification and resume rules. Respect explicit no-push/no-merge/no-deploy boundaries separately.

## 10. Verify exact revisions

After changes, rerun the relevant baseline and focused checks. For generated/public projects compare where applicable:

- generated page/artifact counts;
- public route set;
- sitemap entries;
- schemas and release data;
- localization coverage;
- important metadata;
- build output and deployment configuration.

Before integration, verify the exact PR/candidate head SHA. After integration, resolve the exact final default-branch SHA and verify push/default-branch checks again. Green CI on another SHA is not evidence.

If public/generated surfaces changed, verify deployment/publication separately. A green repository build does not prove live parity.

If `main` protection is materially missing and the session cannot change repository administration, create a concrete issue with desired settings and objective closure criteria. Do not simulate branch protection with docs or CI conventions.

## 11. Stop conditions and output

Stop when every actionable finding is one of:

1. fixed and independently verified;
2. intentionally preserved with evidence;
3. classified UNKNOWN and therefore left untouched;
4. blocked by external/admin access and recorded with a concrete next verification step.

Do not continue deleting merely to produce more changes.

Finish with an evidence-based closure report covering:

- previous and final default-branch SHA;
- PR/commit links;
- repository health and dominant structural risks;
- navigation/context-loading improvements;
- important files intentionally kept despite appearing removable;
- deleted items and evidence for each deletion;
- consolidated validation/pipeline areas;
- repository-memory changes;
- exact PR/candidate and final-revision verification;
- tests/schemas/fixtures/runtime/publication behavior affected or explicitly unchanged;
- deployment/public verification where applicable;
- remaining real debt only.

Distinguish changed, verified, integrated, deployed and measured impact.

## Success criteria

Repository Dream succeeds when a new agent can understand the project faster; canonical sources are easier to locate; irrelevant context loading decreases; duplicated or obsolete machinery decreases; useful history/evidence remains; generated artifacts are not mistaken for source; repository instructions match current reality; validation ownership is clearer; build/deploy behavior is preserved; every deletion is defensible; exact final revision checks are green; and future structural drift is harder to reintroduce.

Safety and comprehension have priority over file-count reduction.
