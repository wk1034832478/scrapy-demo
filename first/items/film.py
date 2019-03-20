import scrapy
class Film(scrapy.Item):
    # 电影名
    filename = scrapy.Field()
    # 作者
    author = scrapy.Field()