```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  subgraph foundation[" "]
    direction TB
    M1["<b>Previous Module</b><br/>Module 1: Foundations<br/><i>(Python, Data)</i><br/>Core Python → Pandas, SQL, plots"]
    M2["<b>Previous Module</b><br/>Module 2: Fundamentals of ML<br/><i>(Tabular ML)</i><br/>Regression, classification, trees, clustering, time series"]
  end

  subgraph path[" "]
    direction TB
    M3U["<b>Current Module Until Previous Session</b><br/>Live data pipeline built<br/><i>(REST, JSON, APIs)</i><br/>HTTP status · fetch · map fields → LLM prompts"]
    CUR["<b>Current Session</b><br/>Open-Source LLMs<br/><i>Mental shift</i><br/>Ollama install · Python API · cloud mode · secrets-safe setup"]
  end

  subgraph value[" "]
    direction LR
    CV["<b>Course value</b><br/>Own the model runtime before RAG and agent chains"]
    RL["<b>Real-life value</b><br/>Private, offline-capable AI on your laptop"]
  end

  subgraph future[" "]
    direction TB
    M3R["<b>Upcoming Module</b><br/>Module 3 continues: RAG &amp; agents<br/><i>(Retrieval, tools, graphs)</i><br/>Grounded generation · embeddings · tool use"]
    M4["<b>Upcoming Module</b><br/>Module 4: Agentic Systems &amp; Design<br/><i>(Orchestration, Ops)</i><br/>Deploy · eval · capstone"]
  end

  M1 ==>|&nbsp;Foundation&nbsp;| M2
  M2 ==>|&nbsp;Toolkit built&nbsp;| M3U
  M3U ==>|&nbsp;Run models locally&nbsp;| CUR
  CUR ==>|&nbsp;Course path&nbsp;| CV
  CUR ==>|&nbsp;Real-life use&nbsp;| RL
  CUR ==>|&nbsp;Next steps&nbsp;| M3R
  M3R ==>|&nbsp;Next module&nbsp;| M4

  classDef prev fill:#e3f2fd,stroke:#1565c0,color:#0d47a1
  classDef currMod fill:#fffde7,stroke:#f9a825,color:#5d4037
  classDef currSes fill:#ffe0b2,stroke:#ef6c00,color:#4e342e,stroke-width:3px
  classDef val fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20
  classDef fut fill:#fce4ec,stroke:#ad1457,color:#880e4f

  class M1,M2 prev
  class M3U currMod
  class CUR currSes
  class CV,RL val
  class M3R,M4 fut

  linkStyle default stroke-width:3px
```
