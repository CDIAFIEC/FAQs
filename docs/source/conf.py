# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Estructuras de Datos'	
copyright = '2025, Estructuras de Datos'
author = 'Allan Avendaño'

release = '0.1'
version = '0.1.0'

html_title = project
# html_logo = "_static/img/myimage.png"

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.graphviz',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    "sphinx_design",
    "hoverxref.extension",
    "sphinx_design_elements",
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_book_theme'	

html_theme_options = {
    "use_sidenotes": True,
    "rightsidebar": True
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
   'css/style.css',
]

# -- GraphViz configuration ----------------------------------
graphviz_output_format = 'svg'