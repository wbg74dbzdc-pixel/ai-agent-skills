# AI-Enabled Product Checklist

Apply when a product uses generative models, classifiers, recommendations, autonomous agents, or model-assisted decisions. Pair with [Software Security](software-security.md), [Product Release and Legal Review](product-release.md), and API checks when exposed through a service.

## Data, model, and vendor boundaries

- [ ] Document model/provider, version, deployment location, data sent/received, retention/training terms, subprocessors, and fallback behavior.
- [ ] Do not send secrets, sensitive personal data, private source code, or customer data to a provider without an approved purpose, data basis, contract/settings, and user authorization where needed.
- [ ] Separate tenant/user data in prompts, retrieval, caches, logs, evaluations, and indexes. Enforce access control before retrieval and again before output.
- [ ] Define retention, deletion, export, correction, and incident handling for prompts, files, embeddings, fine-tuning data, and model outputs.
- [ ] Inventory model, dataset, plugin, tool, and supply-chain provenance and applicable rights, licenses, and restrictions.

## Threats and controls

- [ ] Threat-model direct and indirect prompt injection, poisoned retrieval/content, insecure output handling, sensitive-data disclosure, excessive agency, tool abuse, denial-of-service/cost attacks, and model/provider supply-chain risks.
- [ ] Treat model output and retrieved content as untrusted input. Validate schemas and authorization before using outputs in code, queries, markup, decisions, or actions.
- [ ] Limit tools to task-specific allowlists, scoped credentials, resource ceilings, sandboxing, and explicit approval for destructive, external, financial, or privacy-sensitive actions.
- [ ] Keep secrets and privileged instructions out of user-visible output and untrusted retrieval context; test for leakage and cross-session contamination.
- [ ] Make high-impact decisions reviewable by a competent human; define escalation, correction, appeal, fallback, and shutdown paths appropriate to impact.
- [ ] Protect users from foreseeable abuse, manipulation, unsafe advice, impersonation, and misleading claims. Clearly communicate material AI use and limits when appropriate or required.
- [ ] Set budget/rate limits, timeouts, retries, output bounds, moderation, and abuse monitoring to limit runaway costs and resource exhaustion.
- [ ] Make service failure or unavailable models degrade safely; do not silently substitute a model or capability that materially changes risk or behavior.

## Quality, evaluation, and release

- [ ] Define representative tasks, success thresholds, unacceptable failure classes, and human review criteria before launch.
- [ ] Test normal, adversarial, edge, multilingual, accessibility, privacy, security, and high-impact scenarios against the exact deployed configuration.
- [ ] Evaluate regressions, hallucinations, bias or disparate impact where relevant, prompt injection, tool authorization, data leakage, and refusal/appeal paths.
- [ ] Monitor quality, safety, abuse, cost, drift, vendor changes, and user reports without collecting unnecessary sensitive data.
- [ ] Version prompts, models, tools, policies, and evaluation sets; preserve rollback and incident containment ability.
- [ ] Reassess legal applicability for automated decisions, biometrics, employment, education, health, finance, children, consumer disclosures, and target jurisdictions.

Use the current [OWASP GenAI Security Project](https://genai.owasp.org/) guidance and the [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) as issue-discovery references. Check versions at the time of use; a top-10 list is not a complete control standard.
