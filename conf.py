# -*- coding: utf-8 -*-
import sys, os
from datetime import date
import sphinx_rtd_theme

# Project
project = 'EduKit.me'
copyright = `date.today().year` + ' EduKit.me | <a href="ma&#105;lto&#58;%68i&#64;&#101;d&#117;kit&#46;me">hi&#64;&#101;dukit&#46;me</a>'

# Theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']
source_suffix = '.rst'
master_doc = 'index'
html_favicon = 'favicon.ico'
man_pages = [
    ('index', 1)
]
