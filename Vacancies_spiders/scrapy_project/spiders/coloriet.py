import scrapy


class ThirteenthSpider(scrapy.Spider):
    name = 'coloriet'

    start_urls = ['https://www.coloriet.nl/werken-bij-coloriet/vacatures/']

    #def parse(self, response):
     #  urls = response.xpath('//div[3]/div[3]/div[1]/div/a/a/@href').extract()
      # for url in urls:
       #     url = response.urljoin(url)
        #    yield scrapy.Request(url=url, callback=self.parse_details)

    def parse(self, response):
            yield {
                'title': response.xpath('//div[@class="vacancyintro"]/h2/span/text()').extract(),
                'text': response.xpath('//div[@class="vacancyintro"]/div/text()').extract(),
                'url': response.request.url
            }


