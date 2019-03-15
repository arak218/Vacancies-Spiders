import scrapy


class FortyFifthSpider(scrapy.Spider):
    name = 'talma'

    start_urls = ['https://www.talma-urk.nl/werken-bij-talma/vacatures']

    def parse(self, response):
        urls = response.xpath('//h2/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        yield {
            'title': response.xpath('//h2/text()').extract_first(),
            'text': response.xpath('//div[2]/p/text()').extract(),
            'url': response.request.url
        }

