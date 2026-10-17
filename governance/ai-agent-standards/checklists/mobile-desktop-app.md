# Mobile and Desktop Application Checklist

Apply to native, hybrid, packaged, and installable applications. Pair with [Software Security](software-security.md) and [Product Release and Legal Review](product-release.md).

## Permissions, data, and platform boundaries

- [ ] Request each device or operating-system permission only when needed, explain its purpose in context, and handle denial or revocation gracefully.
- [ ] Store credentials and cryptographic material in platform-provided secure storage; exclude sensitive data from logs, clipboard, keyboard learning, screenshots, backups, notifications, and crash reports when relevant.
- [ ] Review deep links, URL schemes, inter-process communication, intents, extensions, plugins, WebViews, local sockets, and exported components for authentication and authorization flaws.
- [ ] Use least-privilege entitlements, capabilities, and filesystem access. Protect local databases, caches, temporary files, and backups.
- [ ] Verify TLS and platform trust behavior; do not ship debug certificates, test endpoints, developer menus, or production credentials.
- [ ] Make offline, synchronization, conflict, clock-change, interrupted-update, and account-switch behavior safe and understandable.
- [ ] Keep the app and bundled runtimes/dependencies updateable. Verify signed builds, update integrity, rollback, and supported-version policy.

## Accessibility and usability

- [ ] Support platform accessibility APIs: semantic names/roles/states, screen readers, text scaling, keyboard or switch navigation, visible focus, and accessible validation/errors.
- [ ] Respect system contrast, reduced-motion, captioning, input, and other accessibility settings where applicable; provide alternatives for visual, audio, color, and time-dependent cues.
- [ ] Test representative supported OS versions, devices, screen sizes, orientations, input methods, and assistive technologies.
- [ ] Provide understandable permission, privacy, account, deletion, error, and recovery flows.

## Store and release

- [ ] Check current platform review, payment, privacy declaration, age-rating, background activity, data-use, and signing requirements for each target store.
- [ ] Ensure store privacy/data-safety disclosures and screenshots describe the actual submitted build and its third-party SDK behavior.
- [ ] Test install, first launch, upgrade, interrupted upgrade, uninstall/reinstall, account recovery, and removal/deletion behavior.
- [ ] Verify crash reporting and analytics minimize data and honor user choices and applicable consent requirements.
- [ ] Keep a support contact, known-issues process, vulnerability-reporting route, and release/rollback owner.

For mobile security verification, consult the current [OWASP MASVS](https://mas.owasp.org/MASVS/) and its testing materials. For Apple distribution, check current [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and submission requirements; for other stores, use their current official publisher documentation.
