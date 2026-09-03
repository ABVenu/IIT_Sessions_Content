# Lecture Notes QC Report — Sliding Window Problem Solving

**File reviewed:** `Lecture Notes.md`  
**Folder:** `IIT_Sessions_Content/Workshops/30thAugust26`  
**Review date:** 2026-09-03

---

## Iteration 1 (first full draft)

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | Subarray definition; fixed vs variable recap; n ≈ 10^5 vs O(n²); LeetCode 2461 (brute + window + frequency); LeetCode 209 (two claims, shrink-from-left); window sums of size K; LeetCode 438; extra coded 643 / 567 / 3; extra practice table; interview habit; upcoming recursion without a session id. |
| **Creativity** | **5 / 5** | Market-street shops, cricket jerseys, kirana tally, Asha attendance register, 26-column scorebook. Classroom live-coding trap (drop the smaller end) turned into a counter-example `[10,1,1,1]`. |
| **Structural Adherence** | **4 / 5** | Clean `#` title; Official / Simple / Real-Life on core terms; connecting sentences; full Python with a comment on every line; student-facing activities; Key Takeaways; terminology table. **Eighteen prose blocks broke the 3-sentence rule.** |
| **No Logical Mistakes** | **False** | Minimum-size dry run labelled `end at 2 / 3 / 1` using **values**, which a student could read as **indices**. Set-slide example said `set.remove(1)` while dropping a `2`. Messy sample table rows (`[3] wait`, `[7]-style single 8`). |
| **No Presentation Mistakes** | **False** | 3-sentence violations. Typo `resums`. Informal leftover rows in the length table. |
| **No Previous Session Number References** | **True** | “Previous session” / “upcoming” only. |
| **No Metadata/Internal References in Student Text** | **True** | No duration, audience, lite/keep-it-light, or instructor stage directions. |

### Expected Result

- Not met (structure 4; logical False; presentation False)

**Outcome:** QC failed. Improvise, then re-run.

### Improvisation applied (iteration 1 → 2)

1. Split all prose blocks that had more than three sentences.
2. Rewrote the `[2,3,1,2,4,3]` dry run with explicit **indices** (`end=0 include 2`, `drop nums[0]=2`, `start=1`).
3. Replaced the set-slide story with `[1,2,1]`: removing the left `1` from a set forgets the `1` that is still inside.
4. Removed the two informal rows from the length table.
5. Fixed `resums` → `re-sum`.
6. Tightened activity and extra-practice openings so each paragraph stays within three sentences.

---

## Iteration 2 (after improvise)

**Line count:** 761  
**Code check:** every Python statement has an end-of-line comment. All classroom and extra programs re-run with asserts (2461 samples 15 / 0; 209 samples 2 / 0 / 1; window sums `[6,9,12,15]`; anagrams `[0,6]` and `[0,1,2]`; max average `12.75`; permutation True/False; unique substring 3 / 1 / 3 / `dvdf` → 3).

### QC Criteria

| Criterion | Rating / Result | Notes |
|---|---|---|
| **Content Coverage** | **5 / 5** | All transcript problems, the deferred 2461 frequency solution, GFG-style size-`k` sums, anagrams, extra LeetCode (three fully coded + nine linked), interview language note, recursion as upcoming. |
| **Creativity** | **5 / 5** | Indian-relatable analogies retained. Live-session wrong turn (shrink both ends) kept as a student-facing common error with a counter-example. |
| **Structural Adherence** | **5 / 5** | Direct headings. 3-sentence rule restored on prose. Bold terms and bullets. Definition / Simple Words / Real-Life Example on subarray, sliding window, O(n)/O(n²), set, frequency map, frequency array, anagram. Full programs + How the code works. Student activities (“On paper…”, “Copy the table…”). Key Takeaways (5 bullets + future link). Terminology table. No Part/Section labels. |
| **No Logical Mistakes** | **True** | Distinct-window max 15; min length 2 for `[2,3,1,2,4,3]` target 7; anagram starts 0 and 6; `i - wsize + 1` start index; `p` longer than `s` returns `[]`; frequency map deletes zero-count keys so `len(freq)` is the distinct count. |
| **No Presentation Mistakes** | **True** | Headings are documentation-style. Activities are written to the student. Dry run uses index labels. No leftover informal table cells. |
| **No Previous Session Number References** | **True** | Grep clean for `Session N` / `session N`. |
| **No Metadata/Internal References in Student Text** | **True** | No keep-it-light / lite version / instructor-only headings / duration / audience. |

### Expected Result

- All criteria **Met**

**Outcome:** QC passed on iteration 2.

---

## Coverage Checklist (session subtopics)

| Subtopic | Section in notes |
|---|---|
| Previous workshop: fixed vs variable window | What You Will Learn; Recap |
| Subarray vs skipped neighbours | What Is a Subarray |
| Nested loops and n ≈ 10^5 | Why Nested Loops Fail for Large Inputs |
| LeetCode 2461 brute + window + frequency | Maximum Sum of Distinct Subarrays With Length K |
| Why a set is unsafe when sliding | Sliding the Same Window |
| LeetCode 209 two claims + O(n) scan | Minimum Size Subarray Sum |
| Do not shrink from both ends | Common error + `[10,1,1,1]` |
| Sums of every window of size K | Sums of Every Window of Size K |
| LeetCode 438 two arrays of 26 | Find All Anagrams in a String |
| Extra LeetCode | Extra Practice on LeetCode |
| Interview: think, then code in C++/Java/Python | How This Shows Up in Interviews |
| Upcoming recursion (no session id) | How This Shows Up in Interviews; Key Takeaways |

---

## Iteration 3 (images added)

Three S3 figures embedded in student notes. Alt text is descriptive. No session numbers, duration, or metadata leaked into captions.

| Image | Section |
|---|---|
| Subarray vs skipped pick | What Is a Subarray |
| Fixed window exclude/include | Sliding the Same Window (2461) |
| Variable window expand then shrink | Minimum Size Subarray Sum |

QC ratings unchanged from iteration 2 (all **5** / **True**).
