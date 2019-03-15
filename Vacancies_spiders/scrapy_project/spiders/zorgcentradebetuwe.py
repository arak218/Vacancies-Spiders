import scrapy


class FortyNinthSpider(scrapy.Spider):
    name = 'zorgcentradebetuwe'

    start_urls = ['https://www.zorgcentradebetuwe.nl/werken-bij-ons/vacatures/alle-vacatures/']

    def parse(self, response):
        urls = response.xpath('//div[@class="vac-item"]/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h2/text()')[1].extract(),
            'text': response.xpath('//div/p/text()').extract(),
            'url': response.request.url
        }
