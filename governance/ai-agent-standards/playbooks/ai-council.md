# AI Council

Use the Council to pressure-test consequential decisions that contain genuine tradeoffs. It is an escalation mechanism, not a substitute for ordinary reasoning, factual research, testing, professional advice, or the user's authority.

## Invocation

Run the Council when The user explicitly says `ask the council`, `council this`, `run the council`, `pressure-test this`, `stress-test this`, `war-room this`, or an equivalent instruction.

For a decision that is expensive, high-impact, highly uncertain, difficult to reverse, or likely to benefit from independent perspectives, recommend the Council and explain why. Obtain approval before incurring material agent, time, token, or monetary cost unless the current instruction already authorizes it.

Do not invoke it for routine implementation, straightforward factual questions, low-stakes reversible choices, emergencies where delay creates harm, or questions with no meaningful decision to compare.

## Preconditions

The lead agent must first pass the task-readiness gate and record:

- the actual decision and desired end state;
- the owner, success criteria, constraints, non-negotiables, and deadline;
- known facts, assumptions, unknowns, and authoritative sources;
- realistic options, including doing nothing or choosing a smaller experiment when relevant;
- the Council mode and resource budget.

If the framing is materially incomplete, ask focused questions before convening the Council.

## Modes

| Mode | Use | Minimum procedure |
| --- | --- | --- |
| Quick | Moderate-stakes, reversible decision | Three independent advisors; lead synthesis; no peer-review round unless disagreement or uncertainty warrants it |
| Standard | Consequential decision with real tradeoffs | Five independent advisors; anonymized peer review; one chairman synthesis |
| Deep | High-impact, costly, legally sensitive, safety-sensitive, or hard-to-reverse decision | Standard mode plus targeted research or specialist review, explicit disconfirmation, and independent verification of decisive claims |

Use the least expensive mode that matches the decision's risk. The user may select or override the mode.

## Standard advisor lenses

Assign the lenses independently. Adapt their domain expertise to the task without turning them into theatrical personas.

1. **Contrarian:** Find failure modes, weak assumptions, contradictions, second-order harm, and reasons the preferred option may fail.
2. **First Principles:** Reconstruct the problem from the actual goal, constraints, and fundamentals; challenge whether the question is framed correctly.
3. **Expansionist:** Identify overlooked upside, combinations, opportunities, and stronger variants without ignoring cost or feasibility.
4. **Outsider:** Review with minimal inherited narrative; surface obvious gaps, confusing assumptions, stakeholder effects, and questions insiders may miss.
5. **Executor:** Translate options into dependencies, effort, sequencing, operational burden, validation, rollback, and the next concrete action.

Use additional or substituted specialist lenses only when the decision requires them. Preserve at least one disconfirming lens and one execution-focused lens.

## Procedure

### 1. Independent analysis

- Give every advisor the same neutral decision brief, evidence packet, constraints, and output requirements.
- Do not expose other advisors' conclusions during the first round.
- Require each advisor to separate observations, sourced claims, estimates, assumptions, proposals, and unknowns.
- Require evidence or a verification method for decisive factual claims.
- Require practical feasibility, what would change the recommendation, and the strongest objection to the advisor's own conclusion.

### 2. Anonymized peer review

- Remove names and identifying persona labels; assign neutral identifiers.
- Have reviewers rank reasoning quality, evidentiary support, feasibility, and alignment with the actual goal.
- Ask reviewers to locate shared unsupported premises, correlated blind spots, omitted options, and contradictions.
- Peer scores guide synthesis but do not determine truth by vote.

### 3. Chairman synthesis

The lead or designated chairman must:

- reconcile duplicated arguments and factual conflicts;
- distinguish real consensus from a shared premise or shared-model bias;
- preserve material dissent and explain why it matters;
- compare options, tradeoffs, opportunity costs, and feasibility;
- identify claims requiring verification or qualified human review;
- recommend an option only when the evidence supports one;
- state what is lost by following the recommendation;
- give the smallest useful next action, validation step, and revisit conditions.

The chairman may return `insufficient evidence` or request a bounded experiment instead of forcing a verdict.

### 4. Verification gate

Before action, independently verify claims that materially control the decision. Council agreement is never verification. For legal, medical, financial, safety, privacy, security, or other high-stakes matters, follow the relevant specialist rules and escalate uncertainty appropriately.

### 5. Owner decision

Present the Council report to the user. They remain the final decision owner unless he explicitly delegates authority. A Council result does not authorize implementation, purchases, publishing, deployment, destructive changes, external communications, or expanded permissions.

## Degraded operation

If isolated subagents are unavailable, simulate the lenses sequentially only when useful and label the run `sequential fallback`. Do not claim independence or anonymity that the system did not provide. For important decisions, prefer separate model sessions or human reviewers when available.

## Failure and stop conditions

Stop or reframe when:

- the advisors rely on the same unverified premise;
- the decision brief is materially incomplete;
- additional rounds repeat arguments without new evidence;
- the budget is exhausted;
- an upstream fact or tool result fails;
- the answer depends on unavailable specialist judgment.

Use `templates/council-report.md` for the final artifact. Preserve the report with the relevant decision record when the result affects durable project direction.

## Provenance

This protocol is an original, vendor-neutral implementation inspired by Andrej Karpathy's LLM Council concept and Ole Lehmann's Claude Council adaptation. It does not imply endorsement by either creator.
