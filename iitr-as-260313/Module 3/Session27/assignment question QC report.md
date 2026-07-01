# Assignment Question QC Report

## Question-Level QC

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests virtual environment purpose through a two-project version-conflict scenario. Incorrect options misstate what `venv` does. |
| Q2 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests `.env` must not be committed because it may contain secrets. Other listed files are normal shared project files. |
| Q3 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests `python-dotenv` / `load_dotenv()` role. Incorrect options confuse core LangChain and Ollama packages with env loading. |
| Q4 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests `StrOutputParser` as the fix when chain output is an `AIMessage` object. Other options do not address output type conversion. |
| Q5 | MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests `ChatPromptTemplate.from_messages()` for system + human role prompts. Option B incorrectly uses `from_template()` with role tuples. |
| Q6 | MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests LCEL left-to-right execution on a realistic `invoke` input. Option B reverses pipe order; C and D are implausible. |
| Q7 | MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests safe collaborative worktree practices (`.gitignore`, `.env.example`, `requirements.txt`). Option C is correctly excluded as unsafe. |
| Q8 | MSQ - Moderate | Correct options: A, B, C. Relevancy: Yes. Tests minimal package stack for local LCEL chain with `.env`. Option D is correctly excluded for Ollama-only local setup. |
| Q9 | MSQ - Hard | Correct options: A, B, C. Relevancy: Yes. Tests LCEL data flow across prompt, LLM, and parser. Option D is correctly excluded because pipe order is not reversed. |
| Q10 | MSQ - Hard | Correct options: A, B, C. Relevancy: Yes. Tests `load_dotenv` ordering, temperature behaviour, and basic validation. Option D is correctly excluded because committing `.env` is unsafe. |
| Subjective | Practical Task - Medium | Medium difficulty: Yes. Clear submission instructions (case c — single `.py` file in LMS code box): Yes. Dataset needed: No. Task stays within covered implementation: `load_dotenv`, `.env` config, `ChatPromptTemplate.from_messages()`, `ChatOllama`, `StrOutputParser`, LCEL pipe, two `invoke` test cases, and basic validation. Does not require full GitHub worktree submission or surface-only provider-swapping implementation. |

## Overall QC

| Criterion | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 / 5 | Covers venv purpose, `.env` / `.gitignore` / `requirements.txt`, `python-dotenv`, `ChatPromptTemplate`, `ChatOllama`, LCEL pipe order, `StrOutputParser`, configuration loading, temperature, validation, and first-chain troubleshooting concepts from the released notes. |
| Creativity | 5 / 5 | Questions use practical contexts such as two-project setup, GitHub collaboration, campus study buddy app, and realistic chain-debugging scenarios. |
| Structural Adherence | 5 / 5 | Objective assignment has exactly 10 questions: 6 MCQs (4 Easy, 2 Moderate) and 4 MSQs (2 Moderate, 2 Hard), ordered Easy → Moderate → Hard. Subjective assignment has exactly 1 medium practical task. |
| No Logical Mistakes | True | Correct answers are valid; explanations justify incorrect options. Subjective solution matches requirements and runs with local Ollama. |
| No Presentation Mistakes | True | Files named correctly, no session-reference phrasing in questions, self-contained prompts, and consistent formatting. |

## Final QC Outcome

PASS — Expected QC result achieved. No modification required.
