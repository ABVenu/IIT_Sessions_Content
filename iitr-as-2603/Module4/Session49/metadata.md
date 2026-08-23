lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: Deployment: API Facade & Hosting Basics

objective: Expose the agent via a thin API and outline hosting options for pilots.

type of session: mixture of theory + implementation

topics be covered: FastAPI facade (lite); request/response contract; hosting options; environment config


detailed subtopics to be covered:
* Define a minimal REST endpoint that triggers the agent pipeline.
* Document request and response JSON for integrators.
* Compare two hosting options (local; simple PaaS) for a pilot deployment.
* Configure environment variables for production-like runs without containers.

* Explain why deployment is needed beyond a locally running app.
* Compare locally running vs deployed app (URL, process, secrets, data, reachability).
* Build a minimal FastAPI RAG endpoint that retrieves notes and calls Groq.
* Choose knowledge storage: local file in repo or Supabase table.
* Deploy the mini app on Render with env vars (no containers); verify /health and /ask.
