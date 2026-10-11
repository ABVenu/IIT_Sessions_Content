# Final Course Revision — Instructor Pickup

Four theory sessions, about 1 hour 50 minutes each. Teach concepts, edge cases, and how to tell one failure from another. Do not build an application in class.

Notes for each session are in that session’s `Lecture Notes.md`. Close the class in this order: self-check, the short student activity, Key Takeaways, then the terminology table.

Stay on the shared topics below. Leave out classical machine learning, NumPy, Pandas, plotting, and framework-only tracks such as n8n, CrewAI, AutoGen, and make.com.

## Session 1 — Python Foundations and Version Control

- Environment: PATH, terminal, virtual environment, `.py` versus notebook, where an API key belongs (`.env`, never committed).
- Variables and types: `int`, `float`, `str`, `bool`, case sensitivity, aliasing (two names, one list).
- Operators: `/` versus `//`, precedence, `=` versus `==`, short-circuit `and` / `or`.
- Decisions and input: one branch of an `if` / `elif` chain, indentation, `input()` is always text, f-strings.
- Loops: `while` must move toward stopping, `for` and `range` (stop is excluded), `break` leaves only the inner loop, `continue`.
- Lists, strings, dictionaries: slicing excludes the end, `append` versus `extend`, `sort` versus `sorted`, immutability of strings, `[]` versus `.get`, `in` checks keys.
- Functions: `return` versus `print`, scope, never use a list or dict as a default argument.
- Classes: class versus object, `self`, `__init__` runs on creation, each object has its own state.
- Git: working directory, staging, commit, push versus pull, branches, pull request is a review request, restore versus reset, ignore secrets before they enter history.
- Activity: predict `backup` and `bill` before running the short snippet (`append` shares the list; `print` does not return a value).

## Session 2 — Agents, Language Models, Prompts, and Memory

- Agent: observe, think, act. Planning, reasoning, memory, and action. The model decides. Tools change the world. The loop needs a stop rule.
- Human approval for actions that are hard to undo.
- How a model behaves: next-token prediction, hallucination, knowledge cutoff, tokens, context window, temperature, local versus hosted models.
- Prompts: system, user, and assistant roles. Role, task, instructions, constraints, output format.
- Zero-shot, few-shot, and chain-of-thought, and when the extra tokens are worth it. Examples that contradict the rule usually win.
- Self-correction: draft, check, rewrite, with a retry limit. User feedback versus an internal check.
- Memory: stateless versus stateful. Short-term versus long-term. Buffer, window, and summary. Episodic, semantic, and procedural.
- What must be pinned (order id, a real decision) and what must not be stored (secrets, guesses). A session id isolates one chat. A restart forgets an in-memory list.
- Activity: write a five-part prompt for a 20-day return question, with a legal “unknown”, and mark which facts stay pinned.

## Session 3 — Databases, Embeddings, and Retrieval-Augmented Generation

- Why a table replaces a spreadsheet once many people, or an agent, share the data.
- Keys and constraints: primary key, foreign key, one-to-many, many-to-many through a junction table, normalisation.
- SQL: `SELECT`, `WHERE`, `LIKE`, `ORDER BY`, `LIMIT` / `OFFSET`, `INSERT`, `UPDATE`, `DELETE`. A write without `WHERE` hits every row.
- Joins: inner, left, and cross. `IS NULL` is the test for a missing value. Clause order is `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `SELECT`, `ORDER BY`, `LIMIT`.
- Embeddings: same model for documents and questions, cosine similarity, nearest is not the same as relevant. Exact search versus approximate search.
- Chunking: too small splits a rule from its exception, too large mixes topics, overlap, metadata for filter and citation, same-id upsert versus a duplicate.
- RAG: ingest offline, answer online. Retrieve, augment, generate. Grounding. Delimit context so a document cannot act as a new instruction.
- Name the failure before changing anything: retrieval failure versus generation failure. Top-k, metadata filters, query expansion, re-ranking, compression, and a cache that must expire.
- Activity: for “status of order 18”, use the table and name the filter that keeps other customers’ rows out. For “written window for damaged items”, use the vector store, then say whether a wrong answer is a retrieval failure or a generation failure.

## Session 4 — Tools, Safety, Orchestration, and Operations

- HTTP and JSON: `GET` versus `POST`, status codes worth acting on (200, 201, 400, 401, 403, 404, 429, 500). Parse the body only after the status. Do not retry a create blindly.
- Tool loop, also called ReAct: thought, action, observation. The model requests a call, the program runs it, the result goes back. The description routes the call. Validate arguments. Cap the loop.
- Static retrieval always searches. Agentic retrieval may search zero or more times and needs a stop.
- LangChain, as the same loop in parts: prompt template, pipe composition (prompt, then model, then parser), `bind_tools`, `tool_calls` as data, tool message with the call id.
- `create_tool_calling_agent` takes the model, tools, and prompt, not memory. Memory sits beside the loop. The executor caps retries (a small default, often three). In-memory history dies on restart. The scratchpad is only the current turn. A retriever can be one tool next to a table tool.
- Shared tool protocol (MCP): fewer one-off integrations. It does not replace good tool design, permissions, or retries.
- Structured output: schema, parse, then validate. “Valid JSON” can still be a wrong business result. Unknown must be a legal value.
- Safety: prompt injection in the user box or in a retrieved chunk, input checks, output checks, allow-list of tools, read-only queries unless a person approves a write, mask private data.
- Graphs: node, edge, shared state. Sequential, parallel, and conditional flow. One orchestrator can hand work to narrow roles. The user should not be talking to every role. Checkpoints and thread id resume a pause. They do not fix a bad result already stored. Timeouts, backoff with jitter, human approval as a pause.
- Evaluation: judge the whole trajectory, not only the last sentence. Golden cases include refusals. Clear memory between cases. Groundedness versus context relevance.
- Release shape: client, API, agent, store. Secrets in the environment. Ingestion off the live request. Traces with secrets removed.
- Cost: harm of being wrong before model choice. Output tokens usually cost more. Buffer for retries. Cache only what is safe to reuse, and expire it when the source changes.
- Activity: for “Cancel order 18”, name the tool that must run, the tool that must not, which status code may be retried (429, not 401), and where a person approves the write.
