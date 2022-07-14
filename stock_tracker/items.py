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

def strip_whitespace(value):
    return value.strip()

def remove_quotations(value):
    return value.replace('"', '')

class StockTrackerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ticker_symbol = scrapy.Field(input_processor = MapCompose(remove_tags, replace_escape_chars, replace_entities, strip_whitespace), output_processor = TakeFirst())
    company_name = scrapy.Field(input_processor = MapCompose(remove_tags, replace_escape_chars, replace_entities, strip_whitespace, remove_quotations), output_processor = TakeFirst())
    current_time = scrapy.Field()
    stock_price = scrapy.Field(input_processor = MapCompose(remove_tags, replace_escape_chars, replace_entities, strip_whitespace), output_processor = TakeFirst())

