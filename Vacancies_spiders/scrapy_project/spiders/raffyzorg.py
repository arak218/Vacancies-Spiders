import scrapy


class ThirtyNinthSpider(scrapy.Spider):
    name = 'raffyzorg'

    start_urls = ['https://www.raffyzorg.nl/werken-en-leren/vacatures/']

    def parse(self, response):
        urls = response.xpath('//ul[@class="level-02"]/li/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h2/text()').extract(),
            'text': response.xpath('//*[@id="col-center-subs"]/div[1]/p/text()').extract(),
            'url': response.request.url
        }





