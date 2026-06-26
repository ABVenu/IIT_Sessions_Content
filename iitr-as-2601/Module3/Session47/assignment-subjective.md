# Subjective Assignment: Explain a RAG Support Assistant

## Written Task (Medium)

A company sells electronic products. It has many product manuals and policy documents. The company wants to build a support assistant where customers can ask questions like:

- "What should I do if my device shows an error code?"
- "Is this repair covered under warranty?"
- "How many days will delivery take?"

Write a simple explanation of how a RAG-based support assistant should work for this company.

### What to include in your answer

Write your answer in simple English and cover all the points below:

1. What is the **document corpus** in this example?
2. Why should the documents be split into **chunks**?
3. Why are **embeddings** and a **vector database** needed?
4. How does **retrieval** help before the LLM writes the answer?
5. What should the assistant do if the answer is **not found** in the documents?
6. Why is **groundedness** important for this support assistant?
7. Mention any **two possible failure points** in this RAG system.
8. Explain how the company can check answer quality using **groundedness** and **relevance**.

### Expected Answer Length

Write around **250 to 350 words**.

### Submission Instruction

- Type the answer in the answer box.

---

## Answer Explanation

### Ideal Solution Walkthrough

A good answer should explain the RAG flow in simple words. It should not describe RAG as a normal chatbot. It should clearly say that the assistant must first search the company's documents and then answer only from the retrieved content.

The answer should mention that product manuals and policy documents form the document corpus. These documents are split into chunks because large documents are difficult to search and use directly. Each chunk is converted into embeddings and stored in a vector database so that similar chunks can be found when a customer asks a question.

The answer should explain that retrieval brings the most relevant chunks before the LLM writes the final answer. If the required information is not in the retrieved documents, the assistant should politely say that it could not find the answer instead of guessing. This is important because customers may use the answer to take real action, such as claiming warranty or fixing a device.

The answer should also mention two failure points, such as poor chunking, weak embeddings, stale vector database, retrieving too few or too many chunks, or unclear system message. For evaluation, groundedness checks whether the answer is supported by the retrieved context, while relevance checks whether the answer actually answers the user's question.

### Sample Answer

For this company, the document corpus is the collection of product manuals, warranty policies, delivery policies, and repair instructions. These are the only documents the support assistant should use to answer customer questions.

The documents should be split into chunks because manuals can be very long. Smaller chunks make it easier to find the exact part that talks about an error code, warranty rule, or delivery timeline. Each chunk is converted into embeddings, which are numbers that represent the meaning of the text. These embeddings are stored in a vector database so that the system can search by meaning, not only by exact words.

When a customer asks a question, the system first retrieves the most relevant chunks from the vector database. Then the LLM uses those chunks as context and writes the answer. This is better than a normal chatbot because the answer is based on company documents.

If the answer is not found in the documents, the assistant should say that it could not find the answer in the provided documents. It should not guess. Groundedness is important because customers may depend on the answer for warranty, repair, or product safety decisions.

Two possible failure points are poor chunking and a stale vector database. Poor chunking may hide the correct information, and a stale database may miss new or updated documents. The company can check quality using groundedness and relevance. Groundedness checks whether the answer is supported by the retrieved chunks. Relevance checks whether the answer is actually related to the customer's question.
