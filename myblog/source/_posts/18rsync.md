---
title: rsync同步
categories: 
- linux
tags:
- linux
- rsync
date: 2023-01-11 09:21:34
---

`rsync` 是一个用于在两个位置同步文件和目录的命令行工具。 它可用于在网络上将文件从一台电脑复制到另一台电脑。 要使用 rsync 从一台电脑同步文件到另一台电脑，请使用以下命令:

## 从本机复制到远程主机

```shell
rsync -avz -e ssh /path/to/local/files  username@remote_host:/path/to/remote/files
```

- 参数 -a 代表 保留文件权限，所有权和时间戳。
- 参数 -v 让 rsync 变得详细，这样您就可以看到传输进度。 
- 参数 -z 代表 在传输之前压缩数据，这可以加速网络上的传输。
- 参数 -e ssh 代表使用 SSH 连接到远程主机。 这允许您在网络上安全地传输文件。
-  username 是您登录远程主机的用户名，
-  remote_host 是远程计算机的主机名或 IP 地址。

例如，如果远程主机的 IP 地址为 192.168.1.100，您想将本地机器上目录 `/Users/johndoe/Desktop/myfiles `中的文件复制到远程主机上的目录 `/home/johndoe/Desktop/myfiles`，则命令如下:

```shell
rsync -avz -e ssh   /Users/johndoe/Desktop/myfiles    johndoe@192.168.1.100:/home/johndoe/Desktop/myfiles
```

运行 `rsync` 命令的用户应具有源目录的读取权限和目标目录的写入权限，否则它将失败。

## 从远程主机复制到本机

如果要将文件从远程主机复制到本地计算机，您只需要简单地交换本地和远程文件路径就可以了。具体命令如下:

```shell
rsync -avz -e ssh username@remote_host:/path/to/remote/files    /path/to/local/files
```

username 是远程主机登录用户名，remote_host 是远程计算机的主机名或 IP 地址, `/path/to/remote/files `是远程文件的路径，/path/to/local/files 是本地文件夹路径

例如，如果你想要从远程主机 IP 为 192.168.1.100 上的目录 `/home/johndoe/Desktop/myfiles` 中的文件复制到本地计算机的 `/Users/johndoe/Desktop/myfiles`， 命令如下:

```shell
rsync -avz -e ssh johndoe@192.168.1.100:/home/johndoe/Desktop/myfiles        /Users/johndoe/Desktop/myfiles
```

## 扩展

`rsync` 默认是实现增量同步的，它会只传送新增或者更改过的文件，这样可以大大减少传输时间和带宽的使用。

`rsync`使用检验和算法比较源和目标文件的差异，并只传送那些差异的部分。 这就是为什么 `rsync `的传输速度比其他文件传输工具要快的原因。

如果你使用上面给出的命令来传输文件，那么会是增量同步。

需要注意的是, `rsync` 只会对文件内容进行增量同步, 如果文件的属性如权限，时间戳等发生了改变，`rsync `会将其完整的传输过去。

如果你希望同步文件夹的结构和文件的属性的话，可以使用参数 -a 或者` -rlptgoD -a `等同于 `-rlptgoD`，代表将文件的所有属性同步过去 -r 代表递归，传递子文件夹 -l 代表将符号链接作为符号链接来传递 -p 代表保留文件权限 -t 代表保留文件时间戳 -g 代表保留文件组 -o 代表保留文件用户 -D 代表保留特殊文件。

```shell
rsync -avrlptgoD -e ssh 
johndoe@192.168.1.100:/home/johndoe/Desktop/myfiles      
/Users/johndoe/Desktop/myfiles
```

这样可以保证源文件夹和目标文.

除了上述参数之外，`rsync`还支持` --ignore-existing `参数, 只会传递新增的文件，这可以用来在更新文件时避免覆盖已经修改过的文件。

如果你希望将远程目录和本地目录完全同步，并且本地目录是新建的，可以使用 `--delete`参数，来删除本地目录中源目录没有的文件

## 定时同步脚本

可以使用 Linux 上的 cron 工具来设置定时自动同步命令。cron 是一种定时任务计划程序，可以在特定时间自动执行命令。

首先打开 crontab 文件

```shell
crontab -e
```

添加如下内容

```shell
0 0 * * *    rsync -avz -e  ssh /path/to/local/files     username@remote_host:/path/to/remote/files
```

其中的 "0 0 * * *" 代表每天的 00:00 (即凌晨) 执行一次 rsync 命令。如果希望在其他时间执行此命令，可以根据需要修改此部分。

需要注意的是, 这里给出的命令是基于每天的时间运行的,如果需要设置更高级的时间计划，如每周、每月或指定时间执行, 可以参考cron 的语法来编写 例如 :

```shell
# 每周一的10:30执行
30 10 * * 1  rsync -avz -e ssh /path/to/local/files username@remote_host:/path/to/remote/files
#每小时的10分钟执行
10 * * * * rsync -avz -e ssh /path/to/local/files username@remote_host:/path/to/remote/files
```

需要注意的是, cron 只会在系统开机之后才会开始执行定时任务， 如果你需要在系统启动时立即执行任务，需要将任务命令加入系统启动脚本中，如 /etc/rc.local 文件或者systemd 中。
