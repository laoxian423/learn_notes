""" UDP 示例服务端 """
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',8888))
print('server starting...')

# 等待接收数据
data, client_address = s.recvfrom(1024)
print('From client:{0}'.format(data.decode()))  
# 给客户端发送数据
s.sendto("hello".encode(),client_address)

s.close()
