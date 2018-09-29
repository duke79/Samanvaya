# -*- coding: utf-8 -*-
import scrapy


class NicSpider(scrapy.Spider):
    print("class \n\n\n\n\n\n")
    name = 'nic'
    allowed_domains = ['resultsarchives.nic.in']
    start_urls = ['http://resultsarchives.nic.in/cbseresults/cbseresults2006/class10/cbse10.htm']

    def parse(self, response):
        print("\n\n\n\n\n\n")
        # Extracting the content using css selectors
        # titles = response.css('.title.may-blank::text').extract()
        print("\n\n\n\n\n\n")
        print(response.body)
        all = response.css('div').extract()
        titles = response.css('div font b').extract()
        print("\n\n\n\n\n\n")
        print(titles)
        votes = response.css('.score.unvoted::text').extract()
        times = response.css('time::attr(title)').extract()
        comments = response.css('.comments::text').extract()

        # Give the extracted content row wise
        for item in zip(titles, votes, times, comments):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title': item[0],
                'vote': item[1],
                'created_at': item[2],
                'comments': item[3],
            }

            # yield or give the scraped info to scrapy
            yield scraped_info
