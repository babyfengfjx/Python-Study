import paramiko
import os
from time import sleep
transport = paramiko.Transport('139.9.251.57',22)
transport.connect(username='root',password='r@89000696!')
sftp = paramiko.SFTPClient.from_transport(transport)
path= '/fjx'
try :
    sftp.stat(path)
    print('文件夹存在')
except FileNotFoundError:
    print('文件夹不存在')
    sftp.mkdir(path)
    print('文件夹已经创建')

