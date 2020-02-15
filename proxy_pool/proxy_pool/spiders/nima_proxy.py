# -*- coding: utf-8 -*-
import scrapy

import datetime
import re
from proxy_pool.items import ProxyPoolItem

class NimaProxySpider(scrapy.Spider):
    name = 'nima_proxy'

    allowed_domains=['nimadaili.com']
    start_urls = ['http://www.nimadaili.com/gaoni/%d/' % i  for i  in range(1,101)]
    
    def parse(self, response):
        for i  in range(1,51):
            item = ProxyPoolItem()
            x = response.xpath('/html/body/div[1]/div[1]/div/table/tbody/tr[%d]/td[1]' % i).re(r'(\d+.\d+.\d+.\d+):(\d+)')
            print(x)
            print('===========')
            item['ip'] = x[0]
            item['port'] = x[1]
            item['schema'] = 'http'
            item['created_time'] = str(datetime.datetime.now())
            item['original'] = '尼玛代理'
            yield item
         

