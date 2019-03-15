import scrapy


class ThirtyThirdSpider(scrapy.Spider):
    name = "meander"

    start_urls = ['https://www.meandermc.nl/patientenportaal/werken-en-leren/Vacatures/Vacature%20overzicht']

    def parse(self, response):
        yield {
            'title': response.xpath('//h2/text()').extract(),
            #'text': response.xpath('//tr[1]/td[1]/div/div/text()').extract(),
            'url': response.request.url
        }





