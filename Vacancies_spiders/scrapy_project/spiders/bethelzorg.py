import scrapy


class SeventhSpider(scrapy.Spider):
    name = 'bethelzorg'

    start_urls = ['https://www.bethelzorg.nl/werken-bij/']

    def parse(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@class="col-lg-8"]/p/text()').extract(),
            'url': response.request.url
        }

