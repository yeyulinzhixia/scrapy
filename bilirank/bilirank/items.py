# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilirankItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    family = scrapy.Field()
    rank = scrapy.Field()
    points = scrapy.Field()
    video_url = scrapy.Field()
    av = scrapy.Field()
    title = scrapy.Field()
    up = scrapy.Field()
    fans = scrapy.Field()
    contribute_time = scrapy.Field()
    fenqu= scrapy.Field()
    bankuai = scrapy.Field()
    view = scrapy.Field()
    danmaku = scrapy.Field()
    like= scrapy.Field()
    coin = scrapy.Field()
    favorite = scrapy.Field()
    share = scrapy.Field()
    reply = scrapy.Field()
    time = scrapy.Field()
    rank_name = scrapy.Field()