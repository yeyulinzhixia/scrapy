
import requests
import json

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400'}
url = 'http://www.httpbin.org/ip'
x = requests.get(url,headers=headers,proxies={'http':'http://183.147.253.41:9999'},timeout=15)
print(x.text)
y = json.loads(x.text)['origin']

print(y)


# #正则表达式测试
# import re
# one = '185.19.176.237:53281@HTTP#[高匿名]俄罗斯 其他'
# pattern = r'(\d+.\d+.\d+.\d+):(\d+)@(\w+)#\[(\D+)\]'
# b = re.match(pattern,one).group(4)
# print(b)