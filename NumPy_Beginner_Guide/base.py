""" 阅读笔记
《Numpy Beginner's Guide second Edition
  python 数据分析基础教程
  NumPy 学习指南》

注：书名是我看过的书里面最长的，书也很老了，2013年翻译的，估计成书更早，不过内容符合
我的需要。选择这本书主要是看到里面有pygame,我曾想过用pygame实现一些我的交易客户端的
绘制，所以学习一下。
                                          2019年5月17日

本书结构（思维逻辑）
主要分四部分：基础、深入、绘图
基础部分：
    NumPy 快速入门
    NumPy 基础
    常用函数
    便捷函数
    矩阵和通用函数
深入部分：
    深入模块
    专用函数
    质量控制
绘图应用：
    Matplotlib
    NumPy的扩展：SciPy
    玩转Pygame

* NumPy 是什么？
    一个开源的科学计算库。可以很自然的使用数组和矩阵。涵盖线性代数运算、傅里叶变换和
    随机生成等功能。
    NumPy中数组的存储效率和输入输出性能均优于Python的List。对于TB级的大文件，NumPy
    使用内存映射文件来处理，以达到最优性能。
    NumPy的大部分代码是用C语言写成。

注：书中有很多地方都写一句“刚才做了什么？”，这个形式不错。

"""

import numpy as np

# 一种相对于Python，使用简洁方式的向量加法
# 不需要遍历 arange 元素，直接进行运算
def python_sum(n):
    a = list(range(n))
    b = list(range(n))
    c = []

    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c


def numpy_sum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

# 比较一下使用纯Python和NumPy的速度
import sys
from datetime import datetime

def diff_time_Numpy_python():
    # 1000 个向量
    start = datetime.now()
    c = python_sum(1000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('python 1000 用时:', delta.microseconds)

    start = datetime.now()
    c = numpy_sum(1000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('numpy 1000 用时:', delta.microseconds)

    # 10000 个向量
    start = datetime.now()
    c = python_sum(10000)
    delta = datetime.now() - start
    print('\n最后两个元素',c[-2:])
    print('python 10000 用时:', delta.microseconds)

    start = datetime.now()
    c = numpy_sum(10000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('numpy 10000 用时:', delta.microseconds)
 
    # 100000 个向量
    start = datetime.now()
    c = python_sum(100000)
    delta = datetime.now() - start
    print('\n最后两个元素',c[-2:])
    print('python 100000 用时:', delta.microseconds)

    start = datetime.now()
    c = numpy_sum(100000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('numpy 100000 用时:', delta.microseconds)

    # 100 0000 个向量
    start = datetime.now()
    c = python_sum(1000000)
    delta = datetime.now() - start
    print('\n最后两个元素',c[-2:])
    print('python 1000000 用时:', delta.microseconds)

    start = datetime.now()
    c = numpy_sum(1000000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('numpy 1000000 用时:', delta.microseconds)


""" Numpy 基础 ----------------------------------------
*Numpy 数组对象
    Numpy中的ndarray 是一个多维数组对象，有两部分组成：
        实际的数据
        描述这些数据的元数据
    大部分的数据操作仅仅修改元数据，而不改变底层的实际数据。
"""
def demo_ndarray_tpye():
    """ 演示 ndarray数据类型 """
    a = np.arange(5)
    # 类型：64位的机器会现实int64,32位的显示int32
    print(a.dtype)
    # 维度
    print(a.shape)
    # 创建二维数组
    m = np.array([np.arange(2), np.arange(2)])
    print(m)
    print(m.shape, m.dtype, type(m))
    # 创建三维数组
    m = np.array([np.arange(3), np.arange(3), np.arange(3)])
    print(m)
    print(m.shape, m.dtype, type(m))


def demo_select_array():
    """ 选取数组对象 """
    a = np.array([[1, 2],[3, 4]])
    print(a)
    print(a[0,0])
    print(a[0,1])

""" NumPy 的数据类型
bool                
inti                由所在平台决定32位或者64位
int8                -128至127
int16               -32768至32767
int32               -2的31次方至2的31次方
int64               -2的63次方至2的63次方
uint8               无符号，0-255
uint16
uint32
uint64
float16             半精度浮点数，1位表示正负号，5位表示指数，10为表示尾数
float32             单精度浮点数，1位表示正负号，8位表示指数，23为表示尾数
float64或float       双精度浮点数，1位表示正负号，11位表示指数，52为表示尾数
complex64           复数，分别用两个32浮点数表示实部和虚部
comlex128或complex   复数，分别用两个64浮点数表示实部和虚部

* 每一种数据类型都有对应的类型转换函数：
    float64(42)
    int8(42.0)

* 在NumPy中，许多函数的参数可以指定数据类型，通常是可选的：
    arange(7, dtype=uint16)
    array([0, 1, 2], dtype=unit16)
    a.dtype.itemsize  显示数据类型内存中占用字节数

* 查看NumPy完整的数据类型:
    sctypeDict.keys()

* dtype类的属性：
    t = dtype('Float64')
    print(t.char）      显示字符编码
    t.type              显示数据类型
    t.str               显示‘<f8',第一个表示字节序，第二个字符编码，第三个内存大小
"""

""" 创建自定义数据类型  """
def demo_self_type():
    """ 自定义数据结构 """
    # 40个字节的name,32位整数numitems，32的浮点数记录price
    t = np.dtype([('name', np.str_, 40),
                  ('numitems', np.int32), 
                  ('price', np.float32)])
    print(t)
    itemz = np.array([('Meaning of life DVD', 42, 3.14),
                      ('Butter', 13, 2.72)],
                       dtype=t)
    print(itemz[1])


""" 数组的索引和切片
"""
def demo_array_slice():
    """ nparray的切片和Python的list的切片方法是一样的 
    [start:stop:step]
    """
    a = np.arange(9)
    print(a[3:7])

    # 多维数组的切片和索
    # (2, 3, 4) 可以看作Excel中，工作表，行，列的关系
    b = np.arange(24).reshape(2, 3, 4)
    print(b,'\n', b.shape)
    print(b[0, 0, 0])
    print(b[:, 0, 0])
    print(b[0])
    print(b[0, :, :,])
    print(b[0, ...])
    print(b[0,1])
    print(b[0, 1, ::2])
    print(b[..., 1])
    print(b[:,1])

""" 改变数组的维度 """

def demo_change_array_dimension():
    """ 改变数组的维度 """
    # 数组展平
    b = np.arange(24).reshape(2, 3, 4)
    print(b)
    # ravel 返回数组的一个视图
    print(b.ravel())
    # flatten 展平数组
    print(b.flatten())
    # 除了用reshape改变维度外，还可以用一个正整数元组来设置维度
    b.shape = (6, 4)
    print(b)
    # 转置矩阵
    print(b.transpose())
    # resize 直接改变数组的维度
    b.resize((2, 12))
    print(b)

""" 数组的组合
    水平组合、垂直组合、深度组合
    vstack dstack hstack column_stack row_stack concatenate
"""

def demo_stack():
    """ 数组组合演示 """
    a = np.arange(9).reshape(3, 3)
    b = 2 * a
    print(a)
    print('\n',b)
    # 水平组合
    print(np.hstack((a, b)))
    # 水平组合
    print(np.concatenate((a, b), axis=1))
    # 垂直组合
    print(np.vstack((a, b)))
    print(np.concatenate((a, b), axis=0))
    # 深度组合
    # 将一系列数组沿着纵轴（深度）方向进行层叠组合
    print(np.dstack((a, b)))
    # 列组合,对于一维数组将按列方向进行组合
    oned = np.arange(2)
    twice_oned = 2 * oned
    print(np.column_stack((oned, twice_oned)))
    # 可以用 == 运算比较两个Numpy数组
    print(np.column_stack((a, b)) == np.hstack((a, b)))
    # 行组合，对于两个一维数组，将直接叠加组合成一个二位数组
    print(np.row_stack((oned, twice_oned)))
    # 对于二维数组，row_stack与vstack是相同的


""" 数组的分割
    可以进行水平、垂直或深度分割
"""
def demo_split():
    """ 数组的分割 """
    a = np.arange(9).reshape(3, 3)
    # 水平分割
    print(a)
    print(np.hsplit(a, 3))
    print(np.split(a, 3, axis=1))
    # 垂直分割
    print(np.vsplit(a, 3))
    print(np.split(a, 3, axis=0))
    # 深度分割
    c = np.arange(27).reshape(3, 3, 3)
    print(c)
    print('\n',np.dsplit(c, 3))


""" 数组的属性 """
def demo_array_attr():
    """ 数组的属性 """
    b = np.arange(24).reshape(2,12)
    print(b)
    # 数组的维数，或数组轴的个数
    print(b.ndim)
    # size ,给出数组元素的总个数
    print(b.size)
    # itemsize,元素的内存大小
    print(b.itemsize)
    # 这个数组的大小
    print(b.nbytes)
    # T 属性，转置矩阵
    print(b.T)
    # 想遍历以为数组一样遍历多维数组,返回一个扁平迭代器
    f = b.flat
    for item in f:
        print(item)
    # 使用flatiter对象直接获取一个数组元素
    print(b.flat[2])
    # 获取多个数组元素
    print(b.flat[[2,10]])
    # flat属性是一个可赋值的属性。
    b.flat = 7
    print(b)
    # 第 1 、3两个元算赋值为1
    b.flat[[1, 3]] = 1
    print(b)


""" 数组的转换 """
def demo_trans_nparray_python():
    """ 将nparray 转换为 python """
    b = np.arange(9).reshape(3,3)
    print(b)
    print(b.tolist())
    # 转换时指定数据类型
    print(b.astype(int))




if __name__ == "__main__":
    #diff_time_Numpy_python()
    #demo_ndarray_tpye()
    #demo_select_array()
    #demo_self_type()
    #demo_array_slice()
    #demo_change_array_dimension()
    #demo_stack()
    #demo_split()
    #demo_array_attr()
    demo_trans_nparray_python()
    pass