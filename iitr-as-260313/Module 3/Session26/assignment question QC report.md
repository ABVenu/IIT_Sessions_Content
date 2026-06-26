# Assignment Question QC Report

## Question-Level QC

| Question Number | Type | Remarks |
|---|---|---|
| Q1 | MCQ - Easy | Correct option: B. Relevancy: Yes. Tests LangChain definition and purpose through a helpdesk chatbot scenario. Incorrect options are clearly unrelated. |
| Q2 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests LangChain stack placement between model provider and application logic. Incorrect options are not plausible roles for LangChain. |
| Q3 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests PromptTemplate as the reusable prompt solution. Incorrect options do not solve repeated prompt editing. |
| Q4 | MCQ - Easy | Correct option: A. Relevancy: Yes. Tests Runnable as input-work-output component. Incorrect options are unrelated. |
| Q5 | MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests LCEL pipe operator and chain order. Incorrect options do not describe pipe behavior. |
| Q6 | MCQ - Moderate | Correct option: A. Relevancy: Yes. Tests StrOutputParser for predictable string output. Incorrect options do not parse LangChain model output. |
| Q7 | MSQ - Moderate | Correct options: A, B, C. Relevancy: Yes. Tests when LangChain is useful compared with one-off raw API scripts. Option D is correctly excluded because LangChain still uses code. |
| Q8 | MSQ - Moderate | Correct options: A, B, D. Relevancy: Yes. Tests Core/package/provider-package understanding for a minimal Ollama chain. Option C is correctly excluded because community integrations are optional, not required for every minimal flow. |
| Q9 | MSQ - Hard | Correct options: A, B, C. Relevancy: Yes. Tests module-role mapping for tools, memory, and retrievers. Option D is correctly excluded because PromptTemplate does not store memory. |
| Q10 | MSQ - Hard | Correct options: A, B, D. Relevancy: Yes. Tests LangChain vs build-from-scratch tradeoffs. Option C is correctly excluded because developers still need conceptual understanding. |
| Subjective | Practical Task - Medium | Medium difficulty: Yes. Clear submission instructions: Yes. Dataset needed: No. Task stays within covered coding flow: PromptTemplate, ChatOllama, StrOutputParser, LCEL pipe, and `chain.invoke`. It avoids surface-level-only topics such as agents, tools, memory, retrievers, and vector DB implementation. |

## Overall QC

| Criterion | Rating / Result | Remarks |
|---|---|---|
| Content Coverage | 5 / 5 | Covers LangChain definition, framework need, stack placement, Runnable/chains, modules overview, Core vs provider packages, PromptTemplate, LCEL, output parsers, Ollama setup, and first chain implementation. |
| Creativity | 5 / 5 | Questions use practical contexts such as helpdesk chatbot, support chatbot, architecture decisions, setup debugging, and reusable explanation assistant. |
| Structural Adherence | 5 / 5 | Objective assignment has exactly 10 questions: 6 MCQs and 4 MSQs, ordered Easy -> Moderate -> Hard. Subjective assignment has exactly 1 medium practical task. |
| No Logical Mistakes | True | Correct answers are valid and explanations clearly justify why alternatives are wrong. |
| No Presentation Mistakes | True | Files are named correctly, questions are self-contained, and formatting is consistent. |

## Final QC Outcome

PASS - Expected QC result achieved. No modification required.
