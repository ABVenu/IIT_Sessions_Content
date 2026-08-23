# Deployment: Streamlit User Interface

## Introduction

In the **previous** session you packaged the campus parcel desk as a **release bundle**, ran a **pre-release eval gate**, measured **token cost**, and kept **API keys** in environment variables.

A gated release still needs a **human-facing window**. Stakeholders — faculty, product owners, teammates — will not open notebooks or chase cells in a spreadsheet to “feel” the agent.

**Running story:** the same **campus parcel desk**. Today the focus is **why Streamlit**, how it beats a **Google Sheet** as a demo UI, how to design the **screen**, and how to build a demo from a **sample parcel dataset** — with only a short create-and-run recipe at the end.

**What you will learn:**

- Merits of **Streamlit** for agent demos
- Why Streamlit is a better **stakeholder UI** than Google Sheets for this job
- How to plan **layout**, **user input**, and a calm **trace** panel
- How to create a demo from a **sample dataset**, wire it to an agent mindset, run it **locally**, and note **cloud** differences

---

## The Problem a Spreadsheet Cannot Solve Alone

You already have a clerk brain and release habits. The missing piece is a **front counter**: type a question, see an answer, optionally peek at sources and steps.

Many teams start demos in a **Google Sheet** because everyone knows Sheets. That works for tables. It fails as a product preview.

| What stakeholders want | What a Sheet usually gives |
|---|---|
| “Ask like WhatsApp / a website” | “Open tab → find column → filter → scroll” |
| One clear answer on screen | Many rows; visitor must interpret |
| Foldable “how we checked” proof | Extra columns that look like raw data dump |
| Feels like a shipped desk | Feels like homework shared on Drive |

![Campus parcel desk comparison — confused faculty scrolling a huge Google Sheet versus a clean Streamlit front counter with one clear Flipkart Room 214 answer](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session48/session48-01-sheet-vs-streamlit-demo-ui.png)

- **Official Definition:** A **user interface (UI)** is the interactive screen where a person types, clicks, and reads results.
- **In Simple Words:** The glass counter between the student and the back-room clerks.
- **Real-Life Example:** IRCTC shows a booking form — not a giant Excel of every train in India.

**Common doubt:** “Our Sheet already has the parcel register. Isn’t that enough?”  
The **register** can live in a Sheet or CSV. The **demo experience** still needs a proper UI on top.

### Activity — Sheet Pain Point

A faculty member opens your Drive Sheet with 200 parcel rows. They ask: “Where is Flipkart for Room 214?” List two clicks/scrolls they must do that a website would hide. **Sample answer:** filter brand + room, or Ctrl+F twice, then read status/gate columns manually.

---

## What Is Streamlit? (and Its Merits)

Before comparing tools, name the tool you will use for the counter window.

- **Official Definition:** **Streamlit** is a Python library that turns scripts into simple interactive web apps — text boxes, buttons, tables, expanders — without hand-writing HTML/CSS.
- **In Simple Words:** You describe the page in Python; Streamlit draws a browser UI for you.
- **Real-Life Example:** Like a hostel notice template with ready boxes — fill fields; visitors see a clean form, not your drafting mess.

### Merits of Streamlit for agent demos

- **Fast demo path:** From idea to browser page without a full website team
- **Python-native:** Fits the same language your agent / module work already uses
- **Clear widgets:** Inputs, buttons, success/warning messages, expanders for optional detail
- **One-command run:** `streamlit run ...` opens a local web page stakeholders can click
- **Calm storytelling:** Put the answer large; hide sources/steps until someone opens a panel
- **Shareable on LAN:** Classmates on the same Wi-Fi can try your laptop URL for a quick peek
- **Honest scope:** Excellent for demos and prototypes — not a claim that it replaces every production web stack forever

**Why these merits matter for agents**

Agents are not only “a table of facts.” They **answer**, **retrieve**, and **act** in steps. Streamlit’s layout matches that story: question → answer → optional trace.

**Merits that matter in an Indian classroom / campus demo**

| Merit | What a visitor feels | Parcel-desk example |
|---|---|---|
| Browser page, not a Drive maze | “This is the product” | Dean types Room 214 once |
| Placeholder + tips in sidebar | “I know what to try” | Tip: `Flipkart Room 214` |
| Success / warning chips | “Did it work?” without reading logs | Green for found; warning for miss |
| Expanders | “I can go deeper if I want” | Sources / Steps stay closed |
| Same Python as the agent | “Team can maintain this” | Capstone function behind the button |

**What Streamlit is *not* claiming**

- It is not “always better than Sheets for data entry”
- It is not automatically a hardened public production site
- It is not a substitute for eval gates and release versioning you already practised

**Common error:** Judging Streamlit only by “can it store 10,000 rows?” Storage is not its main merit. **Interaction and presentation** are.

### Activity — Merit Match

Match each merit to a stakeholder need: (1) expanders, (2) `streamlit run`, (3) Python-native. Needs: (A) open a browser demo quickly, (B) reuse agent code skills, (C) hide raw steps until asked. **Answers:** 1→C, 2→A, 3→B.

### Activity — Merit or Not?

Is “everyone in India already has a Google account” a merit of Streamlit? **Answer:** No — that is a merit of Sheets for *data collaboration*. Streamlit’s merit is the **demo UI**, not account familiarity.

---

## Streamlit vs Google Sheets — Which Wins for the Demo UI?

Sheets stays useful as **data**. Streamlit wins as the **demo UI** that shows the agent to humans.

| Dimension | Google Sheets | Streamlit |
|---|---|---|
| Main job | Store, edit, share tabular data | Build an interactive app screen |
| Visitor skill needed | Spreadsheet navigation | Type a question and click |
| Feels like | Shared register / homework file | Mini product / front counter |
| Showing “agent steps” | Extra columns or comments (noisy) | Foldable expanders (calm) |
| Wiring an agent | Awkward (scripts, Apps Script, copy-paste) | Natural call from Python backend |
| Branding a demo | Spreadsheet chrome everywhere | Your title, caption, sidebar tips |
| Best use here | Sample parcel **dataset** source | Stakeholder **face** of the desk |

- **Official Definition:** A **front-end** is what users see; a **back-end** is the logic and data work behind it.
- **In Simple Words:** Streamlit is the counter glass; the agent + dataset are the back room.
- **Real-Life Example:** Swiggy UI vs kitchen + inventory sheets — both matter; customers meet the app first.

**When Sheets is still the right tool**

- Editing the raw parcel register with non-coders
- Quick collaborative data cleanup
- Exporting a **sample CSV** that Streamlit will read

**When Streamlit is the better demo choice**

- Faculty should not hunt columns
- You must show answer + optional sources/steps
- You want the demo to feel like a **shipped desk**, not a Drive link

**Side-by-side story (same sample data)**

Imagine both tools contain AWB1001–AWB1005.

- In **Sheets**, the dean asks “Flipkart 214?” You share screen, open filters, hope the right row is visible, then verbally explain status.
- In **Streamlit**, the dean types the question, clicks **Ask the desk**, reads one sentence, and only opens Sources if curious.

Same facts. Completely different **trust and clarity**.

**Common doubt:** “Can’t I put a Google Form in front of a Sheet?”  
A Form collects input. It still does not give you a polished agent reply + foldable trace the way a Streamlit page does.

### Activity — Tool Choice

Pick one: You must demo the parcel agent to a non-tech dean in 3 minutes. Do you open (a) the raw Sheet, (b) a Streamlit page fed by sample rows, (c) a notebook with five code cells? **Answer:** **(b)**.

### Activity — Dual Role

Write one line each: (1) “I will use Sheets for ___.” (2) “I will use Streamlit for ___.”  
**Sample:** (1) editing and exporting the sample register. (2) the stakeholder-facing ask-and-answer window.

**Connecting idea:** Comparison tells you *why* Streamlit. Next you design *what* appears on the screen — layout, input, and a short trace.

---

## Streamlit UI = Desk Zones (Layout)

A messy counter confuses visitors. **Layout** is how you place title, input, answer, and trace so the eye knows where to look.

- **Official Definition:** **Layout** in Streamlit means arranging page regions with pieces like title, caption, sidebar, main body, and expanders.
- **In Simple Words:** Counter top, side drawer, and foldable trays — each has one job.
- **Real-Life Example:** Parcel desk: big “Ask here” board; rules on the side; tracking slips folded underneath.

### Recommended desk zones

| Zone | What visitors see | Desk feel |
|---|---|---|
| Title + caption | App name + one-line purpose | Board above the counter |
| Sidebar | Tips, sample questions, “demo release” note | Side drawer with rules |
| Input | Text box + “Ask” button | Where the student speaks |
| Answer | Large reply text + success/warning | Clerk’s spoken reply |
| Trace (folded) | Sources and steps inside expanders | Tracking slip on request |

![Streamlit Campus Parcel Desk mockup showing desk zones — title, sidebar tips, question input, large answer with success chip, and closed Sources and Steps expanders](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session48/session48-02-streamlit-desk-zones-layout.png)

**UI rules that keep demos calm**

- One job per zone — do not dump the whole register on the home view
- Answer **above** the foldable trays
- Keep expanders **closed** by default
- Sidebar for tips — not for API keys

**User input (simple pattern)**

- Prefer a clear **text box + button** for beginners
- Button click means “now run the desk” — so idle page loads do not burn tokens
- Placeholder text can show a sample question from your dataset

**Displaying agent trace (beginner level)**

- **Sources:** short lines from retrieved rows (AWB, room, gate) — not raw JSON
- **Steps:** numbered plain English (“Searched register — found 1 row”)
- If nothing found: honest warning — never invent Gate numbers

- **Official Definition:** An **agent trace** (demo level) is a short ordered list of what the agent did — retrieval hits and tool/desk steps — shown for transparency.
- **In Simple Words:** The foldable tracking slip under the final SMS.
- **Real-Life Example:** Courier app checkpoints, not the warehouse database dump.

### Activity — Sketch Three Zones

On paper, draw Title, Input+Answer, and a closed “Sources / Steps” tray for the parcel desk. Mark which zone a dean should understand **without** opening anything. **Answer:** Title + Answer (and maybe a success/warning line).

### Activity — Trace Calmness

Which belongs on the first screen: (1) full system prompt, (2) final desk reply, (3) API key preview? **Answer:** Only **(2)**.

---

## Sample Dataset — The Parcel Register Under the UI

Streamlit needs something to answer from. For learning, use a tiny **sample dataset** — the same spirit as a Sheet tab, but sized for a demo.

- **Official Definition:** A **sample dataset** is a small, realistic set of rows used to build and demonstrate an app before connecting full production data.
- **In Simple Words:** A practice register with a handful of parcels — enough to look real, small enough to understand.
- **Real-Life Example:** A canteen demo menu with 8 items, not the entire city’s restaurant catalog.

### Sample parcel register (use this)

| awb | brand | room | gate | status |
|---|---|---|---|---|
| AWB1001 | Flipkart | 214 | Gate 2 | Ready for pickup |
| AWB1002 | Amazon | 118 | Gate 1 | Arrived at campus hub |
| AWB1003 | Myntra | 302 | Gate 2 | Ready for pickup |
| AWB1004 | Flipkart | 118 | Gate 1 | Out for campus delivery |
| AWB1005 | Snapdeal | 215 | Gate 3 | Held at desk — ID pending |

You can keep this table in:

- a Google Sheet tab (easy editing with friends), then **Download → CSV**, or
- a simple `parcels.csv` file next to your app

**How the UI should use these rows**

| Student question (input) | Expected demo behaviour |
|---|---|
| “Flipkart Room 214” | Answer mentions AWB1001, Gate 2, ready for pickup; source line shows that row |
| “Amazon 118” | Answer for AWB1002 at Gate 1 |
| “BlueDart Room 999” | Honest “not found” — no invented gate |
| “Where is my parcel?” (vague) | Prefer a clarifying reply or no confident match — do not guess |

**Sheets → Streamlit handoff**

1. Clean column names in Sheets (`awb`, `brand`, `room`, `gate`, `status`)
2. Freeze a header row so editors do not rename columns by accident
3. Keep only demo rows (five is enough for class)
4. **File → Download → Comma-separated values (.csv)**
5. Place `parcels.csv` next to your Streamlit file (or keep the tiny list in the script for the shortest scaffold)
6. Streamlit / agent **reads** the data; visitors use the UI — they do not edit the Sheet during the dean demo

![Sample parcel register handoff — Google Sheet with five rows exports to parcels.csv and feeds the Streamlit front counter while the Sheet stays the editor not the product UI](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session48/session48-03-sheets-csv-to-streamlit-handoff.png)

**Do / Don’t with sample data**

| Do | Don’t |
|---|---|
| Use real-looking AWB / room / gate values | Invent gates when retrieval finds nothing |
| Keep columns consistent | Mix “Gate2” and “gate 2” without cleaning |
| Export a frozen demo CSV for the talk | Live-edit the Sheet while presenting |
| Treat Sheets as the **editor** | Treat Sheets as the **product UI** |

**Common error:** Showing the entire five-row table as the “answer.” The answer is a **sentence**; the table is **evidence** inside Sources.

### Activity — Map One Row to the Screen

For AWB1003 (Myntra, Room 302): write (a) one answer sentence, (b) one source line, (c) two step lines.  
**Sample:** (a) Myntra parcel AWB1003 for Room 302 is ready at Gate 2. (b) `AWB1003 | Myntra | Room 302 | Gate 2`. (c) Received question → Searched register — found 1 row.

### Activity — Dataset Honesty

Someone asks for “Flipkart Room 118.” Your sample has AWB1004. Is inventing “Gate 2” acceptable because Flipkart often uses Gate 2 elsewhere? **Answer:** No — use AWB1004’s real Gate 1 (or say you are unsure if retrieval fails).

### Activity — Sheet Cleanup

Which column rename breaks the demo most: (a) `status` → `parcel_status`, (b) adding a notes column, (c) sorting rows? **Answer:** **(a)** if your app still expects `status` — rename carefully or update the reader.

**Connecting idea:** Dataset + UI sketch is the plan. Next is a **short create recipe** — enough to scaffold and run — without a heavy coding workshop.

---

## Scaffold Recipe — Create the Demo (Minimal How-To)

You do not need a large codebase to understand deployment today. You need a **thin page**: input → lookup sample data / call agent → show answer + folded trace.

- **Official Definition:** To **scaffold** an app means building a minimal working skeleton you can run and improve.
- **In Simple Words:** A first counter with title, question box, and reply — furniture before fancy paint.
- **Real-Life Example:** Cardboard stall with a signboard and a notebook — open for practice orders.

### Mental model: three thin layers

| Layer | Responsibility | Beginner choice |
|---|---|---|
| UI (Streamlit) | Layout, input, display | Title, sidebar tips, text box, button, expanders |
| Agent / desk logic | Turn question into answer + steps | Start with “search sample rows”; later swap your module/capstone agent |
| Data | Parcel facts | Sample table / `parcels.csv` (can originate from Google Sheets) |

**Wire to the agent backend (concept first)**

Ask whatever agent you have to return a **small dictionary**:

| Field | Meaning |
|---|---|
| `answer` | Final reply shown large |
| `sources` | Short retrieved lines |
| `steps` | Ordered plain-English steps |
| `ok` | True if a confident match finished cleanly |

If today’s agent returns only a string, wrap it: put the string in `answer`, add honest source/step lines when you have them, set `ok` True/False. The Streamlit page should stay thin.

**Capstone / module wiring (still concept-first)**

- Keep Streamlit as the **face**
- Keep your agent as the **brain**
- Keep Sheets/CSV as the **register** (until you plug a real database later)
- Swap only the function behind the button — not the whole page design. The short scaffold below is enough to practise create-and-run; your real capstone agent can replace `run_desk` later.

### Install and run (local)

```bash
pip install streamlit
streamlit run parcel_desk_app.py
```

Browser usually opens at `http://localhost:8501` — your laptop’s local counter.

### Full code — short scaffold with sample data (`parcel_desk_app.py`)

```python
# Short Streamlit desk: sample parcels → answer + folded sources/steps
import streamlit as st  # Draws the web page from this script

PARCELS = [  # Sample dataset (same rows as the teaching table)
    {"awb": "AWB1001", "brand": "Flipkart", "room": "214", "gate": "Gate 2", "status": "Ready for pickup"},  # Row 1
    {"awb": "AWB1002", "brand": "Amazon", "room": "118", "gate": "Gate 1", "status": "Arrived at campus hub"},  # Row 2
    {"awb": "AWB1003", "brand": "Myntra", "room": "302", "gate": "Gate 2", "status": "Ready for pickup"},  # Row 3
    {"awb": "AWB1004", "brand": "Flipkart", "room": "118", "gate": "Gate 1", "status": "Out for campus delivery"},  # Row 4
    {"awb": "AWB1005", "brand": "Snapdeal", "room": "215", "gate": "Gate 3", "status": "Held at desk — ID pending"},  # Row 5
]


def run_desk(question: str) -> dict:  # Stand-in agent backend for the UI contract
    steps = ["Received question at the counter"]  # Beginner trace line 1
    q = question.lower().strip()  # Normalise input for simple matching
    hits = []  # Rows that seem to match
    for row in PARCELS:  # Search the sample register only
        blob = " ".join(str(v).lower() for v in row.values())  # One searchable string per row
        if q and any(tok in blob for tok in q.split() if len(tok) > 2):  # Skip tiny words
            hits.append(row)  # Keep matches
    steps.append(f"Searched sample register — found {len(hits)} row(s)")  # Trace line 2
    if not hits:  # Honest miss path
        steps.append("Stopped — no matching parcel row")  # Trace line 3
        return {
            "ok": False,  # UI warning path
            "answer": "No matching parcel in the sample register. Try brand + room from the demo table.",  # Honest miss
            "sources": [],  # No evidence rows
            "steps": steps,  # Still show what was tried
        }
    row = hits[0]  # Demo: first hit is enough
    steps.append(f"Read status for {row['awb']}")  # Trace line 3 on success
    answer = f"{row['brand']} parcel {row['awb']} for Room {row['room']} is '{row['status']}' at {row['gate']}."  # Clerk sentence
    sources = [f"{row['awb']} | {row['brand']} | Room {row['room']} | {row['gate']}"]  # One source line
    steps.append("Posted short reply for the student")  # Trace line 4
    return {"ok": True, "answer": answer, "sources": sources, "steps": steps}  # UI contract


st.set_page_config(page_title="Campus Parcel Desk", layout="centered")  # Browser tab + width
st.title("Campus Parcel Desk")  # Main board title
st.caption("Demo UI on sample data — answer first, sources/steps optional.")  # Purpose line
with st.sidebar:  # Side drawer
    st.write("Try: Flipkart Room 214")  # Sample question tip
    st.write("Data: five-row sample register (Sheet/CSV friendly).")  # Dataset honesty
question = st.text_input("Your question", placeholder="e.g. Flipkart Room 214")  # User input
if st.button("Ask the desk"):  # Scaffold action
    result = run_desk(question)  # Back-room call (swap for capstone agent later)
    st.success("Desk reply ready") if result["ok"] else st.warning("No confident match")  # Status chip
    st.subheader("Answer")  # Answer zone
    st.write(result["answer"])  # Large reply
    with st.expander("Sources", expanded=False):  # Folded evidence
        st.write(result["sources"] or "No rows retrieved.")  # Source lines or empty note
    with st.expander("Steps", expanded=False):  # Folded trace
        for i, step in enumerate(result["steps"], start=1):  # Numbered steps
            st.write(f"{i}. {step}")  # Plain English only
```

**How the code works**

- Sample rows sit in `PARCELS` — same facts you could maintain in Google Sheets and export
- `run_desk` is a stand-in **agent backend**; later point this call at your module/capstone agent but keep the same return keys
- Streamlit only handles **UI zones**; it does not invent parcels

### Activity — Scaffold Check

After `streamlit run`, you click Ask with an empty box and somehow get “Gate 2.” Is that acceptable? **Answer:** No — empty/vague input should not invent a gate.

### Activity — Wire Thought

Your capstone agent already returns a long paragraph string. What do you change first — the Streamlit title font, or a wrapper that fills `answer` / `sources` / `steps` / `ok`? **Answer:** The **wrapper** (contract), then display.

---

## Local Run, Share, and Cloud Differences

Scaffold success means the page opens on your machine. Sharing and hosting change the **front door**, not the meaning of answer/sources/steps.

### Local run checklist

1. Save `parcel_desk_app.py` (sample data inside or loaded from CSV)
2. `pip install streamlit` in your environment
3. `streamlit run parcel_desk_app.py`
4. Open `http://localhost:8501`
5. Test one known row (“Flipkart Room 214”) and one unknown (“BlueDart 999”)

**Quick peer share on the same Wi-Fi**

```bash
streamlit run parcel_desk_app.py --server.address 0.0.0.0
```

Friends may use `http://YOUR_LAPTOP_IP:8501`. Fine for a classroom peek — not a public internet launch.

### Local vs cloud (what actually changes)

| Topic | Local laptop | Typical cloud host |
|---|---|---|
| Who starts the app | You in a terminal | Host keeps the process running |
| URL | `localhost` or LAN IP | Public `https://...` link |
| Secrets | Shell / local `.env` | Host environment variables panel |
| Sample data file | Next to your script | Uploaded / mounted storage |
| Sleep / cost | Your laptop power | Free tiers may sleep; paid stay up |
| Audience | You + nearby peers | Anyone with the link (protect it) |

![Local versus cloud hosting for the parcel desk Streamlit app — laptop with localhost:8501 and LAN share on the left, cloud shop with public URL and locked env secrets on the right](https://s13n-curr-images-bucket.s3.ap-south-1.amazonaws.com/iitr-as-2603/module4/session48/session48-04-local-vs-cloud-hosting.png)

- **Official Definition:** **Cloud hosting** means running the app on a remote provider so people open a URL without using your laptop as the server.
- **In Simple Words:** Counter moves from your hostel room to a rented shop in the market.
- **Real-Life Example:** Practising a canteen billing screen on your PC vs putting it on a lab server for the whole floor.

**Secrets reminder (from previous habits):** Never type API keys into Streamlit boxes. Read them in the backend from environment variables — Sheets demos often tempt people to paste keys in cells; do not.

**Common error:** Calling a Sheet “deployed” because the Drive link is public. A public Sheet is shared **data**, not an agent **UI**.

### Activity — Hosting Map

Match: (1) `localhost:8501`, (2) host env-var panel, (3) free-tier sleep. To: (A) cloud secret injection, (B) local-only URL, (C) app may go cold after idle. **Answers:** 1→B, 2→A, 3→C.

### Activity — One-Minute Pitch

Say aloud: “Sheets hold the sample register. Streamlit is the front counter. Visitors see the answer first; sources and steps stay folded. Today it runs on my laptop; cloud would change the URL and where secrets live.” Keep it under 60 seconds.

---

## End-to-End Demo Checklist

Before you show faculty:

- [ ] You can explain **why Streamlit** beats a raw Sheet for this demo
- [ ] UI zones are clear: title, input, answer, folded sources/steps
- [ ] Sample dataset questions produce real row-based answers
- [ ] Unknown questions stay honest — no invented gates
- [ ] `streamlit run` works locally; you know what cloud would change
- [ ] No API keys appear on the page or in the Sheet screenshot

---

## Key Takeaways

- **Streamlit** merits for agents are speed, Python fit, calm widgets, and a one-command browser demo — presentation first, not “another spreadsheet.”
- **Google Sheets** is excellent for the **sample dataset**; **Streamlit** is the better **stakeholder UI** for question → answer → optional trace.
- Design **desk zones**: answer large, sources/steps folded; wire through a simple `answer` / `sources` / `steps` / `ok` contract.
- Build from a tiny **sample register**, run locally with `streamlit run`, and remember cloud mainly changes **URL**, **uptime**, and **secret injection**.

These habits turn a gated release into something people can *try* — a front counter on top of sample data, ready to point at your real agent next.

---

## Important Commands, Libraries, Terminologies Used

| Name | Type | Reminder |
|---|---|---|
| Streamlit | Library | Python → interactive demo UI in the browser |
| Merits of Streamlit | Idea | Fast demo, widgets, expanders, local run |
| Google Sheets | Tool | Great for sample/register data — weak as agent UI |
| User interface (UI) | Term | What visitors see and click |
| Front-end / back-end | Term | Counter glass vs clerks + data |
| Layout / desk zones | Term | Title, sidebar, input, answer, expanders |
| User input | Pattern | Text box + button for beginner demos |
| Agent trace (demo level) | Term | Short sources + steps, folded by default |
| Sample dataset | Term | Tiny realistic rows for the demo register |
| Scaffold | Term | Minimal runnable app skeleton |
| UI–backend contract | Pattern | `answer`, `sources`, `steps`, `ok` |
| `streamlit run` | Command | Start the local demo server |
| `localhost:8501` | Concept | Default local URL |
| LAN share (`0.0.0.0`) | Practice | Same-Wi-Fi peer peek only |
| Cloud hosting | Term | Remote URL, process lifetime, env secrets |
| Environment variables | Practice | Secrets stay off the Streamlit page and Sheet |
