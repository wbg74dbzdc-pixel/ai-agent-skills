# Efficient Agent Workflow

Use this procedure for Claude Code, ChatGPT, Codex, or another coding agent. Optimize for completed, verified work per unit of usage, time, and maintenance—not the fewest messages at any cost.

## Before the task

1. Select one bounded outcome. Write a short task brief with observable acceptance criteria, relevant paths, constraints, and exact verification commands. Use [the task-brief template](../templates/task-brief.md).
2. Read one current handoff or project-context record and verify its version, status, and key claims against current files or repository state. Do not load the history archive or whole project by default.
3. Inspect instructions, code, and evidence only along relevant entry points. Expand the scope when a result, dependency, or failure demonstrates that it is needed.
4. Prefer built-in search, repository CLIs, and existing scripts for simple work. Build a deterministic helper only when repeated work or reliable batching justifies the setup and maintenance.
5. Set a proportional budget for model requests, context, tool calls, parallel work, retries, and time. Define a stop/escalation point for open-ended debugging or research.

## During the task

- Use the primary agent by default. Delegate only a bounded, independent task when isolation, a specialist skill, or a concise report is worth the extra model requests. Subagents keep intermediate work out of the main context; they still use separate model input/output and can increase total usage. Do not spawn them for routine small tasks or as a default quota-saving tactic.
- Batch independent, read-only operations. Serialize dependent writes and review the resulting diff.
- For repetitive deterministic work, run a script or hook rather than asking a model to repeat it. Keep complete logs outside the prompt and return concise counts, exit codes, and actionable failures. Never suppress distinct errors to shorten output.
- Avoid rereading unchanged files, broad surveys without a decision need, large transcripts/logs, recursive delegation, and repeated status polling.
- Keep the current project state in its source of truth. Record verified outcomes and decisions as they happen; do not treat AI conversations or generated summaries as durable evidence.

## Session and context lifecycle

- Continue the current session while its context helps the unfinished task and its acceptance criteria remain active.
- Compact or checkpoint when useful context is being crowded by unrelated exploration or failed attempts. Preserve the task contract, verified state, exact files/commit, checks and results, blockers, and next action. Use [the compact handoff template](../templates/handoff.md).
- Start a fresh chat for a distinct task after a concise, verified handoff is available. Do not reset just because one response finished, nor keep a chat merely to avoid preparing a handoff.
- On resume, check the handoff against current files and Git state before relying on it. Treat stale or contradicted notes as leads only.

## Claude Code implementation

Claude Code commands and extension behavior can change. Check the installed CLI and current official docs before relying on version-dependent features. Useful current commands include /context to inspect context, /compact to summarize a continuing session, and /clear for a distinct fresh task. /skill-doctor and /insights may help review skill/context usage when available in the installed version. Record what the tool actually reports; these commands do not by themselves prove lower account usage.

Keep always-loaded project instructions short and stable. Put occasional procedures in narrowly scoped skills, path-specific rules, or scripts. Use hooks for deterministic actions that must happen on an event; limit hook output because it becomes model context. Audit skills for overlapping triggers, unnecessary always-on descriptions, redundant steps, and unused content.

## Measure the workflow

For representative comparable tasks, record:

- task type and completion/acceptance result;
- plan/session usage and context evidence available from the client;
- model/tool/subagent calls when exposed;
- verification results, retries, and rework;
- elapsed time and recurring script maintenance.

Compare like with like, account for task difficulty and correctness, and make one workflow change at a time. Do not claim savings from shorter prompts, a high cache hit, or a small context window alone. Review the [AI access and availability guide](../docs/ai-client-access.md) separately from task efficiency: a repository link does not guarantee a live client connection.
