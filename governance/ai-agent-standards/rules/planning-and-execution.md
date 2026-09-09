# Planning and Execution

## Standard loop

1. Inspect instructions, source of truth, current state, and related tests.
2. Reproduce the problem or establish a baseline when applicable.
3. Write a plan for multi-step, risky, cross-cutting, or long work.
4. Make the smallest coherent change that advances the agreed goal.
5. Test the changed behavior, then broaden validation based on risk.
6. Inspect the diff and generated artifacts.
7. Update authoritative documentation and decisions.
8. Leave a clean, evidence-based handoff.

## Planning rules

- Plans describe outcomes and verification, not ceremonial steps.
- Keep exactly one active step and update the plan as evidence changes.
- Record decisions and surprises that a future agent would otherwise rediscover.
- Prefer an end-to-end vertical slice before implementing every subsystem.
- Make migrations reversible and releases staged when failure impact warrants it.
- Stop and reopen the task contract if material scope, authority, or assumptions change.

## Engineering boundaries

- Preserve established architecture unless changing it is part of the approved goal.
- Keep durable domain truth separate from presentation.
- Prefer deterministic, inspectable core behavior where feasible.
- Externalize legitimate tunables without turning invariants into casual configuration.
- Version persistent schemas and provide migrations or an explicit compatibility policy.
