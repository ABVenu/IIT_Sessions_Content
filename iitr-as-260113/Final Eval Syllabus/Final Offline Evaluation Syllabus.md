# Certification in Agentic Systems and Design (IITRAS-260113)

## Final Offline Evaluation Syllabus

| S. No. | Lecture Title | Topics |
| --- | --- | --- |
| | **Module 1: Agentic Foundation & Architecture** | |
| 1 | Defining Agentic Systems | Agent definition ◆  autonomy vs automation ◆  perception-reasoning-action loop ◆  agents vs chatbots vs copilots |
| 2 | Core Components of AI Agents | Planning ◆  reasoning ◆  memory ◆  tool use ◆  environment interaction ◆  feedback loops |
| 3 | Exploring Agent Behavior | Interacting with Claude/GPT agents ◆  observing reasoning traces ◆  identifying components in action |
| 4 | Business Case and Use Cases for Agents | Business value ◆  ROI analysis ◆  customer support agents ◆  financial analysis ◆  HR automation ◆  content creation ◆  research assistants |
| 5 | Understanding the LLM Layer: How LLMs Work Internally | Neural network foundations ◆  pretraining objectives ◆  next-token prediction ◆  training data and scale ◆  emergent capabilities |
| 6 | Transformer Fundamentals | Attention mechanism ◆  self-attention ◆  multi-head attention |
| 7 | LLM Selection for Agents | Model comparison (Claude, GPT-4, Gemini, Llama, Mistral) ◆  capability trade-offs ◆  cost vs latency vs quality |
| 8 | Prompt Engineering Fundamentals | System prompts ◆  role definition ◆  constraint specification ◆  output formatting ◆  few-shot prompting |
| 9 | Prompt Engineering Hands On | Writing agent personas ◆  capability definition ◆  testing variations ◆  measuring effectiveness |
| 10 | Python Essentials-1 | Python data structures ◆  functions and classes |
| 11 | Python Essentials-2 | Classes & Objects ◆  OOPS ◆  Exception Handling ◆  Numpy |
| 12 | Pydantic for Data Validation | Pydantic models ◆  field validators ◆  nested models ◆  serialization ◆  settings management |
| 13 | Python and Pydantic Hands-on | Building data models ◆  validation exercises ◆  async patterns ◆  type-safe components |
| 14 | FastAPI Fundamentals | FastAPI basics ◆  path operations ◆  request/response models ◆  dependency injection ◆  automatic docs |
| 15 | FastAPI & Databases | Database integration with FastAPI ◆  CRUD operations |
| 16 | FastAPI Advanced Patterns | Async endpoints ◆  middleware ◆  background tasks ◆  error handling |
| 17 | WebSockets in FastAPI | WebSocket support in FastAPI ◆  streaming |
| 18 | Introduction to Agent Frameworks | LangGraph ◆  LangChain ◆  CrewAI ◆  AutoGen ◆  n8n ◆  Google ADK ◆  Vercel AI SDK ◆  OpenAI Agents SDK ◆  framework comparison |
| | **Module 2: Agent Components - Memory, Tools & RAG** | |
| 19 | Advanced Prompt Engineering for Agents | chain-of-thought prompting ◆  structured prompts ◆  reasoning prompts |
| 20 | Self-Reflection and Feedback Loops | self-correction prompts ◆  iterative prompting ◆  agent prompt design |
| 21 | Introduction to Memory in AI Agents | why agents need memory ◆  stateless vs stateful agents ◆  types of agent memory |
| 22 | Short-Term vs Long-Term Memory | conversational memory ◆  persistent memory ◆  memory storage strategies ◆  (Main focus on Therotical discussion) |
| 23 | Introduction to Databases for AI Systems | relational databases ◆  SQL basics ◆  structured vs unstructured data |
| 24 | Using SQL Databases with AI Applications | querying databases ◆  database access patterns for agents |
| 25 | Embeddings and Semantic Representation | text embeddings ◆  semantic similarity |
| 26 | Introduction to Vector Databases | vector indexing ◆  similarity search |
| 27 | Implementing Vector Search Systems | storing embeddings ◆  querying vector DB |
| 28 | Introduction to RAG | limitations of LLM knowledge ◆  grounding responses |
| 29 | RAG Architecture and Pipeline | retriever ◆  generator ◆  knowledge sources |
| 30 | Building a RAG Pipeline | document loaders ◆  chunking |
| 31 | Evaluating and Improving RAG Systems | hallucination reduction ◆  retrieval tuning |
| 32 | Working with APIs and JSON | REST APIs ◆  JSON structures ◆  API responses |
| 33 | Tool Integration in AI Agents | function calling ◆  connecting APIs and tools |
| | **Module 3: Hands-On Single-Agent Development & Use Cases** | |
| 34 | Ollama: Exploring Another World of LLMs | Ollama install ◆  light model ◆  Python API ◆  Ollama Cloud ◆  dual-mode script |
| 35 | Introduction to LangChain: Concepts Architecture and First Demo | definition ◆  why framework ◆  stack placement ◆  Runnables ◆  modules overview ◆  Core vs Community ◆  PromptTemplate ◆  LCEL ◆  output parsers ◆  instructor demo chain |
| 36 | LangChain Environment Setup and First LCEL Chain | venv ◆  packages ◆  .env ◆  folders ◆  ChatOllama ◆  ChatPromptTemplate ◆  LCEL ◆  StrOutputParser ◆  hello_chain.py |
| 37 | LangChain Tools: Custom Tools and Tool Calling | @tool ◆  bind_tools ◆  tool_calls ◆  ToolMessage ◆  error handling |
| 38 | Building Your First LangChain Agent | create_tool_calling_agent ◆  AgentExecutor ◆  max_iterations ◆  test pack |
| 39 | LangChain Memory on Agents | MessagesPlaceholder ◆  chat_history ◆  multi-turn script ◆  message append |
| 40 | LangChain RAG Pipeline | loaders ◆  Chroma ◆  retriever ◆  LCEL RAG chain ◆  grounding comparison |
| 41 | RAG Tool and Integrated LangChain Agent | create_retriever_tool ◆  second tool ◆  multi-turn ◆  eval pack |
| 42 | Evaluating LangChain Agents: Test Sets and Logging | eval JSON ◆  runner ◆  results.csv ◆  failure trace |
| 43 | Debugging and Iterating LangChain Agents | failure class ◆  prompt/tool patch ◆  retrieval tune ◆  quality metrics |
| 44 | Hands-On Real-World Use Cases | finance use-case pattern ◆  HR onboarding implementation ◆  content use-case pattern ◆  integrated agent extension ◆  eval harness ◆  live demo ◆  module checklist |
| | **Module 4: Multi-Agent Collaboration and Deployment Strategy** | |
| 45 | Multi-Agent Architecture HTTP and Automation Foundations | single-agent vs multi-agent ◆  task decomposition ◆  role-based agents ◆  sequential vs collaborative workflows ◆  researcher-writer-editor pipeline ◆  HTTP methods ◆  triggers ◆  webhooks ◆  API automation |
| 46 | Introduction to n8n Workflow Automation | n8n workspace ◆  triggers ◆  nodes ◆  connections ◆  expressions ◆  credentials ◆  first workflow |
| 47 | n8n LLM Integration and AI Workflow Nodes | LLM nodes ◆  prompt configuration ◆  HTTP Request node ◆  chaining AI steps ◆  error branches |
| 48 | Building End-to-End AI Automation Pipelines with n8n | document ingestion ◆  summarization ◆  routing ◆  notifications ◆  pipeline testing ◆  workflow export |
| 49 | CrewAI: Roles Tasks and First Multi-Agent Crew | Agent ◆  Task ◆  Crew ◆  Process ◆  role-task-crew model ◆  tools per agent ◆  crew kickoff ◆  output artifacts |
| 50 | CrewAI: End-to-End Multi-Agent Workflow | custom tools ◆  hierarchical process ◆  sequential process ◆  memory optional ◆  output validation ◆  iteration |
| 51 | AutoGen: Conversable Agents and Tool Use | AssistantAgent ◆  UserProxyAgent ◆  conversable-agent model ◆  register_function ◆  code execution optional ◆  termination conditions |
| 52 | AutoGen: Group Chat and Multi-Agent Orchestration | GroupChat ◆  GroupChatManager ◆  speaker selection ◆  max rounds ◆  human input optional ◆  multi-agent handoffs |
| 53 | make.com: No-Code AI Automation Scenarios | scenarios ◆  modules ◆  routers ◆  OpenAI or HTTP modules ◆  data stores ◆  scheduling ◆  error handling |
| 54 | ChatGPT Agent and Hosted Agent Builder Patterns | ChatGPT Agent ◆  knowledge sources ◆  actions ◆  instructions ◆  guardrails ◆  hosted vs self-hosted trade-offs |
| 55 | LLM Operations, Security and Guardrails for Agent Systems | prompt and config versioning ◆  production eval gates ◆  token and cost tracking ◆  secrets and access ◆  PII handling ◆  input output guardrails ◆  policy layers ◆  human-in-the-loop |
| 56 | Deployment and Monitoring for Agent Systems | strategising deployment ◆  hosting and runtime choices ◆  environments ◆  observability ◆  monitoring workflows ◆  logging agent decisions ◆  trace and audit fields ◆  performance tracking ◆  incident response planning |
| 57 | Governance, Ethical Scaling and Cost Control for Agent Systems | AI governance ◆  data privacy ◆  bias and safety ◆  human oversight ◆  cost controls ◆  policies ◆  audit trails |
| 58 | Designing a Multi-Agent System for Business | workflow diagram ◆  agent roles ◆  handoffs ◆  tool and data map ◆  risks ◆  success metrics ◆  finance HR or content scenario |

*Note:*
*All the topics covered in the live sessions will be considered as part of the evaluation syllabus.*
