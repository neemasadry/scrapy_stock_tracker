# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy, re
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join, SelectJmes
from w3lib.html import remove_tags, replace_escape_chars, replace_entities
from urllib.parse import urlparse
from unicodedata import normalize


class StockTrackerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
