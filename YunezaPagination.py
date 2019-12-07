# -*- coding: utf-8 -*-
import scrapy


class YunezapaginationSpider(scrapy.Spider):
    name = 'YunezaPagination' #Name of the file
    allowed_domains = ['www.moviefone.com'] #Domain of the webpage
    start_urls = ['http://www.moviefone.com/movies/']  #Exact url of the webpage

    def parse(self, response):
        for movies in response.css('li.movie-wrapper'):
            element={'Movie Title':movies.css('a.movie-title::text').extract_first(),
                     'Movie Availability':movies.css('span.available-text::text').extract_first(),
                     'Movie Link':movies.css('a.movie-poster-link::attr(href)').extract_first(),
                     'Movie Poster':movies.css('img.movie-poster.lazy::attr(src)').extract_first()
            }

        yield element

        UrlNextPage=response.css('a.next-button::attr(href)').extract_first() #refer to econd page and so on
        if(UrlNextPage):
            Next = response.urljoin(UrlNextPage)
            yield scrapy.Request(url=Next, callback=self.parse)
