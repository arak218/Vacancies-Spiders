import scrapy


class FortyEighthSpider(scrapy.Spider):
    name = 'woonzorgbcm'

    start_urls = ['http://www.woonzorgbcm.nl/werken-bij-bcm/vacatures/']


    def parse(self, response):
        yield {
            'title': response.xpath('//p/a/text()').extract_first(),
            'text': response.xpath('//div/p/text()').extract(),
            'url': response.request.url
        }
