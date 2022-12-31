title: requests发送post请求返回405的处理方法
categories:
  - python
  - 爬虫
tags:
  - python
  - 爬虫
  - requests
date: 2022-12-31 11:11:34
---
## Requests 请求返回405

> 主要是因为API请求方式要求是json,但我们在分析不清楚的接口时，一般都按照惯性在传递参数的时候是以data方式，所以在使用requests时，不仅要用data=  xxx  ，还要看json= xxx  这种场景。

下面这个代码当时使用请求时，是使用的是：res_data = requests.post(apiurl,**data=**body,headers=headers)   这里你的data= 并不是网站所需要的，其需要的是json,所以改成json= 就可以了。

```Python
def get_cookie():
    """
    从明道云拉取cookie信息
    """
    apiurl = 'https://cooperation.xxx.com:443/api/v2/open/worksheet/getFilterRows'
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39"}
    body = {
              "appKey": "f7b8e6816d39a931",
              "sign": "ODlkNTVhNDdjZDhjNmYwODhjYjExZTU4NGFmODFkZDQzZjRlNGMzMzJlODdhNzhmNTVjYmQ4ZTA1MzAzNzc3Mw==",
              "worksheetId": "hxggzjxx",
              "viewId": "634509562b5b0f8d7a182f39",
              "pageSize": 5000,
              "pageIndex": 1,
              "filters":[
              {
                "controlId": "leibie",
                "dataType": 2,
                "spliceType": 1,
                "filterType": 2,
                "values": ["应用商店审核平台"]}   ]
                }

    res_data = requests.post(apiurl, json=body, headers=headers)  # 关键就是这里的传参方式改成json
    print(res_data)

get_cookie()
```