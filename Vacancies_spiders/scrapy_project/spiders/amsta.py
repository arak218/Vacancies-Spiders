import scrapy


class FourthSpider(scrapy.Spider):
    name = 'amsta'

    start_urls = ['https://www.amsta.nl/index.php/werken-bij-amsta/vacatures']

    def parse(self, response):
        urls = response.xpath('//div[@class="views-row"]/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        # follow pagination link
        next_page = response.xpath('//ul[@class="pager__items js-pager__items"]/li/a/@href').extract()

        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@class="page-content__padding"]/p/text()').extract(),
            'url': response.request.url
        }
