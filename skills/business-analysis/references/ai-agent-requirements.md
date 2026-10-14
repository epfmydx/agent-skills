# Requirements for products using AI agents

Use only when AI behavior is part of the product or workflow being specified. These are analysis prompts to select by consequence, not a mandatory questionnaire or permission to deploy an agent.

## Define the delegated job

Specify the desired business result, eligible users, relevant data, and excluded work. Separate what the agent may read, recommend, prepare, and execute. Identify whose authority an action uses and any policy conditions, confirmation, or human handoff already required. Model confidence cannot grant authority or replace an applicable policy check.

Resolve consequential ambiguities before enabling dependent actions. When evidence is missing, contradictory, or outside the supported domain, specify whether the product asks, abstains, or transfers work. Make the recipient and retained context explicit where known. Avoid inventing a human service that does not exist.

## Specify outcomes and recovery

Describe observable business states independently of agent narration. A generated email is a draft; successful dispatch is a different outcome; receipt or downstream resolution may require further evidence.

Select applicable cases:

| Situation | Business decision to make |
| --- | --- |
| A tool times out after submitting an action | How to establish whether it occurred before retrying; who handles an unresolved result |
| A request is repeated or resumed | Whether it refers to the same operation; what must never be duplicated |
| Only some steps succeed | Which results remain valid, what can be retried or compensated, and what the user must see |
| Evidence or authorization changes during a run | When work must pause, revalidate, or ask for a decision |
| The user cancels or corrects the request | What can still be stopped; which completed effects need separate recovery |
| The agent cannot complete the job | What is returned, retained, transferred, or discarded |

Describe the required result; engineers select mechanisms such as operation identifiers or transactions. Do not promise that cancellation reverses an external action.

## Make acceptance evaluable

Separate non-negotiable constraints, such as permission boundaries, from graded quality such as usefulness or tone. Use representative, authorized examples with expected outcomes grounded in accepted rules. Include material missing-data, ambiguous, denied-action, and failure cases. A policy-compliant abstention may be the correct outcome.

Agree how outcome quality, human correction effort, latency, and cost will be assessed when they matter. Baselines, tolerances, sample coverage, and release thresholds are proposed until accepted; do not assign universal numbers. Pass these requirements to QA for an evaluation design that accounts for variable responses and alternative valid paths.

An offline evaluation can support a release decision but cannot establish real adoption or business value. Plan outcome follow-up within the user's scope; do not start collecting customer data or conducting live trials without authorization.

Research context and limitations are in [research sources](research-sources.md).
