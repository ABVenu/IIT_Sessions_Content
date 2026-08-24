# Lecture Notes QC Report — LLM Operations, Security and Guardrails for Agent Systems

## QC Iteration 1

| Criteria | Result |
|---|---|
| Content Coverage | 5/5 |
| Creativity | 5/5 |
| Structural Adherence | 4/5 |
| No Logical Mistakes | False |
| No Presentation Mistakes | False |
| No Previous Session Number References | True |
| No Metadata/Internal References | True |

**Notes:** Metadata topics were present (versioning, regression eval gate, tokens/cost, secrets, access, PII, input/output guardrails, policy layers, human-in-the-loop, release decision). Tuesday incident story (invented rule, PII leak, cost spike, key in Slack) matches the running Greenfield desk. Issues found:

1. **Logical / presentation:** `os.environ.get("OPENAI_API_KEY")` was called and discarded — looked like a no-op rather than an ops check.
2. **Structure:** First draft sat **below** the 480-line band; missing a faculty-readable eval report table and a collect-answers / incident-order section.
3. **Presentation:** Need an explicit warn when the environment variable is missing, without printing the secret.

**Improvisation applied:** Assigned the key to a variable and printed a **WARN** if unset (never the key value). Added candidate-answer collection, four-incident fix order, and a NO-GO eval report table. Line count brought into the 480–500 band. Every Python line remains commented; “How the code works” list present.

---

## QC Iteration 2

| Criteria | Result |
|---|---|
| Content Coverage | 5/5 |
| Creativity | 5/5 |
| Structural Adherence | 5/5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |
| No Previous Session Number References | True |
| No Metadata/Internal References | True |

**Notes:** Re-read after improvisation. Context bridges from the **previous** hosted-agent session without session numbers. **Upcoming** work is deployment, monitoring, governance, and business design. No duration, audience, or “keep it lite” leakage. Official Definition / In Simple Words / Real-Life Example on core terms. Student-facing activities. Eval-gate / guardrail sketch is a full commented script with JSON fixtures. Key Takeaways + terminology table present. Forbidden stack words absent (JSON, environment variables, REST endpoint used instead). Line count within range (`482` lines; max 500).

### Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Describe an LLM Ops workflow for versioning prompts, tools, and retrieval configs with pre-release evaluation against a regression set | Versioning; Regression Set; Eval Gate |
| Design security controls for secrets, access boundaries, and sensitive data handling | Secrets, Access, and PII; Incident Walkthrough |
| Implement or configure guardrails that filter unsafe, out-of-scope, or non-compliant inputs and outputs | Airport Lanes; `input_ok` / `output_ok` in the sketch; Policy Layers |
| Relate token usage, cost signals, and quality metrics to release decisions for a representative agent change | Cost Signals and the Release Decision; Fill an Eval Report |

**Outcome:** QC passed on iteration 2 after improvisation from iteration 1.
