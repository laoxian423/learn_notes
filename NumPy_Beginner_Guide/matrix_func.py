""" 矩阵 和 通用函数
    matrix and universal functions
    通用函数可以逐个处理数组中的元素，也可以直接处理标量。
    矩阵是ndarray的子类
"""
import numpy as np
import matplotlib.pyplot as plt

def create_matrix():
    """ 矩阵的创建 """
    # 使用字符串创建矩阵
    A = np.mat('1 2 3; 4 5 6; 7 8 9')
    print(A)
    # 转置矩阵
    print(A.T) 
    # 逆矩阵
    print(A.I)

    # 使用 ndarray创建矩阵
    A1 = np.mat(np.arange(9).reshape(3, 3))
    print(A1)

    # 从已有矩阵创建新矩阵
    A2 = np.eye(2)
    print(A2)
    B2 = 2 * A2
    print(B2)

    # 使用字符串创建符合矩阵
    comp = np.bmat("A2 B2; A2 B2")
    print(comp)

""" 通用函数
    通用函数的输入是一组标量，输出也是一组标量，通常可对应于基本数学运算。
    使用NumPy的frompyfunc函数，通过一个Python函数来创建通用函数
    通用函数拥有自己的方法，通用函数并非真正的函数
    通用函数有4个方法，只对输入两个参数，输出1个参数的ufunc对象有效：
    reduce 
    accumlate
    reduceat
    outer
"""
def ultimate_answer(a):
    result = np.zeros_like(a)
    result.flat = 42
    return result

def demo_unifunc():
    """ 演示创建通用函数 """

    # 指定输入参数的个数为1 ，随后的1为输出的参数个数
    ufunc = np.frompyfunc(ultimate_answer, 1, 1)
    print(ufunc(np.arange(4)))
    print(ufunc(np.arange(4).reshape(2,2)))

    # 通用函数的方法
    a = np.arange(9)
    print(np.add.reduce(a))
    print(np.add.accumulate(a))

""" 算术运算
    在Numpy中，基本运算符+ - * 隐式关联着通用函数add subtract 和 multiply.
    就是说，当你对numpy数组使用这些算术运算时，对应的通用函数会自动调用。
    除法较为复杂，涉及三个通用函数 divide  true_divide  floor_division，以及两个运算符 /  //
"""

def demo_unifunc1():
    """ 通用函数算术运算演示 """
    a = np.array([2, 6, 5])
    b = np.array([1, 2, 3])
    # 书中这divide是截断小数部分的，但我的版本这两个输出是一致的
    print(np.divide(a, b), np.divide(b, a))  
    print(np.true_divide(a, b), np.true_divide(b, a))  
    # floor_divide总是返回整数部分
    print(np.floor_divide(a, b), np.floor_divide(b, a))  

    # 默认情况下，使用 /运算符相当于调用divide,// 相当于调用了floor

""" 模运算
    计算模数或余数，使用mod,remainder,fmod,也可以使用 % 
    这些函数的差异在于处理负数的方式。fmod异于其他函数
"""
def demo_mod():
    """ 演示模运算函数 """
    # remainder 逐个返回两个数组中元素相除后的余数，如果第二个数字为0，则直接返回0
    # % 仅仅是remainder的简写
    a = np.arange(-4, 4)
    print(np.remainder(a, 2))
    # mod和remainder功能完全一致
    print(np.mod(a, 2))
    # fmod所得余数的正负由被除数决定，与除数无关
    print(np.fmod(a, 2))


""" 斐波那契数列
    斐波那契数列是基于地推关系生成的。用Numpy解释递推关系是比较麻烦的，我们用
    矩阵的形式或者黄金分割公式来解释它。
    使用matrix创建矩阵，rint对浮点数取整，但结果仍为浮点数
    斐波那契数列的计算等价于矩阵的连乘
"""

def create_fibonacci():
    """ 计算斐波那契数列 """
    F = np.matrix([[1, 1], [1, 0]])
    # 计算第 8 个数，即矩阵的冥为（8-1）
    print(F ** 7)
    print((F ** 7)[0, 0])
    # 利用黄金分割公式（比奈公式 binet's formula)，加上取整函数，计算斐波那契数列
    n = np.arange(1, 9)
    sqrt5 = np.sqrt(5)
    phi = ( 1 + sqrt5) / 2
    fibo = np.rint((phi**n - (-1/phi)**n) / sqrt5)
    print(fibo)



def draw_lisa():
    """ 利萨茹曲线
    利萨茹曲线是一种很有趣的使用三角函数的方式
    x = A sin(at + n/2)
    y = B sin(bt)
    利萨茹曲线的参数包含A B a b ,为简单起见，我们令A和B均为1
    """
    a = 9.
    b = 9.
    t = np.linspace(-np.pi, np.pi, 201)
    
    x = np.sin(a * t + np.pi/2)
    y = np.sin(b * t) 

    plt.plot(x,y)
    plt.show()


draw_lisa()