```mermaid
%%{init: {"diagramPadding": 24, "flowchart": {"htmlLabels": true, "nodeSpacing": 90, "rankSpacing": 110, "curve": "basis", "padding": 20}, "theme": "base", "themeVariables": {"fontFamily": "Arial", "fontSize": "15px", "lineColor": "#334155"}}}%%
flowchart TB
    subgraph FOUNDATION[" "]
        direction LR
        ENTRY["&nbsp;&nbsp;<b>Course Entry Point</b>&nbsp;&nbsp;<br/><br/>Certification in Agentic<br/>Systems and Design<br/><br/><i>No prior tech background<br/>required to begin</i>"]
        CM[["&nbsp;&nbsp;<b>Current Module Until Previous Session</b>&nbsp;&nbsp;<br/><br/>Module 1: Programming<br/>&amp; Python Foundations<br/><br/><i>Course begins here<br/>No prior sessions covered</i>"]]
    end

    CURRENT{{"&nbsp;&nbsp;<b>Current Session</b>&nbsp;&nbsp;<br/><br/>Introduction to Programming<br/>&amp; Python Basics<br/><br/><i>OneCompiler · variables · operators<br/>input and output</i><br/><br/><b>Mental shift:</b><br/>from app user<br/>to instruction writer"}}

    subgraph VALUE[" "]
        direction LR
        COURSE["&nbsp;&nbsp;<b>Course Connection</b>&nbsp;&nbsp;<br/><br/>First building block for Python logic,<br/>data handling, and the agentic<br/>systems you will design later<br/><br/><i>Foundation for all<br/>future coding work</i>"]
        REAL(["&nbsp;&nbsp;<b>Real-Life Connection</b>&nbsp;&nbsp;<br/><br/>UPI, train booking, WhatsApp,<br/>and AI agents all run on<br/>clear step-by-step logic<br/><br/><i>Learn to give machines<br/>precise directions</i>"])
    end

    subgraph FUTURE[" "]
        direction LR
        M2["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>Fundamentals of ML<br/>(Regression + Classification)<br/><br/><i>Will use: model training,<br/>evaluation, data prep</i>"]
        M3["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>GenAI &amp; Agents<br/>(LLMs + RAG + Tools)<br/><br/><i>Will use: prompts, retrieval,<br/>function calling</i>"]
        M4(["&nbsp;&nbsp;<b>Upcoming Module</b>&nbsp;&nbsp;<br/><br/>Agentic Systems &amp; Design<br/>(LangGraph + Deployment)<br/><br/><i>Will use: agent workflows,<br/>observability, capstone</i>"])
    end

    ENTRY ==>|&nbsp;Start&nbsp;| CM
    CM ==>|&nbsp;Foundation&nbsp;| CURRENT
    CURRENT ==>|&nbsp;Course Path&nbsp;| COURSE
    CURRENT ==>|&nbsp;Real-Life Use&nbsp;| REAL
    COURSE ==>|&nbsp;Next Module&nbsp;| M2
    M2 ==>|&nbsp;Next Module&nbsp;| M3
    M3 ==>|&nbsp;Next Module&nbsp;| M4

    classDef previous fill:#f8fafc,stroke:#475569,stroke-width:2px,color:#0f172a
    classDef current fill:#ecfeff,stroke:#0f766e,stroke-width:3px,color:#134e4a
    classDef value fill:#fff7ed,stroke:#c2410c,stroke-width:2px,color:#7c2d12
    classDef future fill:#f0fdf4,stroke:#15803d,stroke-width:2px,color:#14532d

    class ENTRY,CM previous
    class CURRENT current
    class COURSE,REAL value
    class M2,M3,M4 future

    style FOUNDATION fill:transparent,stroke:transparent
    style VALUE fill:transparent,stroke:transparent
    style FUTURE fill:transparent,stroke:transparent
    linkStyle default stroke:#334155,stroke-width:3px
```
