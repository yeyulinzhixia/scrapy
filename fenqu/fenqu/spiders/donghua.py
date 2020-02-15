'''
动画分区
MAD·AMV https://www.bilibili.com/v/douga/mad/
MMD·3D https://www.bilibili.com/v/douga/mmd/
短片·手书·配音 https://www.bilibili.com/v/douga/voice/
特摄 https://www.bilibili.com/v/douga/tokusatsu/
综合 https://www.bilibili.com/v/douga/other/

翻页 #/all/default/0/%d/
列表 //*[@id="videolist_box"]/div[2]/ul
每个视频的URL /li[1]/div[2]/a::attr(href)

'''

import scrapy
from fenqu.items import FenquItem


import logging
import json

class donghuaSpider(scrapy.Spider):
    name = 'bilibili'
    av = 87006523 #初始av号
    start_urls = ['http://httpbin.org/ip']
    

    def parse(self, response):
        ip = json.loads(response.text)['origin']
        print(ip)
        url = 'http://httpbin.org/ip'
        yield scrapy.Request(url=url,callback=self.new_parse)
        # item = FenquItem()
        # item['biaoti'] = response.xpath('//*[@id="viewbox_report"]/h1/span/text()').extract_first()
        # item['av'] = self.av
        # item['fenqu'] = response.xpath('//*[@id="viewbox_report"]/div[1]/span[1]/a[1]/text()').extract_first()
        # item['bankuai'] = response.xpath('//*[@id="viewbox_report"]/div[1]/span[1]/a[2]/text()').extract_first()
        # item['shijian'] = response.xpath('//*[@id="viewbox_report"]/div[1]/span[2]/text()').extract_first()
        # logging.info(item)
        # yield item
        # self.av = self.av + 1
        # next_url = 'https://www.bilibili.com/video/av%d' % self.av
        # yield scrapy.Request(next_url,callback=self.parse)

    def new_parse(self,response):
        ip = json.loads(response.text)['origin']
        print(ip)