---
title: 通过xargs配合管道符传递参数
categories: 
- linux
- shell
tags:
- linux
- shell
date: 2021-06-03 11:21:34
---
---
# shell脚本通过xargs配合管道符传递结果

> xargs 是一个 Unix 命令，它的作用是将标准输入中的数据转换为命令行参数，并执行指定的命令。

```Shell
# 通过find来查找目录下的相关文件，然后传递给cat，注意这里的I参数很重要
find -name "*list" | xargs -I {} cat {} | grep -i "^deb"
```

**基本用法如下：**

```shell
command | xargs [-options] [command [initial-arguments]]
```

其中:

- `command` 指定要执行的命令，`xargs` 会将标准输入中的数据作为命令行参数传递给这个命令。

- `-options` 是可选的，用于指定 xargs 的行为方式。

- `initial-arguments` 是可选的，表示在传递的命令行参数之前需要传递的额外参数。

例如，你可以使用 xargs 将文件列表转换为 `rm` 命令的参数，从而删除多个文件：

```shell
find . -name "*.txt" | xargs rm
```

或者你可以使用 xargs 将文本文件中的每一行作为 `grep` 命令的参数来搜索多个文件：

```shell
cat patterns.txt | xargs grep -l
```

当 xargs 处理的参数数量较多时，它会自动将这些参数分成多批执行，以避免命令行参数过长的问题。你可以使用 `-n` 选项来指定每批参数的数量，例如：

```shell
find . -name "*.txt" | xargs -n 3 rm
```

这条命令会将找到的文件名分成多批，每批最多包含 3 个文件名。每批文件名都会作为 `rm` 命令的参数执行。

**配合管道：**

使用 xargs 配合管道是一种常见的模式，这种模式可以用于将输出结果传递给另一个命令作为参数。

例如，你可以使用如下命令查找文件系统中大小超过 100MB 的文件，并使用 xargs 将这些文件删除：

```shell
find / -size +100M | xargs rm
```

也可以使用 xargs 配合管道来实现更复杂的任务，例如：

```shell
grep -R "ERROR" . | cut -d ":" -f 1 | sort | uniq | xargs -I{} sed -i '/ERROR/d' {}
```

这条命令会在当前目录及子目录中查找所有包含 "ERROR" 的文件，然后删除这些文件中的 "ERROR" 行。

需要注意的是，使用 xargs 配合管道时，应该**避免在管道中使用命令别名**，因为别名可能不会在 xargs 中生效。应该使用完整的命令名称。



**上面的 -I{} 是什么意思:**

**`-I{}` 是 xargs 的一个选项，用于指定命令中的某个位置应该插入参数**。

例如，在上面的命令中，`-I{}` 表示在命令 `sed -i '/ERROR/d'` 中的 `{}` 处插入参数。因此，当 xargs 执行这条命令时，实际上会执行类似于 `sed -i '/ERROR/d' file1 file2 file3` 的命令。

你可以使用任意的字符替换 `{}`，例如：

```shell
find . -name "*.txt" | xargs -IXXX mv XXX backup/XXX
```

这条命令会将找到的所有 .txt 文件移动到 backup 目录下。

需要注意的是，在使用 xargs 的 `-I` 选项时，**你需要确保命令中的替换字符（例如 `{}` 或 `XXX`）不会在命令本身中出现**。否则，xargs 可能会将命令中的字符也作为参数替换。

**扩展：**

除了 `-I` 选项外，xargs 还提供了其他的选项来控制命令的执行方式。

例如，你可以使用 `-p` 选项来让 xargs 在执行命令前显示命令，以便你可以检查命令是否正确：

```shell
echo a b c | xargs -p rm
```

这条命令会输出 `rm a b c`，然后询问你是否执行这条命令。你可以输入 `y` 来执行命令，或者输入 `n` 来取消执行。

你还可以使用 `-t` 选项来让 xargs 在执行命令前输出命令，以便你可以跟踪命令的执行过程：

```shell
echo a b c | xargs -t rm
```

这条命令会输出 `rm a b c`，然后执行命令。



