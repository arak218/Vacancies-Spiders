import scrapy


class FiftiethSpider(scrapy.Spider):
    name = 'zorgcirkel'

    start_urls = ['https://zorgcirkel.nl/werken-bij/vacatures/']

    def parse(self, response):
        urls = response.xpath('//ul[@class="vacancyList"]/li/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@class="vacancy-contentSection"]/ul/li/text()').extract(),
            'url': response.request.url
        }




