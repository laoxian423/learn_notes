import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1',8888)

s.sendto(b'Hello',server_address)   

data, _ = s.recvfrom(1024)

print('From server:{0}'.format(data.decode()))

s.close()
