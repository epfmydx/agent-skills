# Evaluation, quality gates, and reusable templates

## Separate four questions

1. Does it solve the right problem? Assess task fit and missing information.
2. Can intended users complete it? Assess understanding, errors, completion, and recovery.
3. Is it well crafted? Assess hierarchy, consistency, content, and visual execution.
4. Does it work reliably and accessibly? Assess implemented behavior, assistive access, supported environments, and failure states.

Do not collapse these into an unexplained “UX score.” A visually polished failure is still a failure. A functional prototype can still need craft work. Record confidence independently from severity.

## Evidence ladder

- Measured: observed task results or trustworthy analytics with definitions and context.
- Observed: a reproducible interface behavior or visible property in the available artifact.
- Inferred: a likely usability consequence needing validation.
- Preferred: an aesthetic or product-direction choice.
- Unknown: the available evidence cannot establish it.

An award is evidence of recognition under a particular judging process. A jury statement is attributed judgment. A vendor's outcome claim is a claim, not independently replicated measurement. Keep these distinctions visible.

## Proportionate quality gates

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

## Template: design brief

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

## Template: usability test plan

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

## Template: finding

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

## Template: interaction specification

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

## Template: verification report

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
