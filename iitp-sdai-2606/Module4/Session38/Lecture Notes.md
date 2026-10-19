# Introduction to Large Language Models

You have built a full stack: Python and DSA, HTML/CSS/JS and APIs, FastAPI with SQLAlchemy, and a persistent `campus_api`. In the previous session you used **Claude** on that app to draft routes, ORM queries, and documentation. Claude felt like a fast junior clerk—but every reply still came from a **Large Language Model (LLM)** running behind the chat window.

Today you open that black box at a **conceptual** level: what an LLM is, why the **Transformer** design matters, how **tokenization** turns your sentences into numbers, and how models **read** and **write** text one step at a time. You will not train a model from scratch, and you will not study prompt recipes yet—that comes next when you learn to **steer** model output with clear instructions.

![From your typed sentence to token IDs, through a Transformer stack, to the next piece of text the model prints](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session38/session38-01-text-to-tokens-to-text.png?v=20261019)

## What you will learn in this lesson

- **LLM fundamentals** — definition, scale, pre-training vs chat use, strengths and limits
- **Transformer architecture** — high-level picture: embeddings, attention, layers, output head
- **Tokenization** — chunks of text, token IDs, vocabulary, and why Hindi-English mix behaves differently
- **Hands-on** — encode/decode text, trace a toy generation loop, and call **Gemini** with **`fetch`** (change **temperature** only: sky-color question at **0** vs **0.9**)

Connecting idea: Coding labs taught you to **use** AI assistants responsibly. This lesson teaches you **what the assistant is**, so later prompt work and app integrations make sense.

---

## Why language models matter for your stack

- **Official Definition:** A **Large Language Model (LLM)** is a neural network trained on vast text to model the probability of the next token (or token sequence) given prior context.
- **In Simple Words:** The model has read enormous amounts of text and learned patterns—so it can guess sensible continuations of what you type.
- **Real-Life Example:** A seasoned typist in a government office who has seen thousands of letter formats can finish the first line you dictate. An LLM does something similar with language, not with your `campus.db` rows unless you explicitly pass them in the prompt.

| You already did (earlier course work) | What changes today |
| --- | --- |
| Used ChatGPT/Claude to explain DSA and draft code | You study the **engine**, not the **IDE button** |
| Built REST APIs and SQLAlchemy models | LLMs do not replace databases; they **generate text** |
| Reviewed every AI draft before running Uvicorn | Same habit—models can sound confident when wrong |

**Need:** Before you wire LLMs into products, you must know how input becomes numbers and how output is produced token by token.

**Common doubt:** “Is Claude the same as GPT?” — Different products and policies, but most modern chat models share the same broad recipe: **Transformer + tokenization + next-token prediction**, plus extra training to be helpful in dialogue.

---

## What is a Large Language Model?

- **Official Definition:** **LLM** usually means a **language model** with billions (or more) of **parameters**—the learned numbers inside the network that store patterns from training data.
- **In Simple Words:** Parameters are like adjustable knobs tuned during training so the model gets better at predicting text.
- **Real-Life Example:** A giant register of language habits—not a single FAQ file, but a compressed summary of patterns seen in books, websites, and code.

**“Large” refers to:**

- **Model size** — many parameters (weights)
- **Training data** — huge corpora of text (and sometimes code)
- **Compute** — training needs specialised hardware clusters; you typically **use** a hosted model via API or app

**What LLMs are good at:**

- Drafting and summarising text in many languages
- Explaining concepts in plain language
- Suggesting code **snippets** when you describe intent (as in your GenAI labs)
- Following instructions **when** the prompt is clear (you will practise that next)

**What LLMs are weak at without extra design:**

- Guaranteed factual accuracy (they **predict**, they do not **look up** truth)
- Private data they never saw (your local `.env` is not inside the model)
- Exact arithmetic on long chains unless tools or careful prompting help
- Deterministic “always the same answer” unless temperature and seed are controlled

**Logic to remember:** Treat an LLM as a **strong language predictor**, not as a database, calculator, or deployed FastAPI server.

![Parameters as many tuned knobs; training adjusts them using examples of “what text usually comes next”](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session38/session38-02-parameters-knobs.png?v=20261019)

### Activity — Label the claim

For each statement, write **True**, **False**, or **Partly true** and one line why:

1. An LLM stores a copy of every website on the internet inside its weights.
2. The same prompt can give different answers if the app uses randomness.
3. Deleting a row in `campus.db` automatically updates what the cloud model “knows.”
4. Your GenAI coding lab used an LLM even when you only asked for a FastAPI skeleton.

---

## Pre-training and chat models (high level)

You do not need the full training pipeline today—only the **two-stage story** most products use.

**Stage 1 — Pre-training**

- **Goal:** Learn general language patterns by predicting masked or next tokens on massive text.
- **Analogy:** Reading lakhs of exam papers to learn how sentences usually flow—not memorising one paper by roll number.

**Stage 2 — Alignment / instruction tuning (simplified)**

- **Goal:** Shape the base model to follow user instructions and refuse harmful requests where policy requires.
- **Analogy:** After general reading, a trainee clerk learns your office’s letterhead format and tone.

| Term | Meaning in one line |
| --- | --- |
| **Base model** | Strong text predictor; may not follow chat instructions well |
| **Instruct / chat model** | Fine-tuned (or similarly trained) to answer as an assistant |
| **Context window** | Maximum tokens the model can consider at once for one request |

**Common mistake:** Assuming the model “remembers” your last coding lab session globally. Each API call sends a **fresh context** (your messages in that chat). Persistence is the **app’s** job (database, files), not the weights’ job.

Connecting idea: Tokenization decides how many characters fit in the context window—next section.

---

## Tokenization — how text becomes numbers

Computers do not store “words” natively in neural nets—they store **numbers**. **Tokenization** is the bridge.

- **Official Definition:** **Tokenization** splits raw text into **tokens** (subword units, words, or symbols) and maps each token to an integer **token ID** using a fixed **vocabulary**.
- **In Simple Words:** Cut your sentence into puzzle pieces the model was trained on, and give each piece a serial number.
- **Real-Life Example:** A pantry labels jars (“dal”, “chana”, “masala”) instead of dumping whole sacks. The model reads labeled jars, not your handwriting on a bag.

**Why subwords?**

- Rare words split into smaller pieces so the vocabulary stays finite.
- English, Hindi (Roman script), code, and emoji can share some pieces; others are language-specific.

**Effects you will notice:**

| Text | Typical observation |
| --- | --- |
| `"Hello campus"` | Few tokens in English |
| `"Namaste, aaj class hai"` | Token count may differ from word count |
| `"GET /students?city=Pune"` | Slashes and punctuation often become their own tokens |
| Long JSON from `/docs` | Token count rises fast—context limits matter for AI on APIs |

**Special tokens (conceptual):**

- Markers for **start/end of sequence**, **padding**, or **roles** in chat templates (system/user/assistant)—exact names vary by model family.
- **Common doubt:** “Why did my Hindi line cost more?” — More or longer tokens → more compute → higher API usage where billing is per token.

![Sentence on the left split into token chips; each chip maps to an ID in a vocabulary table](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session38/session38-03-tokenization-chips.png?v=20261019)

### Hands-on setup — token lab

Create a folder `llm_token_lab`, activate a venv, and install libraries used only for **encoding demos** (not for training).

```bash
mkdir llm_token_lab  # Folder for today’s small scripts
cd llm_token_lab  # Enter the folder
python3 -m venv .venv  # Same pattern as campus_api
source .venv/bin/activate  # Enable the virtual environment
pip install tiktoken transformers  # tiktoken + Hugging Face tokenizers
```

---

### Full code — explore tokens with `tiktoken`

Save as `explore_tiktoken.py`. This uses OpenAI’s **cl100k_base** encoding—a common teaching example for GPT-style tokenizers.

```python
# explore_tiktoken.py — show how text becomes token IDs and back

import tiktoken  # Library for OpenAI-compatible token counting

def main():
    # Pick an encoding widely used in GPT-4 era models (teaching example)
    enc = tiktoken.get_encoding("cl100k_base")  # Load the vocabulary tables

    samples = [
        "Hello from campus_api!",  # Short English with punctuation
        "Namaste, aaj SQLAlchemy class hai.",  # Hindi-English mix
        "GET /students?city=Pune HTTP/1.1",  # Looks like your API route
    ]

    for text in samples:
        # encode converts text -> list of integer token IDs
        ids = enc.encode(text)  # Each ID is one token in this vocabulary

        # decode converts IDs back to text (should match original for plain text)
        back = enc.decode(ids)  # Round-trip check

        # Show human-readable token strings (pieces after splitting)
        pieces = [enc.decode([i]) for i in ids]  # One piece per ID

        print("=" * 60)  # Visual separator between samples
        print("TEXT:", text)  # Original string you typed
        print("WORD COUNT (split on spaces):", len(text.split()))  # Naive word count
        print("TOKEN COUNT:", len(ids))  # What the model "sees"
        print("TOKEN IDS:", ids)  # Raw numbers sent to the model internally
        print("TOKEN PIECES:", pieces)  # How the string was chopped
        print("ROUND TRIP:", back)  # Should equal text unless normalization occurred
        print()  # Blank line for readability


if __name__ == "__main__":
    main()  # Run the demo when you execute the file
```

**How the code works:**

- **`get_encoding`** loads a fixed vocabulary; the model family chooses which encoding table to use in production.
- **`encode`** returns IDs; **`decode`** rebuilds text—proves tokenization is reversible for normal strings.
- **Word count ≠ token count** — your API billing and context limits follow **tokens**, not words.
- Comparing the **route string** shows punctuation and slashes often become separate tokens—relevant when you paste OpenAPI JSON into a chat.

### Activity — token diary

Run `python explore_tiktoken.py`. Copy one line from your real `StudentOut` JSON example (from the campus project) into a fourth `samples` entry. Note whether token count is closer to word count or much higher.

---

### Full code — compare with a Hugging Face tokenizer (GPT-2 table)

Different model families use different vocabularies. Save as `explore_hf_tokenizer.py`.

```python
# explore_hf_tokenizer.py — second vocabulary to show family differences

from transformers import AutoTokenizer  # Loads tokenizer files from Hugging Face Hub

def main():
    # GPT-2 tokenizer is small and common in tutorials (downloads once on first run)
    tok = AutoTokenizer.from_pretrained("gpt2")  # Build encode/decode helpers

    sentence = "marks >= 85 and hostel_name in response"  # Domain words from your backend

    # HF returns a dict; input_ids are token IDs
    batch = tok(sentence, return_tensors=None)  # No PyTorch tensor needed for demo
    ids = batch["input_ids"]  # List of integers

    tokens = tok.convert_ids_to_tokens(ids)  # Show BPE-style pieces with ## markers sometimes

    print("TEXT:", sentence)  # Your backend-flavoured phrase
    print("TOKEN COUNT:", len(ids))  # Length in this vocabulary
    print("TOKENS:", tokens)  # Human-readable pieces
    print("DECODED:", tok.decode(ids))  # Should match sentence closely


if __name__ == "__main__":
    main()  # Entry point
```

**How the code works:**

- **`AutoTokenizer`** downloads tokenizer config once; encoding rules differ from `cl100k_base`.
- **`convert_ids_to_tokens`** shows **byte-pair** pieces—useful when two encodings disagree on the same English sentence.
- **Takeaway:** “How many tokens?” always depends on **which model** you target—not a universal ruler.

---

## Transformer architecture — overview only

Before Transformers, long sentences were hard for models to handle in one go. The 2017 **Transformer** design fixed that with **attention**—a way to weigh which earlier tokens matter for each new token.

- **Official Definition:** A **Transformer** is a neural architecture built from stacked **layers**, each containing **self-attention** and **feed-forward** sublayers, processing **token embeddings** in parallel during training.
- **In Simple Words:** Every word (token) can “look at” other tokens in the sentence and decide what to focus on before updating its meaning.
- **Real-Life Example:** In a noisy classroom, you listen to the teacher, the fan, and a friend—but you **attend** most to the teacher when answering a question. Attention scores are that focus mechanism in maths form.

You are **not** deriving equations today. Remember the **assembly line**:

```
Token IDs → Embedding vectors → [Attention + Feed-forward] × N layers → Logits → Softmax → next token choice
```

![Stack of identical Transformer blocks: each block refines every token using attention then a small MLP](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session38/session38-04-transformer-stack.png?v=20261019)

### Key components (names only)

| Component | Role in plain language |
| --- | --- |
| **Embedding layer** | Turns each token ID into a vector (a list of numbers capturing meaning hints) |
| **Self-attention** | Lets each position gather information from other positions in the same sequence |
| **Multi-head attention** | Several attention patterns in parallel (syntax, nearby words, long links) |
| **Feed-forward sublayer** | Small per-token computation after attention mixes information |
| **Layer normalization & residuals** | Stabilise deep stacks so training can go to many layers |
| **Output head / LM head** | Maps final vectors to scores over the whole vocabulary (**logits**) |

**Decoder-only vs encoder-decoder (awareness):**

- **GPT-style chat models** are mostly **decoder-only**—great at generating the next token left-to-right.
- **Encoder-decoder** models (early translation systems) separate “reading” and “writing” stacks—you may meet them in translation tools, not in every chat API.

**Common doubt:** “Do I need to implement attention in FastAPI?” — No. Frameworks and vendors ship trained weights. You need the **mental map** when debugging weird outputs or context limits.

Connecting idea: Attention mixes tokens; the **output head** chooses the **next** token— that is generation.

---

## How an LLM processes input (inference)

**Inference** means using a **trained** model to produce outputs (not training it further on your laptop in this session).

**Steps when you send a prompt:**

1. **Tokenize** the prompt → integer sequence
2. **Embed** each ID → vectors
3. **Run forward pass** through all Transformer layers → final hidden state for the last position
4. **Project** to vocabulary logits → probability-like scores for every possible next token
5. **Select** one token (greedy, sampling, or beam—policy depends on settings)
6. **Append** that token to the sequence and repeat from step 2 until stop condition

Connecting idea: Step 5 is where **API knobs** (temperature, top-p, top-k, max tokens) change the answer without retraining the model.

---

## Generation settings — logits, temperature, top-p, top-k, and limits

After the Transformer runs, the **LM head** outputs **logits**—raw scores for every token in the vocabulary.

- **Official Definition:** **Logits** are unnormalised scores; **softmax** turns them into probabilities that sum to 1 across the vocabulary.
- **In Simple Words:** The model ranks every possible next “puzzle piece”; softmax converts ranks into chances on a weighted die.
- **Real-Life Example:** Ten students raise hands to answer; logits are hand heights; softmax converts them into “who gets picked” percentages.

**Greedy decoding**

- **Official Definition:** Always pick the **highest-probability** next token (argmax).
- **In Simple Words:** Always choose the safest, most obvious next word.
- **Real-Life Example:** Exam answer key with one officially correct option—you always mark **A** if A is listed first every time.
- **When to use:** Factual summaries, code skeletons, JSON-like output when you want stability (often with **temperature 0**).

**Sampling**

- **Official Definition:** Draw the next token **randomly** using the probability distribution instead of always taking the top score.
- **In Simple Words:** Roll a die weighted by the model’s confidence.
- **Real-Life Example:** A quiz club picks the next speaker by lottery tickets—strong students have more tickets, but others can still win.

### Temperature

- **Official Definition:** **Temperature** scales logits before softmax: lower values sharpen the distribution (more deterministic); higher values flatten it (more random).
- **In Simple Words:** A **focus dial**—turn it down for predictable answers; turn it up for variety and creative wording.
- **Real-Life Example:** Low temperature = railway announcement (same script daily). High temperature = antakshari where many rhymes are acceptable.

**Same question, different temperature** (run this in the Gemini lab below):

- **Question:** `What is the color of the sky?`
- **temperature 0.0** (typical style): *“The sky is blue.”* — short, factual, same idea every run.
- **temperature 0.9** (typical style): *“The sky is a peaceful blue, like a calm sheet over the city.”* — still about blue, but more poetic words and variation each run.

| Temperature (typical) | Behaviour | Good for |
| --- | --- | --- |
| **0.0 – 0.3** | Stable, repetitive, “safe” wording | Definitions, API docs, debugging hints |
| **0.4 – 0.8** | Balanced chat | Explanations, email drafts |
| **0.9 – 1.2+** | Surprising phrasing, more risk of drift | Story ideas, brainstorming (verify facts yourself) |

**Common mistake:** Using high temperature when you need exact field names like `hostel_name`—the model may invent plausible-but-wrong keys (e.g. `hostelName` in camelCase).

### Top-k

- **Official Definition:** **Top-k sampling** keeps only the **k** highest-scoring tokens, renormalises their probabilities, then samples from that shortened list.
- **In Simple Words:** “Only the **k** best candidates may win the lottery.”
- **Real-Life Example:** Shortlist three job applicants, then pick one randomly with weights—never hire from the whole city in one draw.

- **Typical values:** **40** is common in APIs (including Gemini defaults). Very small **k** → dull text; very large **k** → almost full vocabulary randomness.

### Top-p (nucleus sampling)

- **Official Definition:** **Top-p** (nucleus) keeps the **smallest** set of tokens whose cumulative probability ≥ **p**, then samples inside that set.
- **In Simple Words:** Keep adding top candidates until their combined chance reaches **p** (e.g. 0.95), then roll the die only within that group.
- **Real-Life Example:** Pack a tiffin until it is 95% full—only items that fit in that box are eligible; the box size changes with each step.

| Knob | What it limits |
| --- | --- |
| **top-k** | **Count** of candidates (fixed number) |
| **top-p** | **Probability mass** (flexible number of candidates) |

APIs often use **both** together; the effective pool is the stricter of the two rules after vendor-specific merging.

### Max output tokens and context window

- **Max output tokens** (Gemini: **`maxOutputTokens`**): Hard cap on **new** text the model may **generate** in one call—like `max_tokens` in other APIs.
- **Context window**: Cap on **input + output together** (prompt, chat history, pasted code, and the answer). Exceeding it causes errors or truncated input.

**Finish reason (read the response):**

| Value (typical) | Meaning |
| --- | --- |
| **STOP** | Model chose to end naturally |
| **MAX_TOKENS** | Hit your output cap—answer may be cut mid-sentence |
| **SAFETY** / blocked | Policy filter; change prompt or check API docs |

**Usage metadata:** Many responses include **prompt** and **candidate** token counts—compare with your local `tiktoken` estimates.

**Context window (reminder):** All tokens from instructions, your message, prior turns (if resent), **and** the model’s answer share one budget. Long pasted `main.py` consumes the same space as your question.

**Common mistake:** Pasting entire error logs and three files, then wondering why the tail was “forgotten”—you exceeded practical context, not because the model “ignored” you.

![Autoregressive loop: append one predicted token, re-run the network, append again until STOP](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitp-sdai-2606/module4/session38/session38-05-autoregressive-loop.png?v=20261019)

---

## How an LLM generates text — autoregressive decoding

- **Official Definition:** **Autoregressive generation** produces a sequence one token at a time, each step conditioned on all previously generated tokens.
- **In Simple Words:** The model writes one piece, reads everything so far including that piece, then writes the next.
- **Real-Life Example:** Completing a shloka line by line—you only know the next line after you speak the current one aloud in the assembly.

**Stop conditions:**

- Model emits an **end-of-sequence** token
- App hits **max tokens**
- App detects a closing pattern (e.g., a complete JSON object when the product enforces format)

**Why it matters for you:**

- Partial code may **look** done but stop mid-function if `max_tokens` is low—same as your lab when Claude stopped early.
- Regeneration with the same prompt can differ when temperature > 0—always **run and test** like you did with Uvicorn.

### Full code — toy autoregressive loop (no GPU, no API)

This does **not** run a real LLM. It teaches the **control flow** real servers use.

```python
# toy_autoregressive.py — educational loop with a fake tiny vocabulary

import random  # Only to show non-greedy choice in demos

# Fake logits: for each context ending, what token might come next
FAKE_NEXT = {
    "": ["The", "A"],  # Start of sentence
    "The": ["campus"],  # After "The"
    "The campus": ["API"],  # Building phrase
    "The campus API": ["returns"],  # Verb
    "The campus API returns": ["JSON", "students"],  # Branch
    "The campus API returns JSON": ["."],  # End punctuation
    "The campus API returns students": ["."],  # Alternate ending
    "A": ["student"],  # Other branch start
    "A student": ["has"],  # Continue
    "A student has": ["marks"],  # Domain word
    "A student has marks": ["."],  # Finish
}

STOP_PIECES = {".", "<|end|>"}  # Tokens that end generation


def pick_token(options, temperature=0.7):
    # If temperature is 0, always pick first option (greedy)
    if temperature <= 0:
        return options[0]  # Deterministic choice
    # Otherwise random choice weighted equally (toy only)
    return random.choice(options)  # Shows variability between runs


def generate(start_context="", max_steps=20, temperature=0.0):
    context = start_context.strip()  # Current text so far
    for step in range(max_steps):  # Safety cap like max_tokens
        # Look up possible next tokens; unknown context stops the demo
        choices = FAKE_NEXT.get(context)  # None if we fell off the map
        if not choices:
            print(f"Stopped: no fake rules for context={context!r}")  # Debug
            break  # Exit loop
        token = pick_token(choices, temperature=temperature)  # Choose one piece
        # Append with space unless punctuation
        if context == "":
            context = token  # First token
        elif token in STOP_PIECES:
            context = context + token  # Attach punctuation directly
        else:
            context = context + " " + token  # Normal word boundary
        print(f"step {step + 1}: added {token!r} -> {context}")  # Trace
        if token in STOP_PIECES:
            break  # End of sequence
    return context  # Final string


if __name__ == "__main__":
    print("=== Greedy path ===")  # Label
    generate(start_context="", temperature=0.0)  # Should walk one stable path
    print("\n=== With randomness ===")  # Label
    generate(start_context="", temperature=1.0)  # May branch at "JSON" vs "students"
```

**How the code works:**

- **`FAKE_NEXT`** plays the role of the **LM head**—mapping context to allowed continuations.
- The loop is identical in shape to production: **append → re-encode context → predict again**.
- **`temperature`** illustrates why two Claude answers can differ when randomness is on.
- Real models use billions of contexts, not a Python dict—this is **flow**, not **intelligence**.

### Activity — trace on paper

Pick the greedy run (`temperature=0.0`). Write the context string after each step. Circle where the model would need **attention** to choose between `"JSON"` and `"students"` in a real network.

---

## Hands-on — Gemini API with `fetch` (free tier)

Same **`fetch`** pattern as calling `campus_api`: **POST JSON**, read JSON, print to the console.

**Setup once**

1. Get a free **API key** from [Google AI Studio](https://aistudio.google.com/apikey).
2. In `llm_token_lab`, add `.env` (never commit it):

```
GEMINI_API_KEY=your_key_here
```

3. Install **`dotenv`** and run with **Node 18+**:

```bash
npm init -y  # One-time in llm_token_lab if you have no package.json
npm install dotenv  # Loads GEMINI_API_KEY from .env into process.env
```

### Full code — `gemini_ask.mjs`

Save as `llm_token_lab/gemini_ask.mjs`. Edit **`TEMPERATURE`**, save, run again.

```javascript
// gemini_ask.mjs — load key from .env, ask one question, print answer

import "dotenv/config"; // Reads GEMINI_API_KEY from .env in this folder

const TEMPERATURE = 0; // Step 1: run with 0. Step 2: change to 0.9 and run again
const QUESTION = "What is the color of the sky?"; // Same question both times

const key = process.env.GEMINI_API_KEY; // Key must not be hard-coded in source
if (!key) {
  throw new Error("Add GEMINI_API_KEY=... to llm_token_lab/.env"); // Stop if missing
}

const url =
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" +
  key; // Free-tier flash model; swap name if AI Studio shows another

const response = await fetch(url, {
  method: "POST", // HTTP POST like creating a resource
  headers: { "Content-Type": "application/json" }, // JSON request body
  body: JSON.stringify({
    contents: [{ parts: [{ text: QUESTION }] }], // Your question for Gemini
    generationConfig: { temperature: TEMPERATURE }, // Only knob you change today
  }),
});

const data = await response.json(); // Parse Google's JSON
const text = data.candidates?.[0]?.content?.parts?.[0]?.text ?? JSON.stringify(data); // Answer or error blob

console.log("temperature:", TEMPERATURE); // So you remember which run this was
console.log("question:", QUESTION); // Echo the prompt
console.log("answer:", text); // Read style difference: short vs poetic
```

**How the code works:**

- **`dotenv/config`** loads **`GEMINI_API_KEY`** from `.env`—same idea as `python-dotenv` on `campus_api`.
- Change only **`TEMPERATURE`** from **`0`** to **`0.9`**, keep the sky question, run **`node gemini_ask.mjs`** twice, and compare console output.
- Do **not** put this key in frontend `fetch`—anyone could steal it from the browser.

### Activity — sky color comparison

Run with **`TEMPERATURE = 0`**, note the answer length and tone. Run again with **`0.9`**. Write one line: which run sounded like a textbook vs a story?

---

## From tokens to the chat products you use

| Layer | What you interact with | What happens inside (today’s view) |
| --- | --- | --- |
| **App UI** | ChatGPT, Claude web, IDE plugins | Sends messages, shows streamed text |
| **API** | HTTP request with model name, messages, limits | Server schedules GPU, runs tokenizer + model |
| **Model weights** | Hidden | Transformer forward passes + sampling |
| **Your backend** | `campus_api` on Uvicorn | Unchanged—LLM does not replace SQL unless you integrate |

**Streaming:** Apps often print tokens as they arrive because generation is sequential—perceived speed improves even though total work is similar.

**Grounding reminder:** In your coding labs, **facts** about routes and columns came from **your prompt + files**, not from the model memorising your repo. Production systems add **retrieval, tools, and validators**—topics for later modules—not covered here.

Connecting idea: You now know **what** is being steered. The next lesson focuses on **how to write prompts** so steering is reliable.

---

## Limits, hallucinations, and responsible use (integrated)

- **Official Definition:** A **hallucination** is fluent, confident model text that is **not grounded** in facts, your data, or the instructions you gave.
- **In Simple Words:** The model “fills in the blank” with a guess that **sounds** right.
- **Real-Life Example:** A clerk writes “Room 204 paid fees” without opening the register— neat handwriting, wrong fact.

**Hallucination vs honest “I don’t know”**

| You ask (without sending real data) | Bad pattern (hallucination) | What a developer should do |
| --- | --- | --- |
| “How many rows are in **my** `campus.db` right now?” | “You have 42 students.” | Never trust this—run `SELECT COUNT(*)` on **your** DB |
| “Add field `gpa` to `StudentOut`—what does our app return today?” | Invents JSON with `gpa: 9.2` | Open `/docs` and read actual `StudentOut` |
| “Cite the 2024 IIT fee circular PDF page 12.” | Makes up a page number | Use real documents or search tools, not memory |

**Other terms — quick examples**

| Term | Mini example |
| --- | --- |
| **Context window** | You paste all of `main.py` + logs + chat; the model ignores the bottom error line—not malice, **token limit**. |
| **Inference** | You run `node gemini_ask.mjs` and wait for text—that call is inference, not training. |
| **Autoregressive** | Answer appears word-by-word in chat UI because each word depends on prior words. |
| **Embedding** | “hostel” and “dorm” land near each other as numbers—helps meaning, not magic SQL access. |

- **Mitigation you already practise:** Run code, hit `/docs`, compare to `StudentOut`, reject drafts that drop CORS or persistence.
- **Mitigation you will add later:** Clearer instructions, tool calls, and retrieval when you build on this foundation.

| Risk | Simple guard |
| --- | --- |
| Secret leak | Never paste `.env`, API keys, or Aadhaar into public chats |
| Wrong ORM | Execute queries against real `campus.db` |
| Over-long paste | Summarise errors; attach only the relevant route |
| False authority | Treat the model as a draft clerk, not the registrar |

---

## Hands-on — end-to-end mini checklist

Work through this single-student checklist in order:

1. Run **`explore_tiktoken.py`** on three sentences you write (include one Hinglish line).
2. Add your **`StudentOut`** JSON fragment; record **token count**.
3. Run **`explore_hf_tokenizer.py`** on the same JSON line; note count difference vs tiktoken.
4. Run **`toy_autoregressive.py`** greedy and random modes; compare paths.
5. Add **`.env`**, run **`node gemini_ask.mjs`** at **`TEMPERATURE = 0`**, then **`0.9`**, same sky question.
6. Draw the pipeline: **Text → Tokens → Transformer → Logits → temperature → Next token → Text**.

---

## Common doubts — quick answers

| Doubt | Short answer |
| --- | --- |
| Do I train Transformers in this course track? | You **use** models; training-at-scale is out of scope for this intro. |
| Is attention the same as “prompt focus”? | Related metaphor only; prompt instructions are text the model reads, not a manual attention dial. |
| Why both tiktoken and GPT-2 tokenizer? | To prove tokenization is **model-specific**. |
| Does bigger always mean better? | Often stronger, but slower and costlier; apps pick trade-offs. |
| Can an LLM replace FastAPI? | No—it generates text; your server executes Python and SQL. |
| Why did sky answers differ at 0 vs 0.9? | Low temp sticks to plain facts; high temp adds creative wording. |
| Why keep the API key out of `fetch` in the browser? | **Secret exposure**—call Gemini from Node or your backend. |

---

## Why software developers need to know LLMs

- **You already ship software that talks to models** — GenAI labs used chat tools; today you saw the same thing as an HTTP **`fetch`** call with **`temperature`**.
- **Bugs change shape** — Wrong output is not always a traceback; it can be a **hallucinated** field name or route that looks fine in code review.
- **Cost and limits are real** — Long prompts eat **context window** and API quota; token counts matter when you paste whole files.
- **You choose where AI lives** — Frontend-only, backend-only, or both; each place has different security and data rules.
- **You stay the owner of truth** — **`campus.db`**, `/docs`, and tests beat a confident paragraph from a model.

Connecting idea: Knowing LLMs is not becoming an ML researcher—it is knowing what the **component** does so you integrate it like any external API (timeouts, errors, validation).

---

## Integrating AI in real software (frontend, backend, and both)

| Pattern | Where it runs | Real-life style example | Developer note |
| --- | --- | --- | --- |
| **Chat in the browser** | Frontend UI → **your backend** → LLM API | Student portal “Ask help” box | API key stays on server; browser never holds **`GEMINI_API_KEY`** |
| **Copilot in admin panel** | Backend route calls LLM after reading DB | “Summarise hostel occupancy” using **`/hostels/summary`** numbers you pass in the prompt | Send **facts from SQL**, not “guess my DB” |
| **Inline assist on a form** | Frontend calls **your** FastAPI route | Address auto-suggest or “explain this error” on failed POST | Validate LLM JSON before UPDATE |
| **Batch / background** | Worker or FastAPI **background task** | Nightly plain-language email from log summaries | Retry on **429** rate limits |
| **Dev-only (what you did today)** | Local Node/Python script | `gemini_ask.mjs` on laptop | Fine for learning; not how production serves users |

**Frontend (FE) integration — typical flow**

- User types in React/vanilla page → **`fetch("/api/help")`** to **your** origin → your FastAPI builds prompt → Gemini/OpenAI → your API returns text to UI.
- **Why not FE → Gemini directly?** Keys leak in DevTools; **CORS** blocks or exposes abuse.

**Backend (BE) integration — typical flow**

- New route e.g. **`POST /ai/explain-error`** accepts `{ "trace": "..." }` → server trims trace → calls LLM with **`temperature: 0.2`** → returns `{ "hint": "..." }`.
- Same **`Depends(get_db)`** world: LLM does not replace SQL; it **explains** or **drafts** while DB stays source of truth.

**Full-stack example tied to `campus_api`**

- User filters **`GET /students?city=Pune`** on the UI → clicks “Explain this list in simple Hindi” → frontend sends **already-loaded JSON** (not the whole DB) to your backend → backend calls LLM → UI shows explanation. Facts came from **your API response**; LLM only rephrased.

---

## Key Takeaways

- A **Large Language Model** is a Transformer-based **next-token predictor**; chat apps wrap it with instructions and UI.
- **Temperature** changes **style**, not facts—sky is still blue at 0.9, but words get more creative; use **low** temp for schema-like output.
- **Hallucination** means confident wrong text—always verify against **DB**, **tests**, and **`/docs`**.
- **`gemini_ask.mjs`** shows the real integration primitive: **`.env` key + fetch + JSON + console output**.
- **Production AI** almost always sits **behind your backend** (or dev scripts), with keys secret and data you choose to send.
- Next you will learn **prompt structure and techniques** to steer answers reliably.

## Important Commands, Libraries, Terminologies used

| Name | Meaning in this lesson |
| --- | --- |
| **LLM** | Large Language Model; predicts continuations of text |
| **Token** | Subword unit after tokenization |
| **Token ID** | Integer label for a token in a vocabulary |
| **Vocabulary** | Fixed list of tokens a model knows |
| **Transformer** | Architecture with attention + feed-forward layers |
| **Self-attention** | Mechanism to relate each token to others in the sequence |
| **Embedding** | Vector representation of a token ID |
| **Logits** | Scores over vocabulary before choosing the next token |
| **Autoregressive** | Generate one token at a time, conditioning on prior tokens |
| **Context window** | Max tokens processed together in one request |
| **Temperature** | Scales logits before softmax; low = stable, high = varied |
| **Top-k** | Sample only from the k highest-scoring next tokens |
| **Top-p (nucleus)** | Sample from smallest set whose cumulative probability ≥ p |
| **Softmax** | Turns logits into probabilities that sum to 1 |
| **Greedy decoding** | Always pick the highest-probability next token |
| **Sampling** | Random next token weighted by probabilities |
| **maxOutputTokens** | Gemini cap on generated tokens in one response |
| **finishReason** | Why generation stopped (e.g. STOP, MAX_TOKENS) |
| **usageMetadata** | Provider token counts in Gemini JSON responses |
| **generationConfig** | Gemini JSON block for temperature, top-p, top-k, limits |
| **generateContent** | Gemini REST method you call with POST + fetch |
| **GEMINI_API_KEY** | Secret from Google AI Studio; keep in `.env`, not git |
| **dotenv** | Loads `.env` into `process.env` for local Node scripts |
| **gemini_ask.mjs** | Minimal lab: one question, print answer, change temperature |
| **Inference** | Running a trained model to obtain outputs |
| **Pre-training** | Initial learning pass on broad text |
| **tiktoken** | Python library for OpenAI-style encodings |
| **`cl100k_base`** | Example encoding table used in demos |
| **AutoTokenizer** | Hugging Face helper to load a model’s tokenizer |
| **BPE** | Byte-pair encoding; common subword strategy |
| **Decoder-only** | GPT-style stack focused on generation |
| **EOS token** | Special token marking end of generation |
| **Hallucination** | Plausible but incorrect model output |
