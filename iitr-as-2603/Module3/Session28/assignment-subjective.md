# Subjective Assignment: Build a Mini Text Embedding Explorer

## Practical Task

**Difficulty:** Medium

A support team wants to understand how text becomes vectors before they connect those vectors to a vector database. Create a single Python file named `embedding_explorer.py` that converts short support-related sentences into embeddings and prints a clean summary.

### Requirements

Your script must:

1. Use the `sentence-transformers` library.
2. Load the model `sentence-transformers/all-MiniLM-L6-v2`.
3. Create a list with exactly these four sentences:
   - `How do I return a product?`
   - `What is the refund policy?`
   - `When is the Module 3 capstone viva?`
   - `Refunds are processed within seven working days.`
4. Convert all four sentences into embeddings.
5. For each sentence, print:
   - The sentence text.
   - The vector length.
   - The first 5 numbers of the vector.
6. Print a final 2-3 line explanation of what a RAG system would do with these vectors later.

### Expected Output Format

Your exact numeric values may differ slightly depending on the environment, but the structure should look like this:

```text
--- Mini Text Embedding Explorer ---
Sentence: How do I return a product?
Vector length: 384
First 5 numbers: [...]

Sentence: What is the refund policy?
Vector length: 384
First 5 numbers: [...]

Sentence: When is the Module 3 capstone viva?
Vector length: 384
First 5 numbers: [...]

Sentence: Refunds are processed within seven working days.
Vector length: 384
First 5 numbers: [...]

--- RAG Connection ---
Each sentence can become a document chunk in a RAG library.
The embeddings can later be stored in a vector database.
When a user asks a question, similar chunks can be retrieved and added to the prompt.
```

### Submission Instructions

- Code all the points mentioned in VS Code in a single `.py` file.
- Run the code and verify it is working.
- Submit the code in the code editor/answer box in the LMS.

---

## Answer Explanation

### Ideal Solution Walkthrough

The script loads a ready-made Hugging Face embedding model through the `sentence-transformers` library. It passes four text sentences to the model and receives one numeric vector for each sentence.

The vector length should be 384 because the selected model maps each sentence into a 384-dimensional vector. The first 5 numbers are printed only as a sample because printing all 384 values for every sentence would be hard to read.

In a later RAG system, these sentence vectors would be stored in a vector database. A user question would also be converted into an embedding, and the system would retrieve the closest matching chunks before adding them to the prompt.

### Complete Code

```python
from sentence_transformers import SentenceTransformer  # Import the class used to load embedding models.

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"  # Store the model name in one place for easy reuse.

sentences = [  # Create the exact text inputs required for this task.
    "How do I return a product?",  # Sentence about product returns.
    "What is the refund policy?",  # Sentence about a related refund topic.
    "When is the Module 3 capstone viva?",  # Sentence about a different academic topic.
    "Refunds are processed within seven working days.",  # Sentence containing a specific refund fact.
]  # End the sentence list.

model = SentenceTransformer(MODEL_NAME)  # Load the embedding model from the Hugging Face ecosystem.
embeddings = model.encode(sentences)  # Convert every sentence into one embedding vector.

print("--- Mini Text Embedding Explorer ---")  # Print a clear heading for the output.

for sentence, vector in zip(sentences, embeddings):  # Pair each original sentence with its vector.
    print("Sentence:", sentence)  # Print the original text.
    print("Vector length:", len(vector))  # Print how many numbers are inside the vector.
    print("First 5 numbers:", vector[:5])  # Print a small sample instead of the full vector.
    print()  # Add a blank line after each sentence block.

print("--- RAG Connection ---")  # Print a heading for the concept connection.
print("Each sentence can become a document chunk in a RAG library.")  # Connect sentences to chunks.
print("The embeddings can later be stored in a vector database.")  # Explain where vectors can be stored.
print("When a user asks a question, similar chunks can be retrieved and added to the prompt.")  # Explain retrieval and augmentation.
```

### Alternative Approaches

- The sentences can be stored in a tuple instead of a list, but a list is simpler for beginners.
- The first 3 or first 10 vector values can be printed for exploration, but the task asks for the first 5.
- Another embedding model can be used for experimentation, but the required solution must use `sentence-transformers/all-MiniLM-L6-v2` so that the expected vector length is 384.
