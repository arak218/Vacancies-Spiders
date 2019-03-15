import scrapy


class ThirtyFourthSpider(scrapy.Spider):
    name = 'mmc'

    start_urls = ['https://www.mmc.nl/werkenbijmmc/vacatures/']

    def parse(self, response):
        urls = response.xpath('//ul[@class="vacancy-list list-unstyled"]/li/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        #follow pagination link
        #next_page = response.xpath('//ul[@class="list-inline pagination"]/li/a/@href').extract_first()

        #if next_page is not None:
         #   next_page_link = response.urljoin(next_page)
          #  yield scrapy.Request(url=next_page_link, callback=self.parse)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@class="main-content"]/p/text()').extract(),
            'url': response.request.url
        }

