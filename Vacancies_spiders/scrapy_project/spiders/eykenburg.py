import scrapy


class EigteenthSpider(scrapy.Spider):
    name = "eykenburg"

    start_urls = ['http://www.eykenburg.nl/vacatures']


    def parse(self, response):
        yield {
            'title': response.xpath('.//h1/text()').extract(),
            'text': response.xpath('.//p/text()').extract(),
            'url': response.request.url
        }

