# Knowledge Terminal Case Theory and Reality Testing

## 1. Core Idea: 
Our “case” is your vision of a unified, natural-language research terminal. The theory of the case explains how combining Codex’s UI/engine and the Agents SDK’s orchestration delivers that vision, from your perspective as both developer and first user.

### Declarative Case Theory Statement

“By embedding Codex’s rich TUI and file-I/O as a service within a lightweight Agents SDK orchestrator—where each user prompt flows through Intent → Dialogue → CaseTheory → Artifact → Memory agents—we create a seamless, client-centered terminal that captures every insight as immutable, versioned artifacts and surfaces past knowledge on demand.”

### Why it matters to you (the “client”): 
You get a single workspace that feels familiar, yet is powered by modular AI “specialists.”

How it shapes everything: Every design and implementation choice (from where to hook into the UI, to how tools are named) orients back to this statement.

## 2. Reality-Testing Our Theory
Using Loewald’s richer definition of reality-testing, we don’t just check “Is this technically feasible?” but we also probe where our “fantasy” of a perfect terminal might clash with the “actual” behavior of Codex or the SDK. Let’s surface a few concrete tests:

### Latency & Flow

Fantasy: “All agent handoffs happen instantly, so the TUI never feels laggy.”

Reality Test: Prototype the Intent→CodexTool→TUI loop on a typical machine—measure round-trip time. Is it under 200 ms? If not, we need to rethink where the orchestrator runs or whether to batch calls.

### Command-Less Interaction

Fantasy: “Users can simply type English; no hidden commands ever leak through.”

Reality Test: Observe real users typing open-ended questions. Does the IntentAgent misclassify >10% of prompts? If yes, we’ll need to refine our prompt templates or allow for quick “undo” to re-route.

### Artifact Fidelity

Fantasy: “Every key insight is reliably captured as a clean artifact.”

Reality Test: After a session, manually review 20 generated artifacts for completeness and clarity. If more than 30% feel ambiguous or duplicated, we’ll need to adjust ArtifactAgent’s selection criteria.

### Maintainability Over Time

Fantasy: “Upstream Codex or Agents SDK updates never break our integration.”

Reality Test: Lock versions and run a CI pipeline that updates to the latest patches monthly—track how often the integration layer fails. If breakages occur >1/month, introduce automated tests against those endpoints.


┌──────────────────────────────────────────────────────────────────┐
│ 1. UI Layer: KnowledgeTerminalUI (Codex TUI)                   │
│    • Ink-based terminal capturing plain-English input          │
└───────────────▲──────────────────────────────────────────────────┘
                │
                │ (event: new user line)
┌───────────────┴──────────────────────────────────────────────────┐
│ 2. Orchestration Layer (Agents SDK Core)                       │
│    • Receives input events                                      │
│    • Updates Context                                            │
│    • Schedules on-demand and background agents                  │
└───────────────▲──────────────────────────────────────────────────┘
                │
                │ (context.call_agent)
┌───────────────┴──────────────────────────────────────────────────┐
│ 3. Agents Layer                                                │
│                                                                  │
│  ┌── Speak Agents (on demand) ─────────────────────────────────┐ │
│  │ • DialogueAgent     (elicit)                                │ │
│  │ • CaseTheoryAgent   (theorize)                              │ │
│  │ • RenderAgent       (instating/representing)                │ │
│  │ • ExchangeAgent     (exchange)                              │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                  │
│  ┌─ Memory Agents (continuous) ─────────────────────────────────┐ │
│  │ • ListeningAgent   (capture all dialogue)                   │ │
│  │ • ArtifactAgent    (epistemic snapshotting)                 │ │
│  │ • SaveAgent        (local FS & Git commit)                  │ │
│  │ • EmbeddingAgent   (compute & store embeddings in DB)       │ │
│  │ • SearchAgent      (retrieve relevant artifacts)            │ │
│  └──────────────────────────────────────────────────────────────┘ │
└───────────────▲──────────────────────────────────────────────────┘
                │
                │ (context.call_tool)
┌───────────────┴──────────────────────────────────────────────────┐
│ 4. Tools Layer                                               │
│   • CodexTool      ↔ MCP Protocol → codex-rs engine            │
│   • FileTool       ↔ local FS & Git                            │
│   • DBAgent (Tool) ↔ embeddings database                       │
│   • NetworkTool    ↔ peer-to-peer sharing API                  │
│   • SearchTool     ↔ search index or external APIs             │
└───────────────▲──────────────────────────────────────────────────┘
                │
                │ (HTTP/stdio, POSIX, DB driver, HTTP)
┌───────────────┴──────────────────────────────────────────────────┐
│ 5. External & Protocol Layer                                    │
│   • mcp-types, mcp-server, mcp-client (Rust)                   │
│   • codex-rs core: apply-patch, exec-policy, LLM calls         │
│   • Local FS, Git, Database, Network peers                     │
└──────────────────────────────────────────────────────────────────┘


graph TD

    UI["**UI Layer**"]
    ORCH["**Orchestration Layer**"]

    subgraph AGENTS["**Agents Layer**"]
        SPEAK["Speak Agents"]
        MEM["Memory Agents"]
    end

    TOOLS["**Tools Layer**"]
    EXTERNAL["**External & Protocol Layer**"]

UI -- (event: new user line) --> ORCH
ORCH -- (context.call_agent) --> AGENTS
AGENTS -- (context.call_tool) --> TOOLS
TOOLS -- (HTTP/stdio, POSIX, DB driver, HTTP) --> EXTERNAL


