import scrapy

class NinteenthSpider(scrapy.Spider):
    name = 'ggz_centraal'

    start_urls = ['https://www.werkenbijggzcentraal.nl/1412/alle-vacatures.html']

    def parse(self, response):
        urls = response.xpath('//div[@class="link-container"]/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)



    def parse_details(self, response):
        yield {
            'functietitel': response.xpath('//h1/text()').extract(),
            'tekst': response.xpath('//div[@class="vacanciesIntro"]/p/text()').extract(),
            'url': response.request.url
        }

