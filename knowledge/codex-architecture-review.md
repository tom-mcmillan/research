# Codex Architecture

## 1. Overview

The openai/codex monorepo, showing its two main workspaces (Rust + Node), the core components in each, and how they relate.

- Two “execution engines” (Rust + Node) joined by the MCP protocol and shared data schemas.

- The Rust code provides core inference and patch capabilities.

- The TS/Node code provides a user-friendly terminal UI, delegating heavy lifting to Rust.


                            ┌─────────────────────────────┐
                            │       codex-main            │  (Root, PNPM workspace + scripts/docs)
                            └───────────┬─────────────────┘
                                        │
   ┌────────────────────────────────────┴─────────────────────────────────────  ┐
   │                                                                            │
┌──▼───────────────────┐                                                    ┌───▼───────────────┐
│      codex-rs        │              ┌─── MCP Protocol ───┐                │    codex-cli      │
│  (Rust Workspace)    │              │ (mcp-types schema) │                │  (Node/TypeScript)│
├──────────────────────┤              └────────────────────┘                ├───────────────────┤
│  ┌────────────────┐  │                                                    │  ┌──────────────┐ │
│  │ mcp-types      │  │  ←─── Shared data schemas (JSON/Serde) ────→       │  │ hooks/       │ │
│  └────────────────┘  │                                                    │  └──────────────┘ │
│  ┌────────────────┐  │                                                    │  ┌──────────────┐ │
│  │ mcp-server     │  │  ←── Exposes HTTP/stdio endpoints for              │  │ utils/       │ │
│  └────────────────┘  │      model & patch operations                      │  └──────────────┘ │
│  ┌────────────────┐  │                                                    │  ┌──────────────┐ │
│  │ mcp-client     │  │  ←── Rust client library used by CLI/TUI           │  │ commands/    │ │
│  └────────────────┘  │      or by other Rust services                     │  └──────────────┘ │
│  ┌────────────────┐  │                                                    │  ┌──────────────┐ │
│  │ core           │  │      Core logic: apply-patch, execpolicy,          │  │ entrypoint:  │ │
│  └────────────────┘  │      evidence gathering, etc.                      │  │ cli.tsx/app.tsx│
│  ┌────────────────┐  │                                                    │  └──────────────┘ │
│  │ cli            │  │  ←── Rust‐based CLI (alternative entry)            │                   │
│  └────────────────┘  │                                                    └───────────────────┘
│  ┌────────────────┐  │
│  │ tui            │  │  ←── Rust‐based TUI (Ink‐style alternative)
│  └────────────────┘  │
│  ┌────────────────┐  │
│  │ exec /         │  │  ←── Helpers for invoking subprocesses,
│  │ apply-patch    │  │      patch application, file I/O, etc.
│  └────────────────┘  │
└──────────────────────┘

### Key Points

```codex-rs``` (Rust workspace) is the engine:

   - ```mcp-types``` defines JSON/Serde schemas.

   - ```mcp-server``` exposes model-inference and patch tools over HTTP/stdio.

   - ```mcp-client```, core, and other crates implement the business logic (applying patches, running policies, managing evidence).

It also includes its own Rust CLI and Rust TUI as alternative frontends.

```codex-cli``` (Node/TypeScript) is the modern JS wrapper/UI:

    - Written in TS/React (Ink) for a richer, extensible terminal experience.

   - Organizes commands (```commands/```), state hooks (```hooks/```), and file utilities (```utils/```).

    - Its entrypoint (```cli.tsx``` / ```app.tsx```) wires user input to Codex operations—under the hood, calling into the Rust engine via the MCP protocol.


## 2. Layered Architecture View

### The Layered Diagram clarifies where you’d insert an HTTP shim for Agents SDK.

**UI Layer** (codex-cli): User-facing terminal, built in TypeScript/Ink.

**Protocol Layer** (MCP): The “glue” that connects UI ↔ Engine, with JSON schemas and a lightweight server.

**Engine Layer** (Rust crates): Core text-manipulation and reasoning logic.


┌────────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                              │
│                         (codex-cli)                                │
│   ┌─── Ink/React TUI    ┌─── Command Dispatcher ┌─── File I/O      │
│   │  (cli.tsx/app.tsx)  │  (commands/)          │  (utils/)        │
│   └──────────────────── ┴────────────────────── ┴──────────────────┘
│                         ↑                       │
│                         │ Invokes via MCP       │ Reads/Writes
│                         │ Protocol              │ local files
├────────────────────────────────────────────────────────────────────┤
│                       PROTOCOL LAYER                               │
│                          (MCP)                                     │
│   ┌── JSON Schemas ──┐  ┌── HTTP/STDIO Server ──┐  ┌── Client  ────┐
│   │ (mcp-types)      │  │ (mcp-server crate)    │  │ (mcp-client   │
│   └──────────────────┘  └───────────────────────┘  └───────────────┘
│   Defines a stable, language-agnostic “contract” between UI        │
│   and engine, and handles JSON-RPC-ish calls under the hood.       │
├────────────────────────────────────────────────────────────────────┤
│                       CORE ENGINE LAYER                            │
│                      (codex-rs crates)                             │
│   ┌── apply-patch   ──┐  ┌── exec-policy  ─┐  ┌── evidence ──┐     │
│   │ (patch utility)   │  │ (decision logic)│  │  gathering   │     │
│   └───────────────────┘  └──────────────── ┘  └───────────── ┘     │
│   Contains all of the “thinking”—how to transform text, apply      │
│   edits, and enforce high-level policies or evidence checks.       │
└────────────────────────────────────────────────────────────────────┘


## 3. Component Interaction Sequence

### The Sequence Diagram shows how each component interacts per request—critical for reasoning about latency and error handling.

Let’s visualize the steps when you type a prompt and see output. This flow shows how the UI, Protocol, and Engine collaborate on each user request.

**User Input**

User types:  gen-snippet "Summarize chapter 3"

     │
     ↓
[ codex-cli TUI ]
(cli.tsx/app.tsx)
  • parse command
  • match to "gen-snippet" handler
     │
     ↓ HTTP/STDIO JSON request
[MCP Server in Rust]
  • deserialize JSON
  • route to "generate_snippet" endpoint
     │
     ↓ invoke Rust Engine
[core::exec-policy & apply-patch]
  • call LLM, receive delta edits
  • apply patches to buffer
     │
     ↓ return patched text via MCP
[MCP Server responds JSON]
     │
     ↓
[ codex-cli TUI ]
  • render updated buffer in Ink
  • optionally write to file via `utils/text-buffer`
     │
     ↓
User sees new snippet in terminal and on disk

**System Output**

## 4. Tabular Breakdown of Key Modules

### The Table makes clear the surface area of each layer, helping you decide which modules to expose or wrap.

| Layer        | Module/Crate          | Language    | Responsibility                                        |
| ------------ | --------------------- | ----------- | ----------------------------------------------------- |
| **UI**       | `cli.tsx` / `app.tsx` | TypeScript  | Command parsing, Ink-based rendering, user input      |
| **UI**       | `commands/`           | TypeScript  | Mappings of textual commands to actions               |
| **UI**       | `utils/`              | TypeScript  | File I/O (read/write/patch), config management        |
| **Protocol** | `mcp-types`           | Rust + JSON | Data schemas for requests/responses                   |
| **Protocol** | `mcp-server`          | Rust        | HTTP/STDIO server exposing JSON-RPC-style endpoints   |
| **Protocol** | `mcp-client`          | Rust        | Client library for other services or CLI to call into |
| **Engine**   | `core`                | Rust        | Text transformation, patch application                |
| **Engine**   | `apply-patch`         | Rust        | Core patching logic                                   |
| **Engine**   | `exec-policy`         | Rust        | High-level orchestration rules for commands           |
| **Engine**   | `evidence`            | Rust        | Logging/checks for policy compliance                  |


## 5. MCP Protocol - Core Behavior

### Overview of layer

`mcp-types` defines the “envelopes” and “labels” (message formats).

`mcp-server` is the “post office clerk” that processes incoming letters and sends back replies.

`mcp-client` is your “pre-stamped mailbox” library that handles sending and receiving letters correctly.

### Benefits of this layer

**Stable Contract Between UI and Engine**
The MCP schemas (in mcp-types) and server (mcp-server) define a clear JSON-based “language” that Codex’s UI layer speaks to its Rust engine. If we wrap Codex as an external service, we must honor that language precisely—otherwise our calls will fail or produce subtly wrong behavior.

**Language-Agnostic Integration Surface**
Because the protocol is pure JSON over HTTP or stdio, it doesn’t care whether the caller is TypeScript, Python, or anything else. This makes it the perfect “glue” for the Agents SDK (Python) to invoke Codex’s capabilities without entangling the two runtimes at the source-code level.

**Minimal, Focused Shim**
By targeting the protocol layer, we avoid having to peel apart the entire codex-cli or modify core Rust logic. Instead, we write a small wrapper that exposes only the endpoints we need—keeping maintenance low and risk minimal.

**Consistent Versioning & Compatibility**
Codex’s protocol layer evolves deliberately: API changes happen there, not ad-hoc across the codebase. Building against MCP means our integration is less likely to break when Codex updates.

**Performance & Error Handling**
The protocol server already handles batching, streaming, and error codes. If we interface at that point, we inherit its resilience—rather than re-implementing ad-hoc HTTP calls into internal methods.

### Why this matters for our integration

Understanding `mcp-types`, `mcp-server`, and `mcp-client` is critical because together they form the stable, language-neutral boundary where Codex’s UI/engine stack can cleanly meet our Python-based Agents SDK orchestrator:

1. **Shared Schema** (`mcp-types`) Provides the single source of truth for every request and response shape. By honoring these types, our Agents SDK tools will always send correctly structured JSON and parse results without guesswork.

2. **Runtime Bridge** (`mcp-server`) Exposes Codex’s core capabilities—text generation, patch application, policy enforcement—over HTTP or stdio. Wrapping this server means we don’t have to modify Codex’s UI or engine code; we simply invoke proven endpoints.

3. **Client Abstraction** (`mcp-client`) Demonstrates how to encapsulate transport, error handling, and streaming in a language-agnostic way. It offers a blueprint for our Python `CodexTool`: clean, type-safe calls with predictable behavior and minimal boilerplate.

### Opportunities for integrating at this layer

1. **Minimize coupling** (no deep code merges or language interop hacks).

2. **Maximize reliability** (leverage Codex’s existing API versioning and error contracts).

3. **Keep the UI magic intact** (Codex’s TUI and Rust engine remain untouched).

4. **Outcome** A protocol-centric approach yields a lightweight, maintainable “glue” that lets the Agents SDK sequence domain-specific agents around Codex’s powerful local operations.

### Each mcp defined

#### 1. mcp-types

**What it contains**
- A collection of Rust structs and enums annotated with Serde’s Serialize/Deserialize.  
- Definitions for every message you can send to the Codex engine, and every response you can get back.  
- Common building-block types (e.g. `Position`, `TextEdit`, `DocumentId`, `Url`) that appear in many operations.

**Its function**
- Acts as the shared schema library across all components (Rust engine, Node UI, and any external caller).  
- Guarantees that everyone—whether it’s the Rust server, the Node CLI, or your own Python orchestration layer—uses exactly the same data shapes.  
- Ensures forward- and backward-compatibility: when Codex evolves, changes to these types are centrally versioned.

**Its nature**
- Purely declarative: no business logic lives here, only type definitions.  
- Language-agnostic at the JSON level, but authoritative in Rust code.  
- The single source of truth for how to structure your JSON payloads.

#### 2. mcp-server

**What it contains**
- A small Rust application (`main.rs` and supporting modules) that:  
  1. Listens for requests—either via HTTP (on a localhost port) or via standard I/O streams.  
  2. Deserializes each incoming JSON blob into the corresponding `mcp-types` struct.  
  3. Dispatches the request to the appropriate handler in the engine crates (e.g. `apply_patch`, `exec_policy`, or `generate`).  
  4. Serializes the handler’s output back into JSON and returns it to the caller.  
- A built-in router that maps method names (like `"apply_patch"`) or HTTP paths (like `POST /apply_patch`) to Rust functions.

**Its function**
- Provides the runtime bridge between any client (Node, Python, or Rust CLI) and the core text-manipulation engine.  
- Ensures robust error handling, converting Rust panics or engine errors into well-formed JSON error objects.  
- Optionally supports streaming responses for long-running tasks (e.g. token-by-token generation).

**Its nature**
- A stateless server from request to request—each call is independent, carrying its full context in the JSON payload.  
- Lightweight and embeddable: you can run it in a background thread, containerize it, or even compile it into a binary for offline use.  
- Designed for performance: minimal overhead beyond JSON (no heavyweight RPC framework), with direct calls into optimized Rust logic.

#### 3. mcp-client

**What it contains**
- A Rust crate (`mcp-client`) with:  
  - Typed client structs and methods corresponding to each MCP endpoint (e.g. `apply_patch()`, `generate()`, `exec_policy()`).  
  - Transport abstractions that let you switch between calling over HTTP or over a spawned subprocess’s stdio.  
  - Helper utilities for building request payloads and parsing response streams.  
  - Re-exports of `mcp-types` so you don’t need to depend on that crate directly.

**Its function**
- Encapsulates all the boilerplate of making requests:  
  1. Serializing your Rust data into JSON (using the same `mcp-types`).  
  2. Sending it over your chosen channel (HTTP client or stdio pipe).  
  3. Deserializing the response back into rich Rust types.  
- Offers ergonomic APIs so engine-consumers can write:
  ```rust
  let client = McpClient::new_http("http://localhost:3000");
  let edits = client.apply_patch(args).await?;``` 

...rather than manually crafting HTTP requests.

**Its nature**
- A thin, stateless library: each method call carries its entire context in its arguments, with no hidden global state.
- Pluggable transport: behind a single trait, you can swap out HTTP for a direct child-process invocation (helpful if you want to embed the server binary rather than run it separately).
- Error-safe: wraps engine errors in Rust’s Result<_, McpError> so you get typed, actionable failures rather than raw JSON blobs.

**What it does**
- Abstracts the protocol so Rust callers never touch raw JSON or URL paths.
- Manages connections (e.g. keeping an HTTP client instance alive or restarting a subprocess if it dies).
- Chews on responses, turning JSON streams into idiomatic Rust iterators or futures.

## 6. Rust Engine - Core Behavior

“Core engine behavior” is all the high-performance, safety-critical logic inside the Rust crates—text-editing algorithms, policy enforcement, model calls, and protocol routing—that together power codex’s fast, reliable transformations. If you need to tweak how patches are applied, add new safety checks, or change the way the LLM is called (e.g. different retry logic), you’d dive into this engine layer. Broadly, it includes:

1. ### Text-Patching

What it is: Applying a set of incremental edits (insertions, deletions, replacements) to an existing text buffer.

Why it’s core: When you ask Codex to “edit this code” or “apply these diffs,” the engine must merge edits consistently, handle conflicts, and keep the document’s integrity.

2. ## Policy Logic (exec-policy)

What it is: A layer of rules or “policies” that decide whether a given operation is permitted, and how it should be shaped. For example, you might have a policy that enforces maximum snippet length, filters out dangerous shell commands, or validates that a patch won’t corrupt syntax.

Why it’s core: Policies protect you from invalid or unsafe operations at high speed—before or after the LLM generates content.

3. ## LLM Invocation

What it is: The mechanics of calling the underlying language model—streaming tokens in, handling timeouts, batching requests, and collecting its output.

Why it’s core: This is where performance and reliability matter most. The engine wraps API calls (e.g. to OpenAI) or local model inference in robust, asynchronous Rust code that can handle partial failures, retries, and streaming responses.

4. ## Evidence Gathering & Validation

What it is: Collecting metadata about operations (e.g., timings, token usage, success/failure counts) and optionally validating outcomes against expected patterns.

Why it’s core: It provides the data needed for auditing, metrics, or feeding back into higher-level “audit” agents.

5. ## Protocol Handling

What it is: Serializing incoming JSON requests into Rust types, routing them to the right handler, and serializing back the JSON responses.

Why it’s core: It’s the engine’s “front door,” ensuring every request is parsed, dispatched, and replied to in a minimal-overhead, crash-safe manner.

# UI Layer

codex-cli/
├─ package.json               ← NPM manifest & dependencies
├─ bin/                       ← Thin shims to launch the CLI
├─ src/
│   ├─ cli.tsx                ← Entry point: wires Commander + Ink TUI
│   ├─ app.tsx                ← Defines the top-level Ink layout & panels
│   ├─ commands/              ← One file per user-facing command
│   │    ├─ generate.ts       ← e.g. “gen-snippet” handler
│   │    ├─ patch.ts          ← “apply-patch” handler
│   │    └─ …                 ← Many more (status, config, etc.)
│   ├─ hooks/                 ← React hooks for state & side-effects
│   │    ├─ useBuffer.ts      ← Manages the in-memory text buffer
│   │    ├─ useDispatcher.ts  ← Invokes MCP calls on demand
│   │    └─ …                 ← e.g. useConfig, useDebounce
│   └─ utils/                 ← Low-level helpers
│        ├─ textBuffer.ts     ← Read/write/patch a file on disk
│        ├─ applyPatch.ts     ← Diff logic for filesystem updates
│        └─ config.ts         ← Load & validate user config (.codexrc)
└─ README.md
