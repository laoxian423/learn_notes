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
    a = [range(n)]
    b = [range(n)]
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
    print('python 1000 :', delta.microseconds)

    start = datetime.now()
    c = numpy_sum(1000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('numpy 1000 :', delta.microseconds)

    # 10000 个向量
    start = datetime.now()
    c = python_sum(10000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('python 10000 :', delta.microseconds)

    start = datetime.now()
    c = numpy_sum(10000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('numpy 10000 :', delta.microseconds)
 
    # 100000 个向量
    start = datetime.now()
    c = python_sum(100000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('python 100000 :', delta.microseconds)

    start = datetime.now()
    c = numpy_sum(100000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('numpy 100000 :', delta.microseconds)

    # 100 0000 个向量
    start = datetime.now()
    c = python_sum(1000000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('python 1000000 :', delta.microseconds)

    start = datetime.now()
    c = numpy_sum(1000000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('numpy 1000000 :', delta.microseconds)


if __name__ == "__main__":
    # diff_time_Numpy_python()
    start = datetime.now()
    c = numpy_sum(1000000)
    delta = datetime.now() - start
    print('最后两个元素',c[-2:])
    print('numpy 1000000 :', delta.microseconds)
    
    pass