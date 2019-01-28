#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__name__), '..'))

import lightkurve


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'nbsphinx',
    'numpydoc',
    'sphinx_automodapi.automodapi']

numpydoc_show_class_members = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Exclude build directory and Jupyter backup files:
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Lightkurve'
copyright = 'Lightkurve developers'
author = 'Kepler/K2 Guest Observer Office'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = lightkurve.__version__.split('.dev')[0]
# The full version, including alpha/beta/rc tags.
release = lightkurve.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["**/.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Some notebook cells take longer than 60 seconds to execute
nbsphinx_timeout = 300

# PUT PROLOG HERE
nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::
        **This page is a static version of an interactive Jupyter notebook**

        - Try the interactive version: :raw-html:`<a href="https://mybinder.org/v2/gh/KeplerGO/lightkurve/master?filepath=docs/source/{{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>`

        - Download the source file: `{{ docname }}`__

    __ https://github.com/KeplerGO/lightkurve/blob/master/docs/source/
        {{ docname }}

"""

# -- Options for HTML output ----------------------------------------------
html_theme = 'kurvian'
html_theme_path = ['../']

html_theme_options = {
    "navbar_title": "Lightkurve v" + version,
    "navbar_links": [
        ("Quickstart", "quickstart"),
        ("Tutorials", "tutorials/index"),
        ("API", "api"),
        ("About", "about/index"),
    ],
}

html_title = "Lightkurve"

html_static_path = ['_static']

sys.path += ['exts']
extensions += ['sphinxcontrib_rawfiles']
rawfiles = ['CNAME']  # Files we want to copy
