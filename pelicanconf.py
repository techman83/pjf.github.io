#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Leon Wright'
SITENAME = '"Techman83\'s Blog"'
SITEURL = 'http://techman83.me'

MARKDOWN = {
    'extension_configs': {
        'mdx_video': {},
    },
    'output_format': 'html5',
}

MD_EXTENSIONS = [
    'mdx_video',
]

PATH = 'content'
PLUGIN_PATHS = [
    './plugins',
]
PLUGINS = [
    'related_posts',
    'summary',
    'jinga2content',
]

OUTPUT_PATH = './_site/'
STATIC_PATHS = [
    'images',
    'js',
]

EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
    'images/favicon.png': {'path': 'favicon.png'},
}

JINJA2CONTENT_TEMPLATES = [
    './_content',
]

# THEME
THEME = "./themes/pelican-bootstrap3/"
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGINS = ['i18n_subsites']
BOOTSTRAP_THEME = "simplex"
DISPLAY_PAGES_ON_MENU ="true"


#SITELOGO = 'images/my_site_logo.png'

TIMEZONE = 'Australia/Perth'

FILENAME_METADATA = '(?P<slug>.*)'

DEFAULT_LANG = 'en'
RELATED_POSTS_MAX = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
