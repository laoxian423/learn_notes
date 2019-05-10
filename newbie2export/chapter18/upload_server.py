# coding=utf-8

""" 上传文件示例程序 """

import socket

HOST = '192.168.0.21'
PORT = 8888

f_name = './copy01.pdf'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    print('Server starting....')

    while True:
        with s.accept()[0] as conn:
            # 创建字节序列对象列表，作为接收数据的缓冲区
            buffer = []
            while True:
                data = conn.recv(1024)
                if data:
                    # 把接收到的数据添加到缓冲区
                    buffer.append(data)
                else:
                    # 没有接收到数据就退出
                    break
            # 将接收的字节序列对象列表合并为一个字节序列对象    
            b = bytes().join(buffer)
            with open(f_name, 'wb') as f:
                f.write(b)
            print('Server accept finished.')