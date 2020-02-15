import bs4
import scrapy
import pymongo
from bs4 import BeautifulSoup
from pymongo import MongoClient

class UniversityRankSpider(scrapy.Spider):
    name = "university-rank"  #name of spider
    start_urls = ['http://gaokao.xdf.cn/201702/10612921.html']  #url of website

    def parse(self, response):  #parse function
        content = response.xpath("//tbody").extract()[0]
        soup = BeautifulSoup(content, "lxml")  #use BeautifulSoup      
        table = soup.find('tbody')
        count = 0 
        lst = []   # list to save data from the table
        for tr in table.children:  #BeautifulSoup grammmer
            if isinstance(tr, bs4.element.Tag):
                td = tr('td')
                if count >= 2:  #ingore the first line
                    lst.append([td[i]('p')[0].string.replace('\n','').replace('\t','') for i in range(8)])
                count += 1

        conn = MongoClient('mongodb://localhost:27017/')  #connect mongodb
        db = conn.testdb

        for item in lst:  #insert data into university_rank table
            db.university_rank.insert([
            {'rank':'%s'%item[0], 'university':'%s'%item[1], 'address':'%s'%item[2], 'local_rank':'%s'%item[3],
                 'total grade':'%s'%item[4], 'type':'%s'%item[5], 'star rank':'%s'%item[6], 'class':'%s'%item[7]},
        ]) 

        print ('Successfully downloading data from website, and write it to mongodb database!')
