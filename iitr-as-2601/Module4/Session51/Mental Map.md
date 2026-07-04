```mermaid
%%{init: {'flowchart': {'nodeSpacing': 55, 'rankSpacing': 70, 'diagramPadding': 20}} }%%
flowchart TB
    subgraph Foundation["Foundation So Far"]
        M2["<b>Previous Module</b><br/>GenAI & Agents<br/><i>RAG + Tools</i><br/>Built retrieval apps and agent flows"]
        M3["<b>Previous Module</b><br/>Agentic Systems & Design<br/><i>Safety + Guardrails</i><br/>Protected agents from unsafe inputs"]
        CM["<b>Current Module Until Previous Session</b><br/>Agentic Systems & Design<br/><i>Retrieval Tuning</i><br/>Measured and improved document search quality"]
    end

    CS(["<b>Current Session</b><br/>Multimodal Pipelines<br/><i>Speech + Vision</i><br/>Chain voice and image inputs into useful outputs"])

    subgraph Value["Why This Matters"]
        CV["<b>Course Value</b><br/>Extends text-only agents to real-world voice and photo inputs"]
        RV["<b>Real-Life Value</b><br/>Build assistants that listen, summarise, speak, and read images"]
    end

    subgraph Future["What This Enables Next"]
        U1["<b>Upcoming Module</b><br/>Agent Memory Architecture<br/><i>Short + Long Term</i><br/>Persist context across sessions safely"]
        U2["<b>Upcoming Module</b><br/>Agent Communication<br/><i>Planner + Executor</i><br/>Design multi-step agent workflows"]
        U3["<b>Upcoming Module</b><br/>LLMOps & Deployment<br/><i>Eval + Release</i><br/>Ship agents with checks and evidence"]
    end

    M2 ==>|&nbsp;Foundation&nbsp;| M3
    M3 ==>|&nbsp;Hardening&nbsp;| CM
    CM ==>|&nbsp;Text Mastery&nbsp;| CS
    CS ==>|&nbsp;Course Path&nbsp;| CV
    CS ==>|&nbsp;Real-Life Use&nbsp;| RV
    CS ==>|&nbsp;Next Skills&nbsp;| U1
    U1 ==>|&nbsp;Builds Into&nbsp;| U2
    U2 ==>|&nbsp;Ships With&nbsp;| U3

    classDef previous fill:#eef6ff,stroke:#4b83c4,color:#111827;
    classDef current fill:#fff4cc,stroke:#c79200,color:#111827,stroke-width:2px;
    classDef value fill:#ecfdf5,stroke:#2f855a,color:#111827;
    classDef future fill:#f5f3ff,stroke:#7c3aed,color:#111827;

    class M2,M3,CM previous;
    class CS current;
    class CV,RV value;
    class U1,U2,U3 future;
    linkStyle default stroke-width:3px;
```
