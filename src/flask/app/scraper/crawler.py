from twisted.internet import reactor

from app.scraper.scraper.spiders.nic import NicSpider
from scrapy.crawler import CrawlerProcess, CrawlerRunner

runner = CrawlerRunner({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    # 'FEED_FORMAT': 'csv',
    # 'FEED_URI': 'output.csv',
})
d = runner.crawl(NicSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()  # the script will block here until the crawling is finished
