import scrapy


class ThirtyFifthSpider(scrapy.Spider):
    name = 'molendrift'

    start_urls = ['https://www.molendrift.nl/organisatie/werken-bij-molendrift']

    def parse(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract(),
            'text': response.xpath('//p/text()')[4].extract(),
            'url': response.request.url
        }
