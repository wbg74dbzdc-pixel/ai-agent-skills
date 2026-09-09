# AI Agent Skills

Portable, vendor-neutral skills and public AI-agent operating standards for Claude, Codex, ChatGPT, Gemini, and compatible systems.

## Start here

A web-enabled agent can use this single public repository for both governance and reusable skills:

1. Read the [public AI Agent Standards](governance/README.md), beginning with the [universal constitution](governance/ai-agent-standards/AGENTS.md).
2. Load only the standards modules relevant to the current task.
3. Load any relevant reusable skill from the catalog below.

The public governance snapshot currently distributes **AI Agent Standards v1.3.0** from source revision `98b6475e8913b7918f3a472459d4fa2253027f77`. Its [version manifest](governance/VERSION.json) makes stale copies detectable.

Each skill lives in `skills/<skill-name>/` and uses `SKILL.md` as its entry point. Agents should load only the skill that matches the current task, then read linked references only when needed.

## Available skills

| Skill | Purpose |
| --- | --- |
| [`ai-council`](skills/ai-council/SKILL.md) | Pressure-test consequential decisions using independent perspectives, peer review, dissent-preserving synthesis, and verification. |

See [CATALOG.md](CATALOG.md) for triggers, boundaries, and compatibility notes.

## Installation

Clone the repository, then copy or link the desired skill directory into your agent's skill directory. Platform paths vary, so see [docs/installation.md](docs/installation.md). A capable agent can also read the standards and a skill directly from this repository when repository access is available.

## Design rules

- Skills must be portable and self-contained.
- Keep `SKILL.md` concise; put conditional detail in `references/`.
- Preserve user intent, authorization boundaries, and final decision authority.
- Do not include secrets, private project information, personal data, or unlicensed material.
- Distinguish facts, estimates, assumptions, proposals, and unknowns.
- Never treat model agreement as evidence; verify claims that control a decision.
- Check for duplicate or superseded guidance before adding or changing a skill.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). This repository is licensed under Apache-2.0; third-party adaptations must retain compatible licensing and attribution.
