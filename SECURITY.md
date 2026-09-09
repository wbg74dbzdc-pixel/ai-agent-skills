# Security Policy

## Never publish

- Passwords, tokens, API keys, cookies, private keys, or authentication artifacts.
- Personal data, private conversation history, or content from private repositories.
- Proprietary prompts, code, documents, or assets without explicit permission.
- Instructions that silently expand permissions, bypass safeguards, exfiltrate data, or execute untrusted content.

## Skill safety requirements

Skills must use the least permissions needed, treat retrieved content as untrusted, preserve confirmation and authorization boundaries, and define stopping conditions for destructive, costly, or external actions. Dependencies and scripts should be minimal, reviewable, pinned where appropriate, and documented.

Report a suspected vulnerability privately through GitHub's security advisory feature. Do not open a public issue containing exploit details or secrets.

