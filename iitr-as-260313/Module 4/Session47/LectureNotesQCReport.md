# Lecture Notes QC Report — Deployment and Monitoring for Agent Systems

**File reviewed:** `Lecture Notes.md`  
**Batch / folder:** `iitr-as-260313/Module 4/Session47`  
**Review date:** 2026-08-24

---

## Iteration 1

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All four metadata subtopics present: deployment options and hosting/runtime justification; observability (measure, trace, alert) across agent/tool/retrieval; logging of inputs, decisions, tool traffic, retrieval, errors, outcomes plus audit fields; monitoring workflows tied to incident response. Topics: strategising deployment, hosting, environments, observability, logging, traces, performance, incident planning. |
| **Creativity** | **5 / 5** | Running story (Ananya’s campus support agent on a WhatsApp-like channel) plus fintech WhatsApp twin; airport control-tower analogy; courier/PNR/canteen/fest-lighting examples. |
| **Structural Adherence** | **4 / 5** | Clean `#` title, previous/upcoming wording, Official/Simple/Real-Life, student-facing activities, commented Python + “How the code works,” Key Takeaways, terminology table. **Gaps:** “Run it” and the sixty-second defence activity packed more than three sentences into one paragraph. |
| **No Logical Mistakes** | **True** | Hybrid on-prem circulars vs vendor chat is consistent. Toy alert threshold matches the sleep-demo instruction. Redaction of the demo phone number is correct. |
| **No Presentation Mistakes** | **False** | 3-sentence rule breached in the post-script “Run it” paragraph and the sixty-second defence activity. |
| **No Previous Session Number References** | **True** | Uses **previous** / **upcoming** only. |
| **No Metadata/internal reference** | **True** | No duration, audience, or “lite” leakage in student notes. |

### Expected Result

- Content Coverage, Creativity, Structural Adherence: all **≥ 5** — **Not met** (Structural Adherence 4)
- Logical / Presentation flags must be **True** — **Not met** (presentation)

**Outcome:** QC **failed** on iteration 1. Notes improvised: split the “Run it” instruction; rewrote the defence activity as four short lines plus a closing sentence.

---

## Iteration 2

**Re-review after improvisation.** Demo script extracted and executed:

```
{"run_id": "CAMP-8842", ..., "step": "input", "query": "mess rebate June, call [PHONE]", "pii_redacted": true}
{"run_id": "CAMP-8842", ..., "step": "retrieve", "chunk_ids": [...], "index": "prod-v3"}
{"run_id": "CAMP-8842", ..., "step": "tool", "tool": "create_ticket", "status": "ok"}
{"run_id": "CAMP-8842", ..., "step": "alert", "rule": "latency_high", "fired": false}
```

Line count: **492** (metadata cap 480–500).

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Subtopic map below. Extra but on-brief: sampled quality, alert hygiene, SEV levels, campus vs fintech comparison table. |
| **Creativity** | **5 / 5** | Campus go-live + external fintech example; mermaid for runtime path, observability, and incident flow (no new S3 images). |
| **Structural Adherence** | **5 / 5** | `#` title only; context from previous LLM-Ops / guardrails / release gates without numbers; connecting sentences; Official/Simple/Real-Life on core terms; full commented Python; student-facing activities; Key Takeaways; terminology table. |
| **No Logical Mistakes** | **True** | HTTP API / n8n / CrewAI schedule named as runtimes (no FastAPI/Pydantic). Environments catch the Sunday index-path bug. Incident playbook matches the 45-second tool-timeout story. |
| **No Presentation Mistakes** | **True** | Long paragraphs split; activities not written as “Ask students to…”. |
| **No Previous Session Number References** | **True** | Confirmed. |
| **No Metadata/internal reference** | **True** | Confirmed. |

### Expected Result

- Content Coverage, Creativity, Structural Adherence: all **≥ 5** — **Met**
- No Logical Mistakes, No Presentation Mistakes, No Previous Session Number References, No Metadata/internal reference: **True** — **Met**

**Outcome:** QC **passed** on iteration 2.

---

## Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Compare deployment options and justify hosting/runtime for a scenario | Deployment Options and Hosting Strategy; Runtime Choices; Compare Two Scenarios; One Go-Live Picture |
| Design an observability plan (measure, trace, alert) across agent, tool, retrieval | Observability — Measure, Trace, Alert; Sampled Quality and Alert Hygiene |
| Specify a logging strategy for inputs, decisions, tool traffic, retrieval, errors, outcomes | Trace and Audit Fields; Logging Agent Decisions; `campus_support_log.py` |
| Relate monitoring and performance signals to operational response | Monitoring Workflows; Incident Response Planning; SEV table |

| Topic from metadata | Where covered |
|---|---|
| strategising deployment | From a Tested Agent to a Live System; hosting tables |
| hosting and runtime choices | Hosting Strategy; Runtime Choices mermaid |
| environments | Environments — Keep Risk in Separate Rooms |
| observability | Observability section + mermaid |
| monitoring workflows | Monitoring Workflows table |
| logging agent decisions | Logging Agent Decisions; decision field in script |
| trace and audit fields | Trace and Audit Fields table |
| performance tracking | Metrics table; sampled quality; p95 |
| incident response planning | Incident mermaid + playbook + SEV |

---

## Prompt / length checks

| Check | Result |
|---|---|
| Starts with `# Lecture Title` only | Pass |
| No session numbers | Pass |
| No duration / audience / internal “lite” wording | Pass |
| No FastAPI / Pydantic / SQLAlchemy | Pass |
| Student-facing activities (not instructor prompts) | Pass |
| Full code with per-line comments + How the code works | Pass |
| Key Takeaways (3–5 bullets) + future link without session numbers | Pass |
| Terminology / commands table | Pass |
| Mermaid used instead of new S3 images | Pass |
| Line count vs metadata 480–500 max | **492** — Pass |
