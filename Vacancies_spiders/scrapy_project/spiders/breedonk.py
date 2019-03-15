import scrapy


class EighthSpider(scrapy.Spider):
    name = 'breedonk'

    start_urls = ['http://www.breedonk.nl/4783/Vacatures.html?Locatie=2&page=0']

    def parse(self, response):
        urls = response.xpath('//h4/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        #follow pagination link
        next_page = response.xpath('//div[@class="pages"]/a/@href').extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse_details(self, response):
        yield {
            'title': response.xpath('//h4/text()').extract_first(),
            'text': response.xpath('//div[@class="text"]/p/text()').extract(),
            'url': response.request.url
        }





