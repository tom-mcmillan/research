# PostgreSQL Instructions from Russell Foltz-Smith (April 14, 2025)

---

## Context

In a strategic design meeting for the Conduct knowledge system, Tom McMillan raised concerns about whether storing knowledge artifacts (in JSON form) in a vector database would destroy their atomicity. The goal was to preserve artifact integrity while enabling flexible querying and vector-based similarity search.

Russell Foltz-Smith responded with a direct recommendation to use **PostgreSQL** combined with **PGVector**, allowing both traditional SQL-style queries and vector similarity searches, while preserving JSON structure.

---

## Instructions from Russ

### 1. Use PostgreSQL with PGVector
> “Just use Postgres and PGVector. Don't mess around with anything else.”

### 2. Store Knowledge Artifacts as JSON in PostgreSQL
> “Store your JSON in a Postgres JSON field.”

### 3. Vectorize Within PostgreSQL
> “Vectorize it. You're going to vectorize in a million different ways—different fields and different chunks—and you'll be fine.”

### 4. Enable Flexible Querying
> “You can query it SQL style, you can query it JSON style... the database schema goes with you.”

### 5. Avoid Overcomplication
Russ emphasized simplicity:
> “Don't mess around with anything else.”

---

This setup ensures your knowledge artifacts remain intact, atomic, and referenceable, while enabling flexible and performant information retrieval using SQL and vector searches.
