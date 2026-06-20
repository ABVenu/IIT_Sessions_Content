```mermaid
%%{init: {'flowchart': {'nodeSpacing': 45, 'rankSpacing': 55, 'padding': 20}}}%%
flowchart TB
  subgraph foundation[" "]
    direction TB
    M1["<b>Previous Module</b><br/>Module 1: Foundations<br/><i>(Python, Data, APIs)</i><br/>Python → Pandas, SQL, JSON, APIs"]
    M2["<b>Previous Module</b><br/>Module 2: Fundamentals of ML<br/><i>(Workflow, Models)</i><br/>Splits, regression, classification, clustering"]
  end

  subgraph path[" "]
    direction TB
    M3U["<b>Current Module Until Previous Session</b><br/>Module 3: GenAI &amp; Agents<br/><i>(RAG, tools, versioning)</i><br/>Retrieval, ReAct, prompt files, rate limits, retry logs"]
    CUR["<b>Current Session</b><br/>Structured Outputs for Agents<br/><i>Mental shift</i><br/>JSON schema · structured generation · parse · validate"]
  end

  subgraph value[" "]
    direction LR
    CV["<b>Course value</b><br/>Reliable machine-readable agent answers before you wire tools and UI"]
    RL["<b>Real-life value</b><br/>Dashboards, routers, and APIs that trust every model reply"]
  end

  subgraph future[" "]
    direction TB
    M4["<b>Upcoming Module</b><br/>Module 4: Agentic Systems &amp; Design<br/><i>(Orchestration, Ops)</i><br/>Guardrails, LangGraph, eval gates, deploy, capstone"]
  end

  M1 ==>|&nbsp;Foundation&nbsp;| M2
  M2 ==>|&nbsp;Components&nbsp;| M3U
  M3U ==>|&nbsp;Shape the output&nbsp;| CUR
  CUR ==>|&nbsp;Course path&nbsp;| CV
  CUR ==>|&nbsp;Real-life use&nbsp;| RL
  CUR ==>|&nbsp;Next module&nbsp;| M4

  classDef prev fill:#e3f2fd,stroke:#1565c0,color:#0d47a1
  classDef currMod fill:#fffde7,stroke:#f9a825,color:#5d4037
  classDef currSes fill:#ffe0b2,stroke:#ef6c00,color:#4e342e,stroke-width:3px
  classDef val fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20
  classDef fut fill:#fce4ec,stroke:#ad1457,color:#880e4f

  class M1,M2 prev
  class M3U currMod
  class CUR currSes
  class CV,RL val
  class M4 fut

  linkStyle default stroke-width:3px
```
