# Research Notes

This repository hosts my personal research writings. Markdown source files live in the `docs/` folder. The site is built with [MkDocs](https://www.mkdocs.org/) and the [Material](https://squidfunk.github.io/mkdocs-material/) theme, and the static site is output to the `site/` folder.

## Local Preview

To run a local live-reloading preview server:

```bash
pip install mkdocs-material
mkdocs serve
```

Then open <http://127.0.0.1:8000> in your browser.

## Building & Publishing

To rebuild the site and commit the updated HTML:

```bash
mkdocs build
touch site/.nojekyll
git add site
git commit -m "Update site"
git push
```

### GitHub Pages Setup

In your GitHub repository's **Settings > Pages**, set the source to the `main` branch's `/site` folder. Your site will then be available at:

```
https://tom-mcmillan.github.io/research/
```