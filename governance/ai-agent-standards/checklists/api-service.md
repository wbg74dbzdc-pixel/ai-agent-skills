# API and Network Service Security Checklist

Apply to public or internal APIs, backends, multiplayer services, webhooks, and other network interfaces. Pair with [Software Security](software-security.md) and applicable product checklists.

- [ ] Maintain an inventory of endpoints, versions, data classifications, authentication methods, owners, consumers, and deprecation dates.
- [ ] Authenticate callers where required and enforce object-, function-, and property-level authorization on every request; never trust client-supplied ownership or role fields.
- [ ] Validate schemas, content types, sizes, pagination, sort/filter fields, identifiers, and nested payload depth. Reject unexpected fields where appropriate.
- [ ] Apply rate, concurrency, and resource limits by account, key, IP, and expensive operation as appropriate; protect against scraping, brute force, enumeration, and denial of service.
- [ ] Use scoped, revocable credentials; avoid long-lived shared secrets. Verify webhook signatures, timestamps, replay protection, and idempotency.
- [ ] Restrict outbound requests and redirects; prevent SSRF through URL validation, DNS/IP controls, and network egress policy.
- [ ] Set deliberate CORS and cache behavior. Never publicly cache personalized or authorization-sensitive responses.
- [ ] Avoid leaking sensitive data in errors, logs, metrics, URLs, headers, traces, and analytics. Redact credentials and personal data.
- [ ] Protect uploads and downloads from malicious content, path traversal, archive bombs, unsafe previews, and unauthorized access.
- [ ] Define consistency, retry, timeout, pagination, duplicate-submission, and partial-failure behavior; fail safely without corrupting state.
- [ ] Use TLS, secure service identity, least-privilege service accounts, secret rotation, and separate environments.
- [ ] Test authorization boundaries, tenant isolation, injection, mass assignment, rate limits, replay, invalid/oversized input, and failure states.
- [ ] Monitor abuse and operational health with alerts, incident runbooks, backups, restore tests, and safe rollback.
- [ ] Review breaking changes, version support, deprecation notice, data migrations, and client compatibility before release.

Use the current [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) as a risk-discovery aid and a pinned [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) version for web service verification. Neither replaces a product-specific threat model.
