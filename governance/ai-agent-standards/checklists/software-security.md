# Software Security Checklist

Apply to software that handles user or business data, executes code, runs in a user environment, or communicates over a network. This is a baseline. Use a risk-based verification standard for stronger assurance; do not claim certification from this checklist.

## Scope and design

- [ ] Identify assets, sensitive data, trust boundaries, entry points, privileged actions, dependencies, deployment environments, and likely abuse cases.
- [ ] Create or update a lightweight threat model proportionate to impact. Include malicious users, compromised dependencies, insider mistakes, prompt/tool abuse where AI exists, and failure or recovery paths.
- [ ] Set security requirements and acceptance tests before implementing sensitive flows. Record explicit risk decisions and owners.
- [ ] Choose supported versions, secure defaults, minimum privileges, and a patch/support policy.

## Identity, authorization, and data

- [ ] Enforce authentication where needed and authorization on every protected action and object on the trusted side of the boundary.
- [ ] Test cross-user, cross-tenant, role-change, admin, account-recovery, logout, and revoked-session cases.
- [ ] Use established password, session, MFA, and cryptographic libraries; do not invent cryptography or expose secrets in client code.
- [ ] Protect secrets with managed storage, narrow scopes, rotation/revocation, and environment separation. Keep secrets out of source, builds, logs, crash reports, and test fixtures.
- [ ] Inventory and minimize sensitive data. Define purpose, access, encryption, retention, deletion, export, backup, and recovery behavior.
- [ ] Prevent personal data, credentials, tokens, payment data, and sensitive prompts from leaking through telemetry, analytics, URLs, logs, notifications, screenshots, or error messages.
- [ ] Use secure transport and appropriate at-rest protections. Document key ownership and recovery limits.

## Inputs, outputs, and execution

- [ ] Validate all inputs at trust boundaries with strict types, size limits, allowlists where feasible, and safe failure behavior.
- [ ] Use parameterized queries and context-aware output encoding. Prevent injection in databases, shells, templates, markup, file paths, and interpreters.
- [ ] Protect state-changing requests against forgery and replay where applicable; configure CORS, content security policy, cookies, and security headers deliberately.
- [ ] Treat uploaded, downloaded, imported, decompressed, rendered, and user-generated files as hostile. Limit size, type, path, archive expansion, and processing time; isolate parsers when practical.
- [ ] Restrict outbound network access and validate destinations to reduce SSRF, data exfiltration, and unsafe URL handling.
- [ ] Apply least privilege to processes, containers, plugins, extensions, permissions, filesystem access, and network access.
- [ ] Bound expensive work, retries, concurrency, storage, and third-party calls. Add abuse throttles and cost controls.
- [ ] Return safe errors without stack traces, internal paths, secrets, or sensitive records.

## Dependencies, build, and operations

- [ ] Pin and inventory direct and transitive dependencies; review provenance, license, maintainer health, known vulnerabilities, and update path.
- [ ] Run appropriate secret, dependency, static-analysis, and build-integrity checks in CI. Protect release credentials and production environments.
- [ ] Produce an SBOM when risk, customers, contracts, or regulation warrant it; retain artifact provenance and required notices.
- [ ] Separate development, test, staging, and production data and credentials. Never copy sensitive production data into tests without approved safeguards.
- [ ] Define secure configuration, patching, backups, restore tests, rollback, vulnerability intake, incident response, and end-of-life handling.
- [ ] Log security-relevant events with useful timestamps and actor/target context while excluding secrets and unnecessary personal data. Restrict and monitor log access.
- [ ] Verify access control, validation, failure, recovery, and migration behavior with automated tests; add manual testing or independent assessment when impact warrants it.

## Evidence and stop conditions

- [ ] Run checks against the release candidate and production-like configuration; record tool, version, scope, result, and known blind spots.
- [ ] Triage findings by exploitability and impact; assign owner and deadline. No critical unresolved security finding is silently waived.
- [ ] Document residual risk, mitigations, monitoring, rollback, and explicit risk owner for accepted non-blocking findings.
- [ ] Keep a private vulnerability-reporting path and a process for acknowledging, triaging, fixing, and disclosing issues safely.

## Reference baselines

- [NIST Secure Software Development Framework (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final) for lifecycle practices.
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) for web application security requirements and verification; pin the selected stable version.
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) is awareness material, not a substitute for a complete verification standard.
- Select sector, platform, and jurisdiction-specific controls based on product facts. Recheck source versions at each material release.
