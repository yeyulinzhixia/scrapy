# -*- coding: utf-8 -*-
import scrapy
import json


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['www.httpbin.org/ip']
    start_urls = ['http://www.httpbin.org/ip']

    def parse(self, response):
        ip = json.loads(response.text)['origin']
        print(ip)
        url = 'http://www.httpbin.org/ip'
        yield scrapy.Request(url=url,meta={'proxy':'http://183.157.57.150:8118'},callback=self.new_parse,dont_filter=True)
    
    def new_parse(self,response):
        ip = json.loads(response.text)['origin']
        print(ip)
