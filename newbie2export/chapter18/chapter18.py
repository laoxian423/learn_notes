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

"""UDP Scoket 编程 API
创建 UDP Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
与服务器编程有关的方法：
    socket.blind()
服务器和客户端编程socket共用方法：
    socket.recvfrom(buffsize): 接受UDP数据，返回而元组(data,address),
        data是接收的字节序列对象，buffsize指定一次接受的最大字节数。
    socket.sendto(bytes, address): 把bytes发送到address的socket
    socket.settimeout(timeout):超时
    socket.close()
"""
# 示例1：udp_server.py udp_client.py

""" 访问互联网资源
    HTTP 支持C/S网络结构，是无连接协议，即用完就断开
    HTTP的8种请求：
        OPTIONS，HEAD，GET，POST，PUT，DELETE，TRACE，CONNECT
    GET 方法：向指定资源发出请求，只用在读取数据。
    POST方法：向指定资源提交数据，请求服务器处理。

    HTTS：HTTP和SSL的组合。采用X.509数字认证
"""

""" Python 的urllib库：
    urllib.request 模块：打开和读写URL资源
    urllib.error 模块：包含由request引发的异常
    urllib.parse 模块：解析URL
    urllib.robotparser 模块：分析 robots.txt 文件。给搜索引擎用的，告诉引擎
        机器人那些页面可以抓取，那些不可以。

    urllib.request.urlopen():简单访问网络资源
    urllib.request.Request对象：访问复杂网络资源
"""
# 简单示例
import urllib.request
import urllib.parse

def request_html():
    with urllib.request.urlopen('http://www.sina.com.cn') as response:
        data = response.read()
        html = data.decode()
        print(html)

# 发送GET请求
def get_html():
    url = 'http://www.51work6.com/service/mynotes/WebService.php'
    params_dict = {'email':'your@email','type':'JSON','action':'query'}
    params_str = urllib.parse.urlencode(params_dict)
    print(params_str)

    url = url + '?' + params_str
    print(url)

    # 创建Request对象，该构造方法还有一个参数data，没指定就是GET，否则是POST
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        json_data = data.decode()
        print(json_data)

# 发送POST请求：
def post_http():
    url = 'http://www.51work6.com/service/mynotes/WebService.php'
    params_dict = {'email':'your@email','type':'JSON','action':'query'}
    params_str = urllib.parse.urlencode(params_dict)
    print(params_str)
    params_bytes = params_str.encode()

    req = urllib.request.Request(url, data=params_bytes)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        json_data = data.decode()
        print(json_data)

# 一个下载示例：
def downloader():
    url = 'http://e.hiphotos.baidu.com/image/pic/item/4610b912c8fcc3cef70d70409845d688d53f20f7.jpg'

    with urllib.request.urlopen(url) as response:
        data = response.read()
        f_name = '/home/morgan/Downloads/my.jpg'
        with open(f_name,'wb') as f:
            f.write(data)
            print('OK,download')



if __name__ == '__main__':
    downloader()