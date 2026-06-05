lecture ID: 155989

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr 50mins

title: RAG Architecture and Pipeline

objective: Learn the key components involved in a RAG system pipeline


type of session: implementation

topics be covered: retriever;generator;knowledge sources


detailed subtopics to be covered:

- This session: hands-on implementation — build a minimal working RAG loop for the e-commerce customer support assistant; reuse the Session 18 Chroma vector search setup as the retriever layer (top-k tuning and metadata filtering deferred to Session 22)
- Frame Customer Support as a RAG Problem — Learners articulate the assistant's purpose, users, and knowledge boundaries — and identify which policy documents (returns, shipping, warranty, refund) constitute the knowledge base;
- Demonstrate Semantic Retrieval of Relevant Policy Content — Learners show that a customer query retrieves the most relevant policy excerpt from the knowledge base — and can judge whether retrieval matched the question's intent;
- Produce Answers Grounded in Retrieved Evidence — Learners generate responses that reflect retrieved policy text rather than the model's general knowledge — and can explain how context shapes the output;
- Validate a Minimal RAG Pipeline Against an LLM-Only Baseline — Learners run the full retrieve → generate loop on representative queries and justify why grounded answers are more accurate than standalone LLM responses, connecting back to Session 19;

