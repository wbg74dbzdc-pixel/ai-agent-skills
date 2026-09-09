# Website Launch Playbook

Complete each applicable item in the deployed production-like environment. Record `pass`, `fail`, `blocked`, or `not applicable`, with evidence and an owner. This checklist does not guarantee legal compliance.

## Legal, privacy, and trust

- [ ] Publish a privacy notice that matches actual data handling.
- [ ] Publish accurate terms and conditions.
- [ ] Publish refund, cancellation, subscription, fulfillment, warranty, and business details where applicable.
- [ ] Inventory cookies, analytics, advertising, pixels, and embeds; implement consent and withdrawal where required.
- [ ] Collect only necessary data and present clear form purpose and consent.
- [ ] Substantiate claims, use genuine reviews, disclose material relationships, and remove deceptive patterns.
- [ ] Verify ownership, licenses, attribution, and notices for every asset and dependency.

## Security and forms

- [ ] Keep secrets, private keys, privileged tokens, and sensitive configuration out of frontend bundles, public repositories, logs, source maps, and downloadable assets.
- [ ] Enforce HTTPS and redirect HTTP; use secure cookies and appropriate transport and security headers, including HSTS where suitable.
- [ ] Validate forms on both client and server, encode output, protect state-changing requests, constrain uploads, and show accessible errors.
- [ ] Add proportionate spam and abuse protection such as rate limits, honeypots, verification, moderation, or accessible CAPTCHA alternatives.
- [ ] Verify authentication, authorization, session handling, account recovery, least privilege, dependency risk, backups, and rollback.

## Accessibility and responsive behavior

- [ ] Provide meaningful alt text for informative images and empty alt attributes for decorative images.
- [ ] Meet the project's contrast target and test more than the default visual state.
- [ ] Verify keyboard navigation, visible focus, semantics, labels, headings, errors, zoom, reduced motion, captions, and assistive-technology behavior.
- [ ] Test responsive layout, readable text, viewport behavior, touch target size, orientation, and critical workflows on representative mobile devices.
- [ ] Use WCAG 2.2 AA as the default web target unless a different applicable requirement is documented.

## Discovery, identity, and navigation

- [ ] Add unique, accurate page titles and useful meta descriptions.
- [ ] Add correct canonical metadata where duplicate URLs may exist.
- [ ] Add and test social preview metadata and an appropriately licensed preview image.
- [ ] Add favicon and applicable application icons or manifest metadata.
- [ ] Generate and validate sitemap and `robots.txt`; do not treat `robots.txt` as access control.
- [ ] Test internal and external links, anchors, redirects, navigation, and downloadable files.
- [ ] Provide a useful custom 404 page with navigation or recovery actions; handle other expected error states.
- [ ] Make the primary call to action clear without hiding necessary alternatives or using coercive design.

## Performance and media

- [ ] Compress images and use appropriate formats, dimensions, responsive sources, and lazy loading without harming essential above-the-fold content.
- [ ] Define and test page-load and interaction budgets on representative devices and constrained networks.
- [ ] Minimize unnecessary scripts, fonts, trackers, render blocking, layout shift, and oversized payloads.
- [ ] Verify caching and content-delivery behavior without caching private or stale-sensitive data incorrectly.

## Analytics, operations, and final proof

- [ ] Configure analytics only when justified; minimize collected data, honor consent, exclude secrets and sensitive fields, and test opt-out behavior.
- [ ] Verify production domain, DNS, certificates, environment variables, email delivery, monitoring, logging, alerts, backups, restore, and rollback.
- [ ] Test critical user journeys end to end, including empty, slow, invalid, offline, failure, and recovery states.
- [ ] Run automated accessibility, security, dependency, link, and performance checks plus required manual review.
- [ ] Produce a proof packet containing deployed version, results, screenshots or logs where useful, blockers, untested areas, owners, and final approval.
