import scrapy


class NinthSpider(scrapy.Spider):
    name = 'burgemeester_zorgplein'

    start_urls = [
        'https://www.zorgpleinnoord.nl/vacatures/vacature'
    ]

    def parse(self, response):
        urls = response.xpath('//div/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        #follow pagination link
        next_page = response.xpath('//ul[@class="pagination"]/li/a/@href').extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@class="col-12 col-md-8 col-lg-9 mb-3 vacancy-content"]/p/text()').extract(),
            'url': response.request.url
        }

