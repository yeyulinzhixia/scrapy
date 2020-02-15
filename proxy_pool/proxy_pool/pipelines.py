# -*- coding: utf-8 -*-
 
import json
import pymongo 
from proxy_pool.settings import PROXIES_UNCHECKED_LIST,PROXIES_UNCHECKED_SET
from proxy_pool.utils import  logger
import requests

 
myclient=pymongo.MongoClient(host='127.0.0.1',port=27017)   #指定主机和端口号创建客户端
mydb=myclient['spider']#数据库使用
mycol=mydb['proxy']#表（集合）使用
 
class ProxyPoolPipeline(object):
    
    
    # 将可用的IP代理添加到代理池队列
    def process_item(self, item, spider):
        # proxies = {}
        item = dict(item)
        # schema = item['schema']
        # schema = schema.lower()
        # proxy= schema + '://' + item['ip'] + ':' + item['port']
        # if(item['schema'] == 'http'):
        #     proxies['http'] = proxy
        # elif (item['schema']== 'https'):
        #     proxies['https'] = proxy
        # x = requests.get('https://www.baidu.com',proxies = proxies)
        # if(x.status_code == 200):
        #     data = mycol.find_one({'ip':item['ip']})
        #     if (data == None):
        #         logger.info('正在存入：< ' +str(item)+ ' >')           
        #         mycol.insert_one(item)
        #代理测试
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'}
        url = 'http://www.httpbin.org/ip'
        proxy = item['schema'] + '://' + item['ip'] + ':' + item['port']
        try:
            x = requests.get(url,headers=headers,proxies={item['schema']:proxy},timeout=10)
            flag = False
            if(x.status_code == 200):
                ip = json.loads(x.text)['origin']
                print("================%s=================" % ip)
                print("================%s=================" % item['ip'])
                if(ip == item['ip']):
                    flag = True
            if(flag):
                data = mycol.find_one({'ip':item['ip']})
                if (data == None):
                    logger.info('正在存入：< ' +str(item)+ ' >')           
                    mycol.insert_one(item)
        except:
            pass
        
        
 
    
    
