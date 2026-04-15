# Pre-read: Introduction to Vector Databases

## The hook

Imagine you run a support desk and a customer describes a problem in their own words. You do not have a perfect keyword for it, but you have seen something *like* this before. Your brain matches *meaning*, not just spelling. Modern AI systems face the same situation millions of times a day: find the closest match when the question is fuzzy, long, or phrased in many different ways. Storing and finding information by *similarity* is now a core skill for anyone building search, recommendations, or assistants.

## The problem

**What if** you had to help a user find the right document, product, or answer from crores of items—and “close enough” is more useful than “exactly the same words”? Doing this by hand, or by scanning every row one by one, breaks down as soon as the collection grows. You need a way for the machine to organise *meaningful nearness* and fetch good options quickly, not only when the text matches letter for letter.

## The solution preview

This session introduces **vector databases**: systems built to store **embeddings** (think of them as compact numeric “fingerprints” of meaning) and to **retrieve** items that are *semantically* close to a query. We will see why ordinary relational databases are a poor fit for this job, how **similarity search** works at a high level, and why **vector indexing** and **approximate nearest neighbour (ANN)** search matter when speed and scale both matter.

## A simple analogy

Picture a huge library where books are not shelved alphabetically by title, but by *topic nearness*: books on similar ideas sit nearer to each other. When someone describes what they need in plain language, you walk to the “region” of the shelf where that meaning lives and pick the closest few volumes. Vector databases do something like that for embeddings—organising space so “near” means “similar in meaning,” not “same spelling.”

## Key terms

- **Embedding:** A way to turn text (or other content) into a list of numbers so the computer can compare “closeness” of meaning.
- **Similarity search:** Finding the best matches by nearness in that meaning-space, not by exact string match.
- **Vector indexing / ANN:** Smart shortcuts so the system does not compare every item to every other item when the dataset is massive—trading a little perfection for a lot of speed.

## Questions we will answer in the session

1. Why do normal databases struggle when the goal is “find things like this” rather than “find this exact key”?
2. How does a query turn into a search for *nearby* vectors, and what role do indexing and ANN play?
3. Where do vector databases show up in real products—from search and recommendations to agents that need memory and context?

## What’s next (after this session)

You will be able to:

- Explain why **embeddings** and **similarity retrieval** sit at the heart of many AI features.
- Contrast **exact match** search with **semantic / similarity** search in everyday terms.
- Describe **vector indexing** and **ANN** as the bridge between “correct enough” answers and **fast** answers at scale.
- Connect vector databases to **semantic search**, **recommendations**, **conversational systems**, and **agentic** workflows that need quick, relevant context.
