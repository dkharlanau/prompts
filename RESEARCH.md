# Research and design decisions

Sources checked **2026-09-09**. These sources support mechanisms, not a claim that this library is the strongest prompt system or guarantees product success. Current official pages can change; recheck before a model/configuration refresh.

| Primary source | Relevant guidance | Library decision |
|---|---|---|
| [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model) | Explicit follow-through, instruction hygiene, purposeful delegation and proportionate verification | Infer routine details, act within authority, condition review depth on risk |
| [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903) | ChatGPT retrieves authorized repository content on demand; capabilities vary by product surface | Treat search as discovery, keep an exact SHA/path evidence map, inspect active tools instead of assuming synced state or write access |
| [Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) | End-to-end work, preservation of existing edits, meaningful implementation and avoiding unproductive repetition | Inspect live state, protect concurrent work, verify and checkpoint rather than simulate endless progress |
| [Codex best practices](https://developers.openai.com/codex/learn/best-practices) | Clear goals/context/constraints/completion, practical repository guidance and testing | Six filled inputs, short task-specific context, executable checks |
| [AGENTS.md guidance](https://developers.openai.com/codex/guides/agents-md) | Repository-scoped instructions and explicit discovery of applicable guidance | Use this library as a router; inspect the target's applicable instructions rather than copying the whole library |
| [Harness engineering](https://openai.com/index/harness-engineering/) | Inspectable repository knowledge, feedback loops and manageable instruction structure | Two templates, progressive reading, durable evidence instead of accumulating process documents |
| [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Task-specific evaluation, representative cases, explicit criteria and evaluation of changes | Frozen baselines, critical failures, held-out cases and separation of structural checks from model performance |

## Why v2 changes the previous design

At baseline `cfd120d893ed7a049402b3a36bc4464d6df24878`, the library already had strong outcome-first reasoning, backlog deduplication and continued execution. The main weaknesses found by repository review were:

- A long staged Deep Run risked making every task pay for councils, tournaments and repeated analysis. v2 keeps those mechanisms conditional instead of prescribing fixed alternatives or roles.
- Agent-filled inputs had no mechanical completeness check. The optional renderer validates fields and removes the unused mode; it does not replace real context discovery.
- Generic issue closure did not clearly distinguish a branch result from the required integration/release boundary. v2 requires that distinction.
- Capability gaps, concurrent edits, repeated no-progress attempts and interrupted sessions needed concrete handling. v2 adds targeted rules without requiring a particular agent product.
- Templates were marked candidate although the published candidate standard requires recorded real-run scores. v2 remains experimental pending that evidence.

## Deliberately not added

No mandatory multi-agent council, hidden-reasoning transcript, domain prompt clones, invented "best model" ranking, background scheduler, paid benchmark runner or self-awarded quality score. No claim that shorter text alone is better.

The design hypothesis is that a capability-aware contract preserves decision quality while reducing mode confusion and unsupported completion claims. It must be tested on actual task traces, not inferred from safety phrases or passing renderer tests. Keep failed-run evidence with the target project and revise only what the evidence implicates.

## GitHub execution update: templates v2.1

Baseline: `b3841804e49f46ee291e3cb62669c0cb1381c85a`. The owner requested lower branch/merge overhead and more recoverable ChatGPT-to-GitHub work. Main-first is this library's operating preference for authorized low-risk implementation, not a universal GitHub recommendation or permission to bypass repository policy.

The update replaced end-of-session-only recovery with early per-batch checkpoints, preferred atomic publication, reconciled ambiguous writes before retries, and reduced CI waste without leaving workflows disabled. Essential rules were embedded in both templates; optional recipes live in [GITHUB_WORKFLOW.md](GITHUB_WORKFLOW.md).

| Primary source checked 2026-09-09 | Mechanism | Design consequence |
|---|---|---|
| [Git trees](https://docs.github.com/en/rest/git/trees) and [references](https://docs.github.com/en/rest/git/refs) | Multiple file entries can share a tree/commit; a non-forced ref update requires a fast-forward | Preserve the current base tree, publish coherent batches atomically, reconcile moved HEAD instead of forcing |
| [REST API best practices](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api) | Avoid excessive polling/concurrent calls, handle rate limits, reuse conditional reads | Targeted SHA-based reads, serialized writes, bounded retries and explicit mutation read-back |
| [Workflow concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency) | A concurrency group can cancel superseded running validation | Scope cancellation to the same validation workflow/ref; do not copy it blindly to deployment |
| [Skip workflow runs](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs) and [job conditions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-jobs-with-conditions) | Skipped workflows may leave required checks pending; job-level skip has different status semantics | No blanket skip tokens; preserve an always-reporting required gate and distinguish skipped from actual verification |

## ChatGPT execution adapter: Deep Run v2.2

Baseline: `ab349c1959636ff9f9b5f1383081a5d4630b4000`. The previous GitHub protocol was runtime-neutral. That left avoidable inefficiency in conversation-first ChatGPT runs: repeated search after paths were already known, too many connector round-trips, no explicit decision lock for high reasoning effort, and a checkpoint gap when no issue/state artifact existed.

v2.2 adds a **conditional ChatGPT adapter** without creating a fourth command or changing Backlog Executor. The adapter is not a Codex prompt.

Design changes:

- maintain a compact session evidence map keyed by observed HEAD/path/blob SHA/issue IDs instead of repeatedly rediscovering unchanged state;
- use repository search for discovery, then exact current reads because ChatGPT GitHub retrieval is on demand rather than a guaranteed synced repository index;
- establish a write barrier before remote mutation;
- when Git data tools exist, create and inspect an unreferenced candidate commit before moving `main`, giving ChatGPT a staging/review point without branch/PR overhead;
- use `Agent-Run`, `Agent-Next`, and `Agent-Verify` commit trailers only as a fallback resume cursor on already-needed coherent commits;
- treat existing CI as remote executable evidence when no shell exists and allow minimal measured CI-loop tuning within repository authority;
- prevent High/Extra High reasoning from becoming repeated architecture reconsideration by recording a decision and its reversal condition;
- resume from checkpoint + current HEAD + changes since the confirmed SHA, expanding to a fresh audit only when evidence invalidates the saved decision.

The OpenAI GitHub help page documents on-demand retrieval and variable product-surface capabilities. It does not establish that every ChatGPT surface can write; the library therefore requires live capability inspection. The staged-candidate and commit-trailer mechanisms are library design choices based on Git primitives, not OpenAI product guarantees.

Checkpoint cadence, main-first, staged candidate commits and CI tuning remain hypotheses about execution efficiency until validated on repeated real tasks. Structural checks cannot establish outcome gains.


## Repository-side preparation: Deep Run v2.3

Baseline: `556455fca4014bb3ca5c8ad89719ade3583c98fb`. The owner asked to prepare repository structure for the ChatGPT app, not only to add model instructions. The library had runtime guides but no compact task-to-source map, and no version-controlled validation workflow at this baseline.

[REPOSITORY_SETUP.md](REPOSITORY_SETUP.md) defines a minimal explicit entry point, task map, canonical/generated source boundary, real check contract, connector-readable CI output and resumable state. [REPO_MAP.md](REPO_MAP.md) applies that navigation to this library. The entry point is shortened rather than duplicating the new guide. Deep Run reads existing target navigation first; ordinary feature work does not automatically become setup work. Backlog Executor remains unchanged.

The new [prompt-only workflow](.github/workflows/prompts-check.yml) closes a missing remote structural-check path; it is not a measured CI speed optimization. It runs the existing standard-library validator, keeps one read-only validation job, pins checkout, does not persist checkout credentials, reports the actual revision to stdout and a job summary, and preserves command failures. No site fixtures, paid model runner, deployment, arbitrary-command dispatcher or new user command is introduced. Installing YAML and a local shell test are not evidence of a successful hosted run.

Sources checked 2026-09-09: [OpenAI GitHub access](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt) documents on-demand retrieval and describes the standard app as read-only; actual exposed tools determine this session's write capabilities. [AGENTS.md documentation](https://developers.openai.com/codex/guides/agents-md) specifies automatic discovery for Codex, not a guarantee for ordinary ChatGPT connector chat. [Contents](https://docs.github.com/en/rest/repos/contents) and [trees](https://docs.github.com/en/rest/git/trees) have retrieval/truncation boundaries. [Job summaries](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#adding-a-job-summary) complement logs, while [checkout](https://github.com/actions/checkout) documents event-specific revisions. [Secure use](https://docs.github.com/en/actions/reference/security/secure-use) supports least privilege, immutable pins and avoiding untrusted privileged execution.

Task maps, source-first edits and minimal navigation are engineering choices, not new ChatGPT platform features. Check map routes and command failure behavior locally; measure discovery effort and real task outcomes before claiming improvement. A larger guide or a passing structural check alone cannot prove faster or better model work.

## Website stack adaptation: Deep Run v2.4

Baseline: `b291695e75393ec34f906a4adb52bb95a82bbaa4`. The owner requested more effective ChatGPT work across GitHub Pages and Next.js websites. [WEBSITE_STACKS.md](WEBSITE_STACKS.md) separates framework/version, router, export/runtime and hosting rather than creating conflicting prompt variants. It supplies a narrow task-to-source read path and stack-specific verification boundaries; repository setup records only missing facts in existing navigation.

The [Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) and [Next.js static-export guide](https://nextjs.org/docs/app/guides/static-exports) support treating Next.js-on-Pages as a valid combination. [Next.js agent guidance](https://nextjs.org/docs/app/guides/ai-agents) supports version-matched docs, but installed package documentation is not assumed available to a GitHub-only reader. [Version 16 guidance](https://nextjs.org/docs/app/guides/upgrading/version-16) establishes why universal lint/build commands are unsafe. The adapter's sources also cover client/server boundaries, environment variables, base paths and provider previews.

The canonical prompt gains a 31-word website contract, remaining at 1097/1100 template words without increasing its budget. Detailed profiles load only when relevant. Three commands, six inputs, BACKLOG's issue-only scope, publication restrictions and the unchanged Backlog Executor remain intact. No site tests, project configuration, new CI, dependency or deploy integration is added here.

Review selection against static HTML, Next.js export, runtime, mixed-workspace and unavailable-runtime cases. Structural rendering/link checks are not empirical proof that an agent selected correctly or that websites improved. Actual task failures and before/after evidence belong in the target repositories; revise the shared adapter only when repeated evidence warrants it.
