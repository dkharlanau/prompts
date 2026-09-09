# Research basis

The library is intentionally pattern-driven rather than vendor-specific. The templates borrow from recurring findings in agent systems, iterative refinement and evaluation research.

## Sources

### Anthropic — Building Effective Agents
https://www.anthropic.com/engineering/building-effective-agents

Relevant patterns:
- parallelization for independent perspectives or voting;
- orchestrator–workers for complex tasks whose subtasks are not known in advance;
- evaluator–optimizer when explicit quality criteria permit iterative improvement;
- preference for simple composable workflows before adding unnecessary agent complexity.

Used in: `council`, `best-of-n`, `autonomous-improvement`, `evaluator-optimizer`.

### OpenAI — Harness engineering: leveraging Codex in an agent-first world
https://openai.com/index/harness-engineering/

Relevant observations:
- repository knowledge works better as a structured system of record than a giant monolithic instruction file;
- agent-first development benefits from explicit feedback loops, executable verification, quality tracking and periodic repository gardening;
- progressive disclosure helps preserve useful context.

Used in: `autonomous-improvement`, `repository-gardening` and repository usage conventions.

### OpenAI — How evals drive the next chapter in AI for businesses
https://openai.com/index/evals-drive-next-chapter-of-ai/

Relevant pattern:
- specify → measure → improve;
- evaluate real outputs under real conditions;
- turn failures and expert judgments into a compounding evaluation/data flywheel.

Used in: `BENCHMARKS.md`, `experiment`, `evaluator-optimizer`.

### Self-Refine — Iterative Refinement with Self-Feedback
https://arxiv.org/abs/2303.17651

The paper studies iterative generation → feedback → refinement across multiple tasks and reports material improvements over one-shot generation.

Used in: `evaluator-optimizer` and the requirement that feedback must change subsequent iterations.

### Reflexion — Language Agents with Verbal Reinforcement Learning
https://arxiv.org/abs/2303.11366

The framework uses verbal feedback and stored reflection from prior attempts to improve later trials without changing model weights.

Used in: `autonomous-improvement`, `experiment`, and the rule to preserve reusable learning between iterations.

### SWE-bench Verified
https://www.swebench.com/verified.html

A human-validated benchmark of real GitHub software-engineering tasks. Its core lesson for this library is methodological: agent quality should be judged by whether a real task is resolved under executable tests, not by the apparent quality of the generated reasoning or patch description.

Used in: verification and benchmark design for software tasks.

## Library interpretation

These references do **not** prove that every multi-agent or self-reflective loop is better than a simpler prompt. The repository therefore treats complexity as a cost.

A loop should be retained only when repeated evaluation shows that its feedback structure improves outcomes relative to a simpler baseline.
