# LOOK 网络编程
"""
Python提供：
    Scoket 低层次网络编程：采用TCP、UDP
    基于URL的高层次网络编程：采用HTTP和HTTPS

很好用的两个firefox插件
    百度网盘下载助手，直接加速版
    group speed dial    
"""

"""TCP Socket API
    python 提供了两个socket模块，socket和socketserver
    socket模块提供标准的BSD Scoket API 伯克利套接字，伯克利大学学生Berkeley开发。
    socketserver重点是网络服务器开发，提供了4个基本服务器类型
"""

""" 常见TCP Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

第一个参数说明是IPV4，如果IPV6就socket.AF_INET6
第二个参数设置通信类型为TCP
* socket对象常用方法：
socket.bind(address)    绑定地址和端口，一个二元组对象
socket.listen(backlog)  监听端口，backlog最大连接数，默认是1
socket.accept()         等待客户端连接，成功返回二元组（conn, address),conn是新的socket对象
                        ，可以用来接收和发送对象，address是客户端地址。
* 与客户端有关的scoket方法：
scoket.connet(address)  
* 服务端与客户端公用的socket方法：
socket.recv(buffsize):      接收TCP Scoket 数据，返回字节序列对象，接收的字节大于buffsize，需要
                            多次调用该方法。
socket.send(bytes):         发送数据，将bytes发送到远程socket,返回成功发送的字节数。
socket.sendall(bytes):      连续发送，知道发完或者异常
socket.settimeout(timeout): 设置超时，timeout是一个浮点数，单位是秒，None永远不超时
socket.close()              关闭socket，要立即关闭用socket.shutdown()
"""

# 示例程序1 : tcp-server.py   tcp-client.py
# 示例程序2 : upload-server.py upload-client.py