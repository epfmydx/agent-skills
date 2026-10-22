# UI/UX Design Guide

A reusable guide for purposeful, distinctive, accessible interfaces.

Research snapshot: 14 October 2026. Includes selective 2025/2026 award evidence and current Apple HIG interpretation. Designed for people and agents; use it alongside implementation expertise, not as a mandate to redesign or copy a style.

## How to read it

Start with the user’s task and constraints. Choose the relevant sections; a small change should stay small. Award facts, inferred lessons, aesthetic preferences, and tested usability are different kinds of evidence. This guide supplies practical decision tools and testing templates, not proof that a proposed interface will work.

The modular agent skill is in `SKILL.md`, with focused references in `references/`. This consolidated edition contains the same guidance for convenient human reading. The references are canonical; `scripts/build_guide.py` refreshes this edition after reference changes.

## Using the package

- For reading or reference, start with this guide and select the sections relevant to your task.
- To use it with an agent immediately, provide the `ui-ux-design-guide` folder and ask the agent to read `SKILL.md` for your specific design task. Keep the `references` folder beside it so linked guidance remains available.
- When the skill is installed, use the host's supported invocation method or name it in your request. Codex, for example, supports `$ui-ux-design-guide`; other clients may differ. A development workflow can select it for relevant interface work. Installation and automatic discovery depend on the host.
- Example: “Use the UI/UX Design Guide to plan this workflow, then use the available implementation skill to build the approved direction. Preserve the existing design system and report what you actually tested.”
- For a scoped review, specify the task and available evidence: “Review only the search-to-detail flow. I have screenshots, not a working prototype. Separate visible issues from behavior that needs testing.”

## Contents

1. [Workflow design](#workflow-design)
2. [Visual craft](#visual-craft-without-fashionable-sameness)
3. [Apple and platform adaptation](#apple-guidance-and-platform-adaptation)
4. [Accessibility](#accessibility-as-a-design-constraint)
5. [Evaluation and templates](#evaluation-quality-gates-and-reusable-templates)
6. [Examples and invocations](#general-examples-and-realistic-invocations)
7. [Evidence and sources](#evidence-award-examples-and-source-limits)
8. [Working with other skills](#working-with-other-skills)

## Workflow design

### 1. Frame the job before the screen

Write a short design contract:
- Person: who is using it, what they know, and what they may find difficult.
- Situation: device, input, time pressure, interruptions, connectivity, and environment.
- Job: the outcome they need, phrased without naming an interface control.
- Stakes: consequences of delay, error, accidental disclosure, or incorrect automation.
- Success: an observable outcome and the evidence that will demonstrate it.
- Constraints: existing system, brand, content, technical limits, deadline, and permission boundaries.

Example: “An occasional visitor must compare two appointments, understand their local times and cancellation rules, and reserve the right one without losing entered details.” This is more useful than “make an elegant booking dashboard.”

For existing products, inspect actual content, support themes, analytics definitions, and known accessibility findings when authorized. Do not interpret a lack of complaints as success. If research is unavailable, state hypotheses and design a way to disprove them.

### 2. Model the task and information

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

### 3. Reduce uncertainty, not merely clicks

A shorter flow can be worse if it hides consequences or forces recall. Remove redundant decisions, repeated entry, and avoidable context switches. Keep helpful review steps where errors are costly. Reveal advanced settings at the point of need while keeping essential constraints visible before commitment.

Show what changed after an action. Distinguish saved locally, queued, syncing, and confirmed remotely. Do not display a final success state before the underlying operation succeeds. For long work, show progress when meaningful, explain what can happen next, and offer cancellation or background continuation where technically safe.

Use undo for genuinely reversible actions. For destructive or consequential actions, identify the affected object and consequences clearly. A confirmation dialog cannot compensate for ambiguous labels, misleading defaults, or an incorrectly scoped action.

### 4. Treat state coverage as a design artifact

For each important component or screen, specify applicable states:
- Initial, loading, ready, empty, filtered-empty, partial data, stale data.
- Focus, hover where supported, pressed, selected, expanded, disabled with reason.
- Validation failure, permission failure, connection loss, service failure, retry.
- In-progress mutation, success, cancellation, conflict, and recovery.

Not every component needs every state. Record “not applicable” rather than manufacturing complexity. Distinguish an empty account from a search with no matches: the first may need onboarding; the second needs query/filter recovery. Never conceal an error behind an endless spinner or misleading empty state.

Specify behavior as well as appearance: focus destination, keyboard interaction, announcement, retained data, retry semantics, and what happens after navigation or refresh. Prevent accidental duplicate submission while allowing recovery after failure. Coordinate idempotency and conflict handling with engineering; visual button disabling alone is insufficient.

### 5. Forms and content

Ask only for information needed now. Label fields persistently, expose required format before errors, and preserve valid entries. Use appropriate input types and autocomplete when useful. Do not use placeholder text as the sole label. Explain why uncommon or sensitive information is needed.

Validate when the user can act on the feedback. Avoid scolding while they are still typing an incomplete but potentially valid value. On submission, identify affected fields and provide a discoverable summary when needed. Use specific recovery language: “Enter a date after 14 October” is more useful than “Invalid value.”

Button labels should predict the next action. “Review order” and “Place order” signal different commitments. Include units, time zones, fee scope, and data freshness where they change interpretation. Localize grammar, layout, names, addresses, and formatting rather than translating isolated strings.

### 6. Dense operational interfaces

Density is useful when it supports comparison and frequent work. Remove decorative padding before removing information needed for a decision. Group rows by meaningful relationships; keep identifiers and crucial status visible. Use progressive disclosure for secondary detail, not to conceal exceptions.

For web tabular interfaces, choose between a semantic table with ordinary links/buttons and an interactive grid that manages focus within cells. Sort controls or row checkboxes alone do not require a grid. Prefer native table markup for ordinary tabular data; use a grid when the task needs its composite interaction model and implement its keyboard behavior deliberately. Consult the relevant [WAI-ARIA table](https://www.w3.org/WAI/ARIA/apg/patterns/table/) or [grid pattern](https://www.w3.org/WAI/ARIA/apg/patterns/grid/) before specifying keys, focus, and editing behavior.

Define bulk-action scope: selected rows, all visible results, or all matching records. Show affected count and filters. Handle partial failures per item and provide a safe next step. Do not silently discard selection when paging or change its meaning after filtering.

For dashboards, give every metric a question it answers and an action or interpretation it supports. Define time range, units, denominator, comparison period, freshness, and empty data behavior. A large number without context can mislead. Use tables for exact values, charts for meaningful relationships, and a concise summary for the main conclusion.

### 7. AI-mediated work

Distinguish suggestion, draft, pending approval, executing, and completed work. Show inputs, scope, editable assumptions, and evidence when they help someone judge correctness. Let people preview material changes before commitment and recover from mistakes where possible.

Do not invent numerical confidence, conceal uncertainty behind fluent language, or make a conversational interface replace efficient direct controls by default. Use conversation when expressing intent or iterating benefits from it; use structured controls for bounded selection, comparison, and precise editing. Preserve a readable record of consequential actions without exposing secrets.

Decide how cancellation, late results, stale context, partial completion, and model failure behave. Test whether users correctly understand what has and has not happened. An elegant generation animation is not evidence of trustworthiness.

For an agent that acts across several steps, make the following clear where relevant:

- **Before action:** expose the target, scope, and material parameters in a form people can inspect and correct. Reuse established authorization; require review or confirmation where the accepted policy and consequences call for it, without prompting for every harmless step.
- **During work:** show meaningful state, including waiting for input or an external result. Make background work findable and provide supported stop or redirect controls. Do not fabricate percentage progress or expose internal reasoning to explain activity.
- **After interruption:** distinguish “stopped future work” from “undid completed changes.” Show completed, pending, failed, and unconfirmed parts separately. Late responses must remain associated with the originating task rather than overwrite a newer one.
- **When correction is needed:** preserve usable input, allow focused edits or an available manual path, and explain what will be retried. Regenerating a draft and repeating an external action need different semantics. If the system hands work back, make the next actor and next step clear without promising unavailable support.

## Visual craft without fashionable sameness

### Start with a direction that fits the product

Describe the intended character with a few operational choices, not a collage of adjectives. “Editorial, image-led, generous reading space, quiet chrome” implies different decisions from “technical, compact, tabular, high-contrast status.” Existing brand and audience may make either inappropriate.

When direction is unresolved, sketch meaningfully different alternatives using the same content and task. Compare their hierarchy, readability, identity, implementation cost, and likely usability risks. Do not make arbitrary variants that change only accent color. For a narrow change, work within the established direction.

Aesthetic preferences are legitimate requirements when stated as such. “We prefer warm colors” is not equivalent to “warm colors improve completion.” Label taste, convention, hypothesis, and observed behavior separately.

### Composition and hierarchy

Make the screen's primary purpose apparent from its title, content order, and emphasized action. Establish a small number of visual levels through size, weight, position, whitespace, and contrast. If everything is prominent, the hierarchy has failed.

Use alignment and proximity to express relationships. Reserve boundaries, cards, shadows, and colored surfaces for meaningful grouping or interaction. A card is not automatically the correct container for every section. Large empty spaces can improve focus in one context and waste critical comparison space in another.

Choose layout from content and behavior. A narrow reading column, responsive gallery, dense table, split editor, and full-bleed canvas solve different problems. Avoid applying a marketing hero pattern to operational work simply because it produces an attractive screenshot.

Check the screen at a glance, then examine it at normal reading distance. What draws attention first? Does that match the user's next decision? This is an inspection heuristic, not a substitute for testing comprehension.

### Typography and rhythm

Use a coherent type system with purposeful roles: page title, section title, body, label, metadata, and numeric data where needed. Establish readable line height and paragraph spacing for actual content. A compact table and a long article need different rhythms.

Choose fonts for language coverage, legibility, identity, performance, and licensing. Use existing approved fonts when appropriate. Test realistic long headings, translated labels, numerals, missing data, and user-generated content. Do not rely on truncation for information required to choose safely; offer accessible full-value disclosure when truncation is necessary.

Use a small spacing vocabulary to improve consistency, then allow optically justified exceptions. A rigid grid is a tool, not a reason to make text awkward or targets difficult. Align repeated content by meaningful baselines and comparison axes.

### Color, surfaces, and iconography

Assign semantic roles to colors: background, surface, text, border, action, selection, error, warning, and success. Keep brand accent separate from status semantics. Test themes independently rather than assuming an inversion works. Do not communicate status through hue alone.

Evaluate text and controls against their actual backgrounds, including imagery, transparency, gradients, overlays, and interaction states. A beautiful palette with unreadable secondary text is unfinished. Avoid lowering contrast merely to make dense information feel calmer.

Use icons with recognizable meanings, consistent visual weight, and accessible names. Label unfamiliar or consequential actions in visible text when space permits. An icon's visual simplicity does not guarantee comprehension. Emoji and mismatched icon sets can undermine a deliberate system unless their informality is intentional.

### Imagery and content quality

Use imagery when it carries subject matter, emotional intent, spatial understanding, or useful preview. Prefer relevant imagery over generic decoration. Check crop behavior, focal points, text overlap, loading fallbacks, and accessibility alternatives. Do not misrepresent generated imagery as documentary evidence.

Use realistic sample content during design. Include a long name, an unusually large value, a missing image, a zero value, and a failed operation. Interfaces designed only around convenient demo text are not ready for production.

### Motion and interaction craft

Use motion to communicate cause, continuity, location, or progress. Avoid delaying a task so an animation can finish. Preserve the outcome when motion is reduced, and never make motion the only way to understand a change. Match feedback to action scale: a minor toggle should not compete with a serious alert.

Design focus, pressed, selected, and disabled states with the same care as the default state. These are different concepts and should not be visually collapsed. Avoid hover-only essential actions. Check pointer, touch, and keyboard interaction according to the supported platform.

### Responsive and technical restraint

Use content-driven layout changes. At narrow widths, decide what stacks, wraps, becomes a detail view, scrolls intentionally, or changes navigation. Do not merely shrink desktop text. Preserve task context and access to essential actions.

Define image sizes and placeholders to avoid disruptive shifts. Choose motion and effects within a realistic performance budget. If animation, blur, or large media undermines response on supported devices, reduce the effect or provide a lighter equivalent. Coordinate measurable performance targets with the implementation team rather than claiming a universal number is sufficient.

### Visual review questions

1. Can a person identify the purpose, current state, and next action?
2. Does emphasis correspond to task importance rather than decoration?
3. Do typography, spacing, imagery, and interaction states feel intentionally related?
4. Is the amount of information appropriate for the work?
5. Does the design retain character without borrowing another product's identity?
6. Do long content, narrow layouts, alternate themes, and accessibility settings still work?

Report specific defects and useful improvements. “Feels premium” or “looks modern” alone is not an actionable evaluation.

## Apple guidance and platform adaptation

### Choose the target platform first

Identify the target OS, supported versions, framework, input methods, and existing design system before choosing component conventions.

- Apple platforms: use the current HIG and relevant framework documentation; the Apple-specific sections below apply here.
- Android: consult current [Android design guidance](https://developer.android.com/design/ui/mobile) and [Android accessibility guidance](https://developer.android.com/design/ui/mobile/guides/foundations/accessibility), including the relevant Material component guidance when that is the product's system. Check navigation/back behavior, adaptable layouts, font scaling, semantics, and TalkBack. Preserve an established product system rather than imposing a new theme.
- Web: preserve semantic HTML, browser navigation, keyboard behavior, and applicable WCAG criteria. A mobile web surface still needs web semantics.
- Other platforms: consult their official component and accessibility guidance before recommending native interactions.

For Flutter, Ionic, or another cross-platform framework, identify whether each surface uses native controls, framework-rendered widgets, or web content. Verify the framework's accessibility mapping and target-platform behavior. Apple points, Android density-independent units, and CSS pixels are not interchangeable requirements. Carry task logic and identity across platforms; verify controls and assistive-technology behavior on each actual target.

### Current source interpretation

Checked 14 October 2026. Apple's general design-principles page identifies purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, and delight. Treat these as decision lenses: meaningful outcomes, user control, trustworthy behavior, recognizable patterns, varied needs, clarity, detail, and appropriate emotion. They are not a visual recipe. [Apple design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles/)

Apple's Liquid Glass guidance also emphasizes hierarchy, harmony, and consistency. Do not confuse that framing with the complete general-principles page. Standard framework components can adopt the new appearance; adoption does not inherently require redesigning the whole app. [Liquid Glass overview](https://developer.apple.com/documentation/technologyoverviews/liquid-glass)

Apple separates navigation/control materials from the content layer. It advises restrained custom Liquid Glass use, with standard materials for content; its regular and clear variants serve different legibility contexts. [Materials](https://developer.apple.com/design/human-interface-guidelines/materials)

### Operational application: original synthesis

For an Apple-native app, check the current HIG and API behavior for the specific component and supported OS versions rather than copying a promotional screenshot.

- iPhone: prioritize the compact, touch-based task and interruption/resume behavior.
- iPad: consider variable window sizes and both touch and keyboard/pointer work.
- Mac: preserve efficient windowed work, keyboard access, menus, and contextual actions.
- Watch, TV, and spatial platforms: investigate their actual interaction constraints separately. They are not resized phone screens.

These are design prompts, not a replacement for platform-specific HIG requirements. Check behavior on real supported configurations, including large text and assistive technology.

Keep product identity in content, typography choices permitted by the platform, imagery, tone, and task-specific structure. Use native components where they fit. Customize when the task warrants it, with explicit responsibility for accessibility, adaptation, and interaction states.

For a web application, preserve browser expectations, semantic HTML, links, navigation history, keyboard behavior, and responsiveness. Translate useful principles such as clear hierarchy and recovery; do not imitate native chrome or add translucency simply to appear Apple-like. Cross-platform coherence means recognizable identity and task logic, not identical controls everywhere.

### Material decision checklist

1. What relationship does the surface communicate?
2. Is it content, navigation, or a temporary control?
3. Can text remain readable over realistic moving content?
4. What happens in high contrast, reduced transparency, reduced motion, and alternate appearance?
5. Is a system component available for the target version?
6. Does the effect improve orientation enough to justify complexity and rendering cost?

If the answer is uncertain, prototype a simpler surface too and compare in the actual task. Do not claim that an award-winning glass implementation proves glass improves every interface.

### Version discipline

HIG pages evolve and some require JavaScript. Indexed primary-source text helped verify these pages; no hands-on device testing was performed for this guide. Before implementation, refresh the relevant guidance, SDK availability, and accessibility settings. Record the date and target versions. Avoid treating older “clarity, deference, depth” summaries as a complete account of current HIG.

## Accessibility as a design constraint

Accessibility should shape information structure, controls, and recovery from the beginning. Automated testing is useful, but passing a scanner is not proof that a workflow is usable or conforms to all applicable requirements. Use the relevant standard and platform guidance, plus manual and user testing.

### Selected web baseline checks

WCAG 2.2 is the reference standard used here. For a Level AA target, evaluate all applicable A and AA criteria across the relevant scope; this short checklist is not a conformance audit or legal determination. Check keyboard access, semantic relationships, labels, error identification, alternatives, resizing/reflow, focus visibility, and assistive-technology compatibility. [WCAG 2.2](https://www.w3.org/TR/WCAG22/)

- Text contrast: normally at least 4.5:1; large text can use 3:1. Large means at least 18 pt regular or 14 pt bold (approximately 24 CSS px or 18.67 CSS px). Exceptions exist for incidental text and logos; required labels are not decorative. Do not round a failing ratio upward. [Contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- Pointer targets: WCAG 2.2 AA generally requires 24 × 24 CSS pixels or a permitted exception, such as sufficient spacing. The exceptions need actual evaluation. This is a minimum criterion, not an ideal target for every context. [Target size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- Focus: at AA, an item receiving keyboard focus must not be entirely hidden by author-created content. A stronger design goal is to keep the entire focused control visible. Test sticky headers, banners, popovers, and dialogs. [Focus not obscured](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)

Native platform points and web CSS pixels are different units. Apple button guidance gives a general 44 × 44 pt hit-region rule, with 60 × 60 pt for visionOS; consult specific current platform/component guidance. Do not describe 44 px as a universal WCAG AA requirement. [Apple buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)

### Manual workflow checks: original testing protocol

Run the primary task without a mouse. Confirm a logical focus order, a visible focus indicator, operable controls, an escape route from overlays, and appropriate focus restoration. Verify that a visual change is also conveyed through the interface's accessible structure when necessary.

Use an appropriate screen reader to inspect headings, landmarks, names, roles, states, field instructions, validation, and asynchronous results. Test the complete task, not just a list of individually labeled buttons. Avoid over-announcing frequent updates that make the experience noisy.

Increase text size, zoom, and spacing; examine content at narrow widths. Essential information must remain available rather than being clipped behind fixed-height containers. Test long translations and right-to-left layouts if they are supported.

Check reduced-motion, contrast, and transparency preferences where applicable. Test status comprehension without color. Review images, charts, and media for equivalent information, including captions or transcripts when needed. In data visualizations, provide usable labels and an alternative means of accessing important values.

For authentication and forms, inspect avoidable memory demands, repeated entry, input assistance, and recovery. Offer inclusive input methods; do not assume everyone can drag precisely, hear audio, or interpret an unfamiliar symbol.

### Report honestly

Record platform, browser/OS, assistive technology and version, exact task, tested states, results, and unresolved barriers. Report “keyboard task passed in this environment” rather than “fully accessible.” Include users with relevant access needs in research when feasible; simulations and expert inspection do not reproduce their experience.

## Evaluation, quality gates, and reusable templates

### Separate four questions

1. Does it solve the right problem? Assess task fit and missing information.
2. Can intended users complete it? Assess understanding, errors, completion, and recovery.
3. Is it well crafted? Assess hierarchy, consistency, content, and visual execution.
4. Does it work reliably and accessibly? Assess implemented behavior, assistive access, supported environments, and failure states.

Do not collapse these into an unexplained “UX score.” A visually polished failure is still a failure. A functional prototype can still need craft work. Record confidence independently from severity.

### Evidence ladder

- Measured: observed task results or trustworthy analytics with definitions and context.
- Observed: a reproducible interface behavior or visible property in the available artifact.
- Inferred: a likely usability consequence needing validation.
- Preferred: an aesthetic or product-direction choice.
- Unknown: the available evidence cannot establish it.

An award is evidence of recognition under a particular judging process. A jury statement is attributed judgment. A vendor's outcome claim is a claim, not independently replicated measurement. Keep these distinctions visible.

### Proportionate quality gates

Before agreeing the direction:
- User, task, constraints, stakes, and success are explicit enough to choose.
- Main information and navigation reflect the job.
- Material tradeoffs and assumptions are visible.

Before implementation handoff:
- A coherent end-to-end flow exists with relevant non-happy states.
- Important controls have behavior, content, and accessibility expectations.
- Responsive/platform adaptations and realistic content cases are specified.
- Design choices work within the technical and existing-system constraints.

Before release or a “verified” claim:
- Critical paths and high-risk failure/recovery cases have been exercised.
- Relevant accessibility checks include manual work.
- Visual QA covers actual implemented states and supported layouts.
- Blocking failures are resolved or explicitly accepted by the responsible owner.
- Remaining uncertainty is documented, with a next step where warranted.

These gates scale to scope. A one-button fix may need just that button's states and the affected task. Do not demand a full redesign, research program, or deployment for an isolated recommendation.

### Verify selected-reference fidelity

Render the integrated interface in the actual application and compare it with the same selected reference/version under equivalent viewport, theme, content, interaction state, and loaded fonts. Inspect concrete discrepancies such as geometry, spacing, typography, color, and assets; exercise relevant transitions or inspect recordings for motion. When implementation is authorized, repair unintended differences and render again; for a review-only request, report the needed repairs. Record necessary adaptations and remaining differences. If repairs repeat without progress, reassess the cause and report the unresolved issue instead of continuing an unbounded loop. A source-code review or standalone prototype render alone does not verify integration fidelity.

Keep the selected reference as the baseline. Never automatically overwrite it with the implementation to make a comparison pass. Use task-appropriate visual judgment and any available comparison tools; no universal similarity threshold establishes acceptance, and no new tool or full design package is required for a small change.

Report fidelity separately from functional, accessibility, and real-data verification. If the source or browser is unavailable, name the missing evidence, mark the affected fidelity checks unverified, and continue other supported work. State the environments and states actually inspected; one browser viewport does not establish full device acceptance.

### Template: design brief

Product or feature:
Intended people and context:
Task and desired outcome:
Current friction and evidence:
Risk of error or misunderstanding:
Existing conventions to preserve:
Technical, content, brand, and time constraints:
Success criteria and proposed measurement:
Assumptions and open decisions:
Out of scope:

### Template: usability test plan

Decision this test will inform:
Participant characteristics relevant to the task:
Prototype/implementation version and environment:
Task scenario, in the person's language:
Starting state and realistic data:
Observable success condition:
Critical error definition:
Recovery scenario:
Neutral follow-up questions:
Metrics to capture:
Privacy/consent and recording plan:
Known limitations:

Write scenarios without naming the control the participant should discover. For example, “Find an available session next week that starts after your working day” rather than “Click the evening filter.” Obtain appropriate consent; do not upload private participant data casually.

Observe before explaining. Capture where the person hesitates, what they believe will happen, how they detect success, and how they recover. Do not equate silence with comprehension. Small exploratory studies reveal issues; they do not reliably estimate population conversion rates.

Choose metrics based on the decision: completion, critical errors, assistance, time on successful tasks, comprehension, confidence, or recovery. Define the denominator, start/stop rules, and comparison condition. Do not optimize time at the expense of accuracy for consequential work. Use a properly planned experiment for causal or statistical claims; a before/after change can have other causes.

For agent-mediated tasks, include an applicable interruption, uncertain result, or correction scenario. Observe whether people can identify the action's scope, distinguish a draft from completed work, and recover without an unintended repeat. Check control discoverability, keyboard/focus behavior, and accessible status updates in the implemented flow. Consider review and correction effort alongside completion time. Simulated users and AI reviewers can suggest gaps; they do not establish real-user understanding or accessibility acceptance.

### Template: finding

Title:
Affected task and location:
Evidence type: measured / observed / inferred / preferred / unknown
Evidence and reproduction steps:
User consequence:
Severity and rationale:
Confidence and limitations:
Smallest useful change:
Tradeoffs:
Acceptance test:
Owner/status, if applicable:

Suggested severity language: blocking (task cannot be completed or creates serious harm); major (substantial error or effort); moderate (recoverable friction); minor (small polish issue). Adapt to product risk. Do not assign numerical precision without a defined rubric.

### Template: interaction specification

Component or screen:
Purpose and content:
Entry conditions and permissions:
States and transitions:
Pointer/touch/keyboard behavior:
Accessible name, role, state, and announcements:
Focus behavior:
Validation and recovery:
Responsive/platform behavior:
Data freshness, persistence, and concurrency:
Acceptance tests:

### Template: verification report

Artifact/version:
What changed:
Environments and tools used:
Tasks/states tested:
Observed results:
Screenshots or recordings, if actually captured:
Untested conditions and why:
Unresolved issues and impact:
Recommendation: ready within tested scope / revise / more evidence needed

Never invent results to fill the template. If only a screenshot was available, say so and propose the behavioral checks that remain.

## General examples and realistic invocations

The prompts below use Codex's `$ui-ux-design-guide` notation as an example. In other environments, use the host's supported skill invocation or refer to the guide by name; the design tasks do not depend on that syntax.

All examples below are illustrative, not reports of measured user outcomes.

### Booking flow

Weak direction: remove the review screen because fewer screens must be easier.
Better decision: first identify the cost of selecting the wrong service, date, or location. If consequences matter, use a concise review showing those details and the final commitment. Preserve entries when editing. Measure correct completion and recovery, not only speed.

Visual approach: clear option comparison, subdued secondary details, strong date/time clarity, and one unambiguous final action. A distinctive brand can coexist with conventional form controls.

### Collection or editorial exploration

Weak direction: put every item in identical heavily bordered cards.
Better decision: let content type and browsing intent determine the layout. Rich imagery may deserve space; metadata can have quieter but readable hierarchy. Retain clear search/filter access and stable return context. Test finding a known item separately from exploratory discovery.

A visual collection interface is not evidence that image-led grids are appropriate for administrative records.

### Operational table

Weak direction: convert rows to large cards so the product looks modern.
Better decision: retain aligned fields when users compare many records. Improve headings, status semantics, row actions, selection scope, and detail access. On narrow screens, expose essential fields and provide accessible detail views rather than shrinking everything.

Test a representative comparison, a bulk operation, a partial failure, and keyboard navigation. A compact interface can be carefully crafted without imitating a consumer landing page.

### AI authoring tool

Weak direction: automatically publish generated output and briefly display a success toast.
Better decision: distinguish draft from approved content, show meaningful changes, preserve editing, and make publication consequences clear. Handle cancellation and partial results. Test whether people can explain what has been saved, shared, or only proposed.

### Native utility

Weak direction: add translucent surfaces to every panel after seeing an award winner.
Better decision: begin with supported system components, keep content readable, and customize only where the task benefits. Check current HIG and target SDK behavior. Assess reduced transparency and large text rather than judging only a promotional screenshot.

### Selected prototype in an existing application

Weak direction: rebuild a selected browser prototype with the application's usual cards and spacing, then call it complete because the controls work.
Better decision: inspect the selected version, preserve its compatible composition, typography, assets, and motion while integrating real components and data. Check the app's reset, font loading, tokens, and container styles when the result drifts. Compare the integrated screen with the reference at an equivalent viewport and state, repair discrepancies, and render again. Record any required accessibility adaptation and verify functionality separately. Use accepted permissions rather than treating a mock enabled button as permission policy.

### Invocation examples

“Use $ui-ux-design-guide to review this checkout flow. I only want the three most consequential usability issues. Keep the brand and layout unless the evidence calls for a change.”
Expected behavior: inspect the flow and evidence; prioritize task failures; label screenshot-only inferences; avoid a full rebrand.

“Use $ui-ux-design-guide to plan a responsive volunteer scheduling tool. Provide task flows, navigation, key states, and a lightweight test plan before implementation.”
Expected behavior: establish people and work context; create a coherent flow and realistic state coverage; define what validation would establish.

“Use $ui-ux-design-guide alongside our frontend implementation skill to build this approved design. Preserve the existing design system and flag only necessary accessibility or behavior fixes.”
Expected behavior: respect the approved direction; hand implementation concrete acceptance criteria; verify what was actually tested.

“Use $ui-ux-design-guide to compare two art directions for this reading app. Separate your aesthetic preference from evidence about reading and navigation.”
Expected behavior: compare the same content/tasks; discuss typography, hierarchy, identity, and tradeoffs; avoid invented usability rankings.

“Use $ui-ux-design-guide to adapt this iPhone feature for Mac. Keep its purpose and identity while using appropriate Mac interaction conventions.”
Expected behavior: inspect target platform guidance and task context; adapt behavior, window use, and input rather than scaling the phone screen.

### Behavioral evaluation cases for the skill

- Narrow request: “Change the error text only.” Pass if the agent fixes scoped content and mentions any genuinely necessary related issue without redesigning.
- Insufficient evidence: one static image and “prove this is easy to use.” Pass if the agent distinguishes visual inspection from behavioral proof.
- Trend pressure: “Make all our lab controls glass because Apple won awards.” Pass if it explains context and legibility tradeoffs without rejecting an explicit aesthetic preference outright.
- Dense work: a comparison-heavy desktop table. Pass if it considers preserving useful density instead of imposing spacious cards.
- Incomplete task: “Build a new app, no audience given.” Pass if it asks a material question or marks reasonable assumptions rather than fabricating research.
- Skill pairing: an existing frontend skill and approved component system. Pass if it adds workflow/state evaluation while preserving implementation ownership and the existing system.

## Evidence, award examples, and source limits

Research snapshot: 14 October 2026. This is a selective primary-source review across native apps, enterprise systems, and web interfaces, not an exhaustive ranking or a hands-on audit of the products. Award-year labels below follow the organizing body's record. Source text was reviewed through web retrieval; screenshots, live product behavior, and underlying studies were not independently evaluated.

### Verified examples, with bounded lessons

#### HP Veneer Design System — UX Design Awards, 2025

Evidence: the organizer's entry describes reusable components, tokens, and writing guidance. Its jury praises organizational enablement and cites faster development, savings, and adoption figures. Those figures are attributed claims, not independently verified results. [Official entry](https://ux-design-awards.com/winners/2025-2-hp-veneer-design-system)

Inference: a design system may need education, documentation, and adoption support as well as components. Test whether teams can successfully use the system; do not assume matching visuals alone produce efficiency.

#### Rijksmuseum Collection Online — Webby Awards, 2025

Evidence: the official record identifies both Webby Winner and People's Voice Winner for Best User Interface, credited to Fabrique & Q42. It does not provide causal usability metrics. [Official record](https://winners.webbyawards.com/2025/websites-and-mobile-sites/features-design/best-user-interface/333807/rijksmuseum-collection-online)

Inference: this is a relevant candidate for studying cultural-content discovery. Its award record alone cannot establish which layout patterns work, accessibility conformance, or superiority over alternatives.

#### Watch Duty — Apple Design Awards, 2025

Evidence: Apple names Watch Duty the Social Impact app winner and emphasizes clear, timely wildfire information and resources. [Apple announcement](https://www.apple.com/newsroom/2025/06/apple-unveils-winners-and-finalists-of-the-2025-apple-design-awards/)

Inference: urgency can make information clarity and reliability more important than decorative novelty. A lesson for another product still requires understanding that product's stakes and data quality.

#### LINQ — UX Design Awards Gold, Autumn 2026

Evidence: the jury explicitly awards Gold and praises the shift from device-centered laboratory control toward scientific workflows and system-wide consistency. [Official entry](https://ux-design-awards.com/winners/2026-2-linq-fully-integrated-lab-automation-platform)

Inference: organizing work around user intent can be more valuable than polishing existing technical categories. This is a hypothesis to validate, not permission to hide essential operational detail.

#### Moonlitt, Tide Guide, and Guitar Wiz — Apple Design Awards, 2026

Evidence: Apple names Moonlitt the Interaction app winner, Tide Guide the Visuals and Graphics app winner, and Guitar Wiz the Inclusivity app winner. Its descriptions highlight onboarding/platform integration, weather-data presentation, and accessibility features respectively. [Apple announcement](https://www.apple.com/newsroom/2026/06/apple-reveals-winners-of-the-2026-apple-design-awards/)

Inference: craft can serve orientation, comprehension, and access in different ways. No single surface treatment explains these awards or guarantees similar results elsewhere.

### How to use awards responsibly

Awards can reveal interesting work and the criteria a jury values. They cannot, by themselves, establish representative-user success, conversion uplift, causal effects, accessibility conformance, long-term retention, or suitability for a different domain. Entrant selection, judging criteria, platform incentives, public voting, and promotional presentation all limit generalization.

For each example, ask: What exactly is verified? What mechanism might transfer? What context differs? What could fail? What test would distinguish a good idea from an attractive imitation?

Do not describe “2025/2026 design” as a single style. The reviewed examples span cultural discovery, urgent information, enterprise infrastructure, laboratory workflows, and native utilities. Their useful common ground is purposeful execution, not a mandatory palette, font, corner radius, animation, or material.

### Design-fidelity sources

Selected sources reviewed 2026-10-22; this does not refresh the award snapshot above.

- [OpenAI, frontend designs](https://learn.chatgpt.com/use-cases/frontend-designs): supports comparing actual browser output with the reference and using existing components and tokens. This is practical guidance, not a measured fidelity guarantee.
- [Playwright, visual comparisons](https://playwright.dev/docs/test-snapshots): documents screenshot baseline comparison under the same environment. A regression tool can detect differences; it does not prove the target baseline is correct.
- [1D-Bench, version 3](https://arxiv.org/html/2602.18548v3), revised 2026-07-15: iterative feedback generally improves rendering success and often visual similarity on its fixed e-commerce React benchmark. It does not establish universal gains, accessibility, or production readiness.

The selected-reference authority, integration, and repair workflow in this guide is original synthesis informed by these sources, not a prescribed toolchain or a claim of benchmark-level results on other tasks.

### Primary guidance used elsewhere in this guide

Agent-interaction refresh, 2026-10-14:

- [Microsoft Design, UX design for agents](https://microsoft.design/articles/ux-design-for-agents/), 2025-04-11: informs visible state, control over background work, and appropriate uncertainty. This is vendor design guidance with some forward-looking capabilities, not a universal interaction standard or measured proof of usability.
- [Microsoft Learn, Human-centered design for agents](https://learn.microsoft.com/en-us/agents/design-guidelines/human-centered-design), updated 2026-05-21: informs scope refinement, editable outputs, contextual evidence, and correction. The readable article body was reviewed; Microsoft-specific Fluent UI and platform requirements are not imposed on other products. Its guidance does not replace testing with intended users.

The agent scenarios in the workflow and evaluation references are this guide's practical synthesis. They do not imply that every interface needs AI, extra confirmation screens, or a dedicated research programme.

- [Apple HIG design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles/)
- [Apple materials](https://developer.apple.com/design/human-interface-guidelines/materials)
- [Apple Liquid Glass overview](https://developer.apple.com/documentation/technologyoverviews/liquid-glass)
- [Apple buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [W3C contrast explanation](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- [W3C target-size explanation](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [W3C focus-obscuration explanation](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)

Refresh primary guidance before version-sensitive implementation or new award claims. If retrieval is incomplete, report the limit rather than filling gaps from memory. The workflow, evaluation templates, and design tradeoff guidance in this package are original synthesis, not official Apple or award-organizer requirements.

## Working with other skills

This guide works independently. When another skill or implementation capability is available, combine them around the requested outcome. Discover actual capabilities through the environment's catalog or configured locations; no particular frontend skill, client, installation path, or extra worker is required.

### Share responsibilities

- Business analysis establishes accepted outcomes, business rules, and unresolved policy decisions.
- This guide defines usable task flows, information hierarchy, interaction states, design tradeoffs, and acceptance criteria.
- Implementation capabilities realize the agreed direction in the project's stack and design system, with appropriate technical checks.
- Documentation preserves accepted decisions, relevant behavior, and verification evidence using project conventions.
- The coordinating workflow, when present, owns staffing, integration, and overall acceptance. Codex Dev Team is one optional example.

These responsibilities can be performed by one agent. Inspect the actual skills before assigning work; their coverage can overlap, and no fixed team is needed.

### Resolve overlapping guidance

Follow explicit user and repository requirements, existing product conventions, and relevant task/accessibility constraints before optional style defaults. Apply a specialized skill within its actual scope. When requirements conflict materially, explain the conflict and resolve it with the appropriate owner; do not silently replace an approved direction or ignore a required constraint.

For example, an implementation skill may favor a spacious promotional layout while the task is a dense operational screen. Keep the information and controls needed for repeated work, then use the skill's relevant visual techniques within that constraint. Preserve the user's chosen brand and platform.

### Preserve a selected reference

Identify the selected artifact and version from the request or available evidence: for example, a design file, browser prototype, component demo, or captured screen. Inspect the accessible actual artifact, including relevant states and assets, rather than relying only on a prose summary. Record which source/version governs the requested appearance and behavior. If source and screenshot disagree, use the user's specified authority; otherwise surface a material disagreement and resolve which version applies before changing the affected decision. Do not silently combine conflicting versions.

Within the accepted scope, the selected reference takes precedence over optional aesthetic defaults from other skills. Preserve explicit user and repository requirements and applicable accessibility constraints. Surface material conflicts and the smallest necessary adaptation; do not use a port as an opportunity to redesign the approved direction.

When moving a prototype into the product, preserve compatible layout, styles, assets, and motion. Adapt architecture, component boundaries, and data integration to the production stack. Inspect sources of drift such as CSS resets, fonts and weights, tokens, container widths, inherited styles, and existing components before replacing the reference's design choices. Mock interactions and data illustrate intent; they do not establish business rules or permission policy. Use accepted product rules for those decisions. For unspecified states, adapt existing conventions and state relevant assumptions.

### Keep the handoff concrete

Pass the task, intended people, accepted scope, relevant states, design-system constraints, and observable acceptance criteria. Include unresolved assumptions and evidence limits. Evaluate the implemented flow against the same criteria, including applicable accessibility and visual checks.

If an optional skill is unavailable, perform the supported work directly or report the specific capability gap. Do not install tools, launch workers, generate code for a research-only request, or publish merely because collaboration guidance is active.
