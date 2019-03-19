import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.80s.la/movie/list/-2019----p1',
            'https://www.80s.la/movie/list/-2019----p2',
        ]
		# 提供爬取的url，并设置爬取后的回调函数
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
		#response.css('.clearfix h3 a');