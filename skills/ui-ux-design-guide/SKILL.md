---
name: ui-ux-design-guide
description: Design or review product workflows, information architecture, interaction states, visual hierarchy, and accessible cross-platform interfaces. Use for UX planning and design-quality evaluation alongside frontend implementation; do not turn narrow changes into unsolicited redesigns.
---

# UI/UX Design Guide

Help people complete meaningful tasks with confidence. Treat visual excellence, task usability, accessibility, and technical reliability as related but separately testable qualities.

## Working contract

- Preserve the requested scope, existing brand, successful patterns, platform, and implementation constraints. A small fix needs a small process.
- Establish the user, task, context, risk, and success criterion before choosing a visual direction. Ask only for missing information that changes the decision; mark other assumptions.
- Use existing product evidence first. Awards supply examples and hypotheses, not proof of universal usability. Separate observation, measured finding, recommendation, and aesthetic preference.
- Do not fabricate research, test participants, analytics, screenshots, benchmarks, or implementation verification. A screenshot supports visual observations, not behavior claims.
- Respect native conventions without imposing Apple styling on other platforms. Do not prescribe glass, rounded cards, monochrome palettes, oversized headlines, or any other fashion as the default.
- This skill grants no authority to publish, deploy, purchase assets, change external systems, collect personal data, or perform destructive actions.

## Working with other skills

Use this as a standalone design/review skill or alongside an available development workflow. This skill supplies task flows, interaction decisions, and design acceptance criteria; the coordinating workflow owns staffing, integration, and completion. Codex Dev Team is one optional integration, and no dedicated design worker is required for every task.

When another design or implementation skill is active, read [collaboration guidance](references/collaboration.md). Follow explicit user and repository requirements, existing product conventions, and task/accessibility needs before optional visual defaults. Use the available implementation capability for relevant visual execution and stack-specific code. Keep operational interfaces appropriate for repeated work.

## Select the relevant depth

Infer the work mode for the affected scope from the request: reproduce a selected reference, refine an existing interface, or create a new direction. Reproduction preserves the selected reference; refinement preserves unaffected decisions. Do not ask a mode question when intent is clear. For a narrow change, inspect its affected workflow and states, make the smallest useful recommendation, and verify the relevant quality gates. For a new product or substantive redesign, use the workflow reference and build a coherent end-to-end slice before expanding.

When a UI reference is selected, read [collaboration guidance](references/collaboration.md) for source authority and faithful integration, then use the [evaluation guidance](references/evaluation.md) to compare the actual implementation with that reference. Scale both to the requested scope.

Read only the references needed:
- [Workflow design](references/workflow-design.md): problem framing, navigation, task flows, states, forms, complex work, and AI interactions.
- [Visual craft](references/visual-craft.md): hierarchy, typography, composition, density, color, motion, and distinctive art direction.
- [Platform adaptation](references/apple-platforms.md): target-platform routing, Apple HIG interpretation, Android guidance, and web boundaries.
- [Accessibility](references/accessibility.md): practical checks and standards boundaries.
- [Evaluation and templates](references/evaluation.md): quality gates, research plans, evidence reports, and handoff contracts.
- [Examples and invocations](references/examples.md): realistic uses and context-dependent choices.
- [Evidence and sources](references/evidence.md): verified 2025/2026 examples, source limits, and refresh rules.
- [Working with other skills](references/collaboration.md): optional collaboration, responsibilities, and overlapping guidance.

## Delivery contract

Return a decision or deliverable proportionate to the task: the proposed design, rationale tied to the user's goal, important states, constraints/tradeoffs, and verification results. Report tested, inferred, and untested separately. For reviews, prioritize concrete task failures before optional style changes. For implementation handoff, provide behavior and state acceptance criteria, not only a polished happy-path image.

The companion [UI-UX-DESIGN-GUIDE.md](UI-UX-DESIGN-GUIDE.md) combines the references for human reading; use the modular references during agent work to avoid loading the whole guide. References are canonical. After editing them, run `python3 scripts/build_guide.py` from this skill's directory to refresh the combined edition, then `python3 scripts/build_guide.py --check` to check synchronization.
