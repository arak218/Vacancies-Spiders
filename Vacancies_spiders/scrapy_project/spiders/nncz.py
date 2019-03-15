import scrapy


class FiftyThirdSpider(scrapy.Spider):
    name = 'nncz'

    start_urls = ['https://nncz.nl/werken-en-leren']

    def parse(self, response):
        urls = response.xpath('//li[6]/ul/li/ul/li/a/@href').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


    def parse_details(self, response):
        yield {
            'title': response.xpath('//h1/text()').extract_first(),
            'text': response.xpath('//p/text()').extract(),
            'url': response.request.url
        }


class FiftyFourthSpider(object):
    pass