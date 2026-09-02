lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI / Software Development with Applied AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: Hands_On LangChain

objective: Introduce LangChain as a first-class toolkit (contrasted with LangGraph they already know), then build one end-to-end integrated agent with LCEL, RAG, tools, memory, and a compact eval pack.

type of session: mixture of theory + implementation

topics be covered:
LangChain foundations; LCEL; LangChain vs LangGraph; tools and AgentExecutor; conversational memory; retriever tool (agentic RAG); integrated end-to-end app; compact EvalPack

detailed subtopics to be covered:

* Open with a direct intro to LangChain — definition, building blocks, advantages, disadvantages, how it differs from LangGraph, and real-life applications (not a scenario-first framework intro).
* Students already know LangGraph (nodes, edges, shared state, checkpoints, retries) plus RAG, tools, Groq, and golden evals — use that as prior context without session numbers.
* LCEL warm-up: ChatPromptTemplate | ChatGroq | StrOutputParser.
* One file (`t20_rules_assistant.py`), three phases: Phase 1 LCEL, Phase 2 integrated T20 Rules & Match Inquiry Assistant, Phase 3 EvalPack.
* Domain: T20 cricket rules assistant — RAG over a short rulebook + live match incident tool + multi-turn memory + polite refusal.
* Phase 2: Document ingest, HuggingFace embeddings, Chroma, create_retriever_tool, get_match_incident, AgentExecutor, chat_history, ask().
* Phase 3: compact keyword EvalPack, results log, failure signatures, one controlled patch.
* Stack matches this batch: ChatGroq, GROQ_API_KEY, all-MiniLM-L6-v2, essential langchain-core / groq / chroma / classic packages.
