import scrapy


class ThirdSpider(scrapy.Spider):
    name = 'altrecht'

    start_urls = ['https://www.werkenbijaltrecht.nl/vacatures']

    def parse(self, response):
        next_page = response.xpath('//td[3]/p/a/@href').extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse(self, response):
        yield {
            'title': response.xpath('.//td[@style="padding-left: 5px;"]/text()').extract(),
            'text': response.xpath('.//td/text()').extract(),
            'url': response.request.url
        }

