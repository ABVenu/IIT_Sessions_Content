lecture ID:

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr 50mins

title: RAG Architecture and Pipeline

objective: Learn the key components involved in a RAG system pipeline


type of session: implementation

topics be covered: retriever;generator;knowledge sources


exsiting detailed subtopics to be covered (2.5 hours):

🎯 What Should Be Done in This Session - Important 

In this session, students should move beyond the introductory theory of RAG and begin working with a minimal functional RAG architecture. Using the e-commerce support use case, learners should understand how the main components of a RAG system interact in practice: the knowledge source (company policy documents), the retriever (fetches relevant information), and the generator (LLM that creates final responses). By the end of the session, students should observe how retrieval improves response quality compared with a standalone language model.

🔹 Detailed Subtopics / Learning Objectives
* Define the E-Commerce RAG Use Case — Establish the goal of building a customer support assistant using company policy documents;
* Identify Knowledge Sources for the System — Work with a small set of policy documents such as returns, shipping, warranty, and refund policies;
* Set Up a Minimal RAG Environment — Configure required libraries and reuse the previously built vector search system;
* Implement the Retriever Component — Retrieve relevant policy content based on customer queries;
* Inspect Retrieved Policy Content — Analyze whether retrieved results match the intent of the query;
* Implement the Generator Component — Use an LLM to generate responses based on retrieved policy content;
* Inject Retrieved Context into Prompts — Structure prompts so policy content is included as grounding context;
* Build a Minimal End-to-End RAG Flow — Execute: query → retrieve policy content → generate response;
* Compare Responses With vs Without Retrieval — Observe how grounded responses differ from standalone LLM outputs;
* Experiment with Retrieval Depth (Top-K) — Analyze how the number of retrieved items affects response quality;
* Trace Component Interaction in the Workflow — Understand how retriever and generator work together during execution;


		