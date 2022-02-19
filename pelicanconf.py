#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Yong Yong Cheng"
SITENAME = "时间 · 空间 · 相间"
SITESUBTITLE = "Time · Space · Phase"
GITHUB_URL = "https://github.com/aarnchng"

# can be useful in development,
# but set to False when you're ready to publish
RELATIVE_URLS = True

DEFAULT_LANG = "en"
DEFAULT_PAGINATION = False
DEFAULT_DATE = (2020, 9, 26, 0, 0, 0)
REVERSE_CATEGORY_ORDER = True
THEME = "themes/pelican-sober"
TIMEZONE = "Asia/Singapore"
LOCALE = "C"

FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"

SOCIAL = None
LINKS = (("时间 · 空间", "https://aarnchng.blogspot.com/"),)

READERS = {"html": None}
PYGMENTS_RST_OPTIONS = {"linenos": "table"}

STATIC_PATHS = ["favicon"]
TEMPLATE_PAGES = {}
EXTRA_PATH_METADATA = {"favicon/favicon.ico": {"path": "favicon.ico"}}
