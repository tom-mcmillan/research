# Tractus on Technology

Our technological architecture is a **symbiosis** of microservices and orchestrated agent workflows. At its core sits **Dialectic**—our forked Agents SDK—providing the primitives for streaming, guardrails, and tool invocation. Conductor, the system’s beating heart, imports this SDK and delegates responsibilities to four sister services:

1. **Artifacting** — runs parallel/sequential Agent pipelines that distill raw inputs into canonical JSON artifacts.  
2. **Database** — a lean Postgres JSONB ledger enforcing only the core schema constraints, ensuring every artifact conforms before it’s committed to the ledger.  
3. **Assembly** — performs logical and epistemic analysis, weaving artifacts into higher-order constructs or documents.  
4. **Front-end** — a Google Doc with an embedded terminal UI, giving users a direct line into Conductor’s inner workings.  

Each repository ships with its own local Docker setup, CI pipeline, and a minimal “hello-world” example—proofs of life that validate the most basic behavior before layering complexity. We treat **Codex** not as a runtime component but as our **development companion**, freeing Conductor’s production flows to rely exclusively on the robust, Pythonic APIs of the Agents SDK.

This architecture embodies **separation of concerns**: the SDK handles orchestration and protocol, service clients expose specific domain logic (artifact insertion, assembly processing, data retrieval), and Conductor emerges as the **glue** that binds them into coherent, end-to-end user experiences. In doing so, we achieve both **resilience** (fault isolation at the service level) and **observability** (clear logging, streaming contexts, and diagnostic flags at each step).