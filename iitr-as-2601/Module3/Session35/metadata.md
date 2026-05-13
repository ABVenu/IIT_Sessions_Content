lecture ID: 152465

Course Name: Certification in Agentic Systems and Design

Target Audience : Students from any backgorund may not be necessarily form tech background


session duration: 2hr 15 mins

title: GenAI Concepts for Beginners

objective: Learn the terminology of the LLM world.	Where classical ML fails

topics be covered: Intro to Neural Networks intuition; The rise of LLMs, Tokens; Context windows; Hallucinations; Probabilistic text generation


detailed subtopics to be covered:

- Recognise Where Classical ML Falls Short — Recall Module 2 models (regression, classification, clustering, time series) and their shared limitation of needing structured tabular data with fixed features; identify why language tasks like writing an email or translating a sentence cannot be solved with a decision tree or logistic regression;
- Understand Why Language Breaks Classical ML — Explain the word ambiguity problem ("bank" = river or financial institution) to show why features cannot capture meaning; recognise that bag-of-words and keyword matching break with any new phrasing and cannot scale to the complexity of human language;
- Build Intuition for Neural Networks — Connect neural networks to logistic regression already covered in Module 2: one decision layer stacked many times creates a neural network; use the biological neuron metaphor to explain how nodes activate; trace the flow of information through Input → Hidden layers → Output visually without any math; note that every connection has a weight (w) and every neuron has a bias (b) as learnable parameters — instructor to mention at high level;
- Trace the Rise of LLMs — Follow the evolution from Word2Vec (words as vectors) to RNNs (process one word at a time, forget early context) to the Transformer (processes all words simultaneously using attention); understand pre-training as the key shift — learn from a massive slice of the internet once, then adapt to specific tasks — contrasted with classical ML which trains a separate model per task;
- Define and Count Tokens — Define a token as a chunk of text (full word, word-piece, punctuation, or number) and explain why tokenisation converts text into numbers the model can compute on; use a live token counter to count tokens vs. words in a sample sentence; apply the rule of thumb (1 token ≈ 0.75 English words) and recognise that Indian languages tokenise less efficiently than English, which has direct API cost implications;
- Understand Context Windows — Define the context window as the maximum number of tokens an LLM can process in one call — its working memory for that interaction; use the short-term memory analogy to explain what happens when content exceeds the limit; compare sizes across models (4k tokens early, 128k–1M tokens today) and relate this to real tasks like summarising long documents or holding multi-turn conversations;
- Explain Probabilistic Text Generation — Describe how an LLM predicts the most likely next token one at a time rather than looking up a stored answer; use the phone autocomplete analogy to build intuition; explain why the same prompt produces different outputs each time and distinguish LLMs (generate new text) from search engines (retrieve existing documents);
- Apply the Concept of Temperature — Interpret temperature as the control for output randomness: low temperature → precise and predictable, high temperature → creative and varied; choose an appropriate temperature range for different use cases such as a customer support bot (low) vs. a creative writing assistant (high);
- Identify and Mitigate Hallucinations — Define hallucination as the model confidently producing factually wrong or fabricated information; keep explanation short and simple — one real-world example (fake legal case) and brief cause (optimised for plausible tokens not factual accuracy); recognise the higher risk in agentic systems where wrong outputs trigger real-world actions; identify mitigation strategies including RAG, constrained prompts, and human-in-the-loop verification;
