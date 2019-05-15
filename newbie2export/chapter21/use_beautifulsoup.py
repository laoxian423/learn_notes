"""
https://www.crummy.com/software/BeautifulSoup/
pip install beautifulsoup4
解析网页结构
BeautifulSoup类的常用API:
    .find_all(tagname): 根据标签返回所有符合条件的元素列表
    .find(tagname): 根据标签返回符合条件的第一个元素
    .select(selector):通过css中选择器查找符合条件的所有元素
    .get(key, default=None): 获取标签属性值
    .title: 获得当前HTML页面的title属性值
    .text:放回标签中的文本内容。
"""
import os
import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.umei.cc/tags/meinvyouwu.htm'

def find_images(htmlstr):
    """ 从html中查找匹配的字符串"""
    # 解析器：
    # html.parser ：python编写的解析器，速度比较快
    # lxml :C 编写的解析器，速度很快，依赖于C库，CPython可以使用该解析器
    # lxml-xml : C编写的XML解析器
    # html5lib : HTML5 解析器。
    sp = BeautifulSoup(htmlstr, 'html.parser')
    # 返回所有的img 对象
    imgtaglist = sp.find_all('img')

    # 从img标签中返回对应的src列表
    srclist = list(map(lambda u: u.get('src'), imgtaglist))
    # 过滤掉非.png和.jpg结尾的src字符串
    filtered_srclist = filter(lambda u: u.lower().endswith('.png') or u.lower().endswith('.jpg'),srclist)

    return filtered_srclist
    # # 定义正则
    # pattern = r'http://\S+(?:\.png|\.jpg)'
    # return re.findall(pattern, htmlstr)

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