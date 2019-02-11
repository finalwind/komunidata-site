#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Win'
SITENAME = 'komunidata'
SITEURL = ''

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_URL = 'blog/{slug}.html'
STATIC_PATHS = ['static']

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('treeclouds', 'http://treeclouds.com/'),)

# Social widget
SOCIAL = (('Email', 'mailto:windalfinc@gmail.com', 'envelope'),
          ('Twitter', 'https://twitter.com/windalfin'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True