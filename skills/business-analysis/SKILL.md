---
name: business-analysis
description: Clarify software and product requirements, business rules, permissions, exceptions, and testable acceptance criteria. Use for requirements discovery or review, ambiguous feature requests, and consequential workflow changes. Keep clear, small fixes lightweight and separate proposed rules from accepted decisions.
---

# Business Analysis

Turn a business need into an implementable, testable agreement. The user or designated business owner decides priorities, policies, and acceptable tradeoffs. This skill supports those decisions; it does not invent approval or stakeholder consensus.

Use it independently or alongside a development team. The guidance is independent of model vendors and delegation tools. A team lead can perform the analysis directly; staffing and project coordination remain with the lead.

## Scope and evidence

- Preserve the requested mode and scope. Analysis does not authorize implementation, contacting stakeholders, or changing external trackers. Reuse decisions and authorization already established in the task.
- For a clear small fix, confirm the affected requirement and acceptance condition, then proceed within the existing authorization. Do not manufacture discovery meetings, questionnaires, or a full requirements document.
- For ambiguous or consequential work, inspect relevant user statements, accepted requirements, repository instructions, existing documentation, and affected source or tests. Distinguish accepted intended behavior, observed current behavior, proposals, and assumptions. Existing code is evidence of implementation, not proof of business intent.
- Surface conflicts between sources with their implications. Do not silently promote a guess, legacy implementation, or analyst recommendation into an accepted rule. An explicit authorized change can supersede an older requirement; record that relationship.
- Ask focused questions only when an answer materially changes business behavior or scope. Continue independent work while a decision is pending. Do not implement the dependent policy as though silence were approval; use clearly labeled, reversible assumptions for non-material details.

## Analysis workflow

Scale these steps to the assignment rather than requiring every artifact:

1. Establish the objective, affected actors, current problem, desired outcome, and observable success. Separate the deliverable from the business outcome it should improve. For outcome measurement, record an available baseline, proposed or accepted target, measurement method, and owner; leave unknowns explicit. Record what is in scope and what is deliberately excluded.
2. Describe the current and intended process where the difference matters. Identify relevant entities, ownership, roles, data boundaries, state transitions, and external dependencies.
3. Make business rules explicit: conditions, permitted actors/actions, outcomes, exceptions, and recovery. Cover applicable boundary cases, conflicting changes, repeated requests, and integration failures. Separate business decisions from implementation choices.
4. Write concrete acceptance examples covering the main outcome and material negative or boundary cases. Link each important rule to its source or pending decision and to its acceptance examples. Use the project's identifiers and format where they exist.
5. Hand off accepted requirements, unresolved decisions with their impact, and assumptions. Proposed acceptance criteria are not test results. Mark verified behavior only when supporting checks actually ran.

Read [requirements patterns](references/requirements-patterns.md) when the task needs a structured brief, decision table, permissions/state analysis, or acceptance examples. Ordinary small fixes need only the relevant subset.

## AI-assisted analysis and AI product requirements

When using AI to synthesize substantial or conflicting evidence, read [AI-assisted analysis](references/ai-assisted-analysis.md). Preserve source coverage and uncertainty; generated stakeholder opinions or polished requirements are not stakeholder validation.

Only when the product itself uses AI agents, read [AI-agent requirements](references/ai-agent-requirements.md) for delegated authority, uncertain outcomes, recovery, and evaluation requirements. The analyst using AI does not by itself activate this product checklist.

For the research basis or a future refresh, read [research sources](references/research-sources.md). These sources inform the skill; they do not establish a customer's policies or prove this workflow improves delivery outcomes.

## Delivery and collaboration

Return a concise answer or requirements artifact in the requested location. Follow existing documentation roots and conventions; do not create a parallel requirements system or tickets merely because this skill is active.

For a material feature, include the objective and scope, accepted rules, applicable acceptance criteria, and unresolved decisions. Identify who must decide when known; otherwise leave ownership open rather than inventing a stakeholder. Avoid unsupported delivery dates, budgets, or numerical confidence.

Business analysis defines the required outcomes and rules. UI/UX design translates them into usable flows and interactions; implementation chooses the technical solution; documentation preserves accepted knowledge. When a design or technical constraint changes a business outcome, bring that specific tradeoff back to the decision owner. These collaborators are optional; this skill does not require another skill or launch workers itself.
