# LOOK 数据交换格式

r""" 数据交换格式
    主要有CSV格式、XML格式、JSON格式
    CSV格式：
        "张三同学","你好！\n 我下午去找你借书","王五","2012年12月8日"
    XML格式(使用标签进行自描述）：
        <?xml version="1.0" encoding="UTF-8"?>
        <note>
            <to>张三同学</to>
            <content>你好！\n 我下午去找你借书</content>
            <from>王五</from>
            <date>2012年12月8日</date>
        </note>
    JSON 格式：
        {to:"张三同学",content:"你好！\n 我下午去找你借书",
            from:"王五",date:"2012年12月8日"}
"""

""" CSV 数据交换格式(Comma Separated Values)：
    主要用于电子表格和数据库之间的数据交换
    交换双方约定好字段名
    windows平台默认是GBK
"""

""" csv 模块
    csv.reader(csvfile, dialect='excel', **fmtparams)
    csvfile     csv文件
    dialect     方言，csv.Dialect的子类
                csv.excel 定义Excel生成的CSV文件的常用属性
                csv.excel_tab 水平制表符分隔
                csv.unix_dialect 方言名称:unix,即使用'\n' 作为行终止符，win 下是'\r\n'
    fmtparams   提供单个格式化参数
"""
import csv
with open('f:/temp/test.csv', 'r', encoding='gbk') as f:
    reader = csv.reader(f, dialect=csv.excel)
    for row in reader:
        print(row)


""" csv.writer()
    csv.writer(csvfile, dialect='excel', **fmtparams)

with open('f:/temp/test.csv', 'r', encoding='gbk') as rf:
    reader = csv.reader(rf)
    with open('f:/temp/test1.csv', 'w', newline='', encoding='gbk') as wf:
        writer = csv.writer(wf, delimiter='\t') # 设置分隔符为水平制表符
        for row in reader:
            print(row)
            writer.writerow(row)
"""

""" 解析 XML 文档
    SAX（Simple API for XML) 和 DOM（Document Object Model)两种流行模式
    SAX ：基于时间驱动的解析模式。自上而下遇到开始、结束标签和属性时触发相应事件
        这种模式只能解析，不能写入。优点是速度快。
    DOM ：将XML当作一棵树进行解析。一次性读入内存。
    ElementTree :python提供的兼顾SAX和DOM优点的模块
"""
import xml.etree.ElementTree as ET

tree = ET.parse(r'F:\myRepositraies\learn_notes\newbie2export\chapter16\notes.xml')
print(type(tree))

root = tree.getroot()
print(type(root))
print(root.tag) 

for index, child in enumerate(root):
    print('第{0}个{1}元素，属性：{2} '.format(index, child.tag, child.attrib))
    for i, child_child in enumerate(child):
        print('   标签:{0},内容：{1}'.format(child_child.tag, child_child.text))



""" XPath XML匹配查找
    XPath是专门用来在XML中查找信息的语言。如果说XML是数据库，XPath就是SQL。
    XPath将所有元素看作节点，根节点、父节点、子节点、兄弟节点
    nodename            选择nodename子节点
    .                   选择当前节点           ./Note 当前节点下的所有Note子节点
    /                   路劲指示符             ./Note/CDate  表示所有Note子节点下的CDate节点
    ..                  选择父节点             ./Note/CDate/..  选择Note节点
    //                  选择后代节点           .//CDate 表示当前节点中查找所有的CDate后代节点
    [@attrib]           选择指定属性的所有节点  ./Note[@id] 表示有id属性的所有Note节点
    [@attrib='value']   选择指定属性等于value   ./Note[@id=1] 表示有id属性等于'1'的所有Note节点
                        的所有节点  
    [position]          指定位置，位置从1开始   ./Note[1] 表示第一个Note节点,./Note[last()]标识最
                        最后一个可以使用last()  后一个Note节点，./Note[last()-1]表示倒数第2个。
                        获取
"""
tree = ET.parse(r'F:\myRepositraies\learn_notes\newbie2export\chapter16\notes.xml')
root = tree.getroot()

node = root.find("./Note")
print(node.tag, node.attrib)

node = root.find("./Note/CDate")
print(node.text)

node = root.find("./Note/CDate/..")
print(node.tag, node.attrib)

node = root.find(".//CDate")
print(node.text)

node = root.find("./Note[2]")
print(node.tag, node.attrib)


""" JSON 数据交换格式（JavaScript Object Notation)
    JSON文档的两种结构为对象(object)和数组(array),
    对象(object)示例：
    {
        "name":"a.htm",
        "size":345,
        "saved":true
    }
    数组(array)示例：
    ["text","html","css"]
"""

""" Python 数据与 JSON 数据的隐射关系
        python              JSON
    字典                对象 
    列表、元组           数组
    字符串              字符串
    整数、浮点           数字
    True                true
    False               false
    None                null
"""

""" JSON的编码和解码：
    json内置模块
    dumps() 将编码结果以字符串形式返回
    dump()  将编码结果保存到文件对象中
"""
import json

# 准备数据
py_dict = {'name': 'tony', 'age': 30, 'sex': True}
py_list = [1,2,3]
py_tuple = ('A', 'B', 'C')

py_dict['a'] = py_list
py_dict['b'] = py_tuple

print(py_dict)

# 编码过程
json_obj = json.dumps(py_dict)
print(json_obj)

# 写入JSON数据到data1.json中
with open('f:/temp/data1.json', 'w') as f:
    json.dump(py_dict, f)

# indent=4 表示缩进4个空格
with open('f:/temp/data2.json', 'w') as f:
    json.dump(py_dict, f, indent=4)

""" JSON 解码
    loads() 将JSON字符串进行解码，返回Python数据
    load()  读取文件或流，对其中的JSON数据解码，返回Python数据
"""
# 准备数据
json_obj = r'{"name": "tony", "age": 30, "sex": true, "a": [1, 2, 3], "b": ["A", "B", "C"]}'
py_dict = json.loads(json_obj)
print(py_dict)
print(py_dict['name'])
print(py_dict['age'])
print(py_dict['sex'])

py_dicta = py_dict['a']
print(py_dicta)

with open('f:/temp/data2.json', 'r') as f:
    data = json.load(f)
    print(data)



""" Python 处理配置文件(window ini 文件)
    ini 配置文件示例：
    [Startup]
    RequireOS = windows 2000
    RequireMSI = 3.0
    RequireIE = 6.0.2600.0
    [Product]
    msi = AcroRead.msi
"""

""" configparser  配置文件解析

"""
import configparser

config = configparser.ConfigParser()

config.read('newbie2export/chapter16/test.ini', encoding='utf-8')

print(config.sections())    

section1 = config['Startup']
print(config.options('Startup'))
print(section1['RequireOS'])
print(section1['RequireIE'])

# 写入配置文件
config['Startup']['RequireMSI'] = '8.0'
config.add_section('Section2')
config.set('Section2', 'name', 'Mac')
with open('newbie2export/chapter16/test.ini', 'w') as fw:
    config.write(fw)
