import scrapy


class TwentySeventhSpider(scrapy.Spider):
    name = 'laprovidence'

    start_urls = ['https://www.laprovidence.nl/vacatures']

    def parse(self, response):
        urls = response.xpath('//*[@id="divJobs"]/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//div[@class="inner content"]/p/text()').extract(),
            'url': response.request.url
        }
