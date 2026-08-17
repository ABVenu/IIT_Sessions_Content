lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: Prototyping a Multi-Agent System

objective: Build a functional multi-agent prototype with tools, SQL, RAG, automation hook, and an eval loop. (Nimbus PayDesk: CLEAN ready; HIGH and BADGST gated.)

type of session: implementation

topics be covered: Multi-agent implementation; tool integration; memory setup; iterative development


detailed subtopics to be covered:
* Implement tools the agents can call (GST check, PO lookup, policy retrieve, and append-only ticket logging.)
* Build a sequential multi-agent pipeline with LangChain (extract → policy → route on the PayDesk InvoicePacket.)
* Connect SQL as working and episodic memory (ticket row after pipeline; find_duplicate on vendor + amount + date.)
* Connect the RAG pipeline with Chroma DB (seed data/policy.md; retrieve_policy; fail closed if the store is empty.)
* Attach a human-approval path on the API (POST /tickets/{id}/stamp; router queues needs_human and must not approve.)
* Create an n8n workflow and attach it to the system (HTTP Request to POST /ingest; alert when status is needs_human.)
* Evaluate and iterate on live cases (INV-CLEAN ready_to_pay; INV-HIGH amount_gate; INV-BADGST gst_mismatch; one targeted fix.)
