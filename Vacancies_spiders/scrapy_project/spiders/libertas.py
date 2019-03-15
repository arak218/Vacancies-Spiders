import scrapy


class TwentyEighthSpider(scrapy.Spider):
    name = 'libertas'

    start_urls = ['https://www.werkenbijlibertasleiden.nl/c/vacatures']

    def parse(self, response):
        yield {
            'title': response.xpath('//h1/div/text()').extract(),
            'text': response.xpath('//span/a/text()').extract(),
            'url': response.request.url
        }
