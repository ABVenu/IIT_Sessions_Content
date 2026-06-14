lecture ID:

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

title: Working with APIs and JSON

objective: Understand how applications communicate using APIs and JSON

type of session: mixture of theory + implementation

topics be covered: REST APIs;JSON structures;API responses


detailed subtopics to be covered:

- This session: theory-leaning mixture — build the API and JSON foundation only; anchor on Groq calls from the ShopKart RAG labs (Sessions 20–22) and one lite hands-on GET exercise that parses JSON in the terminal; defer Groq prompt routing, function calling, RAG-plus-API agent workflows, and tool wiring to Session 24
- Connect Agent Workflows to the API Request–Response Pattern — Learners distinguish RAG (answers grounded in stored documents) from live external data accessed through APIs; define an API as a structured contract between software components; map Groq calls from Sessions 20–22 onto request parts (URL, method, headers, body) and response parts (status code, JSON body);
- Understand REST Conventions and HTTP Status Codes — Learners map GET/POST/PUT/PATCH/DELETE to read/create/update/delete actions at overview level; interpret common status codes (200, 400, 401, 404, 429, 500) and relate rate-limit failures to the Groq experience from Session 22;
- Read and Parse JSON as the API Data Format — Learners identify objects, arrays, and nested key-value fields in sample API responses; relate JSON structure to Python dictionaries; use `json.loads()` and `response.json()` to turn API response text into Python data and extract selected fields;
- Execute a GET Request and Validate Parsed JSON Output — Learners call a public API with `requests`, check status before trusting the body, handle non-200 responses safely, and print extracted JSON fields in the terminal — proving the fetch-and-parse pattern Session 24 extends when tools feed an LLM;
