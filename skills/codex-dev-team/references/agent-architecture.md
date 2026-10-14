# Architecture for products that delegate actions to AI

Use for the affected agent workflow, not as a reason to redesign an unrelated application. Begin with accepted business rules and the existing architecture. A deterministic workflow or single agent may suffice; extra agents need a demonstrated coordination or context benefit.

## Enforce the action boundary

Map each tool to the actor, data scope, and permitted operation. Enforce authorization, tenant isolation, validation, and hard business rules in the service that performs the action. A prompt, model confidence, hidden button, or well-formed JSON is not an authorization control. Give the agent only the capabilities needed for its job; a draft-only assistant should not be able to execute the underlying transaction.

Treat retrieved documents, tool text, and external messages as data, not authority to change instructions, permissions, or destinations. Validate structured fields before use; schema conformance does not establish trustworthy intent. When policy requires confirmation, bind it to the concrete action and material parameters being executed; revalidate changed scope. Reuse valid existing authorization and do not invent confirmation for every read or harmless step.

## Make tools understandable and testable

Use distinct tool purposes, clear parameters, bounded results, and errors that say what is known about execution. Mark pagination, truncation, stale evidence, and partial data where these affect decisions. Return verifiable identifiers and state when available. Descriptions must match implementation and should not hide side effects behind a read-sounding operation.

Validate the same tool/service path the product actually uses, including denial and failure paths. Mock success proves only the mocked contract. Keep technical mechanisms out of product-facing flows unless users need them to decide or recover.

## Handle uncertain and repeated work

Distinguish rejected-before-execution, completed, partly completed, and unknown outcomes. For a timeout after submission, inspect operation status or authoritative state before another consequential action. Use a stable operation identity and a supported idempotency contract for retries of the same intent; a newly generated key can create a duplicate.

Check the provider's actual semantics, retention period, parameter matching, and concurrency behavior. Do not assume all services or API versions deduplicate in the same way. Where no safe reconciliation or retry mechanism exists, surface the unknown state and hand off within the accepted workflow instead of guessing.

Specify bounded retries and termination behavior appropriate to the operation. Cancellation should stop future work where possible; completed external effects need separately authorized recovery. Preserve partial results and guard against late responses applying to a replaced request. Recheck relevant permissions and preconditions at execution time.

## Make behavior diagnosable

Record enough privacy-conscious operational evidence to connect a request, approved scope, configuration, tool attempts, and verified outcomes. Do not collect secrets, unnecessary customer content, or hidden reasoning as routine diagnostics. Preserve existing retention and access controls.

Version relevant prompts, tool contracts, model settings, and retrieval dependencies using the project's conventions. Evaluate the affected behavior after changes using [agent evaluation](agent-evaluation.md); document fallback and recovery through the existing documentation workflow. A model upgrade does not by itself prove a workflow improvement.

See [research sources](research-sources.md) for the basis and limits of these recommendations.
