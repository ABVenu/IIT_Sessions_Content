# GenAI Concepts for Beginners

## What We Covered Before and Where We Are Heading

In our last session, we wrapped up the entire classical Machine Learning journey. We compared different ML models side by side using metric tables, understood how to save and load a trained model using `joblib`, and built a checklist for choosing the right model for the right job. We even deployed a saved model into a simple Gradio UI — which was the closest we got to putting ML into the real world.

That workshop was the final chapter of the classical ML story. Every model we built — linear regression, logistic regression, decision trees, random forests, K-Means clustering, and time series forecasting — had one thing in common: **they all needed structured, tabular data**. Rows, columns, fixed features, and labelled outputs.

Today, we enter a completely new world. This session is the first step in **Module 3: Agentic Systems**, and we start by understanding the technology that makes modern AI agents possible — **Large Language Models (LLMs)**. By the end of this session, you will know the vocabulary of the LLM world and understand exactly why the models from Module 2 cannot do what LLMs do.

**In this session, you will learn:**
- Why classical ML fails when the input is human language
- What neural networks are — intuitively, without math
- How LLMs evolved and what makes them different from everything before
- What tokens, context windows, temperature, and hallucinations mean in practice
- How to count tokens using real code and experiment with temperature using the OpenAI API

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

### Why Bag-of-Words and Keyword Matching Failed

Before LLMs, engineers tried to work around this problem using simpler techniques:

- **Bag-of-Words:** Count how many times each word appears in a document and use those counts as features. It completely ignores word order and meaning.
- **Keyword Matching:** If the sentence contains "refund", route it to the billing team. But what if the customer says "I'd like my money back"? The keyword "refund" never appears.
- **Regex Parsers:** Write rules like "if sentence starts with 'how do I', classify as a how-to question." One unusual phrasing breaks the entire rule.

All of these approaches are **brittle** — they work for the specific sentences you wrote rules for, and fail the moment someone phrases something differently. Human language is too rich and creative for rigid rules. A fundamentally different approach was needed.

---

## Neural Networks — The Bridge to LLMs

Now that we understand why classical ML cannot handle language, let us understand the type of model that can. The key technology powering LLMs is the **neural network** — and the good news is, you already know part of how it works.

### From Logistic Regression to Neural Networks

Cast your mind back to **logistic regression** from Session 30. It takes input features, multiplies each by a weight, adds a bias, and passes the result through a sigmoid function to produce a probability. That is essentially **one layer of decision-making**.

A **neural network** is what happens when you stack many such layers on top of each other. Each layer takes the output of the previous layer as its input, transforms it, and passes it to the next. Instead of one set of weights, the network has **millions of sets of weights** — each layer learning a progressively more abstract version of the input.

> **Official Definition:** A **Neural Network** is a computational model made of layers of connected nodes (neurons) that learn patterns from data by adjusting the strength (weights) of connections through training.
>
> **In Simple Words:** Think of it as a team of decision-makers arranged in a line. The first team looks at raw data and passes a simplified version to the next team, who looks for bigger patterns, and so on — until the last team makes the final prediction.
>
> **Real-Life Example:** Imagine recognising a face in a photo. Your eyes first notice edges and colours (layer 1), then shapes like eyes and nose (layer 2), then the overall face structure (layer 3), and finally you recognise the person (output). A neural network does exactly this, but with numbers.

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

With the Transformer architecture in place, OpenAI built **GPT (Generative Pre-trained Transformer)**. The key innovation was the training strategy: **pre-training**.

- **Pre-training:** Train the model on an enormous amount of text — books, Wikipedia, websites, code, news articles — using a simple objective: *predict the next word*. No labelling needed, no specific task defined. Just learn the patterns of human language.
- **Fine-tuning:** After pre-training, adapt the model to specific tasks (answer questions, write code, translate text) with a much smaller labelled dataset.

This is the fundamental difference from classical ML. A random forest for predicting loan defaults knows nothing about text. An LLM pre-trained on the internet knows grammar, facts, reasoning patterns, and writing styles across hundreds of topics — all from one massive training run.

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

### Activity 1 — Count Tokens Live

Let us see tokenisation in action using the `tiktoken` library, which is the same tokenizer used by OpenAI's GPT models.

```python
# Install the tiktoken library (run this once in your terminal or notebook)
# pip install tiktoken

import tiktoken  # Import the tokenizer library from OpenAI

# Load the tokenizer used by GPT-4
encoder = tiktoken.encoding_for_model("gpt-4")

# The sentence we want to tokenise
sentence = "The quick brown fox jumps over the lazy dog."

# Convert the sentence into a list of token IDs (numbers)
token_ids = encoder.encode(sentence)

# Print the token IDs
print("Token IDs:", token_ids)

# Print the number of tokens
print("Number of tokens:", len(token_ids))

# Decode each token ID back into the text it represents
tokens_as_text = [encoder.decode([t]) for t in token_ids]

# Print each token individually so we can see how the sentence was split
print("Tokens:", tokens_as_text)
```

**How the code works:**
- `tiktoken.encoding_for_model("gpt-4")` loads the specific tokenizer that GPT-4 uses — different models can have different tokenizers.
- `encoder.encode(sentence)` converts the sentence into a list of numbers — one number per token.
- `encoder.decode([t])` converts a single token ID back into its text — we do this for every token to see exactly how the sentence was split.
- The output will show you that "jumps" is one token, "over" is one token, and even the full stop at the end is its own token.

**Try these sentences yourself:**
- A simple English sentence vs. a Hindi sentence written in English script — notice the token count difference.
- A technical word like "Transformer" vs. a common word like "cat".
- The rule of thumb: **1 token ≈ 0.75 English words**, or roughly **100 tokens ≈ 75 words ≈ a short paragraph**.

### Why Token Count Matters for You

Tokens are not just a technical detail — they have direct practical consequences:

- **API Cost:** OpenAI and other providers charge per token (both input tokens you send and output tokens the model generates). Longer prompts cost more.
- **Context Limits:** Every LLM has a maximum number of tokens it can process in one call. If your text exceeds this limit, the model cannot see all of it.
- **Indian Languages:** Hindi, Tamil, Telugu, and other Indian languages written in their native scripts are often tokenised less efficiently than English — the same meaning may take 2–3× more tokens. This directly affects cost when building apps for Indian users.

---

## Context Windows — The Model's Working Memory

Now that you know what tokens are, we can understand one of the most important LLM concepts: the **context window**.

> **Official Definition:** The **context window** is the maximum number of tokens an LLM can process in a single call — both the input you send and the output it generates together must fit within this limit.
>
> **In Simple Words:** The context window is the model's short-term memory. It can only "see" and think about whatever fits in this window. Anything outside the window is completely invisible to the model.
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
| Claude 3.5 | 200,000 tokens | ~150 pages |
| Gemini 1.5 Pro | 1,000,000 tokens | ~750 pages |

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

When you build AI agents in the upcoming sessions, the agent will carry conversation history, tool outputs, and instructions all within the same context window. Understanding context limits helps you design agents that do not "forget" critical instructions or run out of space mid-task. We will later learn **RAG (Retrieval-Augmented Generation)** — a technique that allows agents to work with information that does not fit in the context window.

---

## Probabilistic Text Generation — How LLMs Actually Write

This is the most important conceptual shift of the entire session. Most people assume that when you ask an LLM a question, it looks up the answer somewhere and retrieves it. **That is not what happens.**

> **Official Definition:** **Probabilistic text generation** is the process by which an LLM generates output one token at a time, each time predicting the most likely next token given all the tokens that came before it.
>
> **In Simple Words:** The LLM does not know the full answer before it starts writing. It picks the first word, then picks the most likely second word given the first word, then the most likely third word given the first two — and keeps going until the response is complete.
>
> **Real-Life Example:** Think of your phone's keyboard autocomplete. After you type "Happy birth", it suggests "day". If you accept that, it might suggest "to". This is the exact same idea — the LLM is a vastly more powerful autocomplete that has read most of the internet.

### Activity 3 — The Sentence Completion Game

Before we look at how LLMs do this, let us do it ourselves.

**Instructions:** Complete each sentence with the first word that comes to mind. Notice that some completions feel much more natural than others.

1. "The Eiffel Tower is located in ___"
2. "To make tea, first boil ___"
3. "She opened the door and saw a ___"
4. "The capital of India is ___"
5. "Once upon a ___"

**Discussion:** For sentence 1 and 4, almost everyone writes the same word — these have very high **probability** for one specific answer. For sentence 3, there are many equally plausible completions — lower probability concentrated on any one option. An LLM works the same way: for factual questions, one answer has very high probability; for creative prompts, many answers are possible.

### Why the Same Prompt Gives Different Answers

Because the model is **sampling from a probability distribution**, not doing a deterministic lookup, the same prompt can produce different outputs each time you run it. The model calculates the probability of every possible next token and then **randomly samples** from that distribution. Most of the time a likely word is chosen, but occasionally a less likely word gets selected — which is why responses vary.

This is fundamentally different from a search engine, which retrieves the exact same document for the same query every time.

| | Search Engine | LLM |
|---|---|---|
| **What it does** | Retrieves existing documents | Generates new text |
| **Same query, same result?** | Yes | Not necessarily |
| **Can it be wrong?** | Rarely (it found the document) | Yes (it generated text) |
| **Can it be creative?** | No | Yes |

---

## Temperature — The Creativity Dial

The randomness of the generation process can be controlled with a parameter called **temperature**. This is one of the most useful settings when building with LLMs.

> **Official Definition:** **Temperature** is a parameter (between 0 and 2) that controls how much randomness is applied when sampling the next token. Low temperature makes outputs more predictable; high temperature makes them more varied and creative.
>
> **In Simple Words:** Temperature is like a "boldness dial." At 0, the model always picks the safest, most predictable word. At 2, it takes risks and picks more unusual words — sometimes brilliantly creative, sometimes nonsensical.
>
> **Real-Life Example:** Think of two people giving advice. One always gives the textbook answer (low temperature). The other gives fresh, creative, unexpected ideas — sometimes brilliant, sometimes off-the-wall (high temperature). You choose who to ask based on what you need.

![Low temperature keeps next-token choices tight and repeatable; higher temperature spreads probability over more daring continuations — the same prompt, different creative risk](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/module3/session35/session35-08-temperature-sampling.png)

### Temperature in Practice

> **Important Note:** Temperature is a universal concept — it works the same way across **all major LLM providers**. You are not locked into OpenAI. You can use Google Gemini, Anthropic Claude, Mistral, Groq, or any other provider — the `temperature` parameter behaves identically. Below we show the same experiment using two different providers so you can pick whichever API key you have access to.

---

**Option A — Using OpenAI (GPT models)**

```python
# Install the OpenAI library: pip install openai

from openai import OpenAI  # Import the OpenAI client

# Initialise the client — replace with your actual OpenAI API key
client = OpenAI(api_key="your-openai-api-key-here")

# The prompt we will test at two different temperatures
prompt = "Write a one-sentence description of the sky."

# --- Low Temperature: precise and predictable ---
response_low = client.chat.completions.create(
    model="gpt-4o-mini",        # A fast, affordable OpenAI model — good for experiments
    messages=[
        {"role": "user", "content": prompt}  # The user message sent to the model
    ],
    temperature=0.1             # Very low — model will almost always pick the safest next token
)

print("Low Temperature (0.1):")
print(response_low.choices[0].message.content)  # Extract the text from the response object

# --- High Temperature: creative and varied ---
response_high = client.chat.completions.create(
    model="gpt-4o-mini",        # Same model, same prompt — only temperature changes
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=1.5             # High — model explores more unusual token choices
)

print("\nHigh Temperature (1.5):")
print(response_high.choices[0].message.content)
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
# Install the Google GenAI library: pip install google-generativeai

import google.generativeai as genai  # Import the Google Gemini client library

# Configure the client with your Gemini API key
# Get a free API key at: https://aistudio.google.com/app/apikey
genai.configure(api_key="your-gemini-api-key-here")

# The prompt we will test at two different temperatures
prompt = "Write a one-sentence description of the sky."

# --- Low Temperature: precise and predictable ---
model_low = genai.GenerativeModel(
    model_name="gemini-1.5-flash",              # A fast and free-tier-friendly Gemini model
    generation_config=genai.GenerationConfig(
        temperature=0.1                         # Low temperature — very predictable output
    )
)

response_low = model_low.generate_content(prompt)  # Send the prompt and get a response

print("Low Temperature (0.1):")
print(response_low.text)                           # .text gives you the response as a plain string

# --- High Temperature: creative and varied ---
model_high = genai.GenerativeModel(
    model_name="gemini-1.5-flash",              # Same model
    generation_config=genai.GenerationConfig(
        temperature=1.5                         # High temperature — more creative output
    )
)

response_high = model_high.generate_content(prompt)  # Same prompt, different temperature

print("\nHigh Temperature (1.5):")
print(response_high.text)
```

**How the code works:**
- `genai.configure(api_key=...)` authenticates your session with Google's API — you only need to call this once.
- `genai.GenerativeModel(model_name=..., generation_config=...)` creates a model object with the temperature baked in; `"gemini-1.5-flash"` is fast and available on the free tier.
- `GenerationConfig(temperature=0.1)` is Google's way of passing temperature — different library, same concept.
- `model.generate_content(prompt)` sends your prompt and waits for the response.
- `response.text` is Google's shortcut to get the reply as a clean string — simpler than OpenAI's `.choices[0].message.content`.

---

**Try it yourself — compare the outputs:**
- Run the low-temperature version five times. Notice how similar the responses are each time.
- Run the high-temperature version five times. Notice how each response is noticeably different.
- This directly demonstrates that LLMs are probabilistic, not deterministic.

### Choosing the Right Temperature

| Use Case | Recommended Temperature | Why |
|---|---|---|
| Factual Q&A / customer support | 0.0 – 0.3 | Consistent, accurate, predictable |
| Summarisation | 0.3 – 0.5 | Faithful to source material |
| General chat / assistant | 0.7 – 1.0 | Natural, varied, human-feeling |
| Creative writing / brainstorming | 1.0 – 1.5 | Original, unexpected ideas |
| Code generation | 0.0 – 0.2 | Correct syntax matters more than creativity |

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

When you just read a hallucinated response, the worst case is believing something incorrect. But when an **AI agent** acts on hallucinated information — sending an email, booking a flight, executing a financial transaction — the consequences are real and potentially irreversible. This is why hallucinations are the most important safety concept in this entire module.

### How to Reduce Hallucinations

- **RAG (Retrieval-Augmented Generation):** Feed verified documents into the context so the model answers from evidence, not guesswork. We will build this in a later session.
- **Constrained Prompts:** Tell the model: *"Only answer from the provided text. If you do not know, say 'I don't have enough information.'"*
- **Human-in-the-Loop:** For high-stakes decisions (medical, legal, financial), always have a human review before acting.
- **Temperature 0:** For factual tasks, use low temperature to reduce randomness.

---

## Key Takeaways

- **Classical ML cannot handle language** because language is variable-length, ambiguous, and cannot be reduced to fixed numeric feature columns — this is why a completely different architecture was needed.
- **Neural networks** are the foundation of LLMs — they stack many layers of nodes (neurons), each with learnable weights (w) and biases (b), building increasingly abstract patterns from data; crucially, they can process unstructured inputs like text, images, and audio by converting them into numbers first.
- **LLMs work by predicting the next token** one at a time — they do not retrieve answers from a database; they generate plausible-sounding text based on patterns learned during pre-training on massive amounts of internet text.
- **Tokens, context windows, and temperature** are the three most practical parameters to understand when using LLMs — they affect cost, memory, and the character of the output respectively.
- **Hallucinations are an inherent risk** because fluency and accuracy are different things — LLMs are optimised to sound right, not necessarily to be right; in agentic systems where models take real actions, this risk requires mitigation through RAG, constrained prompts, and human oversight.

In the next session, we will move from understanding LLMs to **using them effectively** — with Prompt Engineering, where you will learn how the way you phrase a request dramatically changes the quality of the response.

---

## Quick Reference — Important Terms

| Term | What It Means |
|---|---|
| **Neural Network** | A model made of stacked layers of nodes that learn patterns from data |
| **Deep Learning** | Neural networks with many hidden layers |
| **Pre-training** | Training an LLM on massive general text before adapting it to specific tasks |
| **Fine-tuning** | Adapting a pre-trained model to a specific task using a smaller labelled dataset |
| **Transformer** | The neural network architecture behind all modern LLMs; processes all words simultaneously using attention |
| **Attention Mechanism** | The part of a Transformer that weighs how much each word should "pay attention" to every other word |
| **LLM** | Large Language Model — a massive neural network trained to understand and generate human language |
| **Token** | The basic unit of text an LLM processes; ~0.75 English words on average |
| **Tokenisation** | Converting text into a sequence of numbered tokens the model can compute on |
| **Context Window** | The maximum number of tokens an LLM can process in one call |
| **Probabilistic Text Generation** | Generating text by sampling the next most likely token one at a time |
| **Temperature** | A parameter (0–2) controlling the randomness of the model's output |
| **Hallucination** | When an LLM generates confident but factually wrong or fabricated information |
| **RAG** | Retrieval-Augmented Generation — a technique to ground LLM responses in verified external documents |
| **Knowledge Cutoff** | The date after which an LLM has no training data and may hallucinate about recent events |
| **tiktoken** | OpenAI's tokenizer library used to count and inspect tokens in text |
| **openai** | Python library to call OpenAI models (GPT-4o, GPT-4o-mini, etc.) via API |
| **google-generativeai** | Python library to call Google Gemini models via API — free tier available at aistudio.google.com |
