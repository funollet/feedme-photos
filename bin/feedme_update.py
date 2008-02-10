#!/usr/bin/env python
# -*- coding: utf-8 -*-
# feedme_update.py
"""
Refreshes every Feed ("Feedme for Django" application.) 
"""

from django.core.management import setup_environ
import settings
setup_environ(settings)

from feedme.models import Feed


def main ():
    feeds = Feed.objects.all()
    for some_feed in feeds:
        some_feed.update (force_update=True)


if __name__ == '__main__':
    main()
