
import scrapy
from selenium import webdriver
import time
class MycollectionSpider(scrapy.Spider):
    name = "collection"      
    start_urls = ['https://www.pixiv.net/users/21405138/bookmarks/artworks']#收藏页
    page = 1

    browser = webdriver.Chrome(executable_path=r'C:\Users\王祥霖\AppData\Local\Programs\Python\Python37\Lib\site-packages\chromedriver')
    browser.get('https://accounts.pixiv.net/login')
    browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[1]/input').send_keys('479892367@qq.com')
    browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[2]/input').send_keys('13678475618zl')
    browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/button').click()
    time.sleep(10)

    def parse(self, response): 
        self.page = self.page + 1
        list = response.xpath('//*[@id="root"]/div[2]/div/div[2]/div[1]/section/ul/text()')
        print(list)
        if(response.xpath('//*[@id="root"]/div[2]/div/div[2]/div[2]/a[7]/text()').extract_first() != None):
            next_url = 'https://www.pixiv.net/users/21405138/bookmarks/artworks' + '?p=%d' % self.page
            yield scrapy.Request(next_url,callback=self.parse)

    def parse_page(self,response):
        pass