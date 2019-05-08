# LOOK 数据类型

"""
python有六种数据类型：数字、字符串、列表、元组、集合和字典。

数字类型：4中类型，整数、浮点、复数、布尔类型

整数 int ：
    二进制数  以0b 或者0B 为前缀
    八进制数  以0o 或者0O 为前缀
    十六进制  以0x 或者0X 为前缀
浮点数 float ：
    可用小数表示，也可用科学记数法表示，用大写的E或小写的e表示10的指数，如e2表示10的平方
    3.36e2
    1.56e-2
复数类型 complex ：
    1 + 2j  表示的是实部为1 ，虚部为2 的复数
布尔类型 bool ：
    bool 是 int 的子类，只有 True 和 False 两个值
    任何类型都可以通过 bool() 转为布尔值，如空的、没有的都都会被转为False
"""

"""数据类型的转换：
隐式类型转换--布尔数值可以隐式转换为整数类型  
"""
a = 1 + True
print(a)

"""显式类型转换：
   int()  float()  bool()
   int() 可以将布尔、浮点和字符串转换为整数，浮点数会被截掉小数部分
   float() 可以将布尔、整数和字符串转换为浮点
"""

"""字符串类型 str
python的字符串表示有三种：
    * 用单引号或者双引号包裹起来的字符串
    * r'helloworld'   原始字符串，字符串中的特殊字符不转义
    * 用三重引号包裹起来的字符串 """   """
python中的字符串采用Unicode编码，所以字符串可以包含中文等亚洲字体
"""

"""格式化字符串
   {1:d} 1 表示 format(value1,value2....) 中的索引1
   {:f/F} 十进制浮点
   {:g/G} 十进制整数或浮点数
   {:e/E} 科学计算法表示浮点数
   {:o}   八进制整数
   {:x/X} 十六进制整数。
   {1:10.2f} 标识10位宽，其中小数为精度为2
"""
name = 'Mary'
age = 18
money = 1234.56
print("{0}年龄是{1:d}岁".format(name,age))

"""字符串查找
    str.find(sub[,start[,end]]) 在start 和 end之间查找sub,找到返回索引，没找到返回-1
    str.rfind(sub[,start[,end]]) 从右开始查找
"""
source_str = "There is a string accessing example."    
# len() 属于顶层函数，不属于任何一个类。
print(len(source_str))
print(source_str.find('string'))

"""字符串与数字相互转换
字符串转换为数字
数字转换为字符串
"""
print(int('18'))
# print(int('AB'))  # 抛出 valueError 异常
print(int('AB',16)) # 指定基数，16进制

print(str(3.24))
print(str([1,2,3]))
print(str({'name':'mark'}))
print(str(True))

