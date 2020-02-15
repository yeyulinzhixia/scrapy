scrapy

代理使用字段meta['http_proxy']= 'http://172.0.0.0:1234'

爬虫暂停
方法1：scrapy crawl spidername -s J0BDIR=文件夹名/001
    文件夹需要提前创建好
方法2：setting中设置  J0BDIR='文件夹名/001'



B站爬虫
bilibilirank   rank 
https://www.bilibili.com/ranking


【item】

--榜单页面爬取--
排名rank //*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li[1]/div[1]/text()
分数points //*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li[1]/div[2]/div[2]/div[2]/div/text()
视频链接video_url //*[@id="app"]/div[1]/div/div[1]/div[2]/div[3]/ul/li[1]/div[2]/div[2]/a[@href]
视频号av  video_url.strip('https://www.bilibili.com/video/')

--从视频页爬取--
标题title //*[@id="viewbox_report"]/h1/span/text()
UP主up //*[@id="v_upinfo"]/div[2]/div[1]/a[1]/text()
粉丝数fans //*[@id="v_upinfo"]/div[3]/div[2]/span/span/text()
投稿时间contribute_time //*[@id="viewbox_report"]/div[1]/span[2]/text()
分区fenqu //*[@id="viewbox_report"]/div[1]/span[1]/a[1]/text()
板块bankuai //*[@id="viewbox_report"]/div[1]/span[1]/a[2]/text()
播放量bofang //*[@id="viewbox_report"]/div[2]/span[1][@title]  bofang = bofang.strip('总播放数')
弹幕数danmu //*[@id="viewbox_report"]/div[2]/span[2][@title]  danmu = danmu.strip('历史累计弹幕数')
点赞数dianzan//*[@id="arc_toolbar_report"]/div[1]/span[1]/text()
硬币数coins //*[@id="arc_toolbar_report"]/div[1]/span[2]/text()
收藏数collections //*[@id="arc_toolbar_report"]/div[1]/span[3]/text()
分享数share //*[@id="arc_toolbar_report"]/div[1]/span[4]/text()
评论数pinglun //*[@id="comment"]/div/div[1]/span[1]text()

--额外项--
爬取时间time datetime.datetime.now()


【日排行】
全站 https://www.bilibili.com/ranking/all/0/0/1
动画 https://www.bilibili.com/ranking/all/1/0/1
国创 https://www.bilibili.com/ranking/all/168/0/1
音乐 https://www.bilibili.com/ranking/all/3/0/1
舞蹈 https://www.bilibili.com/ranking/all/129/0/1
游戏 https://www.bilibili.com/ranking/all/4/0/1
科技 https://www.bilibili.com/ranking/all/36/0/1
数码 https://www.bilibili.com/ranking/all/188/0/1
生活 https://www.bilibili.com/ranking/all/160/0/1
鬼畜 https://www.bilibili.com/ranking/all/119/0/1
时尚 https://www.bilibili.com/ranking/all/155/0/1
娱乐 https://www.bilibili.com/ranking/all/5/0/1
影视 https://www.bilibili.com/ranking/all/181/0/1


原创榜 all 改为 origin

新人榜 https://www.bilibili.com/ranking/rookie/0/0/1

【周排行】
新番榜 https://www.bilibili.com/ranking/bangumi/13/0/7

影视榜 
纪录片 https://www.bilibili.com/ranking/cinema/177/0/7
电影   https://www.bilibili.com/ranking/cinema/23/0/7
电视剧 https://www.bilibili.com/ranking/cinema/11/0/7

【各个分区编号tid】
https://s1.hdslb.com/bfs/static/jinkela/online/online.98c7582a48a04d7c48ad075c78ae33b16a816c7e.js
1: 动画  25MMD·3D  47短片·手书·配音  86特摄27 综合
3: 音乐  28原创音乐 31翻唱 30VOCALOID·UTAU 194电音 59演奏 193MV 29音乐现场 130音乐综合 
4: 游戏
5: 娱乐
11: 电视剧
13: 番剧 33连载动画 32完结动画 51资讯 152官方延伸
17: 单机游戏
23: 电影
36: 科技
75: 动物圈
76: 美食圈
119: 鬼畜
129: 舞蹈 20宅舞 198街舞 199明星舞蹈 200中国舞 154舞蹈综合 156舞蹈教程
138: 搞笑
155: 时尚
160: 生活
165: 广告
167: 国创 153国产动画 168国产原创相关 169布袋戏 195动态漫·广播剧 170资讯
177: 纪录片
181: 影视
188: 数码

