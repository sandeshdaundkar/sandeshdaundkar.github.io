#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

AUTHOR = 'Sandesh Daundkar'
SITENAME = "Sandesh's Blog"
SITEURL = ''
SITETITLE = SITENAME
SITESUBTITLE = 'Python Django Developer'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_RSS = 'feeds/%s.rss.xml'
RSS_FEED_SUMMARY_ONLY = False

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None


# Social widget
SOCIAL = (('github', 'https://github.com/sandeshdaundkar'),
          ('stack-overflow', 'https://stackoverflow.com/users/9202733/sandeshdaundkar'),
          ('linkedin', 'https://www.linkedin.com/in/sandesh-daundkar'),
          ('twitter', 'https://twitter.com/sandeshdaundkar'),
          ('facebook', 'https://www.facebook.com/sandeshdaundkr'))

DEFAULT_PAGINATION = 10
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }
THEME = './Flex'
PYGMENTS_STYLE = "monokai"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Menu Config
MAIN_MENU = True
HOME_HIDE_TAGS = True
DISPLAY_PAGES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = False

MENUITEMS = (
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = "Sandesh Daundkar"


THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
}


# Plugins Config
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['post_stats', 'series', 'representative_image', 'liquid_tags']
ADD_THIS_ID = "ra-5f68af799642611f"
