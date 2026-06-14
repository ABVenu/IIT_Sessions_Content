lecture ID:

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

title: Tool Integration in AI Agents

objective: Learn how agents use external tools and APIs to perform actions

type of session: mixture of theory + implementation

topics be covered: function calling;connecting APIs and tools


detailed subtopics to be covered:

- This session: implementation-leaning mixture — extend Session 23 fetch-and-parse skills into agent tool use; wire the ShopKart assistant so the model can choose between policy retrieval (RAG) and a live weather API tool, then synthesise a customer reply with Groq; close Module 2 by tracing one full agentic action from user query to tool result to final answer
- Understand Function Calling — How Agents Choose Tools — Learners explain that an agent does not hard-code every branch; the model reads tool descriptions and selects a function (e.g. search policy documents vs fetch live weather) based on the user query; contrast this with the fixed GET-then-print flow from Session 23;
- Register Python Functions and API Wrappers as Agent Tools — Learners define callable tools with clear names and input schemas (city name, coordinates, or policy query); wrap the Session 23 weather GET helper and a RAG retrieval helper as separate tools the runtime can invoke and return structured JSON from;
- Run the Tool Execution Loop — Call, Return, Continue — Learners execute the model → tool call → Python function → JSON result → model reply cycle; handle tool errors (non-200 API, empty retrieval) with safe messages instead of invented facts;
- Combine RAG and Live API Data in One ShopKart Reply — Learners demonstrate a customer question that needs both policy context and live weather (e.g. express delivery during rain in a metro city): retrieve grounded policy excerpts, call the weather tool, route extracted JSON fields into a single Groq prompt, and produce a final answer that cites policy rules and live conditions without hallucinating either source;