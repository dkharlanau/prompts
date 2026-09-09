# Research basis

The repository intentionally uses **one canonical Deep Run** rather than a growing catalog of domain prompts. The prompt combines a small set of recurring agent patterns as conditional phases: inspect reality, use independent perspectives when useful, compare alternatives, adversarially challenge important decisions, test decision-changing uncertainty, execute, verify, re-evaluate and learn.

Research is used to justify mechanisms and evaluation criteria, not as decorative authority. None of the sources below proves that more agents, more reasoning or longer prompts are automatically better.

## Agent/workflow patterns

### Anthropic — Building Effective Agents
https://www.anthropic.com/engineering/building-effective-agents

Relevant patterns:

- parallelization for genuinely independent perspectives or voting;
- orchestrator–workers when the work naturally decomposes;
- evaluator–optimizer when explicit feedback can improve a result;
- preference for simple composable workflows before unnecessary agent complexity.

Deep Run interpretation: these patterns are optional phases inside one workflow. Roles/subagents are invoked only when they can materially change the outcome.

### OpenAI — Harness engineering: leveraging Codex in an agent-first world
https://openai.com/index/harness-engineering/

Relevant observations:

- the repository/system of record should be inspectable and mechanically useful to agents;
- verification and executable feedback matter more than elaborate plans;
- long-lived agent-developed repositories need periodic simplification/gardening;
- progressive disclosure is preferable to one giant repository instruction file.

Deep Run interpretation: inspect the real project, execute against it, verify the changed state, and run an entropy check before continuing.

### OpenAI — Evals and evaluation-driven improvement
https://openai.com/index/evals-drive-next-chapter-of-ai/

Relevant pattern: specify → measure → improve, with failures turned into future eval cases.

Deep Run interpretation: establish a baseline before changing the project and evaluate the result against the same observable evidence afterward. `BENCHMARKS.md` applies this principle to both prompt versions and model×effort profiles.

### Self-Refine — Iterative Refinement with Self-Feedback
https://arxiv.org/abs/2303.17651

The work studies generation → feedback → refinement loops across multiple tasks.

Deep Run interpretation: feedback must change the next action; repeated self-critique without a changed artifact/evidence state is not considered useful iteration.

### Reflexion — Language Agents with Verbal Reinforcement Learning
https://arxiv.org/abs/2303.11366

The framework uses feedback/reflection from prior attempts to improve later trials without model-weight changes.

Deep Run interpretation: preserve durable validated/rejected hypotheses and failure modes, but do not store ephemeral chain-of-thought or create documentation inflation.

### SWE-bench Verified
https://www.swebench.com/verified.html

A human-validated benchmark of real GitHub software-engineering tasks.

Deep Run interpretation: software work should be judged by resolved behavior and executable verification rather than patch descriptions or apparent sophistication.

## Current model guidance

### OpenAI — Model guidance: GPT-6 Astra
https://developers.openai.com/api/docs/guides/latest-model

Current guidance relevant to this repository includes:

- Astra is positioned for difficult multistep work across coding, browsing/computer use, research and professional workflows;
- Astra is more likely than prior models to pause for consequential clarification, so autonomous workflows should explicitly bias toward follow-through for already-authorized work;
- Astra can be sensitive to instructions in skills/AGENTS files, making instruction hygiene important;
- subagent delegation behavior can be explicitly guided when parallel work is useful;
- verification should be calibrated to the change rather than repeated mechanically;
- reasoning effort can be changed during work in supported API environments;
- Astra does not support `none` reasoning effort.

Deep Run interpretation: keep one core prompt and use a short Astra adapter in `MODEL_PROFILES.md` rather than duplicating the full prompt.

### OpenAI — GPT-5.6 and GPT-6 Pro in ChatGPT
https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt

Relevant current product guidance:

- GPT-5.6 Sol supports Medium, High and Extra High reasoning on eligible plans;
- GPT-6 Astra is exposed as GPT-6 Pro on eligible plans as rollout continues;
- reasoning controls are product-dependent and can change over time.

### OpenAI — Managing usage with GPT-6 Astra in Work and Codex
https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex

Relevant guidance:

- Astra is recommended for the most demanding coding/research/analysis problems;
- Sol offers a strong balance for professional/coding/research work;
- Luna is positioned for focused/repetitive work;
- higher reasoning effort does not always yield a better result;
- Astra at lower effort can outperform Sol at higher effort on some work.

Deep Run interpretation: Astra Medium and Sol High are current starting recommendations, with effort escalation based on task difficulty or observed misses rather than automatically choosing the maximum setting.

## Why one canonical prompt

The previous repository version separated council, Best-of-N, adversarial decision, experiment, evaluator-optimizer, discovery-to-value and gardening into different files. Those patterns are useful, but choosing/composing them created an extra meta-task for the operator and encouraged prompt variants by domain.

The canonical Deep Run instead uses a conditional workflow:

- if perspectives can change a decision → run independent perspectives;
- if the solution space is open → generate materially different alternatives;
- if the choice is consequential → red-team it;
- if uncertainty can reverse the decision → run a falsifiable experiment;
- if execution is authorized → implement;
- always verify material changes;
- always re-evaluate against the same baseline;
- check entropy before starting another iteration.

This preserves the valuable mechanisms while reducing selection overhead and prompt drift.

## Epistemic rule

A source saying that a model is more capable does **not** establish the best model/reasoning setting for this Deep Run. `MODEL_PROFILES.md` treats official model guidance as a prior. Preferred settings must ultimately be based on comparable real-project runs recorded under `BENCHMARKS.md`.
