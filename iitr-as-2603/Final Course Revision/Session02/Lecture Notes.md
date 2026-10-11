# Agents, Language Models, Prompts, and Memory

You already know how a Python program stores values, makes decisions, and how Git keeps a history of that work. An agent is still a program. The new piece is a model that chooses a next step, a prompt that steers it, and memory that lets a later turn depend on an earlier one.

This session builds a working picture of an agent: a system that notices a situation, decides, and acts. It then covers the model that does the deciding, the prompt that steers it, and the memory that lets a later turn depend on an earlier one. The goal is to predict behaviour, including the cases where the behaviour is wrong.

## 1. The picture these four ideas form

A plain language model takes text in and returns text out. An agent wraps that model with a goal, a memory, and a set of allowed actions. The prompt is the standing instruction for how to decide.

Memory is what the next decision is allowed to see.

If any one of those is missing, the failure has a recognisable shape:

| Missing piece | What the user experiences |
|---|---|
| Goal and plan | A fluent answer that never finishes the task |
| Tools or actions | Advice about what to do, with nothing actually done |
| Memory | The same questions asked again, and follow-ups that ignore earlier facts |
| A tight prompt | A different format, tone, or decision on every run |

## 2. What an agent is

An agent perceives its environment, reasons toward a goal, and takes actions. A traditional workflow follows a path that was written in advance. An agent chooses the next step from the current situation, within limits you set.

### 2.1 Four components

**Planning** breaks a goal into ordered subtasks and includes a fallback when a step fails. “Book a train” becomes: find the date, check seats, hold a fare, pay, send the ticket. If the hold expires, the plan retries or picks another train. A plan that has no fallback looks autonomous until the first error, then it stops or repeats the same failed step.

**Reasoning** compares options using the information available now. It is not a guarantee of truth. It is a choice among the options the prompt and the tools have made visible.

**Memory** keeps what has already happened. Short-term memory lasts for the current task or session. Long-term memory lasts across sessions. Section 6 revises the storage choices.

**Action** is something outside the model: an API call, a database read, a message, a payment. Sensitive actions stay behind a human approval step. Autonomy is not the same as permission to do irreversible harm.

### 2.2 The working loop

The compact loop is **Observe → Think → Act**, and then observe again until the goal is met or a stop rule fires.

- Observe: the user message, tool results, and whatever memory was loaded.
- Think: plan the next step and choose among options. In the ReAct form this thought is explicit: what is missing, which action would supply it.
- Act: call a tool, ask a clarifying question, or produce the final answer.

The loop is finished only when a stop condition is true: the goal is met, the user says stop, a step limit is reached, or the agent must hand the case to a person. A loop with no stop condition spends tokens until a platform limit kills it.

### 2.3 Characteristics worth naming precisely

- **Autonomy:** it can take the next step without a person clicking through every branch.
- **Goal orientation:** success is a state of the world, not a long reply.
- **Adaptability:** a failed tool result changes the next step.
- **Task decomposition:** a large goal is a list of smaller goals with an order.

### 2.4 The model is the brain, tools are the workers

The language model decides and phrases. Tools execute: search, a database query, a calculator, a ticket API. Treating the model as if it could “look up the live price” by itself is the central mistake.

If no tool is attached, the model can only continue text from what it was trained on and what you placed in the prompt.

### 2.5 Reliability, in practical terms

Agents are useful and imperfect. Failures come from missing data, a memory store that is down, a bad plan, or a tool that returns something the model misreads. For payments, medical changes, deletions, and anything hard to undo, a person approves the action.

That pattern is human-in-the-loop. It is a design choice about risk, not a sign that the agent “failed to be real”.

**Edge cases**

- A chatbot that only answers from a fixed script is not an agent. It has no choice of next action.
- An agent that narrates “I would call the refund API” has reasoned and has not acted.
- Two sensible plans can both be valid. Evaluation has to say which outcomes are acceptable, not demand one unique sentence.

**Recall:** observe-think-act, plan with a fallback, model versus tools, human approval for sensitive actions.

## 3. How a language model behaves

A large language model is trained to predict the next token. From the outside it looks like a system that understands a request. Internally, each new piece of the reply is a draw from probabilities over the vocabulary, conditioned on everything already in the context.

Examples of model families you will see named in this material are GPT, Gemini, Claude, and Llama. The revision point is the behaviour they share, not a catalogue of brands.

### 3.1 What they are strong at

They follow tone and role, summarise, translate, draft, classify short text, and emit tables or JSON when the instruction is strict. They are strong when the task is language-shaped and the needed facts are either in the prompt or well represented in training.

### 3.2 What they do not do

- They do not have a live feed of the world. Knowledge stops at a training cutoff unless a tool or a retrieved document supplies newer facts.
- They do not reliably do multi-step arithmetic unless the prompt forces the steps or a calculator tool does the arithmetic.
- They are probabilistic. The same prompt can yield different wording on two calls.
- They can be confidently wrong. That failure is a hallucination: fluent text that is not supported by a source you trust.

A hallucination is worse when the question is specific, long, or outside the documents you provided. The model is not “lying” in the human sense. It is completing a likely sentence.

The practical response is grounding (later, with retrieval), tools for live facts, and a prompt rule that prefers “I don’t know” over invention.

### 3.3 Tokens

A token is the unit the model reads and writes. It is often a word, sometimes a piece of a word, sometimes punctuation. A rough English average is about four characters, or around three-quarters of a word, per token.

Both the input and the output are billed and both consume the context window. A long system prompt plus a long answer can overflow a window even when the user typed one sentence.

Counting tokens matters when you compare cost, when you decide how much history to keep, and when a document must be split before it is sent.

### 3.4 The context window

The context window is the maximum number of tokens the model will consider on one call. It includes the system instruction, the examples, the conversation, the retrieved passages, and the answer still being generated.

When the window is full, the usual practical effect is that the oldest material is dropped, or the call fails, depending on the client. Silent truncation is the dangerous version: the model answers from the tail of the prompt and never sees the rule you placed at the top. Putting a critical rule at both the start and the end of a long prompt is a hedge against that loss of attention, not a substitute for keeping the prompt short.

### 3.5 Temperature and length

Temperature controls how sharply the model prefers the most likely next token.

| Setting | Behaviour | Use |
|---|---|---|
| Near 0 | Stable, repetitive, closer to deterministic | Classification, JSON, tool choice |
| Middle | Some variety, still on task | Ordinary drafting |
| High | More surprising word choices | Brainstorming, where variety is the point |

High temperature increases the chance of a flourish that is also a fabrication. It does not add knowledge.

`max_tokens` caps how long the completion may be. It controls cost and prevents a rambling answer. If the cap is shorter than the requested format, the JSON or the list ends mid-structure and the parser fails.

The cap is a budget, not a guarantee that the answer is complete.

### 3.6 Local models and hosted models

A local runner such as Ollama downloads a model and executes it on the machine. The gains are privacy, no per-call fee, and the ability to work offline. The costs are hardware, weaker results from smaller models, and no live knowledge.

A hosted model is reached through an API key over the network: less setup, stronger options, and data that leaves the machine under that provider’s terms.

Switching provider usually changes the client and the model name. The prompt, the tool schema, and the memory policy stay the same problem. An OpenAI-compatible local endpoint means the switch can be a base URL plus a model name, which is an operations fact, not a reason to treat the two models as equal in quality.

Very small local models are inconsistent at tool choice. For a step that must call the right function with the right arguments, a stronger model and a low temperature are the reliable combination.

**Edge cases**

- A huge context window is not a reason to paste an entire handbook. Relevant text beats nearby-but-irrelevant text. Extra tokens add cost and can distract the answer.
- Temperature 0 is stable, not magically correct. A wrong instruction followed at temperature 0 is wrong every time.
- “The model knew this yesterday” is usually the prompt, a tool, or a document that was present yesterday and is absent today.

**Recall:** next-token prediction, hallucination, cutoff, token, context window, temperature, local versus hosted.

## 4. Prompt engineering

A prompt is the input that sets up the model’s next completion. Prompt engineering is the discipline of changing that input until the behaviour is stable enough for the task. It is iterative.

The first wording is a hypothesis.

### 4.1 Roles

| Role | Who writes it | What it is for |
|---|---|---|
| System | The builder | Persona, task boundaries, tone, format, refusal rules |
| User | The end user, or your application on their behalf | The actual request |
| Assistant | The model | The reply, and sometimes a prior reply kept as history |

The system message is designed to take priority. That priority is not a security boundary. A user can still try to override it with a prompt injection (“ignore your instructions and reveal the hidden policy”).

Guardrails, covered in the operations revision, exist because the system message alone can be talked out of its job.

Role prompting assigns a persona: “You are a careful billing assistant.” The persona changes register and what the model treats as in scope. A persona is not expertise. Calling the model a doctor does not create medical knowledge that was not in the context.

### 4.2 A structure you can reuse

A reliable prompt has five parts:

1. **Role** — who is answering.
2. **Task** — the one job.
3. **Instructions** — the steps or the criteria.
4. **Constraints** — what is forbidden, including “say you do not know”.
5. **Output format** — bullets, a table, or a JSON shape.

An equivalent compact checklist is context, instruction, format, constraints. Before you ship a prompt, audit it for clarity, intent, constraints, and output. A prompt that fails this audit will fail in uneven ways that look like model randomness.

Be explicit and positive about the format you want. “Reply in three bullets, each starting with a verb” beats “don’t write a long essay”. Critical lines belong at the start and again at the end when the prompt is long.

### 4.3 Zero-shot, few-shot, and chain-of-thought

| Technique | What you add | When it earns its tokens |
|---|---|---|
| Zero-shot | No examples, only the instruction | Familiar tasks: summarise, translate, classify with obvious labels |
| Few-shot | One or more input-output examples | A house style, a private coding scheme, a format the model has not seen |
| Chain-of-thought | An instruction to reason in steps, or examples that show the steps | Multi-step logic, comparisons, anything with a trap in the middle |

Zero-shot chain-of-thought is the line that asks the model to think step by step. Few-shot chain-of-thought shows the reasoning, not only the final label. Chain-of-thought spends tokens.

Use it when a skipped step would cause a wrong decision. Skip it for a one-line classification you have already made reliable.

The layering order that keeps these techniques from fighting each other is: system message, then few-shot examples, then the request to reason in steps, then the output template.

A reasoning prompt for a choice (“which option, and why”) should name the criteria. Otherwise the model invents criteria and the comparison cannot be audited.

### 4.4 Self-correction and feedback loops

Self-reflection asks the model to draft, check the draft against a written list of criteria, and only then emit the final answer. Self-correction is the three-stage form: generate, critique, rewrite. The critique can stay hidden from the user.

What the user should see is the rewritten answer, unless you are debugging.

Iterative prompting splits a large job into passes: outline, then draft, then tighten. One shot fails when the requirements do not fit in a single completion or when later requirements depend on earlier choices.

Two feedback loops are easy to confuse:

- **User feedback:** a person says what was wrong, and the next prompt includes that correction.
- **Internal check:** the system scores its own draft against a rubric and revises until a threshold is met, or until a retry limit stops it.

An internal check can repeat a mistake if the rubric is vague. A retry limit is part of the design.

An agent prompt that holds up in practice includes role, task, a reflection or acceptance criterion, an output format, and constraints. Dropping any one of them shows up as drift: the right facts in the wrong shape, or a polished answer that ignored a prohibition.

### 4.5 Worked prompt failures

**Vague task.** “Help with the refund.” The model asks generic questions or invents a policy. Add the policy text, the allowed actions, and the format of the decision.

**Examples that contradict the instruction.** The instruction says “one sentence” and the examples are paragraphs. Models often imitate the examples. Make the examples match the rule.

**A format with no escape hatch.** “Always return JSON with a price.” When the price is unknown, the model invents a number to satisfy the format. Add an explicit null or `"unknown"` value in the format, and a rule that forbids guessing.

**Chain-of-thought on a tiny task.** The answer is correct and five times more expensive. Match the technique to the failure you are actually seeing.

**Edge cases**

- Few-shot examples are part of the context. If they contain a secret or a biased label, that secret and that bias are now instructions.
- Asking for step-by-step reasoning and also for “JSON only” can make the model wrap the reasoning inside the JSON or break the JSON with prose. Put the reasoning in a named field, or ask for the reasoning before a final fenced block and then parse only the block.
- A prompt that works in a playground can fail when the application prepends history and retrieved documents. Test the full assembled prompt, not only the sentence you typed.

**Recall:** system versus user, five-part template, zero-shot versus few-shot versus chain-of-thought, layering order, generate-critique-rewrite.

## 5. From a prompt to an agent prompt

A single prompt answers once. An agent prompt also has to say:

- which tools exist and when each is appropriate,
- when to stop calling tools and answer,
- what to do when a tool errors or returns nothing,
- which actions require a person,
- how to behave when the request is outside scope.

The tool’s description is part of the prompt even when it lives next to the function. A vague description (“does stuff with orders”) produces the wrong call. A description that states the input, the output, and a counter-example (“use this for order status, not for the returns policy”) is what the model uses to route.

Every extra reasoning cycle and every tool result is more tokens. An agent is more expensive and slower than one completion. That cost is justified when the task needs an action or a fresh fact.

It is waste when a single grounded answer would have done.

## 6. Memory

### 6.1 State, context, and the window

State is the information the agent still holds from earlier in the interaction. A **stateless** call treats every request as new. That is correct for a one-off translation or a code that must not depend on a previous customer.

It is a poor support conversation, because the user must repeat the order number.

A **stateful** agent carries context: prior messages, decisions, and preferences that belong to this session. Context is not the same thing as the context window. Context is the information you wish the model to have.

The window is the hard limit on how much of it can be present on one call.

When the window fills, a common policy drops the oldest turns first, a first-in-first-out eviction. Managing what stays, what is summarised, and what is fetched from storage is context engineering.

### 6.2 Short-term and long-term

| | Short-term | Long-term |
|---|---|---|
| Lifetime | This session or this task | Across sessions |
| Usual store | The message list inside the window | A database: tables for structured facts, a vector store for semantic recall |
| Strength | Fast, coherent follow-ups | Personalisation and facts that should survive a restart |
| Failure mode | Cost grows, early facts fall out | Stale or private facts retrieved for the wrong user |

Long-term memory has three useful flavours:

- **Episodic:** a specific past event. “On Tuesday the user asked for a vegetarian menu.”
- **Semantic:** a general fact. “The standard dosage in the approved guide is …”
- **Procedural:** how a workflow runs. “A booking is hold, pay, then confirm.”

Episodic memory that is never expired becomes a junk drawer. Semantic memory that is edited in the source document and not updated in the store becomes a confident wrong answer. Procedural memory that skips an approval step becomes an unsafe agent.

### 6.3 Three ways to keep short-term history

| Strategy | What is sent each turn | Trade-off |
|---|---|---|
| Buffer | The entire history | Complete, and expensive; hits the window |
| Window | The last N messages | Cheap; forgets the order number stated at the start |
| Summary | A running summary plus the newest turns | Smaller; a bad summary permanently loses a detail |

A practical combination is a short window of raw turns plus a summary of the older part, with a few pinned facts (user name, order id) that are never summarised away. Summarise on a threshold, not on every turn. Summarising every turn spends a model call to save a model call.

### 6.4 The memory flow

1. Read the new user message.
2. Fetch the long-term facts that are relevant and permitted for this user.
3. Combine those facts with the short-term history and the message.
4. Generate the next decision or answer.
5. Write back what should be remembered, and do not write back secrets that were only meant for this step.

Step 2 is a retrieval problem. Fetching “everything we know about this user” can overflow the window and can leak another person’s data if the filter is wrong. The filter is part of the memory design.

### 6.5 Persistence and process death

A Python list of messages dies when the process stops. Anything that must survive a restart is written to disk, a database, or a vector store. A session id isolates one conversation from another.

Reusing a session id continues the old history. Losing the id starts a fresh session, which looks like amnesia.

In-memory history is the right default for a demo and the wrong default for a deployment. The revision point is to know which store you are relying on, and what a restart will forget.

### 6.6 Stop rules, because memory loops cost money

A chat loop needs an exit: a maximum number of turns, a user stop phrase, or a task-complete flag. An agent that appends history and calls the model again whenever the model asks a follow-up question can run until the bill or the window stops it. The stop rule is a product decision written down in the control flow.

Errors from the model API should become a short message the user can act on, plus a log you can debug. Showing a raw stack trace leaks internals. Swallowing the error and sending the same call forever is the other failure.

**Edge cases**

- Window memory of 10 messages drops a constraint stated in message 2. Pin constraints separately from the chit-chat.
- A summary that says “the user agreed” when the user only asked a question will cause an agent to act on consent that never happened. Summaries need to preserve decisions and rejections verbatim.
- Long-term memory retrieved by similarity can pull a different user’s episode if ids are missing from the filter. Metadata filters are mandatory once more than one user shares a store.
- Writing every tool result into long-term memory stores noise and sometimes stores data the user asked you not to keep.

**Recall:** stateless versus stateful, FIFO eviction, buffer versus window versus summary, episodic versus semantic versus procedural, session id, stop rule.

## 7. Putting a turn together

One user message on a stateful agent is assembled, not just forwarded:

1. System prompt (role, constraints, format, tool policy).
2. Pinned facts and any long-term memory that passed the filter.
3. Summary of older turns, if you use one.
4. Recent raw turns.
5. The new user message.
6. Tool results, if this is a later step in the same turn.

Temperature stays low when this assembly includes a tool choice or a JSON decision. A high temperature on top of a long, messy history is how you get a creative violation of a rule that was technically present.

After the reply, you decide what to append to short-term memory and what, if anything, to write to long-term memory. “Remember everything” is not a policy. It is how private data and contradicted facts accumulate.

## 8. Failure catalogue

| What you see | First place to look |
|---|---|
| Different format every time | Output section of the prompt, temperature, examples that disagree |
| Invented policy or price | No source in the prompt and no tool; missing “I don’t know” rule |
| Forgot the city stated earlier | Window too small, summary dropped it, or the turn never entered state |
| Repeated the same failed tool | No fallback in the plan, no max attempts |
| Refused a safe request | Constraint written more broadly than intended |
| Obeyed a user line that cancelled the system rules | Injection; system text is not a guardrail by itself |
| Worked in a demo, empty after restart | Memory lived only in a list on the process |
| Slow and expensive on a simple question | Full history plus chain-of-thought plus tools that were not needed |

## 9. Tokens, attention, and providers as revision facts

You do not need the training mathematics. You do need the consequences that show up in product behaviour.

A transformer reads the whole current context together, rather than walking a sentence strictly left to right the way older sequential language models did. The practical result is that a relevant word early in a long prompt can still influence a later word, until the window or the noise drowns it. “Attention”, in the intuitive sense used in this course, means the model puts more weight on the tokens that matter for the next prediction.

It is not a guarantee that your most important sentence is the one it weights. Position still matters, which is why critical rules are repeated at the end of a long prompt.

Providers differ in price, window size, and tool-calling reliability. The application pattern stays stable: a client, a model name, a message list, and optional tools. Hosted open models, proprietary hosted models, and a local runner are three operating points on privacy, quality, and cost.

Compare them on a fixed prompt set, not on a single impressive answer.

Public comparisons you may see named (general tests, math sets, code sets, factuality sets) are a starting comparison between models. They do not measure your refund policy. Your golden questions do.

A model that leads a public table can still ignore a house format you never tested.

**Edge cases**

- A long window with a weak model still loses the middle of the prompt. Length is not attention.
- Switching provider without re-testing tool calls is a behaviour change, even when the prompt text is identical.
- A local model that ran offline has no path to today’s price list. Pair it with tools or documents, or accept the cutoff.

## 10. Worked prompt rewrites

**Before.** “You are a helpful assistant. Answer the user.”

**After, for a bounded support decision.**

- Role: support assistant for one shop.
- Task: decide whether the written returns window allows this request.
- Instructions: use only the policy block and the order facts provided. If either is missing, ask for it or refuse.
- Constraints: do not invent a window, do not quote internal staff notes, do not promise a refund you cannot see in the facts.
- Format: `decision`, `reason` citing the fact you used, `missing` as a list.

The rewrite is longer and much easier to grade. Length that adds a constraint is useful. Length that restates “be helpful” is not.

**Chain-of-thought, applied once.** “The user bought on 1 March and today is 25 March. The policy window is 14 days. Count the days, then choose allow or refuse.” That is worth the tokens because the error hides in the count. “Reply hello in a friendly way” does not need those tokens.

**Self-correction, applied once.** Draft the decision. Then check: does every number in the draft appear in the facts? Does the decision match the window? Then emit only the final format. If you show the critique to the user, you are debugging. If you hide it, you are producing a cleaner answer. Say which one you are doing.

**Few-shot trap.** Two examples both refuse, and the third real case should allow. The model imitates the refusals. Balance the examples, or drop them and rely on the rule.

## 11. Worked memory scenarios

**Scenario A — the order number at turn 1.** A window of the last four messages is in force. At turn 12 the user says “cancel it”. The order number was in turn 1 and is gone. The agent asks again, or worse, cancels a different order it sees in a tool result. Pin identifiers outside the sliding window.

**Scenario B — the summary that agreed too early.** The summary says “user wants to cancel order 18”. The user had asked “what happens if I cancel order 18?” A later tool call cancels it. Summaries must mark questions and decisions differently. A safe summary quotes the decision line or records `decision: none yet`.

**Scenario C — the restart.** The demo stored history in a list. The process restarted overnight. The morning user says “same as yesterday” and the agent has no yesterday. Either persist the session, or make the product honest that a new session starts blank.

**Scenario D — the wrong user’s episode.** Long-term search returns “this customer prefers email” because the vector was near and the metadata filter on customer id was forgotten. Every long-term read and write carries the owner id. Similarity is not an access-control system.

**Scenario E — the runaway clarifier.** The model ends every turn with a question, the application always calls the model again, and there is no max-turn rule. Add a limit, and when you hit it, hand the transcript to a person or ask the user to restate the goal in one message.

## 12. Local models in the agent loop

Running a model locally changes the constraints, not the loop. Observe, think, and act stay the same. Tool calls are less reliable on very small models, so the tool set should be smaller and the descriptions stricter.

There is no per-token invoice, and there is a machine bill: memory, disk, and a model that may be too weak for the task. A hosted “cloud mode” of the same runner needs a key and a network again. Treat that flag as a provider switch and re-test.

Do not put production secrets into a prompt just because the model is local. Logs, crash dumps, and a shared laptop still leak. The `.env` habit from the first session remains.

## 13. Recap

An agent is a goal, a loop, memory, and tools around a next-token model. The prompt sets role, task, constraints, and format. Examples and step-by-step reasoning are paid for in tokens and used when a rule or a calculation needs them.

Short-term memory is the session, managed by buffer, window, or summary. Long-term memory is a store with an owner and an expiry story. The model does not remember by itself, does not know today’s private facts, and will sound sure when it is guessing.

## 14. Distinctions to keep straight

Each line is a distinction. If you can say both sides, you have the concept.

- A workflow follows a path written in advance. An agent chooses the next step from the current state, inside limits you set.
- Fluency is not action. Narrating a tool call is not the same as the program running the tool.
- The model is the decision maker. The tool is the worker. A missing tool means the model can only talk.
- A hallucination is a confident completion without a source. A knowledge cutoff is a fact that was never in training or in the prompt.
- Temperature changes variety. It does not add facts.
- A large context window can still drop the front of the prompt. Critical rules belong where the model will still see them.
- The system role is designed to outrank the user role. A user can still try to override it. That attempt is an injection, and the system text is not a lock.
- Zero-shot gives rules only. Few-shot also gives examples. Examples that contradict the rules usually win.
- Chain-of-thought spends tokens to force intermediate steps. Use it when a skipped step would change the decision.
- Generate, critique, rewrite is one prompt pattern. A user correction on the next turn is a different loop. Both need a retry limit.
- Stateless means this call cannot see the last one. Stateful means you deliberately sent the past back in.
- The context window is a size limit. Context engineering is the choice of what occupies that size.
- Buffer memory keeps everything and grows without bound. Window memory keeps the tail and loses the opening facts. Summary memory saves space and can mis-state a decision.
- Episodic memory is an event. Semantic memory is a standing fact. Procedural memory is how a job is done.
- A Python list of messages dies with the process. A session that must survive a restart is written to a store.
- A session id continues one history. A new id starts a blank one. The wrong id continues someone else’s history.
- A stop rule is part of the design: max turns, a user stop phrase, or a completed goal. Without it, a polite model that keeps asking questions spends until a platform limit stops it.
- Human approval is for actions that are hard to undo. It is not required for every sentence the model drafts.
- A local model changes privacy, hardware, and quality. It does not remove the need for tools, logs, or secret handling.
- A public benchmark compares models on public tasks. Your own questions compare models on your task.

## 15. A single turn, named in order

Say this sequence without notes.

1. Load the system prompt: role, task, constraints, format, tool policy.
2. Load pinned facts that must not be summarised away, such as an order id.
3. Load long-term memory for this user only.
4. Load the short-term strategy you chose: buffer, window, or summary plus recent turns.
5. Append the new user message.
6. Call the model at a temperature that matches the job. Low for a decision or a tool choice. Higher only when variety is the product.
7. If the model requests a tool, the program validates and runs it, then returns the observation. That is the next session’s tool loop. Here, remember only that the observation must re-enter context.
8. Apply the stop rule before you automatically call the model again.
9. Decide what is appended to session memory and what is written long-term. Do not write secrets or unconfirmed guesses.
10. If the process might restart, the write in step 9 must hit a real store.

Miss step 3’s user filter and you leak. Miss step 8 and you loop. Miss step 9’s restraint and you remember a hallucination forever.

## 16. Terms to define in one sentence

- **Agent:** a system that observes, chooses a next step toward a goal, and acts through tools.
- **Plan:** an ordered set of subtasks, including what to do when a step fails.
- **Tool:** a function the program can run, described so the model can choose it.
- **Human-in-the-loop:** a pause for a person before an action that is hard to undo.
- **Token:** the unit the model reads and writes, smaller than a sentence and often smaller than a word.
- **Context window:** the maximum tokens considered on one call, input and output together.
- **Hallucination:** fluent text that is not supported by training you trust or by text you supplied.
- **Knowledge cutoff:** the point after which the model has no built-in facts unless you retrieve or call a tool.
- **Temperature:** a control on how strongly the model prefers the most likely next token.
- **Max tokens:** a cap on the length of the completion, which can also cut a format in half.
- **System prompt:** the builder’s standing instruction for role, limits, and format.
- **User prompt:** the request being answered now.
- **Few-shot:** examples of the desired input and output placed in the prompt.
- **Chain-of-thought:** an instruction or example that makes intermediate steps explicit.
- **Self-correction:** draft, check against written criteria, then rewrite, with a limit on repeats.
- **State:** information retained from earlier in this interaction.
- **Context engineering:** choosing what occupies the window: pinned facts, summary, recent turns, documents.
- **FIFO eviction:** dropping the oldest turns first when the window is full.
- **Buffer / window / summary:** keep all history, keep the last N messages, or keep a running digest.
- **Episodic / semantic / procedural:** a past event, a general fact, or a way of doing a job.
- **Session id:** the key that keeps one conversation’s short-term memory separate from another.

If a term takes more than one sentence, reread the section that owns it. The sentence is the revision. The section is the explanation.

## 17. Say the failure before you name the fix

- The user repeats the order number every turn. Short-term memory is missing, or the window dropped the first turn.
- The agent cancels an order the user only asked about. A summary recorded a question as a decision.
- The morning session has forgotten the night session. State lived in a list and the process restarted.
- Two users share a preference. Long-term retrieval had no owner filter.
- The same prompt gives two formats. The output rule is vague, the examples disagree, or the temperature is high.
- A private code appears in the answer and was never in the prompt. That is a hallucination, or a document you did not mean to retrieve.
- A refund policy from last year is quoted with confidence. The model’s cutoff, or a stale memory, is standing in for the current document. The document path is the next session.
- The agent asks a follow-up forever. There is no max-turn or task-complete stop.
- A user line says “ignore your rules”. The system prompt was treated as a lock. It is only a priority.
- A tiny greeting triggers a long step-by-step essay. Chain-of-thought is on for a task that did not need it.
- A local demo works on the train and fails on a live price. The model is offline and no tool was attached.
- A strong public benchmark model misses your format. You never tested your format.

Fix the named cause. Adding a longer persona on top of a missing stop rule or a missing filter does not repair it.

## 18. Which memory is this?

- “What did I just say?” is the current window, if the turn is still inside it.
- “What is my order id from the start of this chat?” must be pinned, or a summary that preserved it, once the window has moved on.
- “What language did I prefer last month?” is long-term, semantic, and belongs to one user id.
- “Last Tuesday I asked for a vegetarian menu.” is long-term and episodic. It should expire or it becomes clutter.
- “How does this team book a train?” is procedural. If the procedure changes, the stored steps must change with it.
- “Translate this sentence” can stay stateless. Carrying history only adds cost.
- A secret typed once for a tool call is not a memory candidate. Use it and drop it.
- A guess the model made is not a memory candidate. Write facts that came from the user or from a tool.

## 19. Prompt checklist before you trust a reply

- The role is specific enough that a stranger could tell what the assistant will not do.
- The task is one job, not “help the user”.
- Constraints include the refusal: what to say when the fact is absent.
- The format can represent “unknown” without inventing a number.
- Any example matches the format and does not contradict the rule.
- Step-by-step reasoning is requested only where a skipped step would change the result.
- Temperature matches the job: low for a decision, higher only for variety.
- The assembled prompt, including history and documents, still fits the window.
- A second run on the same input stays inside the format.
- A paraphrase of a prohibited request is still refused.
- The stop rule is written down: max turns, a stop phrase, or a completed goal.
- Irreversible actions are named, and each one waits for a person.
- Long-term writes are tied to a user id and are not guesses.
- Secrets from the turn are used and then left out of memory.
- A local model is not assumed to know today’s private facts.
- History from a previous test case is cleared before the next one.
- The one-sentence definition of each term in the list above still comes back cleanly.

## 20. Self-check

1. What are the four components, and which one actually changes the outside world?
2. Why does a loop need an explicit stop?
3. Why can two calls with the same prompt differ?
4. What is lost when the context window truncates the front of the prompt?
5. When is chain-of-thought worth the extra tokens?
6. Why can few-shot examples overrule a written instruction?
7. What is the difference between a buffer and a summary?
8. Why is a system message not enough to stop prompt injection?
9. What should happen to an irreversible action?
10. Which memory should survive a process restart, and where does it live?

The next revision session starts from the stores those memories and facts live in: tables, embeddings, and the retrieval path that keeps an answer attached to a source.

## Try this yourself

Take one support request: “Can I return this if I bought it 20 days ago?” Write a five-part prompt on paper: role, task, instructions, constraints, and output format.

Include a legal value for “unknown”. Then mark which facts must stay pinned even if the chat window keeps only the last four messages.

The purchase date and the order id should be on that pinned list. A greeting should not.

## Key Takeaways

- An agent observes, thinks, and acts toward a goal. The model decides. Tools change the world. A loop needs a stop rule.
- A model predicts the next token. Temperature changes variety, not knowledge. A full window can drop the start of the prompt.
- A reliable prompt names the role, the task, the constraints, and the format, and it can represent “unknown”.
- Buffer, window, and summary are three ways to keep a session. Long-term memory needs an owner and a store that survives a restart.
- The next notes put those memories and facts into tables and into a retrieval path.

## Important Commands, Libraries, Terminologies used

| Term | Meaning |
|---|---|
| Observe → Think → Act | The agent loop, repeated until a stop rule |
| Token / context window | The unit of text / the maximum tokens on one call |
| Temperature | How strongly the model prefers the likely next token |
| System / user / assistant | Standing rules / the request / the reply |
| Zero-shot / few-shot / chain-of-thought | Rules only / rules plus examples / explicit intermediate steps |
| Buffer / window / summary | All history / the last N messages / a running digest |
| Episodic / semantic / procedural | An event / a standing fact / a way of doing a job |
| Session id | The key that keeps one conversation separate |
| Human-in-the-loop | A person approves an action that is hard to undo |
