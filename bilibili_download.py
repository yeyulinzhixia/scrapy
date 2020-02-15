#-*- coding:UTF-8 -*-
import requests,json
from urllib import parse
from bs4 import BeautifulSoup
from contextlib import closing
from multiprocessing import Process
class Bilibili(object):
    def __init__(self):
        self.target='https://www.bilibili.com/video/avreplace/'#视频地址
        self.av=''#av号
        self.video=[]#视频下载链接
        self.grade1=[]#视频画质等级
        self.grade2=[]#音频等级
        self.music=[]#音频地址
        self.name=''#视频名字
        self.headers={'Referer': 'https://www.bilibili.com/','User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        #上面是一些头部信息，用于伪装自己
    #获取视频的各种信息
    def getinfo(self):
        req=requests.get(url=self.target,headers=self.headers)
        bf=BeautifulSoup(req.text,'lxml')
        # self.name=bf.find_all('span',class_="tit")[0].text
        cont1=bf.find_all("script")#寻找我们需要的东西
        cont1=cont1[2].text.replace("window.__playinfo__=","")#把内容替换掉以便后面进行json数据解析
        cont1=json.loads(cont1)#json数据解析
        for each in cont1['data']['dash']['video']:#遍历json数据，获取视频下载地址
            self.grade1.append(each['id'])
            self.video.append(each['baseUrl'])
        for each in cont1['data']['dash']['audio']:#获取音频下载地址
            self.grade2.append(each['id'])
            self.music.append(each['baseUrl'])
    def start(self):
        while True:
            s=input("请输入AV号（只用输数字）:")
            self.av=s
            self.target=self.target.replace('replace',s)
            req=requests.get(url=self.target,headers=self.headers)
            #可以根据返回的内容判断视频是否存在
            if req.text.find('视频去哪了呢？_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili')!=-1 or  req.text.find(' 404  ')!=-1:
                print ("视频不存在！")
            else:
                break
        self.getinfo()
        bf=BeautifulSoup(req.text,'lxml')
        #对数据进行解析，获取视频名称
        self.name=bf.find_all('span',class_="tit")[0].text
        print("视频名称:%s" %self.name)
        grade=[]
        for i in range(len(self.grade1)):
            grade.append(str(i)+':'+str(self.grade1[i]))
        a=input("请选择下载画质：%s(数字越高越清晰，只需要输入序号)" %grade)
        grade.clear()
        for i in range(len(self.grade2)):
            grade.append(str(i)+':'+str(self.grade2[i]))
        b=input("请选择下载音质：%s(数字越高越音质好，只需要输入序号)" %grade)
        #下面是多线程的代码，一个线程下视频，一个下音频
        p1 = Process(target=self.down,args=(a,1))
        p1.start()
        p2 = Process(target=self.down,args=(b,2))
        p2.start()
        p1.join()
        p2.join()
        print ("下载成功！")
    def down(self,v,a):
        #判断下载的内容
        if a==1:
            av=self.av+'.mp4'
            target=self.video[int(v)]
            print ("正在下载视频.....")
        else:
            av=self.av+'.mp3'
            target = self.music[int(v)]
            print ("正在下载音频......")
        #下面是下载视频和音频的代码
        with closing(requests.get(url=target, stream=True, headers=self.headers)) as r:  # 这里就是下载图片的代码了
            with open(av, 'ab+') as f:  # 这里是保存图片
                for chunk in r.iter_content(chunk_size=1024):  # 下面都是下载图片数据的代码，所以不解释
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__=="__main__":
    bi=Bilibili()
    bi.start()
