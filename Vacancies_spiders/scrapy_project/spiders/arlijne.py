import scrapy


class FifthSpider(scrapy.Spider):
    name = 'arlijne'

    start_urls = ['https://alrijne.onlinevacatures.nl/nl/Vacature/']

    def parse(self, response):
        urls = response.xpath('//h6/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        #follow pagination link
        next_page = response.xpath('//div[@class="pagination"]/a/@href').extract_first()

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//header/h1/text()').extract_first(),
            'text': response.xpath('//div[@id="boxFull"]/p/text()').extract(),
            'url': response.request.url
        }
