import scrapy


class TwentyFourthSpider(scrapy.Spider):
    name = 'isala'

    start_urls = ['https://isalawerkt.nl/vacature-overzicht']

    def parse(self, response):
        urls = response.xpath('//section/div/p/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div/p/text()').extract(),
            'url': response.request.url
        }






