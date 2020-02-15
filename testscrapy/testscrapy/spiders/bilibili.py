import scrapy


class BilibiliSpider(scrapy.Spider):
    name = 'bili'
    start_urls = ['http://www.bilibili.com/video/av86755171']
    


    def parse(self, response):
        title = response.xpath('//*[@id="viewbox_report"]/h1/span/text()').extract_first()
        print(title)
        url = 'http://www.bilibili.com/video/av86755173'
        yield scrapy.Request(url=url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'},
        meta = {'https_proxy':'https://114.99.28.191:37002'} ,callback = self.parse)