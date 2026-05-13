# Assignment — Subjective (Session 35: GenAI Concepts for Beginners)

**Type:** One practical coding task (medium difficulty, applied / scenario-based)  
**Scope:** Token counting (`tiktoken`), prompt versus completion budgeting, context-window fit checks, a common **words ↔ tokens** heuristic, and optional **temperature** comparison via an LLM API (see Part F).

---

## Scenario

You volunteer for your college **Eco-Council**. The council president wants to try an LLM to polish outreach emails, but they are worried about **cost** and about hitting **context limits** on cheaper models. They asked you for a **small sanity-check script** they can run before any campaign goes live.

---

## Your task

Create **one** Python file named `eco_council_llm_sanity.py` that does **all** of the following when run with `python eco_council_llm_sanity.py`:

### Part A — Build a realistic prompt string (no API calls yet)

Inside the file, define **three** Python strings and then concatenate them (with clear separators like newlines) into one variable called `full_prompt`:

1. **`safety_block`** — Between **40 and 70 words**, instructing the model to stay factual, avoid inventing sponsors, and refuse if information is missing.  
2. **`email_body`** — Between **100 and 140 words**, a draft thank-you email to a fictional sponsor (`GreenLeaf Motors`) for funding a tree-planting drive. Mention date, venue city, and student volunteers generically (you may invent plausible details).  
3. **`follow_up_instruction`** — **Exactly one sentence** asking the model to suggest a subject line under 60 characters.

Concatenate into **`full_prompt`** (order: safety → email → follow-up).

### Part B — Exact prompt token count with `tiktoken`

- Import `tiktoken`.  
- Create an encoder with `tiktoken.encoding_for_model("gpt-4")`. If your environment raises an error, fall back to `tiktoken.get_encoding("cl100k_base")` and print a one-line note that you used the fallback.  
- Print: `Prompt tokens (tiktoken): <integer>` using `len(encoder.encode(full_prompt))`.

### Part C — Completion budget estimate (rule of thumb)

Assume the model’s answer may be as long as **220 words** of completion text.

Use the common English heuristic **≈ 1 token per 0.75 words** (i.e. estimated completion tokens ≈ words ÷ 0.75). Compute and print:

`Estimated completion tokens (rule of thumb): <value>`  

Include a short **comment** next to your calculation showing the formula you applied.

### Part D — Context window check

Assume a **4096-token** context limit (a realistic budget for many small or legacy chat models). Set `CONTEXT_LIMIT = 4096`.

Let `prompt_tokens` be the integer from Part B. Let `completion_tokens_est` be your estimate from Part C, **rounded up** to the nearest integer for the fit test.

Print **both** of the following on separate lines:

- `Total tokens needed (rounded-up completion): <prompt_tokens + completion_tokens_est>`  
- `Fits in 4096 window? <True or False>` — `True` only if the sum is **≤ 4096**.

### Part E — Concept recall (printed, not from API)

Print a short paragraph (**80–120 words**, plain text) in your own words that explains **why the same prompt can yield different answers** on repeated API calls, linking the behaviour to **probabilistic next-token** generation. Paraphrase; do not copy text from any single published tutorial verbatim.

### Part F — Optional: temperature and how “creative” the reply feels

**Task**

You will **compare how creative or varied** the model’s wording is when the **same user message** is sent twice at **different temperatures**. The prompt is intentionally a bit loose (**“Describe how is the cloud today??”**) so you can see whether the answers differ in imagination or tone, not only in facts.

**Instructions**

1. **If** `OPENAI_API_KEY` is set in the environment, use the official **`openai`** Python package: `from openai import OpenAI`, then create a client (read the key from the environment; **never** embed a key as a string literal in code you submit).
2. Make **two** separate API calls to a **chat completions** endpoint. Each call must use **exactly** this `messages` argument (verbatim user text, including punctuation):

   `messages=[{"role": "user", "content": "Describe how is the cloud today??"}]`

3. Use the **same model id** for both calls, for example **`gpt-4o-mini`** (or another small model your key supports, but keep it **identical** across the two calls).
4. First call: **`temperature=0.2`**. Second call: **`temperature=0.9`**. Print each assistant reply with a clear header, e.g. `--- temperature=0.2 ---` and `--- temperature=0.9 ---`.
5. For the **default OpenAI** path: if `OPENAI_API_KEY` is **not** set, print exactly:  
   `Skipping live temperature demo — set OPENAI_API_KEY to enable.`  
   If you implement **another** provider from the Note and that provider’s API key is **not** set, print a **one-line** skip that names the missing environment variable (do not call the API without a key).

**Note (Part F)**

- **API keys:** Use environment variables (or a local `.env` that you do **not** commit). Do not paste real keys into source or into the LMS.
- **Other providers:** You may use **Google Gemini**, **OpenRouter**, **xAI Grok**, **Groq**, or another chat LLM instead of OpenAI, as long as you send the **same user string** as above, use a **`messages`-style** chat structure with a **user** role (or the provider’s equivalent), run once at **0.2** and once at **0.9**, and print both replies with the same style of labels.
- **Document the SDK call:** In a short comment next to your Part F code, name the **exact function or method** you use to obtain the model text (for example `client.chat.completions.create`, `GenerativeModel.generate_content`, or the Groq client method you call) and which **environment variable** holds the API key.

---

## Example output shape (illustrative — your numbers will differ)

Your script’s console output should resemble (values not literal requirements except labels):

```text
Prompt tokens (tiktoken): 312
Estimated completion tokens (rule of thumb): 294
Total tokens needed (rounded-up completion): 606
Fits in 4096 window? True
Skipping live temperature demo — set OPENAI_API_KEY to enable.
<your 80–120 word paragraph here>
```

If `OPENAI_API_KEY` is set, the skip line is **replaced** by two blocks such as `--- temperature=0.2 ---` then the model text, then `--- temperature=0.9 ---` then the model text (your exact wording will differ).

---

## Submission instructions (**case c** — single file)

- Code **all** parts in **Visual Studio Code** in a **single** file named `eco_council_llm_sanity.py`.  
- Run the file locally and confirm it prints without errors (`python eco_council_llm_sanity.py`).  
- **Submit** the complete file in the **code editor / answer box** in the LMS (paste the full source code).

**Dependencies:** You may assume `pip install tiktoken openai` is allowed for the default Part F path. Do **not** commit real API keys; use `OPENAI_API_KEY` from the environment (or the env var required by your chosen alternative API).

---

## Answer explanation (for Assess platform)

**Ideal walkthrough**

1. **Part A** checks that learners can assemble a **multi-section prompt** (policy block + draft content + a precise downstream instruction), mirroring real integration patterns.  
2. **Part B** validates correct use of **`tiktoken`**: `encode` then `len` for exact **prompt-token** measurement.  
3. **Part C** applies the given **0.75 words per token** heuristic in the completion-budget direction.  
4. **Part D** tests the definition that **prompt + completion** must fit one **context window**; `4096` is a concrete threshold typical of smaller commercial models.  
5. **Part E** probes understanding of **sampling / stochastic decoding** without requiring network access.  
6. **Part F** is optional; when enabled, it compares **creative variation** on the same playful user prompt at **temperature 0.2** vs **0.9** using a real chat API call (default: OpenAI `chat.completions.create`; other vendors allowed per the note under Part F). Learners should comment which SDK **function/method** they invoked.

**Alternative approaches**

- If `encoding_for_model("gpt-4")` fails, document use of `cl100k_base` or another encoding consistent with your target API.

**Reference solution sketch (evaluators only — students may paraphrase structure)**

```python
import os
import tiktoken
from openai import OpenAI

safety_block = """..."""  # 40-70 words
email_body = """..."""    # 100-140 words
follow_up_instruction = "One sentence here."
full_prompt = "\n\n".join([safety_block, email_body, follow_up_instruction])

try:
    enc = tiktoken.encoding_for_model("gpt-4")
except Exception:
    enc = tiktoken.get_encoding("cl100k_base")
    print("Note: using cl100k_base fallback encoding.")

prompt_tokens = len(enc.encode(full_prompt))
print(f"Prompt tokens (tiktoken): {prompt_tokens}")

completion_words = 220
completion_tokens_est = int((completion_words / 0.75) + 0.999)  # round up
print(f"Estimated completion tokens (rule of thumb): {completion_tokens_est}")

CONTEXT_LIMIT = 4096
total = prompt_tokens + completion_tokens_est
print(f"Total tokens needed (rounded-up completion): {total}")
print(f"Fits in 4096 window? {total <= CONTEXT_LIMIT}")

print(
    "Your paragraph here explaining probabilistic next-token sampling "
    "and why outputs can vary between runs."
)

# Part F: e.g. client.chat.completions.create(...) ×2 with temperature 0.2 and 0.9
CREATIVE_PROMPT = "Describe how is the cloud today??"
msgs = [{"role": "user", "content": CREATIVE_PROMPT}]

if os.environ.get("OPENAI_API_KEY"):
    client = OpenAI()
    for temp in (0.2, 0.9):
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=msgs,
            temperature=temp,
        )
        print(f"--- temperature={temp} ---")
        print(r.choices[0].message.content)
else:
    print("Skipping live temperature demo — set OPENAI_API_KEY to enable.")
```

---

**End of subjective assignment.**
