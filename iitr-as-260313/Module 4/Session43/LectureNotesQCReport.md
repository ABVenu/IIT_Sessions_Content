# Lecture Notes QC Report — AutoGen: Group Chat and Multi-Agent Orchestration

## QC Iteration 1

| Criteria | Result |
|---|---|
| Content Coverage | 5/5 |
| Creativity | 5/5 |
| Structural Adherence | 4/5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | False |
| No Previous Session Number References | True |
| No Metadata/Internal References | True |

**Notes:** Metadata topics were all present (GroupChat, GroupChatManager, speaker selection, max rounds, human input optional, multi-agent handoffs). Campus feature launch + placement-drive briefing with research, risk, and messaging specialists continues Ananya / Meera / GIT Pune / Nimbus / Riverbank. Issues found:

1. **Presentation:** `FACTS` string, specialist system messages, and the opening ask lacked per-line comments on continuation strings.

**Improvisation applied:** Commented every continuation line in the group script (facts fence, three system messages, opening message).

---

## QC Iteration 2

| Criteria | Result |
|---|---|
| Content Coverage | 5/5 |
| Creativity | 5/5 |
| Structural Adherence | 5/5 |
| No Logical Mistakes | True |
| No Presentation Mistakes | True |
| No Previous Session Number References | True |
| No Metadata/Internal References | True |

**Notes:** Re-read after improvisation. Context bridges from the **previous** AutoGen conversable pair without session numbers. Upcoming work is make.com, hosted builders, ops, and governance. No duration, audience, or “keep it lite” leakage. No Pydantic or FastAPI. Official Definition / In Simple Words / Real-Life Example on core terms. Student-facing activities (including break-then-fix on `max_round`). Full group script with line comments and “How the code works.” Mermaid instead of S3. Failure modes (wrong speaker, repetition deadlock) plus one configuration fix. Key Takeaways + terminology table. Line count within range (`491` lines; max 500).

### Coverage Checklist (metadata subtopics)

| Subtopic | Section in notes |
|---|---|
| Design a group chat with three or more specialized agents for one complex task | Three Specialists, One Complex Task; Full Group Script |
| Configure speaker selection and round limits | Speaker Selection, Handoffs, and Max Rounds; `select_briefing_speaker`; `max_round=10` |
| Demonstrate successful task completion with distinct sub-results | A Healthy Group Trace; What “Good” Looks Like |
| Diagnose repetition deadlock or wrong speaker and apply a configuration fix | Diagnose One Failure Mode; Lab fix rows; Break then fix activity |
| Human input optional | Optional Human Input; `human_input_mode="NEVER"` |

**Outcome:** QC passed on iteration 2 after improvisation from iteration 1.
