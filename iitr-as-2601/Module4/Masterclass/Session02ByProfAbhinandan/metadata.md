lecture ID:

Course Name: Certification in Agentic Systems and Design 

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: Hands-on Workshop: LangGraph 02 — Campus Lost & Found Claim Desk

objective: Build a Campus Lost & Found Claim Desk in LangGraph that classifies lost-item reports, branches to clarify / escalate high-value / search matches, checkpoints before item release, and hardens a flaky match API with timeout, retries, and calm user-facing errors.

type of session: mixture of theory + implementation

topics be covered: LangGraph nodes edges state; conditional routing with three-way branch; checkpoints resume before release; timeouts retries; campus lost and found hands-on


detailed subtopics to be covered:
* Design a campus lost & found claim workflow on paper (parse → classify → clarify OR escalate OR search → release/confirm) with minimal shared state.
* Build and run a three-way branching LangGraph for electronics / documents / apparel vs unclear vs high-value reports, and read execution via a trace field.
* Enable SqliteSaver checkpointing with interrupt_before release_item; inspect get_state / get_state_history; resume the same thread_id after a human review pause.
* Harden search_match with per-attempt timeout, RetryPolicy backoff, and a clear user-facing error when retries are exhausted.
* Complete an end-to-end walkthrough and a minimal reliability checklist for the lost & found desk app.
