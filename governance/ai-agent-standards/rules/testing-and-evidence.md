# Testing and Evidence

Define success before implementation whenever practical.

- Use deterministic checks for objective behavior: tests, schemas, linters, formatters, type checks, builds, security scans, and artifact inspection.
- Use explicit rubrics for subjective quality.
- Include representative normal, edge, failure, adversarial, and recovery cases based on risk.
- Test the behavior changed, not merely the function touched.
- Never delete, weaken, skip, or rewrite a valid test solely to make a change pass.
- If a test is wrong, explain why and update it with evidence of the intended behavior.
- Verify generated documents and interfaces visually where layout matters.
- Benchmark performance claims under representative and credible worst-case conditions.
- For scalable systems, define budgets, bounded work, pathological cases, and graceful degradation.
- Log exact commands, environment, meaningful results, and untested areas.
- Convert serious or repeated failures into regression cases.

Prefer continuous evaluation against production-like cases over one-time demonstrations.
