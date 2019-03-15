import scrapy


class FortyFourthSpider(scrapy.Spider):
    name = "sutfene"

    start_urls = ['https://www.sutfene.nl/werken-bij-sutfene/vacatures']


    def parse(self, response):
        yield {
            #'title': response.xpath('//header/h1/text()').extract_first(),
            'text': response.xpath('//div[@itemprop="articleBody"]/p/text()').extract(),
            'url': response.request.url
        }










