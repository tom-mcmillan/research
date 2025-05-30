# Restated Vision (“Facts”)

## UI Layer

The user interacts via the full Codex terminal UI—rich TUI widgets, local file I/O, desktop‐app capable.

## Orchestration Layer

OpenAI Agents SDK sits “above” Codex, defining and sequencing multiple agents:

**Dialogue Agent** (guided by client-centered case theory)

**CaseTheory Agent** (periodically synthesizes the conversation into a declarative case theory)

**Artifact Agent** (produces and saves knowledge artifacts to markdown files, commits to Git)

**Memory Agent** (indexes and embeds past artifacts, surfaces relevant context back to Dialogue)

## Data Flow

User ↔ Dialogue Agent ↔ CaseTheory/Artifact/Memory Agents ↔ Codex (for file operations and TUI feedback)

## Goals

**Joy & Focus:** Seamless, single-workspace experience in VS Code/Codex.

**Orchestration:** Clear, modular handoffs so each agent can specialize.

**Persistence:** Every artifact lives as a versioned markdown file.

**Autonomy & Richness:** Past knowledge remembered and surfaced automatically.

# Hypothetical Theory of the Case (Working Draft)

By wrapping Codex’s local-first, UI-rich capabilities as an agent within the OpenAI Agents SDK, we can orchestrate a family of domain-specific agents (Dialogue, CaseTheory, Artifact, Memory) to deliver a unified, joyful knowledge-creation experience. This integration centralizes all interactions in one workspace, ensures maintainability through clear agent boundaries, and preserves low-latency local operations—thereby fulfilling both developer and end-user needs.