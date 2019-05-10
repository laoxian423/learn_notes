""" 上传文件客户端 """
import socket

HOST = '192.168.0.21'
PORT = 8888

f_name = 'f:/temp/Python从小白到大牛.pdf'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))

    with open(f_name, 'rb') as f:
        b = f.read()
        s.sendall(b)
        print('OK ,Client send over.')