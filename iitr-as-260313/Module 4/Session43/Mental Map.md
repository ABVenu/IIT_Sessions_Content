```mermaid
%%{init: {"flowchart": {"nodeSpacing": 70, "rankSpacing": 90, "diagramPadding": 24}} }%%
flowchart TB
  subgraph Foundation["What Students Bring Into This Session"]
    M1["<b>Previous Module</b><br/>Agentic Foundation & Architecture<br/><i>[Python + LLM Basics]</i><br/>Prompts, APIs, agent concepts"]
    M2["<b>Previous Module</b><br/>Agent Components - Memory, Tools & RAG<br/><i>[Memory + Retrieval]</i><br/>Chunking, vectors, RAG pipeline"]
    M3["<b>Previous Module</b><br/>Hands-On Single-Agent Development<br/><i>[LangChain + eval loop]</i><br/>Tools, LCEL, AgentExecutor"]
  end

  CM[["<b>Current Module Until Previous Session</b><br/>Multi-Agent Collaboration and Deployment<br/><i>[CrewAI + AutoGen]</i><br/>Specialist crews and multi-agent dialogue"]]

  CS{{"<b>Current Session</b><br/>LangGraph Fundamentals and Setup<br/><i>[State + Nodes + Edges]</i><br/>Mental shift: a runnable map, not a hidden loop"}}

  subgraph Value["Why This Matters"]
    CV["<b>Course Value</b><br/>Control flow you can draw and trace"]
    RV["<b>Real-Life Value</b><br/>Know which step ran and why it branched"]
  end

  subgraph Future["Where This Leads"]
    F4["<b>Current Module Ahead</b><br/>Multi-Agent Collaboration and Deployment<br/><i>[E2E graph + ops]</i><br/>Full workflow, then go-live"]
    F5["<b>Upcoming Module</b><br/>Capstone Project - Autonomous System Build<br/><i>[Architecture + Prototype]</i><br/>LangGraph multi-agent prototype"]
  end

  M1 ==>|&nbsp;Foundation&nbsp;| M2
  M2 ==>|&nbsp;Components&nbsp;| M3
  M3 ==>|&nbsp;Scale up&nbsp;| CM
  CM ==>|&nbsp;Graph Control&nbsp;| CS
  CS ==>|&nbsp;Course Path&nbsp;| CV
  CS ==>|&nbsp;Real-Life Use&nbsp;| RV
  CS ==>|&nbsp;Next Steps&nbsp;| F4
  F4 ==>|&nbsp;Capstone Prep&nbsp;| F5

  classDef previous fill:#eef6ff,stroke:#4b83c3,stroke-width:2px,color:#0f2540;
  classDef current fill:#fff4cc,stroke:#d99a00,stroke-width:3px,color:#2d2100;
  classDef value fill:#eefaf1,stroke:#4c9f63,stroke-width:2px,color:#16351f;
  classDef future fill:#f4efff,stroke:#7b61c8,stroke-width:2px,color:#261c45;

  class M1,M2,M3,CM previous;
  class CS current;
  class CV,RV value;
  class F4,F5 future;
  linkStyle default stroke-width:3px;
```
