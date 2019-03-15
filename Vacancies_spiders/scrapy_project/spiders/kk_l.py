import scrapy


class TwentySixthSpider(scrapy.Spider):
    name = 'kk_l'

    start_urls = ['https://kk-l.nl/over-ons']

    def parse(self, response):
        yield {
            'title': response.xpath('//*[@id="vacatures"]/div/div/div/ul[1]/li/text()').extract(),
            'text': response.xpath('//p[4]/text()').extract(),
            'url': response.request.url
        }

