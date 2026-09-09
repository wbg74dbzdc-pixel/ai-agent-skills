# Website Compliance Playbook

This is a risk-discovery and implementation checklist, not legal advice or a guarantee of compliance.

## Establish facts

- Identify operator, product, audience, jurisdictions, age restrictions, transactions, data collected, processors, hosting, analytics, advertising, embeds, cookies, and user-generated content.
- Inventory every form, tracker, SDK, payment flow, account feature, marketing claim, asset, and third-party service.

## Implement and verify applicable controls

- Privacy notice describing actual collection, purpose, sharing, retention, security, rights, and contact method.
- Terms and conditions consistent with the actual service.
- Confirm every policy, disclosure, permission request, and consent interface matches actual deployed behavior; do not ship generic legal boilerplate as if it were verified.
- Refund, cancellation, fulfillment, subscription, and warranty information where relevant.
- Cookie policy and consent controls where required; nonessential tracking must respect consent and withdrawal.
- Clear form purpose and consent; collect only necessary data.
- Secure transport, storage, access, deletion, export, backup, incident, and support handling.
- Accessible semantics, headings, labels, instructions, errors, keyboard navigation, focus, contrast, alt text, captions, and motion behavior.
- Clear button labels and no deceptive interfaces or dark patterns.
- Genuine reviews only; remove fake testimonials and unsupported claims.
- Accurate business identity and contact details.
- Verified rights or licenses for images, text, fonts, audio, code, datasets, trademarks, and generated assets.
- Review third-party embeds, processors, international transfers, platform rules, and applicable local law.
- Document AI-generated or AI-mediated experiences, automated decisions, provider data handling, human review, and correction or appeal paths where applicable.
- Substantiate explicit and implied marketing claims; disclose material relationships and preserve honest customer reviews.
- Record dependency, code, media, font, dataset, and generated-asset provenance plus required notices.

## Evidence and escalation

Record jurisdiction, applicable requirement, source, implementation, test, owner, status, and review date. Never invent legal language or state that the website cannot be sued. Flag unresolved or jurisdiction-specific questions for qualified legal review before release.

Complete the technical and operational checks in `website-launch.md` as a separate gate.
