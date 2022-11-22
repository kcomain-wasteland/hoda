# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../../"))

# -- Project information -----------------------------------------------------

project = "hoda"
copyright = "2021-2022, soopyc"
author = "soopyc"
html_title = "hoda"
REPO = "https://patchy.soopy.moe/mizuki/hoda"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    # 'sphinx.ext.autosummary',
    "sphinx_copybutton",
    "sphinxext.opengraph"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

locale_dirs = ["../locale/"]
gettext_compact = "hoda"

# -- Options for Sphinx AutoDoc ----------------------------------------------
autodoc_default_options = {"special-members": "__init__"}
autodoc_class_signature = "separated"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Custom CSS styling files
# Files are relative to $html_static_path
html_css_files = [
    "css/font-weight.css"
]

# Theme options for goode.
html_theme_options = {
    "footer_icons": [
        {
            "name": "Git",
            "url": REPO,
            "html": """
            <svg xmlns="http://www.w3.org/2000/svg" stroke="currentColor" fill="currentColor" width="92pt" height="92pt" viewBox="0 0 92 92"><defs><clipPath id="a"><path d="M0 .113h91.887V92H0Zm0 0"/></clipPath></defs><g clip-path="url(#a)"><path style="stroke:none;fill-rule:nonzero;fill:#100f0d;fill-opacity:1" d="M90.156 41.965 50.036 1.848a5.913 5.913 0 0 0-8.368 0l-8.332 8.332 10.566 10.566a7.03 7.03 0 0 1 7.23 1.684 7.043 7.043 0 0 1 1.673 7.277l10.183 10.184a7.026 7.026 0 0 1 7.278 1.672 7.04 7.04 0 0 1 0 9.957 7.045 7.045 0 0 1-9.961 0 7.038 7.038 0 0 1-1.532-7.66l-9.5-9.497V59.36a7.04 7.04 0 0 1 1.86 11.29 7.04 7.04 0 0 1-9.957 0 7.04 7.04 0 0 1 0-9.958 7.034 7.034 0 0 1 2.308-1.539V33.926a7.001 7.001 0 0 1-2.308-1.535 7.049 7.049 0 0 1-1.516-7.7L29.242 14.273 1.734 41.777a5.918 5.918 0 0 0 0 8.371L41.855 90.27a5.92 5.92 0 0 0 8.368 0l39.933-39.934a5.925 5.925 0 0 0 0-8.371"/></g></svg>
            """
        }
    ],
    "source_edit_link": f"{REPO}/src/branch/master/docs/source/{{filename}}"
}

# autosummary_generate = True
autosectionlabel_prefix_document = True

extlinks = {
    "issue": (f"{REPO}/issues/%s", "BUG-%s"),
}

# Links used for cross-referencing stuff in other documentation
intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "aio": ("https://docs.aiohttp.org/en/stable/", None),
}
