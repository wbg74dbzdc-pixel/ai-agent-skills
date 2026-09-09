# Context and Memory

Context is finite. Use the smallest high-signal set of instructions and evidence sufficient for the task.

- Keep the root agent file short and route details to scoped rules.
- Load project and path-specific instructions only when relevant.
- Prefer reusable playbooks or skills for procedures instead of repeating them in every prompt.
- Treat memory and summaries as provisional context; reconcile them with current authoritative files.
- Detect stale dates, superseded decisions, contradictions, and duplicated guidance.
- Before adding information, search the full relevant repository scope—not only the currently open file—for equivalent, overlapping, conflicting, or older statements.
- When new evidence makes prior information outdated, update all active references or mark them explicitly superseded with a pointer to the current source.
- Consolidate true duplicates into one authoritative location and replace repeated copies with links or generated adapters where practical.
- Preserve useful historical reasoning in version control, decision records, or an archive; do not leave obsolete guidance active merely to preserve history.
- Do not store secrets, sensitive personal data, or transient guesses in durable memory.
- Record durable project facts in repository artifacts, not only agent memory.
- Summarize long tasks into a progress ledger before context is likely to be lost.

When instructions conflict, identify the conflict and apply `GOVERNANCE.md` precedence. Do not silently choose whichever instruction is most convenient.
