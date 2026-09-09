# AI Council Protocol

Use the Council to pressure-test consequential decisions with genuine tradeoffs. It is an escalation mechanism, not a substitute for ordinary reasoning, research, testing, professional advice, or the user's authority.

## Preconditions

Record the actual decision and desired end state; decision owner; success criteria; constraints; non-negotiables; deadline; known facts; assumptions; unknowns; authoritative sources; realistic options; mode; and resource budget. Include doing nothing or a smaller experiment when relevant. Ask focused questions if the framing is materially incomplete.

## Modes

| Mode | Use | Minimum procedure |
| --- | --- | --- |
| Quick | Moderate-stakes, reversible decision | Three independent advisors and lead synthesis; peer review only if disagreement or uncertainty warrants it |
| Standard | Consequential decision with real tradeoffs | Five independent advisors, anonymized peer review, and chairman synthesis |
| Deep | High-impact, costly, legally sensitive, safety-sensitive, or hard-to-reverse decision | Standard mode plus targeted research or specialist review, explicit disconfirmation, and independent verification of decisive claims |

Use the least expensive mode that matches the risk. The user may override the mode.

## Standard lenses

1. **Contrarian:** Failure modes, weak assumptions, contradictions, second-order harm, and reasons the preferred option may fail.
2. **First principles:** Reconstruct the problem from the goal, constraints, and fundamentals; challenge the framing.
3. **Expansionist:** Overlooked upside, combinations, opportunities, and stronger variants, with cost and feasibility.
4. **Outsider:** Obvious gaps, confusing assumptions, stakeholder effects, and questions insiders may miss.
5. **Executor:** Dependencies, effort, sequencing, operational burden, validation, rollback, and the next concrete action.

Adapt expertise to the task. Preserve at least one disconfirming lens and one execution lens.

## Procedure

### Independent analysis

Give every advisor the same neutral brief, evidence packet, constraints, and output requirements. Do not expose other conclusions in the first round. Require separation of observations, sourced claims, estimates, assumptions, proposals, and unknowns. Require evidence or a verification method for decisive claims, plus feasibility, what would change the recommendation, and the strongest self-objection.

### Anonymized peer review

Remove identifying labels when possible. Rank reasoning quality, evidence, feasibility, and goal alignment. Identify shared unsupported premises, correlated blind spots, omitted options, and contradictions. Scores guide synthesis but do not determine truth.

### Chairman synthesis

Reconcile duplication and factual conflict; distinguish consensus from shared premises; preserve material dissent; compare tradeoffs, opportunity costs, and feasibility; flag required verification or human review; state what the recommendation sacrifices; and give the smallest useful next action, validation step, and revisit conditions. Return `insufficient evidence` or a bounded experiment instead of forcing a verdict.

### Verification and owner decision

Independently verify claims that materially control the decision. Agreement is never verification. Escalate legal, medical, financial, safety, privacy, security, or other high-stakes uncertainty appropriately. Present the report to the decision owner. The report does not authorize purchases, publishing, deployment, destructive changes, external communications, or expanded permissions.

## Degraded operation

If isolated agents are unavailable, simulate lenses sequentially only when useful and label the run `sequential fallback`. Do not claim independence or anonymity that the system did not provide. Prefer separate model sessions or human reviewers for important decisions when available.

## Stop conditions

Stop or reframe when advisors rely on the same unverified premise, the brief is incomplete, further rounds add no evidence, the budget is exhausted, an upstream fact or tool fails, or unavailable specialist judgment controls the answer.

## Provenance

This is an original, vendor-neutral implementation inspired by Andrej Karpathy's LLM Council concept and Ole Lehmann's Claude Council adaptation. It does not imply endorsement by either creator.

