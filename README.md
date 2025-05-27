# Research Notes

This repository hosts my personal research writings. Markdown source files live in the `docs/` folder. The site is built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme, and the static site is output to the `site/` folder.

## Local Preview

To run a local live-reloading preview server:

```bash
pip install mkdocs-material
mkdocs serve
```

Then open <http://127.0.0.1:8000> in your browser.
## Continuous Deployment

This site uses MkDocs Material and is automatically built and deployed to GitHub Pages via GitHub Actions whenever you push changes to the `main` branch.
Simply commit and push your Markdown files to `main`, and your documentation will be live at:

```
https://tom-mcmillan.github.io/research/
```