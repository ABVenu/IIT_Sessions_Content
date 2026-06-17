# Hands On RAG


## Resources

[Deck](https://canva.link/fylv43q6ycaxzn2)

[Ideal project submission template](https://docs.google.com/document/d/1FsCSVLryWnXz4-oGrNheihl-mBzSW76D/edit?usp=sharing&ouid=109823013851316341035&rtpof=true&sd=true)



## Context: What We Covered Before & What's Coming Today

In the previous session, we built a strong foundation in **RAG (Retrieval-Augmented Generation)**. We studied the difference between a normal LLM and a RAG-based system, the six building blocks of RAG (retrieval, query, collation, top-K, top-P, storage, and tokenization), chunking strategies, how to adjust chunk size, and how to write prompts for exact and semantic word matching. We also looked at **accuracy** and **recall** when the wrong token gets picked up.

Today we move into **advanced, industry-shaping AI topics** that go beyond the standard curriculum. These are nascent technologies that will influence how AI products are built over the next few years.

In this session, you will learn:

- **Model Context Protocol (MCP)** — how LLMs connect to external apps like Zerodha, Zomato, and Microsoft 365
- **On-Device SLMs (Small Language Models)** — why the future of AI is moving from cloud LLMs to your phone and car
- **Token Optimization** — practical techniques to reduce cost across input, processing, and output
- **LLMOps** — how companies monitor, measure, and fix AI applications in production

---

## Model Context Protocol (MCP)

### Why Do We Need MCP?

Today, if you ask ChatGPT, Gemini, or Perplexity to *"order food for me on Zomato"* or *"place this investment on Zerodha"*, the LLM **cannot** do it. It will only suggest what you should do manually.

**n8n** and **Make.com** solve part of this problem — but only for big tech connectors (Gmail, Slack, WhatsApp). What about Swiggy, Hotstar, Spotify, Tally, or Angel One? There is no universal way to plug any app into any LLM.

That gap is exactly what **MCP** fills.

### What Is MCP?

**Official Definition:** **Model Context Protocol (MCP)** is an open standard launched in 2024 by **Anthropic**. It defines how LLMs connect to external tools, APIs, and applications through a common interface.

**In Simple Words:** MCP is the **USB Type-C port for all LLM models**. Just like one Type-C cable can charge your phone, connect a monitor, or transfer files — one MCP setup lets your LLM talk to many different apps.

**Real-Life Example:** Think of a universal power adapter. Earlier, every country had a different plug. MCP is that one adapter that lets your LLM "plug into" Zerodha, Zomato, Notion, Lovable, or Microsoft Teams — without building a separate integration for each one.

![MCP is the USB Type-C port for LLMs — one standard connector lets your AI assistant talk to Zerodha, Zomato, Microsoft Teams, and other apps through MCP servers](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/other-sessions/rahul-singh-23may/advanced-ai/adv-ai-01-mcp.png?v=20260617)

### How MCP Works

- An app or company publishes an **MCP server** — a small program that wraps its existing API.
- You add that server's configuration to your LLM's **developer config** (for example, in **Claude Desktop**).
- Once connected and authenticated, you can ask the LLM to perform actions on that app directly — check stock holdings, read portfolio data, or (in future) place orders.

**Important:** MCP does **not** work on the web browser version of ChatGPT, Claude, or Gemini. You need the **desktop app** (for example, Claude Desktop).

### Live Demo: Zerodha (Kite) MCP on Claude Desktop

The instructor connected **Zerodha's Kite MCP server** in Claude Desktop and demonstrated:

1. Opening Claude Desktop → **Settings** → **Developer** → **Edit Config**
2. Adding the Zerodha MCP server entry to the config file
3. Restarting Claude and granting tool permissions
4. Asking: *"Tell me the stocks that I hold"*
5. Claude called the Zerodha API endpoint, pulled real holdings data, and displayed current prices and fundamentals

This showed the real power of MCP — chatting with an LLM and getting **live data** from a financial app without leaving the chat window.

A **Zomato MCP** demo was also attempted. Authentication via OTP worked, but the server callback failed (it tried to hit `localhost`). This is a useful lesson: **not every MCP server in the marketplace is production-ready**.

### MCP Marketplace

Most major companies now publish MCP servers on their portals or marketplaces. Examples include:

- **Microsoft 365** — Teams, Outlook, To-Do, Fabric, Playwright (for testing)
- **Zerodha (Kite)** — portfolio and trading data
- **Zomato** — food ordering (evolving)
- **11 Labs, Firecrawl, Browserbase, Unity, Excel** — and many more

Setup instructions are usually very similar across providers: add an MCP server name and endpoint to your config file.

### How MCP Wraps Your Existing API

MCP does not replace your backend. It **wraps** your existing API or application and exposes it in a standard format that LLMs understand.

- If you build a capstone project, you can expose it as an MCP server so any LLM can use it.
- On **n8n**, you can also drop MCP configurations in a standard format.

### MCP Metrics to Track

When you set up or build MCP integrations, track these metrics:

| Metric | What It Measures |
|---|---|
| **Tool success rate** | How often the MCP call succeeds vs fails |
| **Latency** | How long the MCP server takes to respond |
| **Groundedness** | Is the response based on real data, or is the LLM fabricating? |
| **Permission violations** | Is someone else trying to use your connected account? |

In the live demo, Zomato had a **100% failure rate** (2 attempts, 0 success), while Zerodha worked correctly.

### Security Warning

Connecting personal accounts (Zerodha, Zomato) to an LLM is **at your own risk**. Zerodha explicitly warns: *"Interacting with Zerodha via AI is at your own risk."* Never share sensitive credentials casually. MCP is powerful but still an evolving, stateful technology.

### Activity: Explore MCP Setup

1. Install **Claude Desktop** (or another MCP-compatible desktop LLM).
2. Go to **Settings → Developer → Edit Config**.
3. Browse an **MCP marketplace** and pick one server (start with a well-known provider like Microsoft or a weather MCP).
4. Add the server entry, save, restart the app, and check if the tool appears under **Tools**.
5. Note the **success rate** and **latency** for your first 3 queries.

### MCP Server Config Example

Below is a simplified example of what an MCP config file looks like in Claude Desktop. Your actual file may already have other servers listed.

```json
{
  "mcpServers": {
    "kite-zerodha": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.kite.zerodha.com/mcp"]
    },
    "zomato": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.zomato.com/mcp"]
    },
    "weather": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-weather"]
    }
  }
}
```

**How the code works:**
- `"mcpServers"` is the root object where all MCP connections are defined.
- Each key (like `"kite-zerodha"`) is a friendly name you choose for that tool.
- `"command": "npx"` tells the system to run the server using Node's package runner.
- `"args"` lists the package or remote URL that the MCP server listens on.
- After saving this file, restart Claude Desktop — the new tools appear in the Tools panel.
- Each time you start a new session, the LLM may ask you to log in and verify again for security.

---

## On-Device SLMs (Small Language Models)

Cloud-hosted LLMs are powerful — but they come with two big problems. Understanding these problems explains why **SLMs** are the next big shift in AI.

### Why Cloud LLMs Are Not Scalable Forever

**Problem 1 — Infrastructure cost:** Running large LLMs needs massive data centres, GPUs, and compute power that a common person cannot own.

**Problem 2 — Privacy fear:** People worry about their health data, voice recordings, photos, and personal chats being sent to cloud servers. Data leaks and privacy breaches are a real concern.

**Regulatory push:** Laws like **GDPR** (Europe) and **HIPAA** (US) may limit how companies use cloud LLMs. Many companies already say: *"We will not allow cloud LLM usage inside the company — but employees can carry their own SLM on their device."*

### What Is an SLM?

**Official Definition:** A **Small Language Model (SLM)** is a compact language model designed to run **on your device** (phone, car, edge chip) rather than on a remote cloud server.

**In Simple Words:** Instead of sending your question to a server in the US and waiting for a reply, a small AI brain lives **inside your phone** and answers you locally.

**Real-Life Example:** A Tesla autopilot does not need to know poetry, history, or cooking recipes. It only needs to understand roads, signs, parking, and cruise control. That focused, smaller model is an SLM — trained for **one job**, not everything.

### Where SLMs Already Exist

| Device / Product | SLM Use Case |
|---|---|
| **Google Pixel** | On-device AI features (post Google I/O updates) |
| **Apple iPhone** | Personal, private on-device intelligence |
| **Snapchat lenses** | Real-time face and AR processing on phone |
| **Tesla / Mahindra XUV 9e** | Driving patterns, road sign detection, autopilot, self-parking |
| **Qualcomm / NVIDIA chips** | Hardware designed to run SLMs faster with less energy |

### SLM vs LLM — Key Differences

| | Cloud LLM | On-Device SLM |
|---|---|---|
| **Internet needed?** | Yes, always | No — works offline |
| **Speed** | Depends on network | Faster — no round trip to server |
| **Privacy** | Data leaves your device | Data stays on your device |
| **Cost model** | Pay per API token / subscription | Built into device price (₹50,000–₹1,00,000+ phone) |
| **Scope** | General — knows many topics | Narrow — trained for specific use cases |
| **Personalization** | Cloud-based memory | Learns your patterns locally |

![Cloud LLMs need internet and send data to remote servers; on-device SLMs run locally on your phone or car — faster, private, and work offline](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/other-sessions/rahul-singh-23may/advanced-ai/adv-ai-02-slm-vs-llm.png?v=20260617)

### The Industry Shift

The instructor noted that the **growth phase of general LLMs is largely done**. The next wave is:

- **Use-case-specific SLMs** on devices
- **Personalization** that never leaves your phone
- **Energy-efficient** chips from Qualcomm and NVIDIA built for edge AI

If you plan to upgrade your phone in the next 1–2 years, look for devices with strong **on-device AI / SLM** capabilities — you will feel the difference in daily tasks.

### Activity: Compare Cloud vs On-Device AI

1. Open any cloud LLM (ChatGPT or Gemini) and ask a simple question **with Wi-Fi on** — note the response time.
2. Turn off Wi-Fi and try the same question — it will fail.
3. On a modern smartphone, try an on-device feature (voice typing, photo search, or a lens filter) **without internet** — notice it still works.
4. Write down one task from your daily life that would be **better on-device** (health tracking, personal finance notes, voice memos) and one that is **fine on cloud** (research, long writing).

---

## Token Optimization

This was the **most detailed topic** of the session. AI products often fail not because AI lacks value — but because they become **too expensive to scale** when more users join and more tokens get burned.

### The Microsoft Lesson

Microsoft initially gave all employees **unlimited Claude access**. By end of February, the bill was so high that they **stopped** unlimited usage. Claude, in particular, burns tokens aggressively — especially during its internal processing (reasoning) steps, even when the final output looks short.

**Key insight:** Your users do not care whether you use GPT-2 or GPT-5 behind the scenes. They only care about a good answer. Smart companies route most queries to cheaper models.

### The Three Layers of Token Usage

Every LLM interaction burns tokens at three stages:

| Layer | What Happens | Example |
|---|---|---|
| **Input** | Your prompt + context sent to the model | A 2,000-word job description pasted into a resume analyzer |
| **Processing** | Internal reasoning, retrieval, multiple model calls | Claude iterating 3–4 times before answering |
| **Output** | The text the model generates back to you | A 500-word or 5,000-word response |

You must optimize **all three** — not just the prompt.

![Token optimization across three layers: Input (pruning, caching), Processing (model routing, RAG, quantization), and Output (max_tokens, batching, streaming)](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/other-sessions/rahul-singh-23may/advanced-ai/adv-ai-03-token-optimization.png?v=20260617)

---

### Input Layer Techniques

#### 1. Prompt Pruning

**Official Definition:** Removing unnecessary words from a prompt before sending it to the final LLM — keeping only keywords and action-relevant text.

**In Simple Words:** Instead of writing a long paragraph, cut it down to the essential instruction.

**How to apply:** Use a **low-cost LLM** first to shorten the user's query, then send the trimmed version to your main model. In Lovable or your agent, add an instruction: *"Whenever a user asks a query, prune the prompt for minimal token usage, then forward it."*

#### 2. Keyword Mapping & Token Caching

If a user repeatedly talks about the same topics (for example, "construction operations" or "sports equipment"), store those keywords in an **in-memory cache**. Next time, augment the prompt automatically without the user repeating everything.

**Token caching** also stores frequently asked **responses** — if the same question comes again, serve from cache instead of calling the LLM.

#### 3. Use a Smaller Model to Refine the Prompt

Before sending to GPT-5 or Gemini Pro, run the raw user input through a cheaper model (GPT-2.5, Gemini 1.5) to clean and shorten it. This is what Faisal suggested in class — **optimize the prompt using a low-end LLM first**.

---

### Processing Layer Techniques

#### 4. Model Routing

**Official Definition:** Sending different types of user queries to different LLM models based on complexity — cheap models for simple tasks, expensive models only for hard ones.

**In Simple Words:** Like a hospital — minor cuts go to a clinic, serious surgery goes to a specialist. Not every question needs the most powerful (and expensive) model.

**Real-Life Example from class:**

| Query Type | Route To |
|---|---|
| Payments, cashbacks, discounts, order status | Cheaper model (GPT-2 / GPT-2.5) |
| Escalations, complaints | Mid-tier model |
| Investment decisions, complex analysis | Premium model (GPT-5 / Claude Opus) |

**Target:** Resolve **90% of queries** with a lower-end model. Only **10%** go to the premium model. This dramatically cuts processing cost.

![Model routing sends simple queries to cheaper models and complex queries to premium models — like a hospital triage system for AI](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/other-sessions/rahul-singh-23may/advanced-ai/adv-ai-04-model-routing.png?v=20260617)

**How to apply in n8n / Make:** Use **two models** in your workflow — for example, Gemini 1.5 and Gemini 3. If both give good quality for simple queries, you do not need the latest model for everything.

#### 5. Quantization

**Official Definition:** Reducing a large model's size by keeping only the weights and parameters relevant to a specific domain.

**In Simple Words:** You do not need the entire ChatGPT brain if you only work in sports equipment or healthcare. Quantization trims the model down to what matters for **your industry**.

**Examples:**
- **Sarvam AI** in India quantizes models for **Indian languages**
- **DeepSeek** quantized for the top 5–6 most common use cases instead of running the full general model

This is closely related to how **SLMs are created** — start big, then narrow down.

#### 6. RAG Instead of Full LLM Knowledge

Rather than asking the LLM to "know everything," use **RAG** to retrieve only relevant documents and pass those as context. This reduces both input and processing tokens. (Covered in depth in the previous session.)

#### 7. Fine-Tuning Instructions to Limit Reasoning

Add system-level instructions like:

- *"Only process if necessary."*
- *"Process and refine only if the user asks for it."*
- *"Apply reasoning only for the first level of understanding — do not cross-reference until the user requests it."*
- *"Only iterate once to get the answer — do not validate repeatedly."*

Claude Opus and Claude Sonnet often iterate 3–4 times internally before answering. These instructions stop unnecessary processing loops.

#### 8. Rule-Based Checks Before LLM

Not every request needs an LLM. Mirage pointed out in class: sometimes a **basic rule-based check** can answer the question directly. Microsoft learned this the hard way — do not use LLMs for everything.

---

### Output Layer Techniques

#### 9. Batching and Streaming

Instead of generating the full answer at once, send **smaller batches** or **stream** partial responses. If the user is satisfied with a short answer, you save output tokens.

#### 10. Output Token Hyperparameter

In your agent or n8n workflow, set **maximum token output count** — try 500, then 2,000, then 5,000. If 500 tokens give a good answer, you do not need 2,000.

```json
{
  "model": "gpt-4o-mini",
  "max_tokens": 500,
  "temperature": 0.3,
  "messages": [
    {
      "role": "system",
      "content": "Give concise answers. Do not repeat the question. Stop when the answer is complete."
    },
    {
      "role": "user",
      "content": "What are the revised non-maintenance charges for business classic current account from October 2025?"
    }
  ]
}
```

**How the code works:**
- `"max_tokens": 500` caps the output at 500 tokens — the model stops generating after that limit.
- `"temperature": 0.3` keeps answers focused and factual (lower = less creative rambling).
- The system message tells the model to be concise — saving both output and processing tokens.
- Compare response quality at 500 vs 2,000 tokens for your use case before finalizing.

#### 11. Sampling (Show Small Answers First)

Show the user a **short sample response**. If they accept it, stick with short answers. Over time, learn what response length works for your audience.

#### 12. Claude vs ChatGPT Output Style

Mirage asked why ChatGPT gives long outputs while Claude gives brief ones. This is a **configuration choice** — Claude is tuned for concise outputs, but it often burns **more processing tokens** internally to achieve that brevity. Output length alone does not tell you the full cost picture.

---

### Token Metrics to Track

Before launching an AI product to 100,000 users, launch for **10 users** first and measure:

| Metric | Why It Matters |
|---|---|
| **Cost per million tokens** | Your direct billing number |
| **Average tokens per user query** | Split across input, processing, and output |
| **Cache hit rate** | What % of responses come from cache vs fresh LLM calls? (20–30% cache hit = good strategy) |
| **Throughput** | How many requests per second/minute can you serve before the system breaks? (Remember the Ghibli image trend that overloaded servers) |
| **Model cost comparison** | GPT-2 is cheaper than GPT-5 — are you using the right model per query type? |

**Interview tip:** *"How do you optimize tokens across input, processing, and output?"* is a favourite question. Use the three-layer framework from this section.

### Quick Summary: Token Optimization by Layer

| Layer | Techniques |
|---|---|
| **Input** | Prompt pruning, keyword mapping, token caching, smaller model to refine prompt |
| **Processing** | Model routing, quantization, RAG, fine-tuned reasoning instructions, rule-based checks |
| **Output** | Batching, streaming, `max_tokens` hyperparameter, sampling (short answers first) |

### Activity: Token Optimization Audit

Pick any AI workflow you have built (n8n, Make, Lovable, or Dify):

1. Count roughly how many tokens your **input prompt** uses today.
2. Rewrite the same prompt in **half the words** (prompt pruning) — does quality drop?
3. Set `max_tokens` to **500** and test 3 queries — is the answer still useful?
4. Identify one query type that could go to a **cheaper model** via routing.
5. Note one place where a **rule-based check** could replace an LLM call entirely.

---

## LLMOps (LLM Operations)

Every large company has an **operations team** watching live dashboards. Ola monitors ride demand across India. Zomato watches restaurant ratings. At Myntra, an operations team once caught that American Express credit card payments had broken for two days — because someone was watching the numbers.

**LLMOps** is the same idea — but for AI applications.

### What Is LLMOps?

**Official Definition:** **LLMOps (LLM Operations)** is the practice of monitoring, measuring, and managing LLM-powered applications in production — covering prompts, models, costs, safety, and performance.

**In Simple Words:** LLMOps is the **control room dashboard** for your AI product. It tells you if your AI is healthy, expensive, slow, or hallucinating — before your users complain.

**Real-Life Example:** Think of an **ECG monitor for a patient's heart**. The LLMOps dashboard is the ECG for your application's AI layer — it shows the heartbeat of every prompt, model, and token in real time.

![LLMOps dashboard monitors token usage, latency, cost, prompt explorer, and model health — the control room for your AI application in production](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/other-sessions/rahul-singh-23may/advanced-ai/adv-ai-05-llmops.png?v=20260617)

### What the LLMOps Team Monitors

| Category | Metrics Tracked |
|---|---|
| **Prompt lifecycle** | How many prompts asked, A/B prompt variants, follow-up acceptance rate |
| **Quality & safety** | Hallucination rate, citation rate, politeness, harmful content, adversarial/jailbreak attempts |
| **Token & cost** | Token count, cost per request, model-wise spend |
| **Model health** | Success rate, failure rate, model drift, last deployment date, which model is most active |
| **Performance** | Latency percentiles by model, throughput, bottlenecks |
| **Security** | Daily adversarial attack count, jailbreak attempts by region |

At Microsoft, the first screen employees see tracks which parts of the world are attempting jailbreak prompts — that dashboard is part of LLMOps.

### Building an LLMOps Dashboard (Live Demo)

In class, students used a **prompt library** shared by the instructor and ran it in **Lovable** (and Replit as backup) to auto-generate an LLMOps dashboard. The generated dashboard included:

- **Dashboard** — overview of API usage
- **Product Metrics** — prompts asked, response time, satisfaction scores
- **Business Metrics** — user conversion, model usage split (GPT-4 vs Gemini), cost per request
- **Technical Metrics** — latency percentiles filtered by model
- **Prompt Explorer** — every user prompt, tokens burned, success vs failure

The dashboard connects via your **API key** (from Google AI Studio, OpenAI, etc.). Once validated, it tracks real usage data from your application's API calls.

### Who Uses the LLMOps Dashboard?

| Role | How They Use It |
|---|---|
| **AI Engineer** | *"Gemini responses have low satisfaction — let me check Prompt Explorer and latency."* |
| **Product Manager** | *"We upgraded to GPT-5.2 — token usage jumped from 1.5M to 3M. Where is the cost spike?"* |
| **Business / Leadership** | Daily or weekly reports on cost, user adoption, and model performance |
| **LLMOps Team** | Proactive alerts when metrics drop — automatic emails when something breaks |

### When to Use LLMOps

Use LLMOps when your application is **live with real users** and powered by LLM APIs. Every morning or evening, the team reviews:

- What prompts are users asking?
- What is the response success rate?
- How many tokens are burned per request?
- What will the end-of-month bill look like?

This prevents billing surprises and helps you catch failures early.

### Activity: Set Up a Mini LLMOps View

1. Go to **Google AI Studio** (aistudio.google.com) and create a free **API key**.
2. Open **Lovable**, **Replit**, **Bolt.new**, or **Cursor**.
3. Use a prompt like: *"Build an LLMOps dashboard for my finance AI app with Product Metrics, Business Metrics, Technical Metrics, and Prompt Explorer tabs. Include API key validation for Gemini."*
4. Publish the app and connect your API key.
5. Run 5 test queries through your app and check which metrics update with real data vs sample data.

---

## Key Takeaways

- **MCP** is the universal connector that lets LLMs talk to external apps (Zerodha, Zomato, Microsoft 365) — think USB Type-C for AI tools. Track success rate, latency, and security when using MCP servers.
- **On-device SLMs** are the next wave of AI — faster, private, offline-capable, and use-case-specific. The industry is shifting from general cloud LLMs to small models on your phone, car, and edge devices.
- **Token optimization** must cover all three layers: **input** (pruning, caching), **processing** (model routing, quantization, RAG, fine-tuned instructions), and **output** (max tokens, batching, streaming, sampling). Route 90% of queries to cheaper models.
- **LLMOps** is your AI application's health monitor — track prompts, costs, latency, hallucinations, and model drift through a single dashboard before users feel the pain.
- These four topics together form the foundation of **production-grade AI engineering** — building AI that is connected (MCP), efficient (token optimization), observable (LLMOps), and eventually personal (SLMs).

---

## Important Commands, Libraries & Terminologies

| Term / Tool | Meaning |
|---|---|
| **MCP (Model Context Protocol)** | Open standard by Anthropic for connecting LLMs to external tools and APIs |
| **MCP Server** | A published endpoint that wraps an app's API for LLM access |
| **MCP Marketplace** | Portal where companies list their MCP servers (Microsoft, Zerodha, Zomato, etc.) |
| **Claude Desktop — Edit Config** | JSON config file where MCP servers are added (Settings → Developer) |
| `npx mcp-remote` | Command pattern used to connect remote MCP servers |
| **SLM (Small Language Model)** | Compact model that runs on-device for specific use cases |
| **Edge / On-Device AI** | AI processing on local hardware instead of cloud servers |
| **Quantization** | Shrinking a model by keeping only domain-relevant weights |
| **Prompt Pruning** | Shortening a prompt to essential keywords before sending to LLM |
| **Token Caching** | Storing frequent keywords or responses to avoid repeat LLM calls |
| **Model Routing** | Sending queries to different LLM models based on complexity |
| **max_tokens** | API parameter that limits how many tokens the model generates in output |
| **Cache Hit Rate** | Percentage of responses served from cache instead of fresh LLM calls |
| **Throughput** | Number of requests the system handles per second/minute |
| **LLMOps** | Operations practice for monitoring LLM apps in production |
| **Prompt Explorer** | Dashboard view showing every user prompt, tokens used, and success/failure |
| **Model Drift** | When model performance degrades over time after deployment |
| **RAG** | Retrieval-Augmented Generation — fetch relevant docs instead of relying on full LLM knowledge |
| **n8n / Make.com** | Workflow automation tools where model routing and token limits can be configured |
| **Lovable / Replit / Bolt.new** | AI app builders used in class to generate the LLMOps dashboard |
| **Google AI Studio** | Platform to create Gemini API keys for dashboard integration |
| **GDPR / HIPAA** | Privacy regulations driving adoption of on-device SLMs |
