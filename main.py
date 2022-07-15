import schedule, time, os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

print('Scheduler initialised')
schedule.every(30).seconds.do(lambda: os.system('scrapy crawl yfinance -o yfinance.csv -t csv'))
print('Next job is set to run at: ' + str(schedule.next_run()))

while True:
    schedule.run_pending()
    time.sleep(1)

