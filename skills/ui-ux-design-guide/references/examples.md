# General examples and realistic invocations

The prompts below use Codex's `$ui-ux-design-guide` notation as an example. In other environments, use the host's supported skill invocation or refer to the guide by name; the design tasks do not depend on that syntax.

All examples below are illustrative, not reports of measured user outcomes.

## Booking flow

Weak direction: remove the review screen because fewer screens must be easier.
Better decision: first identify the cost of selecting the wrong service, date, or location. If consequences matter, use a concise review showing those details and the final commitment. Preserve entries when editing. Measure correct completion and recovery, not only speed.

Visual approach: clear option comparison, subdued secondary details, strong date/time clarity, and one unambiguous final action. A distinctive brand can coexist with conventional form controls.

## Collection or editorial exploration

Weak direction: put every item in identical heavily bordered cards.
Better decision: let content type and browsing intent determine the layout. Rich imagery may deserve space; metadata can have quieter but readable hierarchy. Retain clear search/filter access and stable return context. Test finding a known item separately from exploratory discovery.

A visual collection interface is not evidence that image-led grids are appropriate for administrative records.

## Operational table

Weak direction: convert rows to large cards so the product looks modern.
Better decision: retain aligned fields when users compare many records. Improve headings, status semantics, row actions, selection scope, and detail access. On narrow screens, expose essential fields and provide accessible detail views rather than shrinking everything.

Test a representative comparison, a bulk operation, a partial failure, and keyboard navigation. A compact interface can be carefully crafted without imitating a consumer landing page.

## AI authoring tool

Weak direction: automatically publish generated output and briefly display a success toast.
Better decision: distinguish draft from approved content, show meaningful changes, preserve editing, and make publication consequences clear. Handle cancellation and partial results. Test whether people can explain what has been saved, shared, or only proposed.

## Native utility

Weak direction: add translucent surfaces to every panel after seeing an award winner.
Better decision: begin with supported system components, keep content readable, and customize only where the task benefits. Check current HIG and target SDK behavior. Assess reduced transparency and large text rather than judging only a promotional screenshot.

## Invocation examples

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

## Behavioral evaluation cases for the skill

- Narrow request: “Change the error text only.” Pass if the agent fixes scoped content and mentions any genuinely necessary related issue without redesigning.
- Insufficient evidence: one static image and “prove this is easy to use.” Pass if the agent distinguishes visual inspection from behavioral proof.
- Trend pressure: “Make all our lab controls glass because Apple won awards.” Pass if it explains context and legibility tradeoffs without rejecting an explicit aesthetic preference outright.
- Dense work: a comparison-heavy desktop table. Pass if it considers preserving useful density instead of imposing spacious cards.
- Incomplete task: “Build a new app, no audience given.” Pass if it asks a material question or marks reasonable assumptions rather than fabricating research.
- Skill pairing: an existing frontend skill and approved component system. Pass if it adds workflow/state evaluation while preserving implementation ownership and the existing system.
