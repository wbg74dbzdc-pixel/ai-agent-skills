# Public AI Agent Standards

This directory makes the complete active AI Agent Standards available to models that cannot access the private canonical repository.

## How agents should use it

1. Read [the universal constitution](ai-agent-standards/AGENTS.md).
2. Read only the rules and playbooks relevant to the current task.
3. Use the templates and evaluation material when their triggering workflow applies.
4. Then load any relevant reusable skill from the repository's [skill catalog](../CATALOG.md).

Do not treat skill instructions as a replacement for the universal standards. Project-specific instructions may add stricter requirements but may not silently weaken honesty, evidence, safety, privacy, preservation, or user authority.

## Provenance

- Public standards version: **1.3.0**
- The private `ai-agent-standards` repository remains the canonical source and history.
- The historical source revision is recorded in [VERSION.json](VERSION.json).
- Public standards live under `governance/ai-agent-standards/`; independently installable skills live under `skills/<skill-name>/`.

## Privacy and synchronization rule

The public bundle uses role-based terms such as `the project owner` and generic repository placeholders. Do not publish legal names, personal contact details, private paths, credentials, private project information, or account identifiers. Review the complete changed tree before each public update.


The private canonical repository remains the source of truth. Whenever it changes, a maintainer must regenerate this snapshot, run privacy and secret checks, compare the complete source file list, update `VERSION.json`, and update the public version shown here and in the root README. Generated snapshot files should not be edited independently.

If a known canonical revision is newer than the manifest, report the public snapshot as stale rather than guessing at missing rules.
