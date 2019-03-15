import scrapy


class ThirtySixthSpider(scrapy.Spider):
    name = 'ouderenzorg_annenborch'

    start_urls = ['http://www.annenborch.nl/30/werken-bij-annenborch']

    def parse(self, response):
        yield {
            'title': response.xpath('//article/p[3]/text()').extract_first(),
            'text': response.xpath('//article/p/text()').extract(),
            'url': response.request.url
        }
