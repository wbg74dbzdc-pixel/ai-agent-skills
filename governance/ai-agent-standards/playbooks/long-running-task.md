# Long-Running Task Playbook

Use a living execution plan and progress ledger for multi-hour, multi-session, or handoff-dependent work.

The ledger must record:

- task contract and source of truth;
- completed outcomes and evidence;
- current step and next concrete steps;
- decisions, rationale, assumptions, and unresolved questions;
- tests run and results;
- failures, dead ends, and recovery notes;
- changed files and current commit or version;
- permissions still required.

Work incrementally, leave the repository in a coherent state, and commit meaningful checkpoints when authorized. Before stopping, ensure a new agent can resume without reconstructing hidden context.
