```mermaid
%%{init: {'flowchart': {'nodeSpacing': 55, 'rankSpacing': 70, 'diagramPadding': 20}} }%%
flowchart TB
    subgraph Foundation["Foundation So Far"]
        M2["<b>Previous Module</b><br/>Fundamentals of ML<br/><i>Models + Evaluation</i><br/>Learnt prediction workflows and metric thinking"]
        M3["<b>Previous Module</b><br/>GenAI and Agents<br/><i>Chroma RAG + Tools</i><br/>Grounded generation and tool loops"]
        CM["<b>Current Module Until Previous Session</b><br/>Agentic Systems and Design<br/><i>Demo Ready</i><br/>PayDesk window, cost note, traces, retro"]
    end

    CS(["<b>Current Session</b><br/>Capstone Project Phase — Buffer and Submission<br/><i>Checklist + README + Stretch</i><br/>Pack a replay kit a stranger can run"])

    subgraph Value["Why This Matters"]
        CV["<b>Course Value</b><br/>Turns a live demo into artifacts an exam and reviewer can replay"]
        RV["<b>Real-Life Value</b><br/>Handover docs that keep the no-payout rule visible"]
    end

    subgraph Future["What This Enables Next"]
        U1["<b>Upcoming Module</b><br/>Program Close<br/><i>Support + Exam</i><br/>Remaining cases and UI polish — still no bank"]
    end

    M2 ==>|&nbsp;Foundation&nbsp;| M3
    M3 ==>|&nbsp;Demo&nbsp;| CM
    CM ==>|&nbsp;Pack&nbsp;| CS
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
