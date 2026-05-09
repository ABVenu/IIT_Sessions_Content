# Evaluating and Improving RAG Systems

## What You Will Learn in This Session

In the previous session, we built a complete, production-style RAG pipeline for an e-commerce customer support assistant. We worked with multiple real policy documents, implemented document ingestion using document loaders, applied chunking strategies, generated embeddings, stored them in a vector database, and built a working end-to-end multi-document RAG assistant.

In this session, we take that system one step further — from building to improving. This is a conceptual session focused on:

- How to test whether your RAG system is giving correct answers
- What metrics to use for measuring retrieval and response quality
- How to detect and fix hallucinations, poor retrieval, and weak prompts
- How to set up a continuous improvement loop using user feedback

---

## Why RAG Quality Is Not a 0 or 1 Problem

When you run a math problem, the answer is either correct or incorrect — that is a binary result. A RAG system is completely different. **Your system can give an answer and still be wrong.** The question is never just "did it answer?" — it is "how accurate, relevant, and trustworthy was that answer?"

Think about this: when you use Swiggy's customer support chat, someone ordering from Domino's might get a perfect reply, while someone ordering from a small local restaurant might get a confusing, wrong response. The code is the same, but the **quality** is different for each user. This is why quality in RAG is always **subjective** — and companies like Amazon, Flipkart, and Zomato all have their own measurement frameworks.

- **Binary evaluation** (Yes/No, Working/Not Working) works for deterministic problems like code execution or math.
- **Quality evaluation** is needed for RAG because answers can be partially right, outdated, hallucinated, or incomplete.
- Every company or team defines its own quality parameters — there is no single universal correct score.

![RAG answers vary in quality on a spectrum—not just correct vs wrong](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session31/lecture-notes-images/session31-01-rag-quality-spectrum.png)

---

## The Retriever: The Most Important Component in Your RAG System

Before talking about evaluation, it is essential to understand **why the Retriever is the most critical component** in a RAG system. Getting this right means getting your RAG output right.

A RAG system has two main components: the **Retriever** (which fetches relevant documents from the knowledge base) and the **Generator** (the LLM that writes the final answer). The LLM can only work with what you give it — if you give it wrong or irrelevant documents, it will generate a wrong or irrelevant answer. This is the classic AI principle: **"Garbage In, Garbage Out."**

- **Retriever** = The librarian who goes and fetches the right books for you
- **Generator (LLM)** = The reader who reads those books and writes your answer
- If the librarian brings the wrong book, the reader's answer will be wrong — and **it is not the reader's fault**

**Key rule to remember:** When your RAG system is underperforming, always focus on improving your **Retriever first**. Do not blame the LLM for generating bad answers when the retrieved context itself is weak or irrelevant.

![Retriever fetches context from the vector database; the LLM generates the answer—garbage in, garbage out](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session31/lecture-notes-images/session31-02-retriever-generator.png)

---

## Properties of a Good RAG System

Once you build a RAG system, the most important question is: what makes it a *good* one? Here are the five essential properties every production RAG system must have.

![Five pillars of a production RAG system: accuracy, grounding, completeness, safety, and freshness](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session31/lecture-notes-images/session31-03-five-properties-rag.png)

### Accuracy

**Official Definition:** Accuracy means the system returns a factually correct answer that is fully consistent with the source documents.

**In Simple Words:** The answer should not be wrong. If the policy says returns are allowed within 30 days, the system should never reply with 7 days.

**Real-Life Example from the Session:**
- Query 1: *"When will I get my refund?"*
- Query 2: *"When will my product be delivered?"*

Both queries ask about time and may look similar to a weak RAG system because both have the word "when" in them. But one is about a **refund** and the other is about **delivery** — they require completely different policy documents. If the system confuses the two and retrieves the wrong document, the answer will be inaccurate.

### Grounding

**Official Definition:** A grounded response is one that is directly supported by the retrieved documents and contains no claims that come from outside the knowledge base.

**In Simple Words:** The answer should not come from "something I read somewhere once." Every fact in the answer must be traceable to a specific document or section.

**Real-Life Example:** Think of a lawyer in court. A good lawyer says *"As per Section 302 of the agreement..."* A bad lawyer says *"I think this is how it works."* The first is grounded; the second is not. Your RAG system should always be the good lawyer — every claim should have a source.

- **Grounded answer:** *"As per the Refund Policy (Section 3), your refund will be processed in 5–7 working days."*
- **Ungrounded answer:** *"Your refund will come soon."*

### Completeness

**Official Definition:** A complete response covers all relevant aspects of the query without leaving out important details.

**In Simple Words:** The answer should not be half-baked. If a user asks about returning a product, the answer should cover the time limit, the condition of the product, and the packaging requirement — not just one part of it.

### Safety and Privacy

**Official Definition:** A safe response does not disclose confidential company information or internal policy details that are not meant for customers.

**In Simple Words:** Not every document in your database is meant to be shared with the customer. Internal escalation procedures, pricing strategies, or legal references should stay internal. Your RAG system must be built to respect these boundaries and never accidentally expose sensitive data.

### Freshness (Up-to-Date)

**Official Definition:** The response should be based on the latest version of the policy documents, not on outdated or expired rules.

**In Simple Words:** If the return policy was 7 days last year but was updated to 30 days this year, your system should use the **new rule**. If the knowledge base is not updated and the old document is still being retrieved, the answer will be wrong — even if the retrieval and generation logic is perfect.

---

## Common Failure Cases in a RAG System

Now that we know what a good RAG system looks like, let us understand where things can go wrong. This is your debugging checklist when responses are rated poorly.

### Wrong Policy Date in the Response

- **Example:** The current policy says returns are allowed within **30 days**, but the system says **7 days**.
- **Root Cause:** The system retrieved an older, outdated version of the policy document, or the LLM is using its own stale internal knowledge.
- **How to Catch It:** Always verify that the retrieved document matches the latest version in your knowledge base.

### Confusion Between Similar-Looking Queries

- **Example:** *"When will I get my refund?"* vs. *"When will my order arrive?"* — both use the word "when" and talk about time, but they need completely different policy sections.
- **Root Cause:** The retriever is matching based on surface-level keywords instead of understanding the true intent of the query.
- **How to Catch It:** Build a test dataset with pairs of similar-but-different queries and check which document was actually retrieved for each.

### Hallucinated Responses

**Official Definition:** A hallucinated response is one where the LLM confidently states something that is NOT present in any retrieved document — it is effectively making things up.

**In Simple Words:** The LLM adds information from its own training memory instead of sticking strictly to the policy documents you provided.

**Real-Life Example from the Session:**
- Retrieved context says: *"Refund takes 5 to 7 days."*
- The system responds: *"Refund takes 5 to 7 days, and you will also get a ₹100 coupon code as compensation for the delay."*
- The coupon code was **never mentioned in any retrieved document**. The LLM added it based on something it may have learned during training — perhaps some other company offers this compensation.
- **This is hallucination.** It is dangerous in a business context because the customer will expect a coupon that does not actually exist, leading to complaints and loss of trust.

![Grounded answers stick to retrieved policy text; hallucinations add details that never appeared in the context](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session31/lecture-notes-images/session31-06-hallucination-vs-grounded.png)

---

## The Evaluation Framework: 4 Things to Always Check

Here is a practical, step-by-step framework to evaluate your RAG system for every query it handles.

| Step | Question to Ask |
|------|----------------|
| **1. Right Document Retrieved?** | Did the system fetch the correct policy document for this query? |
| **2. Right Chunk Retrieved?** | From that document, did the system pick the right section (chunk)? |
| **3. Final Response Correct?** | Is the generated answer factually right and complete? |
| **4. Response Grounded?** | Is the answer backed by the retrieved document — not random assumptions? |

**Why this step-by-step order matters:**
- If Step 1 fails (wrong document fetched), all the following steps will automatically fail too.
- If Step 1 passes but Step 2 fails (right document, but wrong chunk), the answer will be partially wrong.
- Only if both Steps 1 and 2 pass can you expect a strong Step 3 and Step 4.

**Analogy — Ordering food on Zomato:**
1. Did the app find the right restaurant? → *Right Document*
2. Did you select the right dish from the menu? → *Right Chunk*
3. Did the food arrive as described on the menu? → *Correct Response*
4. Does the dish actually match what was shown in the photo? → *Grounded Response*

![Four-step RAG evaluation checklist: document → chunk → answer correctness → grounding](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session31/lecture-notes-images/session31-04-evaluation-four-steps.png)

---

## Building a Sample Evaluation Dataset

Before launching your RAG application to real customers, you must test it internally. The way to do this is by creating a **sample evaluation dataset** — a collection of test queries with known correct answers and expected source documents.

**Step-by-step process for building the dataset:**

1. **Write 20–50 realistic user queries** that cover all the major policy categories (e.g., return, refund, shipping, warranty, cancellation).
2. **For each query, note the expected policy document** that the system should retrieve (e.g., Return Policy document).
3. **For each query, write the expected correct answer** based on what the policy actually says.
4. **Index your documents** — chunk, embed, and store all policy documents in the vector database.
5. **Run the RAG system** on each test query and collect the actual response.
6. **Compare outputs** — did the system retrieve the right document? Is the answer correct?
7. **Give a score** to each response (e.g., on a scale of 0–2 or 1–5 stars).
8. **Dig into low-scored responses** — analyse 1-star and 2-star answers to find the root cause.

**Sample Evaluation Dataset for an E-Commerce RAG System:**

| User Query | Expected Document | Expected Answer |
|-----------|-------------------|-----------------|
| Can I return my shoes after 15 days? | Return Policy | Returns allowed within 30 days if product is unused and original packaging is intact |
| Can I return opened personal care items? | Return Policy | Opened personal care items are not eligible for return |
| How long does express shipping take? | Shipping Policy | Express shipping is delivered within 1–2 business days |
| Does the warranty cover liquid damage? | Warranty Policy | Liquid damage is not covered under warranty |
| When will I get my COD refund? | Refund Policy – COD | COD refunds require bank details; processing takes longer than online payment refunds |

**How many times should you run the test?**
Run the RAG application on the same test queries many times — even up to 100 iterations — to check consistency. Then:
- Count how many 5-star responses you got
- Focus on the 1-star and 2-star responses — these reveal where your system is failing
- Investigate each low-star response to find what went wrong (wrong document? hallucination? incomplete answer?)

---

## Scoring Retrieval Quality: The 0–2 Scale

When evaluating whether a specific retrieval was good or not, you can use a simple **0 to 2 scoring scale** to rate the quality:

| Score | Meaning | Example |
|-------|---------|---------|
| **0** | Completely irrelevant — wrong document retrieved altogether | User asks about refund; system fetches the shipping policy |
| **1** | Partially relevant — right category but missing key details | User asks about COD refund; system gives a general refund timeline without addressing COD-specific rules |
| **2** | Fully relevant — correct document, complete information, grounded | User asks about COD refund; system retrieves the COD-specific refund section with correct process and timeline |

**Why COD (Cash on Delivery) requires a different document:**
- For **online payments** (credit card, debit card, UPI, net banking): The refund automatically goes back to the source account — quick, typically 2–3 hours to 2–3 days.
- For **COD payments**: The customer paid in cash, so there is no digital source to refund to. The customer must provide bank details, and the process is more complex and takes longer.
- A system that gives a general "5–7 days" answer to a COD refund query, without acknowledging this critical difference, deserves a **Score 1** — not Score 2.

---

## Retrieval Metrics: Precision and Recall

Now let us move to two important **measurable retrieval metrics** — numbers you can actually calculate and track over time.

### Precision

**Official Definition:** Precision measures, out of all the documents your system retrieved for a query, how many of them are actually relevant to answering that query.

**In Simple Words:** Out of everything you brought back from the database, how much of it was actually useful?

**Formula:**
```
Precision = Number of Relevant Retrieved Documents / Total Retrieved Documents
```

**Example:**
- A user asks about refund.
- Your system retrieves **4 documents** (top-K = 4).
- Only **2 of those 4** are actually about refund. The other 2 are about delivery and product warranty.
- **Precision = 2 / 4 = 0.5 = 50%**

**What does high precision mean?**
- High precision = most retrieved documents are relevant = **less noise**.
- Noise in RAG means irrelevant documents that confuse the LLM and dilute the quality of the answer.
- **Analogy:** Imagine standing at a busy traffic signal in Mumbai. There is constant horn honking — lots of sound, but none of it is useful information for you. That noise is exactly what low-precision retrieval feels like for your LLM.
- High precision = mostly useful signal, very little noise.

**How to improve precision?**
- **Reduce the top-K value** — retrieve fewer, more targeted documents.
- **Apply metadata filtering** — narrow the search space before running similarity search (covered in a later section).

### Recall

**Official Definition:** Recall measures, out of all the relevant documents that exist in your knowledge base for a query, how many did your system actually retrieve?

**In Simple Words:** Of all the useful documents that are out there, how many did you actually find?

**Formula:**
```
Recall = Number of Relevant Documents Retrieved / Total Relevant Documents in Knowledge Base
```

**Example:**
- There are **4 relevant documents** about refund in your entire knowledge base.
- With top-K = 3, your system retrieved only **3 of them**.
- **Recall = 3 / 4 = 0.75 = 75%**

**What does high recall mean?**
- High recall = you are not missing important relevant documents.
- You found most (or all) of the useful context for this query.

### Precision vs. Recall: The Trade-Off

These two metrics often push in opposite directions. Understanding the trade-off is essential for tuning your system well.

| | **Precision** | **Recall** |
|-|-----------|--------|
| **What it measures** | Quality/relevance of retrieved documents | Coverage — are you missing any relevant documents? |
| **What it tries to avoid** | Irrelevant (noisy) documents | Missing relevant documents |
| **Improves when you…** | Retrieve fewer, more focused docs | Retrieve more, broader docs |
| **Risk of going too far** | You might miss some relevant docs | You might bring in too many irrelevant docs |

**The goal:** Find the right balance between the two. Both metrics are ultimately trying to increase the relevance of your retrieved content — just from different angles.

![Precision vs recall: fewer retrieved docs reduce noise; more retrieved docs improve coverage—tune Top-K for balance](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session31/lecture-notes-images/session31-05-precision-recall-tradeoff.png)

### Top-K Recall

**Official Definition:** Top-K Recall checks whether the correct and most relevant document or answer appears within the top-K documents that your system retrieved.

**In Simple Words:** Did the right answer show up somewhere in your top K results — even if it was not ranked first?

**Why this matters:**
- Semantic search works on vector similarity across potentially **1,536 dimensions** (for OpenAI embeddings). Even if you expect a certain document to be the first result, the actual ordering depends on all those dimensions simultaneously — not just the obvious keywords.
- The document you expect to be ranked #1 might end up at position #2 or #3 due to how the embeddings are weighted.
- As long as that document appears within the top-K window, it will be included in the context for the LLM.

**Example:**
- Query: *"What is the refund timeline for COD orders?"*
- Top-3 results: [General Refund Policy, COD Refund Policy, Shipping Policy]
- The correct answer is in the **COD Refund Policy**, which ranked second.
- **Top-3 Recall = Passed ✓** (the answer was within top 3)
- **Top-1 Recall = Failed ✗** (the answer was not the first result)
- With K=3, the LLM will still have access to the right context.

---

## Scoring Response Accuracy: The 0–3 Scale

Beyond retrieval, you also need to score the **quality of the final generated answer**. Here is a practical 0–3 scale:

| Score | Meaning |
|-------|---------|
| **0** | Completely wrong — hallucinated, contradicts the policy, or totally off-topic |
| **1** | Partially correct — some right information, but mixed with wrong or missing details |
| **2** | Mostly correct — right answer with minor gaps or a small unverified claim |
| **3** | Fully correct — accurate, complete, and grounded in the retrieved document |

**Example — Warranty and Liquid Damage:**

| System Response | Score | Reason |
|----------------|-------|--------|
| *"Yes, warranty covers liquid damage."* | **0** | Completely wrong. Policy says liquid damage is NOT covered. This is a hallucination. |
| *"Warranty does not cover liquid damage."* | **3** | Correct, complete, and grounded. |
| *"Warranty does not cover liquid damage, but you may get a free replacement."* | **1 or 2** | First part is correct. "Free replacement" needs to be verified against the document — if it is not there, it is a hallucination and pulls the score down. |

These scores are always subjective. Your team will refine the scoring criteria over time as more people review the evaluation process and suggest improvements.

---

## How to Detect Hallucinations

There is no perfect automatic sensor for hallucination — it is not like a spell-checker that turns red when something is wrong. But here is a practical **approximate framework** you can apply:

**Step 1: Flag every specific claim in the response.**
Look for claims about timelines, amounts, conditions, offers, discounts, coupon codes, or eligibility rules.
- *"Refund takes 5–7 days"* → Claim about timeline
- *"You will get ₹100 coupon code"* → Claim about compensation
- *"Express shipping is free for orders above ₹499"* → Claim about pricing condition

**Step 2: Cross-check each claim against the retrieved document.**
- Is this claim present in the retrieved chunk or document? **→ Not a hallucination.**
- Is this claim absent from the retrieved content? **→ Possible hallucination.**

**Step 3: Investigate further if a claim is not found in the retrieved document.**
- Is it in any other document in the knowledge base?
- Did the LLM pull this from its own pre-training knowledge?
- If the claim has no source document, it is **hallucinated**.

**Key tip:** The more specific and numerical a claim (exact days, exact rupee amounts, exact conditions), the higher the risk of hallucination if your RAG system is not perfectly grounded. Always be suspicious of very specific numbers that you did not expect.

---

## Improving Grounding in Responses

Now that we understand grounding, let us see how to **actively make your responses more grounded** during the generation step.

**Core strategy: Always cite the source in the answer.**

When the system generates an answer, it should explicitly reference where that information came from. This is how good customer support agents at companies like Flipkart work — they say *"As per our Return Policy, Section 2..."* rather than just *"You can return it."*

**Grounded vs. Ungrounded Answers:**

| Ungrounded | Grounded |
|-----------|----------|
| *"Your refund will come in a few days."* | *"As per the Refund Policy, your refund will be processed within 5–7 working days."* |
| *"You cannot return this product."* | *"As per the Return Policy (Section 3), personal care items once opened cannot be returned."* |
| *"Your order will arrive soon."* | *"As per the Shipping Policy, standard delivery takes 3–5 business days."* |

**Important note on privacy and citations:**
You may not always be allowed to share the exact section number or document name with the customer — internal policy might restrict this. But even then, your prompt should be designed so that the system **does not make up claims** that are absent from the retrieved documents. Not citing a source is acceptable; making up a source or fact is not.

---

## Tuning the Top-K Parameter

One of the most direct ways to improve your RAG system is tuning the **top-K value** — the number of documents retrieved from the vector database for each query.

**Official Definition:** Top-K is the parameter that controls how many of the most-similar documents are retrieved from the vector database in response to a user query.

**In Simple Words:** K is like telling a librarian how many books to bring. K=3 means bring the top 3 most relevant books. K=10 means bring 10 books — but some of those might be loosely related.

**The core trade-off:**

| K Value | What Happens | Problem |
|---------|-------------|---------|
| **Too Low (K=1 or K=2)** | Only closest matches retrieved | You might miss important context from other relevant documents — low recall |
| **Too High (K=8 or K=10)** | Many documents retrieved | Irrelevant documents creep in, adding noise and confusing the LLM — low precision |

**How to tune K step-by-step:**
1. Start with a low value like **K=3**.
2. Run your test dataset. Check precision, recall, and response quality scores.
3. If queries are missing important context (low recall), **increase K by 1**.
4. If queries are returning irrelevant documents (low precision), **decrease K by 1**.
5. At the point where increasing K starts hurting precision without improving recall, you have found your sweet spot.

**General recommendation:** For most e-commerce RAG use cases, **K = 3 to 5** works well. But the right value is always system-specific — a large knowledge base with many detailed documents may need higher K, while a focused system with a few precise documents may work better with K=2 or K=3.

![Tuning Top-K: very low K risks missing context; very high K adds irrelevant noise—aim for a sweet spot](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session31/lecture-notes-images/session31-07-top-k-tuning.png)

---

## Applying Metadata Filtering for Better Precision

Metadata filtering is a powerful technique that improves precision **before** the similarity search even runs — by restricting the search to only documents in the relevant category.

**Official Definition:** Metadata filtering means applying a category-based restriction on the vector database so that similarity search only runs on a specific subset of documents matching a filter condition.

**In Simple Words:** Instead of searching through all 1,000 documents, you first say *"only look at refund documents"*, and then run similarity search on just those 50 refund documents.

**Real-Life Example:**
- Your knowledge base has 1,000 documents across categories: return policy, shipping policy, warranty policy, payment policy, cancellation policy, and more.
- A user asks: *"Can I get a refund on a cancelled order?"*
- **Without metadata filtering:** Similarity search runs across all 1,000 documents. The top-5 results might include irrelevant shipping or cancellation documents.
- **With metadata filtering:** You apply the filter `category = "refund"` first. Similarity search now runs on only 50 refund documents. Every result is directly about refund.

**Benefits:**
- Even if K=5, all 5 results will be from the correct category — precision improves dramatically.
- Irrelevant categories are completely excluded from the search, no matter how similar they might look based on word choice alone.
- This technique was implemented in our earlier session when we built the RAG pipeline — it is a simple parameter you pass when calling the vector database search function.

---

## Improving Prompt Design for Policy-Based Answers

The quality of your final answer heavily depends on how you design your **prompt template** — the instructions you pass to the LLM along with the retrieved context. A weak prompt leads to hallucination; a strong prompt grounds the LLM to the retrieved context.

**Weak Prompt — Do NOT use this:**
```
Answer this customer question: {question}
```
This gives the LLM zero restrictions. It will mix its own pre-training knowledge with the retrieved context and potentially hallucinate details that are not in your policy documents.

**Strong Prompt — Always use something like this:**
```
You are a customer support agent for an e-commerce company.
Use ONLY the policy context provided below to answer the customer's question.
Do NOT make up any policy details, timelines, or offers not mentioned in the context.
If the answer is not present in the provided context, respond with:
"I don't have enough information to answer this. Please contact our support team."
Always mention specific timelines, eligibility conditions, and limitations when they are available.

Context:
{retrieved_context}

Customer Question:
{question}
```

**Why each rule in the strong prompt matters:**

| Rule | Why It Is Important |
|------|---------------------|
| *"Use ONLY the provided context"* | Prevents the LLM from mixing in outside knowledge or guesses |
| *"Do NOT make up policy details"* | Directly prevents hallucination |
| *"If not found, say I don't know"* | Better to admit ignorance than to give a wrong, confident answer |
| *"Mention specific timelines and conditions"* | Ensures completeness — no vague, wishy-washy answers |

**Remember:** It is completely acceptable for your RAG system to say *"I don't have that information."* A wrong answer is far more damaging than an honest *"I don't know."* When the system says it does not know, the team can add that information to the knowledge base and improve the system for future queries.

---

## Incorporating User Feedback for Improvement

Once your system is live, the most powerful source of improvement data is real **user feedback**. This is what makes production RAG systems get better over time.

**How apps like Swiggy and Amazon collect feedback today:**
- After a support query is resolved: *"Was this helpful?"* — **Thumbs up / Thumbs down** (simple binary feedback).
- Some apps use star ratings: 1 to 5 stars.
- After the rating, they ask **follow-up questions that change based on the rating:**
  - **5 stars:** *"What did you like? Speed / Accuracy / Clarity of response?"*
  - **1 star:** *"What went wrong? Wrong answer / Took too long / Did not understand my issue?"*
- This is called **structured feedback** — it gives the team actionable, categorised data rather than just a number.

**How to use collected feedback to improve your RAG system:**
1. **Store every piece of feedback** linked to the specific query, the retrieved document, and the generated response.
2. **Identify failure patterns** — Are most 1-star ratings on warranty questions? On refund queries from COD customers? On queries submitted after 9 PM?
3. **Dig into low-rated interactions** — What document was retrieved? Was the answer grounded? Was there a hallucination?
4. **Fix the root cause** — Add a missing document, update an outdated policy, improve the prompt template, or tune the K value.
5. **Re-test** — Run the test dataset again and measure whether the scores have improved.
6. **Repeat continuously** — This loop never ends.

---

## Establishing Continuous Evaluation Practices

Building a RAG system is not a one-time event. **Evaluation and improvement is an ongoing cycle** — like maintaining a restaurant. You do not cook the dish once and never update the recipe.

**Two types of evaluation loops you must run:**

**1. Internal Testing Loop (Before Launch)**
- Build a test dataset with known queries and expected answers.
- Run the RAG system many times on this dataset.
- Score every response. Find patterns in low-scoring responses.
- Improve retrieval, prompt design, or documents. Then re-test until quality is consistently high.

**2. External Improvement Loop (After Launch — User Feedback)**
- Actively collect real user feedback after every query resolution.
- At a regular cadence (weekly or daily), analyse the feedback data.
- Identify which types of queries are failing most often.
- Update the knowledge base, tune parameters, and refine prompts accordingly.

**How often should you run the evaluation cycle?**
- **Large platforms (Amazon, Swiggy):** Every 2–3 days because they get massive feedback volumes daily. There is always enough new data to act on.
- **Medium applications:** Weekly evaluation is a good starting cadence.
- **There is no finish line.** Your RAG system should keep getting better as long as you keep running this loop.

![Continuous evaluation loop: deploy, collect feedback, fix retrieval and prompts, retest, repeat](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-260113/module2/Session31/lecture-notes-images/session31-08-continuous-feedback-loop.png)

**What can change in production that you must keep up with?**
- New products added to the catalogue (new return/warranty rules)
- Existing policies updated or new policies introduced
- New payment methods with different refund timelines (e.g., new UPI wallet)
- Seasonal rule changes (e.g., different return policies during sale season)
- New types of user queries that were never anticipated during development

---

## Key Takeaways

- **RAG quality is never binary.** A system can respond and still be wrong, incomplete, hallucinated, or outdated. Evaluation must look at accuracy, grounding, completeness, safety, and freshness together.
- **The Retriever is your most important component.** Poor retrieval means the LLM gets bad context, and "Garbage In, Garbage Out" will always apply. Fix the Retriever before blaming the LLM.
- **Precision and Recall are your two core retrieval metrics.** Precision measures how much of what you retrieved was relevant; Recall measures how much of what exists you actually found. The top-K value is the main dial you use to balance them — 3 to 5 is a good starting range for most systems.
- **Hallucination must be actively detected and reduced.** Flag every specific claim in the response, cross-check it against the retrieved document, and design your prompts to force the LLM to use only the provided context. Always instruct the system to say "I don't know" rather than guessing.
- **Evaluation is never finished.** Policies change, products change, and users evolve. Set up a continuous evaluation loop — internally with test datasets, and externally with structured user feedback — and run it at a regular cadence to keep improving your system over time.

**What comes next:** In upcoming sessions, we will step into the world of truly agentic systems — where the AI does not just retrieve and answer, but actively uses tools, makes multi-step decisions, and takes actions across complex workflows.

---

## Important Commands, Libraries, and Terminologies

| Term / Concept | Meaning |
|---------------|---------|
| **RAG (Retrieval-Augmented Generation)** | AI system that retrieves relevant documents from a knowledge base before generating an answer |
| **Retriever** | The component responsible for fetching relevant documents from the vector database |
| **Generator (LLM)** | The language model that generates the final answer using the retrieved context |
| **Grounding** | Ensuring every claim in the answer is directly supported by a retrieved document |
| **Hallucination** | When the LLM generates information that is not present in any retrieved document |
| **Garbage In, Garbage Out** | AI principle: the quality of output is limited by the quality of the input context |
| **Precision** | Out of all retrieved documents, how many are actually relevant? (Relevant Retrieved / Total Retrieved) |
| **Recall** | Out of all relevant documents in the knowledge base, how many did we retrieve? (Relevant Retrieved / Total Relevant) |
| **Top-K** | Parameter controlling how many of the most-similar documents are retrieved from the vector database |
| **Top-K Recall** | Whether the correct answer document appears within the top-K retrieved results |
| **Noise (in RAG)** | Irrelevant documents retrieved alongside relevant ones; they confuse the LLM and reduce quality |
| **Metadata Filtering** | Restricting similarity search to a specific category of documents before retrieval runs |
| **Continuous Evaluation** | Ongoing cycle of testing, scoring, and improving the RAG system after each iteration |
| **Evaluation Dataset** | A set of test queries paired with expected documents and expected correct answers |
| **Structured Feedback** | User feedback collected via star ratings + category-specific follow-up questions |
| **Weak Prompt** | A vague instruction to the LLM with no restrictions on knowledge use — leads to hallucination |
| **Strong Prompt** | A detailed instruction that restricts the LLM to use only provided context and refuse unknown answers |
| **COD (Cash on Delivery)** | Payment method where cash is paid at delivery; has a different and more complex refund process |
| **Embedding Dimensions** | The number of numerical values used to represent a text chunk in vector form (e.g., 1,536 for OpenAI) |
| **Semantic Search** | Search based on meaning similarity using embeddings — not just keyword matching |
| **0–2 Retrieval Score** | Simple scoring scale: 0 = irrelevant, 1 = partially relevant, 2 = fully relevant and complete |
| **0–3 Response Accuracy Score** | Scoring scale for final answer quality: 0 = wrong, 1 = partial, 2 = mostly correct, 3 = fully correct and grounded |
