import scrapy

class QuoteSpider(scrapy.Spider):
    name='quotes'
    start_urls=[
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.css('title::text').extract()
        #Using xpath
        #response.xpath("//title/text()").extract()
        heading = response.css("span.text::text").extract() #To extract title from class,<span class="text" itemprop="text">“Imperfection is beauty, madness is ge

        '''
        <small class="author" itemprop="author">Albert Einstein</small>'''
        author = response.css('.author::text').extract()
        #author = response.css('.author::text')[1].extract() to get one author

        '''Using xpath'''
        #author=response.xpath("//span[@class='text]/text().extract()")
        """
        <a href="/page/2/">Next <span aria-hidden="true">→</span></a>
        """
        lnk=response.css("li.next a").xpath("@href").extract()

        """To select all anchor tag"""
        #lnk=response.css("a").xpath("@href").extract()

        yield{'titletext': title, 'heading':heading, 'author':author, "link": lnk}