import sys, os
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.ifconfig', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'pypi-stat'
copyright = u'2012, Julien Tayon'
version = u'1.2.5'
release = u'1.2.5'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'nature'
html_static_path = ['_static']
htmlhelp_basename = 'pypi-statdoc'
latex_elements = {
}
latex_documents = [
  ('index', 'pypi-stat.tex', u'pypi-stat Documentation',
   u'Julien Tayon', 'manual'),
]
man_pages = [
    ('index', 'pypi-stat', u'pypi-stat Documentation',
     [u'Julien Tayon'], 1)
]
texinfo_documents = [
  ('index', 'pypi-stat', u'pypi-stat Documentation',
   u'Julien Tayon', 'pypi-stat', u'One line description of project.',
   u'Miscellaneous'),
]
