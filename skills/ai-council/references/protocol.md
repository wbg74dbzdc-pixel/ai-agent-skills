# AI Council Protocol — Standalone Skill Companion

This file is self-contained when the `ai-council` skill is copied without the standards bundle. The **canonical full governance protocol** is `governance/ai-agent-standards/playbooks/ai-council.md` in the public standards repository. If both exist, use the canonical version; the constraints below are the portable minimum, not a competing policy.

## When and how much

Use Council review only for consequential decisions with genuine tradeoffs, or when explicitly requested. Record the decision, owner, goals, constraints, verified evidence, disputed assumptions, realistic alternatives (including doing nothing), deadline and budget.

- **Quick:** 3 independently scoped advisors plus lead synthesis; add peer review if uncertainty warrants it.
- **Standard:** 5 independent advisors, anonymized peer comparison, lead synthesis.
- **Deep:** Standard plus targeted research, deliberate disconfirmation and independent verification.

Choose a mode proportional to importance and cost. Approval is required before material new agent/cost fan-out unless already authorized.

## Independent lenses

1. **Contrarian:** failure modes and hidden assumptions.
2. **First principles:** core goal, constraints and framing.
3. **Expansionist:** valuable alternatives and overlooked upside.
4. **Outsider:** missing stakeholders, surprising gaps.
5. **Executor:** implementability, resources, rollback and validation.

Give each a neutral identical evidence packet; do not show other findings before the first pass. Require each to state its strongest objection to its own view, and distinguish facts from estimates and unknowns.

## Reconcile, verify, return

Anonymize peer feedback when feasible; inspect correlated error, dissent and missing evidence. Synthesize tradeoffs and a feasible smallest next step. Independently verify claims that determine the decision. Do not infer truth from agreement, simulation, or repeated model output.

Deliver a report with options, evidence, objections, feasibility/cost, remaining uncertainties, recommendation or `insufficient evidence`, and an owner decision field (see `report-template.md`). Preserve dissent and provenance.

If real independent agents are unavailable, label the process **sequential fallback** and disclose its limits. Never claim anonymity or independence that was not achieved.

Stop when the premise is broken, the budget is exhausted, repeated rounds add no new evidence, or specialist judgment is missing. The user retains decision authority; Council review does not authorize code changes, external actions, deployment, purchases, or other restricted operations.

## Provenance

Portable implementation informed by the AI Council concepts described by Andrej Karpathy and Ole Lehmann; no endorsement implied.
