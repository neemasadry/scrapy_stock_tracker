# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# send_data.py - InfluxDB Intern Hackathon
# File containing functions to: 
# 1. parse a CSV file that contains stock tickers, prices, sources, and dates
# 2. send organized data to a bucket in InfluxDB

import scrapy, os, sys, csv
from datetime import datetime
from mimetypes import guess_extension
from pathlib import Path
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from urllib.parse import urlsplit
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
bucket = "stocks_recent"
org = "9c5955fc99a60b8f"
token = "Z1zTLcdabiA3tXhxQ3vHqt5_UVy0TJLrYVqdpomCr8FnYCGKJMKmQfeNOgcISV2qoNJkYGvuWm2c-gsWpj41tw=="


class StockTrackerPipeline:

    def process_item(self, item, spider):
        with InfluxDBClient(url="https://twodotoh-dev-andrew20220517115401.remocal.influxdev.co", token=token, org=org) as client:
            write_api = client.write_api(write_options=SYNCHRONOUS)
            
            with open('yfinance.csv', 'r') as f:          # Read lines separately
                reader = csv.reader(f, delimiter=',')
                for line in reader:
                    if line[0] == "company_name": continue
                
                    p = Point("Stocks") \
                        .tag("Ticker", "Ticker") \
                        .field(line[3], float(line[2])) \
                        .time(line[1])
                    
                    write_api.write(bucket, org, p)
