---
name: project-documentation
description: "Establish, standardize, or maintain repository documentation alongside software changes or in a documentation audit, reconciliation, handoff, or release preparation. Follow existing project documentation conventions; use the default documentation standard where conventions are missing. Verify guides against source, accepted requirements, and evidence. Use for engineering project knowledge, not general prose, office-document formatting, or external notes publishing."
---

# Project Documentation

Keep project knowledge accurate, easy to find, and explicit about what has been verified. Preserve existing project documentation conventions and use the default documentation standard to fill missing conventions. This skill can be used independently or alongside a development workflow; it does not require a team or prescribe models, efforts, or delegation.

## Choose the documentation convention

Apply this precedence before writing:

1. Follow the user's explicit request and applicable repository instructions. An explicit request to standardize or migrate documentation can change the existing convention within that scope.
2. Reuse the existing canonical documentation location, organization, formats, and maintenance tools. Find it through repository instructions, the root README, indexes, and current guides. An existing `documentation/` root stays `documentation/`; sparse documentation is not a reason to create a competing `docs/` tree.
3. For decisions the project has not defined, use the [default documentation standard](references/documentation-standard.md) within the chosen documentation root. Preserve established choices while filling the gaps; adopting the standard does not require renaming the root.
4. If no project documentation structure exists, use `docs/` and the default documentation standard when documentation setup is in scope. A framework boilerplate README alone does not establish a project documentation convention.

If several documentation roots exist, use instructions and navigation to establish their roles before consolidating anything. Ask only when a material ambiguity remains. For ordinary changes, maintain affected guides and report relevant foundation gaps; do not turn a small edit into a repository-wide reorganization. Read the reference when establishing documentation, standardizing it, or choosing a missing convention, not for every routine prose edit.

## Establish the scope and authoritative sources

Read applicable repository instructions, the documentation index, and the affected current guides. Inspect any source-to-document map and documented checking tools. Discover actual filenames and commands. Check that suggested files and tools exist before using them.

Choose the work that matches the request:

- **Foundation or standardization:** establish documentation when requested, or align it to an explicitly requested standard. Read the reference, map existing material to the selected structure, and implement the relevant foundation within the authorized scope. Preserve history and update navigation and source mappings when moving material.
- **Change support:** review the documentation impact of the authorized software change and maintain the relevant explanations and contracts.
- **Audit or reconciliation:** inspect the requested documentation surface, report discrepancies and missing coverage, and edit only when the request authorizes fixes. An audit is not permission to implement proposals or change product behavior.
- **Handoff or release preparation:** capture the actual source state, accepted decisions, remaining work, and verification boundaries. Creating a handoff or release note does not authorize publication or deployment.

Agree scope through the existing request and project context; ask only for material missing decisions. Preserve pre-existing edits. Keep repository-owned documentation in the repository unless the user explicitly requests another destination. Do not create a parallel copy in a notes app or cloud Page simply because that tool is available.

Code describes implementation; accepted requirements and decisions describe intent. Neither silently overrides the other. If they disagree, state the discrepancy, its evidence, and the next verification or decision needed. Historical plans, archived outcomes, and stale checkpoints do not authorize work or establish the current baseline.

## Review impact and reconcile content

1. Identify the actual input state: repository, branch or revision where relevant, local changes, and the comparison base. Include staged, unstaged, and relevant untracked files when reviewing a local change. Do not use a branch compared with itself as evidence that earlier committed work has no documentation impact.
2. Use the repository's impact tool or source map where present. Otherwise inspect the changed behavior and search for its descriptions, configuration, examples, and callers. Review unmapped changes with judgment. A clean impact report or a modified guide does not itself prove adequate coverage.
3. Verify consequential statements using current source, configuration definitions, tests, and accepted decisions. Trace related consumer or integration code when the scope crosses repositories. Do not infer end-to-end integration from one component's implementation or tests.
4. Update the affected canonical explanation, or record **reviewed unchanged** with a concrete reason. Link related guides to the canonical material. Record unresolved uncertainty in the established gaps location or the completion report, with evidence and a next step.
5. Preserve useful historical records. Mark a superseded record and link its replacement instead of rewriting its old outcome. Do not revive unfinished tasks from an archive or refresh a document's status without verifying its claims.

Keep this proportional: a wording correction does not require a repository-wide audit; a requested comprehensive audit must state which surfaces were inspected and which remain uncovered. Broaden scope when a concrete inconsistency warrants it, not merely because more documents exist.

When the change affects a product's AI behavior or a maintained agent workflow, read [AI-system documentation](references/ai-system-documentation.md). Apply only the relevant records within the existing documentation structure. Using AI to write ordinary software does not itself require an AI-system guide.

## Put information where its reader needs it

Use the project's established locations. Where placement is undefined, use the reference standard. Create categories only when relevant material belongs in them; ordinary maintenance does not require scaffolding every category:

| Content | What belongs there |
| --- | --- |
| Entry point and topic index | Orientation and navigation, with links to canonical guides |
| Architecture | Boundaries, invariants, implementation explanations, and useful source pointers |
| Operations | Setup, configuration, operator actions, troubleshooting, and recovery |
| API and integrations | Consumer contracts, compatibility, examples, ownership, and cross-system behavior |
| Decisions | Meaningful accepted decisions, alternatives, consequences, and explicit supersession |
| Handoff and historical evidence | Dated state, verification performed, remaining work, and references for resumption |
| Changelog or release notes | Meaningful changes for the intended audience, using the project's release convention |

Keep consumer guides concise. Put internal implementation detail in developer guidance unless it helps a consumer act correctly. Write release notes for the repository's intended audience rather than turning them into an agent activity log.

Create a decision record only for an actual accepted decision supported by the task or evidence. Do not invent an owner, approval, date, or rationale from the code alone. Routine Git history does not need a second document per work session. Avoid empty directories and bulk metadata stamping. Documentation foundation work can include the standard's source map and lightweight checks; ordinary edits do not automatically expand to tooling work. New blocking CI gates require task scope that calls for them.

Use portable repository-relative links in committed documentation. Preserve established external sources and explicitly historical references. Keep source/document mappings and navigation accurate when paths move. Do not hide unmapped areas by mapping everything to the index.

## Evidence and freshness

For substantial new or reverified material, identify the inspected baseline and verification scope using the repository's format. If local edits matter, state that the evidence includes them; a HEAD hash alone does not describe a dirty snapshot. A recorded revision is the snapshot inspected, not a promise to equal the documentation's eventual commit.

- Distinguish source inspection, tests actually executed, local or synthetic checks, browser/device or external-provider acceptance, push, and deployment. Test source inspected is not a test run.
- Link useful source/test evidence and record actual commands and outcomes where appropriate. Retain failures, skipped coverage, and unresolved discrepancies that limit the conclusion.
- Update dates and source identifiers only after verifying the corresponding scope. Moving files, editing prose, or passing link checks does not reverify untouched claims.
- Keep credentials, customer records, sensitive request/response bodies, and private environment output out of committed guides. Use sanitized examples and the project's approved evidence location.

Treat AI-generated drafts and handoff summaries as claims to reconcile with their sources. Preserve material omissions, conflicting evidence, pending decisions, and failed checks; a fluent summary or another agent's agreement does not reverify the project.

Check operational command examples against the real interfaces and preconditions. Execute safe checks when useful and authorized. Do not perform destructive recovery, send messages, publish, or deploy merely to verify a documented command; mark unexecuted steps accurately.

## Validate and report

Run the repository's applicable documentation checks and inspect their results. If documentation tooling changed, test that tooling. Documentation-only prose work does not automatically require a full application test suite; behavior or executable examples may warrant focused checks. Follow the repository's existing requirements without turning an advisory impact report into a new blocking gate.

Where no checker exists, inspect affected links and file references, examples, terminology, and consistency manually. Report that scope. Missing dependencies or failed checks must remain visible; a fallback check does not count as the original checker passing.

Structural validation cannot establish semantic accuracy, schema compliance beyond the validator's scope, live provider behavior, or deployment. Review material claims independently of formatting and links.

Complete with a concise report of:

- Documents updated and the behavior or explanation corrected.
- Relevant documents reviewed unchanged, with the reason.
- Checks actually run and their limits.
- Unresolved discrepancies, unreviewed scope, and the next verification step when any remain.

For foundation or standardization work, also name the selected documentation root, which existing conventions were retained, and which defaults were adopted or remain incomplete.

For example: “Updated the setup guide for the new catalogue action. Reviewed the API contract unchanged because requests and responses are unchanged. Documentation checks passed; the provider workflow was not exercised.”

When used within a development team, return this evidence to the lead. Keep staffing and overall acceptance with that workflow; this skill does not load a team skill or launch workers. Codex Dev Team is one optional integration.
