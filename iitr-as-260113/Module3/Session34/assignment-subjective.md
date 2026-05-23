# Assignment — Subjective (Session 34: Ollama — Exploring Another World of LLMs)

**Type:** One practical coding task (medium difficulty)  
**Scope:** Use the starter code below, complete `ask_ollama`, run **local** and **cloud**, save two HTML resumes, compare quality, submit the full file.

---

## Scenario

You will generate a resume in **HTML** using Ollama — once with a **small local model** (0.5B or 1B) and once with **Ollama Cloud** — then open both files in a browser and decide which resume is better.

**Important:** Copy the **starter code** section into `resume_generator.py`. Do **not** rewrite the save-to-file logic — use `save_resume_html()` exactly as given.

---

## What you must do

1. Copy the full **starter code** below into `resume_generator.py`.  
2. Set `LOCAL_MODEL` and `CLOUD_MODEL` to model tags you have pulled.  
3. Complete **`ask_ollama(mode, prompt_text)`** (instructions in the starter).  
4. Run: `python resume_generator.py`  
5. Confirm two files are created (see naming below). **Open both HTML files in a browser** (see [How to open the HTML files](#how-to-open-the-html-files)).  
6. At the **bottom** of the file, fill in the **two comment lines** (which resume is better — local or cloud, including **styling**).  
7. **Paste the entire file** into the LMS answer box.

---

## Starter code — copy into `resume_generator.py`

```python
import os
from datetime import datetime
import requests

# --- Set your model names (must match `ollama list`) ---
LOCAL_MODEL = "qwen2.5:0.5b"   # 0.5B or 1B class only, e.g. qwen2.5:0.5b
CLOUD_MODEL = "gpt-oss:120b-cloud"  # your Ollama Cloud tag; set export OLLAMA_API_KEY first

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
      Cloud  -> Cloud_Resume_YYYYMMDD_HHMMSS.html
    """
    prefix = "Local" if mode == "local" else "Cloud"
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_Resume_{stamp}.html"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_text)

    print(f"Saved {filename}")
    return filename


def ask_ollama(mode: str, prompt_text: str) -> str:
    """
    TODO (you implement):
    - mode "local": POST http://localhost:11434/api/chat, model LOCAL_MODEL, no API key
    - mode "cloud": POST https://ollama.com/api/chat, model CLOUD_MODEL,
      header Authorization: Bearer <OLLAMA_API_KEY from os.environ>
      if key missing, raise ValueError with a clear message
    - JSON body: model, messages=[{{"role":"user","content": prompt_text}}], stream=False
    - timeout=120
    - return response.json()["message"]["content"]
    """
    # YOUR CODE HERE
    raise NotImplementedError("Complete ask_ollama before running.")


def generate_resume_html(mode: str) -> str:
    """Call Ollama, then save HTML using save_resume_html (do not change this function)."""
    html_from_model = ask_ollama(mode, RESUME_PROMPT)
    return save_resume_html(html_from_model, mode)


if __name__ == "__main__":
    print("Generating local resume...")
    generate_resume_html("local")

    print("Generating cloud resume...")
    try:
        generate_resume_html("cloud")
    except ValueError as e:
        print(f"Cloud skipped: {e}")

    print("Open both HTML files in your browser and compare quality.")

# TODO after comparing both files in the browser — replace the lines below (2 lines; mention styling):
# Local resume quality:
# Cloud resume quality:
```

---

## File names after a successful run

You should see files like:

- `Local_Resume_20260519_153045.html`  
- `Cloud_Resume_20260519_153102.html`  

---

## How to open the HTML files

After `python resume_generator.py` finishes, open **each** saved file in a browser using **either** method:

**Method 1 — Double-click (easiest)**  
- Go to the folder where you ran the script (same folder as `resume_generator.py`).  
- **Double-click** `Local_Resume_....html` — it should open in your default browser (Chrome, Edge, Safari, etc.).  
- Repeat for `Cloud_Resume_....html`.

**Method 2 — Paste the file path in the browser address bar**  
- Right-click the HTML file → **Copy as path** (Windows) or hold **Option** and copy path (macOS), or note the full path from your terminal/file explorer.  
- Open Chrome/Firefox/Edge.  
- Paste the path into the address bar and press Enter.  
  - Example (macOS): `file:///Users/you/projects/Local_Resume_20260519_153045.html`  
  - Example (Windows): `file:///C:/Users/you/projects/Local_Resume_20260519_153045.html`  

Compare **local** and **cloud** side by side (two browser tabs are fine).

---

## Quality check (brief)

| Check | What to look for |
| --- | --- |
| Valid HTML | Page opens in browser without errors |
| Two-column layout | Left column has Skills/Education; right has Experience/Projects; full-width name header |
| Sections | All required sections present with correct content |
| Facts | No invented jobs or degrees |
| **Styling** | Which resume looks better visually? (colors, spacing, fonts, skill tags, borders, overall polish) |
| Overall | Which resume would you show a mentor — local or cloud? |

---

## Submission instructions (**case c**)

- Use the **starter code** above (with `save_resume_html` and `generate_resume_html` unchanged).  
- Complete only `ask_ollama`, model constants, and the **two comment lines** at the bottom.  
- Run the script; confirm at least the **local** HTML file exists.  
- **Paste the full `resume_generator.py`** into the LMS code editor / answer box.

**Setup**

```bash
pip install requests
ollama run qwen2.5:0.5b
export OLLAMA_API_KEY="your-key"   # for cloud only
```

Do **not** hard-code API keys.

---

## Answer explanation (for Assess platform)

**Grading focus**

- `save_resume_html` used as provided; files created with correct naming.  
- `ask_ollama` correct for local vs cloud (URL, headers, payload, parse `message.content`).  
- Same `RESUME_PROMPT` for both runs.  
- Two honest comment lines comparing local vs cloud (content **and styling** / two-column polish).

**Reference `ask_ollama` (evaluators only)**

```python
def ask_ollama(mode: str, prompt_text: str) -> str:
    if mode == "local":
        url = "http://localhost:11434/api/chat"
        headers = None
        model = LOCAL_MODEL
    elif mode == "cloud":
        api_key = os.environ.get("OLLAMA_API_KEY")
        if not api_key:
            raise ValueError("OLLAMA_API_KEY is not set. Run: export OLLAMA_API_KEY='your-key'")
        url = "https://ollama.com/api/chat"
        headers = {"Authorization": f"Bearer {api_key}"}
        model = CLOUD_MODEL
    else:
        raise ValueError('mode must be "local" or "cloud"')

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt_text}],
        "stream": False,
    }
    r = requests.post(url, json=payload, headers=headers, timeout=120)
    r.raise_for_status()
    return r.json()["message"]["content"]
```

---

**End of subjective assignment.**
