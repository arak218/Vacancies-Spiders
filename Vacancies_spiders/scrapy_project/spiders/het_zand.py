import scrapy


class TwentyThirdSpider(scrapy.Spider):
    name = 'het_zand'

    start_urls = ['https://hetzand.nl/vacatures']

    def parse(self, response):
        urls = response.xpath('//h5/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//div[@class="pagecontent"]/h1/text()').extract(),
            'text': response.xpath('//div[@class="description"]/p/text()').extract(),
            'url': response.request.url
        }
















