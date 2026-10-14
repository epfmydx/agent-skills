# Evaluating agent behavior

Use for material changes to an agent, skill, prompt, model route, or tool workflow. Select checks by the changed behavior and its consequences. A narrow wording correction does not need a benchmark suite; ordinary application code still needs its relevant software checks.

## Establish the contract

Use accepted requirements to define what may happen, what must not happen, and what observable result counts as completion. Keep proposed thresholds separate from accepted release criteria. Start with representative tasks and material failures, including a known regression when available. Label synthetic cases and missing production coverage.

For skill testing, give a fresh worker a realistic request and the minimum raw artifacts, without the intended answer or the implementer's diagnosis. Restrict writes and side effects to a prepared fixture. Evaluate the actual resulting answer, files, and actions. A structural skill validator cannot test these decisions.

## Inspect the outcome

Verify state changes with authoritative artifacts or state queries where available. An attempted tool call, a polished answer, or a log saying “done” does not establish completion. Inspect relevant tool inputs, returned errors, authorization decisions, and partial results. An unknown external result stays unknown; do not rerun a consequential action merely to obtain a passing test.

Separate task outcome, required constraints, and graded quality. Permission violations cannot be averaged away by good prose. Allow alternative valid solutions; require an exact sequence only when order is itself a requirement. Keep evaluation answers and private grading artifacts out of the worker's input, and protect them from modification by the system under test.

## Assess variability and evaluation quality

Where model variability matters, use repeated independent trials with fresh or reset state. Report cases, attempts, failures, coverage, and relevant model/prompt/tool configuration. Choose trial counts to fit consequence, uncertainty, and available budget; one successful attempt is a smoke check, not a reliability estimate.

Use deterministic assertions for checkable properties. Use clear rubrics for judgment and calibrate model scoring against relevant human review when making quality claims. Multiple model judges can share errors; agreement alone is not ground truth. Diagnose grader, fixture, and tool-service failures separately from product failures, and retain invalid or excluded trials with reasons instead of silently improving the score.

## Compare and report

Compare candidates on the same conditions and task distribution; distinguish a new capability from preservation of existing behavior. Hold out meaningful cases when repeated tuning could overfit the suite. Repeat affected evaluations after model, prompt, tool, retrieval, or routing changes; expand only for demonstrated gaps or changed risk.

Report what passed, failed, or remains untested, with enough evidence to reproduce the conclusion and without unnecessary private traces. Include cost and latency only when observed and comparable. Offline checks do not prove production outcomes, usability, or business benefit; authorized live acceptance and monitoring are separate evidence.

See [research sources](research-sources.md) for provenance and limitations. No specific evaluation platform or paid service is required.
