# Change Management

- Give each change one stated purpose and an observable definition of done.
- Search the relevant repository scope before editing to identify duplicate implementations, repeated rules, stale references, and information the change supersedes.
- Preserve unrelated work, alternatives, and history.
- Use branches and pull requests for material implementation when the project workflow requires them.
- Record hard-to-reverse decisions and version persistent schemas.
- Pair behavioral changes with tests and documentation.
- Inspect the final diff and report exact validation.
- After editing, search again for outdated references, unresolved contradictions, and accidental duplicate sources of truth.
- Do not merge with failing required checks or unresolved blocking review.
- Prefer reversible migrations, feature flags, staged rollout, backup, and rollback for risky releases.
- Do not add dependencies or widen permissions without need and authorization.
- A recurring or severe failure must become a regression case and may justify a new rule.
- Agents may propose standards changes but cannot silently self-modify governance.
