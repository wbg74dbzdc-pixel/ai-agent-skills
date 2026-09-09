# AI Agent Standards

Canonical, cross-project operating standards for AI agents working on the user's projects and deliverables.

The goal is not a larger prompt. It is a reliable operating system: a short mandatory constitution, scoped rules, repeatable playbooks, reusable templates, deterministic enforcement, and regression cases for known AI failure modes.

## Start here

1. Read `AGENTS.md`.
2. Read the adopting project's instructions and source-of-truth documents.
3. Establish the task contract in `rules/task-readiness.md`.
4. Load only the rules and playbook relevant to the task.
5. Verify the result and complete a clean handoff.

## Repository map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Compact universal constitution loaded for every task |
| `GOVERNANCE.md` | Ownership, changes, exceptions, and versioning |
| `rules/` | Detailed requirements by concern |
| `playbooks/` | Task-specific operating procedures |
| `skills/` | Portable reusable agent skills that implement approved procedures |
| `templates/` | Cross-agent and project bootstrap files |
| `evals/` | Compliance rubrics and regression cases |
| `docs/research-sources.md` | Primary sources behind the standard |

## How projects adopt this standard

Every project repository should contain its own root `AGENTS.md`. It must:

1. adopt this baseline and pin the adopted revision;
2. identify local authoritative specifications;
3. add project-specific scope, architecture, validation, safety, and release requirements;
4. explain precedence between local and universal rules;
5. include compatible adapter files for the AI tools used by the project;
6. update deliberately when this standard changes.

A link alone is insufficient because an agent may not have cross-repository access. Keep an operative snapshot or generated adapter in each project.

## Core principles

- Understand the desired result before acting.
- Inspect reality; do not guess from memory.
- Separate evidence from confidence.
- Use the least authority necessary.
- Preserve source-of-truth history and owner intent.
- Prefer small, reversible, tested changes.
- Treat tests, schemas, linters, hooks, and CI as enforcement—not optional decoration.
- Make long-running work resumable.
- Never confuse AI consensus with proof.
- Never claim completion without evidence.

For consequential decisions, the optional AI Council in the repository's public `skills/ai-council/` and this snapshot's `playbooks/ai-council.md` provides structured independent review without replacing factual verification or the user's authority.

This repository remains private until The user explicitly approves publication.
