#
# NumPy 学习笔记整理
# 
# 描述 ：
#       对Numpy的学习资料整理，以函数的形式进行组织和演示
# 历史版本 ：
#       2019-06-03 ：创建 刘昕
#       2019-06-03 ：create_array()  access_array() common_func_and_attr() maths()
#       2019-06-17 : numerical_oper()  sort_function()
#                    6月10日母亲住院准备膝盖置换手术，好久没学习了。

# 文档关键字：
# ndarray

import numpy as np



def create_array():
    """ndarray的创建

    关键字：创建数组 一维 二维 多维
    """

    # 方式1:用python的list结构创建一维数组
    list1 = [1, 2, 3, 4]
    array1 = np.array(list1)
    print(1, array1, type(array1))

    # 方式2：用np.arange创建一维数组
    array1 = np.arange(1, 10, 1, dtype=int)
    print(2, array1, type(array1))

    # 创建多维数组
    list1 = [[1, 2, 3], [4, 5, 6]]
    array1 = np.array(list1)
    print(3, array1, type(array1), array1.ndim)
    array1 = np.arange(9).reshape(3, 3)
    print(4, array1, array1.ndim)

    # 在创建数组时指定元素类型
    array1 = np.array([1, 2, 3, 4], dtype=np.float32)
    print(5, array1)
    # 修改元素类型，并返回一个新数组
    array2 = np.asarray(array1, dtype=np.float64)
    print(6, array2)
    # 修改原始数据类型
    array1.astype(np.float64)
    print(7, array1)
    # 创建混合数据类型，不提倡
    array3 = np.array([1, 2.0, '3'], dtype=object)
    print(8, array3)



#create_array() 
"""总结：
    1、归类：数据结构。NumPy目前来看发现有两种数据结构ndarray和matrix,ndarray它是一个可变数组，意思是可以修改数据值。
    另外它一个ndarray数组只能保留一种数据类型，如都是int，或者都是float，str等。
    ndarray 是NumPy的基础，所有操作都是围绕这个数据结构进行，它本身有大量的属性和方法，如上面的ndim查看数组维度。
    2、关联：ndarry和python中的list非常像，不知道是不是从List继承过来的，以后查看一下。但又不同，它比List要方便的多，
    可以直接加减乘除等。
        python本来只设计了很少的基础数据类型，整形、浮点型、布尔型，由于Numpy是C语言开发的，为了提高运算
    速度，有增加了很多的基础数据类型。
        事物的发展应该是分类越来越细的，尤其在数据分析领域，怪不得numpy始终进不了python标准库，也难怪python
        的创始人黯然离开，确实作为数据分析的流行语言，原有的python设计思想确实很难坚持了。
    3、用途：由于可直接运算，如加减乘除，一个array可以乘以一个常数，也可以乘以另外一个array,做一一对应的运算。感觉用于
    矩阵运算应该很方便，不过NumPy中有专门做矩阵运算的数据结构matrix。不过ndarray是用c实现的，应该说NumPy大部分
    运算都是c实现的，从速度上讲用它就很划算。
"""

def access_array():
    """ ndarray数组的访问

    关键字：索引 访问 切片 布尔 条件筛选等
    """
    # 索引（下标）访问
    arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
    arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(1, arr1[2])  # 第3个
    print(2, arr2[1,1])  # 第二行第二列

    # 切片，和python的语法一致
    print(3, arr1[1:])
    print(4, arr1[3:-1])
    print(5, arr2[1,]) # 第二行
    print(6, arr2[:,1]) # 第二列
    print(7, arr1[::2]) # 步长为2

    # 布尔
    mask = np.array([0,1,0,0,1,0,1], dtype=bool)
    print(8, arr1[mask])

    # 条件筛选
    print(9, arr1[arr1 % 2 == 0])
    print(10, np.where(arr1 % 2 == 0)) # 返回索引值
    print(11, arr1[np.where(arr1 % 2 == 0)])


#access_array()
""" 总结：
    1、归类：数组访问。
    2、关联：ndarray和python的切片操作基本一致。切片的操作非常灵活，我也经常这么用，但是个人觉得简单的切片还行，过于复杂
    或者及其负责的切片操作不宜提倡，如有些切片下标干脆用数学公式生成，可读性太差，和c的指针一样难以阅读。where的用
    法还不错，让我想起sql语句，简单且明了。
    3、用途：对数组的访问用处很多，往往我们不会对全部数组数据进行运算，而是只处理他的一部分，以往需要遍历操作，现在通过筛选
    和切片等操作能够快速提取数据。比如通过where操作提取符合条件的下标，再统一进行运算。不知道array中能不能存放二进制
    数据，不然做图像处理就方便多了。
"""

def common_func_and_attr():
    """ 常见的方法和属性

    关键字：fill copy ndim dtype shape size itemsize
        填充 深拷贝 浅拷贝 维度 数据类型 数组大小 内存大小
    """
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.arange(9).reshape(3, 3)
    # 填充
    arr1.fill(9)
    print(1,'\t',arr1 )
    # 深拷贝、浅拷贝
    arr1 = np.array([1,2,3])
    arr3 = arr1   # 浅拷贝，实际上arr3也是指向arr1的内存地址，修改其中一个都会变
    arr1[1] = 1000
    print(2, '\t', arr1, arr3)

    arr1 = np.array([1, 2, 3])
    arr3 = arr1.copy()   # 深拷贝，修改其中一个另一个不变
    arr1[1] = 1000
    print(3, '\t', arr1, arr3)

    # 查看属性：维度、数据类型、大小、占用空间
    print(4, '\t', arr1.shape, arr2.shape)
    print(5, '\t', arr1.ndim, arr2.ndim)
    print(6, '\t', arr1.dtype)
    print(7, '\t', arr1.size)
    print(8, '\t', arr1.itemsize)


#common_func_and_attr()

"""总结
    1、归类：数组的方法和属性
    2、关联：python的一切都是类，虽然也提供了一些函数式编程的东西。ndarray作为NumPy最重要的一部分，它的方法和属性很多。
    他的方法和属性体现着浓浓的数学特征，像fill,填充一个数组，List里面就没有，其他的方法和属性也是这样，为了参与
    各种运算提供方便。
    3、用途：深拷贝和浅拷贝很重要，我记得在java里面这个处理比较麻烦，尤其将“类”作为参数传递的时候，一个不小心就把你不想
    改变的数据修改了。size的用途一般需要迭代元素时可以取它，不过len()函数也可以；ndim,shape我能想到的也是在迭代中使用。
    dtype,itemsize估计只有很复杂的一些程序里会用到，我的代码生涯里很少动态去判断数据类型和所占空间。
"""

def maths_func01():
    """ 数学函数

    关键字：随机数
    """
    # 生成10个1以内的随机浮点数。返回一个ndarray
    rand1 = np.random.rand(10)
    print(1, '\t', rand1, type(rand1))

#maths_func01()

""" 总结
    1、归类：数学函数
    2、关联：
        随机数是数学中很重要的部分，每种语言都提供，NumPy的random类中提供了好几个随机数的函数。python本身也提供
        但numpy似乎提供更多的，比如随机整数randint(),虽然通过处理小数也能得到随机整数，但是NumPy的大部分运算和
        函数都是 c 编译的，所以还是能用它提供的就用。
    3、用途：
        随机数的用途很广，在数据分析和统计分析中都有很重要的地位。通过对随机浮点数的处理，我们可以生成很多有用的数据。
        比如在绘制曲线，模拟分布等等。

"""

def numerical_oper():
    """ 数值运算

    关键字：累加、累乘、标准差、方差、平均数、限定、最大最小、四舍五入
    """
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    # 累加、求和
    print(1, arr1.sum())
    print(2, arr2.sum())
    print(3, arr2.sum(axis=0)) # y轴
    print(4, arr2.sum(axis=1)) # x轴
    # 累乘
    print(5, arr1.prod())
    print(6, arr2.prod(axis=0))
    # 平均数
    print(7, arr1.mean())
    print(8, arr2.mean())
    print(9, arr2.mean(axis=0))
    # 方差
    print(10, arr1.var())
    # 标准差
    print(11, arr1.std())
    # 限定,小于2的等于2，大于4的等于4
    print(12, arr1.clip(2, 4))
    # 最大最小值
    print(13, arr1.min(),arr1.max())
    # 返回最大最小值的索引值
    print(14, arr1.argmin(),arr1.argmax())
    # 四舍五入
    arr3 = np.array([1.22, 2.285, 9.345])
    print(15, arr3.round())
    print(16, arr3.round(decimals=1))

#numerical_oper()
""" 总结
    1、归类：
        数学运算之常用数值运算
    2、关联：
        上面所有的数值运算，都有对应的Python函数。方差和标准差的计算似乎和数学中的定义不同。
        按照定义，标准差应该是方差的平方根，但是这里似乎不是。
    3、用途：
        这一部分的类方法应该是数值运算中最为常用的一些。不同的人有不同的思路，在《Numpy基础》这
        本书中，prod是作为阶乘来说的，这里按累乘来解释，虽然是一回事，但是体现了两种思想，一个基于
        数学的思路，一个基于应用的思路。对于这个函数来说，累乘更加准确，阶乘只是它的一个特列，函数值
        连续的一个特列。
"""

def sort_function():
    """  排序操作

    关键字：排序
    """
    # 一维数组的排序,不改变原有顺序，返回一个新的数组
    arr1 = np.array([2, 4, 1, 9, 7, 2, 10, 8])
    print(1, np.sort(arr1))
    # 返回一维数组排序后的索引值
    print(2, np.argsort(arr1))
    # 二维数组的排序
    arr2 = np.array([[2, 5, 1, 3],
                     [10, 8, 7, 6]])
    print(3, np.sort(arr2))
    print(4, np.sort(arr2, axis=0))

    # 排序插入
    arr3 = np.linspace(0, 10, 20)
    values = np.array([1.3, 3.5])
    print(5, arr3, '\n', np.searchsorted(arr3, values))

#sort_function()
""" 总结：
    1、归类：
        通用操作
    2、关联：
        基本算法实现。对一维算法的排序还行，多维有些乱，尤其指定轴时就搞不清楚怎么回事了。
        好像pandas的排序要好用些，这个知道就可以了。此外它还有一个np.lexsort()可以对每
        个列指定排序规则，需要时在翻看吧，很难用的样子。
    3、用途：
        简单的数组排序，似乎都没办法倒序排列。
"""
