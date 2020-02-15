# -*- coding: utf-8 -*-
BOT_NAME = 'proxy_pool'
 
SPIDER_MODULES = ['proxy_pool.spiders']
NEWSPIDER_MODULE = 'proxy_pool.spiders'
 
# 保存未检验代理的Redis key
PROXIES_UNCHECKED_LIST = 'proxies:unchecked:list'
 
# 已经存在的未检验HTTP代理和HTTPS代理集合
PROXIES_UNCHECKED_SET = 'proxies:unchecked:set'
 
# 代理地址的格式化字符串
PROXY_URL_FORMATTER = '%(schema)s://%(ip)s:%(port)s'
 
# 通用请求头字段
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive'
}

# 请求太频繁会导致 503 ,在此设置 5 秒请求一次
DOWNLOAD_DELAY = 2  # 250 ms of delay

USER_AGENT_LIST = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
 
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'proxy_pool.middlewares.RandomUserAgentMiddleware': 543,
    #   'proxy_pool.middlewares.RandomProxyMiddleware': 544,
}
 
ITEM_PIPELINES = {
    'proxy_pool.pipelines.ProxyPoolPipeline': 300,
}
 

 
######################################################
##############下面是Scrapy-Redis相关配置################
######################################################
 
# # 指定Redis的主机名和端口
# REDIS_HOST = '172.16.250.238'
# REDIS_PORT = 6379
# REDIS_PARAMS = {'password': '123456'}
 
# # 调度器启用Redis存储Requests队列
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
 
# # 确保所有的爬虫实例使用Redis进行重复过滤
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
 
# # 将Requests队列持久化到Redis，可支持暂停或重启爬虫
# SCHEDULER_PERSIST = True
 
# # Requests的调度策略，默认优先级队列
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
