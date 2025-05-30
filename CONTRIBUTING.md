# Contributing Guide

Thank you for helping improve this documentation site!

## Setup
1. Create a Python 3.11 virtual environment and activate it:
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Preview the site locally with:
   ```bash
   mkdocs serve
   ```

## Guidelines
- Make changes inside the `docs/` directory whenever possible.
- Do **not** commit build output (`site/`), `.DS_Store`, or other system files.
- Keep pull requests focused and easy to review.
- Summarize commit messages with what changed (e.g. "Add MkDocs docs and config").
- The navigation is handled automatically by `awesome-nav` using `docs/.nav.yml`.

Once your changes are pushed to the `main` branch, GitHub Actions will build and deploy the site.
