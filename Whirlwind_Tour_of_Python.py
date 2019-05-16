""" 《Python 旋风之旅》阅读笔记 
    网上很火的一本python入门书，告诉哪些想从事数据科学研究的人，如何快速
掌握必要的python知识。如果你有其他语言的基础，想快速了解Python可以看本书。
本书的结构：
    1、 语法速览
    2、 变量和对象
    3、 运算符
    4、 简单变量类型
    5、 内置数据结构
    6、 控制流
    7、 函数
    8、 迭代器
    9、 列表推导
    10、生成器
    11、模块和包
    12、字符串处理和正则表达式
    13、数据科学工具概览
"""

# 使用Conda安装，Anaconda有两个版本：
# Miniconda :最小化版本，提供一个Python解释器和conda的命令行工具
# Anaconda ：科学计算套件。

r""" 1、语法速览 --------------------------------------------------------------------

#  井号单行注释，三引号多行注释
\  语句太长，可用斜杠继续下一个句子
;  在一行上分割多个语句
   a  = b + 1 ; print(a)
PEP 8 : https://www.python.org/dev/peps/pep-0008/
"""

""" 2、变量和对象 -----------------------------------------------------------------

*   在python中，变量不是作为容器，而是作为一个指针。变量名称可以指向任何类型的变量，这也是
    动态语言的一个特性。  
    所以如果有两个或多个变量指向某个内存地址，当你改变一个就都改变了。 

*   数字、字符串和其他简单类型是不可变的：不可更改值，只能更改变量指向。 

*   python中一切皆对象。type(x)
"""
def demo_point():
    """ 演示变量是指针的函数 """
    # x , y 都是列表[1,2,3]的指针，是数据的标签
    x = [1, 2, 3]
    y = x
    print(x, y)
    # 当 x 被改变后，应该说把 4 加到 x 指向的列表。y 的值也变了，应为y也指向这里。
    x.append(4)
    print(x, y)
    # 如果 x 是被 = 赋值，它不会影响到 y,应为赋值被定义为 改变变量指向的对象。
    x = 'somethin else'
    print(x, y)

def demo_all_isObj():
    """ 演示一切都是对象 """
    x = 4.5
    print(x.real, "+", x.imag, "i")
    print(x.is_integer())

""" 3、运算符 ----------------------------------------------------------------
*   Python 实现了 7 种基础二元运算符，其中两种可以同时被用做一元运算符：
        + - * / 
        % 取模
        // 向下整除，a 与 b 求商，去掉小数部分
        ** 乘方
        -a 取反
*   位运算符：
    a & b   按位与
    a | b   按位或
    a ^ b   按位异或
    a << b  左移
    a >> b  右移
    ~a      按位取反
*   比较运算符：
    a == b
    a != b
    a < b
    a > b
    a <= b
    a >= b 
    异或的技巧：(x > 1) != (x < 10) 相当于 (x > 1) xor (x < 10)
*   身份和成员运算符：
    a is b          a 和 b 是相同对象？
    a is not b      a 和 b 不是相同对象？
    a in b          a 是 b 的成员？
    a not in b      a 不是 b 的成员 ？
"""
def demo_operator():
    """ 演示部分运算符 """
    # 输出二进制表示,以0b开头
    print(bin(10))
    # 按位与
    print( 4 | 10)
    print(bin(4 | 10))

""" 4、简单变量类型 -----------------------------------------------------------
    int         可变，不会溢出
    float       精度有限，print( 0.1 + 0.2 == 0.3 )  => False
    complex     复数
    bool
    str
    None        python中所有没有返回值的函数，事实上都会返回None
"""
def demo_var_type():
    """ 变量类型演示 """
    # 浮点数精度问题
    print(0.1 + 0.2 == 0.3)
    print('0.1 = {0:.17f}'.format(0.1))
    print('0.2 = {0:.17f}'.format(0.2))
    print('0.3 = {0:.17f}'.format(0.3))

""" 5、内置数据结构--------------------------------------------------------------
list  : [1, 2, 3]               列表，有序集合,下标从 0 开始
tuple : (3, 2, 1)               元组，不可变的有序集合
dict  : {'a':1, 'b':2, 'c':3}   字典，无序的键值对隐射，key:value
set   : {1, 2, 3}               集合，无序性和唯一性, 没有key 的字典
其他  :                          collections 模块
列表的方法：https://docs.python.org/3/tutorial/datastructures.html
元组的方法：https://docs.python.org/3/tutorial/datastructures.html
字典的方法：https://docs.python.org/3/library/stdtypes.html
集合的方法：https://docs.python.org/3/library/stdtypes.html
其他数据结构：https://docs.python.org/3/library/collections.html
"""
def demo_list():
    """ 列表的特性演示 """
    L = [1, 2, 3, 4, 5, 6]
    # 索引
    print(L[0], L[-6], L[5], L[-1])
    # 切片,显示下标0 到2 的数据，[start:stop:step] 不包含stop
    print(L[0:3])
    print(L[:3])
    print(L[0:])
    print(L[-3:])
    print(L[::-1])
    # 切片的赋值
    L[1:3] = [22, 33]
    print(L)

def demo_tuple():
    """ 元组的特性演示 """
    T = (1, 2, 3)
    print(T)
    # 元组也有长度
    print(len(T))
    # 元组常见的用法是函数返回多个值
    x = 0.125
    # 返回浮点数的分子分母
    print(x.as_integer_ratio())

def demo_dict():
    """ 字典的特性演示 """
    D = {'one':1, 'two':2, 'three':3}
    # 字典值的提取
    print(D['one'])
    # 字典值的增加
    D['four'] = 4
    print(D)

def demo_set():
    """ 集合的特性演示 """
    primes = {2, 3, 5, 7}
    odds = {1, 3, 5, 7, 9}
    # 并集：包含所有元素
    print(primes | odds)
    print(primes.union(odds))
    # 交集:同时出现在两个集合
    print(primes & odds)
    print(primes.intersection(odds))
    # 差分：属于primes不属于odds的元素
    print(primes - odds)
    print(primes.difference(odds))
    # 对称差分：只出现在其中一个集合元素
    print(primes ^ odds)
    print(primes.symmetric_difference(odds))

""" 6、控制流 -------------------------------------------------------------------
* 条件语句：if-elif-else
* for循环：
* while 循环：
* 调整循环执行：break, continue
* 带有else代码块的循环：当作no break语句，只有循环自然结束才执行
"""
def demo_control_flow():
    """ 控制流演示 """
    a = 7
    b = 4
    c = 5
    # if 语句:
    if a == 3:
        print('a = 3')
    elif b == 4:
        print('b = 4')
    else:
        print('c = 5')
    # for 循环,只要是可迭代器都可以用来循环，比如本例中的range(10):
    for i in range(20):
        if i % 2 == 0:
            continue
        else:
            print(i)
    else:
        print('循环全部结束，没有被break')
    # while 循环
    a = 0
    while a <= 30:
        print(a)
        if a == 15:
            break
        a += 1

""" 7、函数 -----------------------------------------------------------------
def :   自定义函数
lambda : 匿名函数
"""     
def demo_fun_no_para():
    """ 没有形式参数的函数 """
    pass
    return None

def demo_fun_have_parameters(a, b, c):
    """ 有多个形式参数的函数 """
    pass

def demo_fun_change_para1(a, *b):
    """ 拥有可变参数的函数 """
    # *b 会把多个参数转换成元组，或者接收一个元组实参
    pass

def demo_fun_change_para2(a, **b):
    """ 拥有可变参数的函数 """
    # **b 会把多个参数转换成字典,或者接收一个字典实参
    pass


def demo_fun_default_para(a=3, b=4):
    """ 拥有缺省参数的函数 """
    pass


def demo_lambda():
    """ lambda 函数的演示 """
    add = lambda x, y: x + y
    """上面这句lambda可以这样理解
     def add(x,y):
         return x + y
    """
    print(add(1, 2)) 
    # 对字典进行排序
    data =[{'first':'Guido', 'last':'Van Rossum', 'YOB':1956},
           {'first':'Grace', 'last':'Hopper',     'YOB':1906},
           {'first':'Alan',  'last':'Turing',     'YOB':1912}]
    sorted_data = sorted(data, key=lambda item: item['first'])
    print(sorted_data)

""" 8、错误和异常 ---------------------------------------------------------
* 捕获异常： try...except...else...finally
* 抛出异常： raise
"""
def demo_try_except():
    """ 异常的演示函数 """
    try:
        print('in try....')
        # 制造异常
        x = 1/1
    except:
        print('in except....')
        raise ZeroDivisionError("不要除零操作")
    else:
        print('这里成功就会执行')
    finally:
        print('不管怎么样都会执行')

    # 获取异常的错误信息
    try:
        x = 1 / 0
    except ZeroDivisionError as err:
        print(type(err))
        print(err)


class MySpecialError(ValueError):
    """ 自定义异常 """
    pass

def demo_use_myExcept():
    """ 调用自定义异常 """
    try:
        pass
    except:
        raise MySpecialError("have a error....")


""" 9、 迭代器 ------------------------------------------------------------------
*   当你对数据进行遍历时，python会检查它是否包含迭代器
*   python的itertools库中包含了一个无穷range的count函数：
        from itertools import count
        for i in count():
*   enumerate : 不仅迭代值，还需要对索引进行跟踪。
*   zip : 对多个列表同时进行迭代
*   map : map接收一个函数，并且将它应用到迭代器中每一个值上。
*   filter: 允许使得过滤函数为真的保留下来。
*   专用迭代器：itertools  https://docs.python.org/3/library/itertools.html
    form itertools import permutations

    permutations(range(3)) 在全排列中迭代
    combinations(rang(4), 2) 在全组合中迭代
    product('ab',range(3)) 对多个可迭代对象两两配对进行迭代
"""
def demo_iter():
    """ 迭代器演示函数 """
    # list 包含一个迭代器
    L = iter([2, 4, 6, 8])
    print('L =',*L)
    print(iter([2, 4, 6, 8]))
    print(iter(range(0,10)))
    

    # enumerate 的使用
    L = [2, 4, 6, 8]
    for i, val in enumerate(L):
        print(i, val)

    # zip 的使用
    L = [2, 4, 6, 8]
    R = [1, 3, 5, 7]
    for lval, rval in zip(L, R):
        print(lval, rval)

    # map 的使用
    square = lambda x: x ** 2
    # for val in *map(lambda x: x**2, range(10)))  # 等价下面一行
    for val in map(square, range(10)):
        print(val,end=' ')

    # filter 的使用
    is_even = lambda x: x % 2 == 0
    for val in filter(is_even, range(10)):
        print(val, end=' ')

""" 10、 列表推导 --------------------------------------------------------------
基本格式：[expr for var in iterable]  iterable可以是任意一个python可迭代对象。
        [i for i in range(20) ]

多重迭代：[(i, j) for i in range(2) for j in range(3)]

条件控制迭代： [val for val in range(20) if val % 3 > 0]
              [val if val % 2 else -2 
                   for val in range(20) if val % 3]
              去除所有3的倍数，并且把2的倍数取负
集合的推导：{a % 3 for a in range(1000)}
字典推导：{n:n**2 for n in range(6)}  加个冒号
生成迭代器：(a % 3 for a in range(1000)) 使用小括号
"""

def demo_list_tuidao():
    """ 列表推导演示函数 """
    L = [i for i in range(20) if i % 3 > 0]
    print(L)
    L = [(i, j) for i in range(2) for j in range(3)]
    print(L)
    # python 的类似三元操作
    #   如果 val 能够整除 2，那么返回val，否则返回-val
    val = 9
    print(val if val % 2 else -val)
    print([val if val % 2 else -2 
                   for val in range(20) if val % 3])
    # 集合推导
    print({a % 3 for a in range(1000)})
    # 字典推导
    print({n:n**2 for n in range(6)})

""" 11、生成器
* 包括生成器表达式和生成器函数
* 列表推导和生成器表达式的区别：
    1、列表推导使用方括号，生成器表达式使用圆括号。
    2、列表推导生成具体元素，而生成器表达式返回一个迭代器
    3、列表是值的集合，而生成器是产生值的方法。
    4、列表可多次迭代，生成器只能迭代一次（这意味着可以被停止和继续）。
* 生成器函数 yield:
    def gen():
        for n in range(12):
            yield n ** 2
"""
def demo_generator():
    """ 生成器特性演示 """
    # 停止和继续
    G = (n ** 2 for n in range(12))
    for n in G:
        print(n, end=' ')
        if n > 30 :break
    print("\n doing something in between")
    
    for n in G:
        print(n, end=' ')

def generator_primes(N):
    """ 返回一个素数生成器，不大于N """
    primes = set()
    for n in range(2,N):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

""" 12、模块和包 ---------------------------------------------------------------
* 显式导入模块： import math
                import numpy as np          导入并取别名
                from math import cos, pi    导入函数cos和常量pi
* 隐式导入模块： from math import *    导入到本地命名空间

* 导入第三方库：
    PyPI仓库 , Python Package Index,Python软件包索引，https://pypi.python.org/ 

"""

""" 13、字符串处理和正则表达式
"""
def demo_str_fun():
    """ 字符串常用函数 """
    fox = "tHe qUICk bROWn fOX."
    # 大小写转换
    print(fox.upper())  
    print(fox.lower())
    # 首字母大写，段落首字母大写
    print(fox.title())
    print(fox.capitalize())
    # 大小写颠倒
    print(fox.swapcase())
    # 添加和删除空格
    line = '      this is the content     '
    print(line.strip())
    print(line.rsplit())
    print(line.lstrip())
    num = '000000000435'
    print(num.strip('0'))
    # 填充空格及其他符号
    line ='this is the content'
    print(line.center(30))
    print(line.ljust(30))
    print(line.rjust(30))
    print('333'.rjust(10,'0'))
    print('333'.zfill(10))
    # 查找和替换
    line = 'the quick brown fox jumped over a lazy dog'
    print(line.find('fox'))
    print(line.index('fox'))
    print(line.rfind('a'))
    print(line.rindex('a'))
    print(line.startswith('the'))
    print(line.endswith('dog'))
    print(line.replace('brown', 'red'))
    # 拆分和分割字符串
    print(line.partition('fox'))
    print(line.split())
    # 组合字符串
    print('--'.join(['1', '2', '3']))

""" 14、数据科学工具概览



"""






if __name__ == "__main__":
    #demo_point()
    #demo_all_isObj()
    #demo_operator()
    #demo_var_type()
    #demo_list()
    #demo_tuple()
    #demo_dict()
    #demo_set()
    #demo_control_flow()
    #demo_lambda()
    #demo_try_except()
    #demo_iter()
    #demo_list_tuidao()
    #demo_generator()
    #print(*generator_primes(1000))
    demo_str_fun()
    pass
