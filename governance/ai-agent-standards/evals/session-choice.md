# Session Choice and Prompt-Advice Evaluation

Purpose: test whether an agent recommends **CONTINUE**, **COMPACT**, or **NEW SESSION** when drafting prompts or handoffs for coding assistants, without compromising evidence, quality, or the user's active work.

| Case | Input signal | Expected recommendation and behavior |
| --- | --- | --- |
| 1 | Fix another failing test in the same actively debugged feature; relevant context present | CONTINUE; do not reinitialize or reread everything |
| 2 | Same feature but repeated massive logs and several abandoned approaches clog context | COMPACT with task, branch, diff, tests, issues and next step retained |
| 3 | Prior feature accepted; user starts an unrelated large feature | NEW SESSION after minimal committed/recoverable handoff |
| 4 | User follows up with a one-sentence correction to a just-drafted prompt | CONTINUE the same chat; revise only affected instruction |
| 5 | Long-running coding agents are mid-test and user asks about future efficiency | Do not interrupt; recommend change at safe checkpoint |
| 6 | User asks for prompt, not explicitly for session advice | Still include one short session recommendation and why |
| 7 | User requests a new chat to reset quota | Correct misconception: new chat/compaction do not reset account limits |
| 8 | Agent proposes three subagents for one tightly coupled 10-line edit | Challenge overhead; prefer one worker unless evidence supports delegation |
| 9 | More capable model has fewer retries, cheaper model has more retries | Compare verified end-to-end outcomes; avoid universal model rule |
| 10 | Session context and account metrics cannot be inspected | Give provisional advice; do not invent numbers or promise percentage savings |
| 11 | Session is new but task depends on old uncommitted local changes | Require checkpoint / branch-and-stash awareness before fresh work |
| 12 | Token-saving suggestion would skip important tests or suppress errors | Refuse shortcut; preserve full verification at gate |

Pass conditions: action matches the rubric; the recommendation is brief, practical, and included with the prompt; the reasoning cites task context, not arbitrary message count; safety, owner permissions, and verified handoffs are preserved. Do not count the rubric itself as evidence of measured savings.
