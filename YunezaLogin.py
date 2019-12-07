# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import FormRequest


class YunezaLoginSpider(Spider):
    name = 'YunezaLogin' #Name of the file
    allowed_domains = ['quotes.toscrape.com'] #Domain of the webpage
    start_urls = ('http://quotes.toscrape.com/login/') #The url where the login is located

    def parse(self, response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first() #The given token of the user
        return FormRequest.from_response(response,
                                         formdata={'csrf_token': token, #The token of the user
                                                   'password': 'foobar', #The password of the user
                                                   'username': 'foobar'}, #The username of the user
                                         callback=self.scrape_pages)

    def scrape_pages(self, response): #scraping the contents of the whole page
        quotes=response.css('span.text::text').extract() 
        author=response.css('small.author::text').extract()
        tags=response.css('div.quote>a.tag::text').extract()
        
        for quote in zip(quotes,author,tags):
            item={
                'Quote Content':quote[0],
                'Author':quote[1],
                'Tags':quote[2]
            }
            yield item
        
