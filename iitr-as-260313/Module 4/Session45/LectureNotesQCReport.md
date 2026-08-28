# Lecture Notes QC Report — make.com and ChatGPT Hosted Agents

## Redesign note (Session 44 make.com + Session 45 hosted agents → one Session 45)

This is not a concatenation of the old make.com lab and the old hosted-agent lab. One Greenfield Campus Ops morning grows from a **form junction** into a **night concierge**. Session 44’s make.com topic is taught here as the first product; ChatGPT / hosted agent builders remain the second product.

### Four Session 45 learning objectives (combined / updated)

1. Assemble a make.com scenario with a trigger, an AI-powered transformation, a router, and an action to email or a spreadsheet.
2. Compare no-code scenarios and hosted agent builders with code-first frameworks across control, flexibility, cost, and who maintains the system.
3. Configure a ChatGPT-style hosted agent with knowledge boundaries, action permissions, instructions, and guardrails.
4. Test one make.com success path and demonstrate the hosted agent on in-domain and refusal queries with explainable behaviour.

### Learning objectives removed or folded (so the live session stays one sitting)

| Old source | Old LO / topic | What happened |
|---|---|---|
| Session 44 | Explain how make.com scenarios differ from code-first automation | Folded into the three-vehicle comparison (LO 2) |
| Session 44 | Connect output actions to email / CRM / spreadsheet (standalone LO) | Folded into assemble (LO 1) — Gmail + `Enquiry_CRM` stay in the click path |
| Session 44 | Test and document one recoverable error path (standalone LO) | Cut as a full objective. Notes still forbid **Ignore** on Gmail and mention a `Needs_Human` route |
| Session 44 | Data stores, scheduling, HTTP modules (full labs) | Named in building blocks only — not built in class |
| Session 45 (old) | Compare hosted vs code-first (standalone LO) | Folded into the same three-vehicle comparison (LO 2) |
| Session 45 (old) | Define instructions and guardrails (standalone LO) | Folded into configure (LO 3) |

---

## QC Iteration 1

| Criteria | Result |
|---|---|
| Content Coverage | 4/5 |
| Creativity | 4/5 |
| Structural Adherence | 4/5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | False |
| No Previous Session Number References | True |
| No Metadata/Internal References | True |

**Notes:** Combined story was present (enquiry form + leave/placement desk). Issues found:

1. **Structure:** First combined draft sat **above** the 500-line cap (`570`), then **below** the 480-line band (`452`) after a hard cut.
2. **Coverage:** Data stores / scheduling / HTTP vanished instead of being named as “hear, do not build.” Recoverable-error discipline was missing (Ignore vs Needs_Human).
3. **Presentation:** A building-blocks paragraph ran past the 3-sentence rule. Knowledge extracts were too compressed for D1/D2 to be replayable.
4. **Creativity:** Missing bundle-inspection table and hosted failure-mode table after the two products were fused.

**Improvisation applied:** Restored parseable knowledge extracts; added bundle-mapping table, hosted failure-mode table, and an explicit Ignore / `Needs_Human` line; split the data-store / scheduling / HTTP paragraph; brought line count into the 480–500 band.

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

**Notes:** Re-read after improvisation. Context bridges from the **previous** multi-agent dialogue session without session numbers. **Upcoming** work is LLM ops, deployment, and governance. No duration, audience, or “keep it lite” leakage. Official Definition / In Simple Words / Real-Life Example on core terms. Student-facing activities (not “Ask students…”). Click-path configuration + mermaid (no fake make.com export or vendor JSON). Key Takeaways + terminology table present. Forbidden stack words absent. Line count within range (`490` lines; max 500).

### Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Assemble a make.com scenario with trigger, AI transformation, router, and email or spreadsheet action | Click Path — Trigger and AI Stamp; Router, Email, and Sheet |
| Compare no-code scenarios and hosted builders with code-first frameworks | Three Vehicles, One Destination; From Junction to Concierge |
| Configure a ChatGPT-style hosted agent with knowledge, action permissions, instructions, and guardrails | Concierge Model; Click Path — Create, Instructions, Knowledge; Actions, Permissions, Guardrails |
| Test one make.com success path and demonstrate in-domain and refusal queries with explainable behaviour | Test Plan — One Golden Success Path; Demonstrate — In-Domain and Refusal |

**Outcome:** QC passed on iteration 2 after improvisation from iteration 1.
