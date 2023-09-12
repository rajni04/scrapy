import scrapy
from ..items import QuotetItem


class QuoteSpider(scrapy.Spider):
    name='quote'
    start_urls=[
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        items=QuotetItem

        all_div_quotes=response.css('div.quotes')
        for quotes in all_div_quotes:
        #title = all_div_quotes.css('title::text').extract()


        #yield{'titletext': title}


        # all_div_quotes=response.css('div.quotes')
        # for quotes in all_div_quotes:
            title=quotes.css('span.text::text').extract()
            print("tittttttttt",title)
            author=quotes.css('.author::text').extract()
            tag=quotes.css('.tag::text').extract()
            items['title']=title
            items['author']=author
            items['tags']=tag

            # yield{
            #     'title':title,
            #     'author':author,
            #    'tag':tag
            # }
            yield items

        """<li class="next">
                <a href="/page/2/">Next <span aria-hidden="true">→</span></a>
            </li>"""
        next_page=response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callable=self.parse)
