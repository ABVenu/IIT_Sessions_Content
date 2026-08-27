# Final Capstone — Naukri.com Domain Support Agent (LangGraph)

**Track: Recruitment & HR (Naukri.com).** **Estimated duration: 14 days.**

Real production support agents combine several building blocks into one working
system: dataset design, knowledge-base chunking and embedding, vector retrieval,
grounded generation, agent memory, tool-using agents, structured outputs, guardrails,
multi-agent orchestration, evaluation, resilience (timeouts/retries/checkpointing),
protocol standardization (MCP), and API deployment. This capstone asks you to bring
all of it together into ONE working, production-minded agent: a domain support agent
that answers policy questions from a knowledge base you write, looks up real records
from a dataset you design and validate yourself, remembers a conversation, is guarded
against misuse, survives interruptions and transient failures, and exposes its tools
in a standardized, reusable way — orchestrated with LangGraph, deployed behind a
FastAPI backend, and evaluated end to end.

Naukri.com's employer-support team wants an agent that answers hiring-policy questions
and checks a specific job application's status, so recruiters and candidates get
instant answers instead of waiting on email threads. You are building that agent —
and building it to a standard where it could survive a real production incident, not
just a happy-path demo.

**Total marks:** 100 · **One deliverable:** a single public GitHub repository
containing your dataset, RAG core, LangGraph agent, resilience/MCP layer, and FastAPI
deployment.

## Submission Guidelines (read first)

- Submit **one public GitHub repository link** for the whole project. There is no
  per-Part submission — one repo contains everything.
- State at the top of your `README.md` that you completed the **Naukri.com
  (Recruitment & HR)** track, and include the exact dataset-design choices you made
  in Part 1 Task 1 (seed, category/status weights, amount range) so the grader can
  reproduce your dataset deterministically.
- No images, screenshots, diagrams-to-upload, PDFs, slide decks, presentations, video,
  or audio are required or accepted anywhere in this project. Every deliverable is code
  or text inside the repository.
- Nothing in this project requires a paid account or a credit card. Embeddings
  (SentenceTransformers), the vector index (ChromaDB), and the MCP server (`fastmcp`)
  are free and run locally. The agent's language-model calls (grounded generation, the
  judge used for evaluation) default to a deterministic `MOCK_LLM` mode that needs zero
  API keys and zero network access — this is the mode your graded transcripts must
  use. A real LLM API may optionally be wired in behind an environment-variable flag,
  but every acceptance criterion below must be demonstrably satisfied under `MOCK_LLM`
  alone.
- You may refer to official documentation (e.g. the LangChain/LangGraph docs at
  python.langchain.com, the `fastmcp` docs, the ChromaDB docs, the FastAPI docs, the
  Python standard library docs) while writing your code. AI assistants and
  code-generation tools remain prohibited.
- Originality: your dataset, knowledge base, code, and analysis must be your own work
  for this specific brief.
- Submit your one repository link by the end of the 14-day capstone window.

## Your scenario

**Given category vocabulary (use every value at least once; you may add more):**
`Software Engineer`, `Data Analyst`, `Product Manager`, `HR Executive`, `Sales
Associate`.

**Given status vocabulary (use every value at least once; you may add more):**
`Applied`, `Screening`, `Interview Scheduled`, `Offered`, `Rejected`.

**Required knowledge-base topics (≥12 documents, ≥2-5 sentences each):**
job-application eligibility criteria, interview-scheduling process, offer-negotiation
policy, background-verification process, notice-period policy, referral-bonus policy,
internal-transfer eligibility, probation-period policy, remote-work eligibility,
diversity-hiring guidelines, exit-interview process, and applicant-data-retention
policy.

**Guardrail-relevant PII fields:** the phone number inside contact details is
fixed-format and must be demonstrated masked by your input-side guardrail (Task 10).
Candidate name, expected salary, and background-check results are free text or
unformatted numbers with no reliable pattern to match under a keyless, `MOCK_LLM`-only
masker — acknowledged as out of scope for masking; use only fabricated examples for
all three.

## Part 1 — Dataset Design & RAG Core (30 marks)

**Tasks**

1. **Design and validate your own job-application dataset.** Write a seeded,
   deterministic Python generator (`dataset.py`) producing a `JOB_APPLICATIONS` list
   of ≥40 records. Use every category and status value given above at least once
   (you may add more values). Each record needs: `record_id`, `category`, `status`,
   `expected_salary_inr` (choose a realistic range and state your reasoning in one
   sentence), `days_since_created` (integer, 0–30), and `flagged_priority_review`
   (boolean). Print and report: the count per category (every given category ≥3
   records), the count per status (every given status ≥1 record), and the percentage
   of records with `flagged_priority_review=True` (must land between 10% and 30% —
   if your first random draw doesn't land there, change your seed or weights and
   regenerate; never hand-edit individual records to force the number).
2. **Write your knowledge base.** Author the ≥12 required documents above (2–5
   sentences each, in your own words, covering every required topic).
3. **Implement and index two chunking strategies.** Chunk your documents BOTH as
   fixed-size-with-overlap AND as sentence-based chunks. Embed every chunk in both
   sets with a free local SentenceTransformers model (e.g. `all-MiniLM-L6-v2`), and
   index each chunking strategy in its OWN separate ChromaDB collection.
4. **Implement grounded generation.** Given a query, retrieve the top-k chunks (from
   either collection) and generate an answer using ONLY the retrieved context. Under
   `MOCK_LLM` there is no real model to judge groundedness, so retrieval similarity is
   your only signal — **calibrate your "I don't know" threshold empirically before
   picking one**: measure your own top-1 cosine similarity for at least 3 in-scope
   queries and at least 2 deliberately out-of-scope queries, then set the threshold
   between the two clusters you actually observe. Do not use an untested preset
   (0.5/0.6/0.7 are common tutorial defaults that do not reliably separate short
   policy-sentence embeddings from unrelated queries) — state your measured values and
   chosen threshold in `README.md`. Demonstrate on ≥5 real in-scope queries plus 1
   deliberately out-of-scope query that must trigger the fallback.
5. **Evaluate and compare both chunking strategies.** For the same ≥5 queries from
   Task 4, compute Precision@3 and Recall@3 at the document level (map chunks back to
   parent documents and dedup before scoring) **separately for each of your two
   collections**, showing per-query arithmetic for both. Write 2–3 sentences
   recommending which strategy you would deploy, citing your own two sets of numbers.

## Part 2 — LangGraph Agent with Tools, Memory & Guardrails (30 marks)

Using Part 1's RAG core (your recommended chunking strategy's collection) as a fixed
input, build the orchestration layer.

**Tasks**

6. **Build the second tool with a designed escalation score.** Using `dataset.py`
   from Task 1, implement `check_job_application_status(record_id: str) -> dict`
   returning the application's `status`, `expected_salary_inr`, and a **designed**
   `escalation_score` in `[0, 1]` that combines `flagged_priority_review` with a
   normalized recency signal derived from `days_since_created`. State your exact
   formula and the threshold above which you recommend escalation, justified using
   your own dataset's distribution (e.g. "this threshold corresponds to the 80th
   percentile of `days_since_created` in my generated data").
7. **Build the LangGraph agent.** Construct a LangGraph graph with ≥4 nodes and ≥1
   genuine conditional edge that routes an incoming query to either your RAG tool
   (Task 3–5) or your `check_job_application_status` tool (Task 6) based on query
   intent — demonstrate both routes firing on different sample queries.
8. **Add persisted memory.** Persist conversation history to a JSON file, and
   demonstrate state correctly carried across a multi-turn exchange in one
   transcript, with a **separate** fresh-conversation transcript showing that state
   correctly absent/reset.
9. **Add a structured output schema.** Define a JSON Schema (or equivalent) that every
   agent response must conform to, and validate each response against it in code.
10. **Add guardrails.** Implement input-side guardrails — PII masking, demonstrated
    firing on the fixed-format PII field(s) identified above, and prompt-injection
    detection — and an output-side groundedness check that refuses to answer when the
    retrieved context doesn't support the question. Demonstrate each guardrail
    actually firing on one deliberate test case.

## Part 3 — Evaluation, Observability & FastAPI Deployment (20 marks)

Using Part 2's agent as a fixed input, wrap and evaluate it.

**Tasks**

11. **Deploy via FastAPI.** Expose your agent behind at least 2 endpoints (e.g.
    `POST /ask`, `POST /add-document`) using Pydantic request/response models.
12. **Add structured logging.** Log every request as one JSON-Lines entry with a trace
    ID and timing information. The logged request text must NOT contain the raw,
    unmasked value of any fixed-format PII field your Task 10 guardrail masks — apply
    the same masking to what you log as you apply to what the model sees, so a
    fixed-format PII field never reaches disk in the clear.
13. **Evaluate with the RAG triad at scale.** Using an LLM-as-judge prompt (running
    under `MOCK_LLM`), build a test set of **15 queries** — at least 1 touching every
    required KB topic from your scenario, plus at least 2 deliberately out-of-scope
    or edge-case queries — and score context relevance, groundedness, and answer
    relevance for every query, reporting all three scores per query **and** the
    average of each score across all 15.

## Part 4 — Resilience & Interoperability (20 marks)

Using Part 2's agent as a fixed input, harden it.

**Tasks**

14. **Expose your lookup tool via MCP.** Install `fastmcp` (`pip install fastmcp` —
    note there is no hyphen; `fast-mcp` is not a real package) and wrap
    `check_job_application_status` (with a proper docstring) as an MCP tool,
    launching a private MCP server locally. `fastmcp`'s HTTP transport mounts at
    `/mcp` by default (e.g. `http://127.0.0.1:8000/mcp`), not the bare host:port
    root — point your client at that path. Write a **separate** MCP client script (a
    different file/process from your LangGraph agent) that connects to this server
    and successfully calls the tool for at least 2 different record IDs, printing the
    standardized MCP response for each.
15. **Add SQLite-based checkpointing.** Install `langgraph-checkpoint-sqlite` (a
    separate pip package from core `langgraph`) and configure your LangGraph graph
    with its SQLite checkpointer (`checkpoints.sqlite`) keyed by a thread ID.
    Demonstrate: (a) a run
    executing at least 2 of your ≥4 nodes, (b) execution deliberately stopped before
    the remaining nodes run, (c) resuming the SAME thread ID and completing the run,
    explicitly showing (via printed state/log) that the already-completed nodes'
    results were loaded from the checkpoint and NOT re-executed.
16. **Add timeouts and retries.** Add a per-node timeout to at least one node and a
    global timeout to the whole graph. Add an exponential-backoff retry policy
    (state max attempts, initial interval, max interval, and jitter) around a node
    that simulates a transient failure (e.g. fails the first 2 calls via a counter,
    then succeeds). Demonstrate: (a) the retry policy recovering within the
    configured attempts, (b) the per-node timeout correctly firing a clean error
    (not a hang) on a simulated call that exceeds it, (c) the global timeout
    correctly cancelling the whole run on a simulated total-time overrun.

## Acceptance criteria (your submission is complete when…)

**Part 1**
- `dataset.py` generates ≥40 job applications meeting every stated structural
  threshold (category counts, status coverage, `flagged_priority_review` percentage
  band), with your design choices stated in `README.md`.
- Your knowledge base has ≥12 documents covering every required topic.
- Both chunking strategies are implemented, embedded, and indexed into two separate
  ChromaDB collections that both produce sensible retrieval on a sample query.
- Grounded generation is demonstrated on ≥5 in-scope queries plus 1 out-of-scope query
  that correctly triggers the "I don't know" fallback.
- Precision@3/Recall@3 are computed for BOTH collections on the same ≥5 queries with
  visible per-query arithmetic, and a numbers-cited recommendation is given.

**Part 2**
- `check_job_application_status` correctly looks up a record and correctly computes a
  designed, justified `escalation_score` (not a bare boolean OR).
- The LangGraph graph has ≥4 nodes and ≥1 conditional edge that demonstrably routes to
  both tools on different queries.
- Multi-turn memory is demonstrated, with a separate fresh-conversation transcript
  showing it correctly absent.
- Every agent response validates against your declared structured-output schema.
- Both guardrails (input-side PII/injection, output-side groundedness) are demonstrated
  actually firing on a deliberate test case each.

**Part 3**
- The FastAPI backend exposes ≥2 working endpoints with Pydantic models.
- Every request produces one structured JSON-Lines log entry with a trace ID.
- All three RAG-triad scores are reported per-query for all 15 test queries under
  `MOCK_LLM`, plus the three averages.

**Part 4**
- `check_job_application_status` is successfully callable via a real MCP
  client-server round trip on ≥2 record IDs.
- SQLite checkpointing correctly resumes a run from an interruption without
  re-executing already-completed nodes.
- The retry policy recovers a simulated transient failure; the per-node timeout and
  the global timeout each correctly fire on their respective simulated overruns.

## Submission

Submit **one public GitHub repository link**. The repository must contain, in total:
`dataset.py`, your knowledge-base documents, your RAG/agent/resilience/MCP/deployment
code with transcripts demonstrating every task above, and a `README.md` confirming
everything runs under `MOCK_LLM` with zero API keys. There is exactly one submission
link for the whole project.
