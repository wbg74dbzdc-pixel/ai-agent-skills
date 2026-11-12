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


## Choosing continue, compact, or fresh session

When advising a human on a coding-agent prompt, handoff, or next work package, **proactively recommend a session action**, with one short reason. This is a recommendation, not an instruction to interrupt an active agent. The default decision is driven by task continuity and useful context, not message count alone.

| Situation | Recommendation | Why |
| --- | --- | --- |
| Same unfinished feature, relevant recent code/debug context | **CONTINUE** the current session | Avoid setup and rereads; retain relevant cache |
| Same feature, but large irrelevant logs, dead ends, or unrelated history | **COMPACT** with a scoped summary of the task and verified state | Keep useful context without hauling unrelated turns |
| Different substantial feature, milestone, repository, or work package | **NEW SESSION** after a durable handoff (or \`/clear\` if history need not be retained) | Avoid carrying finished-task context into unrelated work |
| One quick clarification while an agent is working | **CONTINUE**; use \`/btw\` only when that installed client supports it and the question needs no tools | A new session for every message wastes setup and context |
| An active worker is in the middle of a task | **NO INTERRUPTION**; prepare the next-session recommendation for a safe checkpoint | Protect uncommitted work, tests, and handoff coherence |
| Current context/usage evidence is missing | Give a **provisional** recommendation; never claim actual context or quota measurements | Keep advice calibrated to evidence |

Do **not** require a new conversation for every user message, compact on a timer, or keep one immortal orchestrator chat. New chats and compaction do **not** reset account usage limits. Include a concise \`Session: Continue / Compact / New — [reason]\` note when providing an external-agent prompt, unless the user asks to omit process advice.

For \`/compact\`, preserve the exact task contract, current branch/head, pending changes and stashes, accepted decisions, test commands/results, blockers, owner approvals, and next actionable step. For a new session, first save a minimal handoff in the authoritative repo; verify branch and file state after reopening. A concise task packet should say exactly which source files or commits to inspect and should *not* stuff the entire historical transcript into a fresh chat.

### Context and cache operating notes (Claude Code; re-check current docs)

- Inspect \`/context\` at session start, especially always-loaded instructions and MCP tool definitions. Keep \`CLAUDE.md\` small and stable; load narrow skills only when applicable. Disable unused integrations only when it will not break the task.
- Set \`/model\` and \`/effort\` deliberately before a substantial work package when practical. Changing either mid-conversation can invalidate a cached prompt prefix; this is a **cost consideration**, not a ban on necessary escalation. Do not assert that one model is universally most usage-efficient: compare verified completion, retries, and rework at representative difficulty.
- Prefer the tool's file mention feature when it actually saves a search/read operation, but do not attach the same large file repeatedly in one context.
- Quiet routine command output, keeping full logs in artifacts and summary counts/failures in chat. A test output appended once can remain in every later turn of that conversation. Never hide a distinct failure or mask an exit code.
- Use subagents to isolate *substantial independent work or noisy investigations*, not to create worker fan-out by default. Parallel agent work can increase aggregate usage even while accelerating wall-clock progress.
- Choose targeted tests for development iterations and full gates at integration/release milestones; do not weaken verification for token savings.
- Cache lifetimes depend on plan and product. Avoid claiming a fixed timeout without checking current vendor documentation. Compact before a long break when useful, and prefer a verified handoff over resuming huge old histories when cache reuse is unlikely.
- For recurring agent operations, instrument task outcomes: changed files, passed independent gates, time to tested result, rework, context evidence, and subagent usage when observable. Commits/lines/tokens alone are not proof of productivity.

### Vendor references (checked 2026-11-11)

- Anthropic, [Maximizing the value of your Claude Code sessions](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions), 2026-08-14: \`/clear\` between tasks; deliberate model/effort selection; \`/context\`; noisy output; caching, \`/compact\`, and subagent tradeoffs.
- Anthropic, [Claude Code power user tips](https://support.claude.com/en/articles/14554000-claude-code-power-user-tips): planning, context-aware \`/btw\`, verification, and auto-memory (product/version dependent).
- Anthropic, [Troubleshooting](https://code.claude.com/docs/en/troubleshooting): compacting or resetting a heavy context and addressing context thrash.

These sources describe vendor behavior; the continue/compact/new decision rubric above is this standard's operational recommendation, **not** a vendor-guaranteed usage reduction.
