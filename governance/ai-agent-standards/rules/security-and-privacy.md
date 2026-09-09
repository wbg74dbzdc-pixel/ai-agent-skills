# Security and Privacy

- Treat prompt injection, goal hijacking, malicious files, unsafe links, poisoned context, tool misuse, identity abuse, insecure inter-agent messages, unexpected code execution, and cascading failures as explicit threat classes.
- Validate intent before tool use and bind tools to the agreed task.
- Use least privilege and least agency; separate read, write, publish, deploy, and administrative capabilities.
- Sandbox or isolate untrusted code and content when possible.
- Validate inputs and outputs at trust boundaries.
- Require approval for high-impact operations and provide a preview or diff.
- Never expose secrets in prompts, logs, commits, screenshots, messages, or error reports.
- Minimize collection, access, retention, replication, and display of personal data.
- Define deletion, export, backup, recovery, breach, and support behavior where applicable.
- Audit significant actions with actor, time, target, reason, and result.
- Bound tool calls and detect unusual repeated or expanding actions.
- Fail closed when identity, target, authorization, or sensitive-data handling is ambiguous.

Security controls should be enforced through permissions, schemas, scanners, tests, and infrastructure—not entrusted solely to agent obedience.
