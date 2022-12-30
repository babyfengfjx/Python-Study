import paramiko
from time import sleep

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname='172.16.158.128', username='deepin', password='1')
# stdin, stdout, stderr = client.exec_command("sudo cat /var/log/kern.log",get_pty=True)
# # stdin, stdout, stderr = client.exec_command("inxi -F")
# print(stdout.read().decode('utf8'))
# client.close()

# 开启交互式会话
channel = client.invoke_shell()
channel.send('inxi -F\n')
output = ''
while True:
    sleep(0.1)
    output = output + channel.recv(1024).decode('utf8')
    # output.decode('utf8')
    # print(output.decode('utf8'))
    output = output.strip()
    if output.endswith("$"):  # 可以通过结尾来判断执行状态再做一次命令发起
        break

print(output)
channel.send('sudo systemctl reboot -i\n')  # 可以直接重启远程服务器
while True:
    res = channel.recv(1024).decode('utf8')
    if res.strip().endswith('请输入密码:'):
        channel.send('1\n')
        sleep(0.2)
        break
client.close()
