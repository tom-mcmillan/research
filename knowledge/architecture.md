# High-Level Architecture

## Diagram


                        ┌───────────────────────┐
                        |    User Interface     |   (Desktop / Web app)
                        └───────────────────────┘
                                  │
                                  ▼
                   ┌────────────────────────────────┐
                   |      API Gateway / Backend     |
                   |   (Python, e.g., Flask/FastAPI)  |
                   └────────────────────────────────┘
                    │              │             │
         ┌──────────┘      ┌───────┴───────┐     └───────┐
         ▼                 ▼               ▼             ▼
┌─────────────────┐  ┌─────────────────┐ ┌─────────────────┐  ┌─────────────────┐
| /orchestrate    |  | /knowledge      | | /logs (optional)|  | /auth (Google)  |  
| Endpoint        |  | Endpoint        | | Endpoint        |  | Endpoint        |  
└─────────────────┘  └─────────────────┘ └─────────────────┘  └─────────────────┘
         │                  │
         ▼                  ▼
   ┌─────────────┐  ┌─────────────┐
   | Conductor   |  | Artifact    |
   | (Orchestrator)|| Agent       |
   └─────────────┘  └─────────────┘
         │      Delegates to (via handoffs)
         │
         ▼
  ┌───────────────────────────────┐
  | Other Agents:                 |
  | - Validate (logic checking)   |
  | - Program (code generation)   |
  | - Network (network integration)|
  | - Store (knowledge management)|
  | - Interface (visual output)   |
  └───────────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
| Vector DB (per-user, via        |
| OpenAI vector stores API)       |
└─────────────────────────────────┘


## Endpoints

/orchestrate Endpoint:

    - Purpose: Serves interactive user requests via the conductor (orchestrator) agent.
    - Output: Dynamic responses (text, visuals, etc.) suitable for real-time user feedback.
    - Behavior: Orchestrates calls to specialized agents (validate, program, network, store, interface) using the Agents SDK.
	
/knowledge Endpoint:

    - Purpose: Dedicated to generating and returning Knowledge Artifacts in JSON format.
    - Output: Raw, structured JSON containing artifact data (e.g., unique knowledge_id, metadata, potential image IDs, LaTeX code, etc.).
    - Behavior: Uses the artifact agent; these artifacts are also stored in each user’s vector DB for later retrieval and further processing.
	
/logs Endpoint (Optional):
    - Purpose: Provides a view into backend logs, useful for monitoring and debugging.
    - Output: Plain text or structured log data.
	
/auth Endpoint (Future):
    - Purpose: Handles user authentication using Google OAuth (this can be integrated later, with tokens stored securely and associated with individual vector DBs).

## Code Organization and Naming Conventions

### Directory Structure (Example)

conductor/
└── backend-python/
    ├── agents/
    │   ├── conduct_prompt.txt
    │   ├── artifact_prompt.txt
    │   ├── program_prompt.txt
    │   ├── network_prompt.txt
    │   ├── store_prompt.txt
    │   ├── validate_prompt.txt
    │   └── interface_prompt.txt
    ├── api/
    │   ├── __init__.py
    │   ├── orchestrate.py
    │   ├── knowledge.py
    │   └── logs.py
    ├── core/
    │   ├── orchestrator.py
    │   └── vector_store.py      # For handling per-user vector DB setup
    ├── services/
    │   └── auth.py              # For Google OAuth (to be integrated)
    ├── tests/
    ├── main.py
    ├── requirements.txt
    └── .env

### Code Naming Conventions
	•	Modules and Directories: Lowercase with underscores (e.g., agents, orchestrate.py).
	•	Files Storing Prompts: Clear names like conduct_prompt.txt, etc.
	•	Environment Variables: Uppercase, e.g., OPENAI_API_KEY, CONDUCT_PROMPT_PATH.
	•	Agent Names in Code: Use descriptive names (e.g., conduct_agent, artifact_agent).

