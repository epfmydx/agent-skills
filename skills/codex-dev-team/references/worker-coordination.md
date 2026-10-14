# Worker coordination

Read before the first delegation in a coherent run. Use the role and effort defaults in the parent SKILL.md; this reference covers runtime resolution, briefing, supervision, and integration.

## Resolve family names at runtime

Astra, Sol, Terra, and Luna are logical selectors in this skill, not model IDs or guaranteed provider aliases. Do not send bare family names, invented `*-latest` IDs, or a constructed next-generation ID to a tool.

1. Honor model restrictions and exact model/version pins from the current request and applicable personal or project instructions before these defaults. A later explicit user instruction can change those restrictions. Otherwise, use the current native spawn tool's supported-model list or an available model catalog for the actual execution host/account. Public API availability alone does not prove a model is accepted by this Codex runtime. If no local list is exposed, use current official documentation to clarify identity, and disclose that local access remains unverified rather than guessing.
2. For each needed family independently, select its newest stable, non-deprecated general-purpose model exposed by that runtime. Use advertised generation/release metadata; for unambiguous versioned IDs, compare numeric version components rather than sorting strings. A future generation is eligible only after it appears in the supported catalog. Do not infer chronology from the word `latest`, arbitrary suffixes, or a snapshot date alone. Prefer the canonical family ID over dated snapshots unless the user pins a snapshot. Do not opt into preview or specialized variants merely because their names sort later.
3. Families need not share a generation. Resolve each eligible family to its actual available ID after applying model exclusions; an exposed but excluded model is not a fallback candidate. If a family is absent, report that and choose a suitable available family within the task's constraints: routine work can usually use Sol, or Luna when narrowly specified. Do not substitute when the user requires a particular model or family; report the blocker and continue only independent permitted work. Do not treat a renamed family as equivalent without current official evidence.
4. Resolve reasoning effort against the chosen model's runtime-supported values. Start from the role table; if that value is unsupported, choose a documented supported setting suitable for the assignment and disclose a material change. Respect exact effort pins. Never assume a new generation has the same effort levels as its predecessor.
5. Record the resolved family-to-ID mapping and effort in the dispatch record and tell the user which concrete models are being used. Resolve once at the start of a coherent delegation run, then reuse the chosen worker for corrections. Refresh for a new run, an explicit upgrade request, or an availability error; do not silently change models mid-assignment. After a rejection, refresh available choices before retrying and follow existing quota/permission failure rules.

This selection happens in the orchestrating agent using live tool metadata; no global configuration changes or separate resolver service are required. The available runtime catalog bounds what “latest” means. If it lags the public release, say “latest available here,” not “latest released.”

## Prepare the assignment

Read applicable repository instructions yourself. Record the working directory, base revision, existing changes, and intended input state before assigning writes. For dirty checkouts or concurrent writers, prefer isolated worktrees or bounded copies. Native agents may share the same filesystem and working directory; a new agent does not create isolation.

If the assignment depends on uncommitted changes, preserve and supply those exact changes, including relevant untracked files. A worktree starting from HEAD does not contain them automatically. Avoid copying dependency caches, secret files, or unrelated content. Track worker output relative to the prepared state so integration does not absorb pre-existing edits.

Give every worker a self-contained brief containing:

1. Role, concrete question or required behavior, and the checkpoint that ends the assignment.
2. Absolute working directory, base/input state, writable paths, useful read paths, exclusions, and applicable repository conventions.
3. Relevant reproduction, compatibility constraints, and acceptance cases, including material failure and boundary cases. Separate worker test responsibilities from parent acceptance checks.
4. Allowed command scope and shared resources to avoid. Investigation, design, and review default to no file edits; implementation and testing may run relevant commands within existing permissions.
5. A concise report: actual changes or findings with file references, commands and results, uncertainties, and blockers. The worker must return at the checkpoint and await follow-up rather than expand scope or publish.

Assign disjoint writable paths to concurrent workers. Serialize shared-file changes and checks contending for databases, ports, or containers. Reviewers inspect a frozen patch or snapshot. Workers may recommend scope or architecture changes; the parent resolves them before dependent implementation. Tell workers not to delegate further unless the parent explicitly assigns that responsibility.

## Keep the task state coherent

For multi-step work, keep a compact current record in the existing task or project location: accepted objective and decisions, active assignments and dependencies, input revisions, completed evidence, unresolved questions, and next checkpoint. Do not create a second tracker or durable memory merely to satisfy this guidance. A brief can link to canonical artifacts; it must still contain the constraints the worker needs to act correctly.

When requirements or shared inputs change, identify the affected workers, update their briefs, and pause dependent work if its basis is no longer valid. Treat a late result against superseded inputs as a candidate to reconcile, not automatically accepted work. Read-only investigations may continue where the change has no bearing.

Handoffs and compacted summaries must preserve material exclusions, authority, pending decisions, failed attempts, and evidence pointers. Distinguish accepted decisions from worker suggestions. Re-read the specific source before a consequential action when the summary is ambiguous or stale; do not routinely reload every transcript.

## Dispatch and supervise native workers

Use the live tool schema as the authority. In environments exposing `collaboration.spawn_agent`, select the model and reasoning effort on that call. Use `fork_turns="none"` with a complete brief for a fresh bounded worker. In this API, an omitted or `"all"` fork inherits the parent model and effort and cannot be combined with model overrides. A limited history fork is optional when supported and genuinely needed; do not copy a large parent transcript by default.

For a substantive implementation worker, resolve Sol and its effort first, then call the live spawn tool with those concrete values. This is pseudocode, not literal tool arguments:

```text
spawn_agent(
  task_name = "implement_fix",
  model = resolved_models["Sol"],
  reasoning_effort = resolved_efforts["Sol"],
  fork_turns = "none",
  message = complete_bounded_brief
)
```

The brief's path and read-only restrictions are instructions, not an OS sandbox. Agents inherit the runtime's permissions unless the actual tool supports a narrower configuration. Do not claim tool allowlists or isolation that were not enforced. A CLI-specific Claude tool restriction has no automatic Codex equivalent.

Keep worker IDs, assigned model/effort, brief, and input-state records. Reuse the same worker for focused corrections in its coherent area: with the collaboration API, `send_message` steers a running worker, while `followup_task` can start another turn on an idle worker. Use status and wait tools appropriate to the host, respecting their limits. Do useful parent work while workers run and collect bounded reports rather than complete transcripts.

A worker's result ends its assignment, not parent acceptance. Inspect failures or denied actions even if a later report claims success. If a different model or materially different permissions are required, create a newly configured worker with an explicit handoff; do not pretend a message changes its model or sandbox. Interrupt cancelled work and preserve unfinished changes. On completion, ensure no worker remains running; idle completed workers may remain available when the API has no close operation. Do not claim process shutdown or background wakeups without evidence.

## Review and integrate

- Review actual diffs, new files, and the relevant execution path against the brief. Verify worker test reports using actual artifacts and command evidence. Run appropriate independent acceptance checks; a reported test count is not sufficient.
- Send focused corrections for demonstrated defects. When repairs repeat without progress, reassess the brief, evidence, or model instead of continuing an unbounded retry loop. Resolve quota, authentication, and permission failures rather than repeating identical calls.
- Use the assignment's checkpoint and explicit task budgets to bound work. When a dependency fails or repeated attempts yield no new evidence, report the specific blocker and change the approach, continue independent work, or request the missing decision. Do not manufacture a deadline, silently exceed a user limit, or keep retrying merely because a worker remains available.
- Recheck the destination state before integrating. Apply only reviewed worker changes, include intended untracked additions, and verify the integrated files match the tested inputs. Run relevant combined checks when composing workers' changes. Preserve user changes and dirty scratch worktrees.
- Commit, push, merge, or deploy only within existing task authorization and repository requirements. Do not introduce a new confirmation step for already authorized actions.

Report delivered behavior, actual worker models, independent validation, unresolved limitations, publication state, and any workers still running. If model resolution was not exposed, distinguish the requested model from a verified actual model.

When usage is available, report its scope and record input, cached input, output tokens, and observed elapsed time. Missing metrics are unknown, not zero. Do not sum repeated cumulative snapshots or add parallel durations as wall time. Account for parent briefing and review overhead; nominal cost, subscription limits, and actual charges are different. Do not reuse Claude-specific usage fields or assume Codex exposes equivalent counters.
