# Deep Run Benchmarks

This repository evaluates one canonical prompt and its **model × reasoning-effort configuration**. The goal is to measure whether a Deep Run actually improves a real project, not whether its reasoning sounds sophisticated.

This is an internal repository eval protocol, not an external scientific benchmark.

## DRS-100 — Deep Run Score

Score every dimension from 0–5 and apply the weight.

| Dimension | Weight | 5/5 means |
|---|---:|---|
| Outcome improvement | 25 | The run materially improves the stated real-world outcome or produces decisive evidence that prevents a bad change. |
| Evidence & verification | 20 | Claims are grounded in real sources/artifacts and the changed state is meaningfully verified. |
| Bottleneck & decision quality | 15 | The run identifies the dominant constraint, compares real alternatives and handles uncertainty/trade-offs explicitly. |
| Execution completeness | 15 | Authorized work is carried through to a coherent changed state rather than stopping at analysis or a plan. |
| Independent re-evaluation | 10 | The result is judged from scratch against the same baseline/success evidence and weak work is not defended. |
| Learning & iteration | 5 | New evidence changes subsequent decisions and durable learning is preserved without documentation inflation. |
| Regression & entropy control | 5 | The run checks for regressions, duplicated work and avoidable complexity. |
| Reasoning efficiency | 5 | Heavy reasoning is spent on decision-changing work rather than repeated summaries, theatrical roles or uncontrolled loops. |

`DRS-100 = Σ (dimension_score / 5 × weight)`

## Prompt status

- **experimental** — structure exists but has not passed representative runs.
- **candidate** — DRS ≥ 75 in at least two materially different real tasks with no critical failure.
- **stable** — DRS ≥ 85 in at least three materially different domains and repeated runs show no recurring critical failure.

A high score does not imply that every iteration must change the project. Correctly rejecting a weak proposal or concluding `NO CHANGE` can score highly when evidence supports it.

## Critical failures

A run cannot score as stable if it materially tends to:

- stop after an audit/plan when safe execution was authorized;
- fabricate evidence or silently turn hypotheses into facts;
- optimize number of files/features/issues/commits instead of the outcome;
- choose a bottleneck without examining plausible competing causes;
- generate multiple cosmetic variants and call them alternatives;
- defend an implementation because work was already invested in it;
- declare improvement without inspecting/verifying the changed state;
- loop without a meaningful state/evidence change;
- create duplicate issues, abstractions, content or documentation;
- ignore explicit authority/deployment constraints;
- repeatedly ask questions whose answers are already available from the project context.

## Canonical benchmark protocol

For a prompt-version evaluation:

1. Freeze a meaningful baseline state (commit/snapshot/data window).
2. Define `OUTCOME`, `TARGET`, `CONSTRAINTS`, `AUTHORITY` and `SUCCESS_EVIDENCE` before the run.
3. Run a simpler one-shot baseline using the same context/tools when a baseline comparison is feasible.
4. Run the current `deep-run.md` against the same starting state.
5. Score both against the same observable rubric.
6. Run Deep Run again from the resulting changed state to test whether it finds a new dominant bottleneck rather than repeating the first pass.
7. Record failures that would justify changing the prompt, model adapter or benchmark.

## Model × reasoning-effort benchmark

Do not rank models from vendor claims or one impressive run.

When comparing configurations:

1. Use the **same Deep Run version**.
2. Start each candidate from the **same baseline state**.
3. Give each candidate the same tool access, permissions, files, project context and success evidence.
4. Change only the model/reasoning configuration unless the test explicitly evaluates a model adapter.
5. Run each important configuration at least **3 times** when practical.
6. Record both DRS-100 and real project outcomes.
7. Prefer the configuration whose advantage is repeatable and materially useful.

Current configurations to benchmark:

- GPT-6 Astra — Medium
- GPT-6 Astra — High
- GPT-5.6 Sol — High
- GPT-5.6 Sol — Extra High when available
- GPT-5.6 Luna — Think as a lower-capability/subtask reference

## Representative test domains

Use real work, not artificial trivia. Maintain at least these three categories:

### A. Product / growth

Example shape: identify and implement the highest-leverage improvement to discovery → first value → continuation in an existing user-facing product.

### B. Website / service

Example shape: deeply audit a real website/service, find the dominant user/business bottleneck, make safe changes, and verify the experience rather than only source code.

### C. Software / repository

Example shape: resolve a non-trivial repository problem or improve architecture/maintainability with executable verification and regression control.

Prefer benchmark tasks from projects that already have real history, constraints and artifacts.

## Measures worth recording

Attach project-native metrics when they exist:

- task/issue actually resolved;
- tests/build/static checks;
- regression count;
- time-to-first-value;
- conversion/activation/retention;
- qualified search/discovery visibility;
- user/expert preference score;
- unsupported-claim count;
- duplicated work introduced/removed;
- before/after quality rubric;
- number of consequential decisions changed by new evidence;
- tool calls, elapsed task time and allowance/token usage when exposed by the environment.

Resource use is diagnostic, not the primary goal. A more expensive run is acceptable when it produces materially better outcomes.

## Benchmark record

Store material evaluations using this schema:

```yaml
prompt_id: deep-run
prompt_version: <version>
profile_version: <version>
date: <yyyy-mm-dd>
project: <project>
domain: <product|website|service|software|research|other>
baseline_ref: <commit/snapshot/date>
outcome: <desired outcome>
model: <exact model label/id>
reasoning_effort: <low|medium|high|extra-high|pro|other>
environment: <chatgpt|work|codex|api|other>
run_number: <n>
drs_100: <0-100>
observable_outcome: <before/after result>
completion: <complete|partial|blocked|failed>
regressions: []
unsupported_claims: <n or notes>
resource_usage: <if available>
critical_failures: []
notes: <short evidence-based notes>
```

## Promotion rule

A model profile or prompt version becomes the preferred default only when its improvement is visible in comparable outcomes across multiple runs. Update `MODEL_PROFILES.md` and `catalog.yaml` together with the evidence reference.

The benchmark itself should evolve when real failures expose blind spots in this rubric.
