# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PixivItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pic_url = scrapy.Field()
    pic = scrapy.Field()
    name = scrapy.Field() 
    author = scrapy.Field()
    time = scrapy.Field() 
    pass
