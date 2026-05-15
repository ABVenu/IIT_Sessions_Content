# Assignment Question QC Report — Session 14: Data Prep — Handling Messy Data

---

## Objective Assignment QC

| Q# | Type | Difficulty | Correct Option(s) | Correct Option Relevant to Question? | Remarks |
|---|---|---|---|---|---|
| Q1 | MCQ (Single) | Easy | B | Yes — `head()` is the standard first peek at loaded tabular data | Transport analytics scenario; distractors are later-stage cleaning actions |
| Q2 | MCQ (Single) | Easy | B | Yes — impossible age should be marked missing with `replace(..., np.nan)` before imputation | Clinic scenario distinguishes logic fixes from `abs()`, imputation, and de-duplication |
| Q3 | MCQ (Single) | Easy | A | Yes — exact duplicate rows are counted with `duplicated().sum()` | E-commerce order context; other options address different quality issues |
| Q4 | MCQ (Single) | Easy | B | Yes — sign errors on price are corrected with `.abs()` while keeping magnitude | Used-car listing scenario aligned with lecture examples |
| Q5 | MCQ (Single) | Moderate | B | Yes — ordered `seniority_band` maps to label encoding, not one-hot | Tests ordinal vs nominal encoding choice |
| Q6 | MCQ (Single) | Moderate | B | Yes — fitting the scaler before split leaks test statistics into preprocessing | Data-leakage scenario with `MinMaxScaler` |
| Q7 | MSQ (Multiple) | Moderate | A, B, C | Yes — median/mean for numeric distance and mode for categorical vehicle type are all valid imputation choices | Distractors use cross-column numeric fill and blind zero-fill |
| Q8 | MSQ (Multiple) | Moderate | A, B, C, D | Yes — shape, `info()`, null counts, and `describe()` are core inspection steps | Distractor E is an unsafe full-data scaler fit before cleaning/split |
| Q9 | MSQ (Multiple) | Hard | A, C, D | Yes — invalid-value repair, de-duplication before learned transforms, and train-only fit for encoders/scalers are sound | Distractor B imputes before duplicate removal; E fits scaler on train+test |
| Q10 | MSQ (Multiple) | Hard | A, C, E | Yes — one-hot for nominal fuel/brand, input scaling for large numeric ranges, and before/after QA checks are appropriate | Distractors include nominal label encoding and scaling the target label |

---

## Subjective Assignment QC

| Q# | Type | Difficulty | Submission Instructions Clear? | Dataset Provided? | Remarks |
|---|---|---|---|---|---|
| Q1 | Practical Coding (single `.py` file) | Medium | Yes — VS Code single-file workflow, run verification, and LMS code-box submission are stated | Yes — inline bootstrap code creates `ride_bikes.csv`; expected row/dup/missing checks are listed | Seven-step pipeline covers inspection, sign repair, median/mean imputation, duplicate removal, one-hot encoding, `MinMaxScaler` on inputs only, and impact summary |

---

## Subjective Question — Detailed QC

### Code Logic Verification

| Step | Code / Logic Checked | Verdict |
|---|---|---|
| Dataset bootstrap | 10 rows include one exact duplicate (`RB102` repeated), two missing `kilometers_driven`, one missing `asking_price`, and two negative prices | ✅ No issues |
| Sign repair + mean impute | `.abs()` runs before `asking_price` mean; `-72000` becomes `72000` and enters the mean | ✅ No issues |
| Median impute | Missing odometer values filled with column median after non-null values remain | ✅ No issues |
| Duplicate removal | `duplicated().sum()` returns `1`; `drop_duplicates()` leaves `9` rows | ✅ No issues |
| Encoding | `pd.get_dummies(..., drop_first=True)` applied to nominal `brand` and `fuel` | ✅ No issues |
| Scaling | `MinMaxScaler` fits only `model_year` and `kilometers_driven`; `asking_price` excluded as target | ✅ No issues |
| Alternatives | Train-only `fit`/`transform` scaling and `drop_duplicates(subset=["listing_id"])` noted as valid variants | ✅ No issues |

### Presentation Issues Found & Fixed

| Issue | Location | Fix Applied |
|---|---|---|
| Mismatched list lengths in the embedded dataset generator (`model_year` had 9 entries) | Subjective dataset bootstrap | Aligned all columns to 10 rows |
| Duplicate row did not register because the repeated `RB102` row differed in `model_year` / `kilometers_driven` | Subjective dataset bootstrap | Made the repeated listing an exact duplicate; verified `1` duplicate removed and `9` final rows |

---

## Overall Assignment Quality Ratings

### Objective Assignment

| Criterion | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | Inspection, invalid-value repair, imputation, duplicates, ordinal vs nominal encoding, scaling, leakage, and post-cleaning verification |
| Creativity | 5 | Scenarios span transport, clinic, e-commerce, hiring, delivery, and car resale without session-reference phrasing |
| Structural Adherence | 5 | 10 questions total: 6 MCQ (4 Easy + 2 Moderate) + 4 MSQ (2 Moderate + 2 Hard); progressive difficulty; full answer explanations |
| No Logical Mistakes | True | Correct options and distractors checked against lecture scope; advanced model-based imputation not tested as implementation |
| No Presentation Mistakes | True | Self-contained prompts, consistent markdown structure, grammatically clean wording |

### Subjective Assignment

| Criterion | Rating (1–5) | Notes |
|---|---|---|
| Content Coverage | 5 | End-to-end messy-data workflow on a realistic listing table with explicit expected checks |
| Creativity | 5 | RideMetrics used-bike marketplace scenario; not a verbatim notebook replay |
| Structural Adherence | 5 | One medium coding task with Case C submission instructions and complete answer explanation |
| No Logical Mistakes | True | Pipeline order, duplicate count, final row count, and target-vs-feature scaling rules verified |
| No Presentation Mistakes | True | Dataset generator, task list, expected checks, and submission steps are unambiguous |

---

## QC Summary

All criteria for both assignments meet the required standard:

- Content Coverage: **5 / 5** ✅
- Creativity: **5 / 5** ✅
- Structural Adherence: **5 / 5** ✅
- No Logical Mistakes: **True** ✅
- No Presentation Mistakes: **True** ✅

**Both assignments are approved for platform upload.**
