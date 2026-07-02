# Objective Assignment: RAG Foundations

## Instructions

- Questions 1 to 6 are **MCQs**. Choose **one correct option**.
- Questions 7 to 10 are **MSQs**. Choose **all correct options**.
- The questions are ordered from Easy to Moderate to Hard.

---

## Question 1

**Type:** MCQ  
**Difficulty:** Easy

A learner asks an LLM, "What is the refund rule for our company's May 2026 training batch?" The rule exists only in an internal PDF and was updated yesterday.

What is the main risk if the LLM is used without giving it that PDF text?

A. The LLM will automatically search the company's private PDF folder.  
B. The LLM may give a confident answer based on old or general patterns.  
C. The LLM will always refuse to answer any policy-related question.  
D. The LLM will permanently store the company's latest rule after one question.

**Correct Answer:** B

**Answer Explanation:**  
B is correct because an LLM does not automatically know private documents or very recent changes unless that information is provided in the prompt or retrieved through a system like RAG. It may still produce a fluent answer, but the answer can be outdated or invented.

A is incorrect because an LLM does not automatically access private company folders. C is incorrect because LLMs may answer policy questions, but the answer may be unreliable without context. D is incorrect because asking one question does not permanently update the model's training memory.

---

## Question 2

**Type:** MCQ  
**Difficulty:** Easy

A college helpdesk wants an AI assistant to answer questions from its admission handbook. Before generating an answer, the assistant should first find the relevant handbook paragraph and add it to the prompt.

Which idea best describes this approach?

A. Fine-tuning  
B. Retrieval-Augmented Generation  
C. Random text generation  
D. Image classification

**Correct Answer:** B

**Answer Explanation:**  
B is correct because Retrieval-Augmented Generation, or RAG, means searching an external knowledge source, retrieving relevant context, adding it to the prompt, and then generating the answer.

A is incorrect because fine-tuning changes model weights using training examples, while RAG keeps the model fixed and supplies fresh context. C is incorrect because RAG is not random; it uses retrieved evidence. D is incorrect because the scenario is about text retrieval and answer generation, not classifying images.

---

## Question 3

**Type:** MCQ  
**Difficulty:** Easy

A team tries to paste a 300-page policy manual into one prompt, but the model cannot accept the full input.

Which limitation are they most likely hitting?

A. Context window limit  
B. File name conflict  
C. GPU temperature limit  
D. Password length limit

**Correct Answer:** A

**Answer Explanation:**  
A is correct because the context window is the maximum amount of input text a model can handle in one prompt. Large documents may exceed that limit, so RAG retrieves only the relevant portions.

B is incorrect because the issue is not about duplicate file names. C is incorrect because the prompt size problem is unrelated to hardware temperature. D is incorrect because password length has nothing to do with model input size.

---

## Question 4

**Type:** MCQ  
**Difficulty:** Easy

An assistant receives this instruction:

```text
Answer only using the Context below. If the answer is not in the Context, say you could not find it in the documents.
```

What concept does this instruction mainly support?

A. Grounding  
B. Model compression  
C. Web scraping  
D. Tokenization only

**Correct Answer:** A

**Answer Explanation:**  
A is correct because grounding means the answer should stay supported by the supplied context instead of inventing facts.

B is incorrect because the instruction does not reduce model size. C is incorrect because it does not collect data from websites. D is incorrect because tokenization is about splitting text into model-readable pieces, not about forcing answers to follow context.

---

## Question 5

**Type:** MCQ  
**Difficulty:** Moderate

A small RAG prototype has these actions:

1. Load company FAQs.
2. Clean and split the FAQs into chunks.
3. Convert chunks into embeddings and store them in an index.
4. Find chunks related to a user's question.
5. Add those chunks to the prompt.
6. Generate the final answer.

Which option correctly maps the broad RAG flow?

A. Generate -> Ingest -> Retrieve -> Prepare -> Augment  
B. Ingest -> Prepare -> Retrieve -> Augment -> Generate  
C. Prepare -> Generate -> Ingest -> Augment -> Retrieve  
D. Retrieve -> Generate -> Prepare -> Ingest -> Augment

**Correct Answer:** B

**Answer Explanation:**  
B is correct because the conceptual RAG flow is: ingest documents, prepare them by cleaning/chunking/embedding, retrieve relevant chunks, augment the prompt with those chunks, and generate the final answer.

A, C, and D are incorrect because they put generation or retrieval before the document library has been ingested and prepared. Retrieval can only work after useful document chunks have been prepared and indexed.

---

## Question 6

**Type:** MCQ  
**Difficulty:** Moderate

A product-support assistant gives a wrong warranty answer even though the correct warranty paragraph exists in the company's document library. The model wrote a fluent answer from general knowledge instead of using the retrieved paragraph.

Which part of the system most directly needs improvement?

A. The grounding instruction in the prompt  
B. The spelling of the product name in the final answer only  
C. The color theme of the chat interface  
D. The number of headings in the PDF

**Correct Answer:** A

**Answer Explanation:**  
A is correct because if relevant context is available but the model ignores it, the prompt should more strongly instruct the model to answer from the provided context and admit when the answer is not present.

B is incorrect because spelling alone does not fix unsupported reasoning. C is incorrect because UI color has no effect on whether the model follows context. D is incorrect because headings may help document structure, but the described failure is mainly about using the supplied context during answer generation.

---

## Question 7

**Type:** MSQ  
**Difficulty:** Moderate

A startup wants to build a company-policy assistant using RAG instead of sending the full policy handbook to the LLM for every question.

Which benefits are reasonable expectations from this design?

A. It can reduce token usage by sending only relevant chunks.  
B. It can help keep private information more controlled by not pasting every document into every prompt.  
C. It guarantees that the model will never make any mistake.  
D. It makes policy updates easier because the document library can be updated.  
E. It removes the need for retrieval because the LLM already knows all company documents.

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because RAG can send only the most relevant chunks instead of the full handbook, reducing token usage. B is correct because fewer documents need to be exposed in each prompt, which supports better privacy handling. D is correct because updating the external document library is easier than retraining a model for every policy change.

C is incorrect because RAG reduces guessing but does not guarantee perfect answers. E is incorrect because retrieval is the key step that brings relevant company documents into the prompt.

---

## Question 8

**Type:** MSQ  
**Difficulty:** Moderate

A learner creates embeddings for these sentences:

- "How do I return a product?"
- "What is the refund policy?"
- "When is the Module 3 capstone viva?"

Which statements are correct?

A. Each sentence becomes a numeric vector.  
B. Similar meanings should generally be closer in vector space.  
C. The numbers are easy for humans to read one by one as plain English.  
D. These vectors can later be stored in a vector database.  
E. Embeddings are used only for images and never for text.

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because an embedding represents text as a list of numbers. B is correct because embeddings are designed so that texts with similar meaning are closer in mathematical space. D is correct because RAG systems can store document or chunk embeddings in a vector database for later search.

C is incorrect because individual numbers are not directly meaningful to humans; the vector as a whole represents meaning. E is incorrect because embeddings are commonly used for text as well as other data types.

---

## Question 9

**Type:** MSQ  
**Difficulty:** Hard

A company is planning the first version of an internal RAG assistant. The team wants to stay within a beginner-friendly scope and avoid building a complete production system immediately.

Which design choices match that scope?

A. First compare an LLM answer without document access against an answer where relevant document text is supplied in the prompt (paste or upload).  
B. Start with a small embeddings demo that converts a few sentences into vectors.  
C. Build a full production RAG pipeline with advanced chunk-size tuning, top-k experiments, monitoring, and failure drills on day one.  
D. Explain that vector databases will later store embeddings and retrieve similar chunks.  
E. Claim that fine-tuning is always better than RAG for changing policy documents.

**Correct Answers:** A, B, D

**Answer Explanation:**  
A is correct because comparing answers without document access against answers with supplied document context proves the core RAG idea without building the full app — whether context is pasted or uploaded. B is correct because creating embeddings for a few sentences is a suitable beginner-friendly hands-on step. D is correct because it correctly bridges embeddings to vector databases and future retrieval.

C is incorrect because it goes beyond the beginner conceptual scope and includes advanced production work. E is incorrect because RAG is usually a better starting point for changing facts in documents, while fine-tuning is more about changing model behavior, tone, or patterns.

---

## Question 10

**Type:** MSQ  
**Difficulty:** Hard

A support assistant has two components:

- Component X searches the document library and returns two paragraphs related to the user's question.
- Component Y writes the final answer using those paragraphs.

Which statements correctly describe this setup?

A. Component X is acting as the retriever.  
B. Component Y is acting as the generator.  
C. Grounding means Component Y should answer from the supplied paragraphs when the fact is present there.  
D. If the answer is not in the supplied paragraphs, a grounded assistant should confidently invent the most likely answer.  
E. The retrieved paragraphs are added to the prompt during the augment step.

**Correct Answers:** A, B, C, E

**Answer Explanation:**  
A is correct because the retriever finds relevant information from the document library. B is correct because the generator writes the final answer. C is correct because grounding means the answer should follow the supplied evidence. E is correct because the augment step adds retrieved context to the prompt before generation.

D is incorrect because a grounded assistant should not invent missing facts. It should say that the answer could not be found in the provided context or documents.
