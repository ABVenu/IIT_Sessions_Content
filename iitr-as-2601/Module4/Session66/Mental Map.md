```mermaid
%%{init: {'flowchart': {'nodeSpacing': 55, 'rankSpacing': 70, 'diagramPadding': 20}} }%%
flowchart TB
    subgraph Foundation["Foundation So Far"]
        M2["<b>Previous Module</b><br/>Fundamentals of ML<br/><i>Models + Evaluation</i><br/>Learnt prediction workflows and metric thinking"]
        M3["<b>Previous Module</b><br/>GenAI and Agents<br/><i>Chroma RAG + Tools</i><br/>Meaning shelf and structured outputs"]
        CM["<b>Current Module Until Previous Session</b><br/>Agentic Systems and Design<br/><i>PayDesk Core</i><br/>LangGraph, Chroma policy, golden G01–G03"]
    end

    CS(["<b>Current Session</b><br/>Capstone Project Phase — Polish, Demo and Submit<br/><i>Window + Receipt + Replay kit</i><br/>Streamlit on the same graph, traces as proof, README a stranger can run"])

    subgraph Value["Why This Matters"]
        CV["<b>Course Value</b><br/>Turns a passing graph into a demo and a handover an exam can replay"]
        RV["<b>Real-Life Value</b><br/>A CFO sees one bill pass and one bill stop; Monday’s clerk follows the guide"]
    end

    subgraph Future["What This Enables Next"]
        U1["<b>Upcoming Module</b><br/>Program Close<br/><i>Support + Exam</i><br/>Remaining cases and UI polish — still no bank"]
    end

    M2 ==>|&nbsp;Foundation&nbsp;| M3
    M3 ==>|&nbsp;Build&nbsp;| CM
    CM ==>|&nbsp;Counter and Pack&nbsp;| CS
    CS ==>|&nbsp;Course&nbsp;Path&nbsp;| CV
    CS ==>|&nbsp;Real-Life&nbsp;Use&nbsp;| RV
    CV ==>|&nbsp;Exam&nbsp;| U1
    RV ==>|&nbsp;Handover&nbsp;| U1

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
