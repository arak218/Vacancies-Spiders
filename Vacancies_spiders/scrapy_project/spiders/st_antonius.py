import scrapy


class FortySecondSpider(scrapy.Spider):
    name = 'st_antonius'

    start_urls = ['https://werkenbijantonius.nl/vacatures/']

    def parse(self, response):
        urls = response.xpath('//footer[@class="entry-read-more"]/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

        next_page = response.xpath('//div[@class="load"]/a/@href').extract()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse_details(self, response):
        yield {
            'title': response.xpath('//h2/text()').extract_first(),
            'text': response.xpath('//p/text()').extract(),
            'url': response.request.url
        }
