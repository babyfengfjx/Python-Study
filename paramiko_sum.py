import paramiko
import sys


user = "root"
pwd = "r@89000696!"



# 上传文件
def sftp_upload_file(server_path, local_path):
    try:
        t = paramiko.Transport((ip, 22))
        t.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_path, server_path)
        t.close()
    except Exception as  e:
        print(e)

# 下载文件
def sftp_down_file(server_path, local_path):
    try:
        t = paramiko.Transport((ip, 22))
        t.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(server_path, local_path)
        t.close()
    except Exception as e:
        print(e)

# 连接
def ssh_conn(ip, cmd):

    ssh = paramiko.SSHClient()
    # 允许连接不在known_hosts文件上的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(ip, 22, user, pwd)
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command(cmd)
    # 获取结果
    print(10 * "-", 'start', 10 * "-")
    for line in stdout:
        res=(line.strip('\n').split())
        print(res)
    else:
        print(stdout)
    print(10 * "-", 'end', 10 * "-")

def menu():
    print('''
    * - - - - - - - - - - - - - - - - - *     
                   菜单                     
                1>上传文件                 
                2>下载文件
                3>执行命令
                4>退出
    * - - - - - - - - - - - - - - - - - *
    ''')

    choice = int(input('请输入你要执行的操作：\n'))
    if choice == 1:
        src = input('请输入原路径：\n')
        dest = input('请输入目标路径：\n')
        sftp_upload_file(src, dest)
    elif choice == 2:
        src = input('请输入原路径：\n')
        dest = input('请输入目标路径：\n')
        sftp_down_file(src, dest)
    elif choice == 3:
        while True:
            cmd = input('请输入要执行的命令：\n')
            if cmd == 'exit':
                sys.exit()
            ssh_conn(ip, cmd)
    else:
        sys.exit()


if __name__ == '__main__':
    ip = input('请输入目标ip：\n')
    while True:
        menu()