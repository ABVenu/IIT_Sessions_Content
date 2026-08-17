lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: Architecture and Planning

objective: Design the complete system architecture — components, integrations, and risks — ready for repository scaffolding. (Nimbus PayDesk four floors; no bank.)

type of session: mixture of theory + implementation

topics be covered: Architecture design; component selection; integration planning; risk assessment


detailed subtopics to be covered:
* Draw the end-to-end multi-agent architecture (intake → extract → policy → route on FastAPI; SQLite + Chroma; human stamp; no payout floor.)
* Select components for API, SQL, RAG, orchestration, and automation (FastAPI, SQLite, Chroma, LangChain sequential, n8n webhook.)
* Plan integrations between API, agents, tools, and webhooks (n8n posts /ingest; tools fail closed to needs_human; stamp is human-only.)
* Produce a risk register covering money, privacy, downtime, and cost (wrong GSTIN, skipped ₹50,000 gate, PAN leak, n8n double ingest.)
* Freeze the folder map and interface contracts so scaffolding can start (POST /ingest, GET /tickets/{id}, POST stamp, GET /report.)
