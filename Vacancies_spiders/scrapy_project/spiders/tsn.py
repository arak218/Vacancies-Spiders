import scrapy


class FortySixthSpider(scrapy.Spider):
    name = 'tsn'

    start_urls = ['https://werkenbijtsn.nl/vacatures']

    def parse(self, response):
        urls = response.xpath('//div[5]/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        #follow pagination link
        next_page = response.xpath('//*[@id="js__load_vacatures"]/div[3]/div/ul/li/a/@href').extract_first()

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)


    def parse_details(self, response):
        yield {
            'title': response.xpath('.//h1/text()').extract_first(),
            'text': response.xpath('.//*[@id="main"]/article/div[1]/div/div[1]/div/p/text()').extract(),
            'url': response.request.url
        }






