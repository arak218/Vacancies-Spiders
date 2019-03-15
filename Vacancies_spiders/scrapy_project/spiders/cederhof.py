import scrapy


class TwelfthSpider(scrapy.Spider):
    name = 'cederhof'


    start_urls = ['http://www.cederhof.eu/vacatures/vacatures-cederhof']

    def parse(self, response):
        yield {
            'title': response.xpath('//div[@class="field-items"]/div/h2/text()').extract(),
            'text': response.xpath('//div[@class="field-items"]/div/p/text()').extract(),
            'url': response.request.url
        }



