# Task Readiness and Task Contract

## Required gate

Before material implementation, establish:

- **Goal:** What end state should exist?
- **Context:** What problem, users, environment, and prior decisions matter?
- **Deliverables:** Exactly what must be created, changed, or reported?
- **Constraints:** What must be preserved, avoided, or kept compatible?
- **Authority:** Which reads, edits, external actions, and risk levels are authorized?
- **Source of truth:** Which files or systems govern the work?
- **Done when:** What observable criteria prove completion?
- **Verification:** Which tests, inspections, or reviewers will establish success?

Ask the owner for the end goal unless it is already explicit. Restate the contract and ask focused questions until no known unresolved issue could materially alter the implementation. If clarification materially shaped the contract, obtain confirmation before implementing.

## Avoid clarification theater

Do not delay work for preferences that are inconsequential, safely reversible, or governed by existing project conventions. State those assumptions. If the user explicitly requests immediate exploration or a prototype, the requested experiment may itself be the goal.

## Reopen the gate when

- evidence contradicts the agreed assumptions;
- scope or authority would need to expand;
- a destructive, costly, external, sensitive, or irreversible action appears;
- competing interpretations would produce materially different outcomes;
- the definition of done becomes impossible or unsafe.
