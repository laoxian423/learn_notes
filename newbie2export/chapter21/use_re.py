import urllib.request

import os
import re

url = 'http://www.umei.cc/tags/meinvyouwu.htm'

def find_images(htmlstr):
    """ 从html中查找匹配的字符串"""
    # 定义正则
    pattern = r'http://\S+(?:\.png|\.jpg)'
    return re.findall(pattern, htmlstr)

def get_filename(urlstr):
    """更具图片连接取文件名"""
    pos = urlstr.rfind('/')
    return urlstr[pos + 1:]

# 分析获得的url列表
url_list = []
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode('utf8')
    url_list = find_images(htmlstr)

for imagesrc in url_list:
    req = urllib.request.Request(imagesrc)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        if len(data) < 1024 * 10:
            continue
        if not os.path.exists('f:/temp/download'):
            os.mkdir('f:/temp/download')
        filename = get_filename(imagesrc)
        filename = 'f:/temp/download/' + filename
        with open(filename, 'wb') as f:
            f.write(data)
        print('下载图片', filename)