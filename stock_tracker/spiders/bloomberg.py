import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime

# client = influxdb_client.InfluxDBClient('localhost', '8086', 'neema', 'password', '')

# with influxdb_client.InfluxDBClient(url=influxdb_url, token=token, org=org) as client:


class BloombergSpider(scrapy.Spider):
    name = 'bloomberg'
    allowed_domains = ['bloomberg.com']
    start_urls = [
        # 'http://bloomberg.com/'
        'https://www.bloomberg.com/quote/INDU:IND/members'
    ]

    headers = {
       # "Host": "c.go-mpulse.net",
       # "Origin": "https://www.burberry.com",
       # "Referer": "https://www.burberry.com/",
       "Connection": "keep-alive",
       # "Cache-Control": "max-age=0",
       # "Upgrade-Insecure-Requests": "1",
       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
       # "Accept": "*/*",
       # "DNT": "1",
       "Accept-Encoding": "gzip, deflate, br",
       "Accept-Language":"en-US,en;q=0.9"
    }

    def start_requests(self):
        'https://www.nasdaq.com/market-activity/stocks/screener'
        
        yield scrapy.Request(
            url=temp_link,
            callback=self.parse,
            meta={
                'splash': {
                    'args': {
                        'wait': 3.0,
                        'resource_timeout': 10.0,
                        'timeout': 50.0
                    },
                    'endpoint': "render.html"
                }
            },
            # cb_kwargs={
            #     'nav_category_group_key': nav_category_group_key,
            #     'nav_category_key': nav_category_key,
            #     'nav_c_value': nav_c_value[0],
            #     'nav_c_list': nav_c_value
            # }
        )

    def parse(self, response):
        response.css('main#content')
