""" 正则表达式
    效率高。
    数据挖掘、数据分析、网络爬虫、输入有效性验证
"""

r""" 元字符
    用来描述其他字符的特殊字符。由基本元字符和普通字符构成
    基本元字符有14个。
    如 '\w+' ，它由基本元字符 \ + 和 普通字符 w 组成
    学习正则表达式就是学习元字符的使用
    \   转义符
    .   表示任意一个字符
    +   表示重复一次或多次
    *   重复0次或多次
    ?   重复0次或一次
    |   或，A|B 匹配 A 或则 B
    {}  定义量词
    []  定义字符类
    ()  定义分组
    ^   取反，或匹配一行的开始
    $   匹配一行的结束
"""

# ^ 和 $
import re

p1 = r'\w+@zhijieketang\.com'
p2 = r'^\w+@zhijieketang\.com'

text = "Tony's email is tony_guan588@zhijieketang.com."

m = re.search(p1, text)
print()
print(m)
m = re.search(p2, text)
print(m)

email = 'tony_guan588@zhijieketang.com'
m = re.search(p2, email)
print(m)

# [] 定义字符类

p = r'[Jj]ava'  # 匹配Java java  或者 r'java|Java|JAVA'

m = re.search(p, 'I like Java and Python.')
print()
print(m)

# 字符类取反
# 在正则表达式中指定不想出现的字符
p = r'[^0123456789]'
m = re.search(p, 'python 1000')
print(m)

# 区间
# [a-z]
# [A-Za-z0-9]
# [0-25-7]
p = r'[^0-9]' 
m = re.search(p, 'python 1000')
print(m)

r""" 预定义字符类
    \n  匹配换行
    \r  匹配回车
    \f  匹配一个换页符
    \t  匹配一个水平制表符
    \v  匹配一个垂直制表符
    \s  匹配一个空位符
    \S  匹配一个非空位符
    \d  匹配一个数字字符
    \D  匹配一个非数字字符
    \w  匹配任何语言的单词字符、数字和下划线等。
    \W  等价于[^\w]
"""

""" 量词
    ?       出现零次或一次
    *       出现零次或多次
    +       出现一次或多次
    {n}     出现n 次
    {n,m}   至少出现n 次，但不超过m 次
    {n,}    至少出现n 次
"""

m = re.search(r'\d?','87654321') # 出现一次数字
print(m)

m = re.search(r'\d?','abc') # 出现数字零次
print(m)

m = re.search(r'\d*','87654321') # 出现数字多次
print(m)

m = re.search(r'\d{8}','87654321') # 出现数字8次
print(m)

m = re.search(r'\d{8}','8765432') # 不匹配
print(m)

m = re.search(r'\d{6,7}','87654321') # 出现数字7次
print(m)

m = re.search(r'\d{9,}','87654321') # 不匹配
print(m)

""" 贪婪量词 和 懒惰量词
    贪婪量词会尽可能的多匹配字符
    懒惰量词会尽可能的少匹配量词
"""
m = re.search(r'\d{5,8}','87654321') # 出现数字8次
print(m)

m = re.search(r'\d{5,8}?','87654321') # 出现数字8次
print(m)


""" 分组的使用
    对一个字符串整体使用量词
    捕获分组：匹配的结果保存在内存中，以备引用
"""
p = r'(121){2}'
m = re.search(p, '121121abcded')
print(m)
print(m.group())
print(m.group(1))

p = r'(\d{3,4})-(\d{7,8})'
m = re.search(p, '010-87654321')
print(m)
print(m.group())
print(m.groups())


""" 分组命名
    在正则表达式中为分组命名
    (?P<phone_code>........)
"""
p = r'(?P<area_code>\d{3,4})-(?P<phone_code>\d{7,8})'
m = re.search(p, '010-87654321')
print(m)
print(m.group())
print(m.groups())

print(m.group(1))
print(m.group(2))

print(m.group('area_code'))
print(m.group('phone_code'))


""" 反向引用分组
    可以在正则表达式内部应用之前的分组
"""
# 解析XML代码，找到某一个开始和结束标签
p = r'<([\w]+)>.*</([\w]+)>'
m = re.search(p, '<a>abc</a>')
print(m)
m = re.search(p, '<a>abc</b>') 
print(m)

# 第二行也是匹配的，因此需要反向引用解决这个问题
p = r'<([\w]+)>.*</\1>'  # \1 表示反向引用第一个分组
m = re.search(p, '<a>abc</a>')
print(m)


""" 非捕获分组
    不想保存匹配结果
    ?:   实现非捕获分组
"""
s = 'img1.jpg,img2.jpg,img3.bmp'
# 捕获分组
p = r'\w+(\.jpg)'
mlist = re.findall(p, s)
print(mlist)

# 非捕获分组
p = r'\w+(?:\.jpg)'
mlist = re.findall(p, s)
print(mlist)


""" re 模块
    Python 内置的正则表达式模块
    search()    在输入字符串中查找，返回第一个匹配内容，没找到返回None
    match()     在输入字符串“开始”处查找，返回第一个匹配内容，没找到返回None
    findall()   匹配成功，返回match列表对象，失败None
    finditer()  匹配成功，返回迭代器，失败None
    split()     字符串分割，按匹配字符串分割，返回列表对象
    sub()       字符串替换
"""
# re.split(pattern, string, maxsplit=0, flags=0)
# pattern 正则表达式
# string 要分割的字符串
# maxsplit 分割次数
# flags 编译标志
p = r'\d+'
text = 'AB12CD34EF'
clist = re.split(p, text)
print(clist)

# re.sub(pattern, repl, string, count=0, flags=0)
# pattern 正则表达式
# repl 替换字符串
# string 要被替换的数据
# count 替换次数
# flags 编译标志
p = r'\d+'
text = 'AB12CD34EF'
repace_text = re.sub(p,' ',text,count=1)
print(repace_text)

""" 编译正则表达式
    为了提高效率。
    re.compile(pattern[, flags=0])
    返回一个编译过的正则表达式对象regex
                    regex   与   re 模块函数比较
    search()    regex.search(string[, pos[,endpos]])        re.search(pattern, string,flags=0)
    match()     regex.match(string[, pos[,endpos]])         re.match(pattern, string,flags=0)
    findall()   regex.findall(string[, pos[,endpos]])       re.findall(pattern, string,flags=0)
    finditer()  regex.finditer(string[, pos[,endpos]])      re.finditer(pattern, string,flags=0)
    sub()       regex.sub(repl, string, count=0)            re.search(pattern, repl,string,count=0,flags=0)
    split()     regex.split(string, maxsplit=0)             re.search(pattern, string, maxsplit=0,flags=0)
    pos 是开始查找的索引，endpos是结束的索引
"""
p = r'\w+@zhijieketang\.com'
regex = re.compile(p)

text = "Tony's email is tony_guan588@zhijieketang.com"
m = regex.search(text)
print(m)


""" 编译标志
    可以改变正则表达式引擎行为
    1） ASCII 和 Unicode : re.A   re.U
        regex = re.compile(p, re.U)
    2)  忽略大小写：
        regex = re.compile(p, re.I)
    3)  点元字符匹配换行符
        默认情况下 . 匹配除了换行符外的所有字符，这个连换行符也匹配
        regex = re.compile(p, re.S)  # re.DOTALL
    4)  多行模式
        会影响到 ^ 和 $ 的范围，多行模式下匹配任意一行
        text = 'Hello\nWorld.'
        p = r'^World'
        regex = re.compile(p, re.M)
    5)  详细模式
        可在正则表达式中添加注释 re.X
"""        
p = """(java)  # 匹配java
       .*      # 匹配任意字符0个或多个         
       (python) # 匹配python
    """
regex = re.compile(p, re.I | re.X)
m = regex.search('I like java and python.')
print(m)
