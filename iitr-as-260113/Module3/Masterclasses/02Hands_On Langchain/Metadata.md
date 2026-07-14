lecture ID:

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

title: Hands_On Langchain II — UPI Dispute Desk

objective: A second Module 3 hands-on that rebuilds the full LangChain stack in a new domain (UPI dispute desk) and deepens evaluation, structured logging, and controlled debug iteration.

type of session: implementation

topics be covered:
All Module 3 LangChain foundations (Sessions 35–41) plus evaluation harness and debug iteration patterns (Sessions 42–43), practiced on a fresh domain distinct from the T20 masterclass and course-ticket / HR classroom examples.


detailed subtopics to be covered:

* Recap Module 3 concept map briefly — LCEL, tools, AgentExecutor, memory, RAG, integrated agent, EvalPack, failure-class fixes — then dive into a new product domain.
* One file (`upi_dispute_assistant.py`), three phases: Phase 1 LCEL warm-up, Phase 2 build integrated UPI Dispute Desk, Phase 3 EvalHarness + debug-and-patch.
* Domain: UPI payment dispute help desk (not cricket, not e-commerce course tickets) — RAG over UPI FAQ handbook + transaction status tool.
* Phase 2: Document ingest, Chroma, create_retriever_tool, get_transaction_status, AgentExecutor, chat_history, ask().
* Phase 3: structured eval cases, printable results log, failure signatures, one controlled prompt/tool/retrieval patch with before/after comparison.
* Keep code minimal — ChatOllama, OllamaEmbeddings, essential langchain-core/classic/chroma packages only; line comments on key code lines.
