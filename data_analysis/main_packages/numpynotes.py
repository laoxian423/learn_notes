#
# NumPy 学习笔记整理
# 
# 描述 ：
#       对Numpy的学习资料整理，以函数的形式进行组织和演示
# 历史版本 ：
#       2019-06-03 ：创建 刘昕
#       2019-06-03 ：

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

#create_array() 
"""总结：
    1、归类：NumPy目前来看发现有两种数据结构ndarray和matrix,ndarray它是一个可变数组，意思是可以修改数据值。另外它一个
    ndarray数组只能保留一种数据类型，如都是int，或者都是float，str等。
    ndarray 是NumPy的基础，所有操作都是围绕这个数据结构进行，它本身有大量的属性和方法，如上面的ndim查看数组维度。
    2、联系：ndarry和python中的list非常像，不知道是不是从List继承过来的，以后查看一下。但又不同，它比List要方便的多，
    可以直接加减乘除等。
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
    1、归类：切片、索引等操作都属于数组的访问。
    2、联系：ndarray和python的切片操作基本一致。切片的操作非常灵活，我也经常这么用，但是个人觉得简单的切片还行，过于复杂
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
    arr1 = np.array([1,2,3,4,5])
    arr2 = np.arange(9).reshape(3,3)
    # 填充
    arr1.fill(9)
    print(1,'\t',arr1 )
    # 深拷贝、浅拷贝
    arr1 = np.array([1,2,3])
    arr3 = arr1   # 浅拷贝，实际上arr3也是指向arr1的内存地址，修改其中一个都会变
    arr1[1] = 1000
    print(2, '\t', arr1, arr3)

    arr1 = np.array([1,2,3])
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
    1、归类：ndarray的方法和属性
    2、联系：python的一切都是类，虽然也提供了一些函数式编程的东西。ndarray作为NumPy最重要的一部分，它的方法和属性很多。
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

maths_func01()

""" 总结
    1、归类：数学函数
    2、联系：
        随机数是数学中很重要的部分，每种语言都提供，NumPy的random类中提供了好几个随机数的函数。python本身也提供
        但numpy似乎提供更多的。
    3、用途：
        随机数的用途很广，在数据分析和统计分析中都有很重要的地位。通过对随机浮点数的处理，我们可以生成很多有用的数据。
        比如在绘制曲线，模拟分布等等。

"""

