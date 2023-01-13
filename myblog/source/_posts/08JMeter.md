---
title: JMeter基础
categories: 
- Jmeter
tags:
- Jmeter
- 性能测试
date: 2019-06-20 15:21:34
---

# 性能测试基本概念

## RT -Response time

请求响应时间

从客户端发出请求到得到响应的整个时间

一般包括网络响应时间+server的响应时间。

用户接受准则:

例如2-5-10原则，即按照正常用户体验，如果用户能够在2秒内得到响应，会感觉速度很快，如果2-5秒得到响应，用户感觉系统的响应速度还不多，在5-10秒之内得到响应时，用户会感觉系统的响应速度慢，但是可以接受，超过10秒后还没有响应，用户就会感觉不能够接受。

不同行业不同业务可接受的响应时间是不同的，一般情况，对于在线实时交易：

-   互联网企业：500毫秒以下，例如淘宝业务10毫秒左右。
-   金融企业：1秒以下为佳，部分复杂业务3秒以下。
-   保险企业：3秒以下为佳。
-   制造业：5秒以下为佳。
-   阿里云规范

## **系统处理能力**

系统处理能力是指系统在利用系统硬件平台和软件平台进行信息处理的能力。系统处理能力通过系统每秒钟能够处理的交易数量来评价，交易有两种理解：

- 一是业务人员角度的一笔业务过程；

- 二是系统角度的一次交易申请和响应过程。

前者称为业务交易过程，后者称为事务。两种交易指标都可以评价应用系统的处理能力。一般的建议与系统交易日志保持一致，以便于统计业务量或者交易量。系统处理能力指标是技术测试活动中重要指标。

### **简称**

一般情况下，用以下几个指标来度量：

-   HPS（Hits Per Second） ：每秒点击次数，单位是次/秒。

-   TPS（Transaction per Second）：系统每秒处理事务数，单位是笔/秒。吞吐量。

    不可分割的。要么完全成功，要么完全失败。

-   QPS（Query per Second）：系统每秒处理查询次数，单位是次/秒。

    对于互联网业务中，如果某些业务有且仅有一个请求连接，那么TPS=QPS=HPS，

    一般情况下用TPS来衡量整个业务流程，用QPS来衡量接口查询次数，用HPS来表示对服务器点击请求。

每秒钟处理完的事务次数，一般TPS是对整个系统来讲的。一个应用系统1s能完成多少事务处理，一个事务在分布式处理中，可能会对应多个请求，对于衡量单个接口服务的处理能力，用QPS比较多。

### **标准**

无论TPS、QPS、HPS,此指标是衡量系统处理能力非常重要的指标，越大越好，根据经验，一般情况下：

-   金融行业：1000TPS\~9000TPS，不包括互联网化的活动

-   保险行业：100TPS\~1000TPS，不包括互联网化的活动

-   制造行业：10TPS\~50TPS

-   互联网电子商务：10000TPS\~100000TPS,例如天猫5万TPS

-   互联网中型网站：100TPS\~500TPS

-   互联网小型网站: 50TPS\~100TPS

## 并发用户数量

常见的错误理解:

使用系统的全部用户数量(注册用户)

使用系统的全部在线用户数量

正确理解

并发用户数指在同一时刻内，打开系统并进行业务操作的用户数量，并发用户数对于长连接(数据库连接时长连接，web请求时短连接)系统来说最大并发用户数即是系统的并发接入能力。对于短连接系统而言最大并发用户数并不等于系统的并发接入能力，而是与系统架构、系统处理能力等各种情况相关

http:请求只能由客户端发出，服务端被动响应。

###  简称

Virtual User: VU

### **标准**

一般情况下，性能测试是将系统处理能力容量测出来，而不是测试并发用户数，除了服务器长连接可能影响并发用户数外，系统处理能力不完全受并发用户数影响，可以用最小的用户数将系统处理能力容量测试出来，也可以用更多的用户将系统处理能力容量测试出来。

并发用户数量:

并发用户多少为好？

中小企业:5000用户

## 错误率

###  定义及解释

错误率指系统在负载情况下，失败交易的概率。错误率＝(失败交易数/交易总数)\*100%。稳定性较好的系统，其错误率应该由超时引起，即为超时率。

### **标准**

不同系统对错误率的要求不同，但一般不超出千分之六，即成功率不低于99.4%

## CPU

### **定义及解释** {定义及解释-1 .ListParagraph}

中央处理器是一块超大规模的集成电路，是一台计算机的运算核心（Core）和控制核心（ Control Unit）。它的功能主要是解释计算机指令以及处理计算机软件中的数据。CPU Load: 系统正在干活的多少的度量，队列长度。系统平均负载。

CPU指标主要指的CPU利用率，包括用户态(user)、系统态(sys)、等待态(wait)、空闲态(idle)。CPU 利用率要低于业界警戒值范围之内，即小于或者等于75%;CPU sys%小于或者等于30%, CPU wait%小于或者等于5%。单核CPU也需遵循上述指标要求。

7\*24不允许宕机

##  Memory

内存是计算机中重要的部件之一，它是与CPU进行沟通的桥梁。计算机中所有程序的运行都是在内存中进行的，因此内存的性能对计算机的影响非常大。

现代的操作系统为了最大利用内存，在内存中存放了缓存，因此内存利用率100%并不代表内存有瓶颈，衡量系统内有有瓶颈主要靠SWAP（与虚拟内存交换）交换空间利用率，一般情况下，SWAP交换空间利用率要低于70%,太多的交换将会引起系统性能低下。

Swap解释:

当物理内存接近崩溃时，将物理内存中最近一段时间最少频率使用到的页框移出物理内存，放进该存储空间，这段存储空间我们称之为**交换空间（Swap）**

## 磁盘吞吐量 Disk Throughput.

磁盘吞吐量是指在无磁盘故障的情况下单位时间内通过磁盘的数据量。

磁盘指标主要有每秒读写多少兆，磁盘繁忙率，磁盘队列数，平均服务时间，平均等待时间，空间利用率。其中磁盘繁忙率是直接反映磁盘是否有瓶颈的的重要依据，一般情况下，磁盘繁忙率要低于70%。

## 网络吞吐量 Network Throughput

**10Mbit带宽，每秒传输的字节数1.25MBytes**

网络吞吐量是指在无网络故障的情况下单位时间内通过的网络的数据数量。单位为Byte/s。网络吞吐量指标用于衡量系统对于网络设备或链路传输能力的需求。当网络吞吐量指标接近网络设备或链路最大传输能力时，则需要考虑升级网络设备。

网络吞吐量指标主要有每秒有多少兆流量进出，一般情况下不能超过设备或链路最大传输能力的70%。

# 性能测试基本流程

![image-20230103174138051](pictures/08JMeter/image-20230103174138051.png)

性能测试需求:

1)  最终用户体验，例如2-5-10原则，即按照正常用户体验，如果用户能够在2秒内得到响应，会感觉速度很快，如果2-5秒得到响应，用户感觉系统的响应速度还不多，在5-10秒之内得到响应时，用户会感觉系统的响应速度慢，但是可以接受，超过10秒后还没有响应，用户就会感觉不能够接受。

2)  技术需求, cpu，内存，网络吞吐量，磁盘吞吐量

3)  标准要求:

    竞品分析-

    响应时间

-   互联网企业：500毫秒以下，例如淘宝业务10毫秒左右。

-   金融企业：1秒以下为佳，部分复杂业务3秒以下。

-   保险企业：3秒以下为佳。

-   制造业：5秒以下为佳。

    TPS

-   金融行业：1000TPS\~9000TPS，不包括互联网化的活动

-   保险行业：100TPS\~1000TPS，不包括互联网化的活动

-   制造行业：10TPS\~50TPS

-   互联网电子商务：10000TPS\~100000TPS,例如天猫5万TPS

-   互联网中型网站：100TPS\~500TPS

-   互联网小型网站: 50TPS\~100TPS

    性能测试计划

测试环境，测试需求，测试方法，测试时间表，测试组织架构，测试风险，输入输出文档

性能测试步骤:

![](pictures/08JMeter/image-20230103174223823.png)

性能测试执行

![](pictures/08JMeter/image-20230103174207519.png)

# 性能测试工具

![](pictures/08JMeter/image-20230103174236971.png)

# Jmeter简介

## Jmeter的基本概念

Apache JMeter是Apache组织开发的基于Java的压力测试工具。用于对软件做压力测试，它最初被设计用于Web应用测试，但后来扩展到其他测试领域。 它可以用于测试静态和动态资源，例如静态文件、Java 小服务程序、CGI 脚本、Java 对象、数据库、FTP 服务器， 等等。JMeter 可以用于对服务器、网络或对象模拟巨大的负载，来自不同压力类别下测试它们的强度和分析整体性能。另外，JMeter能够对应用程序做功能/回归测试，通过创建带有断言的脚本来验证你的程序返回了你期望的结果。为了最大限度的灵活性，JMeter允许使用正则表达式创建断言

## 我们为什么使用Jmeter

开源免费还很好用，基于Java编写，可集成到其他系统可拓展各个功能插件

支持接口测试，压力（负载和压力）测试等多种功能，支持录制回放，入门简单

相较于自己编写框架活其他开源工具，有较为完善的UI界面，便于接口调试

多平台支持，可在Linux，Windows，Mac上运行

# Jmeter安装配置及目录结构

## Windows下Jmeter下载安装

[登录官网]( http://jmeter.apache.org/download\_jmeter.cgi) ，根据自己平台，下载对应文件

![](pictures/08JMeter/image-20230103174419336.png)

![](pictures/08JMeter/image-20230103174430456.png)

![](pictures/08JMeter/image-20230103174437006.png)

安装JDK，配置环境变量（具体步骤不做介绍）

将下载Jmeter文件解压，打开/bin/jmeter.bat

![](pictures/08JMeter/image-20230103174557321.png)

![](pictures/08JMeter/image-20230103174657692.png)

## Jmeter的目录结构

SourceURL:file:///home/babyfengfjx/Downloads/JMeter操作手册大全.docx

/bin 目录（常用文件介绍）

examples：目录下包含Jmeter使用实例

ApacheJMeter.jar：JMeter源码包

jmeter.bat：windows下启动文件

jmeter.sh：Linux下启动文件

jmeter.log：Jmeter运行日志文件

jmeter.properties：Jmeter配置文件

jmeter-server.bat：windows下启动负载生成器服务文件

jmeter-server：Linux下启动负载生成器文件

/docs目录——Jmeter帮助文档

/extras目录——提供了对Ant的支持文件，可也用于持续集成

/lib目录——存放Jmeter依赖的jar包，同时安装插件也放于此目录

/licenses目录——软件许可文件，不用管

/printable_docs目录——Jmeter用户手册

# Jmeter简单入门

## 修改语言

![](pictures/08JMeter/image-20230103174825289.png)

## 创建测试计划

![](pictures/08JMeter/image-20230103174843945.png)

## 添加线程组

![](pictures/08JMeter/image-20230103174901916.png)

## 添加sampler设置http请求

![](pictures/08JMeter/image-20230103175006565.png)

## 添加结果树

![](pictures/08JMeter/image-20230103175024887.png)

## 查看结果

![](pictures/08JMeter/image-20230103175048590.png)

# 测试计划

![](pictures/08JMeter/image-20230103175428021.png)

独立运行每个线程组：

再每一组运行结束后启动下一个

Run tearDown Thread Groups after shutdown of main threads：  

主线程关闭运行后拆除线程组，

# 线程组

![](pictures/08JMeter/image-20230104092545954.png)

Delay Thread creation until needed         \
      延迟创建线程，直到该线程开始采样，即之后的任何线程组延迟和加速时间为线程本身。这样可以支持更多的线程，但不会有太多是同时处于活动状态。

 持续时间（秒）：测试计划持续多长时间，会覆盖结束时间。

 启动延迟（秒）：测试计划延迟多长时间启动，会覆盖启动时间。

# Sampler \--HTTP请求

![](pictures/08JMeter/image-20230104092628654.png)

请求方式

请求路径

请求ip

请求协议

请求编码

![](pictures/08JMeter/image-20230104092652159.png)

重定向之前的和之后的请求都会在结果树中显示出来

![](pictures/08JMeter/image-20230104092707205.png)

自动重定向，只会显示重定向之后的地址。

![](pictures/08JMeter/image-20230104092735864.png)

# 结果收集

## 查看结果树

![](pictures/08JMeter/image-20230104092807270.png)

## 表格查看结果

![](pictures/08JMeter/image-20230104092825613.png)

偏离表示服务器响应时间变化、离散程度测量值的大小，或者，换句话说，就是数据的分布。

## 聚合报告

![](pictures/08JMeter/image-20230104092842121.png)

## Summary Report

![](pictures/08JMeter/image-20230104092857441.png)

# Jmeter参数化

## 用户定义的变量

使用配置原件中用户定义的变量可以进行参数化

![](pictures/08JMeter/image-20230104092916211.png)

## 用户参数

使用前置管理器设置用户参数

![](pictures/08JMeter/image-20230104092938544.png)

## 使用csv配置原件

配置元件(Config Element)维护Sampler需要的配置信息，并根据实际的需要会修改请求的内容。我们主要在参数化中用到CSV Data Set Config![](pictures/08JMeter/image-20230104092956569.png)

## 使用随机函数助手

### 生成随机字符串

![](pictures/08JMeter/image-20230104093024788.png)

### 生成随机数字

![](pictures/08JMeter/image-20230104094422449.png)

### 参数引用

![](pictures/08JMeter/image-20230104094437099.png)

# Jmeter断言\--检查点

断言(Assertions)可以用来判断请求响应的结果是否如用户所期望的。它可以用来隔离问题域，即在确保功能正确的前提下执行压力测试。这个限制对于有效的测试是非常有用的。

设置响应内容监听

![](pictures/08JMeter/image-20230104094455677.png)

设置响应头断言

![](pictures/08JMeter/image-20230104094516722.png)

# Jmeter定时器

## 固定定时器

定时器(Timer)负责定义请求之间的延迟间隔

![](pictures/08JMeter/image-20230104094539586.png)

## 高斯定时器

![](pictures/08JMeter/image-20230104094605360.png)

## **同步定时器（Synchronizing Timer）**

![](pictures/08JMeter/image-20230104094622810.png)

# Jmeter配置原件

## HTTP Cookie管理器

默认保存cookie信息

![](pictures/08JMeter/image-20230104094646033.png)

## HTTP信息头管理器

默认保存常规的请求头

![](pictures/08JMeter/image-20230104094701081.png)

## HTTP Cache管理器

默认管理http请求缓存的信息

![](pictures/08JMeter/image-20230104094718002.png)

## HTTP 请求默认值

可以设置http请求的默认值，在单个的请求中不需要再设置其他内容

![](pictures/08JMeter/image-20230104094737517.png)

# Jmeter逻辑控制器

## 简单控制器

作用：这是Jmeter里最简单的一个控制器，它可以让我们组织我们的采样器和其它的逻辑控制器（分组功能），提供一个块的结构和控制，并不具有任何的逻辑控制或运行时的功能。

![](pictures/08JMeter/image-20230104094756958.png)

![](pictures/08JMeter/image-20230104094816885.png)

## 循环控制器

在之前基础上再去循环,线程10,迭代1,一共十次,放到循环控制器可以多次x请求,用于在某一组中对哪些请求循环执行

![](pictures/08JMeter/image-20230104094909398.png)

![](pictures/08JMeter/image-20230104094926170.png)

## 事务控制器

在线程组下创建事务控制器

![](pictures/08JMeter/image-20230104094947187.png)

创建sample 访问首页和注册页面,放到事务中

![](pictures/08JMeter/image-20230104095110900.png)

# Jmeter关联-后置处理器

## 正则表达式提取

![](pictures/08JMeter/image-20230104095127103.png)

**位置1**：名称及注释

**位置2**：正则表达式提取内容的范围。（关于各字段的详细说明请查阅协议的相关说明）

**位置3**：正则表达式提取的相关设置

-   **引用名称**：自己定义的变量名称，后续**请求**将要引用到的**变量名**,如填写的是：user\_id，后面的引用方式是\${user\_id}

-   **正则表达式**：提取内容的正则表达式，相当于lr中的关联函数

-   ()     括起来的部分就是需要提取的，对于你要提的内容需要用小括号括起来

-   .    点号表示匹配任何字符串

-   \+   一次或多次

-   ？   在找到第一个匹配项后停止

-   **模板**：用\$\$引用起来，如果在正则表达式中有多个正则表达式（多个括号括起来的东东），则可以是\$2\$，\$3\$等等，表示解析到的第几个值给user\_id。例如：\$1\$表示匹配到的第一个值

-   **匹配数字**：0代表随机取值，-1代表所有值，此时提取结果是一个数组，其余正整数代表第几个匹配的内容提取出来。如果匹配数字选择的是-1，还可以通过\${user\_id\_1}的方式来取第1个匹配的内容，\${user\_id\_2}来取第2个匹配的内容。 

-   缺省值：正则匹配失败时，取的值

## 使用debug Sampler获取参数的名称

![](pictures/08JMeter/image-20230104095144838.png)

## 参数化获取参数内容

![](pictures/08JMeter/image-20230104095202731.png)

# 元件的执行顺序

![](pictures/08JMeter/image-20230104095219503.png)

顺序:

HTTP Cookie管理器

HTTP Cache Manager

HTTP 信息头管理器

HTTP 请求默认值

用户参数

固定定时器

简单控制器

第一个请求

HTTP Cookie管理器

HTTP Cache Manager

HTTP 信息头管理器

HTTP 请求默认值

用户参数

固定定时器

第二个请求

响应断言

正则表达式提取器

查看结果树

# Jmeter添加插件

Jmeter本身是不能够展示内存，cpu和吞吐量的，但是可以通过添加插件的方式来对jmeter添加这些功能

![](pictures/08JMeter/image-20230104095234652.png)

## 打开Jmeter，查看是否有插件管理器

![](pictures/08JMeter/image-20230104095258849.png)



![](pictures/08JMeter/image-20230104095321272.png)

不一定一次成功

## 场景控制插件

### Stepping Thread Group

![](pictures/08JMeter/image-20230104095409344.png)

### 设置启动场景

![](pictures/08JMeter/image-20230104095421303.png)

## 结果监听插件

![](pictures/08JMeter/image-20230104095440597.png)

![](pictures/08JMeter/image-20230104095453077.png)

![](pictures/08JMeter/image-20230104095511561.png)

![](pictures/08JMeter/image-20230104095533363.png)

![](pictures/08JMeter/image-20230104095917593.png)

![](pictures/08JMeter/image-20230104095932798.png)

![](pictures/08JMeter/image-20230104100053253.png)

# Jmeter脚本录制

## 什么是脚本录制

在进行测试的时候，可能有好多脚本或者界面需要操作测试，并且有些测试链接需要重复多线程高并发进行测试，我们一般会针对这一些操作，进行一个脚本录制，录制好之后，之后测试就可以在这个基础上进行测试。

## Jemeter脚本录制方式

BadBoy脚本录制

使用Jmeter自带的代理服务器进行脚本录制

# 使用Jmeter自带的代理服务器进行脚本录制

## 在测试计划上创建线程组

![](pictures/08JMeter/image-20230104100121708.png)

## 添加录制控制器

![image-20230104100133886](pictures/08JMeter/image-20230104100133886.png)

## 在工作台上添加http代理服务器

![](pictures/08JMeter/image-20230104100207529.png)

## 配置Http代理服务器

![](pictures/08JMeter/image-20230104100221519.png)

## 配置浏览器

### Google浏览器

![](pictures/08JMeter/image-20230104100253418.png)

![](pictures/08JMeter/image-20230104100306738.png)

![](pictures/08JMeter/image-20230104100329839.png)

### 火狐浏览器

![](pictures/08JMeter/image-20230104100347408.png)

![](pictures/08JMeter/image-20230104100355679.png)

## 浏览器请求测试

![](pictures/08JMeter/image-20230104100426913.png)

## 过滤信息

添加如下内容

.\*\\.js.\*\|.\*\\.css.\*\|.\*\\.png.\*\|.\*\\.jpg.\*\|.\*\\.gif.\*\|.\*\\.bmp.\*

![](pictures/08JMeter/image-20230104100447101.png)

![](pictures/08JMeter/image-20230104100500830.png)

# Android手机端脚本录制

## 查看电脑IP

![](pictures/08JMeter/image-20230104100513719.png)

## 配置手机网路连接

![](pictures/08JMeter/image-20230104100534974.png)

![](pictures/08JMeter/image-20230104100600278.png)

## 手机访问app

![](pictures/08JMeter/image-20230104100620418.png)

![](pictures/08JMeter/image-20230104100635987.png)

## 模拟登陆操作

![](pictures/08JMeter/image-20230104100650698.png)

![](pictures/08JMeter/image-20230104100705102.png)

## 执行结束之后，停止脚本录制

![](pictures/08JMeter/image-20230104100722577.png)

## 脚本测试-线程组设置10个线程分别请求10次

![](pictures/08JMeter/image-20230104100737832.png)

## 查看结果树

![](pictures/08JMeter/image-20230104100757522.png)

# BadBoy脚本录制

## 安装badboy脚本软件

傻瓜式安装即可

## 打开badboy软件

![](pictures/08JMeter/image-20230104100818008.png)

## badboy脚本录制

点击录制按钮进行脚本录制，完成打开搜狗搜索，搜索zhiyuan0932操作，然后停止，回放，（回放的时候，会因为编码原因导致乱码，需要手动调乱码问题）

![](pictures/08JMeter/image-20230104100832454.png)

![](pictures/08JMeter/image-20230104100856535.png)

![](pictures/08JMeter/image-20230104100908487.png)

![](pictures/08JMeter/image-20230104100917874.png)

## 添加验证点

验证点的作用就是验证脚本是否按照我们测试的思路执行，判断脚本执行过程中是否存现问题

![](pictures/08JMeter/image-20230104100933098.png)

## badboy参数化

所谓参数化，是指请求的某个参数提前设定多个值，在具体请求的时候，去获取提前设定的值，不同的业务场景设置的参数不一致。

![](pictures/08JMeter/image-20230104100952874.png)

![](pictures/08JMeter/image-20230104101000440.png)

![](pictures/08JMeter/image-20230104101007977.png)

![](pictures/08JMeter/image-20230104101015465.png)

## 导出Jmeter脚本

![](pictures/08JMeter/image-20230104101031073.png)

## 在Jmeter中导入badboy生成的脚本，验证测试

![](pictures/08JMeter/image-20230104101040623.png)

## badboy并发测试

本身是能做接口测试和压力测试的,并且能兼容jemeter

选择tools run background

![](pictures/08JMeter/image-20230104101050000.png)

## badboy测试报告

在badboy\--\>view\-\--\>report下可以看到测试报告

![](pictures/08JMeter/image-20230104101059830.png)

# Jmeter数据库压力测试

## 先配置jdbc驱动

![](pictures/08JMeter/image-20230104101134264.png)

添加上jar后,在测试计划添加配置原件,jdbc进行配置

![](pictures/08JMeter/image-20230104101200409.png)

添加操作数据库请求 samplerjdbcRequest

## 数据库普通查询操作 

![](pictures/08JMeter/image-20230104101354190.png)

## Jmeter预编译参数查询方式

![](pictures/08JMeter/image-20230104101402444.png)

## ForEach控制器循环请求

![](pictures/08JMeter/image-20230104101410482.png)

## JDBC预编译方式修改数据

### 配置csv文件

![](pictures/08JMeter/image-20230104101419180.png)

### 修改数据

![](pictures/08JMeter/image-20230104101428004.png)

# Jmeter压测接口的性能优化

简介：讲解Jmeter压测减少资源使用的一些建议，即压测结果更准确

1、使用非GUI模式：jmeter -n -t test.jmx -l result.jtl

2、少使用Listener， 如果使用-l参数，它们都可以被删除或禁用。

3、在加载测试期间不要使用"查看结果树"或"查看结果"表监听器，只能在脚本阶段使用它们来调试脚本。

4、包含控制器在这里没有帮助，因为它将文件中的所有测试元素添加到测试计划中。

5、不要使用功能模式,使用CSV输出而不是XML

6、只保存你需要的数据,尽可能少地使用断言

7、如果测试需要大量数据，可以提前准备好测试数据放到数据文件中，以CSV Read方式读取。

8、用内网压测，减少其他带宽影响压测结果

9、如果压测大流量，尽量用多几个节点以非GUI模式向服务器施压

# Linux下运行jmeter压测

我们在做测试的时候，有时候要运行很久，公司用的测试服务器一般都是linux，就可以运行在linux下面，linux下面不能像windows一样有图形化界面，那怎么运行脚本呢。

##  解压JDK8到Linux

tar -xvf jdk-8u171-linux-i586.tar.gz -C /usr/local

mv jdk-8u171-linux-i586 java

![](pictures/08JMeter/image-20230104101441890.png)

## 配置环境变量

\[root\@localhost /\]\# vim /etc/profile

+----------------------------------+
| JAVA\_HOME=/usr/local/java/      |
|                                  |
| CLASSPATH=\$JAVA\_HOME/lib/      |
|                                  |
| PATH=\$PATH:\$JAVA\_HOME/bin     |
|                                  |
| export PATH JAVA\_HOME CLASSPATH |
+----------------------------------+

## 刷新配置文件

source /etc/profile

java -version

## 解压并安装jmeter4.0

## 配置jmeter环境变量

### 解压jmeter到usr/local

![](pictures/08JMeter/image-20230104101517327.png)

### 启动Jmeter

![](pictures/08JMeter/image-20230104101524299.png)

### 打开系统配置文件

vim /etc/profile

### 配置环境变量

+------------------------------------+
| JMETER\_HOME=/usr/local/jmeter/    |
|                                    |
| CLASSPATH=\$JMETER\_HOME/lib/      |
|                                    |
| PATH=\$PATH:\$JMETER\_HOME/bin     |
|                                    |
| export PATH JMETER\_HOME CLASSPATH |
+------------------------------------+

### 刷新系统配置文件

source /etc/profile

### 执行jmeter -?

![](pictures/08JMeter/image-20230104101538473.png)

### 将windows上写好的脚本导入到Linux

### 进行测试

非GUI界面，压测参数讲解

-h 帮助

-n 非GUI模式

-t 指定要运行的 JMeter 测试脚本文件

-l 记录结果的文件 每次运行之前，(要确保之前没有运行过,即xxx.jtl不存在，不然报错)

-r Jmter.properties文件中指定的所有远程服务器

-e 在脚本运行结束后生成html报告

-o 用于存放html报告的目录（目录要为空，不然报错）

jmeter -n --t a.jmx -l res.jtl

![](pictures/08JMeter/image-20230104101551634.png)

## 将测试结果导入到Jmeter中查看结果数据

![](pictures/08JMeter/image-20230104101600808.png)

# Jmeter压测生成HTML测试报告

创建文件夹

mkdir result

指令执行

jmeter -n -t baidu.jmx -l res.jtl -e -o /result

# Jmeter HTML报告dashboard讲解

## **Test and Report informations**

![](pictures/08JMeter/image-20230104101620957.png)

+----------------------------+
| Source file：jtl文件名     |
|                            |
| Start Time ：压测开始时间  |
|                            |
| End Time ：压测结束时间    |
|                            |
| Filter for display：过滤器 |
|                            |
| Lable:sampler采样器名称    |
+----------------------------+

## APDEX(Application performance Index)

![](pictures/08JMeter/image-20230104101631888.png)

+----------------------------------------------------------------+
| apdex:应用程序性能指标,范围在0\~1之间，1表示达到所有用户均满意 |
|                                                                |
| T(Toleration threshold)：可接受阀值                            |
|                                                                |
| F(Frustration threshold)：失败阀值                             |
+----------------------------------------------------------------+

## Requests Summary

![](pictures/08JMeter/image-20230104101644480.png)OK:成功率

KO:失败率

## Statistics 统计数据

![](pictures/08JMeter/image-20230104101652991.png)

lable:sampler采样器名称

samples:请求总数，并发数*循环次数

KO:失败次数

Error%:失败率

Average:平均响应时间

Min:最小响应时间

Max:最大响应时间

90th pct: 90%的用户响应时间不会超过这个值（关注这个就可以了）

95th pct: 95%的用户响应时间不会超过这个值

99th pct: 99%的用户响应时间不会超过这个值 (存在极端值)

throughtput:Request per Second吞吐量 qps

received:每秒从服务器接收的数据量

send：每秒发送的数据量

## 错误信息统计

![](pictures/08JMeter/image-20230104101704720.png)

# Jmeter图形化HTML压测报告Charts报表讲解

## Over Time（随着时间的变化）

![](pictures/08JMeter/image-20230104101717927.png)

Response Times Over Time：响应时间变化趋势

Response Time Percentiles Over Time (successful responses)：最大，最小，平均，用户响应时间分布

Active Threads Over Time：并发用户数趋势

Bytes Throughput Over Time：每秒接收和请求字节数变化，蓝色表示发送，黄色表示接受

Latencies Over Time：平均响应延时趋势

Connect Time Over Time	：连接耗时趋势

## Throughput

Hits Per Second (excluding embedded resources):每秒点击次数

Codes Per Second (excluding embedded resources)：每秒状态码数量

Transactions Per Second：即TPS，每秒事务数

Response Time Vs Request：响应时间和请求数对比

Latency Vs Request：延迟时间和请求数对比

## Response Times

Response Time Percentiles：响应时间百分比

![](pictures/08JMeter/image-20230104101732576.png)

Response Time Overview：响应时间概述

![](pictures/08JMeter/image-20230104101739594.png)

Time Vs Threads：活跃线程数和响应时间

![](pictures/08JMeter/image-20230104101746321.png)

Response Time Distribution：响应时间分布图

![](pictures/08JMeter/image-20230104101754968.png)

# Windows jmeter unGUI测试

## 设置环境变量

![](pictures/08JMeter/image-20230104101805282.png)

## 无界面测试

![](pictures/08JMeter/image-20230104101812589.png)

# 分布式压测介绍

普通压测：

单台机可以对目标机器产生的压力比较小，受限因素包括CPU，网络，IO等

分布式压测：

利用多台机器向目标机器产生压力，模拟几万用户并发访问

![](pictures/08JMeter/image-20230104101821321.png)

# Jmeter分布式压测原理

![](pictures/08JMeter/image-20230104101829831.png)

1、总控机器的节点master，其他产生压力的机器叫"肉鸡" server

2、master会把压测脚本发送到 server上面

3、执行的时候，server上只需要把jmeter-server打开就可以了，不用启动jmeter

4、结束后，server会把压测数据回传给master,然后master汇总输出报告

5、配置详情

# Jmeter分布式压测实战

## Slave机器设置

第一步:禁用ssl

到slave Jmeter的jmeter.properties文件中修改

server.rmi.ssl.disable=true

第二步:修改slave Jmeter的远程连接端口

server\_port=8899 表示master机器要远程连接的端口

第三步:启动slave Jmeter

./jmeter-server

./jmeter-server -Djava.rmi.server.hostname=192.168.179.128

第四步:关闭防火墙

service iptables stop

## 设置Master设备

关闭防火墙

service iptables stop

到slave Jmeter的jmeter.properties文件中修改

server.rmi.ssl.disable=true

修改remote\_hosts=127.0.0.1

为remote\_hosts=192.168.179.128:9999

GUI方式启动

![](pictures/08JMeter/image-20230104101846545.png)

无GUI方式启动

Jmeter -n -t baidu.jmx -r -l result.jtl -e -o result

![](pictures/08JMeter/image-20230104101853765.png)

# 并发用户和TPS关系

简单计算:

在线用户数量(日活量)：

在做性能测试的时候，传统方式都是用并发用户数来衡量系统的性能，觉得系统能支撑的并发用户数越多，系统的性能就越好；同时对TPS不是非常理解，也根本不知道它们之间的关系，因此非常有必要进行解释。因为TPS模式（吞吐量模式）是一种更好的方式衡量服务端系统的能力。

## Vu和TPS换算

简单例子:

在术语中解释了TPS是每秒事务数，但是事务时要靠虚拟用户做出来的，

假如1个虚拟用户在1秒内完成1笔事务，那么TPS明显就是1；

如果某笔业务响应时间是1ms,那么1个用户在1秒内能完成1000笔事务，TPS就是1000了；

如果某笔业务响应时间是1s,那么1个用户在1秒内只能完成1笔事务，要想达到1000TPS，至少需要1000个用户；

## 如何获取Vu和TPS

并发用户数(Vu)获取新系统：没有历史数据作参考，只能通过业务部门进行评估。旧系统：对于已经上线的系统，可以选取高峰时刻，在一定时间内使用系统的人数，这些人数认为属于在线用户数，并发用户数取10%就可以了，例如在半个小时内，使用系统的用户数为10000，那么取10%作为并发用户数基本就够了。

其他计算方式：根据pv计算

PV(访问量)：即Page View, 即页面浏览量或点击量，用户每次刷新即被计算一次。

假设:pv数是80w

（1）平均值情况：80w个用户在时间上均匀地发起请求。那么并发用户数为800000/24\*60\*60=9.25并发/s。

 （2）80\~20原则：根据统计学原理，采用80\~20原则计算并发用户数。\
             800000\*0.8/（24\*60\*60\*0.2）=37并发/s

TPS获取新系统：没有历史数据作参考，只能通过业务部门进行评估。旧系统：对于已经上线的系统，可以选取高峰时刻，在5分钟或10分钟内，获取系统每笔交易的业务量和总业务量，按照单位时间内完成的笔数计算出TPS，即业务笔数/单位时间。

##  总结

-   系统的性能由TPS决定，跟并发用户数没有多大关系。

-   系统的最大TPS是一定的（在一个范围内），但并发用户数不一定，可以调整。

-   建议性能测试的时候，不要设置过长的思考时间，以最坏的情况下对服务器施压。

-   一般情况下，大型系统（业务量大、机器多）做压力测试，10000～50000个用户并发，中小型系统做压力测试，5000个用户并发比较常见。

# 性能指标

## 中间件指标 

### 定义及解释

常用的中间件例如Tomcat、Weblogic等指标主要包括JVM, ThreadPool, JDBC,具体如下：

| **一级指标** | **二级指标**           | **解释**                   | **备注** |      |
| ------------ | ---------------------- | -------------------------- | -------- | ---- |
| GC           | GC频率                 | java虚拟机垃圾部分回收频率 |          |      |
|              | Full GC频率            | java虚拟机垃圾完全回收频率 |          |      |
|              | Full GC平均时长        | 用于垃圾完全回收的平均时长 |          |      |
|              | Full GC最大时长        | 用于垃圾完全回收的最大时长 |          |      |
|              | 堆使用率               | 堆使用率                   |          |      |
| ThreadPool   | Active Thread Count    | 活动的线程数               |          |      |
|              | Pending User Request   | 处于排队的用户请求个数     |          |      |
| JDBC         | JDBC Active Connection | JDBC活动连接数             |          |      |

### 标准

-   当前正在运行的线程数不能超过设定的最大值。一般情况下系统性能较好的情况下，线程数最小值设置50和最大值设置200比较合适。

-   当前运行的JDBC连接数不能超过设定的最大值。一般情况下系统性能较好的情况下，JDBC最小值设置50和最大值设置200比较合适。

-   ＧＣ频率不能频繁，特别是FULL GC更不能频繁，一般情况下系统性能较好的情况下，JVM最小堆大小和最大堆大小分别设置1024M比较合适。

## 数据库指标

### 定义及解释

常用的数据库例如ＭySQL指标主要包括SQL、吞吐量、缓存命中率、连接数等，具体如下：

| **一级指标** | **二级指标**        | **单位** | **解释**           |      |
| ------------ | ------------------- | -------- | ------------------ | ---- |
| SQL          | 耗时                | 微秒     | 执行SQL耗时        |      |
| 吞吐量       | QPS                 | 个       | 每秒查询次数       |      |
|              | TPS                 | 个       | 每秒事务次数       |      |
| 命中率       | Key Buffer命中率    | 百分之   | 索引缓冲区命中率   |      |
|              | InnoDB Buffer命中率 | 百分之   | InnoDB缓冲区命中率 |      |
|              | Query Cache命中率   | 百分之   | 查询缓存命中率     |      |
|              | Table Cache命中率   | 百分之   | 表缓存命中率       |      |
|              | Thread Cache命中率  | 百分之   | 线程缓存命中率     |      |
| 锁           | 等待次数            | 次       | 锁等待次数         |      |
|              | 等待时间            | 微秒     | 锁等待时间         |      |

-------------- --------------------- ---------- -------------------- --
-------------- --------------------- ---------- -------------------- --

###  标准

-   SQL耗时越小越好，一般情况下微秒级别。

-   命中率越高越好，一般情况下不能低于95%。

-   锁等待次数越低越好，等待时间越短越好。

## 前端指标

### 定义及解释

前端指标主要包括页面展示和网络所花的时间，具体如下：

| **一级指标** | **二级指标**   | **单位** | **解释**                                                     | **备注** |      |
| ------------ | -------------- | -------- | ------------------------------------------------------------ | -------- | ---- |
| 页面展示     | 首次显示时间   | 毫秒     | 在浏览器地址栏输入URL按回车到用户看到网页的第一个视觉标志为止 |          |      |
|              | OnLoad事件时间 | 毫秒     | 浏览器触发onLoad事件的时间，当原始文档和所有引用的内容完全下载后才会触发这个事件 |          |      |
|              | 完全载入的时间 | 毫秒     | 所有onLoad JavaScript 处理程序执行完毕，所有动态的或延迟加载的内容都通过这些处理程序触发的时间 |          |      |
| 页面数量     | 页面大小       | KB       | 整个页面大小                                                 |          |      |
|              | 请求数量       | 次       | 从网站下载资源时所有网络请求的总数，尽量少                   |          |      |
| 网络         | DNS时间        | 毫秒     | DNS查找时间                                                  |          |      |
|              | 连接时间       | 毫秒     | 连接时间就是浏览器与Web服务器建立TCP/IP连接的时间            |          |      |
|              | 服务器时间     | 毫秒     | 服务器处理时间                                               |          |      |
|              | 传输时间       | 毫秒     | 内容传输所用时间                                             |          |      |
|              | 等待时间       | 毫秒     | 等待某个资源释放的时间                                       |          |      |

### 标准

-   页面要尽可能小及压缩。

-   页面展示和花费时间越短越好。

##  稳定性指标

### 定义及解释

最短稳定时间：系统按照最大容量的80%或标准压力（系统的预期日常压力）情况下运行，能够稳定运行的最短时间。一般来说，对于正常工作日（8小时）运行的系统，至少应该能保证系统稳定运行８小时以上。对于7\*24运行的系统，至少应该能够保证系统稳定运行24小时以上。如果系统不能稳定的运行，上线后，随着业务量的增长和长时间运行，将会出现性能下降甚至崩溃的风险。

### 标准

-   TPS曲线稳定，没有大幅度的波动。

-   各项资源指标没有泄露或异常情况。

# 性能分析

性能分析的前提除了需要丰富的性能测试监控，还要了解操作系统、中间件(tomcat)、数据库(mysql oracle sqlserver)、开发等。

## 流程

-   很多情况下压测流量并没有完全进入到后端（服务端），在网络接入层（云化的架构比如：SLB/WAF/高防IP，甚至是CDN/全站加速等）可能就会出现由于各种规格（带宽、最大连接数、新建连接数等）限制或者因为压测的某些特征符合CC和DDoS的行为而触发了防护策略导致压测结果达不到预期。

-   接着看关键指标是否满足要求，如果不满足，需要确定是哪个地方有问题，一般情况下，服务器端问题可能性比较大，也有可能是客户端问题（这种情况非常小）。

-   对于服务器端问题，需要定位的是硬件相关指标，例如CPU，Memory, Disk I/O, Network I/O, 如果是某个硬件指标有问题，需要深入的进行分析。

-   如果硬件指标都没有问题，需要查看中间件相关指标，例如：线程池、连接池、GC等，如果是这些指标问题，需要深入的 分析。

-   如果中间件相关指标没问题，需要查看数据库相关指标，例如：慢查SQL，命中率，锁、参数设置。

-   如果以上指标都正常，应用程序的算法、缓冲、缓存、同步或异步可能有问题，需要具体深入的分析。

    ![](pictures/08JMeter/image-20230104101937127.png)可能瓶颈点

###  **硬件/规格上的瓶颈**

一般指的是CPU、内存、磁盘I/O 方面的问题，分为服务器硬件瓶颈、网络瓶颈（对局域网可以不考虑）。

### **中间件上的性能瓶颈**

一般指的是应用服务器、web 服务器等应用软件，还包括数据库系统。例如：中间件weblogic/tomcat平台上配置的JDBC连接池的参数设置不合理，造成的瓶颈。

### **应用程序上的性能瓶颈**

一般指的是开发人员开发出来的应用程序。例如，JVM参数不合理，容器配置不合理，慢SQL，数据库设计不合理，程序架构规划不合理，程序本身设计有问题（串行处理、请求的处理线程不够、无缓冲、无缓存、生产者和消费者不协调等），造成系统在大量用户方位时性能低下而造成的瓶颈。

###  **操作系统上的性能瓶颈**

一般指的是windows、UNIX、Linux等操作系统。例如，在进行性能测试，出现物理内存不足时，虚拟内存设置也不合理，虚拟内存的交换效率就会大大降低，从而导致行为的响应时间大大增加，这时认为操作系统上出现性能瓶颈。

### **网络设备上的性能瓶颈**

一般指的是防火墙、动态负载均衡器、交换机等设备。当前更多的云化服务架构使用的网络接入产品：包括但不限于SLB/WAF/高防IP/CDN/全站加速等等。例如，在动态负载均衡器上设置了动态分发负载的机制，当发现某个应用服务器上的硬件资源已经到达极限时，动态负载均衡器将后续的交易请求发送到其他负载较轻的应用服务器上。在测试时发现，动态负载均衡器没有起到相应的作用，这时可以认为网络瓶颈。

## 方法

### **CPU**

CPU资源利用率很高的话，需要看CPU消耗User,Sys,Wait那种状态下。

-   如果CPU User非常高，需要查看消耗在哪个进程，可以用top(linux)命令看出，接着用top --H --p \<pid\>看哪个线程消耗资源高，如果是java应用，就可以用jstack看出此线程正在执行的堆栈，看资源消耗在哪个方法上，查看源代码就知道问题所在；如果是c++应用，可以用gprof性能工具进行分析。

-   如果CPU Sys非常高，可以用strace(linux)看系统调用的资源消耗及时间。

-   如果CPU Wait非常高，考虑磁盘读写了，可以通过减少日志输出、异步或换速度快的硬盘。

###  **Memory**

操作系统未了最大化利用内存，一般都设置大量的cache,因此，内存利用率高达99%并不是问题，内存的问题主要看某个进程占用的内存是否非常大以及是否有大量的swap(虚拟内存交换)。

###  **磁盘I/O**

磁盘I/O一个最显著的指标是繁忙率，可以通过减少日志输出、异步或换速度快的硬盘。

###  **网络I/O**

网络I/O主要考虑传输内容大小，不能超过硬件网络传输的最大值70%，可以通过压缩、减少内容大小、在本地设置缓存以及分多次传输等。

### **JVM**

jvm主要分析GC/FULL GC是否频繁，以及垃圾回收的时间，可以用jstat命令来查看，对于每个代大小以及GC频繁，通过jmap将内存dump,再借助工具HeapAnalyzer来分析哪地方占用的内存较高以及是否有内存泄漏可能。简单点可以使用APM工具，比如阿里云ARMS，下同。

### **线程池**

如果线程不够用，可以通过参数调整，增加线程；对于线程池中的线程设置比较大的情况，还是不够用可能的原因是：某个线程被阻塞来不及释放，可能在等锁、方法耗时较长、数据库等待时间很长等原因导致，需要进一步分析才能定位。

###  **JDBC连接池**

连接池不够用的情况下，可以通过参数进行调整增加；但是对于数据库本身处理很慢的情况下，调整没有多大的效果，需要查看数据库方面以及因代码导致连接未释放的原因。

###  **SQL**

SQL效率低下也是导致性能差的一个非常重要的原因，可以通过查看执行计划看SQL慢在哪里，一般情况，SQL效率低下原因主要有：

| ***\*类别\**** | ***\*子类\****             | ***\*表达式或描述\****                                   | ***\*原因\****                                               |
| -------------- | -------------------------- | -------------------------------------------------------- | ------------------------------------------------------------ |
| 索引           | 未建索引                   |                                                          | 产生全表扫描                                                 |
|                | 未利用索引                 | substring(card_no,1,4)=′5378′                            | 产生全表扫描                                                 |
|                |                            | amount/30< 1000                                          | 产生全表扫描                                                 |
|                |                            | convert(char(10),date,112)=′19991201′                    | 产生全表扫描                                                 |
|                |                            | where salary<>3000                                       | 产生全表扫描                                                 |
|                |                            | name like ‘%张’                                          | 产生全表扫描                                                 |
|                |                            | first_name + last_name =’beill cliton’                   | 产生全表扫描                                                 |
|                |                            | id_no in(′0′,′1′)                                        | 产生全表扫描                                                 |
|                |                            | select id from t where num=@num                          | 有参数也会产生全表扫描                                       |
|                | 使用效能低的索引           | oder by 非聚族索引                                       | 索引性能低                                                   |
|                |                            | username=’张三’ and age>20                               | 字符串索引低于整形索引                                       |
|                |                            | 表中列与空NULL值                                         | 索引性能低                                                   |
|                |                            | 尽量不要使用IS NULL或IS NOT NULL                         | 索引性能低                                                   |
| 数据量         | 所有数据量                 | select *                                                 | 很多列产生大量数据                                           |
|                |                            | select id,name                                           | 表中有几百万行，产生大量数据                                 |
|                | 嵌套查询                   | 先不过滤数据，后过滤数据                                 | 产生大量无用的数据                                           |
|                | 关联查询                   | 多表进行关联查询，先过滤掉小部分数据，在过滤大部分数据   | 大量关联操作                                                 |
|                | 大数据量插入               | 一次次插入                                               | 产生大量日志，消耗资源                                       |
| 锁             | 锁等待                     | update account set banlance=100 where id=10              | 产生表级锁，将会锁住整个表                                   |
|                | 死锁                       | A:update a;update b;B:update b;update a;                 | 将会产生死锁                                                 |
|                | 游标                       | Cursor Open cursor,fetch;close cursor                    | 性能很低                                                     |
|                | 临时表                     | create tmp table 创建临时表                              | 产生大量日志                                                 |
|                | drop table                 | 删除临时表                                               | 需要显示删除，避免系统表长时间锁定                           |
| 其他           | exist 代替 IN              | select num from a where num in(select num from b)        | in会逐个判断,exist有一条就结束                               |
|                | exist 代替select count(*)  | 判断记录是否存在                                         | count(*)将累加计算，exist有就结束                            |
|                | between 代替 IN            | ID in(1,2,3)                                             | IN逐个判断，between是范围判断                                |
|                | left outer join 代替Not IN | select ID from a where ID not in(select b.Mainid from b) | NOT IN逐个判断，效率非常低                                   |
|                | union all 代替union        | select ID from a union select id from b union            | 删除重复的行，可能会在磁盘进行排序而union all只是简单的将结果并在一起 |
|                | 常用SQL尽量用绑定变量方法  | insert into A(ID) values(1)                              | 直接写SQL每次都要编译，用绑定变量的方法只编译一次，下次就可以用了 |
