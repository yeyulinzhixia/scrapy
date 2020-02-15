# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FenquItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fenqu = scrapy.Field()
    bankuai = scrapy.Field()
    av = scrapy.Field()
    biaoti = scrapy.Field()
    shijian = scrapy.Field()
  
