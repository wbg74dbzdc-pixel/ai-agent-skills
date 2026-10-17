---
name: claude-code-efficiency
description: Audit or improve Claude Code workflows to reduce unnecessary usage, context, tool calls, and rework while preserving correctness. Use when asked to optimize Claude Code usage, investigate usage limits, reduce prompt/context cost, review CLAUDE.md or skills, or automate repeated coding work.
---

# Claude Code Efficiency

Follow the vendor-neutral [Efficient Agent Workflow](../../governance/ai-agent-standards/playbooks/efficient-agent-workflow.md) and inspect only the active project's relevant setup.

## Audit sequence

1. Establish a baseline before changing settings: inspect recent usage and session/context breakdowns available to the user; use /context for the current context and /skill-doctor or /insights only if the installed version offers them. Record missing metrics as unknown.
2. Identify the dominant measured cost: long context, repeated reads, large command output, model/effort choice, subagent calls, retries, or rework. Do not optimize a category just because it sounds expensive.
3. Inspect always-loaded CLAUDE.md files, relevant .claude/rules, skill descriptions, enabled MCP servers/hooks, and recent task workflow. Read full skill content only for likely contributors.
4. Make the smallest change that addresses an observed cause:
   - move rarely needed reference material to a well-scoped skill;
   - remove duplicate or vague instructions and overlapping skill triggers;
   - use deterministic scripts/hooks for repeatable mechanical steps;
   - narrow searches, file reads, output limits, and delegated task inputs;
   - use subagents only for clearly independent work where isolation or a focused result justifies their separate model usage.
5. Verify behavior and compare with a similar task. Report changes to usage, context, retries, correctness, and maintenance separately. Do not promise a savings percentage without representative measured evidence.

## Session habits

- Send one bounded task brief with acceptance criteria, relevant paths, constraints, and exact checks.
- Continue the same chat for active related work. Use /compact with a handoff when continuing but reducing irrelevant history; use /clear for a distinct task after saving a verified handoff.
- Prefer concise tool output and preserved full logs. Never skip required source reading or tests merely to reduce usage.
- Check current [Claude Code best practices](https://code.claude.com/docs/en/best-practices), [commands](https://code.claude.com/docs/en/commands), and [extension/context guide](https://code.claude.com/docs/en/features-overview) because commands, account features, and pricing can change.
