import scrapy

class FortyThirdSpider(scrapy.Spider):
    name = 'stichtingniko'

    start_urls = ['https://www.stichtingniko.com/over-ons/vacatures/']

    def parse(self, response):
        urls = response.xpath('//div[@class="content"]/div/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)



    def parse_details(self, response):
        yield {
            'functietitel': response.xpath('//h2/text()').extract_first(),
            'tekst': response.xpath('//ul/li/text()').extract(),
            'url': response.request.url
        }
