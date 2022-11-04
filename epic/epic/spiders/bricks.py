import scrapy


class BricksSpider(scrapy.Spider):
    name = 'bricks'
    allowed_domains = ['epicentrk.ua']
    start_urls = ['https://epicentrk.ua/ua/shop/kirpich-ogneupornyy-pok-225x111x65-mm.html']

    def parse(self, response):
        filename = 'bricks.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
