import scrapy
from bilirank.items import BilirankItem

import datetime
import json

class BiliSpider(scrapy.Spider):
    name = 'bili'
    start_urls = ['https://www.bilibili.com/ranking/all/0/0/1',
    'https://www.bilibili.com/ranking/all/1/0/1',
    'https://www.bilibili.com/ranking/all/168/0/1',
    'https://www.bilibili.com/ranking/all/3/0/1',
    'https://www.bilibili.com/ranking/all/129/0/1',
    'https://www.bilibili.com/ranking/all/4/0/1',
    'https://www.bilibili.com/ranking/all/36/0/1',
    'https://www.bilibili.com/ranking/all/188/0/1',
    'https://www.bilibili.com/ranking/all/160/0/1',
    'https://www.bilibili.com/ranking/all/119/0/1',
    'https://www.bilibili.com/ranking/all/155/0/1',
    'https://www.bilibili.com/ranking/all/5/0/1',
    'https://www.bilibili.com/ranking/all/181/0/1',
    'https://www.bilibili.com/ranking/origin/0/0/1',
    'https://www.bilibili.com/ranking/origin/1/0/1',
    'https://www.bilibili.com/ranking/origin/168/0/1',
    'https://www.bilibili.com/ranking/origin/3/0/1',
    'https://www.bilibili.com/ranking/origin/129/0/1',
    'https://www.bilibili.com/ranking/origin/4/0/1',
    'https://www.bilibili.com/ranking/origin/36/0/1',
    'https://www.bilibili.com/ranking/origin/188/0/1',
    'https://www.bilibili.com/ranking/origin/160/0/1',
    'https://www.bilibili.com/ranking/origin/119/0/1',
    'https://www.bilibili.com/ranking/origin/155/0/1',
    'https://www.bilibili.com/ranking/origin/5/0/1',
    'https://www.bilibili.com/ranking/origin/181/0/1']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)
    
    def parse(self, response):
        
        for i in range(1,101):
            item = BilirankItem()
            item['rank'] = response.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li[%d]/div[1]/text()' % i).extract_first()
            item['points'] = response.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li[%d]/div[2]/div[2]/div[2]/div/text()' % i).extract_first()
            item['video_url'] = response.xpath('//*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li[%d]/div[2]/div[2]/a/@href' % i).extract_first()
            item['av'] = item['video_url'].strip('https://www.bilibili.com/video/')
            item['time'] = str(datetime.datetime.now())
            rank_list = {'all/0/0/1':'全站','all/1/0/1':'动画','all/168/0/1':'国创相关','all/3/0/1':'音乐','all/129/0/1':'舞蹈',
                'all/4/0/1':'游戏','all/36/0/1':'科技','all/188/0/1':'数码','all/160/0/1':'生活','all/119/0/1':'鬼畜',
                'all/155/0/1':'时尚','all/5/0/1':'娱乐','all/181/0/1':'影视','origin/0/0/1':'全站原创','origin/1/0/1':'动画原创','origin/168/0/1':'国创相关原创','origin/3/0/1':'音乐原创','origin/129/0/1':'舞蹈原创',
                'origin/4/0/1':'游戏原创','origin/36/0/1':'科技原创','origin/188/0/1':'数码原创','origin/160/0/1':'生活原创','origin/119/0/1':'鬼畜原创',
                'origin/155/0/1':'时尚原创','origin/5/0/1':'娱乐原创','origin/181/0/1':'影视原创'}
            for (k,v) in rank_list.items():
                if(k in response.url):
                    item['rank_name'] = v
            yield scrapy.Request(item['video_url'],meta = {'item':item},callback=self.vedio_parse,dont_filter=True)

        

    def vedio_parse(self,response):
        item =response.meta['item']
        item['title'] = response.xpath('//*[@id="viewbox_report"]/h1/span/text()').extract_first()
        item['up'] = response.xpath('//*[@id="v_upinfo"]/div[2]/div[1]/a[1]/text()').extract_first()
        item['fans'] = response.xpath('//*[@id="v_upinfo"]/div[3]/div/span/span/text()').extract_first()
        item['contribute_time'] = response.xpath('//*[@id="viewbox_report"]/div[1]/span[2]/text()').extract_first()
        item['fenqu'] = response.xpath('//*[@id="viewbox_report"]/div[1]/span[1]/a[1]/text()').extract_first()
        item['bankuai'] = response.xpath('//*[@id="viewbox_report"]/div[1]/span[1]/a[2]/text()').extract_first()

        av = item['av'].strip('av')
        next_url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={}'.format(av)
        yield scrapy.Request(next_url,meta = {'item':item},callback=self.json_parse,dont_filter=True)

    
    def json_parse(self,response):
        item =response.meta['item']
        data = json.loads(response.text)['data']
        item['view'] = data['view']
        item['danmaku'] = data['danmaku']
        item['like'] = data['like'] 
        item['coin']  = data['coin']
        item['favorite'] = data['favorite']
        item['share'] = data['share']
        item['reply']  = data['reply']
        yield item
        
 