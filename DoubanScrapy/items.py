# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanscrapyItem(scrapy.Item):
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movieName = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    scoreNum = scrapy.Field()


