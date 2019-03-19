import scrapy

class SupermanSpider(scrapy.Spider):
    name = "guangdongjixie"
    
    def start_requests(self):
        urls = [
            'http://b2b.huangye88.com/guangdong/jixie/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
	# 返回公司名的迭代
    def parse(self, response):
        for text in response.css('a[itemprop=name]::text').getall():
            yield { 'corporation_name': text }
        myas = response.css('.page_tag.Baidu_paging_indicator a')
        for a in myas:
            if a.re(r'下一页'):
                yield response.follow( a , callback=self.parse)