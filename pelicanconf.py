#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Leon Wright AKA Techman83'
SITENAME = '"Techman83\'s Blog"'
SITEURL = 'http://techman83.me'

PATH = 'content'
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['extract_toc']
OUTPUT_PATH = './_site/'
STATIC_PATHS = ['images']
EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
    'images/favicon.png': {'path': 'favicon.png'},
}

# THEME
THEME = "./themes/pelican-bootstrap3/"
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGINS = ['i18n_subsites']
BOOTSTRAP_THEME = "simplex"

#SITELOGO = 'images/my_site_logo.png'

TIMEZONE = 'Australia/Perth'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
