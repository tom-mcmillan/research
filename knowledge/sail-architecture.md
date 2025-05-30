# Sail - A combination of Codex and Agents

## Theory of the Case
To empower researchers with a seamless, natural-language–driven knowledge-creation terminal, we will combine Codex’s rich, local-first UI and file-I/O capabilities with the OpenAI Agents SDK’s robust orchestration and modular agent framework. We’ll leave both codebases’ core functionalities untouched—Codex’s Rust engine and Ink-based TUI, and the Agents SDK’s agent/tool lifecycle and context handling—and introduce a thin “glue” layer of:

CodexAgent (an Agents SDK Tool) that calls Codex’s MCP HTTP endpoints for text-generation and file operations.

Domain Agents (DialogueAgent, CaseTheoryAgent, ArtifactAgent, MemoryAgent, CollaborationAgent) implemented in Python, orchestrated by the existing SDK.

Intent Parsing at the front of the orchestrator to map freeform English input into agent workflows.

This approach preserves low-latency local editing, maximizes maintainability by decoupling concerns, and creates a powerful, unified terminal experience.

## Diagrams (Diff)

These diagrams and the theory of the case together explain why we’re combining Codex and the Agents SDK, how we’ll glue them via the MCP protocol, and what parts remain untouched versus what we’re adding to realize a unified, natural-language–driven research terminal.

### Layered Architecture (Combined)

┌────────────────────────────────────────────────────────────┐
│ 1. User Interface (Codex TUI in Node/TypeScript & Rust)    │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│ 2. Protocol Layer (MCP Server & mcp-types schemas in Rust) │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│ 3. Agents SDK Orchestrator (run.py, lifecycle, handoffs)   │
└────────────────────────────────────────────────────────────┘
                          │
            ┌─────────────┼─────────────┐
            ▼             ▼             ▼
┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ 4a. Agents     │ │ 4b. Tools      │ │ 5. External    │
│  (Python)      │ │  (Python tools │ │    Services    │
│                │ │   including    │ │ (Codex MCP,    │
│ Dialogue,      │ │   CodexAgent)  │ │  FS, Git, DB)  │
│ CaseTheory,    │ └────────────────┘ └────────────────┘
│ Artifact, etc. │
└────────────────┘

### Component Dependency Graph

     +-----------------+          +-------------------+
     |  Codex TUI      |          |  Agents SDK CLI   |
     |(cli.tsx/app.tsx)|          |   (run.py)        |
     +--------+--------+          +---------+---------+
              │                             │
              │  JSON over HTTP / stdio     │
              ▼                             ▼
     +-----------------------------------------------+
     |             MCP Server (Rust)                 |
     +----------------+------------------------------+
                      │
                      │
                      ▼
     +-----------------------------------------------+
     |       Agents SDK Orchestration Engine         |
     |   (agent.py)───┬───(tool.py)───┬── CodexAgent |
     |      │         │              └── FileTool    |
     |      ▼         ▼                              |
     |  DomainAgents  Tools                          |
     +-----------------------------------------------+
                      │
                      ▼
             External Services (FS, Git, DB)

### Sequence Flow (Typical User Prompt)

User types English → Codex TUI captures input 
        │
        ▼
Intent Agent (in orchestrator) classifies “save case theory” 
        │
        ▼
Orchestrator invokes:
  ├─ CaseTheoryAgent.run(context) 
  ├─ ArtifactAgent.run(context) 
  └─ CodexTool.saveFile({path, content})
        │
        ▼
CodexAgent (via HTTP) calls MCP Server → engine applies edits/creates file
        │
        ▼
Orchestrator updates Context, logs output
        │
        ▼
Codex TUI renders success message & updated buffer

### Top-Level Structure of the Combined Solution

my-knowledge-terminal/
├─ codex-main/             ← upstream Codex repo (untouched)
│   ├─ codex-rs/           ← Rust engine & protocol
│   └─ codex-cli/          ← Node TUI & file utils
├─ openai-agents-python/   ← upstream Agents SDK (untouched)
│   └─ src/agents/         ← orchestrator, agents, tools
└─ orchestrator-glue/      ← our new integration layer
    ├─ codex_service.ts    ← Thin HTTP shim (optional)
    ├─ python-setup/       ← venv & requirements for Agents SDK
    └─ workflows/          ← JSON/YAML workflow definitions

### Main Workspaces & Core Components

┌───────────────┐       ┌────────────────────────┐
│  codex-main   │       │ openai-agents-python   │
│ (Rust & TS UI)│       │ (Python SDK)           │
├───────────────┤       ├────────────────────────┤
│ codex-rs/     │       │ src/agents/run.py      │
│  ├ mcp-types  │       │ src/agents/agent.py    │
│  ├ mcp-server │       │ src/agents/tool.py     │
│  └ mcp-client │       │ src/agents/handoffs.py │
│ codex-cli/    │       │ src/agents/lifecycle.py│
│  ├ src/cli.tsx│       │ src/agents/...         │
│  └ src/app.tsx│       └────────────────────────┘
└───────────────┘
       ▲                        ▲
       └────────┬───────────────┘
                ▼
      orchestrator-glue/
      ├ CodexTool (wraps MCP)
      ├ IntentAgent
      ├ Domain Agents
      └ Workflow Definitions

## Diagrams (Integrated & Descriptive)

### Conceptual Layered Stack (Integrated)

- The UI is more than just Codex or a sidebar—it’s a KnowledgeTerminalUI that blends freeform chat, intent parsing, and TUI elegance into one.
- The Orchestration Core merges the SDK’s agent sequencing with case-theory and domain logic into a unified flow.
- The Integration Layer doesn’t just glue; it enriches: Codex becomes one of many agents, while all tools live in a common registry.

┌────────────────────────────────────────────────────────────┐
│                     KnowledgeTerminalUI                    │
│     (Codex TUI + Intent Parsing + Domain Chat Agent)       │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│                    Orchestration Core                      │
│  (Agents SDK Engine + CaseTheory, Artifact, Memory,        │
│    Collaboration Agents all speaking a unified Context)    │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│                 Protocol & Integration Layer               │
│   (MCP “CodexAgent” → Rust Engine, FileAgent → FS/Git,     │
│     NetworkAgent → Peer Exchange, DBAgent → DB)            │
└────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌────────────────────────────────────────────────────────────┐
│                   External Services & Storage              │
│         (Codex Rust Engine, Local FS/Git, Databases,       │
│            External APIs, Peer Nodes)                      │
└────────────────────────────────────────────────────────────┘

### Physical Directory Layout (Descriptive)

Here, integration/ holds only our new layers; the original repos stay intact under their own folders.

knowledge-terminal/
├─ codex-main/                  # upstream Codex repo
│   ├─ codex-rs/                # Rust engine & MCP protocol
│   └─ codex-cli/               # TypeScript Ink UI & file utils
├─ agents-sdk/                  # upstream Agents SDK
│   └─ src/agents/              # orchestrator & base Agent/Tool classes
├─ integration/                 
│   ├─ ui/                      
│   │   └─ intent-parser.ts     # maps English → Agent Intents
│   ├─ agents/                  
│   │   ├─ DialogueAgent.py     
│   │   ├─ CaseTheoryAgent.py   
│   │   ├─ ArtifactAgent.py     
│   │   ├─ MemoryAgent.py       
│   │   └─ CollaborationAgent.py
│   ├─ tools/                   
│   │   ├─ CodexAgent.py        # wraps MCP endpoints
│   │   ├─ FileAgent.py         # wraps codex-cli file utils + git
│   │   ├─ NetworkAgent.py      # peer exchange logic
│   │   └─ DBAgent.py           # optional DB-based memory
│   └─ workflows/               
│       └─ default_workflow.yaml
└─ scripts/                     
    ├─ start_terminal.sh        # launches Codex UI + orchestrator
    └─ deploy_agents.sh         # CI/CD helpers

### Data & Control Flow (Integrated)

Notice the “mix”: each step can call either Codex’s protocol or other services (file, DB, network), orchestrated by the same core engine.

User types “Summarize my case theory and save it.”

           │
           ▼
[KnowledgeTerminalUI]
 (Ink TUI + intent-parser)
           │  intent=”save-case-theory”
           ▼
[Orchestration Core]
  ├─ DialogueAgent (confirm intent)
  ├─ CaseTheoryAgent (synthesize text)
  ├─ ArtifactAgent (produce JSON artifact)
  ├─ FileAgent → CodexAgent (via MCP) & Git commit
  └─ MemoryAgent (index artifact)
           │
           ▼
[Protocol & Integration Layer]
 (Codex MCP, FS/Git, DB, Network)
           │
           ▼
[External Systems]
 (Rust Engine, Disk, DB, Peers)
           │
           ▼
UI shows “✅ Case theory saved to projects/case-2025-05-22.md”

### User Journey & Experience Flow

1. Launch Terminal  ➞   ./start_terminal.sh
     │
2. Terminal Opens   ➞   KnowledgeTerminalUI greets you
     │
3. Type a Prompt    ➞   “Draft a case theory for my research.”
     │
4. Intent Parsing   ➞   IntentAgent labels it “case-theory”
     │
5. Agent Orchestration
     ├─ CaseTheoryAgent synthesizes text  
     ├─ ArtifactAgent captures JSON snapshot  
     └─ FileAgent & CodexAgent save Markdown + git commit
     │
6. UI Feedback      ➞   “✅ Case theory saved: case-2025-05-22.md”
     │
7. Continue Chat    ➞   “Can you suggest related past artifacts?”
     │
8. MemoryAgent     ➞   Retrieves and shows past insights  
     │
…repeat…

### Data Flow Diagram

[User Input]
     │
     ▼
[KnowledgeTerminalUI]
     │
     ▼  “intent”: “generate”
[Intention Agent]
     │
     ▼
[Orchestration Core]
     │
     ├─► [DialogueAgent] ──► (new text)  
     │
     ├─► [CaseTheoryAgent] ──► (theory text)  
     │
     ├─► [ArtifactAgent] ──► (artifact JSON)  
     │
     ├─► [CodexAgent] ──► [MCP Server] ──► [Rust Engine]  
     │                                           │
     │                                           ▼
     │                                      (edits/text)
     │                                           │
     │◄──────────────────────────────────────────┘
     │
     └─► [FileAgent] ──► [Local FS & Git]

### Technology Stack & Responsibility Map

+----------------------+      +----------------------+      +----------------------+
|   KnowledgeTerminal  |      | Orchestration Core   |      | External Integrations|
|   (Node.js + Ink)    |      | (Python + Agents SDK)|      |  • Rust Engine (MCP) |
|  • UI & Input Hooks  |◀─────|  • Context Manager   |─────▶|  • File System & Git |
|  • Intent Parser     |      |  • Agent Sequencer   |      |  • Database / Network|
+----------------------+      +----------------------+      +----------------------+
         ▲  │                         ▲    │                        ▲    │
         │  └─────calls CodexAgent────┘    └─────invokes Tools──────┘    │
         │                                                               │
         └──────────────────────────logs & events────────────────────────┘


### integrated Knowledge Terminal stack

┌────────────┐   ┌────────────────────────────┐   ┌────────────────────┐   ┌───────────────┐
│  codex-rs  │◄─▶│         MCP Layer          │◄─▶│    Agents SDK      │◄─▶│  codex-cli    │
│ (Rust Core)│   │┌─ mcp-types (schemas)      │   │┌─ Agent classes    │   │ (Node TUI &   │
│            │   ││                           │   ││  • DialogueAgent  │   │  file utils)  │
│ • apply-   │   │├─ mcp-server (HTTP/stdio)  │   │├─ CaseTheoryAgent  │   │               │
│   patch    │   ││  endpoints                │   ││  …                │   │ • commands/   │
│ • exec-    │   │├─ mcp-client (Rust client) │   │├─ ArtifactAgent    │   │ • hooks/      │
│   policy   │   ││  lib for HTTP/stdio calls │   ││  …                │   │ • utils/      │
│ • LLM calls│   │└────────────────────────── ┘   │└─ Tool classes     │   │ • cli.tsx/    │
│ • evidence │                                │   │  • CodexTool (wraps│   │   app.tsx     │
│   gather   │                                │   │    MCP calls)      │   │               │
└────────────┘                                │   └────────────────────┘   └───────────────┘
       ▲                                      │
       │  JSON/Serde                          │  context.call_tool("codex", …)
       │  over HTTP or stdio                  │
       │                                      ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                             Integration Glue                                 │
│  • Intent Parser (classifies freeform English into agent intents)            │
│  • Workflow Definitions (YAML/JSON sequencing Dialogue → CaseTheory → …)     │
│  • Startup Scripts (launch Codex CLI + Agents SDK together)                  │
└──────────────────────────────────────────────────────────────────────────────┘

### More granular, multi-layered stack for the Knowledge Terminal

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                  1. User Interface Layer                                │
│   Codex TUI (Node/TS + Ink)                                                             │
│   • Captures freeform English input                                                     │
│   • Renders text buffers, status, and visualizations                                    │
└─────────────▲───────────────────────────────────────────────────────────────────────────┘
              │
              │ (1) in-memory callback / event
              │
┌─────────────┴───────────────────────────────────────────────────────────────────────────┐
│                                2. Intent Parsing Layer                                  │
│   IntentAgent (Python)                                                                  │
│   • Classifies each line as “chat,” “save-artifact,” “reality-test,” etc.               │
│   • Emits a structured Intent object                                                    │
└─────────────▲───────────────────────────────────────────────────────────────────────────┘
              │
              │ (2) direct Python function call
              │
┌─────────────┴───────────────────────────────────────────────────────────────────────────┐
│                            3. Orchestration / Control Layer                             │
│   Agents SDK Core (run.py, lifecycle, handoffs)                                         │
│   • Loads workflow definitions (YAML/JSON)                                              │
│   • Maintains central Context object                                                    │
│   • Sequences Agents according to the Intent & workflow                                 │
│   • Applies handoff rules to pass data between Agents                                   │
└─────────────▲───────────────────────────────────────────────────────────────────────────┘
              │
              │ (3) method invocation: context.call_agent()
              │
┌─────────────┴───────────────────────────────────────────────────────────────────────────┐
│                                  4. Agents Layer                                        │
│   Domain Agents (Python subclasses of Agent):                                           │
│     • DialogueAgent  – manages conversation flow                                        │
│     • CaseTheoryAgent – synthesizes case theory                                         │
│     • ArtifactAgent  – creates JSON knowledge artifacts                                 │
│     • MemoryAgent    – retrieves/contextualizes past artifacts                          │
│     • CollaborationAgent – handles peer artifacts exchange                              │
│   • Agents call Tools via context.call_tool()                                           │
└─────────────▲───────────────────────────────────────────────────────────────────────────┘
              │
              │ (4) method invocation: context.call_tool()
              │
┌─────────────┴───────────────────────────────────────────────────────────────────────────┐
│                                  5. Tools Layer                                         │
│   Tool Classes (Python subclasses of Tool):                                             │
│     • CodexTool     – wraps MCP endpoints                                               │
│     • FileTool      – wraps local FS & Git operations                                   │
│     • NetworkTool   – peer-to-peer artifact exchange                                    │
│     • VisualizationTool – on-demand diagrams/charts                                     │
│   • Tools perform side-effects and return structured responses                          │
└─────────────▲───────────────────────────────────────────────────────────────────────────┘
              │
              │ (5a) HTTP/STDIO JSON   (5b) FS/Git CLI   (5c) HTTP REST
              │
┌─────────────┴──────┬─────────────┬─────────────────────────────────────────────────┐
│      6a. Protocol  │  6b. Storage │                    7. Engine                   │
│      Layer         │  & VCS       │                Layer (codex-rs)                │
│                    │              │                                                │
│ • mcp-types        │ • Local FS   │ • apply-patch, exec-policy, LLM invocation     │
│   (JSON schemas)   │ • Git        │ • Evidence gathering & validation              │
│ • mcp-server       │ • Database   │ • Exposed over HTTP/stdio by mcp-server        │
│   (HTTP/STDIO)     │              │ • Drives actual text transformations           │
│ • mcp-client       │              │                                                │
│   (Rust client lib)│              │                                                │
└────────────────────┴──────────────┴────────────────────────────────────────────────┘


### Component-level diagram

+---------------------------------------------------------------------------------------+
|                                      UI Layer                                         |
|  +------------------+       +------------------------------------------------------+  |
|  | codex-cli/src/   |       | integration/ui/intent-parser.ts                      |  |
|  | ├─ cli.tsx       |◀──────┤  • classifyEnglishInput(text) → Intent object        |  |
|  | ├─ app.tsx       |       +------------------------------------------------------+  |
|  | ├─ commands/     |                                                           ▲     |
|  | └─ hooks/        |                                                           │     |
|  +------------------+                                                           │     |
+--------------------------------───▲─────────────────────────────────────────────┘     |
                                    │ (1) in-process event                               
                                    ▼                                                  
+--------------------------------───┴───────────────────────────────────────────────+  
|                               Orchestration Core                                  |  
|  integration/orchestrator/                                                        |  
|  ├─ run.py            (CLI entry, workflow loader)                                |  
|  ├─ lifecycle.py      (startup/shutdown hooks, logging)                           |  
|  └─ handoffs.py       (maps agent outputs → next input)                           |  
+------------------------------▲────────────────────────────────────────────────----+  
                               │ (2) context.call_agent()                              
                               ▼                                                      
+------------------------------┴────────────────────────────────────────────────-----+  
|                                   Agents Layer                                     |  
|  integration/agents/                                                               |  
|  ├─ DialogueAgent.py        (manages freeform conversation)                        |  
|  ├─ CaseTheoryAgent.py      (synthesizes case theory)                              |  
|  ├─ ArtifactAgent.py        (detects & serializes key insights)                    |  
|  ├─ MemoryAgent.py          (retrieves/presents past artifacts)                    |  
|  └─ CollaborationAgent.py   (peer artifact exchange)                               |  
+------------------------------▲────────────────────────────────────────────────-----+  
                               │ (3) context.call_tool()                                
                               ▼                                                      
+------------------------------┴────────────────────────────────────────────────-----+  
|                                   Tools Layer                                      |  
|  integration/tools/                                                                |  
|  ├─ CodexTool.py           (wraps MCP endpoints for generate/patch)                |  
|  ├─ FileTool.py            (wraps codex-cli utils + git commits)                   |  
|  ├─ NetworkTool.py         (HTTP REST for peer sharing)                            |  
|  └─ VisualizationTool.py    (on-demand diagrams & charts)                          |  
+------------------------------▲───────────┬────────────────────────────────────────+  
                               │ (4a) HTTP/STDIO│ (4b) FS/Git CLI │ (4c) HTTP       
                               ▼               ▼                  ▼               
+----------------───┬────────────────────────┬───────────────────┐  +----------------+
|      Protocol     │       Storage & VCS    │   External APIs   │  | codex-rs Engine|
| integration/mcp/  │                        │ integration/      |  | (Rust crates)  |
| ├─ mcp-types/     │ ├─ local filesystem    │ integration/      |  | • apply-patch  |
| │  (schemas)      │ │   (artifacts.md)     │ external          |  | • exec-policy  |
| ├─ mcp-server/    │ ├─ Git (commits)       │ search, etc.      |  | • LLM invocation|
| │  (HTTP/STDIO)   │ └──────────────────────┘                   |  | • evidence     |
| └─ mcp-client/    │                                            |  +----------------+
|    (Rust client)  │                                            |
+----------------───┴────────────────────────────────────────────+


| Component                | Code Location                                                    | Responsibility                                                       | Communicates With                                 |
| ------------------------ | ---------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------- |
| **UI Layer**             | `codex-cli/src/cli.tsx`, `app.tsx`                               | Captures freeform English, renders TUI                               | Calls **Intent Parser** via in-process callback   |
| **Intent Parsing**       | `integration/ui/intent-parser.ts`                                | Classifies English into structured Intent objects                    | Invokes **Orchestration Core** via function call  |
| **Orchestration Core**   | `integration/orchestrator/run.py`, `lifecycle.py`, `handoffs.py` | Loads workflows, manages central Context, sequences agents           | `context.call_agent()` to **Agents Layer**        |
| **Agents Layer**         | `integration/agents/*.py`                                        | Domain logic (Dialogue, CaseTheory, Artifact, Memory, Collaboration) | `context.call_tool()` to **Tools Layer**          |
| **Tools Layer**          | `integration/tools/*.py`                                         | Side effects (Codex MCP calls, FS/Git, network, visualization)       | HTTP/stdio to **Protocol**, FS/Git to **Storage** |
| **Protocol Layer (MCP)** | `codex-rs/mcp-types/`, `mcp-server/`, `mcp-client/`              | Defines JSON schemas, exposes HTTP/stdio endpoints, Rust client lib  | JSON over HTTP/stdio to **Engine Layer**          |
| **Storage & VCS**        | Local FS & Git (via `FileTool`)                                  | Persists artifacts, commits versioned markdown                       | Filesystem API / Git CLI from **Tools Layer**     |
| **Engine Layer (Rust)**  | `codex-rs/core/`, `apply-patch/`, `exec-policy/`                 | High-performance text patching, policy logic, LLM invocation         | Called by **mcp-server** via direct Rust function |
