# Lecture Script: ML Workshop — Model Selection & Comparison

**Session duration:** 2 hours 15 minutes  
**Audience:** Absolute beginners — Indian learners, minimal prior tech background  

**Break rule:** After roughly 65–75 minutes of instruction (end of Block 7), take **one** 5–8 minute pause. Do not schedule multiple breaks inside the numbered flow.

---

## How to use this document

This file is **for facilitation and timing only**. It is not a substitute for the Lecture Notes; use it to manage pacing, room movement, screen-sharing, and quick checks that learners are following. Keep the Lecture Notes open for definitions, code, and screenshots.

---

## 1. Welcome, recap, and session promise (8 minutes)

- Welcome the cohort; remind them where to find notebooks / Colab and the Lecture Notes for Session 34.
- **Bridge from last session:** In one sentence, recall **time series** — order matters, chronological split, rolling features, MAPE — then pivot: *today we decide **which model to keep** and **how to ship it**.*
- State the four outcomes aloud: metric comparison table, complexity vs simplicity, saving/loading models, checklist for choosing algorithms.
- **Engagement:** *“Thumb up if you’ve trained at least two different model types so far.”* Acknowledge silently — no need to call names.

**Bridge sentence:** *“If we can line up models like marks on one marksheet, the decision gets easier — that marksheet is our metric table.”*

---

## 2. Metric tables — idea, analogy, visual (10 minutes)

- Screen-share the **metric comparison table** image from the notes (cricket / marksheet analogy in your own words — keep it short).
- **Official idea in plain language:** one table, many models, many metrics — side by side.
- **Cold-call (gentle):** *“In one line: why is separate printouts for each model risky on a real project?”* (Expected flavour: easy to miss trade-offs, hard to compare fairly.)
- Point at the sample table in notes (Logistic Regression vs Random Forest) without reading every number.

**Bridge sentence:** *“Let’s build that table in code for classification, then we’ll repeat the same pattern for regression.”*

---

## 3. Live build: classification metric table (17 minutes)

- Screen-share your IDE; use **breast cancer** dataset as in notes (same dataset for the rest of the classification demos).
- Walk **slowly** through: load → split → **StandardScaler** (stress: fit on train, transform test only) → dictionary of models → loop → `results.append` → `DataFrame`.
- **Room action:** Circulate or ask participants to **share screen in breakout / raise hand** if stuck on `transform` vs `fit_transform` — common failure point.
- Show printed table; relate to F1 / accuracy columns in one sentence each.
- **Pair-share (90 seconds):** *“Turn to your partner: why might Logistic Regression win on F1 even though Random Forest is ‘stronger’?”*

**Bridge sentence:** *“Same recipe, different metrics — regression uses MAE, RMSE, and R² instead of accuracy-style scores.”*

---

## 4. Regression metric table — demo or parallel run (12 minutes)

- Either live-code California housing snippet or **pre-run cell** plus line-by-line explanation (pick based on room speed).
- Emphasise: **`np.sqrt(mean_squared_error(...))`** for RMSE; lower MAE/RMSE better, R² nearer 1 better.
- **Check:** *“Thumbs up if the regression table clearly shows which model wins on all three columns.”*

**Bridge sentence:** *“Tables show *scores*, but not *cost* — next we attach **complexity**: simple vs fancy models.”*

---

## 5. Model complexity — table and mental model (11 minutes)

- Screen complexity spectrum image; walk the **complexity table** (Logistic → Neural nets) focusing on **interpretability** and **speed** — not memorising every cell.
- Use **shirt / essay grader** analogies from notes briefly.
- **Engagement:** *“Where would a bank loan officer sit on interpretability — high or low?”* (Chorus: high.)

**Bridge sentence:** *“Complexity bites us through **underfitting** and **overfitting** — we’ll diagnose that with train vs test, not guesses.”*

---

## 6. Overfitting vs underfitting — code with depths (14 minutes)

- Show third image (bias–variance / fit cartoon) quickly.
- Live-code or step through the **DecisionTree** loop: depths `1`, `5`, `None`; train acc, test acc, **gap**.
- **Cold-call:** *“Unlimited depth: training is perfect but test drops — what’s that called?”* (Overfitting.)
- Drill: never trust training score alone when test is far behind.

**Bridge sentence:** *“Rules of thumb tie this together: small data, explanations, latency — sometimes simple wins on purpose.”*

---

## 7. Golden rules and Occam’s Razor (6 minutes)

- Rapid-fire bullets: **when to choose simpler** vs **when to choose complex** from notes.
- One line on **Occam’s Razor** — simplest adequate model as default posture.
- **Quick check:** *“Fingers: 1 = I’ll mostly start simple, 5 = always reach for Random Forest.”* Scan the room — normalise “start simple.”

---

**Take the break (5–8 minutes)** after Block 7.

---

## 8. Model persistence — `joblib` and `pickle` (16 minutes)

- Motivation: spam filter / “save game” — no retraining per request.
- Screen persistence diagram from notes.
- **Live demo:** train small RF → `joblib.dump` model **and scaler** → new kernel or snippet → `joblib.load` → `predict` on **scaled** X_test — stress **saving scaler** as non-optional.
- Show `pickle` pattern with **`with open(..., 'wb'/'rb')`**; contrast **joblib vs pickle** table in one minute.
- **Security line (non negotiable):** never load pickle/joblib from untrusted sources — one sentence only.
- **Pair-share:** *“What breaks if you `StandardScaler()` fresh on new data instead of loading the fitted scaler?”*

**Bridge sentence:** *“We can compare models, tame complexity, and save the winner — the last piece is **how we choose what to train first**.”*

---

## 9. Model selection checklist — six questions + flow (13 minutes)

- Screen checklist flow image.
- Rapid walk through **Questions 1–6** — use lecture table for Q1–Q2; bullets for Q3–Q6; avoid reading every subsection.
- Optional: whiteboard or slide the **ASCII decision flow**; narrate once top to bottom.

**Bridge sentence:** *“Checklist suggests candidates; protocol forces **baseline → stronger → complexity filter → save**.”*

---

## 10. Protocol code, save winner, recap, Q&A (15 minutes)

- Walk **`Start Simple, Go Complex`**: baseline → medium → complex → **2 percentage-point filter** → `joblib.dump` winner + scaler.
- If time: run snippet or show output; otherwise trace logic line by line.
- **Five takeaways** from Key Takeaways — one breath each — plus pointer to pipelines in future sessions.
- **Final engagement:** *“One thing you’ll do differently on your next assignment?”* Take 2–3 verbal shares.
- Direct learners to glossary table in Lecture Notes for `joblib` / `pickle` / metric names.

**Bridge sentence (close):** *“You’ve got the comparison table, the complexity lens, the save/load path, and the checklist — bring all four into the next build.”*

---

## Timing flex (if running late)

- **Trim first:** shorten analogies in Blocks 2 and 5; show regression block as **pre-run notebook** walkthrough instead of typing every line.
- **Compress:** pickle demo to spoken comparison + doc link — keep **joblib + scaler** live (Block 8).
- **Defer:** optional pair-shares shorten to single cold-call; ASCII flow (Block 9) narrate without writing full diagram.
- **Never cut entirely:** scaler-alongside-model warning; train–test gap for overfitting; 2% simplicity rule unless audience is wholly lost — then summarise in prose.
- **If ahead of schedule:** add a **poll** (“Which metric matters most if false negatives are costly?”) before Block 3, or second **live regression** pass with learner driving one cell.
