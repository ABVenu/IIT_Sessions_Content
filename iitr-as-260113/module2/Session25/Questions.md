## Session 25 - Questions

### Q1. Which of the following best describes semantic search?

- A. Searching only exact words  
- B. Searching based on meaning and intent  
- C. Searching only numbers  
- D. Searching only database keys  

**Answer:** B

### Q2. Why are embeddings useful in AI systems?

- A. They make code shorter  
- B. They convert meaning into a machine-friendly form  
- C. They replace all databases  
- D. They store only exact keywords  

**Answer:** B

### Q3. Which of the following is a good example of semantic similarity?

- A. "Laptop" and "banana"  
- B. "Doctor" and "hospital"  
- C. "Car" and "moon"  
- D. "Chair" and "water"  

**Answer:** B

### Q4. If two sentence embeddings are very close in vector space, what does it usually mean?

- A. The sentences are long  
- B. The sentences are grammatically wrong  
- C. The sentences are semantically similar  
- D. The sentences are written by the same person  

**Answer:** C

### Q5. Which of the following is a semantic search use case?

- A. Matching order ID exactly  
- B. Finding a help article with similar meaning  
- C. Sorting numbers  
- D. Creating a database schema  

**Answer:** B

### Q6. In semantic search, stored documents are often:

- A. Converted into vectors beforehand  
- B. Deleted after retrieval  
- C. Stored only as images  
- D. Converted into audio files  

**Answer:** A

### Q7. In an AI agent, embeddings can help retrieve:

- A. Random files only  
- B. Only exact matching words  
- C. Only the latest message  
- D. Relevant past memories or context  

**Answer:** B

### Q8. Why are embeddings called vector representations?

- A. Because they are stored in folders  
- B. Because they are always two-dimensional  
- C. Because they are written in English  
- D. Because they are represented as lists of numerical values  

**Answer:** D

### Q9. Which of the following would likely have similar embeddings?

- A. "Book a cab" and "Reserve a taxi"  
- B. "Learn Python" and "Buy a refrigerator"  
- C. "Hospital" and "football"  
- D. "Table" and "planet"  

**Answer:** A

### Q10. Subjective Question

A company has a help center with many support articles. Users often ask questions in different words.

**Example:**
- **User query:** "How can I get my money back?"  
- **Help article title:** "Steps to request a refund"  

A keyword-based search system is not always able to return the correct article.

**Question:**  
**Explain** how vector embeddings and semantic search can solve this problem.  
Also **describe** the step-by-step workflow of how a semantic search system would **process** the user query and **retrieve** the correct result.

**Submission instruction:** Type the answer in the answer box after the question content.

**Sample solution:**
Vector embeddings convert text into numerical vectors that capture meaning, not just exact words. Because of this, the query "How can I get my money back?" and the article "Steps to request a refund" become close in vector space, even though they use different wording. Semantic search compares meanings, so it can return the correct article more reliably than keyword-only search.

A typical semantic search workflow is:
1. Collect and preprocess all help-center articles.
2. Generate embeddings for each article using an embedding model.
3. Store these vectors in a vector database/index.
4. When a user asks a question, generate an embedding for the query.
5. Run a similarity search (for example, cosine similarity) between the query vector and stored article vectors.
6. Retrieve the top-k most similar articles.
7. Optionally re-rank results and return the best article(s) to the user.
