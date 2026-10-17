# Product Checklists

Use this page as a router. Do not load every checklist for every task.

These are risk-based engineering and issue-spotting baselines, not a promise of complete security, accessibility, or legal compliance. No single checklist can cover every product, threat, jurisdiction, audience, contract, or platform rule. Establish the product facts, identify what applies, and check current authoritative requirements before release.

## How to use

1. Record the product, release stage, supported platforms, user groups, jurisdictions, data flows, integrations, and business model.
2. Always use [Software Security](software-security.md) for software that handles user data, runs code, connects to a network, or is distributed to users. Scale its depth to risk.
3. Select only applicable product checklists below.
4. Complete [Product Release and Legal Review](product-release.md) before public release or a material change.
5. Record each item as `pass`, `fail`, `blocked`, or `not applicable`. Attach concise evidence, an owner, and a date. Explain every `not applicable`; unknown means `blocked`, not `pass`.
6. Track unresolved risks and decisions in the project's source of truth. Do not mark a release ready while a critical security, safety, legal, or platform blocker remains unresolved.

## Choose the relevant checklist

| Product or change | Read |
| --- | --- |
| Any software product | [Software Security](software-security.md) |
| Public API, backend, or network service | [API and Service Security](api-service.md) |
| Mobile or desktop application | [Mobile and Desktop Applications](mobile-desktop-app.md) |
| Website or browser-based product | [Website Launch Playbook](../playbooks/website-launch.md), plus Software Security and API checklist when applicable |
| Game, including online or live-service features | [Game Release](game.md) |
| Product with generative or agentic AI | [AI-Enabled Product](ai-enabled-product.md) |
| Public launch, monetization, user content, personal data, or regulated use | [Product Release and Legal Review](product-release.md) and the [compliance matrix](../templates/compliance-matrix.md) |

For a feature-only change, run the checklist sections affected by the change and record why untouched release gates remain valid. Re-run the full applicable set before first release and when product facts, data flows, jurisdictions, platforms, or major dependencies change.

## References

Use the standards linked inside each checklist as starting points, not substitutes for the complete current source. Record the version/date actually used. Security references include NIST SSDF, OWASP ASVS, OWASP MASVS, and OWASP API Security Top 10; web accessibility uses W3C WCAG; game accessibility includes Microsoft's Xbox Accessibility Guidelines. Platform rules and law must be checked for the actual target.
