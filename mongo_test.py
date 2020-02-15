
from selenium import webdriver
import requests
import json
import time
# browser = webdriver.Chrome(executable_path=r'C:\Users\王祥霖\AppData\Local\Programs\Python\Python37\Lib\site-packages\chromedriver')

#第一次登陆

# browser.get('https://accounts.pixiv.net/login')
# browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[1]/input').send_keys('479892367@qq.com')
# browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/div[1]/div[2]/input').send_keys('13678475618zl')
# browser.find_element_by_xpath('//*[@id="LoginComponent"]/form/button').click()
# cookies = browser.get_cookies()
# print(cookies)
# jsonCookies = json.dumps(cookies)
# with open('../pixiv_cookies.json', 'w') 
# time.sleep(10)

# browser.get('https://www.pixiv.net/users/21405138/bookmarks/artworks')
# print(browser.page_source)

# 下一次登陆用cookies
# browser.get("https://www.pixiv.net/users/21405138/bookmarks/artworks")
# browser.delete_all_cookies
# with open("../pixiv_cookies.json", "r") as fp:
#     cookies = json.load(fp)
#     for cookie in cookies:
#        # 报expiry无效的错误
#         if "expiry" in cookie:
#             del cookie["expiry"]
#         browser.add_cookie(cookie)
# browser.get("https://www.pixiv.net/users/21405138/bookmarks/artworks")


#这个方法可以获取到图片
# import urllib
# headers = {
#             'referer': 'https://www.pixiv.net/artworks/72090962',
#             'origin': 'https://accounts.pixiv.net',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
#                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
#             "Accept-Language": "zh-CN,zh;q=0.9",
#             "Accept-Encoding": "",}
# request = urllib.request.Request(url='https://i.pximg.net/img-original/img/2018/12/13/10/27/25/72090962_p0.jpg', headers=headers)
# response = urllib.request.urlopen(request)
# with open('./haha.png','wb')as f:
#      f.write(response.read())

headers = {
            'referer': 'https://www.pixiv.net/artworks/72090962',
            'origin': 'https://accounts.pixiv.net',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Accept-Encoding": "",}
x = requests.get("https://i.pximg.net/img-original/img/2018/12/13/10/27/25/72090962_p0.jpg",headers=headers)
with open('./haha2.png','wb')as f:
    f.write(x.content)
# import requests
# from http.cookiejar import  CookieJar

# url = 'https://www.pixiv.net/users/21405138/bookmarks/artworks'
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
# rawcookies ='PHPSESSID=21405138_uGAqgw6fSMZZa9rlsXuG3mG9YYdDGFZC; expires=Mon, 09-Mar-2020 13:06:22 GMT; Max-Age=2592000; path=/; domain=.pixiv.net; secure; HttpOnly'
# cookies = {}
# for line in rawcookies.split(';'):
#     print(line)
#     key,value=line.split('=',1)#字符串分割成两个。
#     cookies[key]=value
# x = requests.get(url,headers=headers,cookies=cookies)
# print(x.text)

# headers = {
#     'Origin': 'https://www.pixiv.net',
#     'Referer':'https://www.pixiv.net/users/21405138/bookmarks/artworks',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
# }
# x = requests.get('https://i.pximg.net/img-original/img/2020/02/05/17/57/13/79298732_p0.png')
# print(x.status_code)
# path='./haha.png'
# with open(path,'wb')as f:
#     f.write(x.content)