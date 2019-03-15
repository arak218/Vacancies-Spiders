import scrapy


class ThirtyFirstSpider(scrapy.Spider):
    name = 'maasduinen'

    start_urls = ['https://www.maasduinenzorg.nl/werken-en-leren/nieuwe-medewerkers/']

    def parse(self, response):
        yield {
            'title': response.xpath('//div[@class="href-list-component"]/div/a/text()').extract(),
            #'text': response.xpath('//div/span/text()').extract(),
            #'url': response.request.url
        }
