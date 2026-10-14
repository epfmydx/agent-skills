# Requirements patterns

Use only patterns that resolve uncertainty or make verification clearer. Follow an existing project template when it already serves the purpose.

## Compact requirements brief

- **Outcome and actors:** what should improve, for whom, and how success will be observed.
- **Scope:** included behavior, exclusions, affected systems, and meaningful dependencies.
- **Current versus intended:** relevant differences, with a source for each material claim.
- **Rules and exceptions:** condition, actor, allowed action, result, and recovery.
- **Acceptance examples:** concrete inputs/context and observable expected outcomes.
- **Open decisions:** question, options or proposal when useful, impact of remaining unresolved, and decision owner if known.

Keep evidence status beside the claim: accepted requirement, observed behavior, proposed change, or assumption. A source can be a user statement in the task, an existing requirement identifier, a repository file, or a recorded decision; a separate source registry is unnecessary for a small assignment.

## Decision tables and permissions

Use a decision table when outcomes depend on several conditions. Expose gaps, overlapping rules, rule precedence, and exact boundaries. Identify which columns are accepted and which still need a decision.

Example of an incomplete approval requirement:

| Condition | Known rule | Decision still needed |
| --- | --- | --- |
| Amount below the stated limit | Manager may approve | Whether self-approval is permitted |
| Amount exactly at the limit | Unspecified | Which approval route applies |
| Amount above the limit | Finance approval required | Whether manager approval must happen first |

The table highlights missing rules; it does not authorize filling them in. Do not assume an approval hierarchy, currency conversion policy, rounding rule, or escalation deadline from a job title.

For permissions, distinguish the actor's role, organization/tenant, record ownership, delegated authority, action, and record state where applicable. Check denied cases as well as allowed cases. A role name alone may not establish access to every record.

## Process and state analysis

For each consequential transition, identify the trigger, preconditions, eligible actor, result, side effects, and failure/recovery behavior. Distinguish the business event from notification delivery or synchronization.

Examples of useful questions, selected by relevance:

- Does rejection finish the item, return it for editing, or allow resubmission? What happens to earlier approvals?
- Can a permission or record change while someone is acting on it? Which changes invalidate a previous decision?
- If an external system times out after possibly accepting a request, what outcome may the user be told, and what reconciliation is required?
- Are dates based on the user's local date, a business timezone, or elapsed time? Are boundary days included?
- Does a cancellation reverse the business effect, or only stop future processing? What remains in the audit history?

Describe the required business outcome and discuss feasibility with engineering. Do not prescribe database locks, a queue product, or a UI layout unless that choice is already an actual constraint.

## Acceptance examples and traceability

Use Given/When/Then, a table, or the repository's equivalent. Include enough context to distinguish the intended behavior from an accidental pass. Quantities, boundaries, roles, and dates should be concrete where the rule depends on them.

For an accepted rule that only a record's assigned reviewer may approve it:

- Given a pending record assigned to reviewer A, when reviewer A approves within the authorized scope, the record becomes approved and the decision is attributed to A.
- Given the same record, when an unassigned reviewer attempts approval, approval is denied and the record remains pending.
- If reassignment during review is unspecified, record it as a pending rule and keep the related expected outcome proposed until resolved.

Include applicable error, duplicate-action, partial-success, and recovery cases. Requirements may describe observable outcomes without specifying the internal mechanism. Link important examples to their rule or decision so later changes reveal affected tests, guides, and integrations. Use stable identifiers when the feature is large enough to need them; do not add identifiers to every tiny wording change.

## Scope changes and handoff

When a new request changes accepted requirements, show the specific change and its effects on scope, rules, acceptance examples, and dependencies. Preserve unrelated decisions. The existing authorization may already cover the change; do not add a ceremonial sign-off step.

Distinguish unresolved business policy from an implementation choice the team can make. Report blocking questions together, keep optional improvements separate, and continue work that does not depend on an unanswered policy. A complete-looking brief with invented decisions is not a completed analysis.
