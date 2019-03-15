import scrapy


class ThirtyEigthSpider(scrapy.Spider):
    name = 'perspectief'

    start_urls = ['https://www.perspectief.net/werken-bij-perpectief/']

    def parse(self, response):
        yield {
            'title': response.xpath('//li/strong/a/text()').extract(),
            'text': response.xpath('//div/p/text()').extract(),
            'url': response.request.url
        }

