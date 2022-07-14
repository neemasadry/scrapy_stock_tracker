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
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.client.write_api import ASYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "e_se0YBgpHmSSe4Uj-AzFVQ3U8ImnzD0J_4tE50x0e61ruWP4BUuiyhHCsanC1mjpQ09iMvdn6CxsmvvVKedkA=="
org = "Hackathon Team"
bucket = "stock_tracker"
influxdb_url = "http://localhost:8086"



class StockTrackerPipeline:
    def __init__(self):
        client = influxdb_client.InfluxDBClient(
            url=influxdb_url,
            token=token,
            org=org
        )

    def process_item(self, item, spider):
        write_api = client.write_api(write_options=SYNCHRONOUS)

        data = "mem,host=host1 used_percent=23.43234543"
        write_api.write(bucket, org, data)
        return item

        
