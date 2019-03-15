import scrapy


class SixteenthSpider(scrapy.Spider):
    name = "edt_maastricht"

    start_urls = ['https://www.edtmaastricht.nl/vacatures/index.html']


    def parse(self, response):
        yield {
            'text': response.xpath('//p[5]/text()').extract(),
            'url': response.request.url
        }
