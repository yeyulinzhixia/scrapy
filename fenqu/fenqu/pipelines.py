# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo 
from fenqu.utils import  logger

myclient=pymongo.MongoClient(host='127.0.0.1',port=27017)   #指定主机和端口号创建客户端
mydb=myclient['spider']#数据库使用
mycol=mydb['bili']#表（集合）使用
class FenquPipeline(object):  
    def process_item(self, item, spider):
        data = dict(item)
        if(data['biaoti'] != None):
            x = mycol.find_one({'av':data['av']})
            if (x == None):
            
                mycol.insert_one(data)
