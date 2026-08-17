lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: Hands-on: Project Setup and Scaffolding

objective: Set up the project repository, environment, SQL schema, and API stubs so a record can be created before any LLM call. (Nimbus PayDesk ticket ingest with no model.)

type of session: implementation

topics be covered: Repository setup; environment configuration; scaffolding; initial implementation


detailed subtopics to be covered:
* Initialise the repository, virtual environment, dependencies, and secret handling (nimbus_paydesk venv; .env gitignored; no keys in git.)
* Scaffold folders for app code, knowledge corpus, samples, and evaluation cases (app/, data/policy.md, labelled invoices, eval/cases.json.)
* Connect SQL and persist core records (SQLite tables: tickets, events, vendors, purchase_orders; seed Kaveri / PO-7781.)
* Expose API stubs for health and ingest (FastAPI GET /health and POST /ingest storing status ingested.)
* Prove the empty pipeline can create and fetch a record without calling a model (restart test: ticket survives in paydesk.db.)
