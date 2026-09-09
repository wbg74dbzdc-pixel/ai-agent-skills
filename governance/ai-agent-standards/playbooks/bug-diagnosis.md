# Bug Diagnosis Playbook

1. Clarify expected behavior, observed behavior, impact, and environment.
2. Reproduce the failure or state why reproduction is unavailable.
3. Preserve logs and establish a minimal failing case.
4. Form hypotheses and list evidence that would distinguish them.
5. Test the cheapest, highest-information hypotheses first.
6. Identify root cause, contributing conditions, and blast radius.
7. If authorized to fix, make the smallest root-cause change and add a regression test.
8. Verify the original reproduction, adjacent behavior, and recovery path.

Do not implement a fix when the request authorizes diagnosis only. Do not present the first plausible explanation as the confirmed cause.
