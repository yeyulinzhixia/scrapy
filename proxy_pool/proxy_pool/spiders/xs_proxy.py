# -*- coding: utf-8 -*-
import scrapy
import datetime
import re
from proxy_pool.items import ProxyPoolItem
class XsProxySpider(scrapy.Spider):
    name = 'xs_proxy'
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    # start_urls = ['http://www.xsdaili.com/dayProxy/%d/%d/%d.html/' % (year,month,day)]
    start_urls = ['http://www.xsdaili.com/index.php?s=/index/index.html']

    def parse(self, response):
        for i in range(1,16):
            url = response.xpath('/html/body/div[5]/div/div[2]/div/div/div/div[2]/div/div[2]/div[%d]/div[1]/a/@href' % i).extract_first()
            url = 'http://www.xsdaili.com/' + url
            yield scrapy.Request(url,callback=self.page_parse)
        
    def page_parse(self,response):
        for i in range(1,101):
            one = response.xpath('/html/body/div[5]/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/text()[%d]' % i).re(r'(\d+.\d+.\d+.\d+):(\d+)@(\w+)#\[(\D+)\]')
            if( one[3] == '高匿名'):
                item = ProxyPoolItem()
                item['schema'] = one[2]
                item['schema'] = item['schema'].lower()
                item['ip'] = one[0]
                item['port'] = one[1]
                item['original'] = '小舒代理'
                item['created_time'] = str(datetime.datetime.now())
                print(item)
                yield item