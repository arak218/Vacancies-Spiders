import scrapy

class FortiethSpider(scrapy.Spider):
    name = 'sensire'

    start_urls = ['https://www.werkenbijsensire.nl/vacatures/']

    def parse(self, response):
        urls = response.xpath('//*[@id="nieuwe-vacatures-blokken-container"]/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)



    def parse_details(self, response):
        yield {
            'functietitel': response.xpath('//h1/text()').extract(),
            'tekst': response.xpath('//div[@id="watgajedoen-wiebenjij"]/text()').extract(),
            'url': response.request.url
        }

