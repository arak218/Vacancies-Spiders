import scrapy


class TwentyNinthSpider(scrapy.Spider):
    name = 'liemerije'

    start_urls = ['https://www.liemerije.nl/werken-bij/vacatures']

    def parse(self, response):
        urls = response.xpath('//*[@id="parent-fieldname-text"]/ul/li/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@id="parent-fieldname-text"]/p/text()').extract(),
            'url': response.request.url
        }
