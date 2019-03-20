# -*- coding: utf-8 -*-
import scrapy
from first.items.film import Film
from scrapy.loader import ItemLoader

class TestspiderSpider(scrapy.Spider):
    name = 'testspider'
    allowed_domains = ['80s.la']
    start_urls = ['http://80s.la/']

    # self.logger 是日志打印对象
    def parse(self, response):
        self.logger.info( '设置实例对象__doc__信息：', self.settings.__doc__ )
        self.logger.info('我在打印日志')
        # filmnames = response.css('.me1 h3 a::text').getall()
        # for  name in filmnames:
        #     film = Film( filename = name )
        #     yield film
        il = ItemLoader( item =  Film(), response = response )
        il.add_css('filename', '.me1 h3 a')
        return il.load_item()