import scrapy


class SupermanSpider(scrapy.Spider):
    name = "superman"
    
    def start_requests(self):
        print('参数：', getattr(self, 'tag', '默认tag') )
        urls = [
            'https://www.80s.la/movie/list/', 
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
	# 返回电影名的迭代
    def parse(self, response):
        for text in response.css('.me1.clearfix h3 a::text').getall():
            yield { 'film_name': text.replace('\\n', '').strip() }
        myas = response.css('.pager a')
        for a in myas:
            if a.re(r'下一页'):
                yield response.follow( a , callback=self.parse)