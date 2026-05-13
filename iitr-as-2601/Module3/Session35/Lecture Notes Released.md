# GenAI Concepts for Beginners

## What We Covered Before and Where We Are Heading

In our last session, we wrapped up the classical Machine Learning journey. We compared different ML models side by side using metric tables, understood how to save and load a trained model using `joblib`, and built a checklist for choosing the right model for the right job. We even deployed a saved model into a simple Gradio UI — which was the closest we got to putting ML into the real world.

That workshop was the final chapter of the classical ML story. Every model we built — for example linear and logistic regression, decision trees, and random forests — had one thing in common: **they all needed structured, tabular data**. Rows, columns, fixed features, and labelled outputs.

Today, we enter a completely new world. This session is the first step in **Module 3: Agentic Systems**, and we start by understanding the technology that makes modern AI agents possible — **Large Language Models (LLMs)**. By the end of this session, you will know the vocabulary of the LLM world and understand exactly why the models from Module 2 cannot do what LLMs do.

**In this session, you will learn:**
- Why classical ML fails when the input is human language
- What neural networks are — intuitively, without math
- How LLMs evolved and what makes them different from everything before
- What tokens, context windows, temperature, and hallucinations mean in practice
- How to reason about token counts and how temperature changes outputs (including what we tried on **Groq** with the course **LLaMA** model)

---

## Where Classical ML Hits a Wall

Let us start by looking at everything we built in Module 2 and asking one honest question: **can any of those models write an email?**

A logistic regression model predicts a category — yes or no, pass or fail — based on fixed numerical columns. A decision tree splits data by asking questions like "Is age > 30?" or "Is income > 50,000?" Neither of them has any idea what a sentence is, what a word means, or how to produce new text.

**The core limitation of classical ML on language is this: language does not fit into a table.**

![Structured tabular ML grids versus free-form natural language — the same limitation that blocks email generation or chat from classical models](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-01-tabular-vs-language.png)

### The Feature Engineering Problem

To train a classical ML model, you need **features** — columns with numbers. For a house price model, features are area, number of rooms, location. But what are the features for a sentence like *"Please reschedule my meeting to tomorrow"*?

- Is the word "meeting" a feature? What number does it get?
- What about the word "tomorrow" — that changes every day!
- And what if someone writes *"Can we push the meeting to the next day?"* — same meaning, completely different words.

There is no clean way to turn the meaning of a sentence into a fixed set of numeric columns. This is called the **feature engineering bottleneck** — classical ML breaks down because it cannot handle variable-length, meaning-rich text.

### The Word Ambiguity Problem

Here is a simple example that shows the depth of the problem.

> *"I went to the bank."*

![The same surface word splitting into rival meanings until surrounding context resolves it — what fixed feature columns alone cannot capture](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-02-word-ambiguity-bank.png)

Does "bank" mean the edge of a river or a financial institution? A human knows from context. But a classical ML model that sees the word "bank" as a feature column has **no idea** — it sees the same value regardless of meaning.

This is called **word ambiguity**, and it is everywhere in human language. Words like "bat", "light", "spring", "rock" all carry multiple meanings depending on context. Classical models cannot resolve this because they have no memory of surrounding words.

Older systems sometimes used simple word counts or keyword rules; those ideas break quickly when people rephrase the same intent in new words. The line we drew in class is simpler: **meaning lives in context**, and that is what we need models to capture.

---

## Neural Networks — The Bridge to LLMs

Now that we understand why classical ML cannot handle language, let us understand the type of model that can. The key technology powering LLMs is the **neural network** — and the good news is, you already know part of how it works.

### From Linear Regression to Neural Networks

Cast your mind back to **linear regression** from earlier in the course. It takes input features, multiplies each by a weight, adds a bias, and fits a relationship between inputs and output. That is essentially **one layer of decision-making**.

A **neural network** is what happens when you stack many such computational units on top of each other. Each layer takes the output of the previous layer as its input, transforms it, and passes it to the next. Instead of one set of weights, the network has **millions of sets of weights** — each layer learning a progressively more abstract version of the input.

> **Official Definition:** A **Neural Network** is a computational model made of layers of connected nodes (neurons) that learn patterns from data by adjusting the strength (weights) of connections through training.
>
> **In Simple Words:** Think of it as a team of decision-makers arranged in a line. The first team looks at raw data and passes a simplified version to the next team, who looks for bigger patterns, and so on — until the last team makes the final prediction.
>
> **Real-Life Example:** Imagine recognising a face in a photo. Your eyes first notice edges and colours (layer 1), then shapes like eyes and nose (layer 2), then the overall face structure (layer 3), and finally you recognise the person (output). A neural network does exactly this, but with numbers.

We also touched **image classification** only as motivation: pixels go in, early layers pick up edges and textures, deeper layers combine them into parts, and the network finally predicts a label. You do not need to master vision models for this module — the point is the same **input → hidden layers → output** story that LLMs reuse on text turned into numbers.

### The Architecture — Input, Hidden Layers, Output

Every neural network has three types of layers:

- **Input Layer:** Where the raw data enters. For an image, this is the pixel values. For text, this is the numerical representation of words (more on this soon).
- **Hidden Layers:** The middle layers where the network learns patterns. The more hidden layers, the "deeper" the network — which is where the term **deep learning** comes from.
- **Output Layer:** The final prediction. For a classification model, this might be a probability score. For a language model, this is the probability of what the next word should be.

**What does "deep" mean?** It simply means more hidden layers. A shallow network might have 1–2 hidden layers. A deep network used in LLMs has dozens or hundreds of layers — each one building a richer understanding of the input.

![Input, hidden, and output layers stacked — many weighted transformations in sequence, the same deep stack idea behind modern language models](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-03-neural-network-layers.png)

Every connection between neurons has a **weight (w)** and each neuron has a **bias (b)** — these are the learnable parameters that the network adjusts to improve its predictions. A single neural network used in LLMs can have **billions** of these parameters. Unlike tabular ML which needs pre-defined numeric columns, neural networks can process **unstructured data** — text, images, audio — by converting it into numbers first, then learning from those numbers. This is the unlock that makes LLMs possible.

---

## The Rise of Large Language Models

Neural networks gave us the ability to learn from unstructured data. But the journey from "neural networks exist" to "ChatGPT shocked the world" took several decades. Let us walk through that story.

### Step 1 — Word2Vec: Words Become Numbers (2013)

The first problem to solve was: **how do you convert words into numbers in a way that captures meaning?**

Researchers at Google created **Word2Vec**, a technique that maps every word to a vector of numbers (a list of numbers). The remarkable thing was that the math on these vectors preserved meaning:

> **"king" − "man" + "woman" ≈ "queen"**

This showed that if you represent words as numbers correctly, relationships between words are preserved mathematically. Words with similar meanings end up with similar vectors — "happy" and "joyful" are close together; "happy" and "car" are far apart.

Internally, a large model still learns **word embeddings** — lists of numbers that summarise how a word behaves next to other words in training text. You can combine word-level vectors (for example by averaging) to get a rough **sentence embedding** or **document embedding**: one vector standing in for a whole line or paragraph. That is the same "text → numbers" bridge we need before any neural stack can run.

### Step 2 — RNNs: Reading Text One Word at a Time (2014–2016)

With words as numbers, the next step was building a model that could **process a sequence of words** — a sentence or paragraph. Researchers used **Recurrent Neural Networks (RNNs)**, which read text word by word, maintaining a "memory" of what they had read so far.

But RNNs had a critical weakness: **they forgot early context in long sequences**. By the time an RNN read the 50th word of a paragraph, it had mostly forgotten what the first 10 words said. This made them poor at understanding long documents or maintaining coherent conversations.

### Step 3 — The Transformer: The Architecture That Changed Everything (2017)

In 2017, a team at Google published a paper titled *"Attention is All You Need"* and introduced the **Transformer architecture**. This solved the RNN problem in a brilliant way: instead of reading one word at a time, a Transformer **processes all words simultaneously** and uses an **attention mechanism** to decide which words are most relevant to each other.

> **Official Definition:** The **Transformer** is a neural network architecture that uses an attention mechanism to process all words in a sequence simultaneously and model relationships between any two words regardless of their distance.
>
> **In Simple Words:** Instead of reading a sentence word by word like an RNN, a Transformer reads all words at once and asks: *"Which words should I pay attention to when understanding this particular word?"* For the word "it" in *"The trophy didn't fit in the bag because it was too large"*, attention figures out that "it" refers to "trophy", not "bag".
>
> **Real-Life Example:** Imagine reading an entire book page in one glance rather than one letter at a time, and your brain instantly knowing which sentences are connected to each other. That is what the Transformer does with text.

![Every token considered together with weighted attention links — how Transformers relate distant words without reading strictly left-to-right](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-04-transformer-attention.png)

### Step 4 — GPT and Pre-training: Learning From the Entire Internet

With the Transformer architecture in place, OpenAI built **GPT (Generative Pre-trained Transformer)**. The key idea in the name is **pre-training**: train the model on an enormous amount of text — books, Wikipedia, websites, code, news articles — using a simple objective: *predict the next word*. No labelling needed for that stage. The model learns the statistical patterns of human language from **internet-scale** data.

This is a different mindset from classical ML. A random forest for predicting loan defaults knows nothing about text. A generative transformer trained on huge text corpora learns grammar, surface facts, and many writing patterns from one massive training run.

![From Word2Vec and RNNs to the 2017 Transformer, GPT-style pre-training, and the ChatGPT moment — the stack of ideas that produced modern LLMs](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-05-llm-evolution-timeline.png)

### Step 5 — ChatGPT: The Cultural Moment (2022)

GPT-1 → GPT-2 → GPT-3 → **ChatGPT** (November 2022). When OpenAI released ChatGPT, it reached 1 million users in 5 days and 100 million users in 2 months — faster than any technology in history. For the first time, anyone could type a question in plain English and get a thoughtful, fluent, useful response.

This is why we are here. The technology powering ChatGPT — and every AI agent we will build in this module — is the LLM. And the rest of this session is about understanding exactly how it works under the hood.

---

## Tokens — The Currency of LLMs

Now that we understand what LLMs are, let us understand how they actually process text. The answer is: **they do not process words — they process tokens**.

> **Official Definition:** A **token** is the basic unit of text that an LLM works with. A token can be a complete word, a part of a word, a punctuation mark, a space, or a number.
>
> **In Simple Words:** Think of tokens as the Lego bricks of text. Just like Lego breaks any structure into standard-sized bricks, a tokenizer breaks any sentence into standard-sized chunks that the model can process.
>
> **Real-Life Example:** The word "unhappiness" might be split into three tokens: ["un", "happi", "ness"]. The word "cat" is one token. The sentence "I am happy!" is four tokens: ["I", " am", " happy", "!"].

![Subword pieces mapped to IDs — variable-length text turned into a fixed-vocabulary stream the model can multiply and add over](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-06-tokens-lego-blocks.png)

### Why Tokenisation Exists

Computers fundamentally work with numbers. To feed text into a neural network, every piece of text must be converted into a number. A **tokenizer** does this in two steps:

1. Split the text into tokens (chunks of text).
2. Map each token to a unique number from a fixed **vocabulary** (a dictionary of all known tokens).

The LLM then processes these numbers — not the raw text. After generating its response (also as numbers), the tokenizer converts them back into readable text.

### Subword Tokenisation — Why Not Just Use Whole Words?

You might wonder: why not just map each whole word to a number? The problem is that there are millions of possible words (including typos, names, technical terms, foreign words), and a vocabulary of millions would be too large to handle efficiently.

The solution is **subword tokenisation** — breaking words into common pieces:
- Common words like "the", "is", "a" stay as single tokens.
- Rare or long words get split into meaningful pieces: "Transformer" → ["Transform", "er"].
- This keeps the vocabulary to a manageable size (~50,000–100,000 tokens) while covering almost any text.

### Activity 1 — Count Tokens (the way we did in class)

In the live session we counted tokens by inspection: split the sentence into the pieces the model would treat as one step, and tally them. Try the same on paper or in a notebook:

1. Write a short English sentence and mark each token boundary (words, punctuation, and subword splits for long or rare words).
2. Compare a short sentence with a long technical term (for example "Transformer" vs "cat") and notice how the token count changes.

**Optional — inspect tokens with `tiktoken`:** If you want the exact OpenAI tokenizer on your machine, you can run the snippet below locally. It was shared as optional practice; the core idea is the counting, not the library name.

```python
# Install once: pip install tiktoken

import tiktoken  # Load the tokenizer helpers from OpenAI's tiktoken package

encoder = tiktoken.encoding_for_model("gpt-4")  # Pick the encoding that matches GPT-4 style models
sentence = "The quick brown fox jumps over the lazy dog."  # Any English sentence you want to inspect
token_ids = encoder.encode(sentence)  # Turn the whole string into a list of integer token IDs
tokens_as_text = [encoder.decode([t]) for t in token_ids]  # Decode each ID alone to see the text piece

print("Token IDs:", token_ids)  # Show the numeric stream the model actually sees
print("Number of tokens:", len(token_ids))  # Token count — useful for cost and context math
print("Tokens:", tokens_as_text)  # Human-readable pieces after splitting
```

**How the code works:**
- `encoding_for_model("gpt-4")` loads the tokenizer paired with that model family.
- `encode` turns text into token IDs; `decode` turns one ID back into the text piece it represents.

**Try these comparisons yourself:**
- A simple English sentence vs. a sentence with a rare technical acronym.
- The informal rule we used in class: **about 1 token for every 0.75 English words** on average (so ~100 tokens ≈ ~75 words).

### Prompt Tokens vs Completion Tokens

Providers bill and cap usage in two buckets:

- **Prompt tokens** — everything you send in (your instructions and context). In UIs this is often just called the **input** or **prompt**.
- **Completion tokens** — everything the model generates back. In UIs this is the **output** or **completion**.

If you do not limit completions, cost and latency can jump even on free tiers, because longer answers consume more completion tokens.

### Why Token Count Matters for You

Tokens are not just a technical detail — they have direct practical consequences:

- **API Cost:** Providers charge per token (input and output). Longer prompts and longer answers cost more.
- **Context Limits:** Every LLM has a maximum number of tokens it can process in one call. If your text exceeds this limit, the model cannot see all of it.

---

## Context Windows — The Model's Working Memory

Now that you know what tokens are, we can understand one of the most important LLM concepts: the **context window**.

> **Official Definition:** The **context window** is the maximum number of tokens an LLM can process in a single call — both the input you send and the output it generates together must fit within this limit.
>
> **In Simple Words:** The context window is how much text the model can consider at once. Anything outside that span is invisible on that API call.
>
> **Real-Life Example:** Imagine you can only read the last 10 pages of a book before answering a question about it. If the answer is on page 3 of a 200-page book, you will not find it — because you can only see pages 191–200. That is exactly what happens when content exceeds the context window.

![A long document with only a sliding bright window visible — tokens outside the frame are invisible to the model on that API call](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-07-context-window-viewport.png)

### What Happens When the Context is Full?

When a conversation or document exceeds the context window limit, the model simply **cannot see the earlier parts**. In a long chat, it will forget what was said at the beginning. When summarising a very long document, it may miss important details from early sections.

This is not a bug — it is a fundamental architectural constraint. The model does not have unlimited memory. It only works with what fits in its current context window.

### Context Window Sizes Across Models

| Model | Context Window | Approximate Pages |
|---|---|---|
| GPT-3.5 (early) | 4,096 tokens | ~3 pages |
| GPT-4 | 128,000 tokens | ~100 pages |
| Gemini 1.5 Pro | 1,000,000 tokens | ~750 pages |

**Course setup:** For hands-on work we used **Groq** (a free tier with limits) with Meta's **LLaMA** family. The configuration shown in class used on the order of **12,000 tokens** of context for the chosen model — enough for exercises while still forcing you to think about limits.

### Activity 2 — Estimating Context Window Usage

Let us make this concrete with a quick estimation exercise.

**Scenario:** You want to use an LLM to summarise a textbook chapter.
- Average chapter: ~5,000 words
- Rule of thumb: 1 token ≈ 0.75 words → 5,000 words ÷ 0.75 ≈ **6,667 tokens**
- Your summary prompt adds another 50 tokens.
- **Total: ~6,717 tokens**

A model with a 4,096-token context window **cannot handle this** — the chapter alone exceeds its limit. A model with a 128k context window handles it easily.

**In-class exercise — estimate these:**
1. How many tokens does a typical WhatsApp conversation of 200 messages take?
2. A 50-page PDF report — does it fit in GPT-4's context window?
3. An entire Harry Potter book (~500,000 words) — which model could handle it in one call?

### Why Context Windows Matter for Agentic Systems

When you build AI agents in the upcoming sessions, the agent will carry conversation history, tool outputs, and instructions all within the same context window. Understanding context limits helps you design agents that do not drop critical instructions or run out of space mid-task. We will later learn **RAG (Retrieval-Augmented Generation)** — a technique that allows agents to work with information that does not fit in the context window.

---

## Probabilistic Text Generation — How LLMs Actually Write

This is the most important conceptual shift of the entire session. An LLM does not "look up" a paragraph it memorised word for word. **It generates text step by step.**

> **Official Definition:** **Probabilistic text generation** is the process by which an LLM generates output one token at a time, each time predicting the most likely next token given all the tokens that came before it.
>
> **In Simple Words:** The model proposes the next token, then the next, conditioned on everything so far — like rolling a loaded die where the weights depend on the story so far.
>
> **Link to what you already know:** In classification we sometimes looked at **probabilities** (for example `predict_proba` in scikit-learn). Language models extend that idea: at each step they assign scores across many possible next tokens and sample or pick from that distribution.

### Activity 3 — The Sentence Completion Game

Before we look at how LLMs do this, let us do it ourselves.

**Instructions:** Complete each sentence with the first word that comes to mind. Notice that some completions feel much more natural than others.

1. "The Eiffel Tower is located in ___"
2. "To make tea, first boil ___"
3. "She opened the door and saw a ___"
4. "The capital of India is ___"
5. "Once upon a ___"

**Discussion:** For sentence 1 and 4, almost everyone writes the same word — these have very high **probability** for one specific answer. For sentence 3, there are many equally plausible completions — probability is spread across many options. An LLM works the same way: for factual questions, one answer often dominates; for creative prompts, many answers are possible.

### Why the Same Prompt Gives Different Answers

Because the model is **sampling from a probability distribution**, not following a fixed lookup table, the same prompt can produce different outputs each time you run it. The model calculates the probability of every possible next token and then **randomly samples** from that distribution. Most of the time a likely token is chosen, but occasionally a less likely token gets selected — which is why responses vary.

---

## Temperature — The Creativity Dial

The randomness of the generation process can be controlled with a parameter called **temperature**. This is one of the most useful settings when building with LLMs.

> **Official Definition:** **Temperature** is a parameter (typically between 0 and 2 on many APIs) that controls how much randomness is applied when sampling the next token. Low temperature makes outputs more predictable; high temperature makes them more varied.
>
> **In Simple Words:** Temperature is like a "boldness dial." Near zero, the model keeps choosing the safest next tokens. Higher values spread probability mass over more surprising continuations — sometimes creative, sometimes messy.
>
> **Real-Life Example:** Think of two people giving advice. One always gives the textbook answer (low temperature). The other gives fresh, creative, unexpected ideas — sometimes brilliant, sometimes off-the-wall (high temperature). You choose based on what you need.

![Low temperature keeps next-token choices tight and repeatable; higher temperature spreads probability over more daring continuations — the same prompt, different creative risk](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-08-temperature-sampling.png)

### What we did in class — Groq and the temperature slider

Many frontier models are paid products. In class we used **Groq**, a hosted playground where several open models (including **LLaMA**) are available on a free tier with sensible limits. There you can:

- Type a **prompt** and watch the **completion** come back.
- Move the **temperature** slider from 0 toward 2 and rerun the same prompt to see variability change.
- See why **prompt tokens** and **completion tokens** both matter for cost and speed.

**Important:** The temperature idea is the same across providers (OpenAI, Google, Anthropic, Groq, and others). Only the UI and parameter names differ slightly.

---

**Option A — Using OpenAI (GPT models)**

```python
# Install the OpenAI library: pip install openai  # Run this once before importing

from openai import OpenAI  # Import the OpenAI client class

client = OpenAI(api_key="your-openai-api-key-here")  # Replace placeholder with your real API key

prompt = "Write a one-sentence description of the sky."  # Same user instruction for both temperature runs

response_low = client.chat.completions.create(  # First API call: low randomness
    model="gpt-4o-mini",  # Small fast model suitable for classroom experiments
    messages=[  # Chat API expects a list of role/content objects
        {"role": "user", "content": prompt}  # Single user turn containing our prompt text
    ],
    temperature=0.1  # Keeps sampling tight so outputs stay nearly identical across runs
)

print("Low Temperature (0.1):")  # Label so you can read logs clearly
print(response_low.choices[0].message.content)  # First completion choice → assistant message text

response_high = client.chat.completions.create(  # Second API call: higher randomness
    model="gpt-4o-mini",  # Same backbone model as the low-temperature call
    messages=[  # Same chat structure as above
        {"role": "user", "content": prompt}  # Identical prompt so only temperature differs
    ],
    temperature=1.5  # Encourages more diverse next-token picks on each run
)

print("\nHigh Temperature (1.5):")  # Blank line prefix in string separates the two outputs
print(response_high.choices[0].message.content)  # Again pull assistant text from first choice
```

**How the code works:**
- `OpenAI(api_key=...)` opens a connection to OpenAI's servers using your credentials.
- `client.chat.completions.create(...)` sends your message and gets the model's reply — same as typing in ChatGPT, but through code.
- `model="gpt-4o-mini"` picks the model; you could swap this for `"gpt-4o"` or any other OpenAI model.
- `temperature=0.1` makes the output very conservative — almost the same response every time you run it.
- `temperature=1.5` introduces more randomness — run the same prompt multiple times and you will get noticeably different responses.
- `response.choices[0].message.content` digs into the response object and pulls out the actual text string.

---

**Option B — Using Google Gemini**

```python
# Install the Google GenAI library: pip install google-generativeai  # One-time dependency install

import google.generativeai as genai  # Official Python SDK for Gemini

genai.configure(api_key="your-gemini-api-key-here")  # Paste key from https://aistudio.google.com/app/apikey

prompt = "Write a one-sentence description of the sky."  # Shared string for both experiments

model_low = genai.GenerativeModel(  # Build a low-temperature model handle
    model_name="gemini-1.5-flash",  # Flash tier is quick and free-tier friendly
    generation_config=genai.GenerationConfig(  # Bundle generation hyperparameters
        temperature=0.1  # Forces near-deterministic completions for the same prompt
    )
)

response_low = model_low.generate_content(prompt)  # Blocking call until Gemini returns text

print("Low Temperature (0.1):")  # Console label for the first experiment
print(response_low.text)  # Gemini helper that unwraps the first candidate string

model_high = genai.GenerativeModel(  # Second handle with hotter sampling
    model_name="gemini-1.5-flash",  # Keep model identical to isolate temperature effects
    generation_config=genai.GenerationConfig(  # Same config object pattern as above
        temperature=1.5  # Spreads probability mass for more varied wording
    )
)

response_high = model_high.generate_content(prompt)  # Same prompt text, different randomness knob

print("\nHigh Temperature (1.5):")  # Second label so logs stay readable side by side
print(response_high.text)  # Print the high-temperature narrative output
```

**How the code works:**
- `genai.configure(api_key=...)` authenticates your session with Google's API — you only need to call this once.
- `genai.GenerativeModel(model_name=..., generation_config=...)` creates a model object with the temperature baked in; `"gemini-1.5-flash"` is fast and available on the free tier.
- `GenerationConfig(temperature=0.1)` is Google's way of passing temperature — different library, same concept.
- `model.generate_content(prompt)` sends your prompt and waits for the response.
- `response.text` is Google's shortcut to get the reply as a clean string — simpler than OpenAI's `.choices[0].message.content`.

---

**Try it yourself — compare the outputs:**
- Run the low-temperature version several times. Notice how similar the responses are each time.
- Run the high-temperature version several times. Notice how each response can differ.
- This directly demonstrates that LLMs are probabilistic, not deterministic.

### Choosing the Right Temperature

Use low values when you want stable, factual, or repeatable behaviour; use higher values when you want variety or brainstorming. Exact numbers vary by model, so treat any table as a starting point and validate on your task.

---

## Hallucinations — When LLMs Confidently Get It Wrong

We have now seen that LLMs generate text by predicting the most likely next token. This leads to a critical flaw every LLM user must understand: **hallucinations**.

> **Official Definition:** A **hallucination** in the context of LLMs is when the model generates text that is factually incorrect or fabricated — but presents it with complete confidence as if it were true.
>
> **In Simple Words:** The model is optimised to produce text that *sounds* right, not text that *is* right. It has no internal fact-checker — it just picks the most plausible next token, and plausible is not the same as true.
>
> **Real-Life Example:** A confident student who never admits uncertainty — even when they do not know the answer, they give a well-worded response that sounds authoritative. You believe them, then find out they made it all up. That is a hallucinating LLM.

![Fluent, confident wording is not a guarantee of truth — models optimise for plausible next tokens, not a verified facts database](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-09-hallucination-fluent-not-true.png)

### Why It Happens and Why It Matters

The model was trained to predict plausible next tokens — not to verify facts. It was never taught to check if what it generates is true. LLMs also have a **knowledge cutoff** — they do not know about events after their training date and may still generate a confident but wrong answer when asked about them.

A real documented example: in 2023, two US lawyers submitted a legal brief citing six completely fabricated court cases — all invented by ChatGPT. The cases did not exist. The lawyers were fined.

When you just read a hallucinated response, the worst case is believing something incorrect. But when an **AI agent** acts on hallucinated information — sending an email, booking a flight, executing a financial transaction — the consequences are real and potentially irreversible. This is why hallucinations are one of the most important safety topics in this module.

**What is next:** In class we flagged that **mitigations** (retrieval, safer prompting, human review, and how agents amplify risk) deserve a dedicated treatment. We will pick those up in a follow-on session rather than rushing them here.

---

## Key Takeaways

- **Classical ML cannot handle open-ended language** the way people speak and write because meaning is contextual and hard to squeeze into fixed numeric feature columns — that is why we need different architectures.
- **Neural networks** are the foundation of LLMs — they stack many layers of nodes (neurons), each with learnable weights (w) and biases (b), building increasingly abstract patterns from data; they can ingest unstructured inputs once those inputs are turned into numbers (embeddings).
- **LLMs work by predicting the next token** one step at a time from learned probability patterns over huge text — not by fetching a single stored paragraph like a file search.
- **Tokens, context windows, and temperature** are practical levers — they affect cost, how much text fits in one call, and how stable or creative outputs feel (we saw this concretely on **Groq** with **LLaMA** and the temperature slider).
- **Hallucinations are an inherent risk** because fluency and truth are not the same; for agents that take actions, that gap matters enormously. Mitigation patterns come next in the course.

In the next session, we will move from understanding LLMs to **using them effectively** — with Prompt Engineering, where you will learn how the way you phrase a request dramatically changes the quality of the response.

---

## Quick Reference — Important Terms

| Term | What It Means |
|---|---|
| **Neural Network** | A model made of stacked layers of nodes that learn patterns from data |
| **Deep Learning** | Neural networks with many hidden layers |
| **Pre-training** | Training a generative transformer on massive general text (for example next-word prediction) before any product-specific use |
| **Transformer** | The neural network architecture behind modern LLMs; relates all positions in a sequence using attention |
| **Attention Mechanism** | The part of a Transformer that weighs how much each position should depend on every other position |
| **LLM** | Large Language Model — a massive neural network trained to model and generate human language |
| **Token** | The basic unit of text an LLM processes; often ~0.75 English words per token as a rule of thumb |
| **Tokenisation** | Converting text into a sequence of numbered tokens the model can compute on |
| **Prompt token / Completion token** | Billable (or limited) units for what you send in vs what the model generates out |
| **Context Window** | The maximum number of tokens an LLM can process in one call |
| **Probabilistic Text Generation** | Generating text by choosing successive next tokens from learned probability patterns |
| **Temperature** | A dial on how random those next-token choices are |
| **Hallucination** | When an LLM generates confident but factually wrong or fabricated information |
| **RAG** | Retrieval-Augmented Generation — coming later; helps agents use evidence that does not fit in context |
| **Knowledge Cutoff** | The date after which an LLM has no training data and may be wrong about newer events |
| **Groq** | Hosted playground/API used in class to try open models (including LLaMA) with temperature and token controls |
| **tiktoken** | Optional OpenAI tokenizer library to inspect token IDs in Python |
| **openai** | Python library to call OpenAI models via API |
| **google-generativeai** | Python library to call Google Gemini models via API — free tier available at aistudio.google.com |
