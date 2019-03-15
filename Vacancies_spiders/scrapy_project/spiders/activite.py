import scrapy


class FirstSpider(scrapy.Spider):
    name = 'activite'

    start_urls = ['https://www.activite.nl/home/werken-bij/vacatures']

    def parse(self, response):
        urls = response.xpath('//*[@id="subnavigation"]/ul/li/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


        #follow pagination link
        next_page = response.xpath('//*[@id="main"]/div/div[2]/div[3]/div/p[2]/a[2]').extract_first()

        if next_page is not None:
           next_page_link = response.urljoin(next_page)
           yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@class="content"]/p/text()').extract(),
            'url': response.request.url
        }

