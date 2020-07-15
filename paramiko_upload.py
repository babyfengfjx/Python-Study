import paramiko
import os
from time import sleep
transport = paramiko.Transport('139.9.251.57',22)
transport.connect(username='root',password='r@89000696!')
sftp = paramiko.SFTPClient.from_transport(transport)
localpath = r'c:\TestFJX'
# localpath = localpath #本地文件不可以直接通过文件属性复制，会报错，最好直接手动编辑
dir_name = localpath.split('\\')[-1]
remotepath =r'/' #文件路径一定要精确到文件名，可以不同名，但一定要到文件名
remotepath = os.path.join(remotepath,dir_name)
print(remotepath)

def rm_dir():#递归删除文件夹范例
    """
    递归删除文件夹代码范例
    """
    #第一种：
    def local_rm(dirpath):
        if os.path.exists(dirpath):
            files = os.listdir(dirpath)
            for file in files:
                filepath = os.path.join(dirpath, file).replace("\\", '/')
                if os.path.isdir(filepath):
                    local_rm(filepath)
                else:
                    os.remove(filepath)
            os.rmdir(dirpath)

    # 第二种
    # import shutil
    # shutl.rmtree(dir_path)

def upload ():
    """
    该函数提供文件上传功能，参数都没有直接从外面传，暂时先用着。
    """

    def del_dir (remotepath):
        """
        通过使用SSHClient实例来连接Linux系统，然后发送删除指令来操作文件夹删除
        """

        # 实例化SSHClient
        client = paramiko.SSHClient()

        # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接SSH服务端，以用户名和密码进行认证
        client.connect(hostname='139.9.251.57', port=22, username='root', password='r@89000696!')

        # 打开一个Channel并执行命令
        stdin, stdout, stderr = client.exec_command(f'rm -rf {remotepath} ')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
        print('文件夹删除成功伙计！')

        # 打印执行结果
        print(stdout.read().decode('utf-8'))

        # 关闭SSHClient
        client.close()



    del_dir(remotepath)
    try:
        sftp.mkdir(remotepath)
        print('文件夹已创建！')
    except:
        print('文件夹已存在！')

    print('开始上传……')
    new_localpath = localpath
    def put_file(new_localpath,remotepath):#函数中要使用变量的话一定要通过参数传递进来，不要直接在函数体中使用全局变量，这样在函数中改变局部变量的时候就会出问题，没办法去改变他。

        for file_name in os.listdir(new_localpath):

            sub_remotepath = os.path.join(remotepath,file_name)
            sub_remotepath = sub_remotepath.replace('\\','/') #Linux中路径要替换反斜杠，与Windows的路径是不同的
            if os.path.isdir(sub_remotepath):

                new_localpath = os.path.join(new_localpath,file_name)

                print(sub_remotepath)
                try:
                    sftp.mkdir(sub_remotepath) #先创建文件夹，再来改变远程路径，然后再递归调用即可。
                except:
                    print(f'文件夹{file_name}已存在')
                remotepath = sub_remotepath.replace('\\', '/')
                put_file(new_localpath,remotepath)
            else:
                sub_localpath = os.path.join(new_localpath,file_name)
                print(sub_localpath)
                print(sub_remotepath)
                sftp.put(sub_localpath,sub_remotepath)
                print(f'{file_name}已经上传……')
    put_file(new_localpath,remotepath)
    print('上传结束……')
if __name__ == "__main__":
    upload()