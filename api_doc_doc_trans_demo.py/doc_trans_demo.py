#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : reallyli<lizhuangzhuang@baidu.com>

import hashlib
import time
import requests
import os

appid = '20221226001509084' # Get your appid from this link.https://fanyi-api.baidu.com/api/trans/product/desktop fengjinxiong
seckey = 'LlZ9CECTqAOOzThYXyCg' # Get your seckey from this link.https://fanyi-api.baidu.com/api/trans/product/desktop
# appid = '20221226001509154' # zhoupan
# seckey = 'RXV2MbZkCMxxezNABgWA'
# appid = '20221226001509245'  # fengxintong
# seckey = 'd8NcZ1dIOyeTafDncpr4'
file = 'ISO 29119-5-5.pdf' # Full path of local file.
request_url = 'http://fanyi-api.baidu.com/api/trans/vip/doctrans' # API service url.

params = {
    'appid' : appid,
    'from' : 'en',
    'to' : 'zh',
    'timestamp' : str(int(time.time())),
    'type' : 'pdf',
    'file' : file
}

# Splicing request parameters.
def get_params():
    params_str = ''
    for key in sorted(params):
        params_str += key
        params_str += '='
        params_str += params[key]
        params_str += '&'
    return params_str

# Generating an MD5 checksum of a file.
def md5_file(file):
     with open(file, "rb") as f:
        data = f.read()
        md5 = hashlib.md5(data)
        return md5.hexdigest()

# Send translation request.
def translate():
    str = get_params()+md5_file(file)+seckey
    params['sign'] = hashlib.md5(str.encode("utf-8")).hexdigest()
    # Upload the file with <multipart/form-data>
    files = {'file':(os.path.basename(file), open(file, 'rb'), "multipart/form-data")}
    print(files)
    print(params)
    response = requests.post(request_url, files=files, data=params)
    if response:
        return response.json()
    else:
        return 'error'

if __name__ == '__main__':
    print(translate())