# Evaluating and Improving RAG Systems

## Context of This Session

In the previous session, you built the **ShopKart multi-document RAG assistant** — policy loaders, overlap chunking, **BGE** embeddings, **Chroma** storage, and **Groq** generation. Four demo queries worked: unopened returns, metro express, warranty repair, and COD refund timing.

That proved the **pipeline runs**. It did not prove the bot is **safe for real customers**. Real users ask about **opened boxes**, **prepaid UPI**, **water damage**, and **non-metro express** — edge cases where retrieval misses a chunk or the model adds confident extras.

Today you **extend the same `rag_pipeline.py`**. You run harder queries, read **Rank 1** in the terminal, apply **three targeted levers**, and compare **baseline vs improved**. The implementation **is** the session — no separate worksheets.

**In this session, you will:**

- Test with **realistic customer queries** beyond the happy-path demo
- **Classify** bad answers as **retrieval**, **generation**, or **hallucination**
- **Judge retrieval and generation separately** before changing code
- Apply **at least two levers** — stricter prompt, metadata filter, and **top-k** tuning
- Re-run the same queries and adopt a simple **test → diagnose → improve → re-test** habit

---

## When a Working Pipeline Still Gives Wrong Answers

Your ShopKart assistant can **respond** and still be **wrong**. That is normal in RAG — quality is not a simple on/off switch like a calculator.

A failed answer usually falls into one of three **failure modes**:

| Failure mode | What went wrong | What you see in the terminal |
|---|---|---|
| **Retrieval problem** | Wrong chunks retrieved, or the right rule never surfaced | Rank 1 **category** or **text** does not fit the question |
| **Generation problem** | Good chunks retrieved, but the answer misreads them | Retrieved text says **5–7 days**; answer says **instant** or **2 days** |
| **Hallucination** | Answer adds facts **not in** retrieved excerpts | **UPI refund steps** when your files only mention **COD → UPI/bank** |

- **Failure mode**
  - **Official Definition:** A **repeatable pattern** of wrong behaviour — wrong chunks, misread evidence, or invented facts.
  - **In Simple Words:** The **type of bug** you see again and again, not a one-off glitch.
  - **Real-Life Example:** Every wrong prescription at a clinic traces back to the same missed test — that repeating pattern is the failure mode.

**Why you classify first:** Raising **top-k** fixes a retrieval miss. It does **not** fix a model that ignores good excerpts. Stricter **prompts** help generation and hallucination. They do **not** create missing policy text. Change the **stage that failed**.

**Common doubt:** “The answer sounds polite and confident — retrieval must be fine.” **Confidence is not evidence.** Always read **Rank 1 category, source, and text** before trusting the reply.

![Three RAG failure modes for ShopKart — retrieval wrong or missing chunks, generation misreads good excerpts, hallucination adds facts not in policy text; each mode maps to a different fix lever](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session22/session22-01-three-failure-modes.png)

---

## The Clinic Test — Diagnose Before You Prescribe

Picture a **clinic** explaining why a patient got bad advice. The same three failure modes map cleanly to RAG.

- **Wrong test ordered** — the doctor never checked the report that would answer the question. That is **retrieval failure**: the policy paragraph exists in your library, but search did not bring it to the desk.
- **Report on desk, misread** — the correct paragraph was available, but the doctor quoted the wrong line. That is **generation failure**: evidence was present; the final answer was wrong.
- **No report, confident diagnosis anyway** — the doctor invented a treatment not on any page. That is **hallucination**: the answer is not supported by retrieved evidence.

Good clinics do not rebuild the hospital after one mistake. They ask **which stage failed** and fix **that stage**. Your lab follows the same discipline — **targeted fixes**, not random prompt stuffing.

![Clinic test analogy for RAG — wrong test ordered is retrieval failure, report misread is generation failure, confident diagnosis with no report is hallucination](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session22/session22-02-clinic-test-analogy.png)

---

## Evaluate Retrieval and Generation as Separate Stages

Every customer query passes through **two independent stages**. Judge each on its own before you edit code.

| Stage | Question to ask | Where to look |
|---|---|---|
| **Retrieval** | Did we fetch the **right policy** and **right chunk**? | Rank 1 **category**, **source**, **distance**, **text** |
| **Generation** | Does the **final answer faithfully reflect** the excerpts? | Compare answer numbers and rules to printed chunk text |

**Four-step checklist** (use in order for every test query):

1. **Right policy area?** — A returns question should show **returns** in Rank 1 category, not shipping.
2. **Right chunk within that policy?** — Rank 1 text should contain the specific rule (e.g. **COD → UPI**, not only generic refund wording).
3. **Answer factually correct?** — Days, amounts, and conditions match the retrieved excerpts.
4. **Answer grounded?** — No coupons, instant refunds, or payment steps that never appeared in the excerpts.

**Integrated learning point:** If step 1 fails, steps 3 and 4 almost always fail too. Do not tune the LLM prompt when Rank 1 category is wrong — fix **retrieval first**.

During the lab, your evaluation is simple: for each query in **`TEST_QUERIES`**, read **Rank 1**, then read **Answer**. That terminal read **is** your scorecard.

![Evaluate retrieval and generation as separate stages — Stage 1 inspect Rank 1 category source and text; Stage 2 compare final answer to excerpts; fix retrieval before tuning the prompt](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session22/session22-03-two-stage-evaluation.png)

![Four-step evaluation checklist — right policy area, right chunk, factually correct answer, grounded answer with no invented facts](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session22/session22-04-four-step-checklist.png)

---

## ShopKart Edge Cases — Read Before You Code

These examples use the **same four policy files** from your previous build. The live walkthrough focused on the first three — they show **why** demo success is not enough.

### Example 1 — Opened Accessory Returns (Retrieval)

- **Query:** *"Can I return a laptop charger if the box is opened?"*
- **Policy reminder:** Unopened items get **7 days**; **opened or used** items are **not eligible unless defective**; **electronics** need a warehouse check.
- **Likely symptom:** Answer mentions the **7-day window** but misses **opened / electronics** rules.
- **Terminal clue:** Rank 1 category may be **returns**, but Rank 1 text only shows the **unopened** sentence — the **opened-item** line lives in another chunk.
- **Failure mode:** **Retrieval** — right policy area, **wrong or incomplete chunk**.
- **Fix to try:** Raise **top-k** from 3 to 5, or increase **chunk overlap** so split rules stay together.

### Example 2 — COD Refund Timeline (Generation / Hallucination)

- **Query:** *"I returned a defective kettle on COD last week. When will the refund reach my UPI?"*
- **Policy reminder:** Refunds take **5–7 business days after warehouse verification**; **COD** goes to **UPI or bank account**.
- **Likely symptom:** Rank 1 text is correct, but the answer invents **UPI refund steps** or says **instant UPI credit**.
- **Terminal clue:** Rank 1 **refunds** chunk contains the right timeline — the model **summarised loosely** or **added payment details not in the excerpts**.
- **Failure mode:** **Generation** or **hallucination** — retrieval worked; the LLM misread or invented policy.
- **Fix to try:** **Stricter grounding prompt** — not higher top-k alone.

### Example 3 — Prepaid UPI Refund (Hallucination)

- **Query:** *"Is UPI refund available for prepaid orders?"*
- **Policy reminder:** Your files mention **COD → UPI/bank** only. There is **no prepaid UPI section**.
- **Likely symptom:** A detailed **UPI workflow** appears in the answer, or the model **infers prepaid from COD wording**.
- **Terminal clue:** Retrieved excerpts do not contain prepaid UPI rules — or retrieval is weak and generic.
- **Failure mode:** **Hallucination** — confident facts not supported by evidence.
- **Fix to try:** **Stricter prompt** with the exact **refusal sentence** from your previous build.

**Live diagnosis pattern:** For each query above, compare the **baseline** section (original prompt, no filter, **top_k=3**) with the **improved** section (strict prompt, category filter, **top_k=5**) in your terminal or saved output file.

---

## Hallucination Reduction — Flag and Verify

Hallucinations sound **official** but add facts your policies never contained. They are especially dangerous on **refunds and compliance** questions.

- **Hallucination**
  - **Official Definition:** Model output that **sounds authoritative** but is **not supported** by retrieved documents.
  - **In Simple Words:** The bot **makes up** rules — like a friend who guesses exam answers with full confidence.
  - **Real-Life Example:** A shopkeeper promising **10% extra discount** when the notice board says no discounts — customers will hold you to it.

**Two-step check** (use while reading the terminal):

1. **Flag claims** in the answer — timelines (*5–7 days*), payment types (*UPI*, *COD*), eligibility (*opened*, *metro*), offers (*coupon*, *instant*).
2. **Cross-check each claim** against the printed excerpts. No matching line in excerpts → treat as hallucination until proven otherwise.

**Honest refusal is OK:** Your previous build already used *"I do not have enough information in the provided policy excerpts."* Today you **enforce** that line more strictly when the corpus has no answer.

**Prompt tightening tip:** Compare your **baseline** and **strict** prompts side by side (a line diff tool works well). Add explicit **do not invent rules** lines and a fixed **refusal** sentence. You can draft prompts with ChatGPT, Gemini, or Claude — then review them against your policy files.

---

## Four Improvement Levers — When to Use Each

Once you know the failure mode, pick a **targeted lever**. In the live lab, three levers were applied together in the improved run. Change **one or two** per iteration when experimenting on your own — not all four at once.

### Lever 1 — Top-k Adjustment

- **Top-k**
  - **Official Definition:** The **number of best-matching chunks** returned per search.
  - **In Simple Words:** How many **policy cards** the librarian places on the desk.
  - **Real-Life Example:** Three revision cards for one chapter vs ten cards where seven are from the wrong subject — more is not always better.

| top-k | Risk | When to try |
|---|---|---|
| **Too low (1–2)** | Miss rules split across chunks | Rank 1 right area but **incomplete** answer |
| **Too high (8–10)** | **Shipping noise** on returns questions | Rank 1 OK but ranks 2–5 confuse the LLM |
| **Lab default** | Balanced start | **3** baseline, **5** in improved run |

### Lever 2 — Metadata Filtering by Policy Type

Your previous build already tags each chunk with **`category`**: **returns**, **shipping**, **warranty**, **refunds**.

- **Metadata filter**
  - **Official Definition:** Restricting search to chunks with a chosen metadata label before ranking results.
  - **In Simple Words:** Tell the librarian *“only bring books from the Returns shelf.”*
  - **Real-Life Example:** Asking the **hostel warden** about curfew, not the **mess manager** — same campus, wrong desk.

**Subdividing a large index:** Rather than matching embeddings across the **entire** knowledge base, route the user query to a **subcategory** first, then search only that subset. Chroma stores **metadata** with each chunk — a **`where`** filter on **`category`** implements this shelf-by-shelf search.

**When it helps:** Returns questions that kept pulling **shipping** paragraphs because both mention *"delivery"* and *"days"*.

**When to skip it:** You are unsure which category fits — run without filter first, then add filter once patterns are clear.

**Single-category limitation (important):** The lab’s **`guess_category`** picks **one** category per query. If an answer needs evidence from **both refunds and shipping**, filtering to one shelf can hide the other policy. The live demo showed this on multi-topic questions — a future improvement is to detect **multiple categories**, merge retrieved chunks, then generate.

**Fallback:** When **`guess_category`** returns **`None`**, search the **full index** (no filter). The keyword router is a **hit-and-trial** starting point — refine it as you see mis-routed queries.

### Lever 3 — Stricter Grounding Prompts

- **Grounding prompt**
  - **Official Definition:** Instructions that require answers to **follow retrieved context** and **refuse** when evidence is missing.
  - **In Simple Words:** A strict rule sheet on the support agent’s desk.
  - **Real-Life Example:** A bank teller who may only quote the **printed rate chart** — not guess from memory.

Weak prompts invite the LLM to mix **training memory** with your policies. Today you add **`generate_strict_answer`** with explicit **do not invent** rules and a fixed **refusal** line.

### Lever 4 — Chunk Size and Overlap (Optional Follow-Up)

Your previous defaults were **100 words** per chunk and **20 words** overlap. Some failures trace to **split rules**.

- **Split problem:** *"Opened or used items are not eligible unless defective"* — if *"unless defective"* lands in the **next chunk**, retrieval may return only the **ineligible** half.
- **Fix:** Try **120 words** and **30 overlap**, then delete **`chroma_store/`** and re-run **`build_knowledge_base`**.
- **Trade-off:** Larger chunks keep context together but can add noise within one file — re-test the same **`TEST_QUERIES`** after any change.

The live session focused on **prompt**, **metadata filter**, and **top-k**. Chunk tuning was discussed as an optional second iteration if retrieval still splits rules after those three levers.

![Four improvement levers — top-k adjustment, metadata filter by category, stricter grounding prompt with refusal, optional chunk size and overlap; change one or two per run](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session22/session22-05-four-improvement-levers.png)

---

## Extend `rag_pipeline.py`

Keep **all code from the previous build** — loaders, chunking, indexing, **`retrieve_policy_chunks`**, **`generate_grounded_answer`**, **`print_retrieved_chunks`**. Add the blocks below before **`main()`**.

If you cloned the instructor repository, the script may be named **`code.py`** instead of **`rag_pipeline.py`** — run whichever file is present in your folder.

### Step 1 — Test Queries

Replace the old four-query demo list with this **edge-case set**. You will run the **same list** in baseline and improved passes.

```python
TEST_QUERIES = [
    "Can I return a laptop charger if the box is opened?",  # Returns — opened / electronics
    "Is UPI refund available for prepaid orders?",  # Corpus gap — must refuse, not invent
    "I returned a defective kettle on COD last week. When will the refund reach my UPI?",  # Refunds — COD timeline
    "My earphones got water damage after 8 months. Is repair covered?",  # Warranty — liquid excluded
    "Will express shipping reach my non-metro pin code in 1 day?",  # Shipping — metro only
    "When will I get my refund after return?",  # Refunds — not delivery (word "when" trap)
    "When will my express order arrive in a metro city?",  # Shipping — not refunds (word "when" trap)
]
```

**Why these queries matter:**

- The first three map directly to the **ShopKart examples** walked through in the live lab.
- Queries 4–5 extend **warranty** and **shipping** edge cases — they exercise **`guess_category`** keyword routing.
- The last two **"when"** queries trap weak retrieval that confuses **refund timing** with **delivery timing**.

---

### Step 2 — Stricter Prompt (Hallucination and Generation Fix)

Add this **below** your existing **`generate_grounded_answer`** function:

```python
REFUSAL = "I do not have enough information in the provided policy excerpts."  # Same line as previous build


def build_strict_prompt(user_query, retrieved_chunks):
    context = ""  # One string built from all retrieved chunks
    for i, chunk in enumerate(retrieved_chunks, start=1):
        src = chunk["metadata"].get("source", "unknown")  # File name for traceability
        cat = chunk["metadata"].get("category", "unknown")  # returns / shipping / warranty / refunds
        context += f"\nExcerpt {i} (source: {src}, category: {cat}):\n{chunk['text']}\n"
    return f"""You are ShopKart customer support.
Use ONLY the excerpts below.
Rules:
1. Do not invent numbers, payment methods, or rules not in the excerpts.
2. Do not promise coupons, instant refunds, or extra benefits not in the excerpts.
3. If the excerpts do not contain enough information, say exactly: "{REFUSAL}"
4. Keep the answer short, polite, and faithful to the excerpts.

Excerpts:
{context}

Question: {user_query}

Answer:"""


def generate_strict_answer(client, user_query, retrieved_chunks):
    prompt = build_strict_prompt(user_query, retrieved_chunks)  # Build strict prompt text
    response = client.chat.completions.create(
        model=GENERATION_MODEL_NAME,  # Same Groq Llama model as before
        messages=[
            {"role": "system", "content": "Follow excerpts exactly. Never guess missing policy details."},
            {"role": "user", "content": prompt},  # Grounded user message
        ],
    )
    return response.choices[0].message.content.strip()  # Final answer string
```

**How the code works:**

- **`REFUSAL`** matches **`build_grounded_prompt`** from the previous build — same fallback sentence, **stricter** surrounding rules.
- **`build_strict_prompt`** still labels each excerpt with **source** and **category** — same pattern you already use.
- **`generate_strict_answer`** is called only in the **improved** run so you can compare against **`generate_grounded_answer`**.

---

### Step 3 — Retrieval With Optional Metadata Filter

Add this **below** your existing **`retrieve_policy_chunks`** function. It returns the **same chunk shape** your generator already expects.

```python
def guess_category(query):
    q = query.lower()  # Lowercase for simple keyword matching
    if "return" in q or "opened" in q or "unopened" in q:
        return "returns"  # Returns-related wording
    if "ship" in q or "express" in q or "metro" in q or "dispatch" in q or "deliver" in q:
        return "shipping"  # Shipping-related wording
    if "warranty" in q or "water" in q or "repair" in q or "liquid" in q:
        return "warranty"  # Warranty-related wording
    if "refund" in q or "cod" in q or "upi" in q or "money back" in q:
        return "refunds"  # Refunds-related wording
    return None  # No filter — search all categories


def retrieve_filtered(collection, model, user_query, top_k=3, category=None):
    embedding = model.encode([user_query], convert_to_numpy=True).tolist()  # Query vector
    args = {
        "query_embeddings": embedding,  # Vector input for similarity search
        "n_results": top_k,  # How many chunks to return
        "include": ["documents", "metadatas", "distances"],  # Text, labels, scores
    }
    if category:  # Only when filtering by policy type
        args["where"] = {"category": category}  # Chroma metadata filter
    results = collection.query(**args)  # Run search
    chunks = []  # Output list — same structure as retrieve_policy_chunks
    for doc, meta, dist in zip(
        results["documents"][0],  # Matched chunk texts
        results["metadatas"][0],  # Metadata per chunk
        results["distances"][0],  # Distance scores
    ):
        chunks.append({"text": doc, "metadata": meta, "distance": dist})  # One ranked hit
    return chunks
```

**How the code works:**

- **`guess_category`** is a **simple keyword router** — enough for this lab; production bots use smarter intent detection.
- **`retrieve_filtered`** mirrors **`retrieve_policy_chunks`** but adds optional **`where={"category": ...}`**.
- **`top_k=3`** matches your previous default; the improved run uses **`top_k=5`** when Rank 1 is right but incomplete.
- **`return None`** triggers a **full-index** search when no keyword category matches.

![Metadata filter on ShopKart chunks — guess_category routes the query to returns shipping warranty or refunds; retrieve_filtered searches only that category shelf in Chroma](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session22/session22-06-metadata-filter.png)

---

### Step 4 — Run Baseline, Then Improved

Replace **`main()`** with this. The two runs are your **before/after experiment**.

```python
def run_queries(client, collection, model, queries, top_k, use_filter, use_strict):
    label = f"top_k={top_k} | filter={use_filter} | strict={use_strict}"  # Settings for this pass
    print("\n" + "=" * 72)
    print("RUN:", label)
    print("=" * 72)
    for user_query in queries:
        category = guess_category(user_query) if use_filter else None  # Filter on or off
        chunks = retrieve_filtered(collection, model, user_query, top_k, category)  # Retrieve evidence
        print_retrieved_chunks(user_query, chunks)  # Always read Rank 1 here first
        if use_strict:
            answer = generate_strict_answer(client, user_query, chunks)  # Improved prompt path
        else:
            answer = generate_grounded_answer(client, user_query, chunks)  # Original prompt path
        print("\nAnswer:", answer)
        print("-" * 72)


def main():
    client = Groq()  # LLM client — GROQ_API_KEY from .env
    model = create_embedding_model()  # BGE embedding model
    collection = setup_chroma_collection()  # shopkart_policy_kb_v2 collection
    build_knowledge_base(model, collection)  # Offline load → chunk → embed → upsert

    print("\n--- BASELINE (original prompt, no filter, top_k=3) ---")
    run_queries(client, collection, model, TEST_QUERIES, top_k=3, use_filter=False, use_strict=False)

    print("\n--- IMPROVED (strict prompt + category filter + top_k=5) ---")
    run_queries(client, collection, model, TEST_QUERIES, top_k=5, use_filter=True, use_strict=True)


if __name__ == "__main__":
    main()
```

```bash
cd shopkart_rag_pipeline
python rag_pipeline.py
```

Use **`python3 rag_pipeline.py`** or **`python3 code.py`** if that is how Python is installed on your machine or how the instructor repo names the file.

**How the code works:**

- **Baseline run** mirrors the previous build — **`generate_grounded_answer`**, no filter, **`top_k=3`**.
- **Improved run** applies **three levers together**: strict prompt, **`guess_category`** filter, **`top_k=5`**.
- For each query: **`print_retrieved_chunks`** → read Rank 1 → read **Answer**. That sequence **is** your evaluation workflow.

**Saving output for comparison:** If terminal scrolling makes baseline vs improved hard to read, redirect output to a file (e.g. **`output.txt`**) or copy the **baseline** and **improved** sections into a text file. Compare **Rank 1** and **Answer** side by side for each query.

**Groq free-tier note:** Running many queries in one script makes **many API calls**. Free Groq accounts have **per-minute and daily request limits** — if answers stop generating or look empty, check your usage dashboard before assuming a code bug.

![Baseline vs improved run — same TEST_QUERIES with original prompt top_k=3 no filter versus strict prompt category filter top_k=5; compare Rank 1 and Answer in the terminal](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session22/session22-07-baseline-vs-improved.png)

---

### What to Verify in the Terminal

| Query theme | Rank 1 should show | Good answer should |
|---|---|---|
| Opened charger | **returns** + opened/electronics wording | Follow excerpt — not generic 7-day only |
| Prepaid UPI | **refunds** or weak match | **Refusal sentence** — no invented UPI flow |
| COD kettle | **refunds** + 5–7 days after verification | Timeline from excerpt, not "instant" |
| Water damage | **warranty** + liquid not covered | Clearly not covered |
| Non-metro express | **shipping** + metro-only express | No 1-day promise for non-metro |
| Refund "when" | **refunds** category | Refund timeline from policy |
| Delivery "when" | **shipping** category | Delivery timeline from policy |

| Step | Baseline | After improved run |
|---|---|---|
| Rank 1 **category** | May be wrong on edge cases | More often matches question area |
| Rank 1 **text** | May miss second half of rule | More complete with **top_k=5** + filter |
| **Answer** | May add instant UPI or coupons | Sticks to excerpts or **refuses** |

**If opened-item queries still fail after the improved run**, try chunk tuning at the top of the file:

```python
DEFAULT_CHUNK_SIZE = 120  # Slightly larger chunks — optional second iteration
DEFAULT_CHUNK_OVERLAP = 30  # More overlap across chunk boundaries
```

Delete **`chroma_store/`** (or change **`COLLECTION_NAME`**) and run again so old chunks do not mix with new ones.

---

## The Iterative Evaluation Cycle

Building RAG is **step one**. Reliable products repeat:

```text
test → diagnose → improve → re-test
```

- **Test** — run **`TEST_QUERIES`** every time; same list so results are comparable.
- **Diagnose** — Rank 1 wrong → **retrieval**. Rank 1 right but answer wrong → **generation** or **hallucination**.
- **Improve** — one or two levers per iteration; log what you changed.
- **Re-test** — run **`python rag_pipeline.py`** again after code or policy file changes.

**When to repeat the cycle in real products:**

| Trigger | What to do |
|---|---|
| New **refund PDF** uploaded | Re-run **`build_knowledge_base`**, then **`TEST_QUERIES`** |
| Support team flags wrong **warranty** answers | Filter to **warranty**, tighten prompt, re-test |
| **Groq model** swapped | Re-run full suite — generation behaviour can shift |
| Customer report of **invented offer** | Review hallucination — enforce **refusal** line |

Policy updates mean **refresh the index** — the model and prompts can stay the same while answers drift if documents are stale.

This mindset applies when RAG moves **inside agent workflows** in upcoming work — same quality bar, more places to watch.

![Iterative evaluation cycle — test with TEST_QUERIES, diagnose failure mode from Rank 1, improve one or two levers, re-test; repeat after policy updates or user feedback](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260313/module2/session22/session22-08-iterative-cycle.png)

---

## Key Takeaways

- **Read Rank 1 first** — **category** and **text** tell you if retrieval failed before you blame the LLM.
- **Three failure types** — **retrieval**, **generation**, **hallucination** — each needs a different fix; the clinic analogy keeps that clear.
- **Judge stages separately** — good retrieval does not guarantee a good answer; compare excerpts to the final reply line by line.
- **This lab applies three levers** — **strict prompt**, **metadata filter**, and **top_k=5** in the improved run; optional **chunk overlap** if retrieval still splits rules.
- **Metadata filter picks one category** — multi-category questions may need merged retrieval in a future iteration.
- **Same project, same stack** — you extend **`rag_pipeline.py`** (or **`code.py`**) on **`shopkart_policy_kb_v2`** with **BGE + Chroma + Groq**.
- **RAG is never “done”** — policy updates and new customer questions require ongoing **test → diagnose → improve → re-test**.

---

## Important Commands, Libraries, and Terminologies used

| Term / Command | Meaning in one line |
|---|---|
| **Failure mode** | Repeatable pattern — retrieval, generation, or hallucination |
| **Retrieval tuning** | Adjust top-k, filters, or chunks so the right policy surfaces |
| **Hallucination** | Confident answer not supported by retrieved excerpts |
| **Grounding prompt** | Instructions forcing answers to follow context and refuse when missing |
| **Top-k** | Number of nearest chunks returned per query |
| **Metadata filter** | Chroma **`where={"category": ...}`** — search one policy shelf only |
| **`guess_category`** | Hit-and-trial keyword router → returns / shipping / warranty / refunds |
| **`retrieve_filtered`** | Like **`retrieve_policy_chunks`** with optional category filter |
| **`generate_strict_answer`** | Stricter prompt with fixed **refusal** sentence |
| **`run_queries`** | Runs test list with chosen top_k, filter, and prompt settings |
| **`build_knowledge_base`** | Re-run after chunk size change or new policy files |
| **`shopkart_policy_kb_v2`** | Same Chroma collection as the previous build |
| **`output.txt`** | Optional file to save baseline vs improved terminal output for comparison |
| **Iterative evaluation** | test → diagnose → improve → re-test when corpus or users change |
| **BGE / Chroma / Groq** | Same embedding, vector store, and LLM stack as before |
