#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site Config
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
TIMEZONE = 'Australia/Perth'

# Pelican Config
PLUGIN_PATHS = [
    'plugins',
]

PLUGINS = [
    'jinja2content',
    'summary',
    'related_posts',
    'i18n_subsites',
	'sitemap',
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

# THEME
THEME = "./themes/pelican-bootstrap3/"
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
BOOTSTRAP_THEME = "spacelab"
PYGMENTS_STYLE = 'vim'
DISPLAY_PAGES_ON_MENU ="true"
CUSTOM_CSS = "./css/style.min.css"
CUSTOM_JS = "./js/compiled-bundle.min.js"

# Site generation
ARTICLE_URL = "{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{date:%Y}/{date:%m}/{date:%d}/{slug}.html"
CATEGORY_URL = "{slug}"
CATEGORY_SAVE_AS = "{slug}/index.html"

DEFAULT_LANG = 'en'

# Feeds
FEED_ALL_ATOM = "feeds/all-atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s-atom.xml"
FEED_ALL_RSS = "feeds/all-rss.xml"
CATEGORY_FEED_RSS = "feeds/%s-rss.xml"

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Blogroll
LINKS = (
    ('PJF', 'http://pjf.github.io'),
    ('Superhouse.tv', 'http://superhouse.tv'),
    ('Big Clive', 'http://bigclive.com'),
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
