import scrapy


class TwentiethSpider(scrapy.Spider):
    name = 'ggz_friesland'

    start_urls = ['https://www.ggzfriesland.nl/vacatures',
                  'https://www.ggzfriesland.nl/vacatures?p=2']

    #def parse(self, response):
     #   urls = response.xpath('//article/ul/li/a').extract()
      #  for url in urls:
       #     url = response.urljoin(url)
        #    yield scrapy.Request(url=url, callback=self.parse_details)


        #follow pagination link
       # next_page = response.xpath('//article/nav/ul/li[3]/a').extract_first()

        #if next_page is not None:
         #  next_page_link = response.urljoin(next_page)
          # yield scrapy.Request(url=next_page_link, callback=self.parse)


    def parse(self, response):
        yield {
            'title': response.xpath('//h2/text()').extract(),
            'text': response.xpath('//article/ul/li/a/div/p/text()').extract(),
            'url': response.request.url
        }

