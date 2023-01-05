---
title: 字符串格式时间转换成时间戳
categories: 
- python
- time
tags:
- python
- time
date: 2023-01-04 15:21:34
---
---
> 需求：在明道云中需要做时间比较，而接口传递的时间格式是字符串格式，因此需要转换成时间戳后再做加减运算。

## 实际用途如下：

```python
import time
webhooktime = '2023-01-04 11:19:59'
localtime = '2023-01-04 11:19:27'
def str2timestamp(strdate):
    if strdate:  # 生产环境会出现时间内容为空的情况，需要加个判断
        time_tuple = time.strptime(strdate,'%Y-%m-%d %H:%M:%S')
        return time.mktime(time_tuple)
    else:
        return 0
webhooktime = str2timestamp(webhooktime)
localtime = str2timestamp(localtime)
outtime = webhooktime - localtime
output = {"outtime":outtime}
```

## 具体思路：

使用 Python 的 `time` 模块中的 `strptime` 函数将时间字符串转换成时间元组，再使用 `time` 模块中的 `mktime` 函数将时间元组转换成时间戳。

```
import time

def str_to_timestamp(s):
  # 将时间字符串转换成时间元组
  time_tuple = time.strptime(s, '%Y-%m-%d %H:%M:%S')
  # 将时间元组转换成时间戳
  timestamp = time.mktime(time_tuple)
  return timestamp

print(str_to_timestamp('2023-01-04 11:19:59'))

```

这会输出时间戳（单位是秒）：

```
2147483647.0
```

## 反过来将时间戳转换成字符串时间格式：

```python
import datetime

def str_to_timestamp(s):
  # 将时间字符串转换成 datetime 对象
  dt = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
  # 将 datetime 对象转换成时间戳
  timestamp = dt.timestamp()
  return timestamp
print(str_to_timestamp('2022-01-01 00:00:00'))
```

这也会输出时间戳（单位是秒）：

```python
1609459200.0
```





