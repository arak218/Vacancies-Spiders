import scrapy


class SixthSpider(scrapy.Spider):
    name = 'aza_bijtzorg'

    start_urls = ['https://werkenbijtzorg.nl/vacatures/']

    def parse(self, response):
        urls = response.xpath('//div[1]/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@class="post-content post-content--vacancy"]/p/text()').extract(),
            'url': response.request.url
        }

