# -*- coding: utf-8 -*-

# This code shows an example of ocr translation from Simplified-Chinese to English.
# This code runs on Python 2.7.x and Python 3.x.
# ```
#   python ocr_translate.py <image>
# ```
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/26` for complete api document

import requests
import random
import json
import os
import sys
from hashlib import md5





endpoint = 'http://api.fanyi.baidu.com'
path = '/api/trans/sdk/picture'
url = endpoint + path

from_lang = 'en'
to_lang = 'zh'

# Set your own appid/appkey.
app_id = '20221226001509084'
app_key = 'LlZ9CECTqAOOzThYXyCg'

# cuid & mac
cuid = 'APICUID'
mac = 'mac'

def main(file_name):
	# Generate salt and sign
	def get_md5(string, encoding='utf-8'):
		return md5(string.encode(encoding)).hexdigest()

	def get_file_md5(file_name):
		with open(file_name, 'rb') as f:
			data = f.read()
			return md5(data).hexdigest()

	salt = random.randint(32768, 65536)
	sign = get_md5(app_id + get_file_md5(file_name) + str(salt) + cuid + mac + app_key)

	# Build request
	payload = {'from': from_lang, 'to': to_lang, 'appid': app_id, 'salt': salt, 'sign': sign, 'cuid': cuid, 'mac': mac}
	image = {'image': (os.path.basename(file_name), open(file_name, 'rb'), "multipart/form-data")}

	# Send request
	response = requests.post(url, params = payload, files = image)
	result = response.json()

	# Show response
	res = json.dumps(result, indent = 4, ensure_ascii = False)
	res = json.loads(res)['data']['content']
	# print(res)
	# print(type(res))
	with open('output.txt','a') as file:

		for i in res:
			content = i['src']+"---"+i['dst']+"\n"
			file.write(content)
if __name__ == '__main__':
	for i in range(70):
		file_name = f'images/output_{i}.jpg'
		main(file_name)