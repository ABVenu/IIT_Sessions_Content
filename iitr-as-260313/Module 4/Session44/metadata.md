lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: LangGraph: Building an End-to-End AI Agentic Workflow

objective: Assemble a production-style LangGraph workflow with specialist nodes, persisted checkpoints, a human approval gate, and graceful failure, then prove it on a small golden set.

type of session: mixture of theory + implementation

topics be covered: specialist nodes; policy router; ToolNode; checkpointer; thread ID; MemorySaver; SqliteSaver; interrupt; Command; human-in-the-loop; RetryPolicy; timeouts; fail-closed errors; golden eval; traces

detailed subtopics to be covered:
* Assemble an end-to-end LangGraph workflow with specialist nodes, tool calls, and a Python policy router that cannot self-approve a high-risk action.
* Persist and resume a run with a checkpointer and thread id, including a planned human approval pause.
* Apply timeouts and bounded retries on a flaky tool step, and surface a clear error when retries are exhausted.
* Run a three-case golden pack (clean / blocked / human-gate) and use traces plus checkpoint payloads to explain each outcome.
