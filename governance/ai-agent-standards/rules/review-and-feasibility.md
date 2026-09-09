# Review and Feasibility

Every serious review has two independent tracks: whether the idea is valuable and whether it can be implemented safely, reliably, performantly, and within scope.

For uncertain claims, define:

1. the exact question;
2. the evidence and current hypothesis;
3. plausible counterexamples or disconfirming evidence;
4. a representative prototype or test;
5. the environment and credible worst case;
6. measurable pass/fail thresholds;
7. observed results;
8. the decision and remaining uncertainty.

Implementation reviews should examine state ownership, determinism, schemas and migration, bounded work, failure recovery, observability, security, privacy, accessibility, licensing, operational burden, and maintenance cost.

Every substantial recommendation must include a feasibility card stating:

- estimated complexity and effort range, with the basis for the estimate;
- monetary and ongoing operational costs;
- required skills, people, infrastructure, permissions, and dependencies;
- major risks, unknowns, and credible failure modes;
- the smallest representative prototype or validation step;
- a simpler fallback or phased option;
- conditions that would make the recommendation no longer worthwhile.

Do not recommend enterprise-scale architecture for a small problem without demonstrating why its benefits exceed its implementation and maintenance costs.

Do not upgrade `proposed` to `proven` because multiple agents repeated the same assumption. Label decisions such as `OPEN`, `LOCKED`, `ACCEPTED`, `REJECTED`, or the project's equivalent, and carry unresolved dependencies forward.
