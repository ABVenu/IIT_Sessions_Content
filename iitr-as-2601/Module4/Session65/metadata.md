lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 2hr 30mins

Session Notes Length: 540 lines to 600 lines max

title: Capstone Project Phase — Build

objective: Freeze Nimbus PayDesk, draw a one-page architecture, implement the LangGraph core, and sit the golden eval. (Invoice exception desk; no NEFT.) Extra time is lab, not a second product.

type of session: mixture of theory + implementation

topics be covered: Requirements; architecture sketch; implementation; integration testing


detailed subtopics to be covered:
* Select a capstone scenario with clear users, data, and success criteria *(Nimbus PayDesk: cut 9-day AP wait; no live NEFT)*
* Produce a one-page architecture: RAG, tools, memory, orchestration, deploy path *(Chroma handbook, GST/PO tools, sqlite3 + graph state, LangGraph, Streamlit next)*
* Implement core flows to meet requirements with versioned prompts *(extract → policy → route on InvoicePacket; prompts/extract_v1.txt; Python gates)*
* Run integration tests from the golden set and fix blocking defects *(G01 CLEAN ready; G02 HIGH amount_gate; G03 BADGST gst_mismatch; fail closed if Chroma is empty)*
