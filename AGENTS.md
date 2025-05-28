# Instructions

Please build to these specifications:

- Use best practices. 
- Follow the github pages documentations. 
- Refer to this document as you build. 
- Persist until you complete the project. 
- Be rational, think through the ideas. 
- Imagine what's best for me and the user. 
- Choose simpler solutions over more complex ones. 
- Choose tested methods over expirimental ones. 
- Choose architecture that simplifies my life. 
- This is simply a place for me to publish my ideas.

# AGENTS.md

# 📘 Product Specification: AI Research Public Documentation Site

---

## Overview

This repository contains authored Markdown essays by Thomas McMillan on topics related to AI, strategy, and philosophy. The intent is to serve these writings to the public using GitHub Pages with a clean, documentation-style UI modeled after the OpenAI Agents site.

This document acts as the persistent configuration and contribution guide for Codex or any AI developer working on the repo. It details **UI expectations**, **workflow assumptions**, and **repository hygiene** conventions.

---

## 🔧 Repository Structure (Post-Cleanup)

```
research/
├── .github/workflows/        # CI deployment setup
├── .gitignore                # Excludes build/system files
├── .venv/                    # Local virtual environment (ignored)
├── AGENTS.md                 # This configuration file
├── README.md                 # Setup and deployment docs
├── mkdocs.yml                # Site config (uses mkdocs-material + gen-nav)
├── requirements.txt          # Python deps (includes gen-nav from GitHub)
└── docs/
    ├── index.md
    ├── philosophy/index.md
    ├── strategy/index.md
    ├── technology/
    │   ├── index.md
    │   └── startup_prompt.md
    └── prompts/
        ├── business-model.md
        └── what-feeling-is-this.md
```

---

## 🎨 UI & UX Specification

Codex must ensure the documentation site looks and behaves like:

**Reference**: [OpenAI Agents Docs](https://openai.github.io/openai-agents-python/)  
**Key UI Elements**:

- Fixed **left sidebar** titled "Research Notes" with collapsible sections
- **Top nav bar** with:
  - Site name left-aligned
  - Full-text search bar
  - GitHub repo link (star/fork indicators optional)
- **Main content area** shows:
  - Markdown-rendered content
  - Syntax-highlighted code blocks
  - Mermaid diagrams
- Fully responsive and styled with default **Material for MkDocs (light theme)**

### Required Features

| Feature               | Status       |
|-----------------------|--------------|
| Sidebar navigation    | ✅ gen-nav   |
| Mermaid diagrams      | ✅ mermaid2  |
| Code block copy       | ✅ enabled   |
| Full-text search      | ✅ enabled   |
| Dark mode toggle      | ✅ available |
| Responsive layout     | ✅ expected  |

### `mkdocs.yml` Excerpt

```yaml
site_name: Research Notes
site_url: https://tom-mcmillan.github.io/research/
repo_url: https://github.com/tom-mcmillan/research
repo_name: research

theme:
  name: material
  palette:
    scheme: default
  features:
    - navigation.expand
    - navigation.sections
    - navigation.instant
    - toc.integrate
    - search.highlight
    - search.suggest
    - content.code.copy

plugins:
  - search
  - gen-nav
  - mermaid2

markdown_extensions:
  - admonition
  - toc:
      permalink: true
  - pymdownx.superfences
  - pymdownx.highlight
```

---

## 🧑‍💻 Authoring & Publishing Workflow

- Write files in `docs/` using VS Code
- Preview with `mkdocs serve`
- Commit to `main` → triggers GitHub Actions → deploys to GitHub Pages (`gh-pages` branch)

---

## ✅ Repository Hygiene & Setup

### Cleanup Actions (already applied)

| Step                        | Description                                                       |
|-----------------------------|-------------------------------------------------------------------|
| Switched to `gen-nav`       | Installed via GitHub; updated `requirements.txt` and `mkdocs.yml` |
| Removed legacy CSS          | Deleted `docs/css/custom.css`; dropped `extra_css` from config    |
| Pruned tracked artifacts    | Removed `.DS_Store`, `site/`, and created proper `.gitignore`     |
| Committed untracked files   | `AGENTS.md` + `docs/prompts/*.md` added to Git                    |
| README updated              | Clarified use of GitHub-based gen-nav                             |

### `.gitignore`

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]

# Virtual environment
.venv/

# MkDocs build output
site/

# macOS metadata
.DS_Store

# Editor directories and files
.vscode/
*.sw?
```

### `requirements.txt`

```txt
mkdocs
mkdocs-material
git+https://github.com/lukasgeiter/mkdocs-gen-nav.git@main#egg=mkdocs-gen-nav
mkdocs-mermaid2-plugin
pymdown-extensions
```

---

## 🧪 Validation Checklist

- [ ] `mkdocs serve` runs without warnings
- [ ] Sidebar is auto-generated from `docs/` directory structure
- [ ] GitHub Actions deploys successfully on push to `main`
- [ ] Mermaid diagrams and code blocks render properly
- [ ] No tracked build or system files (`site/`, `.DS_Store`, etc.)
- [ ] Local preview mirrors final production output

---

## 🧵 Prompting Codex

When Codex is used to continue or enhance this repo, it must:

- Read and respect this `AGENTS.md`
- Treat `docs/` structure as canonical
- Avoid reintroducing plugins like `awesome-pages` or custom CSS
- Use `gen-nav` exclusively for navigation
- Make all styling decisions based on Material theme defaults
- Keep PRs small and auditable (clear commit messages, minimal blast radius)

---

## 📅 Milestones

| Milestone                       | Status           |
|--------------------------------|------------------|
| GitHub Pages site live         | ✅ Completed      |
| Navigation verified via gen-nav| ✅ Confirmed      |
| Custom domain setup            | 🔜 Optional later |
| Weekly content additions       | ⏳ In progress    |

---

## ✅ Definition of Done

A deployment is valid when:

- The sidebar, topbar, and content match spec visually and functionally
- All Markdown files in `docs/` are reachable through the UI
- No tracked build artifacts or system files remain
- Build works locally (`mkdocs serve`) and remotely (via CI)

---
