```mermaid
%%{init: {'flowchart': {'nodeSpacing': 55, 'rankSpacing': 70, 'diagramPadding': 20}} }%%
flowchart TB
    subgraph Foundation["Foundation So Far"]
        M2["<b>Previous Module</b><br/>Fundamentals of ML<br/><i>Models + Evaluation</i><br/>Learnt prediction workflows and metric thinking"]
        M3["<b>Previous Module</b><br/>GenAI & Agents<br/><i>RAG + Tools</i><br/>Built retrieval apps and agent flows"]
        CM["<b>Current Module Until Previous Session</b><br/>Agentic Systems & Design<br/><i>Safety + Multimodal</i><br/>Hardened agents and multimodal pipelines"]
    end

    CS(["<b>Current Session</b><br/>Agent Communication Patterns<br/><i>MasaiMato MCP</i><br/>AI orders food through a mini Zomato-style MCP server"])

    subgraph Value["Why This Matters"]
        CV["<b>Course Value</b><br/>Standard way for AI apps to reach tools and context"]
        RV["<b>Real-Life Value</b><br/>Menu, place order, track status — like food delivery apps"]
    end

    subgraph Future["What This Enables Next"]
        U1["<b>Upcoming Session Path</b><br/>LangGraph Basics<br/><i>Nodes + State</i><br/>Orchestrate steps on a visible workflow map"]
    end

    M2 ==>|&nbsp;Foundation&nbsp;| M3
    M3 ==>|&nbsp;Hardening&nbsp;| CM
    CM ==>|&nbsp;Standard&nbsp;Talk&nbsp;| CS
    CS ==>|&nbsp;Course&nbsp;Path&nbsp;| CV
    CS ==>|&nbsp;Real-Life&nbsp;Use&nbsp;| RV
    CV ==>|&nbsp;Orchestration&nbsp;| U1
    RV ==>|&nbsp;Workflow&nbsp;Maps&nbsp;| U1

    classDef previous fill:#eef6ff,stroke:#4b83c4,color:#111827;
    classDef current fill:#fff4cc,stroke:#c79200,color:#111827,stroke-width:2px;
    classDef value fill:#ecfdf5,stroke:#2f855a,color:#111827;
    classDef future fill:#f5f3ff,stroke:#7c3aed,color:#111827;

    class M2,M3,CM previous;
    class CS current;
    class CV,RV value;
    class U1 future;
    linkStyle default stroke-width:3px;
```
