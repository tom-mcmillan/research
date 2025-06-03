# Research Notes

[![Build & Deploy Status](https://github.com/tom-mcmillan/research/actions/workflows/pages.yml/badge.svg)](https://github.com/tom-mcmillan/research/actions)

This repository hosts my personal research writings. Markdown source files live in the `docs/` folder (anything outside `docs/`, such as a top-level `knowledge/` folder, will not be included in the published site). The site is built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme, and the static site is output to the `site/` folder.

## Setup

Create and activate a Python virtual environment (Python 3.11 or earlier):

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```
> **Note:** This requirements file installs the `mkdocs-awesome-nav` plugin directly from its GitHub repository (`https://github.com/lukasgeiter/mkdocs-awesome-nav`) to ensure the latest navigation features.

## Local Preview

To run a local live-reloading preview server:

```bash
mkdocs serve
```

Then open <http://127.0.0.1:8000> in your browser.


## Bibliography Builder

Pull items from your Zotero collection and generate a numbered, MLA-style
bibliography in Markdown format by running the `build_bibliography.py` script.

Ensure you have a top-level `.env` file with your Zotero credentials:
```bash
ZOTERO_API_KEY=<your Zotero API key>
ZOTERO_USER_ID=<your numeric Zotero user ID>
ZOTERO_COLLECTION_KEY=<your Zotero collection key>
```

Then run:
```bash
source .venv/bin/activate
python3 scripts/build_bibliography.py
```

This will overwrite `docs/pedagogy/bibliography.md` with a numbered,
MLA (9th edition) citation list, using Markdown italics for titles.
```

## Continuous Deployment
This site uses MkDocs Material and is automatically built and deployed to GitHub Pages via GitHub Actions whenever you push changes to the `main` branch.

> **No manual Pages setup is required**—the GitHub Actions workflow defined in `.github/workflows/pages.yml` configures and publishes the site for you.
>
> You can monitor build and deployment status via the badge at the top of this README or by visiting the [Actions tab](https://github.com/tom-mcmillan/research/actions).

Simply commit and push your Markdown files to `main`, and your documentation will be live at:

```
https://tom-mcmillan.github.io/research/
```

> **Troubleshooting:** If your updates do not appear after a workflow run, you can manually deploy from your local environment:

```bash
mkdocs gh-deploy --clean
```
