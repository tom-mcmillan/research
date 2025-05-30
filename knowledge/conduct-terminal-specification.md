# Conduct Terminal Specification

## Main Goal:

A desktop/web app (Conductor) empowering users to seamlessly translate natural language into actionable tasks.

Tasks are executed either:
- Locally (e.g., filesystem commands)
- Via external cloud services (OpenAI, Google Workspace, etc.)

## Explicit Functional Mapping:

| Functionality                           | Implementation                        | File/Path                                      |
|-----------------------------------------|---------------------------------------|------------------------------------------------|
| Unified Orchestration                   | Central orchestrator                  | orchestration/conductor.go                     |
| Logical Reasoning & Validation          | Reasoning & validation logic          | reasoning/assistant.go                         |
| Command Translation & Execution         | Bash execution & command runner       | tasks/bash.go, tasks/runner.go                 |
| Data Persistence & Session Management   | File & session storage                | repository/{filestore,session,storage}.go      |
| External Network Integration            | API clients (OpenAI, Google, etc.)    | external/{openai,google,microsoft}.go          |
| User-Facing Presentation                | HTTP handlers & frontend UI           | api/handlers.go                                |
| Configuration & Utility Support         | Central config & utilities            | config/config.go                               |

## Critical User Flow Example:

**User input:**  
`"Make a folder called 'Reports' on my Desktop."`

**Flow:**  
1. Orchestrator (`conductor.go`) receives user input.
2. Logical Reasoning (`assistant.go`) validates and categorizes the command.
3. Command Runner (`runner.go`) translates input into executable command:

```
mkdir ~/Desktop/Reports
```

4. Bash Executor (`bash.go`) executes this safely on the user's local machine.
5. Results logged and stored via repository.
6. User-facing component (`handlers.go`) returns clear, structured response to frontend.

## Key Technical Features:
- OpenAI Thread mechanism for conversation handling.
- Vector DB integration (user & team-level).
- OAuth authentication via Google.
- Cloud and local resource integration.
- Modular and explicit structure for ease of development.
