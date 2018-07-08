#-*- coding: utf-8 -*-
import re
import paramiko          #引入ssh模块，该模块需要单独安装。
import time
LogTime = time.strftime('%Y-%m-%d_%H-%M-%S')
temp = open('config.txt','w')
hostname = '172.16.210.129'
port = 22
username = 'root'
password = '1'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password, timeout=5)
cmd = 'ls'
#cmd = 'ls -l;ifconfig'       #多个命令用;隔开
stdin, stdout, stderr = client.exec_command(cmd)

result = stdout.read()

if not result:
    result = stderr.read()
client.close()

print(result.decode())