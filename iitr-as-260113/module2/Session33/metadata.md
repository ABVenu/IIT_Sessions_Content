lecture ID: 152462

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 2hr 15 mins
 
title: Tool Integration in AI Agents

objective: Learn how agents use external tools and APIs to perform actions

topics be covered: function calling;connecting APIs and tools


detailed subtopics to be covered:
- Recap How APIs Work — Briefly revisit the previous session: what an API is, the request-response cycle, HTTP methods, status codes, and JSON as the data format; establish this as the foundation for everything in this session;
- Understand Function Calling in AI Agents — Explain that agents can call external functions/tools when they need to take action; the agent decides what tool to use, the system executes it, and returns the result back to the agent via structured output;
- See How Agents Use APIs as Tools — Show that every external tool an agent uses (search, calculator, database, email, etc.) is accessed via an API call — the agent sends a request and receives a JSON response, exactly like the previous session;
- Understand How Applications Connect to Databases — Introduce the idea that applications (and agents) do not talk to databases directly — they go through a connection layer (drivers/connectors); explain the role of Python as the application layer that sits between the agent and the database;
- Execute SQL Queries from Python — Explain how SQL queries are triggered from Python code rather than manually typed in a SQL tool; show the concept of running a SELECT or INSERT from within a Python script and receiving results as structured data;
- Understand What Pydantic Does and Why It Matters — Explain Pydantic as a Python library for data validation and structure; show how it defines what a piece of data should look like (field names, types, constraints) — similar to how JSON has a shape, Pydantic enforces that shape in Python;
- Connect Pydantic to APIs — Show that Pydantic models are used to validate incoming API request data and to structure outgoing API responses; this is how Python, APIs, and structured data stay consistent with each other;
- Understand What SQLAlchemy Does and Why It Matters — Introduce SQLAlchemy as an abstraction layer over SQL; explain that instead of writing raw SQL strings, Python code defines and queries database tables using Python objects — making it safer, more readable, and less error-prone;
- See How Python, SQL, and Pydantic Work Together — Walk through a complete flow:
agent triggers a tool → Python function runs → Pydantic validates the input → SQLAlchemy queries the database → SQL executes → result returned as a Pydantic model → agent receives structured JSON output;
- Solidify the Full Stack Mental Model for Agents — Tie together both sessions: agents communicate via APIs (Session 32) and use Python + Pydantic + SQL as the backend layer to access, validate, and return data (Session 33); students should leave able to trace a full agentic action from trigger to data retrieval to response;