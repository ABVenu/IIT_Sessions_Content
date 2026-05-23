# Pre-read: Introduction to LangChain — Concepts, Chains, and Prompt Templates

You have already learned how to **talk to a language model** — from the browser, from Python, even from your own laptop with **Ollama**. You know that a good **prompt** can change everything.

Now imagine you are building something real — a **placement helpdesk**, a **study buddy**, or a tool that **reads a résumé**, **summarises it**, and **drafts an email**. Every step needs a different instruction. Tomorrow the company name changes. Next week you add a spelling check. Next month you want the bot to **remember** what the student asked five messages ago.

At first it feels exciting. Then it feels messy.

---

## The challenge we are solving

What if your entire AI feature lived inside **one giant block of text** in a single Python file — copy-pasted prompts, API keys, and formatting rules all tangled together? Change the greeting once and you break three other flows.

What if you had to **wire five steps by hand** every time: load data → build prompt → call the model → clean the answer → show it — and each new project meant **rewriting the same glue code**?

What if you wanted to **swap** from a cloud model to a local one without rewriting the whole app?

Raw **LLM API calls** work for a demo. They get painful when prompts grow, steps multiply, and you head toward **agents** with tools, memory, and search. You need **structure** — smarter building blocks, not more typing.

That structure is what we open in the live session: **LangChain**.

---

## What we will build toward

**LangChain** is an **open-source framework** for building apps powered by large language models. It sits **between** “the model from OpenAI / Ollama / etc.” and **your product** — your site, your agent, your internal tool.

Instead of one long script, you learn a **mental model**: small pieces called **Runnables** snap into **chains** — pipelines where one step’s output feeds the next. You will see how **chains**, **agents**, **tools**, **memory**, and **retrievers** fit one picture (we build the **first simple chain** today).

The focus is your **first reusable workflow**: a **PromptTemplate** (prompt with blanks) **piped** to an **LLM**, with **predictable text output**. We use **LCEL** — LangChain Expression Language — and the **pipe operator** (`|`) for a readable left-to-right flow.

By the end, **hardcoded** vs **templated** prompts on the same task should feel obviously different — a sticky note vs a **recipe card** anyone can reuse.

---

## A simple analogy from daily life

Raw API-only coding is like cooking **biryani** from memory every Sunday. It works until guests arrive, spice levels change, or your cousin helps — then nobody agrees on the steps.

**LangChain** is a **labelled kitchen**: measured bowls (**templates**), fixed order (**chain**), standard connectors so you **swap the stove (model)** without redesigning the meal.

The **pipe (`|`)** in LCEL is a **conveyor belt** — filled prompt to model, finished answer off the belt.

---

In this pre-read, you'll discover:

- **Why** teams use a **framework** when prompts, memory, tools, and multi-step flows multiply.
- **Where** LangChain sits on the **agentic stack** — between **model provider** and **your app** — and what **Core** vs **Community** mean in practice.
- **How** **PromptTemplate** and **ChatPromptTemplate** keep prompts **reusable** and **variable-driven**.
- **How** your **first LCEL chain** — template **piped** to LLM — delivers **string output** your code can trust.

---

## Words you will hear — explained right away

- **LangChain**: Toolkit to compose LLM apps from reusable parts.
- **Runnable**: A unit you **invoke**; output of one can feed the next.
- **Chain**: Linked steps — step one’s output becomes step two’s input.
- **PromptTemplate / ChatPromptTemplate**: Prompts with **placeholders** or **chat roles** you fill before calling the model.
- **LCEL**: Build chains with `|` — e.g. template **|** LLM.
- **Agent / Memory / Retriever (preview)**: Model picks **tools**; **memory** holds context; **retrievers** fetch documents — mapped today, depth later.
- **String output**: Chain ends in **plain text** your UI can show or parse.

**Hardcoded** = full instruction fixed in code. **Templated** = only **slots** change; the skeleton stays stable.

---

## Where this shows up in real work

- **Support bots** reusing the same polite system message with a **new ticket topic** each time.
- **HR tools** that chain “summarise CV” then “draft email” without duplicating API wiring.
- **Student projects** swapping **local Ollama** for **cloud** by changing one link, not every prompt string.
- **Road to agents**: today’s **template → model** chain is the spine you extend with **tools** and **memory** soon.

---

## Questions we will tackle live

1. **Three features** — summarise, translate, quiz — each with a long prompt in one file. **What breaks first** when tone must change everywhere, and how does **PromptTemplate** help?
2. Same task: **hardcoded** prompt in `print(...)` vs **PromptTemplate + LCEL chain**. **What would you show a non-technical teammate** to prove the second is easier to reuse?
3. Your chain returns something the UI cannot display. **Where do you fix it** — template, model call, or **output handling** — and what does “string output” buy you?

---

## After this session, you should be able to

- **Explain in one sentence** what LangChain is and why raw API calls become hard to maintain.
- **Place LangChain** on the agentic stack and name **chains, agents, tools, memory, retrievers** at overview level.
- **Use** **PromptTemplate** or **ChatPromptTemplate** for variable-driven, reusable prompts.
- **Follow** a simple **LCEL** chain: **PromptTemplate → LLM**, with **string output** handling.
- **Compare** hardcoded vs templated prompts and say **which you would ship** to a small team.
- **Know** multi-agent framework comparison waits for **Module 4** — today: **one clear chain, done well**.
