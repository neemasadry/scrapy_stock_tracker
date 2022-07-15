import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime


class BloombergSpider(scrapy.Spider):
    name = 'bloomberg'
    allowed_domains = ['bloomberg.com']
    start_urls = [
        'https://www.bloomberg.com/quote/INDU:IND/members'
    ]

    headers = {
       "Connection": "keep-alive",
       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
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
        )

    def parse(self, response):
        response.css('main#content')
