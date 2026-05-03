# Lecture Notes QC Report — Session 13: Short-Term vs Long-Term Memory

---

## Iteration 1

**Date:** 2026-05-02

### QC Scores

| Criteria | Rating / Result |
|---|---|
| **Content Coverage** | 5 / 5 |
| **Creativity** | 5 / 5 |
| **Structural Adherence** | 5 / 5 |
| **No Logical Mistakes** | True |
| **No Presentation Mistakes** | True |

### Detailed Remarks

**Content Coverage (5/5):**
All 8 detailed subtopics from the session metadata are fully addressed:
- Memory role recap and why it enables continuity, personalisation, and better decisions ✓
- Short-Term vs Long-Term Memory differentiation with comparison table ✓
- Conversation history as short-term memory — context window mechanics explained step-by-step ✓
- Three limitations of context-window-based memory (token limits, increasing cost, performance degradation) ✓
- All three short-term memory strategies (Buffer, Window, Summary) with definitions, use cases, risks, and pseudo-code ✓
- All three long-term memory types (Episodic, Semantic, Procedural) with definitions, examples, and storage methods ✓
- Pseudo-implementations of all three strategies with full code and "How the code works" explanations ✓
- Memory selection logic (relevance vs recency, four selection approaches) and storage awareness section ✓
Content depth is appropriate for a 2-hour 15-minute session.

**Creativity (5/5):**
- Diverse, relatable analogies used throughout — customer care notepad, doctor's patient file, library desk, cricket commentator, journalist's Day-10 recap, Ravi in Pune, whiteboard with 100 words, legal AI agent
- Connecting sentences bridge every major section to the next without abrupt jumps
- Plain Indian English maintained consistently — conversational, warm, and approachable
- The library analogy in the context section (previous session = knowing the library exists; this session = learning how it is organised) is particularly strong

**Structural Adherence (5/5):**
- File starts directly with `# Short-Term vs Long-Term Memory in AI Agents` — no metadata header
- Context section correctly references previous session (Session 12) content without naming the session number
- Headings are direct and descriptive (`## How Conversation History Works as Short-Term Memory`)
- 3-sentence rule followed across all prose paragraphs
- Official Definition / In Simple Words / Real-Life Example pattern applied to every new technical concept
- Full code provided for all three strategies with single-line English comments on every line
- "How the code works" bulleted explanations follow every code block
- Key Takeaways section present with 5 bullets + forward-looking link to future sessions
- Quick Reference Table covers 18 terms and commands at the end of the file
- File saved in the correct location: `Session13/Lecture Notes.md`

**No Logical Mistakes (True):**
- Context window mechanics are technically accurate — conversation history is passed in full with every LLM call
- Python list slicing `full_history[-WINDOW_SIZE:]` is syntactically and logically correct
- Summary memory's use of `global running_summary` and `.clear()` are correct Python patterns
- Token approximation (1 token ≈ 0.75 words) is a widely accepted industry estimate
- Vector database description (numerical embeddings, semantic similarity retrieval) is accurate
- Long-term memory types (Episodic/Semantic/Procedural) align with standard cognitive science and agent design literature

**No Presentation Mistakes (True):**
- All Markdown tables use correct pipe (`|`) syntax with header separator rows
- Python code blocks use triple-backtick fencing with `python` language tag
- Heading hierarchy is consistent (H1 title → H2 major sections → H3 subsections)
- Bold text used correctly for important terms and key concepts
- Horizontal rules (`---`) used to visually separate major sections
- Bullet points and numbered steps formatted consistently throughout

### Outcome
All criteria meet or exceed the expected threshold. **No improvisation required. Notes are approved.**
