import scrapy


class SeventeenthSpider(scrapy.Spider):
    name = "empathon"

    start_urls = ['https://www.empathon.nl/index.php?page=Vacatures']


    def parse(self, response):
        yield {
            'title': response.xpath('//div[4]/p/u/text()').extract(),
            'text': response.xpath('//div/p/text()').extract(),
            'url': response.request.url
        }

