# Precisely-Tuned Three-Level Knowledge Hierarchy

| Rank | Unit      | Composed Of    | Explanation / Definition                                                  |
|------|-----------|----------------|---------------------------------------------------------------------------|
| 1    | Session   | Dialogues      | Entire interaction sequence covering multiple dialogues.                  |
| 2    | Dialogue  | Ideas          | Clearly bounded set of ideas on a single coherent topic or goal.          |
| 3    | Idea      | (Atomic)       | Single, indivisible concept, statement, question, belief, or orientation. |


## Definitions:

### 1. Session

    - Largest conversational container**, covers an entire interactive engagement.
    - Clearly bounded**, with an explicit beginning and end.
    - Composed explicitly of dialogues**, each addressing distinct themes or topics.

### 2. Dialogue

    - Precisely captures and groups ideas** that revolve around a single, clear, definable topic or objective.
    - Intuitive unit of organization** within a session.
    - Allows clear thematic segmentation** within larger conversational contexts.

### 3. Idea

    - Atomic knowledge-element**, indivisible without loss of coherent meaning.
    - Smallest clearly meaningful conceptual unit**, forming the basic building block for higher-level structures.
    - Includes statements, rhetorical questions, beliefs, hypotheses, orientations, and explicit claims**.


## Nested Set Logic:

Session = { Dialogue₁, Dialogue₂, Dialogue₃, … }

Dialogue₁ = { Idea₁, Idea₂, Idea₃, … }
Dialogue₂ = { Idea₁, Idea₂, Idea₃, … }
Dialogueₙ = { Idea₁, Idea₂, Idea₃, … }

Idea = Atomic meaning-unit (no further subdivision)


## Why this Structure?

- **Clearly distinct and non-overlapping**: Each unit is precisely defined for intuitive clarity.
- **Optimized for computational parsing**: Explicit structure facilitates embedding, indexing, retrieval, and semantic logic.
- **Matches intuitive human conversational patterns**: Easy to understand and implement for both developers and users.

This clearly structured hierarchy serves as the definitive reference for knowledge parsing, abstraction, and management within the AI project.


## Example Flow


User session starts
│
├── User input → /think (response generated)
│
├── User input → /think (response generated)
│
├── (Internal orchestrator agent identifies end of dialogue #1)
│      └─→ Clearly bounded Dialogue #1 (multiple ideas)
│          │
│          └──→ `/abstract` generates Knowledge Artifact
│
├── User continues input → /think (more responses)
│
└── (Another clearly bounded Dialogue #2 identified internally)
       └─→ Dialogue #2 → `/abstract`
