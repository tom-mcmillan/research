┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                  1. User Interface Layer                               │
│   Codex TUI (Node/TS + Ink)                                                           │
│   • Captures freeform English input                                                   │
│   • Renders text buffers, status, and visualizations                                  │
└─────────────▲───────────────────────────────────────────────────────────────────────────┘
              │
              │ (1) in-memory callback / event
              │
┌─────────────┴───────────────────────────────────────────────────────────────────────────┐
│                                2. Intent Parsing Layer                                │
│   IntentAgent (Python)                                                               │
│   • Classifies each line as “chat,” “save-artifact,” “reality-test,” etc.            │
│   • Emits a structured Intent object                                                  │
└─────────────▲───────────────────────────────────────────────────────────────────────────┘
              │
              │ (2) direct Python function call
              │
┌─────────────┴───────────────────────────────────────────────────────────────────────────┐
│                            3. Orchestration / Control Layer                          │
│   Agents SDK Core (run.py, lifecycle, handoffs)                                      │
│   • Loads workflow definitions (YAML/JSON)                                           │
│   • Maintains central Context object                                                 │
│   • Sequences Agents according to the Intent & workflow                               │
│   • Applies handoff rules to pass data between Agents                                │
└─────────────▲───────────────────────────────────────────────────────────────────────────┘
              │
              │ (3) method invocation: context.call_agent()
              │
┌─────────────┴───────────────────────────────────────────────────────────────────────────┐
│                                  4. Agents Layer                                      │
│   Domain Agents (Python subclasses of Agent):                                        │
│     • DialogueAgent  – manages conversation flow                                      │
│     • CaseTheoryAgent – synthesizes case theory                                       │
│     • ArtifactAgent  – creates JSON knowledge artifacts                               │
│     • MemoryAgent    – retrieves/contextualizes past artifacts                        │
│     • CollaborationAgent – handles peer artifacts exchange                             │
│   • Agents call Tools via context.call_tool()                                         │
└─────────────▲───────────────────────────────────────────────────────────────────────────┘
              │
              │ (4) method invocation: context.call_tool()
              │
┌─────────────┴───────────────────────────────────────────────────────────────────────────┐
│                                  5. Tools Layer                                       │
│   Tool Classes (Python subclasses of Tool):                                           │
│     • CodexTool     – wraps MCP endpoints                                            │
│     • FileTool      – wraps local FS & Git operations                                 │
│     • NetworkTool   – peer-to-peer artifact exchange                                  │
│     • VisualizationTool – on-demand diagrams/charts                                    │
│   • Tools perform side-effects and return structured responses                        │
└─────────────▲───────────────────────────────────────────────────────────────────────────┘
              │
              │ (5a) HTTP/STDIO JSON   (5b) FS/Git CLI   (5c) HTTP REST
              │
┌─────────────┴──────┬─────────────┬─────────────────────────────────────────────────┐
│      6a. Protocol  │  6b. Storage │                    7. Engine                  │
│      Layer         │  & VCS       │                Layer (codex-rs)              │
│                    │              │                                             │
│ • mcp-types        │ • Local FS   │ • apply-patch, exec-policy, LLM invocation   │
│   (JSON schemas)   │ • Git        │ • Evidence gathering & validation            │
│ • mcp-server       │ • Database   │ • Exposed over HTTP/stdio by mcp-server      │
│   (HTTP/STDIO)     │              │ • Drives actual text transformations          │
│ • mcp-client       │              │                                             │
│   (Rust client lib)│              │                                             │
└────────────────────┴──────────────┴─────────────────────────────────────────────────┘
