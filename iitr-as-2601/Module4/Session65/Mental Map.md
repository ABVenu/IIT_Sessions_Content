```mermaid
%%{init: {'flowchart': {'nodeSpacing': 55, 'rankSpacing': 70, 'diagramPadding': 20}} }%%
flowchart TB
    subgraph Foundation["Foundation So Far"]
        M2["<b>Previous Module</b><br/>Fundamentals of ML<br/><i>Models + Evaluation</i><br/>Learnt prediction workflows and metric thinking"]
        M3["<b>Previous Module</b><br/>GenAI and Agents<br/><i>Chroma RAG + Tools</i><br/>Meaning shelf, function calling, structured JSON"]
        CM["<b>Current Module Until Previous Session</b><br/>Agentic Systems and Design<br/><i>Graphs + Ops</i><br/>LangGraph, golden eval, Streamlit, cache"]
    end

    CS(["<b>Current Session</b><br/>Capstone Project Phase — Build<br/><i>Job + Graph + Chroma</i><br/>Freeze PayDesk; extract, policy, route; stock the meaning shelf"])

    subgraph Value["Why This Matters"]
        CV["<b>Course Value</b><br/>Turns M3–M4 skills into one bounded money-harm product"]
        RV["<b>Real-Life Value</b><br/>AP files faster without skipping GST or high-value stamps"]
    end

    subgraph Future["What This Enables Next"]
        U1["<b>Upcoming Module</b><br/>Program Close<br/><i>Window + Submit + Exam</i><br/>One meeting: polish the counter, pack evidence, defend the gates"]
    end

    M2 ==>|&nbsp;Foundation&nbsp;| M3
    M3 ==>|&nbsp;Hardening&nbsp;| CM
    CM ==>|&nbsp;New&nbsp;Product&nbsp;| CS
    CS ==>|&nbsp;Course&nbsp;Path&nbsp;| CV
    CS ==>|&nbsp;Real-Life&nbsp;Use&nbsp;| RV
    CV ==>|&nbsp;Window and Handover&nbsp;| U1
    RV ==>|&nbsp;Trust&nbsp;| U1

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
