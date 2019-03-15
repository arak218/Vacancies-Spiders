import scrapy


class TenthSpider(scrapy.Spider):
    name = 'buurtzorgt'

    start_urls = ['https://www.buurtzorgt.nl/vacatures']

    def parse(self, response):
        urls = response.xpath('//div[@class="summary-title"]/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@class="sqs-block-content"]/p/text()').extract(),
            'url': response.request.url
        }
