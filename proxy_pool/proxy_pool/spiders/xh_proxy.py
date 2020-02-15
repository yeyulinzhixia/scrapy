# -*- coding: utf-8 -*-
import scrapy
import datetime
import re
from proxy_pool.items import ProxyPoolItem


class XhProxySpider(scrapy.Spider):
    name = 'xh_proxy'
    day = datetime.datetime.now().strftime("%Y/%m/%d/")
    time ='19'#设置具体时间
    start_urls = ['http://ip.ihuan.me/today/'+day+time+'.html?page=5crfe930']

    def parse(self, response):
        print(response.text)
        x = response.xpath('/html/body/meta"utf-8"/div[2]/div/div/p/text()[1]/text()').extract_first()
        print(x)
