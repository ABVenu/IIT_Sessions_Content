```mermaid
%%{init: {"flowchart": {"nodeSpacing": 55, "rankSpacing": 70, "diagramPadding": 20}} }%%
flowchart TB
  subgraph Foundation["Foundation Built So Far"]
    M1["<b>Previous Module</b><br/>Foundations<br/><i>Python, APIs</i><br/>Code, files, JSON, web calls"]
    M2["<b>Previous Module</b><br/>Machine Learning<br/><i>Models, Evaluation</i><br/>Train, test, compare, improve"]
    M3["<b>Previous Module</b><br/>GenAI &amp; Agents<br/><i>RAG, Tools</i><br/>Prompts, retrieval, memory, structured outputs"]
  end

  subgraph Current["Current Learning Moment"]
    CM["<b>Current Module Until Previous Session</b><br/>Agentic Systems &amp; Design<br/><i>Vision + Speech</i><br/>Recipe mini-app that checks inputs and can refuse"]
    CS(["<b>Current Session</b><br/>Agent Communication Patterns<br/><i>Planner + Executor</i><br/>Structured handoffs, then AI orders through a standard restaurant tool"])
  end

  subgraph Value["Why This Matters"]
    CV["<b>Course Value</b><br/>Clear messages between steps, and a standard way to reach outside tools"]
    RV["<b>Real-Life Value</b><br/>Plan the order, execute one ticket, stop when done or blocked"]
  end

  subgraph Future["Where This Leads"]
    F1["<b>Upcoming Module</b><br/>Workflow Graphs<br/><i>LangGraph Basics</i><br/>Draw nodes, state, and a runnable map"]
    F2["<b>Upcoming Module</b><br/>Reliability on Graphs<br/><i>Checkpoints, Retries</i><br/>Resume long runs after a pause"]
    F3["<b>Upcoming Module</b><br/>Observability, Deploy, Capstone<br/><i>Eval, UI, Demo</i><br/>Trace, ship, and defend the agent"]
  end

  M1 ==>|&nbsp;Foundation&nbsp;| M2
  M2 ==>|&nbsp;Model Habits&nbsp;| M3
  M3 ==>|&nbsp;Agent Skills&nbsp;| CM
  CM ==>|&nbsp;Clear Talk&nbsp;| CS
  CS ==>|&nbsp;Course Path&nbsp;| CV
  CS ==>|&nbsp;Real-Life Use&nbsp;| RV
  CS ==>|&nbsp;Next Step&nbsp;| F1
  F1 ==>|&nbsp;Design Depth&nbsp;| F2
  F2 ==>|&nbsp;Production Path&nbsp;| F3

  classDef previous fill:#EEF6FF,stroke:#4A90E2,stroke-width:2px,color:#111827
  classDef current fill:#FFF7E6,stroke:#F5A623,stroke-width:3px,color:#111827
  classDef value fill:#F0FFF4,stroke:#38A169,stroke-width:2px,color:#111827
  classDef future fill:#F7F0FF,stroke:#805AD5,stroke-width:2px,color:#111827

  class M1,M2,M3 previous
  class CM,CS current
  class CV,RV value
  class F1,F2,F3 future
  linkStyle default stroke-width:3px
```
