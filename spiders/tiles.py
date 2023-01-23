import scrapy
from ..items import SpidertilesItem 
from scrapy.loader import ItemLoader



class TilesSpider(scrapy.Spider):
    name = 'tiles'
    allowed_domains = ['magnatiles.com']
    start_urls = ['http://magnatiles.com/products/page/1/']

    def parse(self, response):
        for p in response.css("ul.products li") :
            il = ItemLoader(item = SpidertilesItem(), selector =p)
            il.add_css('sku', 'a.button::attr(data-product_sku)')
            il.add_css('name', 'h2')
            il.add_css('price', 'bdi')
            yield il.load_item()