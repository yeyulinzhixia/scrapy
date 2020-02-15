# -*- coding: utf-8 -*-
 
import random
from proxy_pool.utils import logger




 
# 随机选择 User-Agent 的下载器中间件
class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        # 从 settings 的 USER_AGENTS 列表中随机选择一个作为 User-Agent
        user_agent = random.choice(spider.settings['USER_AGENT_LIST'])
        request.headers['User-Agent'] = user_agent
        request.headers['Referer'] = 'https://ip.ihuan.me/today/2020/02/10/19.html'
        return None
 
    def process_response(self, request, response, spider):
        # 验证 User-Agent 设置是否生效
        logger.info("headers ::> User-Agent = " + str(request.headers['User-Agent'], encoding="utf8"))
        return response

