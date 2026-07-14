# Objective Assignment: RAG — Retrieval & Grounded Generation

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

In the five-step RAG loop (ingest → prepare → retrieve → augment → generate), what happens during the **Retrieve** step?

A. Top-k semantic search fetches the nearest stored chunks from the vector index for the user question  
B. The LLM writes the final natural-language answer from memory alone  
C. PDFs are split into fixed-size character windows with overlap  
D. Delimiter tokens are written only inside the Groq API key file

**Correct Answer:** A

**Answer Explanation:**  
A is correct because retrieval embeds the query and runs similarity search to pull the top-k chunk neighbours from Chroma.

B is incorrect because generation happens later, after context is assembled. C is incorrect because chunking belongs to the prepare stage. D is incorrect because delimiters live in prompt messages, not API key storage.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A developer queries a Chroma index with `HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")`, but the index was originally built with `thenlper/gte-large`. Results look unrelated.

What is the **most likely** root cause?

A. Different embedding models at index time vs query time make distance scores meaningless  
B. Chroma cannot store vector indexes for annual-report PDFs  
C. `search_kwargs={"k": 5}` only works on numeric CSV columns  
D. LangChain retrievers cannot wrap a Chroma vector store

**Correct Answer:** A

**Answer Explanation:**  
A is correct because the same-model rule requires one encoder for every stored chunk and every query.

B is incorrect because Chroma routinely stores PDF chunk embeddings. C is incorrect because similarity search runs on text embeddings, not CSV schemas. D is incorrect because `as_retriever()` is the standard LangChain pattern on Chroma.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

A grounded annual-report bot must return the **same factual answer** every time for the same question and retrieved context.

Which Groq API setting best supports that goal?

A. `temperature=0`  
B. `temperature=1.5`  
C. `top_p=0.9` with no temperature field  
D. `search_kwargs={"k": 50}` on the retriever only

**Correct Answer:** A

**Answer Explanation:**  
A is correct because temperature 0 reduces randomness so token choices stay deterministic for factual Q&A.

B is incorrect because high temperature increases creative variation. C is incorrect because sampling randomness still matters for repeatability in RAG facts. D is incorrect because k controls retrieval breadth, not generation randomness.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

A user message is assembled like this:

```
##context
[retrieved chunk 1]
[retrieved chunk 2]
##question
What is the annual revenue in 2022?
```

What is the main purpose of the `##context` and `##question` tokens?

A. They act as delimiter labels so the LLM can separate evidence from the user question  
B. They encrypt chunk text before the Groq API call  
C. They replace the need for a system message with grounding rules  
D. They tell Chroma which collection name to open

**Correct Answer:** A

**Answer Explanation:**  
A is correct because labelled sections help the model parse where context ends and the question begins.

B is incorrect because delimiters are plain text markers, not encryption. C is incorrect because grounding rules such as “answer only from context” still belong in the system message. D is incorrect because collection selection is configured on the vector store, not in the user message tokens.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A Tesla annual-report retriever uses `search_kwargs={"k": 1}`. Users report that answers miss revenue figures mentioned in a **second** section of the report.

What is the **most reasonable first tuning step**?

A. Increase k modestly (for example 3–5) so more relevant passages enter the prompt  
B. Remove the system message to free tokens for more chunk text  
C. Switch only the query embedding to a different model while keeping old document vectors  
D. Set `temperature=1.0` so the model explores more wording options

**Correct Answer:** A

**Answer Explanation:**  
A is correct because low k is fast but can drop a second relevant passage; modestly raising k is the direct retrieval fix.

B is incorrect because removing grounding rules increases hallucination risk. C is incorrect because mixed encoders break semantic distance. D is incorrect because temperature affects generation style, not how many chunks are retrieved.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A user asks a Tesla report bot: *"How many casual leaves do I get in a year?"* The retriever returns weakly related chunks with no leave-policy data.

What should a **properly grounded** RAG system do?

A. Reply that the answer is not in the provided context (for example "I don't know") as instructed in the system message  
B. Use the LLM's general world knowledge to invent a typical leave policy  
C. Delete the vector database and rebuild it from scratch  
D. Return the top retrieved chunk verbatim and skip forming an answer

**Correct Answer:** A

**Answer Explanation:**  
A is correct because grounding rules require refusal when evidence is missing, even if retrieval returns noisy chunks.

B is incorrect because that bypasses the RAG evidence constraint. C is incorrect because the index is not the problem for an out-of-corpus question. D is incorrect because users need a grounded answer or explicit refusal, not a raw chunk dump alone.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A team builds a LangChain retriever on a Chroma store for annual-report chunks.

Which statements are **correct**?

A. `vectorstore.as_retriever(search_kwargs={"k": TOP_K})` configures top-k nearest-neighbour search on embeddings  
B. `retriever.get_relevant_documents(query)` returns top-k `Document` objects with `page_content` and `metadata`  
C. `search_kwargs={"k": TOP_K}` sets how many chunks are retrieved per query  
D. The retriever automatically fine-tunes the Groq LLM on the PDFs each time it is called  
E. Retrieved documents can expose **source** and **page** metadata useful for an informal grounding check

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E match the LangChain + Chroma retrieval pattern used for grounded Q&A.

D is incorrect because retrieval does not fine-tune the generator model; it only fetches chunks.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

After a RAG demo answers *"What is the annual revenue in 2022?"*, an engineer runs an **informal grounding check**.

Which audit steps are **appropriate**?

A. Map each factual claim in the answer to a supporting retrieved chunk  
B. Record page or other metadata from chunks used as evidence  
C. Ask an off-topic question and confirm the model says **I don't know** when context lacks the fact  
D. Trust fluent wording alone without reading the retrieval trace  
E. Compare the retrieval trace printed **before** generation with the final answer

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E are correct informal grounding practices for manual verification.

D is incorrect because fluent answers can still be grounding illusions unsupported by chunk text.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A RAG answer sounds polished and mentions a 2022 revenue figure, but that exact number does **not** appear in any retrieved chunk.

Which responses are **reasonable**?

A. Re-read the retrieval trace and flag claims not supported by chunk text  
B. Strengthen the system message to answer only from the `##context` block  
C. Assume fluent tone proves the retrieval layer is always correct  
D. Check whether noisy retrieval pulled irrelevant chunks and consider tuning k  
E. Skip retrieval and call Groq with only the raw user question to save latency

**Correct Answers:** A, B, D

**Answer Explanation:**  
A, B, and D are correct responses to a grounding illusion: audit evidence, tighten rules, and tune retrieval noise.

C is incorrect because fluency does not prove factual grounding. E is incorrect because skipping retrieval removes the core RAG safety step.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A product team is tuning **k** for a customer-support RAG bot over appliance manuals.

Which statements are **accurate**?

A. Very low k (for example 1) can miss a second page needed for a complete answer  
B. Very high k (for example 100) can add noise, more tokens, and higher latency  
C. Latency matters because end users wait for retrieval plus generation  
D. Raising temperature above 0 is the best first fix when retrieval misses relevant pages  
E. The indexing pipeline (chunk + embed + store) can run ahead of time, while retrieval runs at question time

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A, B, C, and E match the k extremes, latency trade-off, and indexing-vs-retrieval ideas from the lab.

D is incorrect because missing pages are a retrieval / k problem first; temperature controls generation randomness, not which chunks are fetched.
