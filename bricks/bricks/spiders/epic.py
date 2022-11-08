import scrapy


class EpicSpider(scrapy.Spider):
    name = 'epic'
    allowed_domains = ['epicentrk.ua']
    start_urls = ['https://epicentrk.ua/ua/shop/kirpich-ogneupornyy-pok-225x111x65-mm.html']

    def parse(self, response):
        title = response.css(".p-header__title::text").get()
        price = float(response.css(".p-price__main::text").get())
        return {
            "title": title,
            "price": price
        }
