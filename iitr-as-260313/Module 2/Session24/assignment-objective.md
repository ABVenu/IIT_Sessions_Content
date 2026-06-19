# Objective Assignment: Tool Integration in AI Agents

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A ShopKart customer writes: *"Can I return unopened headphones within seven days?"* Your agent has **`search_shopkart_policy`** and **`get_city_weather`** registered with **`tool_choice="auto"`**. Which tool should the model route to for this question?

A. **`get_city_weather`**  
B. **`search_shopkart_policy`**  
C. Both tools must always run for every message  
D. No tool — the model should invent policy rules from memory

**Correct Answer:** B

**Answer Explanation:**  
B is correct because the question is about **returns eligibility and timelines** — policy text, not live weather. The policy search tool is the right match.

A is incorrect because temperature data does not answer a returns window question. C is incorrect because **`auto`** routing picks only what the question needs — not every tool on every turn. D is incorrect because support answers must be **grounded in tool JSON**, not invented policy.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

Ankita builds a ShopKart agent with **Groq function calling**. When the model chooses **`get_city_weather`**, who actually sends the HTTP GET request to Open-Meteo?

A. The Groq cloud service imports and runs her `.py` file on her laptop automatically  
B. The customer's phone browser  
C. **Ankita's Python runtime** after it parses **`tool_calls`** and calls the local wrapper function  
D. Open-Meteo pushes weather data directly into the LLM weights

**Correct Answer:** C

**Answer Explanation:**  
C is correct because the **model only requests** a tool in structured JSON — **your agent runtime** executes the Python function that performs **`requests.get`**.

A is incorrect because Groq does not execute undeployed local code on your machine. B and D describe unrelated paths — browsers and model weights do not perform the weather GET in this architecture.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

Your Groq chat call includes **`tool_choice="auto"`**. What does this setting mean in practice?

A. The user must type the tool name in the terminal before each question  
B. The vector database picks which tool to execute  
C. **The model decides** whether to call tools and **which registered tools** to use  
D. **`get_city_weather`** is always invoked before **`search_shopkart_policy`**

**Correct Answer:** C

**Answer Explanation:**  
C is correct — **`auto`** lets the LLM read tool **descriptions** and the user message, then emit zero or more **`tool_calls`** as needed.

A and B shift the decision to the human or database, which is not how **`auto`** works. D describes a hard-coded order, which defeats flexible routing.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A stock-data company publishes an **MCP server** so agents can fetch live prices without hand-written HTTP code for every ticker. In simple terms, what job does that MCP server do?

A. Permanently fine-tunes the LLM on every historical price  
B. **Acts as a translator** — the LLM sends English tool requests; the server turns them into the company's internal API calls  
C. Removes the need for JSON in function calling entirely  
D. Stores and shares every user's **`GROQ_API_KEY`** publicly

**Correct Answer:** B

**Answer Explanation:**  
B is correct — an MCP server is a **standard integration layer** that understands the LLM's tool requests and runs the vendor's APIs behind the scenes.

A is incorrect — MCP connects at runtime; it is not model training. C is incorrect — tool calling still uses structured JSON. D is incorrect and unsafe — API keys stay in your **`.env`**, not on a public MCP listing.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

In the standard **tool execution loop**, a customer has just sent a ShopKart question. The runtime has passed the **system prompt**, **user message**, and **`tools`** list to Groq. The question clearly needs live weather. What is the **first** action typically taken by the **model** (not your Python script)?

A. Run **`get_city_weather`** on the laptop  
B. Append a **`role: tool`** message with JSON results  
C. **Return structured `tool_calls`** naming the function and JSON arguments  
D. Print the final natural-language answer directly to the customer

**Correct Answer:** C

**Answer Explanation:**  
C is correct — step 3 in the loop is the **model proposing** **`tool_calls`** (or a direct answer if no tool is needed). Execution happens **after** that.

A and B are **runtime** steps that occur only after the model proposes tools. D is the **final** step after tool results are fed back.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

Inside your tool loop you write:

```python
raw_arguments = tool_call.function.arguments
arguments = ???  # fill this line
result = TOOL_FUNCTIONS[function_name](**arguments)
```

The model sends **`arguments`** as a JSON **string**. Which call correctly converts it to a Python **dict** before `**arguments`?

A. **`json.loads(raw_arguments)`**  
B. `json.dumps(raw_arguments)`  
C. `response.json()`  
D. `str(raw_arguments)`

**Correct Answer:** A

**Answer Explanation:**  
A is correct — **`json.loads()`** parses a JSON string into a Python dictionary so keyword arguments can be unpacked into your tool function.

B serialises dict → string (opposite direction). C is a **`requests`** response method, not for model tool argument strings. D keeps a string type and will not work with `**arguments`.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

You register ShopKart tools in Groq's **`tools`** list. Which fields belong in the **function schema the model reads for routing**? Select **all** that apply.

A. **`name`** — short identifier emitted in **`tool_calls`**  
B. **`description`** — when and why to use this tool  
C. **`parameters`** — JSON Schema for expected arguments  
D. **`tool_call_id`** — assigned when registering the tool at startup

**Correct Answers:** A, B, C

**Answer Explanation:**  
A, B, and C are the three schema pieces that guide routing — identifier, routing instructions, and argument contract.

D is incorrect — **`tool_call_id`** is generated on the **assistant message** when the model responds, not supplied in the registration schema at startup.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A customer asks: *"I chose express delivery to Bangalore metro tomorrow. What does policy say about express timing, and what is the current temperature there?"* Your agent uses **`tool_choice="auto"`** with policy and weather tools registered. Which statements are **correct**? Select **all** that apply.

A. **Both** **`search_shopkart_policy`** and **`get_city_weather`** may be called before the final reply  
B. Replacing **`auto`** with hard-coded `if "express" in query: get_city_weather()` is **more flexible** than model routing  
C. The final answer should cite **express timing from policy tool JSON excerpts** when available  
D. If policy text has **no weather-impact rule**, the model should **still invent** courier delay guidance so the answer sounds complete

**Correct Answers:** A, C

**Answer Explanation:**  
A is correct — this question mixes **policy rules** and **live weather**, so both tools may be needed. C is correct — grounded answers must trace policy numbers to **tool JSON**, not guesswork.

B is incorrect — hard-coded branches break on wording variants; **`auto`** routing scales better. D is incorrect — inventing rules when tools lack evidence is **hallucination**; honest answers stop at what tools returned.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

Your **`get_city_weather`** wrapper receives **HTTP 503** from Open-Meteo. Which practices prevent **hallucinated weather** in the final ShopKart reply? Select **all** that apply.

A. Return structured JSON such as **`{"error": "Weather API failed", "status_code": 503, "city": "Delhi"}`** instead of fake temperature fields  
B. Call **`response.json()`** on the error body and pass guessed **`temperature_c: 28.0`** to the model  
C. Include a system prompt rule: **ground answers in tool JSON only — do not invent weather**  
D. Omit the tool result message so the model freely estimates today's rain

**Correct Answers:** A, C

**Answer Explanation:**  
A is correct — **honest error JSON** tells the model weather is unavailable. C is correct — grounding instructions plus error JSON lead to safe refusals.

B is incorrect — guessing temperature from failed responses invents data. D is incorrect — skipping tool results encourages the model to fill gaps with fiction.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

You run **Groq function calling** with **locally defined** Python tools (not deployed online). Which statements are **true**? Select **all** that apply.

A. Groq returns **`tool_calls`** as structured JSON; your script matches names in **`TOOL_FUNCTIONS`** and runs them locally  
B. Groq's servers directly **`import shopkart_tool_agent`** from your laptop and execute it in the cloud  
C. After each tool runs, you append a message with **`role: tool`**, matching **`tool_call_id`**, and **`content: json.dumps(result)`**  
D. **`json.dumps(result)`** serialises the Python dict so the model can read tool output as JSON text

**Correct Answers:** A, C, D

**Answer Explanation:**  
A is correct — cloud LLM proposes tools; **local runtime executes**. C is correct — tool results must link **`tool_call_id`** and carry serialised JSON. D is correct — **`json.dumps`** is the standard serialisation step before the next model call.

B is incorrect — undeployed local files are **not** imported by Groq; your machine runs the functions.
