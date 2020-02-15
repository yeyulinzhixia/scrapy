# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo 


myclient=pymongo.MongoClient(host='127.0.0.1',port=27017)   #指定主机和端口号创建客户端
mydb=myclient['spider']#数据库使用
mycol=mydb['rank_temp']#表（集合）使用

class BilirankPipeline(object):
    def process_item(self, item, spider):
        data = dict(item)
        print(data)
        mycol.insert_one(data)
