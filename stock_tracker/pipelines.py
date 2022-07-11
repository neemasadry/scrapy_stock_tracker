# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy, os, sys
from datetime import datetime
from mimetypes import guess_extension
from pathlib import Path
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from urllib.parse import urlsplit
from models import *


class StockTrackerPipeline:
    def process_item(self, item, spider):
        return item

        
