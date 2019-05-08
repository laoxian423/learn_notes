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
"""
with open('f:/temp/test.csv', 'r', encoding='gbk') as rf:
    reader = csv.reader(rf)
    with open('f:/temp/test1.csv', 'w', newline='', encoding='gbk') as wf:
        writer = csv.writer(wf, delimiter='\t') # 设置分隔符为水平制表符
        for row in reader:
            print(row)
            writer.writerow(row)

