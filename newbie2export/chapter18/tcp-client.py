""" socket tcp 客户端程序 """
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
s.connect(('192.168.0.21',8888))

# 给服务器发送数据
# 在字符前加 b 可以将字符串转换为字节序列，只适合ASCII字符串
s.send(b"Hello")
# 从服务器接收数据
data = s.recv(1024) 
print('Recv data From server:{0}'.format(data.decode()))

s.close()

