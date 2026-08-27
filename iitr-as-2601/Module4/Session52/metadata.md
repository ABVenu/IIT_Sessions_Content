lecture ID:

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

title: Agent Communication Patterns

objective: Refresh planner–executor communication briefly, then build MasaiMato — a mini Zomato-style MCP restaurant server where an AI model (Groq, with Ollama Cloud as an option) discovers the menu and places food orders through MCP tools.

type of session: theory/implementation/mixture of theory + implementation / You take the call

topics be covered: Agent communication refresh (planner–executor; JSON handoffs; stop conditions); Model Context Protocol; host client server; tools resources prompts; MasaiMato MCP restaurant app with AI ordering via Groq or Ollama


detailed subtopics to be covered:
* Quickly review how a user goal is decomposed for planner and executor roles with structured JSON handoffs and clear stop conditions (short refresh only).
* Explain Model Context Protocol (MCP) as a standard way for AI apps to talk to external tools and context.
* Distinguish host, client, and server roles, and compare MCP tools vs traditional APIs.
* Build MasaiMato: FastMCP server with get_menu and place_order; run an AI chat loop where Groq (or Ollama Cloud) lists MCP tools, places an order, and confirms from tool results.
* Relate MCP back to agent communication: the model orders through structured MasaiMato MCP tool messages instead of inventing dishes or order ids.
