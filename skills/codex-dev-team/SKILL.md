---
name: codex-dev-team
description: "Coordinate a Codex development team for implementation, investigation, and independent review. Use when the user requests Codex Dev Team, Codex workers, or an established Codex team workflow. Sol leads and develops, Luna handles bounded work, and Astra handles justified escalation; include relevant business analysis, UI/UX, and documentation checks. Preserve an explicitly requested alternative worker workflow."
---

# Codex Dev Team

The user owns priorities, acceptable tradeoffs, and what done means. The current parent agent owns requirements, planning, implementation or delegation, acceptance, integration, and the final report. Keep this ownership regardless of the parent's model.

The lead also owns task-level project management: work breakdown, sequencing, dependencies, blockers, scope changes, and progress reporting. A separate project-manager worker is optional when a concrete coordination task justifies one. Delivery commitments and business-policy decisions remain with the user or designated owner.

## Scope and team size

- Preserve the request's mode: analysis and feasibility requests remain read-only unless implementation is authorized. A documentation audit does not authorize code changes. Reuse existing task authorization without adding approval gates.
- Keep small, cohesive work with the lead. Delegate a concrete assignment when its value justifies briefing and review, including an independent review at a meaningful checkpoint. Parallel workers need useful independent work; do not manufacture assignments or a fixed team size.
- The lead should implement or advance another necessary part while helpers work. Collect concise findings and evidence rather than repeatedly rereading full transcripts. A worker's output is not parent acceptance.
- For substantive features and consequential fixes, obtain a fresh independent review once the candidate is stable, and before authorized publication. Review ordinary tiny edits directly. If delegation is unavailable, disclose that review independence is missing and perform appropriate local checks.
- Use native subagents, not new user-owned sidebar chats or a duplicate CLI supervisor. Do not replace an explicitly requested Claude Code or other worker workflow.
- If the required tool or model is unavailable, disclose the limitation and use a permitted alternative or continue locally within scope. Respect exact model and cost restrictions; do not bypass a denied action through another runtime or provider. Keep credentials, customer records, and unrelated private content out of worker briefs and copied context.
- Invoking this skill preserves the parent model, effort, speed, and global configuration. The user can select Sol for the parent; this skill does not switch it. Where a new worker's speed can be selected and no preference is set, prefer Standard. Do not override an explicit speed choice or claim control the tool does not expose. Ultra is not required to request delegation.

## Roles and effort

These are workflow defaults, not measured quality or cost guarantees. Honor explicit model/version and effort pins. Resolve each family against the current runtime, and set the chosen worker model and supported effort explicitly.

| Assignment | Model family | Starting effort |
| --- | --- | --- |
| Lead or primary developer | Sol when selected for the parent | Recommend `medium`; preserve the actual parent settings |
| Substantive implementation, debugging, investigation, or documentation synthesis | Latest available Sol | `medium`; `high` for difficult logic, debugging, or refactors |
| Business analysis, requirements discovery, or rule clarification | Latest available Sol | `medium`; `high` for complex rules, conflicting requirements, or consequential workflows |
| UI/UX planning or interaction design | Latest available Sol | `medium`; `high` for complex workflows; use the independent-review row for separate usability review |
| Presentation strategy, storyboarding, or substantive slide writing | Latest available Sol | `medium`; `high` for conflicting evidence, difficult audience tradeoffs, or consequential claims |
| Independent review | Fresh latest available Sol | `high`; `xhigh` for subtle security, concurrency, or other consequential risks |
| Bounded coding, regression cases, fixtures, or reproductions with clear acceptance | Latest available Luna | `high` |
| Narrow extraction, inventories, simple summaries, or mechanical transformations | Latest available Luna | `low` (Light in some clients) |
| Difficult architecture, cross-system decisions, or an unresolved material diagnosis | Latest available Astra | `medium` for a focused consultation; `high` for difficult tradeoffs; `xhigh` only when warranted |

Sol can handle ordinary architecture and complex implementation. Escalate a specific uncertainty to Astra with the evidence, attempted approaches, constraints, alternatives, and decision needed. There is no mandatory ladder of cheaper attempts when the risk already warrants stronger judgment. If a helper lacks context, repair the brief before assuming more effort will solve it. Max and Ultra are exceptional supported options, not default roles. Effort levels are not equal capability scores across models.

Apply model exclusions, version pins, and budget limits from the user's current request and applicable personal or project instructions before automatic selection or fallback. Keep personal preferences in those local instructions rather than embedding them in this shared skill. Do not hardcode prices or claim savings without comparable usage evidence.

## Dispatch and review

Before the first delegation in a coherent run, read [worker coordination](references/worker-coordination.md) for family resolution, complete briefs, shared-resource boundaries, tool usage, and acceptance. Reuse that context for subsequent workers; refresh the runtime mapping after an availability error or explicit upgrade request.

Each assignment needs a concrete outcome, exact input state and working directory, writable paths or read-only scope, exclusions, acceptance cases, and a stopping checkpoint. Use fresh bounded context and explicit model/effort settings when the tool supports them. Workers should not delegate further unless that responsibility was explicitly assigned.

Reviewers inspect frozen inputs and the original requirements, with enough context to trace affected paths. Ask for demonstrable defects, missing cases, and test evidence rather than agreement with the implementer's rationale. The lead resolves findings and checks the integrated candidate. After repairs, recheck affected behavior and findings; broaden testing only when new changes, failures, or remaining risk justify it.

For changes to agent behavior, skills, prompts, model routing, or tool workflows, read [agent evaluation](references/agent-evaluation.md) when behavioral evaluation is warranted. Keep ordinary software validation proportionate; an agent writing the code does not make the product an AI system. Confirm results through observable artifacts and state, not the worker's success narrative or a second model's agreement.

Do not mistake a separate agent for an isolated filesystem. Use disjoint writes or prepared worktrees/copies, preserve pre-existing changes, and serialize tests that share mutable databases, ports, or containers. Publication remains subject to existing task authorization and repository instructions.

## Optional companion skills

Resolve named companions through the current environment's skill catalog or configured locations; do not assume they are installed beside this folder. Read only available skills relevant to the task. Missing companions do not authorize installation and do not prevent applying the relevant checks below. The reusable companions can also operate independently of this Codex-specific orchestration workflow.

## Business analysis when requirements need clarification

For ambiguous feature requests, consequential business-rule changes, or requested requirements reviews, read the available `business-analysis` companion. Clear small fixes need only their relevant acceptance condition. If the companion is unavailable, disclose that and perform the necessary clarification within scope.

- Establish the business objective, actors, scope, material rules and exceptions, and testable acceptance criteria before dependent design or implementation. Separate accepted intent, observed implementation, proposals, and assumptions; existing code does not establish business policy.
- The lead can perform this analysis directly. Delegate a bounded analyst assignment when useful using the role table. Keep project coordination and final acceptance with the lead; neither lead nor analyst invents stakeholder decisions.
- Resolve questions that materially change business behavior with the appropriate owner. Reuse established decisions and authorization, continue independent work, and do not turn discovery into a mandatory sign-off ceremony.
- Pass accepted outcomes and rules to UI/UX and implementation, and maintain affected requirements through Project Documentation using the repository's conventions. Trace material rules to acceptance evidence; report unresolved decisions and their impact at completion.

## Architecture and implementation

Choose the simplest design that satisfies the accepted behavior, existing system constraints, and relevant failure cases. Agent-assisted coding does not require adding AI to the product. Keep hard business invariants in enforceable application logic and validate generated changes against the actual integration path.

When the product itself delegates actions to AI, read [agent architecture](references/agent-architecture.md) for tool contracts, permission enforcement, uncertain results, recovery, and operational evidence. Consult Astra only for the specific unresolved decision that warrants it; ordinary design remains with Sol or the current lead.

## UI/UX for interface work

For new interfaces, material workflow changes, or requested usability reviews, read the available `ui-ux-design-guide` companion and only the references relevant to the task. Apply it to backend changes when they alter user-visible states, permissions, recovery, or interactions. Unrelated backend work and tiny wording/style fixes do not need a full design process. If the companion is unavailable, disclose that and still check the task's relevant interface acceptance criteria.

- At scoping, identify the user's task, target platforms, existing design system, important states, and observable success. Infer exploration, refinement, or reproduction for the affected scope. Implementing a user-selected design defaults to reproduction within that scope; do not add a confirmation ceremony when the request is clear. Preserve explicit user/repository requirements and accessibility constraints; optional visual defaults must not override the selected direction.
- The lead can handle design alongside implementation. Delegate a bounded UI/UX assignment only when useful, using the role table; this is a responsibility, not a permanent extra worker. Use an available frontend or implementation skill when relevant, following the companion's collaboration guidance when available.
- For work based on a selected design, preserve the authoritative reference/version and ensure implementers and reviewers can inspect the relevant source and rendered evidence. Follow the conditional UI brief in worker coordination and the companion's handoff guidance. If supplied references disagree materially, resolve the affected decision rather than silently choosing a different target.
- Before claiming a visual match, compare the integrated application against that reference, resolve material discrepancies, and report the layouts/states inspected, intentional departures, and remaining uncertainty. Include this comparison in the existing independent review when applicable. If reference or rendering access is unavailable, report fidelity as unverified while completing other supported work.
- Before completion, review affected flows, errors/recovery, responsive behavior, and accessibility against the agreed criteria. Visual matching and functioning interactions need separate evidence. Distinguish screenshot inspection from tested interactions and actual browser/device or assistive-technology acceptance; report untested behavior.
- Capture accepted design decisions and user-facing behavior through Project Documentation where they affect maintained guides. Keep model routing here and detailed design guidance in the companion.

## Presentations when communication is a deliverable

When the task includes a presentation, proposal deck, demo narrative, or presentation review, read the available `presentation-strategy` companion. Use its audience, purpose, delivery-mode, evidence, and writing checks. For deck creation or editing, also use an available presentation-authoring skill for the file, rendering, and delivery workflow. If a companion is unavailable, disclose that and still perform the task's relevant checks within available capabilities.

- The lead can handle a small presentation directly or delegate a bounded strategy, writing, design, or review assignment using the role table. These are responsibilities, not a fixed team. Business analysis supplies accepted requirements and evidence; presentation strategy shapes how the audience understands or uses them.
- Preserve the requested format, template, slide count, and task mode. Do not turn an outline request into deck production, or a development task into an unrequested presentation.
- Review the argument, source support, audience fit, and actual rendered artifact where applicable. Include likely objections, notes, timing, or a readable companion only when useful and within scope. Distinguish slide inspection and rehearsal from actual audience acceptance.

## Documentation is part of completion

For meaningful changes, review documentation impact before completion. Read the available `project-documentation` companion and follow the repository's current documentation conventions. If it is unavailable, say so and still perform the repository's required documentation review within scope.

- At scoping, locate the relevant current guides, contracts, and operational instructions. Include material documentation needs in acceptance criteria.
- After implementation stabilizes, update affected guides or explain why they remain accurate. Run applicable documentation checks. Include documentation accuracy in the independent review when relevant.
- The implementer handles small updates. Assign substantial writing, reconciliation, or an independent consistency review only when useful, using the role table above. Keep model routing here; the documentation skill defines how to maintain the material.
- Record documents updated, reviewed unchanged with a reason, and unresolved discrepancies. Documentation checks do not prove semantic accuracy, external integration, or deployment.

## Completion and evidence

Report delivered behavior, actual worker models/efforts used, meaningful validation, documentation impact, remaining limitations, and publication state. Distinguish source inspection, tests actually run, browser/device or external-provider acceptance, push, and deployment; report only the relevant states supported by evidence.

Ensure no worker is still running unintentionally. A concise handoff is warranted when work remains, not a new report file for every task. When usage is exposed, retain its scope, input/cached/output tokens, and observed wall time; missing metrics are unknown. Include parent briefing and review overhead in comparisons. More agents may reduce elapsed time while increasing total usage.

## Maintenance sources

Consult current official guidance when availability or behavior needs refreshing; the live tool schema governs execution:

For the delivery-role research basis and its limitations, see [research sources](references/research-sources.md). These workflow recommendations do not establish measured productivity improvements.

- [Subagents and model selection](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Models and reasoning](https://learn.chatgpt.com/docs/models)
- [Speed settings](https://learn.chatgpt.com/docs/agent-configuration/speed)
