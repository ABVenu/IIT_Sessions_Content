lecture ID:

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 60 mins

Session Notes Length: 400 lines max

title: Hands_on Session: LangGraph

objective: Build a Hostel Maintenance Ticket Desk in LangGraph that classifies complaints, branches to create ticket or ask clarification, checkpoints before create, and hardens the flaky ticket API with timeout, retries, and calm user-facing errors.

type of session: mixture of theory + implementation

topics be covered: LangGraph nodes edges state; conditional routing; checkpoints resume; timeouts retries; hostel maintenance ticket hands-on


detailed subtopics to be covered:
* Design a hostel maintenance ticket workflow on paper (parse → classify → create ticket or ask clarification → confirm) with minimal shared state.
* Build and run a branching LangGraph for electrical / plumbing / wifi vs unclear complaints, and read execution via a trace field.
* Enable SqliteSaver checkpointing with interrupt_before create_ticket; inspect get_state / get_state_history; resume the same thread_id.
* Harden create_ticket with per-attempt timeout, RetryPolicy backoff, and a clear user-facing error when retries are exhausted.
* Complete an end-to-end walkthrough and a minimal reliability checklist for the desk app.