""" socket tcp 服务端程序 """
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',8888))
s.listen()
print('Server starting....')

# 等待客户端连接,accept()为阻塞程序，等待客户连接。
# conn 是一个新的socket对象，address是用户地址
conn, address = s.accept()
# 客户端连接成功
print(address)

# 从客户端接收数据
data = conn.recv(1024)
print('Recv Data From Client:{0}'.format(data.decode()))

# 给客户端发送数据
conn.send('Hello'.encode())

# 释放资源
conn.close()
s.close()

