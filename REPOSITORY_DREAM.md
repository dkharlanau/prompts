# Repository Dream

Repository Dream is a conditional repository-maintenance adapter for [Deep Run](loops/deep-run.md). It is not a fifth canonical workflow or renderer command. Load it when the task is repository consolidation, safe cleanup, dead-file review, pipeline simplification, repository-map refresh, or reducing the context an agent must load to work safely.

Use it with the existing Deep Run execution route. `AUDIT` means read/analyse only inside the run; `EXECUTE` means apply only changes that pass the safety gates below.

Example requests:

```text
Prompts Deep Run EXECUTE на <project>. Repository Dream, mode AUDIT: проверь структуру, лишние файлы, pipeline entropy и навигацию для агентов. Ничего не удаляй.
```

```text
Prompts Deep Run EXECUTE на <project>. Repository Dream, mode EXECUTE: безопасно консолидируй репозиторий, обнови карту и удали только доказанно ненужное. Ничего не ломай.
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

This is not a "delete as many files as possible" task. Optimize for comprehension cost, maintenance cost, agent navigation speed, architectural coherence, safety, reproducibility and regression resistance. A larger repository with a clear structure is preferable to a smaller repository that lost useful tests, provenance or operational knowledge.

## Operating cycle

Use:

`OBSERVE -> MAP -> CLASSIFY -> CONSOLIDATE -> PRUNE -> REINDEX -> VERIFY`

Do not begin with deletion.

## 1. Establish repository truth

Work against the actual current repository and default-branch HEAD. Do not rely on remembered architecture, old reports, stale maps, previous agent conclusions or commit messages alone.

Before changing anything:

- resolve exact repository, default branch and HEAD;
- explicitly read applicable `AGENTS.md`, `README.md`, `CONTRIBUTING.md` and linked task map;
- inspect package/build configuration, CI/workflows and deployment configuration relevant to the task;
- inspect repository-specific instructions and scoped guidance;
- determine canonical versus generated sources.

Do not assume a local checkout or CLI exists. Prefer the connected GitHub toolchain and adapt execution to the capabilities actually available in the current session. Do not waste rounds retrying unavailable CLI tooling.

Maps are navigation, not proof. Current source/config/workflows settle discoverable facts.

## 2. Build a repository inventory

Reconstruct the actual repository topology. Identify at minimum:

- canonical source directories;
- generated directories;
- runtime/application code;
- build/generator/post-processing code;
- validation/check code;
- tests and fixtures;
- schemas and datasets;
- documentation and research/provenance material;
- deployment/workflow/configuration files;
- AI/agent instructions;
- public assets and integrations;
- deprecated, archived or migration-only areas.

Look for unusually large files/directories, duplicate or near-duplicate scripts, stale reports, abandoned experiments, obsolete generated artifacts committed to Git, one-off migration/repair scripts, disconnected documentation, checks for removed features, scripts that are never invoked, repeated pipeline stages, overlapping transformations and stale agent instructions.

File age alone is not evidence of obsolescence.

## 3. Reconstruct dependencies before judging files

For every cleanup candidate, inspect whether it is referenced by imports, dynamic imports, package scripts, build scripts, CI, deployment, tests, schemas, generators, documentation, integrations, runtime configuration, public URLs, generated artifacts, localization/Search pipelines or agent workflows.

Consider indirect and convention-based dependencies: glob loading, filesystem discovery, dynamic path construction, GitHub Actions references and generated-data consumers. A file is not dead merely because ordinary text search finds no import.

## 4. Classify before changing

Place candidates into one of these classes:

- `KEEP` — actively needed or provides useful safety/context;
- `CONSOLIDATE` — useful behavior exists but ownership or implementation is unnecessarily fragmented;
- `SAFE_DELETE_CANDIDATE` — strong evidence says the artifact is no longer required;
- `ARCHIVE_CANDIDATE` — operationally unnecessary but historically/evidentially useful;
- `UNKNOWN` — evidence is insufficient.

`UNKNOWN` means KEEP.

## 5. Protect tests and evidence

Tests, checks, fixtures, schemas and validation code are safety infrastructure. Never delete them merely because they are large, old, similar to another test or absent from the default context.

A test/check becomes a deletion candidate only when the protected behavior itself is proven removed or superseded and equivalent protection exists elsewhere. Prefer reorganizing or documenting useful coverage over deleting it.

Apply an especially high deletion threshold to schemas, migrations, lock files, CI/deploy/security files, licences, citation/provenance records, canonical datasets, public compatibility contracts, localization source-of-truth data and reproducibility material.

Do not rewrite Git history as part of Repository Dream. History compaction is a separate destructive operation requiring explicit authorization. Deleting a file from current HEAD does not remove it from historical repository size.

## 6. Safe deletion gate

In EXECUTE mode, delete only with positive evidence. Require all applicable conditions:

1. no active dependency requires the artifact;
2. no build, CI or deployment path requires it;
3. no public interface depends on it;
4. no useful validation coverage is lost;
5. it is reproducible, obsolete, superseded or genuinely unreachable;
6. baseline behavior is known;
7. post-change verification can demonstrate equivalent or better behavior.

If an applicable condition cannot be established, keep the artifact. Do not delete to improve file-count metrics.

## 7. Detect architectural entropy

Do not limit the pass to dead files. Look for complexity created by repeated incremental fixes, especially:

- the same postprocessor running several times;
- generators that repair output from earlier generators;
- `finalize`, `repair`, `ensure` and `reconcile` layers stacking indefinitely;
- long serial build commands;
- overlapping checks;
- scripts whose order is critical but undocumented;
- one new script for every isolated fix;
- repeated output mutation long after canonical generation;
- duplicated sources of truth.

Before removing a repeated stage, determine why it repeats. It may compensate for later-generated output. Preserve behavior first; simplify phase ordering only after proving equivalence.

Prefer a comprehensible flow such as:

`canonical source -> generation -> bounded post-processing -> final reconciliation -> validation`

Do not merge files merely to lower file count. One giant coupled file is not an improvement. Optimize conceptual boundaries.

## 8. Refresh repository memory

The repository should route a new agent from "I have a task" to "these are the few sources/checks I need" quickly.

Prefer a small navigation hierarchy when it fits the target:

- `README.md` — product/human entry point;
- `AGENTS.md` — compact agent rules and task router;
- `REPO_MAP.md` or existing equivalent — current architecture/navigation map;
- domain documentation — loaded only when relevant.

Do not create `REPO_MAP.md` when an equivalent canonical map already exists; improve that source instead. Avoid documentation duplication.

A compact repository map should cover product boundary, canonical sources, meaningful directory map, task router, build phases, generated surfaces, validation, deployment, danger zones and intentional legacy/deprecated boundaries. It should not dump every file.

Optimize for selective context loading: source of truth quickly identifiable, generated output avoided, whole-corpus reads unnecessary, checks selected by task and dangerous cross-cutting surfaces visible.

Where justified, add a lightweight deterministic staleness check for map paths/commands. Do not build a maintenance framework heavier than the problem. Prefer structural validation over timestamp-only or commit-SHA-only churn.

## 9. Baseline and change strategy

Before risky structural work, establish the strongest available baseline using the target repository's own verification contract: build, tests, checks, lint, schemas, artifact generation, sitemap/localization validation or other applicable gates.

Record what already fails. Do not attribute pre-existing failures to cleanup.

Keep changes reviewable and conceptually separated when risk warrants it:

1. navigation/memory refresh;
2. proven-safe dead-file cleanup;
3. structural consolidation;
4. staleness/validation protection.

Do not mix unrelated product features into Repository Dream. Never weaken validation merely to make cleanup pass.

Use [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md) for publication, concurrency, exact-SHA verification and resume rules. Respect explicit no-push/no-merge/no-deploy boundaries separately.

## 10. Verify behavioral equivalence

After changes, rerun the relevant baseline. For generated/public projects compare where applicable:

- generated page/artifact counts;
- public route set;
- sitemap entries;
- schemas and release data;
- localization coverage;
- important metadata;
- build output and deployment configuration.

A successful cleanup should reduce internal complexity without unintentionally changing product behavior. Any intended behavior change must be called out explicitly.

## 11. Output

Finish with an evidence-based report covering:

- repository health and dominant structural risks;
- navigation quality and context-loading improvements;
- important files intentionally kept despite appearing removable;
- deleted items and evidence for each deletion;
- consolidated implementation/pipeline areas;
- repository-memory changes;
- exact verification performed and exact revision verified;
- useful before/after measures where available: tracked files, relevant script count, duplicated pipeline stages, working-tree size, agent entry-point complexity or build/check complexity;
- remaining uncertainty deliberately kept because evidence was insufficient.

Do not optimize these metrics blindly. Distinguish changed, verified, integrated, deployed and measured impact.

## Success criteria

Repository Dream succeeds when a new agent can understand the project faster; canonical sources are easier to locate; irrelevant context loading decreases; duplicated or obsolete machinery decreases; valuable tests and evidence remain; generated artifacts are not mistaken for source; repository instructions match current reality; build/deploy behavior is preserved; every deletion is defensible; and future structural drift is easier to detect.

Safety and comprehension have priority over file-count reduction.
