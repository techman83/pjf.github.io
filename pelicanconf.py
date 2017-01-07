#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Leon Wright'
SITENAME = 'Techman83\'s Blog'
SITEURL = 'http://techman83.me'
CC_LICENSE = 'CC-BY'
GITHUB_USER = 'techman83'
GITHUB_REPO_COUNT = 4
TWITTER_USERNAME = 'Techman_83'
GOOGLE_ANALYTICS = "UA-39211824-2"
DISQUS_SITENAME = "techman83"
ADDTHIS_PROFILE = "ra-52df33e30fca36e7"
GITTIP_SITE = "https://www.gittip.com/techman83/"
FAVICON = 'img/favicon.png'
AVATAR = 'img/leon-vr.png'

PLUGIN_PATHS = [
    'plugins',
]

PLUGINS = [
    'jinja2content',
    'summary',
    'related_posts',
    'i18n_subsites',
]

MARKDOWN = {
    'extension_configs': {
        'mdx_video': {},
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
    },
    'output_format': 'html5',
}

PATH = 'content'

RELATED_POSTS_MAX = 10

OUTPUT_PATH = './_site/'
STATIC_PATHS = [
    'img',
    'js',
    'css',
]

EXTRA_PATH_METADATA = {
#    'extra/robots.txt': {'path': 'robots.txt'},
    'images/favicon.png': {'path': 'favicon.png'},
}

# THEME
THEME = "./themes/pelican-bootstrap3/"
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
BOOTSTRAP_THEME = "spacelab"
PYGMENTS_STYLE = 'vim'
DISPLAY_PAGES_ON_MENU ="true"
CUSTOM_CSS = "./css/style.min.css"
CUSTOM_JS = "./js/compiled-bundle.min.js"


#SITELOGO = 'images/my_site_logo.png'

TIMEZONE = 'Australia/Perth'

ARTICLE_URL = "{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
CATEGORY_URL = "{slug}"
CATEGORY_SAVE_AS = "{slug}/index.html"

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

# Blogroll
LINKS = (
    ('PJF', 'http://pjf.github.io'),
)

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/Techman83'),
    ('Twitter', 'https://twitter.com/Techman_83'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
LOAD_CONTENT_CACHE = False
