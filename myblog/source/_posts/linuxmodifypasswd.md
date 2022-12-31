title: 通过live系统修改linux的密码
categories:
  - linux
tags:
  - linux
date: 2022-12-31 10:11:34
---
> 核心思想就是通过live系统进入一个临时系统，然后通过chroot到物理系统的根目录，进行相关密码重置工作。

# Step One:进入live系统

![1.gif](https://storage.deepin.org/thread/202205201618318171_1.gif)
**很多人可能还不知道如何进入deepin的live系统，可以看上面动图的操作，也是非常简单：**

1. 首先准备好一个装有deepin镜像的启动U盘（推荐使用ventoy）；
2. 直接走装镜像的路子,启动到系统安装界面；
3. 唯一区别是在grub安装界面的时候，不要选择任何选项，而是按一下键盘上的 **“E”** 按键（如果是非EFI启动，可能需要按TAB键）；
4. 按过之后就会出现下图的编辑界面，通过上下左右按键移动到下方红框标识处，删除 **“cd-installer”** 内容；

   ![2.png](https://storage.deepin.org/thread/20220520162047272_2.png)
5. 然后直接按键盘上F10按键，接下来就会直接进入live系统界面了。
6. 进入live系统后是如下界面的样子（下图是V20.6的镜像）：

> 特别提醒：在live系统下长时间也会自动锁屏了，如果你也遇到了锁屏发现没有密码无法进入系统，可能你需要重新来一次，此时可以直接通过ctrl+alt+F2 进入TTY，然后在TTY界面设置密码即可：``sudo passwd uos``,然后再切回来用设置的密码登录即可。

![3.png](https://storage.deepin.org/thread/202205201621386209_3.png)

# Step Two:切换chroot目录

1. 在live系统中打开文件管理器；
2. 找到根目录所在分区（如我这里的Roota）;
3. 进入目录后，右键点击空白处，打开终端；
4. 然后输入 ``sudo chroot ./``;
5. 回车后，我们就切换到原系统的根目录了。

![qiehuanchroot.gif](https://storage.deepin.org/thread/202206011317339861_qiehuanchroot.gif)

# Step Three:修改用户密码

1. 确认你要修改密码的用户名，比如我这里要修改 ‘babyfengfjx’ 用户的密码；
2. 在上面的终端里，接着执行：``passwd babyfengfjx``    -- 这里记得换成自己的用户名；
3. 按照提示设置新的密码即可。

![genghuanmima.gif](https://storage.deepin.org/thread/202206011319569555_genghuanmima.gif)

# Step Four:重启系统，使用新的密码登录

完成上述操作后，即可重启系统，使用刚设置的新密码进行登录了。