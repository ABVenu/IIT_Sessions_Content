lecture ID:

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 2hr 15 mins

title: Working with APIs and JSON	

objective: Understand how applications communicate using APIs and JSON

topics be covered: REST APIs;JSON structures;API responses


detailed subtopics to be covered:
- Understand How Software Is Structured — and Why Agents Need to Know This — Introduce the layered architecture (FE, BE, DB) not as a web dev concept, but to help students understand the environment agents operate in and the systems they interact with;
- Understand the Role of Each Layer — Explain that the frontend is what users see, the backend runs logic and enforces rules, and the database stores data; agents typically interact at the backend layer via APIs;
- Visualize the Full Request Flow: FE → API → BE → API → DB — Walk through the complete data flow:
user action → API call to backend → backend queries database → database returns data → backend sends API response → result displayed;
- Introduce APIs as the Universal Communication Layer — Define an API as a structured contract between two software components; establish that APIs are how all modern systems talk — including AI models and agents;
- Understand REST APIs and HTTP Methods — Explain REST as a widely used API style and map HTTP methods to actions:
GET → Read, POST → Create, PUT/PATCH → Update, DELETE → Remove;
- Understand the Structure of a Request and Response — Break down an API call (URL, method, headers, body) and what the server returns (status code, response body in JSON);
- Decode HTTP Status Codes — Introduce common codes and their meaning: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Internal Server Error;
- Understand JSON as the Data Format for APIs — Define JSON, explain its structure (objects, arrays, key-value pairs), and draw the parallel that JSON objects behave like Python dictionaries — familiar key-value pairs; also cover how to parse JSON (converting a JSON string into a Python dict using `json.loads()`) and stringify it (converting a Python dict back to a JSON string using `json.dumps()`) so students can work with API responses in code;
- Understand That AI Models Also Respond via APIs — Explain that when you call an AI model (e.g., OpenAI, Gemini), you send a structured API request and receive a structured JSON response — the same pattern as any other API; the model's reply is just another API response;
- Trace an Agentic API Call End to End — Walk through a real scenario:
agent sends POST request to OpenAI API with a prompt → API returns JSON response with the model's reply → agent reads the response and decides the next action;
	