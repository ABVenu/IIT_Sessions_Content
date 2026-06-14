```mermaid
%%{init: {"flowchart": {"nodeSpacing": 45, "rankSpacing": 65, "diagramPadding": 20}} }%%
flowchart TB
    subgraph Foundation["Foundation Built So Far"]
        P1(["Previous Module<br/><b>Agentic Foundation &amp; Architecture</b><br/><i>Python, prompts</i><br/>Programming basics, LLM behaviour, agent thinking"])
        C1[["Current Module Until Previous Session<br/><b>Memory, Tools &amp; RAG — Quality Track</b><br/><i>Loaders, chunking, evaluation</i><br/>ShopKart RAG built, tested, and improved end-to-end"]]
    end

    CS{{"Current Session<br/><b>Working with APIs and JSON</b><br/><i>REST, HTTP, JSON parsing</i><br/>API foundation — GET, status codes, parse JSON in terminal"}}

    subgraph Value["Why This Matters"]
        CV(["Course Value<br/><b>Bridge RAG to Tools</b><br/>Understand how agents talk to systems beyond document search"])
        RV(["Real-Life Value<br/><b>Live Data Assistants</b><br/>Order status, weather, rates — not only PDF policies"])
    end

    subgraph Future["Where This Leads Next"]
        F1(["Upcoming Module<br/><b>Hands-On Single-Agent Development</b><br/><i>Ollama, LangChain</i><br/>Agents that call tools inside workflows"])
        F2(["Upcoming Module<br/><b>Multi-Agent Collaboration</b><br/><i>n8n, CrewAI</i><br/>Connect agents to automation and teams"])
        F3(["Upcoming Module<br/><b>Capstone Project</b><br/><i>System design, deployment</i><br/>Autonomous agentic solution"])
    end

    P1 ==>|&nbsp;Foundation&nbsp;| C1
    C1 ==>|&nbsp;Blueprint&nbsp;| CS
    CS ==>|&nbsp;Course Path&nbsp;| CV
    CS ==>|&nbsp;Real-Life Use&nbsp;| RV
    CV ==>|&nbsp;Build&nbsp;| F1
    F1 ==>|&nbsp;Scale&nbsp;| F2
    F2 ==>|&nbsp;Apply&nbsp;| F3

    classDef previous fill:#eef4ff,stroke:#4f7ccf,color:#111827,stroke-width:2px;
    classDef current fill:#fff4d6,stroke:#d9a321,color:#111827,stroke-width:3px;
    classDef value fill:#eaf8ef,stroke:#3f9f63,color:#111827,stroke-width:2px;
    classDef future fill:#f4ecff,stroke:#8a61d1,color:#111827,stroke-width:2px;

    class P1,C1 previous;
    class CS current;
    class CV,RV value;
    class F1,F2,F3 future;
    linkStyle default stroke-width:3px;
```
