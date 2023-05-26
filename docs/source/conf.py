# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Leetcode Notes'
copyright = '2023'
author = 'Anant Singh'

release = '1.0'
version = '1.0.0'



# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path=['custom/templates']



# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_show_sourcelink = False

# Default
# html_theme_options = {
#     'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
#     'analytics_anonymize_ip': False,
#     'logo_only': False,
#     'display_version': True,
#     'prev_next_buttons_location': 'bottom',
#     'style_external_links': False,
#     'vcs_pageview_mode': '',
#     'style_nav_header_background': 'white',
#     # Toc options
#     'collapse_navigation': True,
#     'sticky_navigation': True,
#     'navigation_depth': 4,
#     'includehidden': True,
#     'titles_only': False
# }

html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#282828',
    # 'toc_title':"{Contents}",
    # "show_toc_level": 2,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': False,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_logo = 'assets/leetcode-logo.png'

html_static_path = ['custom/static']

html_favicon = 'assets/favicon.ico'



# -- Options for EPUB output
epub_show_urls = 'footnote'

# import re
# def alpha_sort(iterable):
#         '''
#         Sorts the given iterable in the way that humans expect, by interpreting alphanumeric strings as integers.

#         Args:
#             iterable: A sequence (e.g. list, tuple, etc.) to be sorted.

#         Returns:
#             iterable: A sorted list of items from the input iterable.
#         '''
#         if iterable == None:
#             return None
#         if len(iterable) == 0:
#             return iterable
#         if iterable[0] and not isinstance(iterable[0], str):
#             return sorted(iterable)
#         else:
#             def convert(text): return int(text) if text.isdigit() else text
#             def alphanum_key(key): return [convert(c)
#                                            for c in re.split('([0-9]+)', key)]
#             return sorted(iterable, key=alphanum_key)
        
# def sort_by_number(filename):
#     match = re.match(r'^(\d+)\.', filename)
#     if match:
#         return int(match.group(1))
#     else:
#         return float('inf')

# def convert(text): return int(text) if text.isdigit() else text
# def alphanum_key(key): return [convert(c) for c in re.split('([0-9]+)', key)]
           

# def sort_toc_tree(app, doctree):
#     if not app.builder.name == 'html':
#         return
#     toctrees = doctree.traverse(condition=lambda node: node.tagname=='toctree')
#     for toctree in toctrees:
#         entries = toctree.children
#         with open('entries.log','w') as f:
#             f.write(f'{entries}')
#             f.write(f'\n\n{doctree.tagname}')
#             f.write(f'\n\n{type(entries)}')
#             # f.write(f'\n\n{type(entries[0])}')
#             # f.write(f'\n\n{entries[0]}')
#         # entries.sort(key=lambda e: sort_by_number(e[0].astext()))
#         entries.sort(key=alphanum_key)

# def setup(app):
#     app.connect('doctree-read', sort_toc_tree)
