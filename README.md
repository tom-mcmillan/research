# Research Notes

[![Build & Deploy Status](https://github.com/tom-mcmillan/research/actions/workflows/pages.yml/badge.svg)](https://github.com/tom-mcmillan/research/actions)

This repository hosts my personal research writings. Markdown source files live in the `docs/` folder. The site is built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme, and the static site is output to the `site/` folder.

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

## Continuous Deployment
Changes pushed to `main` automatically trigger the [pages.yml](.github/workflows/pages.yml)
workflow. It installs dependencies, builds the site with MkDocs, and publishes
the output to GitHub Pages using the official actions.

You can monitor build and deployment status via the badge at the top of this README
or by visiting the [Actions tab](https://github.com/tom-mcmillan/research/actions).

Simply commit and push your Markdown files to `main`, and your documentation will be live at:

```
https://tom-mcmillan.github.io/research/
```

> **Troubleshooting:** If your updates do not appear after a workflow run, you can manually deploy from your local environment:

```bash
mkdocs gh-deploy --clean
```
