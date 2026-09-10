# Lecture Notes QC Report

**File:** `Lecture Notes.md`  
**Session:** Masterclass: Evolution of the Web  
**Folder:** `iitp-sdai-2606/Masterclasses/sdai2606/Session03_M3_1`

---

## QC Iteration 1

| Criteria | Result |
|---|---|
| Content Coverage | 4/5 |
| Creativity | 4/5 |
| Structural Adherence | 4/5 |
| No Logical Mistakes | False |
| No Presentation Mistakes | False |
| No Previous Session Number References | True |
| No Metadata/internal reference in student notes | True |

### Iteration 1 Notes

- Curriculum covered: need for evolution beyond static Web 1.0, demerits of static-only sites, Web 2.0 platforms, browser load/render, JavaScript runtime, APIs and cloud, Web 3.0 at a high level.
- Official Definition / In Simple Words / Real-Life Example used on core terms.
- Student-facing activities present; no instructor voice ("Ask students...").
- No session-number references; previous-lesson context taken from Insertion Sort without naming the session.
- No duration, audience, or internal instruction phrases leaked into notes.
- Clean title start, Key Takeaways, and terminologies table present.

### Issues found

- **Coverage / structure:** First draft was **417 lines**, below the planned **480–500** student-document range. **CSS**, **DNS**, **HTTP/HTTPS**, **client/server**, **database**, **JSON**, **call stack**, and **event loop** were named without a full definition trio or enough teaching.
- **Logical:** The script-in-`<head>` activity said the like button “likely does nothing.” The real beginner failure is `querySelector` returning `null` and `addEventListener` **throwing** in the Console.
- **Logical:** The `fetch` demo would often **fail from `file://`**. That was not explained, so students could think APIs themselves were broken.
- **Logical:** Labelling “a personal blog with no comments” as Web 1.0 was shaky (blogs were a Web 2.0 publishing pattern).
- **Presentation:** Learning list used “without extra hype.” Web 3.0 used “High-level caution.” Both read as internal briefing, not student documentation.
- **Creativity:** No era comparison table; public API example had no sample JSON; rendering was a flat list without a revision table.

### Fixes applied before Iteration 2

- Expanded notes into the 480–500 line range with client/server, CSS, DNS, HTTP/GET, database, JSON, events, call stack, and event loop.
- Added a load-and-render table, a Web 1.0 / 2.0 / 3.0 revision table, and a sample JSON body for the demo API.
- Corrected the head-script activity to use the Console **TypeError** path.
- Documented `file://` vs `python3 -m http.server 8000` from the saved folder, plus the address-bar fallback.
- Replaced the blog item with a temple aarti-timings page; noted that the static HTML sample uses today’s tags to show static *behaviour*.
- Removed briefing tone (“hype”, “caution”); added `setTimeout` so the event loop is visible on the same likes page.

**Iteration 1 verdict:** Fail (Coverage, Creativity, Structural Adherence < 5; Logical Mistakes = False; Presentation Mistakes = False) → improvise and re-QC.

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
| No Metadata/internal reference in student notes | True |

### Iteration 2 Notes

- All metadata topics and detailed subtopics are taught: evolution need, static Web 1.0, demerits, Web 2.0, browser rendering, JS runtime, APIs and cloud, Web 3.0 at a high level.
- Full HTML documents include line-level comments and “How the code works” bullets; `likes.html` shows DOM updates plus `setTimeout`; `api-demo.html` shows `fetch` with a documented fallback.
- Indian examples (IRCTC, PNR, UPI, Swiggy, Flipkart, IPL, college circular, temple timings, Pune/Mumbai cloud) sit after definitions, not as scenario-led introductions.
- Notes length is inside the planned 480–500 line range.
- No session numbers, no duration/audience/internal dial language, no instructor-facing activity voice.
- Structure matches the prompt: documentation-style student notes, connecting sentences, Key Takeaways, quick-reference table.

**Iteration 2 verdict:** Pass — all criteria meet expected result.
