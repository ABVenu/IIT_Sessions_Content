# Assignment Subjective

Total Questions: 1  
Difficulty: Medium  
Type: Applied Python implementation (Groq API + token usage + temperature control)

---

## Q1 (Applied, Medium)

**QuickBite** runs a campus food court. Students complain about billing mistakes and food quality on a busy WhatsApp channel. The product team wants a **small Python probe** that:

1. **Classifies** a complaint into exactly one label for routing.  
2. **Drafts** apology copy at two temperature settings so marketing can see **consistency vs creativity**.  
3. **Prints token usage** after each API call so ops can estimate cost.

You are the builder. Write one script that exercises these internals on **Groq**.

---

### Scenario copy (use exactly as given)

**Classifier system message:**

```text
You classify student canteen complaints into exactly one word: Billing, Food, or Other.
Reply with one word only. No punctuation. No explanation.
```

**Classifier user message:**

```text
My biryani was cold and the cashier charged me twice on UPI.
```

**Creative system message:**

```text
You write one short apology line for a campus food court when an item runs out during lunch rush.
Keep it under 20 words. No emojis.
```

**Creative user message:**

```text
We ran out of masala dosa during the lunch rush and many students left unhappy.
```

---

### What your script must do

Create a single file named **`quickbite_internals.py`** that:

1. Reads the API key from the environment variable **`GROQ_API_KEY`** (no hard-coded keys).  
2. Uses the **`groq`** Python client with model **`llama-3.3-70b-versatile`**.  
3. **Call A — Classifier:** Send the classifier system + user messages with **`temperature=0.0`** and **`max_tokens=10`**. Print a header `=== CLASSIFIER (temp=0.0) ===`, the assistant reply, and **`prompt_tokens`** / **`completion_tokens`** from `response.usage`.  
4. **Call B — Creative (steady):** Send the creative system + user messages with **`temperature=0.0`** and **`max_tokens=80`**. Print header `=== APOLOGY steady (temp=0.0) ===`, reply, and usage tokens.  
5. **Call C — Creative (varied):** Repeat **the same** creative messages with **`temperature=1.0`** and **`max_tokens=80`**. Print header `=== APOLOGY varied (temp=1.0) ===`, reply, and usage tokens.  
6. After all three calls, print one line: `Total completion tokens across 3 calls: <sum>`.

**Expected behaviour (illustrative — your exact wording may differ):**

```text
=== CLASSIFIER (temp=0.0) ===
Billing
prompt_tokens: 62
completion_tokens: 1

=== APOLOGY steady (temp=0.0) ===
We are sorry masala dosa was unavailable during lunch; please visit again tomorrow morning.
prompt_tokens: 58
completion_tokens: 18

=== APOLOGY varied (temp=1.0) ===
Sincere apologies for the dosa shortage at lunch — we are restocking for the evening slot.
prompt_tokens: 58
completion_tokens: 22

Total completion tokens across 3 calls: 41
```

(Token numbers will vary slightly by tokenizer; structure and logic must match.)

---

### Submission instructions

- Code all requirements in a **single file** `quickbite_internals.py` in VS Code (or Colab).  
- Set `GROQ_API_KEY` in your environment or Colab Secrets before running.  
- Run the script and confirm all three calls print replies and usage lines.  
- Submit the **complete `.py` file** in the LMS code editor / answer box.

---

### Answer Explanation (for assessors)

**Ideal solution walkthrough**

```python
# quickbite_internals.py — QuickBite internals probe

import os  # Read API key from environment
from groq import Groq  # Groq Python client

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))  # Authenticate with env var
MODEL = "llama-3.3-70b-versatile"  # Model specified in the assignment

CLASSIFIER_SYSTEM = (
    "You classify student canteen complaints into exactly one word: "
    "Billing, Food, or Other. Reply with one word only. No punctuation. No explanation."
)  # Routing rules for Call A

CLASSIFIER_USER = "My biryani was cold and the cashier charged me twice on UPI."  # Fixed test input

CREATIVE_SYSTEM = (
    "You write one short apology line for a campus food court when an item runs out "
    "during lunch rush. Keep it under 20 words. No emojis."
)  # Creative rules for Calls B and C

CREATIVE_USER = (
    "We ran out of masala dosa during the lunch rush and many students left unhappy."
)  # Shared user message for temperature comparison


def run_call(label, system_msg, user_msg, temperature, max_tokens):  # Helper for one completion
  response = client.chat.completions.create(  # Single chat completion request
      model=MODEL,  # Groq model name
      messages=[  # Standard chat roles
          {"role": "system", "content": system_msg},  # System instructions
          {"role": "user", "content": user_msg},  # User input this turn
      ],
      temperature=temperature,  # Sampling randomness knob
      max_tokens=max_tokens,  # Output cap for billing and length control
  )
  text = response.choices[0].message.content.strip()  # Assistant reply string
  usage = response.usage  # Token accounting object from Groq
  print(f"=== {label} ===")  # Section header required by brief
  print(text)  # Model output
  print(f"prompt_tokens: {usage.prompt_tokens}")  # Input token count
  print(f"completion_tokens: {usage.completion_tokens}")  # Output token count
  print()  # Blank line between sections
  return usage.completion_tokens  # Return output tokens for final sum


def main():  # Entry point
  total_completion = 0  # Running sum of output tokens
  total_completion += run_call(
      "CLASSIFIER (temp=0.0)",
      CLASSIFIER_SYSTEM,
      CLASSIFIER_USER,
      temperature=0.0,
      max_tokens=10,
  )  # Call A — stable one-word label
  total_completion += run_call(
      "APOLOGY steady (temp=0.0)",
      CREATIVE_SYSTEM,
      CREATIVE_USER,
      temperature=0.0,
      max_tokens=80,
  )  # Call B — low-temperature apology
  total_completion += run_call(
      "APOLOGY varied (temp=1.0)",
      CREATIVE_SYSTEM,
      CREATIVE_USER,
      temperature=1.0,
      max_tokens=80,
  )  # Call C — high-temperature apology for contrast
  print(f"Total completion tokens across 3 calls: {total_completion}")  # Final aggregate line


if __name__ == "__main__":  # Run only when executed directly
  main()  # Start the three-call demo
```

**Grading notes**

| Criterion | What to check |
|---|---|
| Environment key | Uses `os.environ.get("GROQ_API_KEY")` — no embedded secrets |
| Model + client | `Groq` client, model `llama-3.3-70b-versatile` |
| Call A | Classifier messages, `temperature=0.0`, `max_tokens=10`, one-word style reply |
| Calls B & C | Same creative messages; temps **0.0** vs **1.0**; `max_tokens=80` |
| Usage printing | `prompt_tokens` and `completion_tokens` after each call |
| Final sum | Correct arithmetic on completion tokens across three calls |
| Headers | Exact label pattern `=== ... ===` as specified |

**Alternative valid approaches**

- Inline three separate `create` blocks without a helper function.  
- Slightly different apology wording or classifier label (**Billing** vs **Food** vs **Other**) if the complaint reasonably maps that way — **Billing** or **Food** both acceptable for the sample complaint; penalise only if output is not a single token-like word.  
- `if __name__` block optional if script runs top-to-bottom correctly.

**Common mistakes**

- Hard-coded API key in source.  
- Missing `max_tokens` on classifier call (rambling replies).  
- Only one creative temperature — assignment requires **both** 0.0 and 1.0.  
- Printing usage from only one call.  
- Wrong model name or missing `response.usage` access.
