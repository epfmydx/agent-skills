# Workflow design

## 1. Frame the job before the screen

Write a short design contract:
- Person: who is using it, what they know, and what they may find difficult.
- Situation: device, input, time pressure, interruptions, connectivity, and environment.
- Job: the outcome they need, phrased without naming an interface control.
- Stakes: consequences of delay, error, accidental disclosure, or incorrect automation.
- Success: an observable outcome and the evidence that will demonstrate it.
- Constraints: existing system, brand, content, technical limits, deadline, and permission boundaries.

Example: “An occasional visitor must compare two appointments, understand their local times and cancellation rules, and reserve the right one without losing entered details.” This is more useful than “make an elegant booking dashboard.”

For existing products, inspect actual content, support themes, analytics definitions, and known accessibility findings when authorized. Do not interpret a lack of complaints as success. If research is unavailable, state hypotheses and design a way to disprove them.

## 2. Model the task and information

Identify entities, their relationships, vocabulary, status, and ownership. Distinguish the product's internal data model from the person's mental model. A technical system organized by servers may need a user interface organized by projects or outcomes.

Map the primary task as entry → orientation → action → feedback → outcome → continuation. Add alternate entry points, interruption/resume, no results, denied permission, and failure/recovery. Capture dependencies and irreversible transitions. A flowchart without state meanings is incomplete.

Prefer navigation labels that predict their destinations. Separate global navigation, within-item navigation, and task actions. Keep location apparent through headings, selected navigation, breadcrumbs when useful, and stable context. Preserve filters, scroll position, and selection when returning from detail views unless there is a clear reason not to.

Choose structure by work:
- Known-item lookup: search, relevant identifiers, filters, and recoverable zero results.
- Repeated comparison: aligned fields, sortable tables, explicit units and differences.
- Exploratory discovery: previews, useful grouping, recommendations with controllable criteria.
- Sequential high-stakes task: visible stages, review, correction, and clear final commitment.
- Expert repeated work: efficient bulk actions, shortcuts, saved views, and predictable density.

These are alternatives, not a mandate to add every feature.

## 3. Reduce uncertainty, not merely clicks

A shorter flow can be worse if it hides consequences or forces recall. Remove redundant decisions, repeated entry, and avoidable context switches. Keep helpful review steps where errors are costly. Reveal advanced settings at the point of need while keeping essential constraints visible before commitment.

Show what changed after an action. Distinguish saved locally, queued, syncing, and confirmed remotely. Do not display a final success state before the underlying operation succeeds. For long work, show progress when meaningful, explain what can happen next, and offer cancellation or background continuation where technically safe.

Use undo for genuinely reversible actions. For destructive or consequential actions, identify the affected object and consequences clearly. A confirmation dialog cannot compensate for ambiguous labels, misleading defaults, or an incorrectly scoped action.

## 4. Treat state coverage as a design artifact

For each important component or screen, specify applicable states:
- Initial, loading, ready, empty, filtered-empty, partial data, stale data.
- Focus, hover where supported, pressed, selected, expanded, disabled with reason.
- Validation failure, permission failure, connection loss, service failure, retry.
- In-progress mutation, success, cancellation, conflict, and recovery.

Not every component needs every state. Record “not applicable” rather than manufacturing complexity. Distinguish an empty account from a search with no matches: the first may need onboarding; the second needs query/filter recovery. Never conceal an error behind an endless spinner or misleading empty state.

Specify behavior as well as appearance: focus destination, keyboard interaction, announcement, retained data, retry semantics, and what happens after navigation or refresh. Prevent accidental duplicate submission while allowing recovery after failure. Coordinate idempotency and conflict handling with engineering; visual button disabling alone is insufficient.

## 5. Forms and content

Ask only for information needed now. Label fields persistently, expose required format before errors, and preserve valid entries. Use appropriate input types and autocomplete when useful. Do not use placeholder text as the sole label. Explain why uncommon or sensitive information is needed.

Validate when the user can act on the feedback. Avoid scolding while they are still typing an incomplete but potentially valid value. On submission, identify affected fields and provide a discoverable summary when needed. Use specific recovery language: “Enter a date after 14 October” is more useful than “Invalid value.”

Button labels should predict the next action. “Review order” and “Place order” signal different commitments. Include units, time zones, fee scope, and data freshness where they change interpretation. Localize grammar, layout, names, addresses, and formatting rather than translating isolated strings.

## 6. Dense operational interfaces

Density is useful when it supports comparison and frequent work. Remove decorative padding before removing information needed for a decision. Group rows by meaningful relationships; keep identifiers and crucial status visible. Use progressive disclosure for secondary detail, not to conceal exceptions.

For web tabular interfaces, choose between a semantic table with ordinary links/buttons and an interactive grid that manages focus within cells. Sort controls or row checkboxes alone do not require a grid. Prefer native table markup for ordinary tabular data; use a grid when the task needs its composite interaction model and implement its keyboard behavior deliberately. Consult the relevant [WAI-ARIA table](https://www.w3.org/WAI/ARIA/apg/patterns/table/) or [grid pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) before specifying keys, focus, and editing behavior.

Define bulk-action scope: selected rows, all visible results, or all matching records. Show affected count and filters. Handle partial failures per item and provide a safe next step. Do not silently discard selection when paging or change its meaning after filtering.

For dashboards, give every metric a question it answers and an action or interpretation it supports. Define time range, units, denominator, comparison period, freshness, and empty data behavior. A large number without context can mislead. Use tables for exact values, charts for meaningful relationships, and a concise summary for the main conclusion.

## 7. AI-mediated work

Distinguish suggestion, draft, pending approval, executing, and completed work. Show inputs, scope, editable assumptions, and evidence when they help someone judge correctness. Let people preview material changes before commitment and recover from mistakes where possible.

Do not invent numerical confidence, conceal uncertainty behind fluent language, or make a conversational interface replace efficient direct controls by default. Use conversation when expressing intent or iterating benefits from it; use structured controls for bounded selection, comparison, and precise editing. Preserve a readable record of consequential actions without exposing secrets.

Decide how cancellation, late results, stale context, partial completion, and model failure behave. Test whether users correctly understand what has and has not happened. An elegant generation animation is not evidence of trustworthiness.

For an agent that acts across several steps, make the following clear where relevant:

- **Before action:** expose the target, scope, and material parameters in a form people can inspect and correct. Reuse established authorization; require review or confirmation where the accepted policy and consequences call for it, without prompting for every harmless step.
- **During work:** show meaningful state, including waiting for input or an external result. Make background work findable and provide supported stop or redirect controls. Do not fabricate percentage progress or expose internal reasoning to explain activity.
- **After interruption:** distinguish “stopped future work” from “undid completed changes.” Show completed, pending, failed, and unconfirmed parts separately. Late responses must remain associated with the originating task rather than overwrite a newer one.
- **When correction is needed:** preserve usable input, allow focused edits or an available manual path, and explain what will be retried. Regenerating a draft and repeating an external action need different semantics. If the system hands work back, make the next actor and next step clear without promising unavailable support.
