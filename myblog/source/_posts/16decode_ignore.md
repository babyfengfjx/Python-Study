---
title: decode中的ignore参数
categories: 
- python
tags:
- python
date: 2023-01-09 16:21:34
---

> - 在 `decode` 函数中，`ignore` 参数用于指定在解码字符串时应忽略的字符。当解码的字符串包含不属于目标编码的字符时，或者当字符串因某种原因被损坏并包含无效字符时，这可能很有用。
> - 如果 ignore 参数设置为 True，则 decode() 函数会忽略无效字符，并在解码后的字符串中跳过这些字符。如果 ignore 参数设置为 False，则 decode() 函数会在遇到无效字符时抛出 `UnicodeDecodeError` 异常。

## ignore的效果

例如，假设我们有一个字符串 'hello'，它用 utf-8 编码后为 b'hello'。如果我们尝试使用 ascii 解码该字符串，则会产生无效字符，因为 utf-8 编码的字符可能不在 ascii 编码的字符集中。

下面是一个例子：

```python
# 将字符串 s 用 utf-8 编码
s = b'hello'

# 尝试用 ascii 解码 s，忽略无效字符
print(s.decode('ascii', ignore=True))

# 尝试用 ascii 解码 s，在出现无效字符时引发异常
print(s.decode('ascii', ignore=False))
```

输出结果如下：

```python
hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe9 in position 1: ordinal not in range(128)
```

## ignore做特定错误处理函数

> `ignore` 参数也可以设置为特定的错误处理函数，该函数可用于自定义处理无效字符的方式。

错误处理函数是一种特殊的函数，用于在解码字符串时处理无效字符的情况。

错误处理函数接受两个参数：**一个错误名称和一个错误信息**。**如果错误处理函数返回一个字符，则该字符将被插入到解码后的字符串中；如果返回 None，则忽略无效字符**。

下面是一个例子：

```python
# 定义错误处理函数
def error_handler(error_name, error_info):
    # 忽略无效字符
    return None

# 将字符串 s 用 utf-8 编码
s = b'hello'

# 尝试用 ascii 解码 s，使用错误处理函数处理无效字符
print(s.decode('ascii', errors=error_handler))
```

- error_name 和 error_info 这两个参数是由 decode() 函数自动传入的，不需要我们手动传递。

- 在 decode() 函数中，error_name 参数表示出现的错误的名称，error_info 参数表示错误的具体信息。
  - 例如，当遇到无效字符时，error_name 参数可能是 'strict'；
  - error_info 参数可能是一个 UnicodeDecodeError 对象。

错误处理函数在解码字符串时自动调用，用于处理遇到的错误。我们可以在错误处理函数中使用 error_name 和 error_info 参数来判断错误的类型和信息，然后根据需要进行相应的处理。

**这两个参数是否一定要在错误处理函数中使用？**

如果希望在处理错误时判断错误的类型和信息，则可以使用这两个参数。

例如，可以使用 error_name 参数判断错误的类型，使用 error_info 参数获取错误的详细信息。这样就可以根据错误的不同类型和信息，采用不同的处理方式。

但是，如果不需要判断错误的类型和信息，也可以不使用这两个参数。例如，可以定义一个简单的错误处理函数，直接返回一个固定的字符或 None。

总之，错误处理函数是一种非常灵活的工具，可以根据自己的需求自定义错误处理函数。

## 扩展

decode的函数原型是```decode([encoding], [errors=‘strict’])```，可以用第二个参数控制错误处理的策略，默认的参数就是`strict`，代表遇到非法字符时抛出异常；
如果设置为`ignore`，则会忽略非法字符；
如果设置为`replace`，则会用?取代非法字符；
如果设置为`xmlcharrefreplace`，则使用XML的字符引用。



