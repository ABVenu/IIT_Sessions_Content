# Lecture Notes QC Report — Designing a Multi-Agent System for Business

**File reviewed:** `Lecture Notes.md`  
**Batch / folder:** `iitr-as-260313/Module 4/Session49`  
**Review date:** 2026-08-24

Adapted from the `iitr-as-260113/Module4/Session58` QC, with path and running-story updates only. Nimbus Retail invoice desk, code, mermaid, tables, and existing S3 image URLs (`iitr-as-260113/module4/session58/...`) are kept.

---

## Iteration 1

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All four metadata subtopics covered: problem→workflow mapping with roles/tasks/handoffs; tools, data sources, and human gates; diagram + dual stakeholder narrative; risks, limitations, and metrics. Topics present: workflow diagram, agent roles, handoffs, tool and data map, risks, success metrics, finance/HR/content scenarios. |
| **Creativity** | **5 / 5** | Running story (Nimbus Retail AP desk) with **Ananya** applying campus-ops discipline; India-relatable analogies: passport seva, wedding planner, kirana FAQ, bank branch, pathology report, hospital EMR, UPI vs large transfer, IRCTC, college fest reimbursements, local-train scoreboard. |
| **Structural Adherence** | **4 / 5** | Clean `#` title, previous/upcoming wording, Official/Simple/Real-life pattern, student-facing activities, Key Takeaways, terminology table. **Gaps found (inherited from source iteration 1, already fixed in the adapted file):** a few paragraphs had exceeded the 3-sentence rule; demo loop double-stamped INV-2; `@dataclass` continuation lines needed per-line comments. |
| **No Logical Mistakes** | **False** | Source iteration 1: demo `human_stamp` ran twice on INV-2; sample GSTINs looked like real tutorial IDs; exception router named in design but missing from runnable spec. Adapted file already contains those source iteration-2 fixes. |
| **No Presentation Mistakes** | **False** | Source iteration 1: 3-sentence rule breached in running story, problem-statement quote, and stakeholder narratives — already trimmed in the file copied forward. |
| **No Previous Session Number References** | **True** | Uses **previous** (governance) / **upcoming** (capstone) only. |
| **No Metadata/internal reference** | **True** | No duration, audience, “keep it lite”, or internal instruction leakage. |

### Expected Result

- Content Coverage, Creativity, Structural Adherence: all **≥ 5** — **Not met** (Structural Adherence 4, as in source iteration 1)
- Logical / Presentation flags must be **True** — **Not met**

**Outcome:** QC **failed** on iteration 1 (same defect class as source). The adapted notes already include the source improvisations: 3-sentence trims, dummy GSTIN `29AAAAA0000A1Z5`, single human stamp, `route()` added, per-line comments, plus Ananya as designer without gutting Nimbus. No FastAPI/Pydantic present.

---

## Iteration 2

**Re-review after improvisation.** Demo script extracted and executed:

```
INV-1 ready_to_pay []
INV-2 routed_to tax_desk
INV-2 rejected ['gst_mismatch', 'po_missing', 'amount_gate', 'human_rejected']
report {'total': 2, 'ready': 1, 'rejected': 1}
```

Line count: **499** (metadata cap 480–500).

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Subtopic map below. Extra but on-brief: six-box canvas, capstone checklist, fail-closed limitation, HR/content comparison table. |
| **Creativity** | **5 / 5** | Nimbus storyline retained; Ananya frames the designer role; S3 diagrams kept; mermaid workflow; runnable mock without API keys. |
| **Structural Adherence** | **5 / 5** | `#` title only; context from previous governance session without numbers; upcoming is capstone only; connecting sentences between canvas → problem → roles → handoffs → tools → gates → diagram → code → risks → HR/content → checklist; Official/Simple/Real-life on core terms; full commented Python + “How the code works”; student-facing activities; Key Takeaways; terminology table. |
| **No Logical Mistakes** | **True** | INV-1 never hits a gate; INV-2 type-check then policy then tax_desk reject; payment stays out of scope; dummy GSTIN; reporter cannot NEFT. |
| **No Presentation Mistakes** | **True** | Long paragraphs split; no duration/audience; activities not written as “Ask students to…”. |
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
| Map a business problem to a multi-agent workflow with explicit roles, tasks, and handoff points | Choosing a Business Problem; Mapping Nimbus Retail; Agent Roles; Handoffs |
| Specify data sources, tools, and human approval gates for a trustworthy solution | Tools and Data Map; Human Approval Gates |
| Produce a workflow diagram and narrative for technical and non-technical stakeholders | Workflow Diagram and Stakeholder Narrative (text + mermaid + CFO vs engineer) |
| Identify risks, limitations, and evaluation metrics | Risks, Limitations, and Evaluation Metrics; HR/content canvas reuse |

| Topic from metadata | Where covered |
|---|---|
| workflow diagram | Workflow Diagram section + mermaid + image 01 |
| agent roles | Agent Roles table (Intake, Extractor, Policy, Router, Reporter) |
| handoffs | Handoffs JSON packet + `Packet` dataclass |
| tool and data map | Tools and Data Map table + image 03 |
| risks | Risks table + image 04 |
| success metrics | Success metrics table |
| finance HR or content scenario | Nimbus finance worked example; HR and content comparison canvas |

---

## Prompt / length checks

| Check | Result |
|---|---|
| Starts with `# Lecture Title` only | Pass |
| No session numbers | Pass |
| No duration / audience / internal “lite” wording | Pass |
| No FastAPI / Pydantic / SQLAlchemy | Pass |
| Existing S3 URLs kept (`iitr-as-260113/module4/session58/...`) | Pass |
| Student-facing activities (not instructor prompts) | Pass (Fit Test, Missing Role, Threshold, Two Metrics) |
| Full code with per-line comments + How the code works | Pass |
| Key Takeaways (3–5 bullets) + upcoming capstone without session numbers | Pass |
| Terminology / commands table | Pass |
| Line count vs metadata 480–500 max | **499** — Pass |
