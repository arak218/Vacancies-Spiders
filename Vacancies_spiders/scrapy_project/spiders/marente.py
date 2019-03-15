import scrapy


class ThirtySecondSpider(scrapy.Spider):
    name = 'marente'

    start_urls = ['https://werkenbijmarente.nl/vacatures']

    def parse(self, response):
        urls = response.xpath('//*[@id="main-container"]/ul/li/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@class="content"]/ul/li/text()').extract(),
            'url': response.request.url
        }

