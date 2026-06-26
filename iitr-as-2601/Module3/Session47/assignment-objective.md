# Objective Assignment: End-to-End RAG Application

## Multiple Choice Questions (Single Correct)

### Q1. Easy

A support assistant first searches company documents and then asks an LLM to answer only from the searched content. What is this approach called?

A. Normal chatbot  
B. Retrieval-Augmented Generation  
C. Image classification  
D. Database backup  

**Correct Answer:** B

**Answer Explanation:**  
Retrieval-Augmented Generation, or RAG, first retrieves useful document chunks and then generates an answer using those chunks. A normal chatbot may answer from model memory without checking documents. Image classification and database backup are unrelated to this question.

---

### Q2. Easy

In a RAG application, what is a document corpus?

A. The set of source documents the assistant is allowed to search  
B. The password used for an API key  
C. The final answer given by the LLM  
D. The web page design of the app  

**Correct Answer:** A

**Answer Explanation:**  
A document corpus is the collection of documents used as the knowledge source for the RAG app. An API key, final answer, and web page design are different parts of an application, but they are not the corpus.

---

### Q3. Easy

Why are large documents split into chunks before storing them in a vector database?

A. To make them easier to retrieve in smaller meaningful parts  
B. To delete all useful information  
C. To avoid using embeddings  
D. To convert the document into an image  

**Correct Answer:** A

**Answer Explanation:**  
Chunking breaks a large document into smaller parts so the retriever can find the most relevant pieces for a question. It does not delete useful information, avoid embeddings, or convert text into images.

---

### Q4. Easy

What does grounded generation mean in a RAG system?

A. The model answers only using the retrieved context  
B. The model writes any answer from memory  
C. The model refuses every question  
D. The model stores files on a local computer  

**Correct Answer:** A

**Answer Explanation:**  
Grounded generation means the answer must come from the retrieved context. If the answer is not present in the context, the assistant should say that it could not find the answer instead of inventing one.

---

### Q5. Moderate

A user asks, "Can I pay with UPI?" The policy documents do not mention UPI. What should a well-designed RAG assistant do?

A. Guess that UPI is allowed  
B. Say that the answer is not found in the provided documents  
C. Search the internet automatically  
D. Give a random payment policy  

**Correct Answer:** B

**Answer Explanation:**  
A grounded RAG assistant should not invent an answer. If the retrieved context does not contain UPI information, it should clearly say that the answer is not found in the provided documents. Guessing, random answers, or internet search would break the grounding rule.

---

### Q6. Moderate

Which statement best explains why retrieving too many chunks can be a problem?

A. It can increase cost and may send more private data to the LLM  
B. It always improves answer quality  
C. It removes the need for a system message  
D. It stops the vector database from storing embeddings  

**Correct Answer:** A

**Answer Explanation:**  
Too many retrieved chunks increase the amount of context sent to the LLM. This can increase token cost and may expose more private information than needed. More chunks do not always improve quality, and they do not remove the need for prompts or embeddings.

---

## Multiple Select Questions (Multiple Correct)

### Q7. Moderate

Which of the following are main stages in a RAG pipeline?

A. Select or load documents  
B. Chunk documents and create embeddings  
C. Retrieve relevant chunks for a user question  
D. Ignore the retrieved context and answer from memory  

**Correct Answers:** A, B, C

**Answer Explanation:**  
A RAG pipeline starts with documents, chunks them, embeds them, stores them, and retrieves relevant chunks before generation. Option D is wrong because ignoring retrieved context would make the answer ungrounded.

---

### Q8. Moderate

Which checks help test whether a RAG answer is grounded?

A. Check whether important claims appear in the retrieved chunks  
B. Check whether the answer cites or uses the correct source information  
C. Ask one question that is not present in the corpus and expect a refusal  
D. Accept every fluent answer as correct  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Grounding means the answer should be supported by the retrieved context. Checking claims, sources, and not-in-corpus behavior helps test this. A fluent answer can still be wrong or invented, so option D is incorrect.

---

### Q9. Hard

Which of the following can be points of failure in a RAG system?

A. Poor chunking strategy  
B. Weak embedding model  
C. Stale vector database or missing metadata  
D. Clear grounding rules in the system message  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Poor chunking, weak embeddings, and stale or badly managed vector data can all cause wrong retrieval and wrong answers. Clear grounding rules are helpful, not a failure point. Unclear grounding rules would be the failure.

---

### Q10. Hard

Which statements about RAG evaluation are correct?

A. Groundedness checks whether the answer is supported by the retrieved context  
B. Relevance checks whether the answer is related to the user question  
C. Context relevance checks whether retrieved chunks are useful for the question  
D. RAG evaluation is never needed if the app runs without errors  

**Correct Answers:** A, B, C

**Answer Explanation:**  
Groundedness, relevance, and context relevance are important ways to evaluate a RAG system. Together, they are often discussed as the RAG Triad. Option D is wrong because an app can run without errors and still give incorrect or ungrounded answers.
