# Assignment — Subjective (Session: Open-Source LLMs)

**Type:** One practical coding task (medium difficulty)  
**Scope:** Complete `ask_llm`, run **local Ollama** and **Ollama Cloud**, save two HTML resumes, compare quality, submit the full file.

---

## Scenario

You will generate a resume in **HTML** using two engines — once with a **small local model** on Ollama (0.5B or 1B) and once with a **larger model on Ollama Cloud** — then open both files in a browser and decide which resume is better.

This mirrors how builders choose engines: **local** for privacy and zero per-token cost on a laptop; **Ollama Cloud** for stronger output when your RAM cannot hold a large model.

**Important:** Copy the **starter code** section into `resume_generator.py`. Do **not** rewrite the save-to-file logic — use `save_resume_html()` exactly as given.

---

## What you must do

1. Copy the full **starter code** below into `resume_generator.py`.  
2. Set `LOCAL_MODEL` to a tag from `ollama list` (0.5B or 1B only). Set `CLOUD_MODEL` to a model available on [ollama.com/library](https://ollama.com/library) for Ollama Cloud (e.g. `gpt-oss:20b` — verify on the library page).  
3. Complete **`ask_llm(mode, prompt_text)`** using the **OpenAI-compatible client** for both modes (instructions in the starter).  
4. Before running cloud mode, create an API key at [ollama.com/settings/keys](https://ollama.com/settings/keys) and set it in your terminal:  
   `export OLLAMA_API_KEY="your-key-here"`  
5. Run: `python resume_generator.py`  
6. Confirm two files are created (see naming below). **Open both HTML files in a browser** (see [How to open the HTML files](#how-to-open-the-html-files)).  
7. At the **bottom** of the file, fill in the **two comment lines** (which resume is better — local or cloud, including **styling**).  
8. **Paste the entire file** into the LMS answer box.

---

## Starter code — copy into `resume_generator.py`

```python
import os
from datetime import datetime

from openai import OpenAI

# --- Set your model names ---
LOCAL_MODEL = "qwen2.5:0.5b"   # 0.5B or 1B only; must match `ollama list`
CLOUD_MODEL = "gpt-oss:20b"    # verify on ollama.com/library for Ollama Cloud

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


def ask_llm(mode: str, prompt_text: str) -> str:
    """
    TODO (you implement) — OpenAI-compatible client for BOTH modes:

    - mode "local":
        client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama",  # any non-empty string for local Ollama
        )
        response = client.chat.completions.create(
            model=LOCAL_MODEL,
            messages=[{"role": "user", "content": prompt_text}],
        )
        return response.choices[0].message.content

    - mode "cloud":
        Read OLLAMA_API_KEY from os.environ (if missing, raise ValueError with a clear message)
        client = OpenAI(
            base_url="https://ollama.com/v1",
            api_key=api_key,
        )
        response = client.chat.completions.create(
            model=CLOUD_MODEL,
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

- `Local_Resume_20260630_153045.html`  
- `Cloud_Resume_20260630_153102.html`  

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
  - Example (macOS): `file:///Users/you/projects/Local_Resume_20260630_153045.html`  
  - Example (Windows): `file:///C:/Users/you/projects/Cloud_Resume_20260630_153102.html`  

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
- Complete only `ask_llm`, model constants, and the **two comment lines** at the bottom.  
- Run the script; confirm at least the **local** HTML file exists (cloud file if your API key is set).  
- **Paste the full `resume_generator.py`** into the LMS code editor / answer box.

**Setup**

```bash
pip install openai
ollama pull qwen2.5:0.5b    # or your chosen light model
export OLLAMA_API_KEY="your-key"   # from ollama.com/settings/keys — for cloud only
```

Do **not** hard-code your API key in the file.

---

## Answer explanation (for Assess platform)

**Grading focus**

- `save_resume_html` used as provided; files created with correct naming (`Local_*` / `Cloud_*`).  
- `ask_llm` correct for **local** (`base_url=http://localhost:11434/v1`, dummy key, `LOCAL_MODEL`) vs **cloud** (`base_url=https://ollama.com/v1`, `OLLAMA_API_KEY` from environment, `CLOUD_MODEL`).  
- Both modes use `client.chat.completions.create` with the same `RESUME_PROMPT` (fair comparison).  
- Two honest comment lines comparing local vs cloud (content **and styling** / two-column polish).

**Reference `ask_llm` (evaluators only)**

```python
def ask_llm(mode: str, prompt_text: str) -> str:
    if mode == "local":
        client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama",
        )
        response = client.chat.completions.create(
            model=LOCAL_MODEL,
            messages=[{"role": "user", "content": prompt_text}],
        )
        return response.choices[0].message.content

    if mode == "cloud":
        api_key = os.environ.get("OLLAMA_API_KEY")
        if not api_key:
            raise ValueError(
                "OLLAMA_API_KEY is not set. Create a key at ollama.com/settings/keys and run: "
                "export OLLAMA_API_KEY='your-key'"
            )
        client = OpenAI(
            base_url="https://ollama.com/v1",
            api_key=api_key,
        )
        response = client.chat.completions.create(
            model=CLOUD_MODEL,
            messages=[{"role": "user", "content": prompt_text}],
        )
        return response.choices[0].message.content

    raise ValueError('mode must be "local" or "cloud"')
```

**Alternative approaches:** Students may use the native `ollama` Python package for local mode only if output and model names are correct — partial credit if cloud mode still uses the OpenAI-compatible Ollama Cloud endpoint as taught.

**What a strong submission demonstrates**

- Same prompt, two hosts — applied understanding of **local vs Ollama Cloud** trade-offs.  
- OpenAI-compatible pattern: only `base_url`, `api_key`, and `model` change between modes.  
- Thoughtful comparison comments (tiny local model often weaker on layout/HTML polish vs a larger cloud model).

**Common weak submissions**

- Hard-coded `OLLAMA_API_KEY` in source.  
- Different prompts for local vs cloud (unfair comparison).  
- Changed `save_resume_html` naming logic.  
- Only local run with no attempt to set cloud key (acceptable if comments explain cloud skip, but full credit needs both when key is available).

---

**End of subjective assignment**
