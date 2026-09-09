# Installation

Install only the skills you need. Keep the repository as the update source rather than copying instructions into many unrelated places.

## Claude

Place or link a skill directory where your Claude environment discovers skills, or attach the selected `SKILL.md` and its referenced files to a project. If the environment cannot access GitHub, download the repository once and add the local folder to the project.

## Codex and compatible agents

Copy or link `skills/<skill-name>/` into the agent's configured skills directory. Preserve the directory name and linked references. Restart or refresh skill discovery when the host requires it.

## Direct use

An agent with repository access may read `skills/<skill-name>/SKILL.md` directly. It should load linked references only when the current task needs them.

Platform paths and discovery rules change. Follow the current official documentation for the host, and record any confirmed platform-specific steps in a focused compatibility note rather than embedding them in every skill.

