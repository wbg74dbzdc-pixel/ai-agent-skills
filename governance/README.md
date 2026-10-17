# Public AI Agent Standards

This directory contains the canonical public AI Agent Standards. Skills are maintained separately under `skills/<skill-name>/`.

## How agents should use the standards

1. Read [the universal constitution](ai-agent-standards/AGENTS.md).
2. Read only rules relevant to the current task.
3. Use [the checklist router](ai-agent-standards/checklists/README.md) for software security, product type, accessibility, legal issue-spotting, and release readiness.
4. Use relevant playbooks, templates, and evaluation material when their workflow applies.
5. Then load any relevant reusable skill from the repository's [skill catalog](../CATALOG.md).

Do not treat a skill or checklist as a replacement for the universal standards. Project-specific instructions may add stricter requirements but may not silently weaken honesty, evidence, safety, privacy, preservation, or user authority.

## Provenance

- Current public standards version: **1.4.0**
- The standards and skills are maintained in this public repository; this repository is their source of truth.
- `VERSION.json` records the historical seed revision imported from the former private standards repository and the public snapshot transformations.
- Standards live under `ai-agent-standards/`; independently installable skills live under `../../skills/<skill-name>/`.

## Privacy and change control

Keep the public tree free of legal names, personal contact details, private paths, credentials, private project information, and account identifiers. Review the complete changed tree before each public update. GitHub account, commit, pull-request, and repository metadata are outside the control of document sanitization.

When standards change, update this repository's changelog and version manifest in the same change, review the full diff, run privacy/secret checks, validate internal links and checklist routing, and record the evidence. Do not treat a historical source revision as a live dependency.
