---

title: Python循环创建变量/规律性命名变量
categories: 
- python
- 变量
tags:
- python
date: 2020-01-03 15:21:34

---

# 需求背景：

> 有时候在编写小脚本时，存在一些需要批量创建变量名的时候，在存在多少个变量不确定的情况下，通过提前写死多个变量是不合适的，所以此时就需要根据实际变量个数，来确定最终变量名称，也就有了这个需求。

- 其核心就是通过```locals```来完成这个效果；
- 因为我们在创建变量的时候，也就是一个局部变量
- `locals()` 是一个内建函数，它会返回一个表示当前局部符号表的字典。它允许你检查函数或方法中的局部变量，在调试的时候也非常有用；

## locals输出是一个字典

所以可以通过在字典中使用它的键来访问局部变量的值，如下所示：

```python
def my_function(x):
      y = x + 1
      print(locals()['y'])

my_function(5)
```

这会输出 `6`。

## 动态创建局部变量

那么想要动态的创建局部变量，就可以利用这个字典的特性来直接给`locals()`这个字典中创建字典对象就可以：

---
```python
for i in range(5):
    locals()[f'num_{i}']=i  
```

这样就可以动态的创建局部变量了。

## 全局变量

如果想检查全局变量，可以使用 `globals()` 函数。它的用法与 `locals()` 函数类似，但它返回的是全局符号表。

例如：

```python
x = 5
def my_function():
  y = x + 1
  print(globals())
my_function()
```

这会输出一个包含全局变量 `x` 的字典：

```
Copy code
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 5, 'my_function': <function my_function at 0x1022d1e18>}
```

你可以使用 `globals()['x']` 来访问全局变量 `x` 的值。

就像 `locals()` 函数一样，`globals()` 函数也返回的是一个副本，修改返回的字典并不会更改全局变量。要修改全局变量，你需要使用赋值语句（例如 `x = 5`）。
