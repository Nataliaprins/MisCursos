# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = "MisCursos"
copyright = "2026, Natalia Acevedo Prins"
author = "Natalia Acevedo Prins"
release = "0.1.0"

# -- General configuration ---------------------------------------------------
extensions = [
    "nbsphinx",
]

templates_path = ["_templates"]
exclude_patterns = ["Thumbs.db", ".DS_Store"]

language = "es"

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_book_theme"
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/Nataliaprins/MisCursos",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs/source",
}

# Crear .nojekyll automáticamente para GitHub Pages
import pathlib

nojekyll = pathlib.Path("../build/html/.nojekyll")
nojekyll.parent.mkdir(parents=True, exist_ok=True)
nojekyll.touch(exist_ok=True)
nojekyll.touch(exist_ok=True)
