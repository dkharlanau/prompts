# Prepare a repository for ChatGPT + GitHub

A repository-side guide, not a fourth command or an instruction to reconfigure every project. Use it when preparing an authorized target for work from the ChatGPT app. The session protocol remains in [CHATGPT_DEEP_RUN.md](CHATGPT_DEEP_RUN.md); Git publication and recovery mechanics remain in [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md).

The objective is to make the next safe change easy to locate, check and resume. More agent files are not inherently better. Start with an existing entry point, a small task-to-file map and a real validation command. Add machinery only for an observed problem.

## 1. Give the app an explicit entry point

Reuse the root `AGENTS.md` or the project's existing equivalent. Keep it a short router: purpose/non-goals, important restrictions, where to read next, how to check changes, and where unfinished work lives. Do not paste the whole architecture or a transcript into it. Link it from `README.md`.

In the ChatGPT project instructions or opening request, explicitly ask the assistant to read that entry point through GitHub at the observed ref. A suggested instruction is:

> For repository work, resolve the actual repository/ref, read its root AGENTS.md (or README-linked equivalent) and the linked task map through the available GitHub tools. Read applicable scoped instructions and source before editing. Preserve the current task's authority, branch, push and deployment restrictions. Never assume these files were loaded automatically.

This is not an app configuration that a repository file can install. OpenAI documents on-demand GitHub retrieval, while automatic `AGENTS.md` discovery is documented for Codex. Do not transfer that guarantee to ordinary ChatGPT chat. The standard GitHub app's help page also describes read-only access; other exposed tools may differ. Inspect actual read/write/runtime capabilities, not filenames or model names. [Sources 1–2](#sources)

## 2. Map tasks, not every file

Use a section in the existing entry point for a tiny repository. When it becomes crowded, link one small `REPO_MAP.md` or reuse an existing architecture index. Its useful unit is:

```text
Task or user-visible behavior -> canonical source paths -> coupled files -> verification
```

For each important area, identify the source of truth, relevant schema/interface, and a focused check. Include the generator-to-output relationship where applicable. Avoid a complete file-tree dump and a second hand-maintained copy of package scripts or API definitions.

[This library's map](REPO_MAP.md) is a concrete example. It routes prompt edits to the canonical template plus catalog, renderer changes to the real script, and GitHub workflow changes to their own validation surface.

Mark generated, vendored and large output directories as **not first reads**, not universally irrelevant. An agent may still need them to diagnose a build or distribution defect. Maps route attention; current source and applicable instructions settle what is true. Maintain changed paths/commands in the same commit as the change. Existing link validation can detect a missing path, but it cannot establish semantic freshness.

Do not embed an always-changing HEAD in permanent navigation files. The session records the observed SHA. If a generated index is justified, include source hashes or a manifest digest, exclude its own output from that digest, and validate freshness before trusting it.

### Website repositories

Use [WEBSITE_STACKS.md](WEBSITE_STACKS.md) to distinguish the framework, rendering mode and host. During authorized setup, add only missing decision-relevant facts to the existing map: affected workspace, version source, router/generator, static export or runtime, production URL prefix, source-to-output flow, real checks and publication triggers. Link configuration/scripts as the source of truth rather than copying their changing values into a second manifest.

For static sites, map a representative content/data edit through its generator to a nested public route. For Next.js, also identify the relevant router, client/server boundary and export/runtime constraints. Select a real affected route and existing verification command; do not invent a fixture suite or add Next.js tooling to a plain HTML site.

Check that a fresh reader can locate the source and distinguish a build check from a deployment. Keep production and preview restrictions explicit. Normal feature work consumes this contract; it does not rerun setup or copy every profile into the target.

## 3. Make changes local and sources unambiguous

Prefer readable UTF-8 source, descriptive paths, stable record IDs and deterministic formatting. Keep related behavior in coherent modules. Avoid frequently replacing one enormous minified file or a huge single-line JSON document through a connector. Split by actual domain/schema boundaries when a measured editing problem justifies it, not by arbitrary line limits.

For data-driven sites, document the path **canonical data -> validation/schema -> generator/template -> generated pages**. Change data or templates rather than hand-editing thousands of generated pages. Preserve public URLs, IDs, references and ordering contracts; a structural split is a migration, not harmless agent housekeeping.

Keep lockfiles when the project uses them. Document the supported runtime, dependency install command, working directory and environment variable names with safe placeholders. Keep real secrets and private customer data out of repository instructions, examples, logs and checkpoints.

For binary-heavy projects, a small text index of asset purpose/path/provenance can help discovery; it does not prove that ChatGPT inspected the image, PDF or artifact. Git LFS pointers likewise do not guarantee that the connected tool can fetch the underlying bytes.

Treat truncated reads as incomplete. GitHub's contents API limits directory listings to 1,000 entries; recursive trees have their own truncation limits. Use appropriate tree/subtree reads and inspect truncation flags rather than conclude that the rest of the repository does not exist. Tool-specific response limits may be smaller. [Sources 3–4](#sources)

## 4. Expose a real verification contract

Document existing commands first. For each command, state its working directory, runtime/dependencies, what it checks, side effects and what it does **not** prove. Separate fast validation, broader integration/build checks and deployment. Do not invent `npm test`, `make check` or a shell capability because they would be convenient.

A useful check is deterministic where possible, needs no production secrets for routine validation, returns nonzero on failure, and reports a concise path/rule/expected/actual/reproduction. Keep full diagnostics available for investigation. Use minimal synthetic fixtures in the target project when tests need them; do not move target-project fixtures into this prompt library.

For this repository the real command is `python3 scripts/prompts.py check`, run from the repository root with Python 3.10+ and no third-party packages. It validates template structure, version/catalog agreement, local link existence and rendering. It does not evaluate model performance or the user's websites.

If no local runtime is available, use appropriate existing CI after an authorized publication, or an already-supported isolated verification path. Do not treat main as an experimental execution queue for risky untested code. An unreferenced Git commit is not automatically a CI runner.

## 5. Make CI results readable from repository tools

Prefer one clear validation entry point, with workflow/job names that remain stable. Record workflow, event, run ID, checked revision, command, result and gaps. Print concise diagnostics to stdout as well as any UI summary: a connector may expose logs/checks but not the rendered job-summary page. GitHub supports Markdown job summaries via `GITHUB_STEP_SUMMARY`. [Source 5](#sources)

For a pull request, default checkout may test a synthetic merge commit rather than the PR head. Report the actual checked-out revision and its relationship to the head/base; do not label it a test of a different SHA. For direct main writes, match the push run to the published SHA. [Source 6](#sources)

If there is no CI and repository setup is authorized, a small validation-only workflow can close that evidence gap. Prefer the existing project check, one justified runtime and no deploy. This library's [prompt-only workflow](.github/workflows/prompts-check.yml) is an example, not a universal workflow to copy unchanged.

Keep validation separate from release, migrations and preview publication. Document whether pushes, PRs, tags, issues or comments can trigger external providers as well as Actions. Absence of a deploy YAML is not proof that no external deployment is configured. Under `no deploy`, unresolved publication effects block the relevant remote write.

Use least-privilege permissions, immutable action pins and no stored checkout credentials when unnecessary. Do not build an arbitrary shell-command dispatcher from issue text, expose secrets to untrusted PR code, or use `pull_request_target` to execute such code. Do not weaken required checks or repository protection. [Source 7](#sources)

Keep CI enabled; cancel only superseded validation, not deployment or migration. Avoid duplicate push/PR checks, blanket skip tokens and unnecessary matrices. A manual workflow is useful only if a human or an actually exposed tool can dispatch it. Never promise dispatch from a connector that only lists runs. Detailed tuning stays in [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md).

Do not commit a fresh CI report after every run: that can create noise or a trigger loop. Prefer stdout/check results and, only when needed and retrievable, short-lived artifacts. No workflow is required merely to make a repository look agent-ready.

## 6. Separate durable knowledge from session state

Keep stable constraints and architecture decisions in their existing canonical home. Record a decision only when remembering its rationale and reversal condition will prevent a real repeated mistake. Do not create an ADR for every edit.

Keep unfinished work in existing issues and one resumable checkpoint, not parallel roadmaps. Link the relevant files, acceptance checks and last confirmed published/verified revision. A commit trailer can be a fallback cursor on an already-needed commit, but is immutable: its next action may already have happened. Reconcile live state before following it. A local scratchpad, an unreferenced commit and chat memory are not guaranteed cross-session storage.

Checkpoints do not lock files or restart ChatGPT. Coordinate one writer for overlapping changes; preserve concurrent work. Never let a historical note silently widen the current user's authority.

## 7. Validate the setup by use, not file count

Starting from the entry point and map, check whether a fresh session could locate a relevant source, its coupled files, the real validation command, publication risks and the resume location without a broad audit. Fetch the actual files to verify the route. A same-session walkthrough is a navigation review, not independent-agent evidence.

Run the documented check. In an isolated temporary copy, introduce a harmless structural error and confirm that it fails; never publish the deliberately broken copy. This tests the checker, not model quality. Confirm that any new CI actually reports for the intended revision, or explicitly record that the workflow is installed but execution is unverified.

For repeated real tasks, compare observed discovery calls, stale-context mistakes, retries and completed verified changes against a recorded baseline. Do not invent a speedup percentage or optimize call count at the expense of correctness.

## Applying this through the existing commands

Use **Deep Run EXECUTE** with the goal “prepare this repository for ChatGPT + GitHub work.” Inspect first, reuse existing conventions, implement the minimum useful entry/map/check changes and verify them. In BACKLOG mode, propose the setup as issues only; do not create repository files or workflows.

For a normal feature request, consume the existing entry/map. Repair only a relevant stale pointer when authorized. Do not turn every session into a repository reorganization, copy this whole guide into every project, add a new manifest/schema without a consumer, or edit other repositories without scope.

## Sources

Checked 2026-09-09. These support platform mechanisms, not measured productivity gains.

1. [OpenAI: GitHub in ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)
2. [OpenAI: AGENTS.md discovery in Codex](https://developers.openai.com/codex/guides/agents-md)
3. [GitHub: repository contents API](https://docs.github.com/en/rest/repos/contents)
4. [GitHub: Git trees API](https://docs.github.com/en/rest/git/trees)
5. [GitHub: job summaries](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#adding-a-job-summary)
6. [GitHub: checkout behavior](https://github.com/actions/checkout)
7. [GitHub: secure workflow use](https://docs.github.com/en/actions/reference/security/secure-use)
