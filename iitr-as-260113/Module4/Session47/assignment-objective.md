# Assignment Objective

Total Questions: 10

Difficulty Flow: Easy → Moderate → Hard

Question Types:
- 6 MCQ (Single Correct): Q1–Q6
- 4 MSQ (Multiple Correct): Q7–Q10

---

## Q1 (MCQ, Easy)

Ananya is running n8n locally using Docker on her laptop. She wants to open the workflow editor in her browser. Which URL should she use?

A. `http://localhost:5678`  
B. `http://localhost:3000`  
C. `https://console.cloud.google.com`  
D. `http://localhost:8080`

**Correct Answer:** A

**Answer Explanation:**  
Self-hosted n8n is exposed on port **5678**, so the editor opens at **`http://localhost:5678`**.

Why other options are wrong:
- B and D: These are common dev ports, but n8n’s default local port is **5678**.
- C: Google Cloud Console is for OAuth/API setup, not the n8n canvas.

---

## Q2 (MCQ, Easy)

GreenMart wants a workflow that starts only when a customer submits an online feedback form inside n8n. Which trigger type fits best?

A. Trigger manually  
B. On a schedule  
C. On form submission  
D. On webhook call only

**Correct Answer:** C

**Answer Explanation:**  
When a user submits an n8n-hosted form, the workflow should start with an **on form submission** trigger.

Why other options are wrong:
- A: Manual trigger runs only when someone clicks **Execute workflow**.
- B: Schedule runs on a timer, not on each form submit.
- D: Webhook starts on an external HTTP call, not on the built-in n8n form UI.

---

## Q3 (MCQ, Easy)

Every n8n automation must begin with one specific kind of node. What is that first node called?

A. Credential  
B. Trigger  
C. Expression  
D. Volume

**Correct Answer:** B

**Answer Explanation:**  
The **trigger** is always the starting node — the event that kicks off the workflow (form submit, schedule, webhook, manual execute, etc.).

Why other options are wrong:
- A: Credentials store authentication, they are not the workflow start.
- C: Expressions compute dynamic values inside nodes.
- D: Volume is a Docker storage concept for persisting n8n data.

---

## Q4 (MCQ, Easy)

When n8n connects to Google Sheets using OAuth2, what is the main benefit for the user?

A. n8n gets your Gmail password so it never expires  
B. n8n gets limited, consent-based access without you sharing your Google password  
C. OAuth2 removes the need to enable any Google APIs  
D. OAuth2 hard-codes customer emails into the spreadsheet

**Correct Answer:** B

**Answer Explanation:**  
**OAuth2** lets a third-party app like n8n access Google services with **scoped permissions** after you approve a consent screen — without sharing your password.

Why other options are wrong:
- A: OAuth2 is designed to avoid password sharing.
- C: You still must enable required APIs (Sheets, Drive) in Google Cloud.
- D: Customer emails come from form data via expressions, not OAuth2.

---

## Q5 (MCQ, Moderate)

Rahul enabled **Google Sheets API** in his Google Cloud project, but the n8n Sheets node still cannot access spreadsheets reliably. Which additional API is commonly required?

A. Google Drive API  
B. Google Maps API  
C. YouTube Data API  
D. Google Photos API

**Correct Answer:** A

**Answer Explanation:**  
Spreadsheet files are stored in **Google Drive**. For Sheets integrations, **Google Drive API** is usually required alongside **Google Sheets API**.

Why other options are wrong:
- B, C, D: Maps, YouTube, and Photos are unrelated to reading/writing spreadsheet rows.

---

## Q6 (MCQ, Moderate)

During testing, Kavya clicks **Execute workflow**, but the form does not open and the same customer row is appended repeatedly. What is the most likely cause?

A. The IF node is connected to the wrong branch  
B. Sample data is **pinned** on the form trigger node  
C. She selected **External** audience on the OAuth consent screen  
D. The spreadsheet tab name is too long

**Correct Answer:** B

**Answer Explanation:**  
**Pinned data** freezes sample output on a node. While pinned, the workflow may reuse cached form values instead of opening a fresh form for each full run.

Why other options are wrong:
- A: Wrong IF wiring would affect branching, not duplicate the same row on every run without showing the form.
- C: External audience is normal for personal Gmail learning; it does not cause duplicate cached submissions by itself.
- D: Tab name length does not cause this pin-related behaviour.

---

## Q7 (MSQ, Moderate)

Which of the following are valid ways to **start** an n8n workflow?

A. Trigger manually (click Execute workflow)  
B. On a schedule (e.g., every day at 9 a.m.)  
C. On a webhook call (e.g., payment confirmed)  
D. Only by adding an LLM node first

**Correct Answers:** A, B, C

**Answer Explanation:**  
Workflows can start manually (A), on a timer (B), or when an external system hits a webhook (C). Form and app-event triggers are also valid starters.

Why other options are wrong:
- D: An LLM node is optional for AI steps; it is not required to start every workflow.

---

## Q8 (MSQ, Moderate)

A team is setting up Google OAuth credentials so n8n can append rows to a spreadsheet. Which statements are correct?

A. They need a **Client ID** and **Client Secret** from Google Cloud  
B. They should enable both **Google Sheets API** and **Google Drive API**  
C. For an unverified External app, adding a **test user** can fix “Access blocked” during sign-in  
D. They should paste the Google password directly into the n8n workflow canvas

**Correct Answers:** A, B, C

**Answer Explanation:**  
OAuth setup needs Client ID/Secret (A), both Sheets and Drive APIs (B), and often a test user for External testing mode (C).

Why other options are wrong:
- D: Passwords must never be pasted into workflows; OAuth2 exists to avoid that.

---

## Q9 (MSQ, Hard)

A feedback workflow is built as: **Form → Append row in Google Sheets → IF (feedback equals Positive) → Update Send voucher (Yes/No)**. Which statements are correct?

A. Form fields should be mapped to sheet columns using **expressions**, not hard-coded customer names  
B. The **Append row** step should write `email`, `name`, and `feedback` from the form output  
C. On the update step, **email** is a sensible **column to match on** when writing Send voucher Yes/No  
D. Matching only on the **feedback** column is best because every customer always has unique feedback text

**Correct Answers:** A, B, C

**Answer Explanation:**  
Dynamic mapping uses expressions (A). The first Sheets action stores the three form fields (B). Updates should key on **email** because it identifies the person (C).

Why other options are wrong:
- D: Many customers can share the same feedback label (Positive/Negative/Neutral), so feedback alone is not a reliable unique key.

---

## Q10 (MSQ, Hard)

While debugging a Google Sheets workflow in n8n, which statements are correct?

A. If credentials or API access is revoked, the workflow may fail with **Forbidden — check your credentials**  
B. The form trigger must be **connected** to the Sheets node so output becomes input  
C. Enabling APIs in the **wrong Google Cloud project** is a common setup mistake  
D. Hard-coding one test customer’s email in the Sheets node is the recommended production approach

**Correct Answers:** A, B, C

**Answer Explanation:**  
Revoked access causes Forbidden errors (A). Nodes must be linked for data flow (B). Wrong-project API enablement breaks OAuth (C).

Why other options are wrong:
- D: Production workflows should use expressions from live form data, not hard-coded values.
