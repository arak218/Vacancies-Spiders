import scrapy


class TwentyfirstSpider(scrapy.Spider):
    name = "gkracht"

    start_urls = ['http://www.g-kracht.com/pages/nl/vacatures/']

    def parse(self, response):
        yield {
            'title': response.xpath('//div[2]/p/strong/text()').extract_first(),
            'text': response.xpath('//div[2]/p/text()').extract(),
            'url': response.request.url
        }
