# Automation and Observability

- Define an explicit authority envelope: permitted decisions, prohibited actions, limits, escalation triggers, and human override.
- Never invent missing source fields. Preserve source data and mark ambiguous extraction as uncertain.
- Use deterministic mappings and conflict order where repeatability matters.
- Represent confidence states explicitly: accepted, needs review, blocked, or equivalent.
- Automatically act only when evidence meets the approved threshold; surface or block consequential ambiguity.
- Make decisions inspectable through logs, traces, source links, versions, seeds, time controls, and acceptance tests as applicable.
- Bound work, retries, fan-out, resource use, and failure propagation.
- Provide safe pause, cancellation, rollback, and manual correction paths.
- Preserve an audit trail connecting inputs, transformations, decisions, actions, and outcomes.
- Test adversarial, ambiguous, incomplete, duplicate, stale, and pathological inputs.
