---
title:  UTC时间转换成中国标准时间
categories: 
- python
tags:
- python
date: 2023-02-07 16:21:34
---

## "T"和"Z"的含义

- 在 ISO 8601 格式的日期时间字符串中，"T" 表示日期和时间之间的分隔符，"Z" 表示 UTC 时区。
- 中国属于 UTC + 8 时区，所以与 UTC 时区相差 8 个小时。

## 具体实现

```python
import datetime

time_str = "2023-02-03T08:36:10Z"

# 首先，将时间字符串解析为 datetime 对象
parsed_time = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%SZ")

# 其次，加上8 个小时以调整时差
corrected_time = parsed_time + datetime.timedelta(hours=8)

# 最后，将校正后的时间格式化为标准格式，如：
standard_time = corrected_time.strftime("%Y-%m-%d %H:%M:%S")

print(standard_time)

```

