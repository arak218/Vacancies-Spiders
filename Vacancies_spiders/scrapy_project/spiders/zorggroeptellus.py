import scrapy


class FiftyfirstSpider(scrapy.Spider):
    name = 'zorggroeptellus'

    start_urls = ['https://zorggroeptellus.nl/werken/vacatures/vacature-zorg']


    def parse(self, response):
        yield {
            'title': response.xpath('//div[@class="content"]/div/strong/u/text()').extract_first(),
            'text': response.xpath('//div[@class="content"]/div/text()').extract(),
            'url': response.request.url
        }

