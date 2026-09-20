lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI / Software Development with Applied AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: Masterclass LangSmith: LLM Application Evaluation & Monitoring

objective: Introduce LangSmith as the evaluation and monitoring layer for LangGraph apps students already build (nodes, edges, state, checkpoints, retries), then ship one end-to-end T20 Match Desk lab — tracing, nested spans, a golden dataset, an experiment with evaluators, one controlled patch, and project-level monitoring. Do not assume LangChain as prior learning.

type of session: mixture of theory + implementation

topics be covered:
LangSmith foundations; traces and nested spans; tracing LangGraph; datasets; experiments; custom evaluators; experiment comparison after a patch; monitoring (latency, tokens, errors)

detailed subtopics to be covered:

* Open with a direct intro to LangSmith — definition, building blocks (trace, span, dataset, experiment, evaluator, monitoring), advantages, disadvantages, and how it differs from a local golden pack / print-trace (not a scenario-first framework intro).
* Students already know LangGraph (nodes, edges, shared state, checkpoints, retries) plus Groq and golden questions on graphs — use that as prior context without session numbers. Do not treat LangChain / LCEL / AgentExecutor as previous work (one batch has not learnt LangChain).
* Turn on tracing with LANGSMITH_TRACING, LANGSMITH_API_KEY, LANGSMITH_PROJECT; mention LANGCHAIN_TRACING_V2 for graph eval traces; never hard-code keys.
* Phase 1: one LangGraph invoke so a graph run appears in the LangSmith project before the four live tickets.
* One file (`t20_langsmith_lab.py`), three phases: Phase 1 graph trace, Phase 2 T20 Match Desk LangGraph (classify → rules | incident | refuse), Phase 3 dataset + evaluate() + one patch comparison.
* Domain: T20 Match Desk — rulebook answers, INC-id lookup, polite refusal — LangSmith is the new layer on a graph they already know how to draw.
* Nested spans: graph run → classify (ChatGroq) → @traceable extract_incident_id / lookup_incident; teach that evaluate() experiments live under Datasets, not only the default project run list.
* Custom evaluators: route_match and keywords; empty-keyword refusal scored on route only (N/A, not a fake keyword PASS).
* Monitoring: project tiles for errors, latency, tokens, and experiment pass rate; one controlled prompt patch then compare t20-desk-v1 vs t20-desk-v2.
* Stack matches this batch: ChatGroq, GROQ_API_KEY, llama-3.1-8b-instant, langgraph StateGraph, langsmith Client + evaluate.
