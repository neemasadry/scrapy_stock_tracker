import scrapy
from re import search, sub
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from stock_tracker.items import StockTrackerItem
from datetime import datetime

# client = influxdb_client.InfluxDBClient('localhost', '8086', 'neema', 'password', '')

# with influxdb_client.InfluxDBClient(url=influxdb_url, token=token, org=org) as client:




class YfinanceSpider(scrapy.Spider):
    name = 'yfinance'
    allowed_domains = ['finance.yahoo.com']
    # start_urls = ['https://finance.yahoo.com/']
    start_urls = [
        # 'https://finance.yahoo.com/trending-tickers',
        # 'https://finance.yahoo.com/most-active',
        # 'https://finance.yahoo.com/gainers',
        # 'https://finance.yahoo.com/losers'
        'https://finance.yahoo.com/most-active?count=50&offset=0'
    ]

    # rules = (
    #     Rule(LinkExtractor(allow=(r'/quote/')), callback='parse_quote', follow=True)
    # )

    # def start_requests(self):


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
        table_row_urls = response.css("#screener-results #scr-res-table tbody tr a::attr(href)").getall()

        for row_url in table_row_urls:
            ticker_symbol = search(r"\s*=\s*([\S\s]+)", row_url).group()[1:]
            request_url = f'https://finance.yahoo.com{row_url}'
            print(f"Request sent for: {ticker_symbol} [{row_url}]")

            yield scrapy.Request(
                url=request_url,
                callback=self.parse_most_active_stocks,
                cb_kwargs={
                    'ticker_symbol': ticker_symbol
                }
            )



    def parse_most_active_stocks(self, response, ticker_symbol):
        for stock in response.css('#render-target-default'):
            il = ItemLoader(item=StockTrackerItem(), selector=stock)
            # quotes_table = response.css('section#screener-results div#fin-scr-res-table')
            # response.xpath('//*[@id="list-res-table"]')
            # stocks_most_active_table = response.css("#screener-results #scr-res-table tbody tr").getall()
            # stocks_most_active_table_length = len(stocks_most_active_table)
            # print("Number of stocks to scrape: %d", stocks_most_active_table_length)


            company_name = response.css('#quote-header-info div div h1::text').get()
            sanitized_company_name = sub("\((.*?)\)", "", company_name).replace('"', '')
            il.add_value('company_name', sanitized_company_name)

            stock_price = response.css('#quote-header-info fin-streamer::text').get()
            il.add_value('stock_price', stock_price)

            il.add_value('ticker_symbol', ticker_symbol)

            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            il.add_value('current_time', current_time)

            yield il.load_item()










