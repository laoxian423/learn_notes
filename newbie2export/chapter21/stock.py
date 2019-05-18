""" 爬取股票数据
设计思路：
    * 爬取数据
    * 检测数据是否更新，可用MD5进行计算，通过两次MD5的值判断是否更新
    * 处理数据
    * 存入数据库
爬虫程序真的很烦，与被爬对象耦合度太高，对方变化就得跟着变，应该有解决方案
需要的时候去找找吧。
如果网站打不开，试试把下面的记录放到hosts文件中。
104.85.75.152 www.nasdaq.com
104.118.82.7 www.nasdaq.com
23.77.5.127 www.nasdaq.com
23.205.54.160 www.nasdaq.com
注：mysql 中的库名和表名都是区分大小写的，字段名没有验证。
insert into HistoricalQuote (HDate,Open,High,Low,Close,Volume,Symbol) 
        values (02/14/2019,169.71,171.2615,169.38,170.8,21785180,AAPL)
另外，在插入操作时，日期 和 字符串不用双引号或者单引号包裹，就像上面一样，否则引号
本身也会作为值被插入到表中。
"""
import urllib.request
import hashlib
import re
from bs4 import BeautifulSoup
#import db_access


import os

url = 'https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'

def validateUpdate(html):
    """ 验证数据是否更新，更新返回True,未更新返回False """

    # 创建 MD5
    return True
    md5obj = hashlib.md5()
    md5obj.update(html.encode(encoding='utf-8'))
    md5code =  md5obj.hexdigest()
    print(md5code)

    old_md5code = ''
    f_name = 'md5.txt'

    if os.path.exists(f_name):
        with open(f_name, 'r', encoding='utf-8') as f:
            old_md5code = f.read()
    
    if md5code == old_md5code:
        print('数据没有更新')
        return False
    else:
        # 把新的md5写入到文件中
        with open(f_name, 'w', encoding='utf-8') as f:
            f.write(md5code)
        print('md5数据更新')
        return True

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    data = response.read()
    html = data.decode()
    sp = BeautifulSoup(html,'html.parser')

# 返回指定 CSS 选择器的div 标签列表
div = sp.select('div#quotes_content_left_pnlAJAX')
# 从列表中返回第一个元素
divstring = div[0]

if validateUpdate(divstring):
    # 分析数据
    trlist = sp.select('div#quotes_content_left_pnlAJAX table tbody tr')

    data = []

    # 第一条记录不需要，标记一下，循环中跳过
    first_rec = 1

    for tr in trlist:
        trtext  = tr.text.strip('\n\r')
        # 跳过第一条记录
        if first_rec == 1 :
            first_rec = 0
            continue
        # 如果本行为空，跳过。
        if trtext == '':
            continue
        trtext = trtext.strip()
        rows = re.split(r'\s+', trtext)
        """
        fields = {}
    
        fields['Date'] = rows[0]
        fields['Open'] = float(rows[1])
        fields['High'] = float(rows[2])
        fields['Low'] = float(rows[3])
        fields['Close'] = float(rows[4])
        fields['Volume'] = int(rows[5].replace(',', ''))
        """
        fields = []
    
        fields.append(rows[0])
        fields.append(rows[1])
        fields.append(rows[2])
        fields.append(rows[3])
        fields.append(rows[4])
        fields.append(rows[5].replace(',', ''))

        data.append(fields)
    """
    print('数据格式化完毕，准备入库')
    for row in data:
        row['Symbol'] = 'AAPL'
        db_access.insert_hisq_data(row)
    """
    with open('NumPy_Beginner_Guide/appl.csv', 'w') as f:
        s = ''
        for row in data:
            s += str(row[0]).replace('/', '-')
            s += ' ' + row[1]
            s += ' ' + row[2]
            s += ' ' + row[3]
            s += ' ' + row[4]
            s += ' ' + row[5]
            s += '\n'
        f.write(s)



    print('ok')
