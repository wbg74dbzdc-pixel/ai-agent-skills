# Game Release Checklist

Apply to standalone, mobile, browser, console, multiplayer, modded, and live-service games as applicable. Pair with [Software Security](software-security.md), [API and Service Security](api-service.md) for networked features, and [Product Release and Legal Review](product-release.md).

## Build, player experience, and accessibility

- [ ] Verify the release candidate launches and plays on every advertised platform, supported OS, input device, and minimum configuration.
- [ ] Test new save, load, migration, cloud sync, corrupted saves, low storage, disconnects, offline behavior, crashes, and recovery.
- [ ] Test accessible text size, contrast, captions/subtitles, color-independent cues, screen narration where feasible, remappable controls, input alternatives, difficulty/time options, motion/photosensitivity settings, and clear UI focus.
- [ ] Provide clear onboarding, pause/resume, settings, tutorials, content warnings where appropriate, and support information.
- [ ] Check localization, text expansion, input methods, currencies, dates, and regional content differences in target markets.
- [ ] Verify performance, frame pacing, memory, loading, thermal/battery impact, and graceful degradation on representative low-end and target hardware.
- [ ] Ensure store descriptions, screenshots, trailers, feature tags, early-access statements, and promised features match the shipped build.

## Ownership, licensing, and game terms

- [ ] Inventory material code, art, models, animation, audio, music, voice, writing, level/game design, fonts, datasets, third-party and AI-assisted/generated assets using the [rights and license inventory](../templates/rights-and-license-inventory.md).
- [ ] Verify written agreements or licenses for employees, contractors, co-developers, composers, artists, writers, publishers, and other contributors. Check pre-existing work, newly created work, ownership/assignment or permitted-use scope, credit, commercial rights, and delivery of editable/source files.
- [ ] Confirm commercial distribution and platform rights for every third-party asset, engine, plugin, marketplace item, open-source component, sample, and model output; retain required notices and satisfy license conditions.
- [ ] Review the current EULA/terms of service, store/publisher agreement, and any workshop/mod/UGC terms before enabling distribution. Distinguish your ownership of original game assets from the player's license to access and play.
- [ ] For mods, workshop submissions, fan content, and feedback, accurately state who owns submissions and which hosting, distribution, compatibility modification, derivative-work, sublicensing, monetization, removal, and post-removal rights are granted to the developer and platform.
- [ ] Flag any assignment or broad exclusive, perpetual, irrevocable, transferable, sublicensable, commercial, or derivative-work license for intentional scope review. Confirm it is limited to the rights needed and does not accidentally transfer the game or grant unrelated exploitation rights.
- [ ] Check contribution, modding, redistribution, monetization, takedown, and support rules against the actual platform terms and product behavior. Obtain qualified legal review for material or unclear rights transfers; don't rely on boilerplate or the “work made for hire” label alone.
- [ ] Do not promise players or contributors that their content remains exclusively theirs or that the game cannot be copied unless the agreements and law support that claim. No release checklist can prevent all copying or lawsuits.

## Security, online play, and player safety

- [ ] Keep authoritative state server-side for competitive or economically valuable multiplayer actions; treat clients, mods, and network messages as untrusted.
- [ ] Threat-model account theft, cheating, bots, griefing, harassment, matchmaking abuse, economy exploits, service denial, and unauthorized access.
- [ ] Protect accounts, sessions, lobbies, matchmaking, inventory, progression, trading, cloud saves, and purchases with server-side authorization and abuse controls.
- [ ] Secure chat, voice, user-generated content, mod distribution, and social features with appropriate reporting, blocking, moderation, privacy, escalation, and retention/deletion controls.
- [ ] Define moderation coverage and response for the actual risk and scale; do not promise safety capabilities that are not staffed or implemented.
- [ ] Secure patchers, launchers, anti-cheat, plugins, mods, downloadable content, and update channels. Explain invasive permissions and compatibility limits.
- [ ] Provide incident response, service status, rollback, backup/restore, exploit reporting, and a plan for discontinued online services.

## Monetization, age, and content

- [ ] Inventory purchases, subscriptions, ads, randomized rewards, virtual currency, trading, gifting, refunds, and cross-platform commerce.
- [ ] Disclose real prices, odds or probabilities where required, recurring charges, renewal/cancellation, platform-specific purchase restrictions, and what is included.
- [ ] Assess gambling, loot-box, consumer-protection, tax, age-verification, parental-consent, and regional restrictions with current jurisdiction-specific sources and qualified review when uncertain.
- [ ] Determine age ratings and complete platform content questionnaires accurately. Review user-generated content, chat, sexual/violent content, gambling themes, and sensitive depictions.
- [ ] If children or teens may play, assess age-appropriate design, privacy, communications, spending controls, parental tools, advertising, and safeguarding obligations; do not assume an age gate alone resolves them.

## Platform and launch gates

- [ ] Check the current official requirements for each store, console, launcher, rating authority, payment system, and accessibility-tag program.
- [ ] Complete applicable platform review, content surveys, privacy disclosures, age ratings, achievements/trophies, cloud saves, multiplayer, and commerce setup.
- [ ] Verify rollback, hotfix, version compatibility, save compatibility, player support, community moderation, and live-ops ownership.
- [ ] Record test coverage, known issues, unsupported configurations, launch monitors, escalation contacts, and go/no-go decision.

References: Microsoft's [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines) are best-practice guidance, not a legal compliance checklist. For Steam, check the current [review process](https://partner.steamgames.com/doc/store/review_process), [content survey](https://partner.steamgames.com/doc/gettingstarted/contentsurvey), and [Subscriber Agreement](https://store.steampowered.com/subscriber_agreement/). These platform examples do not replace requirements for other stores or target regions.
