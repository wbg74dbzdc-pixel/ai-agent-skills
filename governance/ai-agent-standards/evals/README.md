# Evaluations

Evaluate agent behavior across four dimensions:

- **Outcome:** Did the requested end state actually exist?
- **Process:** Did the agent respect scope, authority, source of truth, and required checks?
- **Style:** Was the result clear, concise, useful, and honest about uncertainty?
- **Efficiency:** Did the agent avoid unnecessary context, tools, retries, dependencies, and fan-out?

Use deterministic checks for objective requirements and rubrics for judgment. Include typical, edge, adversarial, failure, and recovery cases. Run evaluations before and after material instruction changes and convert repeated real failures into permanent regression cases.

Passing prose review does not override a failing deterministic check.
