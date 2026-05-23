# Assignment — Subjective (Session: Open-Source LLMs)

**Type:** One practical coding task (medium difficulty)  
**Scope:** Use the starter code below, complete `ask_llm`, run **local Ollama** and **Groq cloud**, save two HTML resumes, compare quality, submit the full file.

---

## Scenario

You will generate a resume in **HTML** using two engines — once with a **small local model** on Ollama (0.5B or 1B) and once with a **large model on Groq** — then open both files in a browser and decide which resume is better.

This mirrors how builders choose engines: **local** for privacy and zero per-token cost on a laptop; **Groq** for speed and quality when a 70B-class model is impractical to run locally.

**Important:** Copy the **starter code** section into `resume_generator.py`. Do **not** rewrite the save-to-file logic — use `save_resume_html()` exactly as given.

---

## What you must do

1. Copy the full **starter code** below into `resume_generator.py`.  
2. Set `LOCAL_MODEL` to a tag from `ollama list` (0.5B or 1B only). Set `GROQ_MODEL` to a model Groq hosts (e.g. `llama-3.3-70b-versatile`).  
3. Complete **`ask_llm(mode, prompt_text)`** (instructions in the starter).  
4. Run: `python resume_generator.py`  
5. Confirm two files are created (see naming below). **Open both HTML files in a browser** (see [How to open the HTML files](#how-to-open-the-html-files)).  
6. At the **bottom** of the file, fill in the **two comment lines** (which resume is better — local or Groq, including **styling**).  
7. **Paste the entire file** into the LMS answer box.

---

## Starter code — copy into `resume_generator.py`

```python
import os
from datetime import datetime
import requests

# --- Set your model names ---
LOCAL_MODEL = "qwen2.5:0.5b"   # 0.5B or 1B only; must match `ollama list`
GROQ_MODEL = "llama-3.3-70b-versatile"  # check console.groq.com for available models

CANDIDATE = {
    "name": "Aarav Mehta",
    "email": "aarav.mehta@example.com",
    "phone": "+91-98765-43210",
    "location": "Roorkee, Uttarakhand",
    "education": "B.Tech Computer Science, IIT Roorkee (expected 2026), CGPA 8.4",
    "skills": ["Python", "REST APIs", "SQL", "Git", "Basic ML"],
    "experience": "Summer intern at TechBridge Labs (Jun–Aug 2025): built internal dashboards with FastAPI and PostgreSQL.",
    "projects": "Hostel Room Booking CLI (Python) — 200+ active users on campus.",
}

RESUME_PROMPT = f"""You are a professional resume writer. Create a complete, single-page resume in valid HTML only.

Rules:
- Return ONLY HTML starting with <!DOCTYPE html> — no markdown fences, no explanation before or after.
- Do not invent employers, degrees, or facts not listed below.

Layout (required):
- Use a **two-column** layout for the main body (e.g. CSS flexbox or CSS grid with two columns).
- **Left column (narrower, ~30–35%):** contact block, Skills, Education.
- **Right column (wider, ~65–70%):** Experience, Projects.
- **Full-width header** above the columns: candidate name (large), one-line title or tagline, email / phone / location on one line.

Styling (use a <style> block in <head> — make it look polished):
- Font: a clean sans-serif stack (e.g. Arial, Helvetica, or system-ui).
- **Accent color:** one professional color (e.g. #2563eb blue or #0f766e teal) for headings, section titles, and subtle borders.
- Section headings: uppercase or small-caps, accent color, bottom border or left border.
- Consistent spacing: padding inside columns, margin between sections, readable line-height (1.4–1.6).
- Skills: show as a neat list or small pill/tag style — not a plain comma-separated paragraph.
- Page: max-width ~900px, centered on screen; light background (#f8fafc) with white column areas or a white card look.
- Print-friendly: avoid horizontal scroll; keep everything on one screen-height page if possible.

Candidate data:
Name: {CANDIDATE['name']}
Email: {CANDIDATE['email']}
Phone: {CANDIDATE['phone']}
Location: {CANDIDATE['location']}
Education: {CANDIDATE['education']}
Skills: {', '.join(CANDIDATE['skills'])}
Experience: {CANDIDATE['experience']}
Projects: {CANDIDATE['projects']}
"""


def save_resume_html(html_text: str, mode: str) -> str:
    """
    Save model output to an HTML file. USE THIS FUNCTION AS-IS — do not change the logic.

    File name pattern:
      Local  -> Local_Resume_YYYYMMDD_HHMMSS.html
      Groq   -> Groq_Resume_YYYYMMDD_HHMMSS.html
    """
    prefix = "Local" if mode == "local" else "Groq"
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_Resume_{stamp}.html"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_text)

    print(f"Saved {filename}")
    return filename


def ask_llm(mode: str, prompt_text: str) -> str:
    """
    TODO (you implement):
    - mode "local":
        POST http://localhost:11434/api/chat
        model LOCAL_MODEL, no API key
        JSON body: model, messages=[{"role":"user","content": prompt_text}], stream=False
        timeout=120
        return response.json()["message"]["content"]

    - mode "groq":
        Read GROQ_API_KEY from os.environ (if missing, raise ValueError with a clear message)
        Use the Groq Python SDK: from groq import Groq
        client = Groq(api_key=...)
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt_text}],
        )
        return response.choices[0].message.content
    """
    # YOUR CODE HERE
    raise NotImplementedError("Complete ask_llm before running.")


def generate_resume_html(mode: str) -> str:
    """Call the LLM, then save HTML using save_resume_html (do not change this function)."""
    html_from_model = ask_llm(mode, RESUME_PROMPT)
    return save_resume_html(html_from_model, mode)


if __name__ == "__main__":
    print("Generating local resume...")
    generate_resume_html("local")

    print("Generating Groq resume...")
    try:
        generate_resume_html("groq")
    except ValueError as e:
        print(f"Groq skipped: {e}")

    print("Open both HTML files in your browser and compare quality.")

# TODO after comparing both files in the browser — replace the lines below (2 lines; mention styling):
# Local resume quality:
# Groq resume quality:
```

---

## File names after a successful run

You should see files like:

- `Local_Resume_20260519_153045.html`  
- `Groq_Resume_20260519_153102.html`  

---

## How to open the HTML files

After `python resume_generator.py` finishes, open **each** saved file in a browser using **either** method:

**Method 1 — Double-click (easiest)**  
- Go to the folder where you ran the script (same folder as `resume_generator.py`).  
- **Double-click** `Local_Resume_....html` — it should open in your default browser (Chrome, Edge, Safari, etc.).  
- Repeat for `Groq_Resume_....html`.

**Method 2 — Paste the file path in the browser address bar**  
- Right-click the HTML file → **Copy as path** (Windows) or hold **Option** and copy path (macOS), or note the full path from your terminal/file explorer.  
- Open Chrome/Firefox/Edge.  
- Paste the path into the address bar and press Enter.  
  - Example (macOS): `file:///Users/you/projects/Local_Resume_20260519_153045.html`  
  - Example (Windows): `file:///C:/Users/you/projects/Local_Resume_20260519_153102.html`  

Compare **local** and **Groq** side by side (two browser tabs are fine).

---

## Quality check (brief)

| Check | What to look for |
| --- | --- |
| Valid HTML | Page opens in browser without errors |
| Two-column layout | Left column has Skills/Education; right has Experience/Projects; full-width name header |
| Sections | All required sections present with correct content |
| Facts | No invented jobs or degrees |
| **Styling** | Which resume looks better visually? (colors, spacing, fonts, skill tags, borders, overall polish) |
| Overall | Which resume would you show a mentor — local or Groq? |

---

## Submission instructions (**case c**)

- Use the **starter code** above (with `save_resume_html` and `generate_resume_html` unchanged).  
- Complete only `ask_llm`, model constants, and the **two comment lines** at the bottom.  
- Run the script; confirm at least the **local** HTML file exists (Groq file if your key is set).  
- **Paste the full `resume_generator.py`** into the LMS code editor / answer box.

**Setup**

```bash
pip install requests groq
ollama pull qwen2.5:0.5b    # or your chosen light model
export GROQ_API_KEY="your-key"   # from console.groq.com — for Groq only
```

In **Google Colab**, add `GROQ_API_KEY` in **Secrets** (same name) and enable access for the notebook instead of `export`.

Do **not** hard-code API keys in the file.

---

## Answer explanation (for Assess platform)

**Grading focus**

- `save_resume_html` used as provided; files created with correct naming (`Local_*` / `Groq_*`).  
- `ask_llm` correct for **local** (Ollama POST, no key) vs **groq** (Groq SDK, `GROQ_API_KEY`, `chat.completions.create`).  
- Same `RESUME_PROMPT` for both runs (fair comparison).  
- Two honest comment lines comparing local vs Groq (content **and styling** / two-column polish).

**Reference `ask_llm` (evaluators only)**

```python
def ask_llm(mode: str, prompt_text: str) -> str:
    if mode == "local":
        url = "http://localhost:11434/api/chat"
        payload = {
            "model": LOCAL_MODEL,
            "messages": [{"role": "user", "content": prompt_text}],
            "stream": False,
        }
        r = requests.post(url, json=payload, timeout=120)
        r.raise_for_status()
        return r.json()["message"]["content"]

    if mode == "groq":
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY is not set. Create a key at console.groq.com and run: "
                "export GROQ_API_KEY='your-key'"
            )
        from groq import Groq

        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[{"role": "user", "content": prompt_text}],
        )
        return response.choices[0].message.content

    raise ValueError('mode must be "local" or "groq"')
```

**Alternative approaches:** Students may use `requests` against Groq’s HTTP API instead of the SDK if headers and JSON match Groq docs — acceptable if output and key handling are correct.

**What a strong submission demonstrates**

- Same prompt, two engines — applied understanding of **local vs cloud** trade-offs from this session.  
- Groq pattern matches class: `Groq(api_key=...)`, `client.chat.completions.create`, `choices[0].message.content`.  
- Thoughtful comparison comments (tiny local model often weaker on layout/HTML polish vs Groq 70B-class).

**Common weak submissions**

- Hard-coded `GROQ_API_KEY` in source.  
- Different prompts for local vs Groq (unfair comparison).  
- Changed `save_resume_html` naming logic.  
- Only local run with no attempt to set Groq key (acceptable if comments explain Groq skip, but full credit needs both when key available).

---

**End of subjective assignment**
