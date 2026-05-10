# Lecture Script: Plotting & Storytelling with Data

**Session Duration:** 2 hours 15 minutes  
**Audience:** Absolute beginners — Indian students; little or no prior tech background  

---

## How to Use This Document

This file is for **timing and facilitation only**. It is not a substitute for the Lecture Notes. Use it to pace the room, manage demos and polls, and keep learners engaged. Pair it with your slides or IDE as needed.

---

## Break Rule

After roughly **60–75 minutes** of teaching time, take **one** pause of **5–8 minutes**. Do not schedule multiple breaks in this script; resume with the block that fits your clock after the break.

---

## 1. Opening — SQL Recap & Why We Visualise (10 minutes)

**Facilitator actions**

- Welcome the group; briefly restate the session title: *Plotting & Storytelling with Data*.
- Screen-share one slide or whiteboard: last session = SQL (`GROUP BY`, joins, pandas `groupby`/`merge`). Ask: *“Who remembers one aggregate function we used?”* — cold-call 1–2 students.
- Pose the bridge question from the notes: *Numbers in tables only tell part of the story — what might a chart show faster?* Pair-share for 60 seconds, then invite two pairs to share.
- State today’s arc in one line: EDA → inspect data → Matplotlib → Plotly → pick the right chart → tell a story with visuals.

**Students**

- Recall SQL/pandas mentally; discuss why visuals matter with a partner.

**Bridge Sentence:**  
*"Before we draw anything, every analyst does the same first step — they inspect the data. Let’s make that step concrete with a checklist."*

---

## 2. EDA — Definition & Checklist (Steps 1–2) (18 minutes)

**Facilitator actions**

- Define EDA in plain words (ingredients before cooking / doctor before diagnosis). Keep jargon light.
- Live-code or follow-along: `import pandas as pd`, `read_csv`, `shape`, `head()`, `tail()`. Circulate and glance at student screens — ensure CSV path works or use a shared notebook path.
- Move to Step 2: `df.info()`, `df.isnull().sum()`. Pause for **thumbs up / thumbs sideways**: *“Does everyone see column types and non-null counts?”*
- Address “What is missing?” — NaN in one sentence; why it matters.

**Students**

- Run load/peek commands; run `info()` and missing-value counts on the practice dataset.

**Bridge Sentence:**  
*"Now we know *what* columns we have and *where* gaps are — next we summarise numbers and categories in one shot."*

---

## 3. Summary Stats, Distributions & Outliers (16 minutes)

**Facilitator actions**

- Live-code: `describe()` and `value_counts()` on a suitable column. Explain mean vs median in everyday language if questions arise.
- Walk through the signals table (min/max, mean vs median, imbalance, missing %). Use one concrete example (e.g., salary outlier).
- **Cold-call:** *“Looking at `describe()` output — what would make you suspicious about one column?”*
- Optional 2-minute pair-share: *“Name one signal that would make you investigate further.”*

**Students**

- Run `describe()` and `value_counts()`; connect output to “distribution” and “outlier” ideas.

**Bridge Sentence:**  
*"We’ve inspected the table — now we pick up the pencil. In Python, that pencil is Matplotlib."*

---

## 4. Matplotlib Setup & Line Plot (17 minutes)

**Facilitator actions**

- Explain Matplotlib as “paper and pencil” / whiteboard — static but precise. Show `import matplotlib.pyplot as plt` and stress the `plt` convention.
- Live-code the monthly sales line plot (`figure`, `plot`, `marker`, `title`, `xlabel`, `ylabel`, `tight_layout`, `show`). Narrate each line as you type — beginners often lose the thread if you paste a block without commentary.
- Ask students to change **one** cosmetic (`color` or `linewidth`) so they edit safely.

**Students**

- Reproduce the line plot; optionally tweak styling.

**Bridge Sentence:**  
*"Same library — different question: instead of trend over time, we compare categories side by side."*

---

## 5. Bar Chart & Histogram (19 minutes)

**Facilitator actions**

- Bar chart: categories vs values — scoreboard analogy. Live-code `plt.bar` with the product/revenue example; mention colour list briefly.
- Histogram: **different purpose** than bar chart — one numeric column, bins = ranges. Live-code `plt.hist` with `bins`, `edgecolor`.
- **Check for understanding:** *“When would you use a bar chart vs a histogram?”* — quick show of hands or chat ping.
- Mention bins guidance (start 10–15; avoid too few / too many).

**Students**

- Build both chart types on sample data; fix axis labels if charts look cramped.

**Bridge Sentence:**  
*"Static charts are great for slides — for exploration and demos, interactivity helps. That’s where Plotly comes in."*

---

## 6. Plotly Express — Interactive Bar (12 minutes)

**Facilitator actions**

- Contrast Matplotlib (static) vs Plotly (hover, zoom). Ensure environment has `plotly` installed; if not, show your screen and describe interactions while students note install for later.
- Live-code `px.bar` with `x`, `y`, `color`, `title`, `fig.show()` — narrate DataFrame-first workflow vs manual lists.
- Have everyone **hover** one bar and read the tooltip aloud if doing interactive follow-along.

**Students**

- Run `px.bar` or observe facilitator demo; note browser popup behaviour.

**Bridge Sentence:**  
*"Bar is one shape — Plotly also gives us lines and scatter for trends and relationships."*

---

## 7. Plotly Line & Scatter + Choosing the Right Chart (17 minutes)

**Facilitator actions**

- Show `px.line` (dates/prices) and `px.scatter` (age vs spend, `color`, `size`). Keep datasets small so plots render quickly.
- Display the “Question → Best Chart” table from the notes — walk through each row quickly.
- Highlight common mistakes (pie with too many slices; line for unordered categories; bar for distribution).
- Short activity: show a **wrong** chart choice on screen — *“What would you use instead?”* — cold-call or chat.

**Students**

- Run line and scatter if time; otherwise prioritise watching + noting chart-choice rules.

**Bridge Sentence:**  
*"A chart alone isn’t a decision — we need to turn it into a message. That’s data storytelling."*

---

## 8. Data Storytelling & Annotations (14 minutes)

**Facilitator actions**

- Three pillars: Data, Visuals, Narrative — one slide or verbal only.
- Techniques: insight-first title, declutter, annotations, lead with conclusion.
- Live-code or demo `plt.annotate()` on the sales spike example (`xy`, `xytext`, `arrowprops`). Explain arrow points **to** the spike.
- **Pair-share:** *“Rewrite a vague title into an insight-first title.”* — e.g., “Monthly Sales” → “Sales Grew in Q2.”

**Students**

- Follow annotation demo; draft one better chart title with a partner.

**Bridge Sentence:**  
*"Let’s lock in what you’ll remember after today — and what comes next in the course."*

---

## 9. Key Takeaways & Close (12 minutes)

**Facilitator actions**

- Rapid-fire recap: EDA first; Matplotlib building blocks; Plotly interactivity; chart choice; storytelling + annotations.
- Point to the “Important Commands” table in the Lecture Notes as their cheat sheet.
- Mention upcoming sessions (dashboards, real datasets, AI-assisted workflow) in one sentence.
- Open floor for questions; if time remains, run one **quick revision poll** (e.g., histogram vs bar chart).

**Students**

- Ask questions; note resources for practice.

**Bridge Sentence:**  
*"Thank everyone — send them off with the notes link and any assignment portal."*

---

## Timing Flex — If You Are Running Late

**Cut or shorten (in order)**  

1. **Pair-share activities** — turn into single cold-call or skip one pair-share (saves ~3–5 minutes each).
2. **Plotly line + scatter block** — demo only `px.line` **or** only `px.scatter`, and summarise the other from the table (saves ~8–10 minutes).
3. **Outlier discussion** — keep one example row from the signals table, skip extended discussion (saves ~5 minutes).
4. **Annotation live-code** — show finished annotated chart and explain parameters instead of typing full cell (saves ~5–7 minutes).
5. **Opening recap** — shorten SQL recap to one sentence (saves ~3 minutes).

**Protect if possible**  

- EDA checklist steps 1–2 (`info`, missing values) — foundation for everything else.
- One complete Matplotlib chart (line **or** bar) — confidence builder for beginners.
- Chart-choice table — prevents persistent mistakes later.

**If you are ahead**  

- Let students reproduce Plotly examples locally with their own column names.
- Deepen “wrong chart” discussion with a second example.
