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

# 1、 ndarray NumPy的基本数据结构



def create_array():
    """ndarray的创建

    一维数组的创建
    多维数组的创建
    """

    # 方式1:用python的list结构创建一维数组
    list1 = [1, 2, 3, 4]
    array1 = np.array(list1)
    print(array1, type(array1))

    # 方式2：用np.arange创建一维数组
    array1 = np.arange(1, 10, 1, dtype=int)
    print(array1, type(array1))

    # 创建多维数组
    list1 = [[1, 2, 3], [4, 5, 6]]
    array1 = np.array(list1)
    print(array1, type(array1), array1.ndim)
    array1 = np.arange(9).reshape(3, 3)
    print(array1, array1.ndim)

create_array() 
"""总结：
    1、NumPy目前来看发现有两种数据结构ndarray和matrix,ndarray它是一个可变数组，意思是可以修改数据值。另外它一个
    ndarray数组只能保留一种数据类型，如都是int，或者都是float，str等。
    ndarray 是NumPy的基础，所有操作都是围绕这个数据结构进行，它本身有大量的属性和方法，如上面的ndim查看数组维度。
    2、ndarry和python中的list非常像，不知道是不是从List继承过来的，以后查看一下。但又不同，它比List要方便的多，
    可以直接加减乘除等。
    3、由于可直接运算，如加减乘除，一个array可以乘以一个常数，也可以乘以另外一个array,做一一对应的运算。感觉用于
    矩阵运算应该很方便，不过NumPy中有专门做矩阵运算的数据结构matrix。不过ndarray是用c实现的，应该说NumPy大部分
    运算都是c实现的，从速度上讲用它就很划算。
"""

