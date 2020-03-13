import scrapy

class quotes (scrapy.Spider):
    name        = 'quotes'
    start_urls  = ['https://www.forex.pk/open_market_rates.asp', ] 

    def parse(self, response):
        currency = response.css('table tr td table tr td div')[2].css('table tr td')[1].css  ('table tr td::text')[-15:].extract()

        country = response.css('table tr td table tr td div')[2].css('table tr td')[1].css('table tr td a::text')[-5:].extract()
        
        i = 0
        j = 3
        for x in country:
            yield {x : currency[i:j]}
            i = j
            j += 3