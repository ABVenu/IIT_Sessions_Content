# Session 07 — Practice Questions
*Topics: AI agents vs traditional systems; Planning, Reasoning, Memory, Action; Observe → Think → Act; memory types; common failure modes.*

---

## Objective Questions (9)

### Easy

**Q1.** Which statement best describes an **AI agent**?

- (A) Software that only runs when a human clicks each step in a fixed wizard  
- (B) A system that perceives its environment, makes decisions, and takes actions on its own to achieve a goal without needing a human to guide every step  
- (C) Any program written in Python  
- (D) A database that stores user preferences  

**Answer:** An agent perceives, decides, and acts toward a goal with autonomy at the step level. A click-through wizard is closer to a scripted flow; “any Python program” and “a database” are not definitions of an agent.

---

**Q2.** Which option is the best example of a **traditional (non-agentic) system**?

- (A) A customer-support assistant that looks up order history and proposes a refund in one conversation  
- (B) A navigation app that reroutes when traffic changes  
- (C) A traffic signal that cycles red / amber / green on a fixed timer  
- (D) A traffic system that extends green lights using live camera data  

**Answer:** Traditional systems follow fixed rules; a timer-based signal does not adapt to conditions. Assistants that use order history and refunds, navigation that reroutes for traffic, and camera-driven signal timing illustrate perception, adaptation, or richer behavior closer to agentic systems.

---

**Q3.** Which list correctly names the **four core components** of an AI agent?

- (A) Observe, Think, Act, Loop  
- (B) Planning, Reasoning, Memory, Action  
- (C) Input, Process, Output, Store  
- (D) Perception, Learning, Training, Deployment  

**Answer:** The four pillars are Planning, Reasoning, Memory, and Action. **Observe → Think → Act** is the operational **loop**; it is not the list of the four named components.

---

### Medium

**Q4.** In the **cricket analogy** for planning vs reasoning, which mapping is correct?

- (A) Planning = the captain’s on-field decisions when the match situation changes; Reasoning = strategy agreed in the dressing room before the match  
- (B) Planning = strategy set before the match (e.g., in the dressing room); Reasoning = on-field decisions when the situation changes during the match  
- (C) Planning and reasoning are the same — both mean choosing the batting order  
- (D) Planning applies only to batsmen; reasoning only to bowlers  

**Answer:** Planning is proactive and forward-looking (what steps before you start); reasoning is reactive (what to do given what just happened).

---

**Q5.** **Short-term (working) memory** in an AI agent is best described as:

- (A) Information in a database that persists indefinitely  
- (B) Temporary information for the current task or conversation, typically cleared when the session ends — analogous to RAM  
- (C) Long-term memory, but accessed more quickly  
- (D) Only authentication secrets such as passwords, kept forever  

**Answer:** Short-term memory holds the active context (e.g., current chat, intermediate results). Long-term memory persists across sessions (e.g., profiles, files).

---

**Q6.** In the **Observe → Think → Act** loop, why does the agent usually return to **Observe** after **Act**?

- (A) The loop must always run exactly three times  
- (B) The outcome of an action is new information that should be perceived before the next decision  
- (C) Observe is only needed once, at the start  
- (D) Think and Act are skipped after the first iteration  

**Answer:** Each action can change the world or reveal new facts; the next cycle must incorporate that feedback.

---

### Hard

**Q7.** A user asks for a **budget** hotel near the airport. Hotel A is cheaper and farther; Hotel B is pricier and closest. The agent chooses Hotel B because it is closest. In the usual taxonomy of **planning / memory / reasoning / action** failures, this is best classified as:

- (A) Bad planning — steps were in the wrong order  
- (B) Memory failure — the agent forgot the user’s name  
- (C) Reasoning error — the decision did not respect the user’s stated priority (“budget”)  
- (D) Wrong or incomplete action only — the booking API request was malformed  

**Answer:** The failure is mis-prioritizing constraints (budget vs distance), i.e., a poor **decision** given the goal—not necessarily wrong step ordering, forgotten context such as the user’s name, or a malformed booking request.

---

**Q8.** An agent writes an **internal ordered list of steps** before executing (e.g., a task plan or chain-of-thought–style decomposition). That behavior maps most directly to which component?

- (A) Action  
- (B) Memory  
- (C) Planning  
- (D) Reasoning  

**Answer:** Planning is breaking a goal into ordered, executable steps. Reasoning selects among options when something unexpected appears; the written step list is primarily the plan, not the final outward effect (the action layer) or durable storage (memory systems).

---

**Q9.** Which option best describes **fallback reasoning**?

- (A) If the user’s wording is unclear, pick an option at random  
- (B) If the primary approach fails or is blocked, switch to an alternate approach (e.g., apply via LinkedIn when direct email is not accepted)  
- (C) Retry the same step indefinitely until the server responds  
- (D) Wipe long-term memory to free space  

**Answer:** Fallback reasoning means having a backup path when Plan A cannot be completed.

---

## Subjective Question (1)

**Difficulty:** Medium to Hard

**Q10.** An agent is tasked with **sending the monthly sales report to the CEO**. It handles **how** to email correctly, but its **plan** never includes checking whether this month’s data has been updated, and it sends **last month’s** figures.

In **150–250 words**, address the following:

1. Identify which **failure mode** (among bad planning, memory failure, reasoning error, wrong/incomplete action) this scenario best illustrates, and justify why it fits that category rather than the others.  
2. Propose **one concrete improvement** to the plan: what verification or dependency step should be added, and why?  
3. Name **one other core component** (Planning, Reasoning, Memory, or Action) that could still fail **even if** the plan were fixed for data freshness, and give a **specific** example of that failure in the same reporting task.

**Submission instruction:** Type the answer in the answer box after the question content.

---

### Sample solution (model answer)

This scenario is best classified as **bad planning** (missing or wrong steps / dependencies). The goal—email the monthly report—is sensible, and sending email may be executed correctly, but the **plan omits a required step**: verify that the reporting period’s data is loaded (e.g., pipeline or ETL finished, correct month in the export) before attach and send. That is not primarily **memory** (the user may have stated the month; the issue is the step list), nor **reasoning at a trade-off** like the budget-hotel case, nor a **malformed API call** if the email API succeeded.

The fix is to embed **dependencies and verification** in the plan: e.g., “confirm dataset refresh timestamp or job status for the target month,” then “generate or select attachment,” then “send.” That parallels not confirming an order before payment completes.

Even with that planning fixed, **Action** could still fail: the agent might send to a **wrong address** from stale CRM data, attach the **wrong file path**, or run a script on the **wrong column**—all execution errors distinct from omitting the freshness check in the plan.

---

### Rubric (for evaluators)

- **Part 1:** Expect **bad planning** / missing dependency step; contrast briefly with reasoning vs memory vs action failure.  
- **Part 2:** Expect an explicit **verification** or **ordering** fix tied to data freshness or dependencies.  
- **Part 3:** Another component with a **different** failure in the **same** scenario (e.g., stale recipient in memory, misreading “monthly,” wrong attachment action).
