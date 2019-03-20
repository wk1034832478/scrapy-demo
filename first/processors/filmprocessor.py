from scrapy.loader import ItemLoader
def lowercase_processor(self, values):
    for v in values:
        yield v.upper()

def add_dollar(self, values):
    for v in values:
        yield v + '$'

class MyItemLoader(ItemLoader):
    filename_in = lowercase_processor
    default_output_processor = add_dollar