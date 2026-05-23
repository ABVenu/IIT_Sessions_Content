# Lecture Notes QC Report — IITR-CYB-2510 (23 May 2026)

---

## QC Iteration 1 — Post-Session Alignment (Lecture Notes Released)

**Date:** 2026-05-23

**Evaluator:** Post-session alignment against Transcript (no Live Topic Coverage file provided)

### Criteria Ratings

| Criteria | Rating (1–5) | Notes |
|---|---|---|
| **Content Coverage** | 5 | Released notes match live delivery: symmetric/asymmetric crypto (prime factorization, quantum/PQC), hashing properties and demos, attack vectors (collisions, rainbow tables, GPU speed, LinkedIn 2012), salting, Argon2id/bcrypt/scrypt/PBKDF2, entropy/12-char minimum, AES-256 demo, secret management, secure error handling, Python lab, Bandit + Semgrep live runs, CI/CD workflow explained from repo. Mentimeter/quiz content excluded. |
| **Creativity** | 5 | Retained mermaid diagrams; added class-linked practice (CrackStation, online hash/AES demos, password-hasher sites, `lab-security-scan` repo); Quick Reference table for revision. |
| **Structural Adherence** | 5 | Clean `#` title; What You'll Learn + Detailed Explanation + Key Takeaways + Quick Reference; no session numbers; no poll/Mentimeter content. |
| **No Logical Mistakes** | True | LinkedIn breach corrected to **MD5** (per instructor transcript); FIPS/PBKDF2 iteration count aligned to class (~600K); CI/CD framed as repo example (not claimed as live GitHub run). |
| **No Presentation Mistakes** | True | Consistent headings; code blocks intact; mermaid flowchart retained; tables formatted correctly. |

### Changes from Lecture Notes.md → Released

| Action | Section |
|---|---|
| **Corrected** | LinkedIn 2012 breach: SHA-1 → **MD5** (unsalted) |
| **Added** | Live SHA-256 avalanche demo note; AES-256 class demo wording; password-hasher practice; `lab-security-scan` repo reference; Quick Reference table |
| **Reframed** | CI/CD GitHub Actions — reference workflow in shared repo (walked through in class, not executed live on GitHub) |
| **Removed** | None — all major sections were taught; no Mentimeter content was in source notes |

### Final Status: APPROVED ✓

Released notes aligned to session delivery. All QC criteria pass at level 5.
