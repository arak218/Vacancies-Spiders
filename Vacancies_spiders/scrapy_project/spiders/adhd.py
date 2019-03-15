import scrapy

# Scrapy maak de class voor de Zorgned_ProjectSpider
class SecondSpider(scrapy.Spider):
    # De naam van de spider
    name = 'adhd'

    # De start Domeinen, websites
    start_urls = ['https://adhdcentraal.nl/over-ons/vacatures/']

    # Methode voor het inlezen van de website data
    def parse(self, response):

        # Neem uit 'vac' data en bewaar deze in de volgende items
        for vac in response.xpath('//div[@class="vacatures"]'):
            # Een lijst van de gevonden items
            item = {
                'title': response.xpath('//h1/text()').extract(),
                'text': vac.xpath('//ul/li/span/text()').extract(),
                'url': response.request.url
            }
            # Geef alle gevonden items terug
            yield item







