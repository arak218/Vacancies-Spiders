import scrapy


class TwentyFifthSpider(scrapy.Spider):
    name = 'kalorama'

    start_urls = ['https://www.werkenbijkalorama.nl/actuele-vacatures']

    def parse(self, response):
        urls = response.xpath('//td[1]/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract(),
            'text': response.xpath('//div[@class="inner"]/p/text()').extract(),
            'url': response.request.url
        }

