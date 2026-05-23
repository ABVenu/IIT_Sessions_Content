# Lecture Script: ML Workshop — Credit Card Fraud Detection with Anomaly Detection

**Session Duration:** 2 hours  
**Target Audience:** Learners from diverse backgrounds, including those without prior technical training (e.g. Indian students new to data/ML). Delivery should stay concrete, example-led, and jargon-light until terms are defined.

**How to use this document:** This file is for **timing and facilitation only**. It is not a transcript. Use the numbered blocks to pace the room, manage demos, and trigger participation; adapt wording to your style.

**Break rule:** After **60–75 minutes** of instruction, take **one** pause of **5–8 minutes** (not a numbered block). Do not add extra formal breaks in the run-of-show.

---

## 1. Welcome, Session Arc, and Colab Setup Check (8 minutes)

- Welcome the group; frame today as a **Module 2 capstone**: everything from workflow → prep → modelling → evaluation on one realistic job — **PayGuard** fraud detection.
- Read (or paraphrase) the four learning outcomes from “What You Will Learn”: revisit Module 2 as one story; PayGuard + anomaly detection; 50,000-row dataset from S3; Isolation Forest + precision/recall (not accuracy alone).
- **Room action:** Ask everyone to open Google Colab, create `payguard_fraud_detection.ipynb`, run `print("PayGuard ready")` once.
- **Engagement — thumbs up:** “Do you see `PayGuard ready` below your cell?” Circulate (or watch screens in lab) and help anyone stuck on login or runtime.
- Point to **Lecture Notes** in the course folder as the step-by-step reference; this script is for **your** pacing only.

**Bridge sentence:** “Once Colab is alive, we’ll situate the business problem — why a bank cares about fraud differently than a school exam percentage.”

---

## 2. The PayGuard Problem — Business Story and Dataset (10 minutes)

- Screen-share the **PayGuard problem** figure (`masterclass001-06-payguard-problem.png`).
- Narrate in plain language: **~2% fraud** in **50,000** swipes; goal = flag suspicious activity **before** money leaves, without blocking every honest customer.
- **Why anomaly detection:** fraud often looks **weird** vs normal spending (amount, hour, distance, burst swipes) — one sentence on labels used only for **evaluation**, not for fitting the forest on normal rows.
- Walk the **column table** quickly (skip `transaction_id` as a feature later).
- Show the **end-to-end pipeline** figure (`masterclass001-09-payguard-pipeline.png`) — “this is our roadmap for the next 90 minutes.”
- **Engagement — pair-share (2 min):** In pairs, draft one line: *“PayGuard must detect rare fraud without relying only on accuracy.”* One pair reads aloud.
- **Room action:** Paste the S3 URL into chat for anyone who will type it later:  
  `https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2601/Module2/MasterClass/001/payguard_transactions.csv`

**Bridge sentence:** “Before we touch code, we’ll sprint through Module 2 vocabulary so today feels like a reunion, not a new subject.”

---

## 3. Module 2 at a Glance — Interactive Revision Sprint (14 minutes)

- **Do not** read every “Official Definition” block aloud. Use slides/images + cold-calls only.
- **ML workflow** (`masterclass001-01-ml-workflow.png`): problem → data → prep → split → train → evaluate — **cold-call:** “Which step comes *before* training?” (Prep + split.)
- **Classification vs regression:** fraud = **category** (classification), even if the method is unsupervised.
- **Leakage** (`masterclass001-05-split-first-no-leakage.png`): split **first**, scale on train only — **thumbs up/down:** “Fill missing values on the full table, then split — OK?” (No.)
- **Class imbalance** (`masterclass001-02-class-imbalance.png`): 98% legit → always guessing “not fraud” ≈ 98% accuracy — **check for understanding:** “Does high accuracy prove a good fraud model?” (No.)
- **Confusion matrix** (`masterclass001-03-confusion-matrix.png`): TN, FP, FN, TP in customer language (false alarm vs missed fraud).
- **Precision vs recall** (`masterclass001-04-precision-recall.png`): trust the alarm vs catch the thieves — read the PayGuard activity line from notes: missing fraud often hurts more than one brief block.
- **Anomaly detection** (`masterclass001-07-anomaly-detection.png`): learn normal, flag odd — bank SMS example.
- **Room action:** Keep pace brisk; if a term is unfamiliar, give **one** simple sentence and move on — details are in Lecture Notes.

**Bridge sentence:** “Vocabulary is set — now we load real PayGuard data straight from the course bucket, no manual upload.”

---

## 4. Step 1 — Live Load from S3 (8 minutes)

- **Live-coding:** Run the full **Step 1** import + `DATA_URL` + `pd.read_csv` cell from Lecture Notes (one cell, top to bottom).
- Narrate: S3 bucket name, `read_csv(URL)` in one step, expected shape **(50000, 10)**.
- **Room action:** Circulate; confirm `df.head()` on student screens. If institute network blocks S3, deploy fallback: upload `data/payguard_transactions.csv` from repo and `read_csv` local path (announce once).
- **Engagement — cold-call:** “How many columns do you see — and which one is the target?” (`is_fraud`.)
- **Common doubt (30 sec):** connection timeout → re-run cell; check internet.

**Bridge sentence:** “We have the table — next we behave like analysts and ask what the numbers are hiding before we train anything.”

---

## 5. Step 2 — Explore: Imbalance and the Fraud Bar Chart (10 minutes)

- **Live-coding:** Run **Step 2** exploration cell (`info`, `describe`, `value_counts`, fraud %, merchant counts, bar chart, `groupby` amount).
- Point at the **tiny red bar** in the chart — “this picture is why accuracy lies.”
- **Engagement — cold-call:** “What fraud percentage did you get — roughly 2%?” Confirm ~2% across the room.
- **Activity (notebook, 1 min):** Students note fraud % and answer in Markdown: “If accuracy is ~98%, does that alone prove the model is good?” (No — baseline always-legit guess.)
- **Room action:** Pause on `groupby` output — fraud rows often have higher **average amount**; that’s a clue, not the final model.

**Bridge sentence:** “Exploration done — we encode features and keep leakage out by splitting before we scale.”

---

## 6. Steps 3–4 — Encode Features, Split, Scale (12 minutes)

- **Live-coding:** **Step 3** — drop `transaction_id`, `X` / `y`, `get_dummies` with `drop_first=True`; print new column count.
- **Live-coding:** **Step 4** — `train_test_split` with `stratify=y`, `random_state=42`; `StandardScaler.fit` on **train only**; transform train and test; print train/test sizes and fraud counts in each split.
- Screen **split-first** image again if anyone looks confused.
- **Engagement — pair-share (90 sec):** “Why do we *not* scale before the split?” Pairs share one sentence.
- **Thumbs up:** “Train size around 40,000 and test around 10,000?”

**Bridge sentence:** “Data is honest and scaled — now we teach the model what *normal* swipes look like and flag what doesn’t fit.”

---

## 7. Step 5 — Isolation Forest on Normal Rows Only (12 minutes)

- **Live-coding:** **Step 5** — `normal_mask`, `X_train_normal`, `IsolationForest` with `contamination=0.02`, `fit` on normal only, `predict` on test, map `-1` → flagged fraud.
- Screen **Isolation Forest** figure (`masterclass001-08-isolation-forest.png`) while code runs.
- Explain in plain language: random trees **isolate** weird points quickly; `contamination=0.02` matches ~2% fraud rate hint.
- **Engagement — cold-call:** “Did we pass `y_train` into `fit` for the Isolation Forest?” (No — only normal feature rows.)
- **Room action:** Check how many test rows were flagged (`y_pred_iso.sum()`) — numbers will vary slightly but should be in a sensible hundreds/low-thousands range on ~10k test rows.

**Bridge sentence:** “The model has fired its alerts — a bank would never stop at ‘how many flags’; they measure trust and misses with precision and recall.”

---

**→ Take the single break (5–8 minutes) here if you have hit ~60–70 minutes of teaching. Optional return prompt on slide: “After break: evaluate like PayGuard, not like a school exam percentage.” ←**

---

## 8. Step 6 — Evaluate Like a Bank (12 minutes)

- **Live-coding:** **Step 6** metrics cell — accuracy, precision, recall, F1, confusion matrix, classification report, baseline “always legit” accuracy.
- Stress: print **accuracy for contrast only** — decision metric is **recall** (missed fraud) and **precision** (false alarms).
- Walk the **confusion matrix** on screen: count **false negatives** aloud.
- **Engagement — cold-call:** “Is our accuracy close to the baseline? If yes, is recall still acceptable for PayGuard?”
- **Activity (notebook, 2 min):** One sentence on false negatives from *their* matrix and whether PayGuard should worry.

**Bridge sentence:** “Metrics tell the headline; analysts still open the flagged rows every morning — that’s our next view.”

---

## 9. Steps 7 & 9 — Inspect Flagged Rows and Amount vs Hour Plot (10 minutes)

- **Live-coding:** **Step 7** — build `inspect_df`, `flagged`, show top 10 by amount, count true alerts vs false alarms.
- Narrate: high amount, odd hour, far from home, burst swipes — patterns students should **see** in the sample table.
- **Live-coding (or fast demo):** **Step 9** scatter — amount vs hour, green legit / red fraud sample; link visual clusters to what Isolation Forest uses in many dimensions.
- **Room action:** If time is tight, run Step 9 while students read Step 7 output on their own screens.
- **Pair-share (60 sec):** “Would you rather have more false alarms or more missed fraud for PayGuard?” Brief debrief toward recall.

**Bridge sentence:** “We’ve seen unsupervised alerts in action — in the last stretch we’ll optionally compare to a supervised model you already know.”

---

## 10. Step 8 — Optional Supervised Comparison (8 minutes)

- **Live-coding:** **Step 8** — `LogisticRegression` on `X_train_scaled` with labels; same precision/recall/F1 on test; print side-by-side with Isolation Forest.
- Screen **unsupervised vs supervised** figure (`masterclass001-10-unsupervised-vs-supervised.png`).
- **Engagement — cold-call:** “Which model had higher recall on your split — and would extra false alarms be acceptable?” (Accept varied answers; no single “right” number.)
- **Room action:** If many learners are behind, show your completed outputs and assign Step 8 as post-class — do not stall the whole room.

**Bridge sentence:** “Two approaches, same honest split — let’s close with what you’ll carry into deployment and the rest of the course.”

---

## 11. Key Takeaways, Glossary Flash, and Exit (8 minutes)

- Rapid five bullets from **Key Takeaways** in Lecture Notes: Module 2 applied; imbalance + metrics; Isolation Forest on normal; split-before-scale; recall habits for upcoming model comparison/saving.
- Optional: flash the **terms table** (pandas, `train_test_split`, `StandardScaler`, `get_dummies`, `IsolationForest`, precision/recall/F1, contamination, leakage, stratified split, S3 URL) — no line-by-line drill.
- Point to **Lecture Notes** Steps 1–9 and local `data/payguard_transactions.csv` as backup.
- **Engagement — exit ticket (1 min, chat or paper):** “In one line: why is accuracy misleading when fraud is 2%?”
- **Room action:** Thank the group; remind them notebooks are the deliverable artifact for this masterclass.

**Bridge sentence:** (Final line only if needed) “You didn’t just run a model today — you evaluated it the way a payment security team would, with honest splits and the right metrics.”

---

## Timing Flex — If the Session Is Running Long

- **First trims (save ~8–12 minutes):** Shorten **Module 2 revision sprint** (Block 3) to workflow + imbalance + confusion matrix + precision/recall only — skip regression metrics, trees, PCA/K-Means detail, and time-series aside (one sentence link to `hour` as a feature).
- **Second trims (save ~10–15 minutes):** Run **Step 1** imports as a pre-filled notebook students open; **narrate** Step 2 bar chart from your screen instead of waiting for every chart to render; merge **Steps 7 and 9** into a single facilitator demo (students watch, copy later).
- **Last resort:** Drop **Step 8** (logistic regression comparison) entirely in class; assign as async reading. Skip **Step 9** plot; keep **Step 6** confusion matrix discussion — that is non-negotiable for learning goals.
- **If ahead of time:** Add a **2-minute poll**: “Always predicting ‘not fraud’ is a strong production model — True/False,” then debrief with baseline accuracy; or extra Q&A on **false positives** (customer experience) vs **false negatives** (money lost).

**Never cut:** **split before scale** and **no leakage**; **class imbalance** and why **accuracy misleads**; training Isolation Forest on **normal-only** rows; at least **precision, recall, and confusion matrix** on the test set; students successfully **loading data from S3** (or approved offline fallback).

---
