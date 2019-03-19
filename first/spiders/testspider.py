# -*- coding: utf-8 -*-
import scrapy


class TestspiderSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['80s.la']
    start_urls = ['http://80s.la/']

    def parse(self, response):
        self.logger.info('我在打印日志')
