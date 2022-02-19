#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa

SITEURL = "https://aarnchng.github.io"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
AUTHOR_FEED_ATOM = "feeds/{slug}.atom.xml"
AUTHOR_FEED_RSS = "feeds/{slug}.rss.xml"

DELETE_OUTPUT_DIRECTORY = True
