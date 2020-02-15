# -*- coding: utf-8 -*-
import re
import datetime
import scrapy
from proxy_pool.utils import strip, logger
from proxy_pool.items import ProxyPoolItem
 
 
class KuaiProxySpider(scrapy.Spider):
    name = 'kuai_proxy'
    allowed_domains = ['kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']
 
    def parse(self, response):
        logger.info('正在爬取：< ' + response.request.url + ' >')
        tr_list = response.css("div#list>table>tbody tr")
        for tr in tr_list:
            ip = tr.css("td[data-title='IP']::text").get()
            port = tr.css("td[data-title='PORT']::text").get()
            schema = tr.css("td[data-title='类型']::text").get()
            if schema.lower() == "http" or schema.lower() == "https":
                item = ProxyPoolItem()
                item['schema'] = strip(schema).lower()
                item['ip'] = strip(ip)
                item['port'] = strip(port)
                item['original'] = '快代理'
                item['created_time'] = str(datetime.datetime.now())
                if item._check_format():
                    yield item

        #翻页动作
        next_page = response.xpath("//a[@class='active']/../following-sibling::li/a/@href").get()
        if next_page is not None:
            next_url = 'https://www.kuaidaili.com' + next_page
            yield scrapy.Request(next_url)
