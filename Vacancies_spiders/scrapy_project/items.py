# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


class ZorgnedProjectItem(scrapy.Item):
    functietitel = scrapy.Field()
    tekst = scrapy.Field()
    url = scrapy.Field()
