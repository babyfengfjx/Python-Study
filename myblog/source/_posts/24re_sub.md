---
title: re正则跨行匹配
categories: 
- python
- re
tags:
- re
date: 2023-02-10 16:25:34
---

## 需求背景

> 我在网上复制了他人的文章，用的是Markdown编写的，不过复制后发现对于代码块中我本地的typora并没法识别具体语言，从而高亮的功能就没有，可以手动一个个代码块选择语言，但是一篇文章少说也有几百个这种代码块，手动添加这事是不会做的，肯定得来两句代码帮忙了，因此就有了下面的代码过程。

需要替换的文本内容结构如下：

~~~python
```
t = type("Mikigo", (), {"name": "huangmingqiang"})
T = t()
print(t)
print(T.name)
print(type(t))
<class '__main__.Mikigo'>
huangmingqiang
<class 'type'>
```
~~~

## 匹配结构分析

**原始结构：**

~~~python
```
XXXXX
XXXXXX
XXXXXXX
```
~~~

**要修改成的结构：**

~~~python
```python
XXXXX
XXXXXX
XXXXXXX
```
~~~

想要匹配的结构其实非常简单，就是如上的这种结构，一对```包含起来的结构：

- 其中包含中的内容应该是不变的，只是在第一个```后面加上具体的语言类型就可以；
- 如上面需要修改成的结构，仅仅多了一个“python”；
- 也就是需要将原始结构中的内容在```后都添加上一个python；

## 正则匹配表达式

通过上面结构的观察就很容易发现正则表达是可以按照下面这么写：

```python
compile_str = r'"```(.*?)```"    # 其中（.*?）就代表了括起来的所有内容，且用到了捕获组，因为匹配到的内容我们还需要用到，所以用捕获组方便后面使用
```

很显然，当你使用`re.findall`或者使用`re.sub`的时候发现根本无法匹配到任何内容……

**re.S 和 re.DOTALL**

主要是因为在re正则匹配时，是无法作跨行匹配的，也就是说有换行的内容你都想匹配的话，直接这样写表达式是无法匹配的，默认只是按照行匹配，那遇到这种情况后，就需要用上re.S 或者 re.DOTALL 这种常量标志，它们的含义都是改变正则表达式中 `.` 的含义，使其能够匹配任意字符，包括换行符。

## findall 和 sub 参数的区别

> 使用中遇到的问题：
>
> - 通过re.findall我使用re.S标志，顺利的匹配到了我想要的内容，匹配表达式是这么写的:
>
>     ```python
>     import re
>     
>     with open('/home/babyfengfjx/Desktop/pythonword.txt','r') as file:
>         content = file.read()
>     compiles = "```(.*?)```"
>     matchs = re.findall(compiles,content,re.S)  # 可以看到这里，直接多使用了一个re.S标志
>     ```
>
> - 但是当我同样这么使用`re.sub`的时候发现没生效……
>
>     ```python
>     import re
>     with open('/home/babyfengfjx/Desktop/pythonword.txt','r') as file:
>         content = file.read()
>     compiles = "```(.*?)```"
>             
>     content_new = re.sub(compiles,lambda x:'```python'+ x.group(1)+'```',content,re.S)  # 同样我在这里使用了re.S参数，但是结果压根就没有作任何匹配
>     print(content_new)
>     ```

通过查看这两个方法的内容后发现:

- `re.findall`函数中只有三个参数`pattern, string, flags`,一般情况下就只用前面两个，也就是正则表达式，和待匹配的内容，通常情况下直接写`re.S`就默认赋值给了flags这个关键字参数了，所以没有任何问题的。
- 而`re.sub`函数中有四个参数`pattern, repl, string, count, flags`,如果我同样直接在后面多加一个re.S，那么按照位置参数来对应，实际对应的是count这个参数，而flags这个参数并没有得到任何赋值，所以才不会产生效果了，所以正确的使用方法是，需要加上关键字参数`flags=re.S`,而不能直接省略了`flags`

```python
def findall(pattern, string, flags=0):
    """Return a list of all non-overlapping matches in the string.

    If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.

    Empty matches are included in the result."""
    return _compile(pattern, flags).findall(string)

def sub(pattern, repl, string, count=0, flags=0):
    """Return the string obtained by replacing the leftmost
    non-overlapping occurrences of the pattern in string by the
    replacement repl.  repl can be either a string or a callable;
    if a string, backslash escapes in it are processed.  If it is
    a callable, it's passed the Match object and must return
    a replacement string to be used."""
    return _compile(pattern, flags).sub(repl, string, count)
```

## 最终代码实现

**step1:小试牛刀**

```python
import re

text = """
        isinstance("123", str)  # 返回布尔值        type("123")  # 直接返回类型                    """compiles = "```(.*?)```"newtext = re.sub(compiles, lambda x:'python'+ x.group(1), text,flags=re.DOTALL)  #这里flags=re.S也是一样的效果print(newtext) 
```

**output1:**

```python
python
          isinstance("123", str)  # 返回布尔值
          type("123")  # 直接返回类型
```

从上面的输出结果来看，并不是我们想要的结果，因为外层的```不见了，因为这种情况下会将整个正则表达式匹配到的内容都按照待替换内容替换掉，所以丢掉了外层的引号内容了。

**step2：手动加三引号**

```python
import re

text = """
        isinstance("123", str)  # 返回布尔值        type("123")  # 直接返回类型                    """compiles = "```(.*?)```"newtext = re.sub(compiles, lambda x:'```python'+ x.group(1)+'```', text,flags=re.DOTALL) #这里手动在外层添加了三引号了print(newtext) 
```

**output2:**

~~~python
```python
isinstance("123", str)  # 返回布尔值
type("123")  # 直接返回类型
```
~~~

从上面的输出结果来看就是我们想要的结果了，整个文档直接跑下来然后将替换后的内容粘贴到typora内容就完全到位了。

## 总结

- **re.S 和 re.DOTALL**效果一样，都是可以作跨行匹配的；
- findall 和 sub因参数个数不一样，在使用标志参数时，尽量加上`flags= xx`；
- 在使用捕获组时，是会将匹配到的所有内容一次进行处理的，根据捕获组的个数，依次称为group(1)、group(2)……
- 在对捕获组内容进行处理是可以配合lambda函数类对匹配到的内容进行一些加工处理。
