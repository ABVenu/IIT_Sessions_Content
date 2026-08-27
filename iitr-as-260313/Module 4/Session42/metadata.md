lecture ID:

Course Name: Certification in Agentic Systems and Design / Software Engineering with AI

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 1hr  50mins

Session Notes Length: 480 lines to 500 lines max

title: AutoGen: Hands-on — End-to-End Multi-Agent System

objective: Build one Hotel Guest Complaint Intake Desk in AutoGen that intakes a guest message, classifies it, looks up the stay with tools, creates a ticket, and closes under speaker and termination controls.

type of session: mixture of theory + implementation

topics be covered: AssistantAgent; UserProxyAgent; conversable-agent model; register_function; termination conditions; GroupChat; GroupChatManager; speaker selection; max rounds; conversation traces


detailed subtopics to be covered:
* Configure conversable AutoGen agents with system messages and non-overlapping hotel seats for intake, classify, clerk, and desk-runner roles.
* Register lookup and ticket tools with a safe caller/executor split so the clerk suggests and the desk runner executes.
* Orchestrate a GroupChat with speaker selection and max rounds so specialists contribute distinct sub-results and tools still reach the executor.
* Analyze conversation traces to verify tool use and handoffs, then apply one configuration fix for a failure such as wrong speaker, repetition deadlock, or a missing stop stamp.
