# Instructions

Please follow these principles:

- Use best practices
- Follow the GitHub Pages documentation
- Refer to this document as you build
- Persist until the project is complete
- Be rational—think through the ideas
- Imagine what’s best for the author and the end reader
- Prefer simpler solutions over more complex ones
- Prefer tested methods over experimental ones
- Choose architecture that simplifies the author’s life
- Remember: this is a place for the author to publish thought

---

## Overview

This repository contains authored Markdown essays by Thomas McMillan on topics related to AI, strategy, and philosophy. The goal is not only to publish these ideas, but to make the thinking behind them durable and reproducible. The GitHub Pages layer makes the ideas visible; the scripting and structure layers make them maintainable. Every element—from UI to automation—must honor this intent.

This document serves as a persistent configuration and contribution guide for Codex or any AI developer working on the repo. It outlines **UI expectations**, **workflow assumptions**, **automation philosophy**, and **repository hygiene**.

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
- **Main content area** displays:
  - Markdown-rendered content
  - Syntax-highlighted code blocks
  - Mermaid diagrams
  - Table of contents on the right side reflecting headings (##, ###)
  - Fully responsive and styled with default **Material for MkDocs (light theme)**, custom black header, Inter font stack, and typography overrides to match OpenAI Agents documentation

---

## 🧑‍💻 Authoring & Publishing Workflow

- Write Markdown files in `docs/` using VS Code
- Preview changes locally with `mkdocs serve`
- Commit to `main` → triggers GitHub Actions → deploys to GitHub Pages (`gh-pages` branch)

---

## 🧵 Prompting Codex

When Codex is used to continue or enhance this repo, it must:

- Read and respect this `AGENTS.md`
- Treat the `docs/` folder structure as canonical
- Avoid reintroducing plugins like `awesome-pages`
- Use `awesome-nav` exclusively for navigation
- Use custom CSS only for:
  - Header background override
  - Typography overrides
  - Open-source Inter font stack
- Use Material theme’s built-in `toc.following` feature for right-side ToC
- Use the GitHub Actions workflow in `.github/workflows/pages.yml` to build and deploy the site:
  - `mkdocs build`
  - `upload/download-pages-artifact`
  - `configure-pages`
  - `deploy-pages`
- Control sidebar order via `docs/.nav.yml`:
  - List `Intro` first
  - Then `*` to include all other pages automatically
- Monitor workflow runs at https://github.com/tom-mcmillan/research/actions
- Make all styling decisions based on Material defaults unless noted
- Keep PRs small and auditable with clear commit messages
- Summarize commits descriptively (e.g. "Add MkDocs config and docs")

---

## ✅ Definition of Done

A deployment is complete when:

- The site visually and functionally matches the reference spec
- All authored Markdown pages are reachable through the UI
- No tracked build artifacts, system files, or hidden state are committed
- The build works locally (`mkdocs serve`) and remotely (via CI)
- The system remains maintainable and intelligible to the author months later

---

# Automation Layer

## Purpose

The automation layer supports the author’s publishing and epistemic goals by minimizing friction between source tools (e.g., Zotero) and Markdown-based publication. Its role is to make expression and formatting easier without introducing abstraction, dependencies, or hidden behavior.

This is not a general automation playground. Each script should serve a clearly defined, durable function that the author can understand, maintain, and debug.

## Goals

- Mirror curated Zotero collections into Markdown-formatted bibliographies
- Ensure Markdown is always the **final output**, not an intermediary
- Use the simplest possible tooling—no wrappers, no bloat
- Make all scripts editable and debuggable by a non-specialist in VS Code

## Constraints

- No SaaS or cloud dependencies beyond GitHub and Zotero
- Do not commit or track `.bib`, `.json`, or other database exports
- Use `.env` for secrets—never commit keys
- All scripts must run locally without engineering support
- All file paths must be relative to the repo root (`research/`)

## What’s Acceptable

- Single-purpose, terminal-run Python scripts
- Clear and readable formatting logic (e.g., MLA, Markdown italics)
- One file = one idea
- Environment variables managed in `.env`

## What’s Not Acceptable

- Build systems, transpilers, or complex tooling
- Implicit side effects or hidden state
- Experimental libraries or undocumented APIs
- Automation that reduces control or transparency

## How Codex Should Think

- Think as a *scribe*, not an engineer. Your job is to make the author’s thinking reproducible—not optimized or clever.
- Prioritize **legibility** and **durability** over performance.
- Ask: *Will this still make sense to the author six months from now?*
- If something feels “too clever,” it probably is.
- Automate boring work. Never automate thinking.
- Use abstraction only when it removes noise—not when it creates new categories.

## Current Script

`build_bibliography.py` reads a Zotero collection and writes its contents into `docs/pedagogy/bibliography.md`. It uses the Zotero API with credentials stored in `.env`. Output formatting preserves italics and follows MLA-style conventions.

All future scripts must follow this design philosophy.

