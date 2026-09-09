---
id: discovery-to-value
version: 0.1.0
status: candidate
category: product-growth
pattern: journey simulation + bottleneck optimization + evaluator-optimizer
best_for: products or services that must convert discovery into clear user value and repeat usage/action
avoid_when: acquisition and activation are not relevant to the current goal
benchmark_target: PLS-100 >= 85
research_basis: [openai-evals, anthropic-effective-agents]
---

# Discovery-to-Value Loop

## Inputs

- `{{OFFER}}`
- `{{TARGET}}`
- `{{GOAL}}`
- `{{DISCOVERY_CHANNELS}}`
- `{{CONTEXT}}`
- `{{CONSTRAINTS}}`
- `{{AUTHORITY}}`
- `{{METRICS}}`

## Template

```text
OFFER
{{OFFER}}

TARGET
{{TARGET}}

GOAL
{{GOAL}}

DISCOVERY CHANNELS
{{DISCOVERY_CHANNELS}}

CONTEXT
{{CONTEXT}}

CONSTRAINTS
{{CONSTRAINTS}}

LOOP

1. REALITY CHECK
Inspect the current offer and the actual experience available to {{TARGET}}. Do not infer capabilities from intended positioning when the real artifact differs.

2. INTENT
Identify the concrete problems, jobs or intents that could realistically cause the target user to seek or encounter the offer.

3. DISCOVERY
For the strongest intents, inspect the path from discovery channel to first impression. Identify why the offer would or would not deserve attention relative to alternatives.

4. FIRST VALUE
Trace the shortest journey from arrival to a user-observable useful outcome. Find ambiguity, friction, weak trust signals and steps that do not contribute to value.

5. CONTINUATION
Identify the natural next action: return, progress, purchase, contact, reuse, share or another goal-relevant continuation. Avoid artificial engagement loops.

6. BOTTLENECK
Choose the single point in discovery → understanding → action → value → continuation that most constrains {{GOAL}}.

7. IMPROVE
Within {{AUTHORITY}}, make the smallest coherent change likely to move {{METRICS}}. Prefer improving existing value over creating content or features for volume.

8. REPLAY
Repeat the same target journeys against the changed state. Compare before/after friction, clarity, time-to-value and likely abandonment.

9. LEARN
Record what evidence changed and identify the new dominant bottleneck.

STOP
Stop when {{GOAL}} is sufficiently supported by {{METRICS}}, or when further improvement requires real external/user evidence rather than additional internal simulation.
```

## Expected output

A verified improvement to the discovery-to-value journey, with before/after evidence and the next dominant bottleneck.
