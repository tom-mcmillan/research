# Quick-scan picture of the knowledge terminal

## Overall Vision

### 1. Overall Vision

**Key Takeaway**
“Sail” = a local knowledge terminal that unifies Codex tools + OpenAI Agents under one Electron shell, letting you turn raw notes into structured artifacts and then into rendered outputs.

**Relevant files**
- sail-architecture.md
- big-idea.md

### 2. System anatomy

**Key Takeaway**
You picture three main panes (Cue / Display / Notes) managed by an Orchestrator that talks to domain-specific agents (Memory, Speak, Audit…).

**Relevant files**
- conduct-terminal-overview.md
- conduct-terminal-specification.md
- ui.md

### 3 . Philosophical ground

**Key Takeaway**
Knowledge ≠ mere text; an artifact must be exchangeable, epistemically sound, and context-rich.

**Relevant files**
- bertrand-russell.md
- knowledge-hierarchy.md
- four-key-concepts.md

### 4. Rules & processes

**Key Takeaway**
Clear constraints on how agents segment, validate and store artifacts; strong bias toward human-in-the-loop approvals.

**Relevant files**
- conducting-rules.md
- orchestration-rules.md
- knowledge-artifact-props.md


### 5. Backend tech sketches

**Key Takeaway**
A Python-based agent stack already generates artifacts and writes to Postgres/pgvector; Electron should become the front-end cockpit, not replace that logic.

**Relevant files**
- codex-architecture-review.md
- postgres-russ.md
- codex_agents_integration_overview.md

## Agent specs

### 1. Segmentation Agent

**Core job (from your specs)**
Break raw text into ≥ 250-char “segments” that mark shifts in epistemic focus.

**Typical I/O**
Input: full text string → Output: `SegmentationOutput` JSON array

**Where it would run in Sail**
Backend service (already exists in your Python repo)

### 2. Epistemic Contour Agent

**Core job (from your specs)**
Judge a single segment’s artifact-worthiness (coherence, reusability, etc.) and return `EpistemicContourOutput`.

**Typical I/O**
segment JSON → verdict JSON

**Where it would run in Sail**
Backend

### 3. Artifact Assembler Agent

**Core job (from your specs)**
Given a “validated” segment, assemble the final artifact JSON and save it locally.

**Typical I/O**
valid segment → `ArtifactOutput` JSON

**Where it would run in Sail**
Backend

### 4. Conduct Agent

**Core job (from your specs)**
Orchestrates the above—delegates tasks in sequence.

**Typical I/O**
high-level command → chained agent calls

**Where it would run in Sail**
Backend