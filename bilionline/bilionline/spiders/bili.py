# -*- coding: utf-8 -*-
import scrapy
import json
import pymongo
import datetime

myclient=pymongo.MongoClient(host='127.0.0.1',port=27017)   #指定主机和端口号创建客户端
mydb=myclient['spider']#数据库使用
mycol=mydb['online']#表（集合）使用

class BiliSpider(scrapy.Spider):
    name = 'bili'
    start_urls = ['https://api.bilibili.com/x/web-interface/online']

    def parse(self, response):
        item = {}
        item['web_online'] = json.loads(response.text)['data']['web_online']
        item['play_online'] = json.loads(response.text)['data']['play_online']
        item['time'] = str(datetime.datetime.now())
        print(item)
        mycol.insert_one(item)
