---
title: 使用随机UserAgent来访问链接
categories: 
- python
- 爬虫

tags:
- python
- 爬虫
date: 2023-01-09 15:21:34
---
> 在做爬虫时，经常会被网站封，所以我们经常会做一些基本的反爬处理，此处就使用了一个`fake_useragent`模块，来随机给我们提供浏览器的用户代理信息，可以在一定程度上规避反爬的问题。

下文代码主要是来爬取B站视频的评论，实现有新增评论时自动提醒的功能。

其中在反爬上使用了几点思想：

- 首先是用`fake_useragent`模块，来随机提供UserAgent信息，以便每次构造不同的headers，主要用法就是`UserAgent().random`；
- 在每次访问请求时，随机等待几秒时间，因为此工具对效率没有任何要求，所以尽量搞稳一点；

```python
import requests
import math
import shelve
import time
import random
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from fake_useragent import UserAgent
headers ={"accept": "application/json, text/plain, */*",
        "origin": "https://space.bilibili.com",
        "User-Agent": UserAgent().random   #这里就是关键，每次调用都会随机生成UserAgent信息
}

def get_videoinfo():
    """
    获取UP主的所有视频内容，并返回每个视频的最新评论
    """
    def getpages():
        url_getvideo = f'https://api.bilibili.com/x/space/wbi/arc/search?mid=137324885&ps=30&tid=0&pn=1&keyword=&order=pubdate'
        res = requests.get(url_getvideo,headers=headers).json()['data'] #  获取当前页视频的信息
        pageinfo =  res['page']
        pages = math.ceil(int(pageinfo['count'])/int(pageinfo['ps']))
        return pages
    def getpageinfo(page):
        url_getvideo = f'https://api.bilibili.com/x/space/wbi/arc/search?mid=137324885&ps=30&tid=0&pn={page}&keyword=&order=pubdate'
        videoinfo = requests.get(url_getvideo,headers=headers).json()['data']['list']['vlist'] #  获取当前页视频的信息
        print(headers)
        for i in videoinfo :
            # print(i)
            # print(i['aid'],i['title'],i['bvid'])
            video_outinfo =  (i['aid'],i['title'],i['bvid'])
            # print(video_outinfo)
            getcomment(video_outinfo)
            time.sleep(random.randint(1,3))  # 随机等待几秒钟

    videopages = getpages()
    for page in range(1,videopages+1):
        print(page)
        # 返回评论信息
        getpageinfo(page)
        time.sleep(random.randint(2, 4))

def send2mdy(body):
    webhook = 'https://cooperation.uniontech.com/api/workflow/hooks/NjNhYWFhOWI1OTM0NDkzNTI5ZjQzNmRl'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
    try:
        res = requests.post(url=webhook,headers=headers,data=body)
        if res.status_code == 200:
            print(body)
            return True

    except Exception as e :
        print(e)
        return False
def savedb(rpid,url):
    with shelve.open('Bilidb') as bilidb:
        bilidb[str(rpid)+str(url)] = rpid

def getdb(rpid,url):
    with shelve.open('Bilidb') as bilidb:
        try:
            return bilidb[str(rpid)+str(url)]
        except KeyError as e:
            print(e)
            return None

def  getcomment(videoinfo):
    """
    通过aid返回对应视频的最新评论
    """
    aid, videotitle, bvid = videoinfo
    videourl = f'https://www.bilibili.com/video/{bvid}/'
    url = f'https://api.bilibili.com/x/v2/reply/main?csrf=053f6fa5c656e3ee1ca547ccbf6ab181&mode=2&&oid={aid}&plat=1&type=1'
    res = requests.get(url,headers=headers)
    try:
        res = res.json()['data']['replies']
        for i in res:
            outinfo = (('rpid',i['rpid']),('uname',i['member']['uname']),('sex',i['member']['sex']),('message',i['content']['message']),('videourlv',videourl),('videotitle',videotitle))
            if not getdb(i['rpid'],videourl):
                body = dict(outinfo)
                res = send2mdy(body)
                if res:
                    savedb(i['rpid'],videourl)
    except Exception as e:
        print('获取评论请求段报错了！')
get_videoinfo()

schedu = BlockingScheduler(timezone='Asia/Shanghai')
schedu.add_job(get_videoinfo,'cron',minute='40', id='bilibiliconment',next_run_time=datetime.datetime.now())
schedu.start()
```

