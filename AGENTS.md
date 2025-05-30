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
├── mkdocs.yml                # Site config (uses mkdocs-material + awesome-nav)
├── requirements.txt          # Python deps (includes awesome-nav from GitHub)
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
  - Table of contents on the right side reflecting the page's sections (##, ###)
  - Fully responsive and styled with default **Material for MkDocs (light theme)** with a custom black header, typography overrides to match the OpenAI Agents documentation, and an open-source Inter font stack

### Required Features

| Feature               | Status       |
|-----------------------|--------------|
| Sidebar navigation    | ✅ awesome-nav   |
| Mermaid diagrams      | ✅ mermaid2  |
| Code block copy       | ✅ enabled   |
| Full-text search      | ✅ enabled   |
| Page table of contents (right side) | ✅ toc.following |
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
    primary: "#000000"
  features:
    - navigation.expand
    - navigation.instant
    - toc.following
    - search.highlight
    - search.suggest
    - content.code.copy

plugins:
  - search
  - awesome-nav
  - mermaid2

markdown_extensions:
  - admonition
  - toc:
      permalink: true
      title: "Table of Contents"
      toc_depth: "2-3"
  - pymdownx.superfences
  - pymdownx.highlight

extra_css:
  - css/custom.css
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
| Switched to `awesome-nav`       | Installed via GitHub; updated `requirements.txt` and `mkdocs.yml` |
| Added CSS overrides for header background, typography, and font stack | Created `docs/css/custom.css` & added `extra_css` to `mkdocs.yml` for header background, typography style, and open-source Inter font overrides |
| Added docs/.nav.yml for primary nav ordering | Created `docs/.nav.yml` to pin Intro first and wildcard-include the rest via awesome-nav |
| Adopted pages build & deployment workflow | Added `.github/workflows/pages.yml` and removed the old `.github/workflows/deploy.yml` |
| Pruned tracked artifacts    | Removed `.DS_Store`, `site/`, and created proper `.gitignore`     |
| Committed untracked files   | `AGENTS.md` + `docs/prompts/*.md` added to Git                    |
| README updated              | Clarified use of GitHub-based awesome-nav                          |

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
git+https://github.com/lukasgeiter/mkdocs-awesome-nav.git@main#egg=mkdocs-awesome-nav
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
- Avoid reintroducing plugins like `awesome-pages`; allow custom CSS only for header background, typography style, and open-source Inter font overrides
- Use `awesome-nav` exclusively for navigation
- Use Material theme's built-in `toc.following` feature for page table of contents (right sidebar)
- Use the GitHub Actions workflow defined in `.github/workflows/pages.yml` to build and deploy the site via the official Pages actions (mkdocs build, upload/download-pages-artifact, configure-pages, deploy-pages)
- Control primary sidebar ordering via a `docs/.nav.yml` file: list `Intro` first, then `*` to include all other pages automatically
- Monitor the GitHub Actions workflow runs and report any failures via https://github.com/tom-mcmillan/research/actions
- Make all styling decisions based on Material theme defaults, except header background override via CSS
- Keep PRs small and auditable (clear commit messages, minimal blast radius)

---

## 📅 Milestones

| Milestone                       | Status           |
|--------------------------------|------------------|
| GitHub Pages site live         | ✅ Completed      |
| Navigation verified via awesome-nav| ✅ Confirmed      |
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
