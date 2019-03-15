import scrapy


class TwentysecondSpider(scrapy.Spider):
    name = 'havenpol'

    start_urls = ['https://www.havenpolikliniek.nl/vacatures/']

    def parse(self, response):
        yield {
            'title': response.xpath('//h2/text()').extract_first(),
            'text': response.xpath('//article[@class="content"]/p[2]/text()').extract(),
            'url': response.request.url
        }

