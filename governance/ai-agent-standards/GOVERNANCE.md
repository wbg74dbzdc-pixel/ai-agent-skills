# Governance

## Ownership

The user is the final owner of these standards. AI agents may research, draft, critique, test, and propose changes; they may not silently change governance or reduce protections.

## Rule requirements

A durable rule must have a clear scope, rationale, practical enforcement method, named decision owner, regression coverage for serious failures, and changelog entry for material changes.

Prefer deterministic enforcement—tests, linters, schemas, permissions, protected branches, scanners, and CI—over prose alone.

## Change process

1. State the observed problem or desired improvement.
2. Check for overlap or contradiction with existing rules.
3. Draft the smallest sufficient change.
4. Add or update evaluation cases.
5. Review effects across supported agents and project types.
6. Obtain the user's approval for material policy changes.
7. Version and record the accepted change.

## Exceptions

An exception must state its scope, reason, owner, start date, expiry or review date, affected safeguards, and compensating controls. Silence is not an exception.

## Precedence

1. Applicable law, platform requirements, and non-waivable safety constraints.
2. Explicit current instructions from the user.
3. Project-local instructions and authoritative decisions.
4. This universal standard.
5. Tool defaults and generic agent preferences.

More specific instructions control within their scope, but lower levels cannot silently weaken honesty, evidence, privacy, security, preservation, or owner authority.

## Versioning

- Major: breaking governance or adoption change.
- Minor: new compatible rules, playbooks, templates, or evaluations.
- Patch: clarification or correction without changed intent.
