# Assignment — Subjective (Session 35: Introduction to LangChain)

**Type:** One coding file, **3 tasks** (medium) | **File:** `skillforge_explainer.py` | **Submit:** full file in LMS (**case c**)

**Scenario:** **SkillForge** mentors send lesson briefs as dicts. Build one script: **PromptTemplate → LCEL chain → three runs**. No agents, RAG, or memory.

**Setup:** `pip3 install langchain langchain-openai langchain-core` · `export OPENAI_API_KEY="..."` (never hard-code the key)

---

## Task 1 — Reusable prompt

Define **one** `PromptTemplate` with placeholders `{topic}`, `{audience}`, `{tone}`, `{limit}`. The text must ask the model to:

- explain `{topic}` to `{audience}` in `{tone}` tone  
- include **one real-life analogy**  
- stay within `{limit}` words  

---

## Task 2 — LCEL chain

```python
chain = prompt | llm | output_parser
```

- `llm` = `ChatOpenAI` (any model your key supports)  
- `output_parser` = `StrOutputParser()`  

Add **`validate_brief(brief)`** — raise `ValueError` if any key is missing or if `limit` is not a digit string (e.g. `"120"` OK, `"many"` not).

---

## Task 3 — Run three lessons

Define **`LESSON_BRIEFS`** (exactly 3 dicts; keys must match placeholders):

| topic | audience | tone | limit |
| --- | --- | --- | --- |
| SQL indexes | beginners | simple | 120 |
| FastAPI dependency injection | intermediate developers | technical | 180 |
| LangChain PromptTemplate | product managers | friendly | 100 |

For each brief: print `=== Lesson: <topic> ===` → `validate_brief` → `chain.invoke(brief)` → print result → print `Length: <n> chars`.

**Rules:** one template only (no three hard-coded prompts); use `chain.invoke`, not manual `format()` + `client.invoke`.

---

## Submission (**case c**)

Single `skillforge_explainer.py` in VS Code → run once (3 lessons print) → paste full file into the LMS answer box.

---

## Answer explanation (Assess)

**Pass:** Task 1 template + 4 instructions · Task 2 `prompt | llm | StrOutputParser` · Task 3 table data, validation, loop output · env key only.

**Fail:** `word_count` instead of `limit`; no parser (object not string); three separate prompt strings.

**Reference (evaluators)**

```python
import os, re
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

KEYS = ("topic", "audience", "tone", "limit")
prompt = PromptTemplate.from_template(
    """Explain {topic} to {audience} with these requirements:
- Use {tone} tone
- Give one real-life analogy to explain the concept
- Keep the response within {limit} words"""
)
chain = prompt | ChatOpenAI(model="gpt-4o-mini") | StrOutputParser()

LESSON_BRIEFS = [
    {"topic": "SQL indexes", "audience": "beginners", "tone": "simple", "limit": "120"},
    {"topic": "FastAPI dependency injection", "audience": "intermediate developers", "tone": "technical", "limit": "180"},
    {"topic": "LangChain PromptTemplate", "audience": "product managers", "tone": "friendly", "limit": "100"},
]

def validate_brief(brief: dict) -> None:
    missing = [k for k in KEYS if k not in brief]
    if missing:
        raise ValueError(f"Missing keys: {', '.join(missing)}")
    if not str(brief["limit"]).isdigit():
        raise ValueError(f"limit must be numeric string, got {brief['limit']!r}")

if __name__ == "__main__":
    if not os.environ.get("OPENAI_API_KEY"):
        raise ValueError("Set OPENAI_API_KEY")
    for b in LESSON_BRIEFS:
        print(f"=== Lesson: {b['topic']} ===")
        validate_brief(b)
        r = chain.invoke(b)
        print(r)
        print(f"Length: {len(r)} chars\n")
```

---

**End of subjective assignment.**
