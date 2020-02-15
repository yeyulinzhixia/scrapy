import scrapy
from scrapy.spiders import Spider  
from scrapy.selector import Selector  
from sina_trip.items import SinaTripItem  
# 创建爬虫，用于爬取网页中的图片
class sinaTripSpider(Spider):  
    name = "sinaTripSpider"    # 爬虫的名称 
    start_urls = ["http://travel.sina.com.cn/"]  #需要爬取的网址 
    def parse(self, response):   #parse function
        item = SinaTripItem() # 创建字段实例
        sel = Selector(response) # 创建网页选择器，用于选取网页中的元素
        sites = sel.xpath("//img/@src").extract()   # 提取网页中所有图片的网址
        for site in sites: 
            item['url'] = ['http:'+site] # 视爬取的图片网址决定是否加'http'
            yield item