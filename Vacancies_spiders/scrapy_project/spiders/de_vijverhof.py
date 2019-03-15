import scrapy


class FourteenthSpider(scrapy.Spider):
    name = "vijverhof"

    start_urls = ['https://www.werkenindevijverhof.nl/vacatures']

    def parse(self, response):
        urls = response.xpath('//article/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//section[@class="content-block"]/p/text()').extract(),
            'url': response.request.url
        }
