# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    id = scrapy.Field()
    name = scrapy.Field()
    followings = scrapy.Field()
    followers = scrapy.Field()
    words = scrapy.Field()
    likes = scrapy.Field()
    articles = scrapy.Field()
