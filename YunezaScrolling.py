# -*- coding: utf-8 -*-
import json
import scrapy


class YunezascrollingSpider(scrapy.Spider):
    name = 'YunezaScrolling' #Name of the file
    quotes_base_url = 'http://spidyquotes.herokuapp.com/api/quotes?page=%s' #Base url of the webpage that is about to be scraped
    start_urls = [quotes_base_url % 1] #The first page that is about to be scraped in the webpage
    download_delay = 1.5

    def parse(self, response):
        data = json.loads(response.body) 
        for item in data.get('quotes', []): #Extracting each data in the webpage
            yield {
                'Quote': item.get('text'), #Extracting each quote in the webpage
                'Author': item.get('author', {}).get('name'), #Extracting each author in the webpage
                'Tags': item.get('tags') #Extracting tags in the webpage
                }
            if data['has_next']: #Automatically scrolls the next data in the webpage 
                next_scrolling_page = data['page'] + 1
                yield scrapy.Request(self.quotes_base_url % next_scrolling_page)
                
        
