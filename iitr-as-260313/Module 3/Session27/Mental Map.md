```mermaid
%%{init: {"flowchart": {"nodeSpacing": 70, "rankSpacing": 90, "diagramPadding": 24}} }%%
flowchart TB
  subgraph Foundation["What Students Bring Into This Session"]
    M1["<b>Previous Module</b><br/>Agentic Foundation & Architecture<br/><i>[Python + LLM Basics]</i><br/>Agents, prompts, model providers"]
    M2["<b>Previous Module</b><br/>Agent Components - Memory, Tools & RAG<br/><i>[Memory + Retrieval]</i><br/>Databases, embeddings, RAG, APIs, tools"]
    CM["<b>Current Module Until Previous Session</b><br/>Hands-On Single-Agent Development<br/><i>[Ollama + LangChain Concepts]</i><br/>Local/cloud LLMs, Runnables, LCEL, first demo chain"]
  end

  CS{{"<b>Current Session</b><br/>LangChain Environment Setup and First LCEL Chain<br/><i>[venv + LCEL Pipeline]</i><br/>Move from concept to a running project: build and prove your first chain end-to-end on Ollama"}}

  subgraph Value["Why This Matters"]
    CV["<b>Course Value</b><br/>A clean, reproducible LangChain workspace<br/>The base every later agent builds on"]
    RV["<b>Real-Life Value</b><br/>Set up secure projects with .env and isolated deps<br/>Ship a working prompt-to-output pipeline"]
  end

  subgraph Future["Where This Leads"]
    F3["<b>Current Module Path</b><br/>Hands-On Single-Agent Development<br/><i>[Tools + Agents + RAG]</i><br/>Tool calling, agent loops, memory, evaluation"]
    F4["<b>Upcoming Module</b><br/>Multi-Agent Collaboration and Deployment<br/><i>[CrewAI + n8n]</i><br/>Role-based agents, automation, deployment"]
    F5["<b>Upcoming Module</b><br/>Capstone Project - Autonomous System Build<br/><i>[Design + Prototype]</i><br/>End-to-end agent system"]
  end

  M1 ==>|&nbsp;Foundation&nbsp;| M2
  M2 ==>|&nbsp;Components&nbsp;| CM
  CM ==>|&nbsp;Setup Time&nbsp;| CS
  CS ==>|&nbsp;Course Path&nbsp;| CV
  CS ==>|&nbsp;Real-Life Use&nbsp;| RV
  CS ==>|&nbsp;Next Steps&nbsp;| F3
  F3 ==>|&nbsp;Next Module&nbsp;| F4
  F4 ==>|&nbsp;Capstone Prep&nbsp;| F5

  classDef previous fill:#eef6ff,stroke:#4b83c3,stroke-width:2px,color:#0f2540;
  classDef current fill:#fff4cc,stroke:#d99a00,stroke-width:3px,color:#2d2100;
  classDef value fill:#eefaf1,stroke:#4c9f63,stroke-width:2px,color:#16351f;
  classDef future fill:#f4efff,stroke:#7b61c8,stroke-width:2px,color:#261c45;

  class M1,M2,CM previous;
  class CS current;
  class CV,RV value;
  class F3,F4,F5 future;
  linkStyle default stroke-width:3px;
```
