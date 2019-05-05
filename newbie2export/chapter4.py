# coding=utf-8
"""
 *  python 不需要指定数据类型，赋给它什么数值，它就是该类型变量。
 *  python 是动态语言类型，它不检查数据类型。
"""
_hello = "HelloWorld"
score_for_student = 0.0
y = 20
x = True
print('_hello is ',type(_hello))
print('score_for_student is ',type(score_for_student))
print('y is ',type(y))
print('x is ',type(x))

"""
注释
    #  可以在代码的后面注释，也可以在上面注释
    在windows的pycharm中可以选择一行或多行后按下 ctrl+/ 进行注释
    频繁的注释有时反映了代码的低质量。
#!/usr/bin/python
或者： #!/usr/bin/env python3
# -*- coding: utf-8 -*-  
# 代码文件: newbie_to_export/chapter4.py
_hello = "HelloWorld"
score_for_student = 0.0
y = 20
x = True
"""

"""
 * python中一个模块就是一个文件
 * 模块中可以声明变量、常量、属性、函数、类等
 * 模块提供一种命名空间(namespace),不同模块中可以有相同名字的变量。
 * 下面是模块的使用例子：
"""
import module1
from module1 import z

y = 20
print(y)
print(module1.y)
print(z)
"""
包：
   * 如果有两个名字的模块，就只能使用包来隔离(package)
   * 每个包下面会有一个__init__.py的文件，告诉解释器这事一个包，一般是空的，也可以有内容。
   * 包就是一个文件夹加上一个__init__.py的文件。
   * 导入一个包：
   import com.pkg2.hello as module1
   from com.pkg2.hello import z
   from com.pkg2.hell0 import z as x
   as 语句提供一个别名。
"""