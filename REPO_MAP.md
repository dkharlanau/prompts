# Prompts: task-to-file map

Repository: `dkharlanau/prompts`. Read [AGENTS.md](AGENTS.md) for instructions. This is navigation for this library, not a generated index or a substitute for source. Fetch the observed ref; check live branch policy and publication effects before writes.

## Source of truth and change routes

| Task | Read/edit | Coupling and verification |
|---|---|---|
| Change Deep Run behavior | [Canonical Deep Run](loops/deep-run.md) | Update its version in [catalog](catalog.yaml); preserve both modes and the word budget; run the structural check |
| Change backlog execution | [Canonical Executor](loops/backlog-executor.md) | Update its catalog version; preserve independent usability; run the structural check |
| Route commands or inputs | [Entry point](AGENTS.md), [catalog](catalog.yaml), [renderer](scripts/prompts.py) | Keep three command routes and six fields consistent; exercise all render routes |
| Improve ChatGPT GitHub operation | [ChatGPT adapter](CHATGPT_DEEP_RUN.md), [GitHub protocol](GITHUB_WORKFLOW.md) | Put essential behavior in Deep Run; keep detailed recipes outside the copyable prompt; do not impose a ChatGPT adapter on Codex |
| Prepare a target repository | [Repository setup guide](REPOSITORY_SETUP.md) | Reuse the target's conventions; apply only within its authority; no mass rollout or site fixtures here |
| Change validation/CI | [Validator](scripts/prompts.py), [workflow](.github/workflows/prompts-check.yml) | Local check plus appropriate negative cases; inspect exact-revision CI and logs; YAML syntax alone does not prove execution |
| Refresh source rationale/model guidance | [Research](RESEARCH.md), [profiles](MODEL_PROFILES.md) | Verify current primary sources; do not invent model rankings or measured gains |

The two `loops/*.md` files are the canonical copyable prompts. `catalog.yaml` is JSON-compatible YAML with routes, versions, fields and budgets. `scripts/prompts.py` validates and renders; rendered prompts are transient output, not another source to edit. Keep private run specifications outside this public repository. This library has no generated website or target-product dataset to maintain.

## Verification and side effects

From the repository root: `python3 scripts/prompts.py check`.

Requires Python 3.10+; standard library only, no dependency installation or credentials. This command reads files and prints results; it makes no network/model calls or repository writes. Exit 0 means structural checks passed; errors return nonzero. Coverage: canonical files/placeholders/modes, word budgets, versions, local link existence and three synthetic render routes. It does not prove semantic map freshness, runtime agent behavior, website quality or business impact.

For renderer changes, also run `python3 scripts/prompts.py render <command> --spec <local-json>` for each catalog command and test invalid inputs. The specification contains the six documented fields; it is not committed here.

[Prompt library checks](.github/workflows/prompts-check.yml) runs the same check on main pushes, pull requests and manual dispatch. It has one validation job, a timeout, read-only repository permissions and no deploy step. It prints the actual checked revision and report to logs and the job summary. Inspect the run rather than assume this configuration ran. A PR may validate a synthetic merge revision. External integration settings remain a live preflight check, not a claim made by this map.

## Resume and maintenance

Reuse a relevant issue checkpoint when one exists. Otherwise search coherent commit messages for `Agent-Run`, then reconcile HEAD, diff and checks before following `Agent-Next`. No checkpoint-only commits or mirrored backlog.

Update this map when a route, command or output boundary changes. The structural check validates its local links, not the meaning of its descriptions. Keep generated context dumps, site tests, private run specs and session transcripts out of this library.
