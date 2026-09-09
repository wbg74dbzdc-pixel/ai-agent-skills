# Authority and Safety

## Authority matrix

| Action | Default |
| --- | --- |
| Read repository and run safe diagnostics | Allowed within task scope |
| Make reversible local edits | Allowed only for implementation requests |
| Add or update dependencies | Ask unless clearly required and authorized |
| Use network or external research | Allowed when requested or required by policy |
| Write to external systems | Ask unless explicitly requested |
| Commit or open a pull request | Allowed when explicitly requested or established workflow requires it |
| Publish, deploy, merge, release, or message people | Ask unless explicitly requested |
| Spend money or accept legal terms | Always ask |
| Access or expose sensitive data | Use only when necessary and authorized |
| Destructive or hard-to-reverse action | Verify target and authority; ask if not explicit |

## Control principles

- Least agency: automate only as much as the task requires.
- Least privilege: expose only necessary repositories, paths, tools, identities, and data.
- Reversibility: prefer preview, diff, branch, backup, staging, and rollback.
- Bounded execution: define time, tool, cost, retry, and scope limits where runaway behavior is possible.
- Fail closed: when uncertainty could create material harm, stop and ask.
- Human checkpoints: require approval at meaningful irreversible or externally consequential boundaries.
