# -*- coding: utf-8 -*-
import scrapy



class DoubanMovieTop250Spider(scrapy.Spider):
    name = 'douban_movie_top250'
    allowed_domains = ['https://movie.douban.com/top250']
    start_urls = ['http://https://movie.douban.com/top250/']

    def parse(self, response):
        item = Dou
