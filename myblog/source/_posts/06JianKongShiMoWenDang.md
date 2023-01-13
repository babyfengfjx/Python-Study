---

title: 监控石墨文档的文件数据变化，并提交之明道云
categories: 
- python
- 爬虫
tags:
- python
- 爬虫
- 递归
- requests
- shelve
- cookie
- session
- apscheduler
- 重定向
date: 2022-09-26 15:21:34

---

**核心知识点：**

> - 可使用两种方法来处理登录获取session: 直接通过登录方式，同时**处理重定向问题**；直接手动添加cookie信息来构建session;
> - **通过递归来处理子文件夹的名字，且使用类变量来存储需要的数据**，重点注意**此类变量在使用完后需要清空处理，不然在程序循环跑的过程中会出现数据异常（旧数据一直都在）；**
> - 所有的功能均采用分而治之的思想，拆解到足够细，让方法各司其职；
> - 检测web端数据变化时，**采用本地构建数据库方式（采用shelve），依次对增删改的数据变化做处理**；
> - 本地数据存储时机是在提交数据到web端返回成功后才做存储，避免因提交失败导致本地数据与web数据不一致问题；
> - apscheduler 模块在使用时，采用的后台阻塞式，且采用了触发器对象来更灵活的配置触发规则。

```Python
import requests
import shelve
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.combining import AndTrigger, OrTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
class Oper_shimo():
    """
    石墨文档操作类
    """

    # @classmethod
    # def login_shimo(cls,username,passwd):
    #     """
    #     登录石墨，这个方法就是直接通过登录接口来拿session，但是因为该网站登录有重定向，所以需要进行二次访问重定向后的地址才能拿到session
    #     """
    #     userdata = {
    #         "username": username,
    #         "password": passwd
    #     }
    #     login_url = 'https://doc.uniontech.com/lizard-api/ldap/login'
    #     session = requests.Session()
    #     redirectinfo = session.post(login_url, json=userdata).json()
    #     redirect_url = redirectinfo['redirect_url'] # 拿到重定向链接
    #     session.get(redirect_url) # 在这里拿到session的
    #     return session

    @classmethod
    def login_shimo(cls, cookie):
        """
        登录石墨
        """
        cookie = dict([ i.strip().split('=',1) for i in cookie.split(';')])
        session = requests.Session()
        session.cookies.update(cookie)
        return session
    @classmethod
    def get_folder_source(cls,session,folder_guid):
        """
        获取文件夹下信息
        test:qjPy69jDYXVV6XYr
        返回，获取的原始json信息，以便提供给后续数据清晰函数使用
        """
        folder_url = f'https://doc.uniontech.com/lizard-api/files?folder={folder_guid}'
        return  session.get(folder_url).json()

    @classmethod
    def wash_folderdata(cls,folder_jsondata):
        """
        使用上面获取文件夹基础信息的函数返回数据，返回清洗后的数据列表
        """
        folder_infos = []

        for item in folder_jsondata:
            folder_base_info = {}
            folder_base_info['name'] = item['name']
            folder_base_info['type'] = item['type']
            folder_base_info['url'] = item['url']
            folder_base_info['isFolder'] = item['isFolder']
            folder_base_info['guid'] = item['guid']
            folder_base_info['id'] = item['id']
            folder_base_info['createdby'] = item['user']['name']
            folder_base_info['createdat'] = item['created_at'].split('.')[0].replace('T',' ')
            folder_base_info['updatedAt'] = item['updatedAt'].split('.')[0].replace('T', ' ')
            folder_base_info['updateby'] = item['updatedUser']['name']
            folder_infos.append(folder_base_info)

        return folder_infos
    @classmethod
    def get_file_fathername(cls,session,folderguid):
        """
        通过上级目录guid 返回上级目录名称
        """
        fathername_url = f'https://doc.uniontech.com/lizard-api/files/{folderguid}'
        return session.get(fathername_url).json()['name']

    filelist = []  # 类变量，存储返回信息的，记得用完后，需要清空
    @classmethod

    def get_all_fileinfo(cls,session,foldersinfo,folder_name=''):
        """
        返回文件夹和子文件夹下的所有文件信息
        """
        for file in foldersinfo:
            if not file['isFolder']:
                file['fathername'] = folder_name
                cls.filelist.append(file)
            else:

                foldername = Oper_shimo.get_file_fathername(session,file['guid'])
                if folder_name:
                    foldernames = folder_name +"|>|"+foldername
                else:
                    foldernames = foldername
                folder_jsondata  = Oper_shimo.get_folder_source(session,file['guid'])
                folder_infos = Oper_shimo.wash_folderdata(folder_jsondata)
                Oper_shimo.get_all_fileinfo(session,folder_infos,folder_name= foldernames)
        return cls.filelist
    @classmethod
    def get_send_data(cls,fileinfo):
        """
        判断文件的增删改动,然后输出最终需要更新的信息
        返回数据是字典列表
        用完后需要清空类变量 filelist
        """
        send_list = []
        web_ids = []
        local_ids = []
        for file in fileinfo:
            # print(f"web数据为：{file}")
            web_ids.append(str(file['id']))
            with shelve.open('localdb') as file_localdb:
                local_ids = list(file_localdb.keys())
                try:
                    # print(f"本地数据：{file_localdb[str(file['id'])] }")

                    if file_localdb[str(file['id'])] != file:
                        file['local_status'] = 'update'
                        send_list.append(file)
                except KeyError as e:
                    print('新增数据～')
                    file['local_status'] = 'add'
                    send_list.append(file)


        del_data = list(set(local_ids) - set(web_ids))
        for id in del_data:
            with shelve.open('localdb') as file_localdb:
                del_file = file_localdb[str(id)]
                del_file['local_status'] = 'del'
                send_list.append(del_file)
                del file_localdb[str(id)]
        cls.filelist = [] # 这里很重要，不然在循环过程中，会出现列表数据一直保留导致数据不正常。
        return send_list

    @classmethod
    def store_localdb(cls,file):
        """
        信息提交到明道云成功后，将数据存储更新到本地数据库
        """
        with shelve.open('localdb') as file_localdb:
            if file['local_status'] != 'del':
                del file['local_status']
                file_localdb[str(file['id'])] = file

    @classmethod
    def send_data2mdy(cls,sendinfo):
        """
        将需要更新的数据提交明道云
        接受数据为文件信息原始数据即可
        """
        webhook = 'https://cooperation.uniontech.com:443/api/workflow/hooks/NjMyZDcwMjJjYmJjZjQ3MDkwNjVlY2Mw'
        for file in sendinfo:
            body = {
                    "name": file['name'],
                    "type": file['type'],
                    "url": f"https://doc.uniontech.com{file['url']}",
                    "id": file['id'],
                    "createdby": file['createdby'],
                    "createdat": file['createdat'],
                    "updatedAt": file['updatedAt'],
                    "updateby": file['updateby'],
                    "fathername": file['fathername'].split("|>|")[0],
                    "local_status":file['local_status']

                }
            res = requests.post(webhook,data=body).status_code
            if res == 200:
                Oper_shimo.store_localdb(file)
                print(f'{body} 数据更新成功！')
            else:
                print(f'{body} 数据更新失败！')

def main():
    """
    主函数
    """
    # 此处可以直接手动获取cookie来添加到session，未采用直接登录的方式主要是因为会频繁更换账号密码，且跟他人要cookie信息更加安全
    cookie = 'deviceId=browser-8f474a86-beda-76ea-0d9b-a8b79fb88aff; fp=31ab340bc8205713b458b6f9d2771968; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%223066%22%2C%22%24device_id%22%3A%221834416802a1571-0c31cd72cc2c7d-477a6e25-1fa400-1834416802b13b8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221834416802a1571-0c31cd72cc2c7d-477a6e25-1fa400-1834416802b13b8%22%7D; LOCALE=zh-CN; sensorsdata2015session=%7B%7D; shimo_sid=s%3Ac42f99aa2b1845fbb92f114644d75e7e.aI24YO%2FppGMK1dQxw65DiCfS%2Ba%2BSDwzPWvHGKU7n6WE'
    folderguids = {"技术成果贡献":"8Nk6MwB2zmfZBvqL",}

    for guid in folderguids.values():
        shimo = Oper_shimo()
        session = shimo.login_shimo(cookie)
        folder_jsondata = shimo.get_folder_source(session,guid)
        foldersinfo = shimo.wash_folderdata(folder_jsondata)
        fileinfos = shimo.get_all_fileinfo(session ,foldersinfo)
        # print(fileinfos)
        send_data = shimo.get_send_data(fileinfos)
        print(f'待更新数据为{send_data}')
        shimo.send_data2mdy(send_data)

main()

if  __name__ == '__main__':
    # 创建定时对象
    schedu = BlockingScheduler(timezone='Asia/Shanghai')
    # 创建触发器（通过触发器来设置定时任务，更加灵活）
    trigger = OrTrigger([CronTrigger(day_of_week="0-4", hour='9-22', minute='*/10', second='00'),])  # 可以继续在列表中添加其他更多的规则
    schedu.add_job(main,trigger)
    schedu.start()
```
