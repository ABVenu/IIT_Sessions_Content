lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: Capstone Project Phase — Build

objective: Freeze Nimbus PayDesk, draw a one-page architecture, implement the LangGraph core, and sit the golden eval. (Invoice exception desk; no NEFT.)

type of session: mixture of theory + implementation

topics be covered: Requirements; architecture sketch; implementation; integration testing


detailed subtopics to be covered:
* Select a capstone scenario with clear users; data; and success criteria.
* Produce a one-page architecture: RAG; tools; memory; orchestration; deploy path.
* Implement core flows to meet requirements with versioned prompts.
* Run integration tests from the golden set and fix blocking defects.

* Nimbus PayDesk: cut 9-day AP wait; no live NEFT
* Chroma handbook, GST/PO tools, sqlite3 + graph state, LangGraph, Streamlit next
* extract → policy → route on InvoicePacket; prompts/extract_v1.txt; Python gates
* G01 CLEAN ready; G02 HIGH amount_gate; G03 BADGST gst_mismatch; fail closed if Chroma is empty
