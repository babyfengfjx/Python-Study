---
title: hexo部署
categories: 
- hexo
tags:
- hexo
date: 2020-01-11 09:21:34
---

## nodejs安装

1. [官网下载](https://nodejs.org/zh-cn/)

2. 1. 将其解压到任意目录。
    2. 打开终端，进入到解压后的目录，例如：

    ```shell
    cd /path/to/node-v14.15.1-linux-x64
    ```

    1. 将解压后的目录中的 bin 目录加入到系统环境变量 PATH 中，这样系统就可以找到 Node.js 的可执行文件。 可以在~/.bashrc or ~/.bash_profile 或者 /etc/environment 中加入如下内容：

    ```shell
    export PATH=$PATH:/path/to/node-v14.15.1-linux-x64/bin
    ```

    1. 更新系统环境变量

    ```shell
    source ~/.bashrc or source ~/.bash_profile or source /etc/environment
    ```

    1. 验证 Node.js 是否安装成功。

    ```shell
    Copy code
    node -v
    ```

    这样你就可以在 Linux 系统上使用官方压缩包安装的 Node.js

## 更换npm淘宝镜像地址

npm 是 Node.js 的包管理器，默认使用 npm 官方镜像来安装和管理包。由于网络原因，在国内可能无法使用 npm 官方镜像，因此可以更换为国内镜像来安装包。

一种常用的方法是使用淘宝镜像，下面是更换方法

- 方法1 :使用cnpm

```shell
npm install -g cnpm --registry=https://registry.npm.taobao.org
```

接下来就可以使用cnpm代替npm来安装包，如

```shell
cnpm install [package name]
```

- 方法2 : 更改npm config

```shell
npm config set registry https://registry.npm.taobao.org
```

或者

```shell
npm config set registry https://registry.npm.taobao.org  --global
```

- 方法3 : 编辑 .npmrc 文件 在用户主目录下编辑.npmrc文件，并在其中添加 registry=[https://registry.npm.taobao.org](https://registry.npm.taobao.org/)

需要注意的是，第二种和第三种方法会影响到全局的npm安装，在不更改的情况下会一直使用淘宝镜像。 通过使用淘宝镜像可以提高 npm 安装包的速度，提高工作效率。

## 安装hexo

使用 npm 一键安装 Hexo 博客程序：

```shell
cnpm install -g hexo-cli   #这里我用的是cnpm，使用的上面第一种方法
```

