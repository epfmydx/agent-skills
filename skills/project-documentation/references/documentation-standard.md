# Default documentation standard

Use this fallback where project documentation conventions are missing, or when the user requests this standard. It defines a suggested organization and maintenance workflow. Preserve conventions already selected by the user or repository.

## Select the root and relevant material

Use `docs/` for a new documentation structure. If the project already uses `documentation/` or another canonical root, apply missing conventions there. Do not create both roots to satisfy this reference. Existing custom documentation systems can provide the equivalent navigation and checks.

In the table below, `<docs-root>` means that selected root. During a requested foundation setup, establish the entry points and maintenance workflow, then document relevant project behavior verified from source. Create other documents when they have meaningful content; do not fill empty templates with assumptions.

| Default location | Purpose |
| --- | --- |
| Root `README.md` | Short project orientation and links to setup, integration, and documentation entry points |
| `<docs-root>/README.md` | Topic index for current guides, organized around readers' tasks |
| `<docs-root>/documentation-workflow.md` | Placement, evidence, review process, actual check commands, and their limits |
| `<docs-root>/architecture/` | System overview, boundaries, invariants, and implementation explanations |
| `<docs-root>/operations/` | Setup, configuration, operator workflows, troubleshooting, release, and recovery |
| `<docs-root>/api/` and `integrations/` | Consumer contracts, examples, compatibility, and integration-specific guidance where relevant |
| `<docs-root>/decisions/` | Meaningful accepted decisions and explicit supersession; only create with a real decision |
| `<docs-root>/known-gaps.md` | Unresolved discrepancies or unverified areas, with evidence and next steps; only create when gaps exist |
| `<docs-root>/archive/` | Dated reviews, superseded plans, and historical checkpoints with clear status |

Keep current behavior in durable guides. Keep dated test runs and implementation history distinct so a past checkpoint does not appear to certify today's source. An operational guide may link to evidence, and API changes may have their own consumer changelog. Respect any established product release-note convention.

Link from applicable repository agent instructions to the index and workflow. Keep those instructions short: read affected guides, verify material claims, review documentation impact, run relevant checks, and report updated/reviewed-unchanged/uncertain material. Reuse existing instructions rather than creating competing files. Keep one canonical explanation for each subject.

## Maintenance workflow

1. Read the index, affected current guides, accepted requirements, and source map when present.
2. Verify relevant claims against the actual source state, configuration, and tests. Record disagreements between implementation and accepted requirements.
3. Review the change's documentation impact, including relevant untracked and local changes. Choose a meaningful comparison base for committed work.
4. Update affected guides, or report them reviewed unchanged with a reason. Investigate unmapped changes rather than treating them as documentation-free.
5. Run structural and any applicable tooling checks. Report the exact verification scope and remaining uncertainty.

For substantial new or reverified guides, use existing metadata conventions. Where none exist, a compact header can record `document_type`, `status`, `verified_against_commit`, `last_verified`, and `verification`. Include relevant local edits in the stated baseline. Record only real evidence; metadata refreshes and link checks do not prove correctness. Preserve historical records by adding supersession notices and replacement links.

## Source mapping and checks

Reuse existing tooling first. A requested full documentation foundation should include a useful source-to-document map and lightweight structural/impact checks, or clearly report why a component remains incomplete. If the user requests a narrower documentation task, keep that scope and report material missing capabilities rather than building a tooling system automatically.

The default map is `<docs-root>/docs-map.json`: a versioned JSON object with an `areas` object whose named entries contain `source` glob lists and `documents` path lists. Map actual subsystem boundaries and canonical guides. Maintain mappings as paths change; do not route all source files to the index merely to hide uncovered areas.

The expected tool responsibilities are:

- **Structural check:** validate map shape, mapped paths, and supported relative links in active documentation. Validate machine-readable contracts and local references where supported. Document limitations such as heading fragments, schema validation, or external URLs. Exclude explicitly historical bodies as appropriate while preserving navigable archive entry points.
- **Impact report:** list potentially affected guides, whether they changed, and uncovered source files. Cover staged, unstaged, and relevant untracked changes, and support a meaningful branch/commit comparison. Keep this advisory; prose changes are not proof of review, and unchanged prose can be correct. Invalid input should fail visibly.
- **Tool checks:** test any new or adapted tooling against valid and invalid maps/links and relevant Git change states. A checker must not silently pass when a required parser or dependency is absent.

Suggested script names for a Node/Git implementation are `bin/docs-check.mjs`, `bin/docs-impact.mjs`, and `bin/docs-check.test.mjs`. Those names are reference examples, not installed capabilities in every project. Use the target project's supported runtime and documented equivalents; inspect and adapt any reused scripts rather than copying application paths, dependencies, or pipeline settings blindly. This skill does not bundle those executables.

Document runnable commands and their prerequisites in the project's workflow. Structural checks establish structural validity within their stated scope, not semantic correctness, live integration, or deployment acceptance. Keep application release gates distinct. Do not add mandatory CI approval or impact gates solely because the standard describes a documentation process.
