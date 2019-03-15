import scrapy


class ThirtySeventhSpider(scrapy.Spider):
    name = 'ouderenzorgzitinje'

    start_urls = ['https://ouderenzorgzitinje.nl/vacatures/']

    def parse(self, response):
        urls = response.xpath('//div[@class="vacature_item"]/a/@href').extract()
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
            'text': response.xpath('//*[@id="block-zpn-theme-content"]/div/div[2]/div[1]/p/text()').extract(),
            'url': response.request.url
        }

