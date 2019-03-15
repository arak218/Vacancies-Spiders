import scrapy


class FiftySecondSpider(scrapy.Spider):
    name = 'zorgstroom'

    start_urls = ['https://werkenbijzorgstroom.nl/vacatures']

    def parse(self, response):
        urls = response.xpath('//div/table/tbody/tr/td/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//p/text()').extract(),
            'url': response.request.url
        }
