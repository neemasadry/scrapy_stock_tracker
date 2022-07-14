import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime


class NasdaqSpider(scrapy.Spider):
    name = 'nasdaq'
    allowed_domains = ['nasdaq.com']
    start_urls = [
        # 'http://nasdaq.com/',
        'https://www.nasdaq.com/market-activity/stocks/screener'
    ]

    # def parse_rows(self, response):
        
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

    def parse(self, response):
        response.css("main.page__main span.symbol-page-header__pricing_price")
