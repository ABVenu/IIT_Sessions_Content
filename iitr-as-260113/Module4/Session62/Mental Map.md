```mermaid
%%{init: {'flowchart': {'nodeSpacing': 55, 'rankSpacing': 70, 'diagramPadding': 20}} }%%
flowchart TB
    subgraph Foundation["Foundation So Far"]
        M4["<b>Previous Module</b><br/>Multi-Agent and Deployment<br/><i>Crews + Guardrails</i><br/>Roles, n8n, ops, and governance"]
        CM["<b>Current Module Until Previous Session</b><br/>Capstone Project<br/><i>Scaffolded Repo</i><br/>Doors, SQLite, samples, pipeline stub"]
    end

    CS(["<b>Current Session</b><br/>Prototyping a Multi-Agent System<br/><i>Tools + Memory + Eval</i><br/>Run CLEAN, HIGH, and BADGST live on PayDesk"])

    subgraph Value["Why This Matters"]
        CV["<b>Course Value</b><br/>Assembles LangChain, tools, RAG, and HITL into one demoable product"]
        RV["<b>Real-Life Value</b><br/>A CFO can watch a clean bill pass and a dirty bill stop"]
    end

    subgraph Future["What This Enables Next"]
        U1["<b>Upcoming Module</b><br/>Program Close<br/><i>Demo + Exam</i><br/>Support week: stamp UI, n8n courier, remaining eval cases"]
    end

    M4 ==>|&nbsp;Scaffold&nbsp;| CM
    CM ==>|&nbsp;Prototype&nbsp;| CS
    CS ==>|&nbsp;Course&nbsp;Path&nbsp;| CV
    CS ==>|&nbsp;Real-Life&nbsp;Use&nbsp;| RV
    CV ==>|&nbsp;Demo&nbsp;| U1
    RV ==>|&nbsp;Trust&nbsp;| U1

    classDef previous fill:#eef6ff,stroke:#4b83c4,color:#111827;
    classDef current fill:#fff4cc,stroke:#c79200,color:#111827,stroke-width:2px;
    classDef value fill:#ecfdf5,stroke:#2f855a,color:#111827;
    classDef future fill:#f5f3ff,stroke:#7c3aed,color:#111827;

    class M4,CM previous;
    class CS current;
    class CV,RV value;
    class U1 future;
    linkStyle default stroke-width:3px;
```
