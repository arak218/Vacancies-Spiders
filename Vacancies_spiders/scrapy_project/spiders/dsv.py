import scrapy


class FifteenthSpider(scrapy.Spider):
    name = "dsv"

    start_urls = ['http://www.dsv-verzorgdleven.nl/werken-bij/vacatures/']


    def parse(self, response):
           yield {
             'title': response.xpath('//h4/text()').extract(),
             'text': response.xpath('//div[@class="card news"]/p/text()').extract(),
             'url': response.request.url
           }






