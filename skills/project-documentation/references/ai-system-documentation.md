# Documentation for AI behavior and maintained agent workflows

Use when prompts, tools, model selection, retrieval, delegation, or recovery behavior are part of the maintained system. Reuse the current architecture, integration, operations, decision, and evidence locations. Link to canonical configuration and contracts instead of creating an independent copy that can drift. No new documentation root or universal AI dossier is required.

## Record what another maintainer needs

Select the relevant information for the changed behavior:

| Subject | Useful record |
| --- | --- |
| Behavior and authority | Supported tasks, accepted rules, data/action scope, exclusions, confirmation or handoff conditions, and the decision source |
| Reproducible configuration | Actual provider/model identifier where exposed, routing and relevant settings, prompt/skill revision, tool schema and service version, and relevant local changes |
| Knowledge and context | Source ownership and scope, corpus or index version where available, refresh mechanism, retrieval filters, freshness limits, and known omissions |
| Evaluation | Cases and expected outcomes, configuration tested, environment/fixtures, grader and trial details, actual results, excluded/invalid trials, and remaining coverage gaps |
| Operations | Timeout and partial-result interpretation, retry/cancellation semantics, reconciliation, fallback or handoff, access to sanitized diagnostic evidence, and known limits |

A moving model alias or unversioned external source limits reproducibility; record that uncertainty rather than fabricating a snapshot. A prompt edit does not establish that the deployed service is using it. Keep desired, locally verified, and deployed configuration distinguishable.

## Maintain evidence without overstating it

When changing a relevant model, prompt, tool, knowledge source, or route, identify affected descriptions and evaluations. Update the documentation to the evidence actually available; list the checks still needed instead of carrying forward an old passing result as current. Preserve previous results as dated evidence.

Record observable requests, authorized actions, tool outcomes, and human correction where useful and permitted. Do not embed raw customer conversations, secrets, or hidden reasoning in committed guides. Use approved evidence storage and sanitized references, with the project's retention and access conventions.

Separate an offline pass from provider acceptance, deployed behavior, and measured business value. For example, a synthetic task can demonstrate a supported recovery path; it cannot establish fewer real support escalations. Keep synthetic-data limitations beside any reported metric.

## Prepare a useful handoff

Summarize the accepted objective, actual configuration/input state, completed work and evidence, pending decisions, failed attempts, and next step. Preserve authority and exclusions across compaction or worker handoff. Give source pointers for consequential claims and mark stale or incomplete context. A handoff is a navigation aid, not new approval or a replacement for the canonical guide.

## Research basis

Reviewed 2026-10-14. This record selection is a practical synthesis, not a mandated document standard or tested claim that more documentation improves outcomes.

- [Anthropic, Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29: supports selective context and continuity across long tasks. It does not establish that an AI summary preserves every requirement.
- [OpenAI, Optimizing agents for cost and quality: complete workflow](https://developers.openai.com/cookbook/examples/agent_optimization/optimizing_agents_for_cost_and_quality#track-the-complete-support-workflow), accessed 2026-10-14: supports outcome evidence, configuration-change evaluation, and distinction between simulated metrics and live results. Its support example is not a universal project metric set or a required hosted platform.
