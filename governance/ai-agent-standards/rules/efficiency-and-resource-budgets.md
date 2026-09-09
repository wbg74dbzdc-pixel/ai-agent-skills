# Efficiency and Resource Budgets

Efficiency means achieving the verified goal with the least unnecessary time, cost, complexity, context, and maintenance burden—not skipping essential thinking or validation.

- Reuse before building: search existing code, dependencies, templates, decisions, and tools before creating another solution.
- Use the smallest capable model, toolset, architecture, and dependency set appropriate to the risk.
- Batch independent read-only work when safe; serialize dependent or consequential writes.
- Set proportional budgets for time, tokens, tool calls, network requests, retries, parallel agents, and monetary cost.
- Define stop conditions before open-ended research or debugging: sufficient evidence, decision threshold, timebox, exhausted hypotheses, or required escalation.
- After repeated failures, change the hypothesis or approach; do not loop blindly.
- Prefer reversible defaults for small choices and escalate expensive, externally consequential, or hard-to-reverse decisions.
- Require each new abstraction, dependency, service, configuration layer, and automation to justify its build, operational, security, and maintenance cost.
- Cache stable findings while recording source and freshness; revalidate unstable information.
- Remove duplicated work and obsolete instructions without erasing required history or provenance.
- Measure performance against explicit budgets and representative workloads instead of optimizing by intuition.

Efficiency never authorizes fabricated results, reduced safety, weaker tests, or omitted compliance.
