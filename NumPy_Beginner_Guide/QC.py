""" 质量控制 

NumPy 中的numpy.testing 可以支持NumPy代码的单元测试

TDD（Test Driven Development,测试驱动开发)是软件开发史最终要的里程碑之一。TDD专注于自动单元
测试，它的目标是尽可能最大限度自动化测试代码。如果代码被改动，我们仍可以运行测试并捕捉可能存在
的问题。
"""
""" 断言函数

assert_almost_equal 如果两个数字的近似程度没有达到指定精度，就抛出异常
assert_approx_equal 如果两个数字的近似程度没有达到指定有效数字，就抛出异常
assert_array_almost_equal 如果两个数组中元素的近似程度没有达到指定精度就抛出异常
assert_array_equal 如果两个数组对象不相同，就抛出异常
assert_array_less 两个数组必须形状一致，并且第一个数组的元素严格小于第二个数组的元素，否则抛出异常
assert_equal 如果两个对象不相同，就抛出异常
assert_raises 若用填写的参数调用函数没有抛出指定的异常，则测试不通过
assert_warns 若没有抛出指定的警告，则测试不通过
assert_string_equal 断言两个字符串变量完全相同
assert_allclose 如果两个对象的近似成图超出了指定的容差限，就抛出异常
"""

import numpy as np
import unittest
from numpy.testing.decorators import setastest
from numpy.testing.decorators import skipif
from numpy.testing.decorators import knownfailureif
from numpy.testing import decorate_methods


def demo_assert():
    """ 断言函数示例 """
    # 判断两个浮点数是否在指定精度下近似相等
    # print(np.testing.assert_almost_equal(0.123456789, 0.123456789, decimal=8))
    # print(np.testing.assert_almost_equal(0.123456789, 0.123455677, decimal=8))

    # 断言近似相等
    # print(np.testing.assert_approx_equal(0.123456789, 0.123456780, significant=8))
    # print(np.testing.assert_approx_equal(0.123456789, 0.123456780, significant=9))

    # 数组近似相等
    # print(np.testing.assert_array_almost_equal([0, 0.123456789], [0, 0.123456780], decimal=8))
    # print(np.testing.assert_array_almost_equal([0, 0.123456789], [0, 0.123456780], decimal=9))

    # 严格比较数组
    # print("pass",np.testing.assert_allclose([0, 0.123456789, np.nan], [0, 0.123456780, np.nan], 
    #                                  rtol=1e-7, atol=0))
    # print("Fail",np.testing.assert_array_equal([0, 0.123456789, np.nan], [0, 0.123456780, np.nan]))

    # 一个数组是否严格大于另一个数组
    # print("pass ", np.testing.assert_array_less([0, 0.123456789, np.nan], [1, 0.23456780, np.nan]))
    # print("fail ", np.testing.assert_array_less([0, 0.123456789, np.nan], [0, 0.123456780, np.nan]))

    # 比较两个对象，这里的对象可以是python对象
    # print(np.testing.assert_equal((1,2),(1,3)))

    # 比较字符串
    print(np.testing.assert_string_equal("NumPy","NumPy"))

    # 浮点数的比较,ULP 最小精确单位
    # 使用finfo函数确定机器精度
    eps = np.finfo(float).eps
    print(eps)

    # print(np.testing.assert_array_almost_equal_nulp(1.0, 1.0 + eps))
    # print(np.testing.assert_array_almost_equal_nulp(1.0, 1.0 + 2 * eps))

    # 设置 maxulp 比较浮点数
    print(np.testing.assert_array_max_ulp(1.0, 1.0 + eps))
    print(np.testing.assert_array_max_ulp(1.0, 1.0 + 2 * eps, maxulp=2))


""" 单元测试

单元测试是对代码的一小部分进行自动化测试的单元，通常是一个函数或方法
"""

def factorial(n):
    """ 阶乘函数 """
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("Unexpected negative value")
    
    return np.arange(1, n+1).cumprod()

class FactorialTest(unittest.TestCase):
    """ 用一个简单的阶乘函数编写测试代码，检查所谓的程序主逻辑及非法输入的情况"""
    def test_factorial(self):
        # 计算3的阶乘，测试通过
        fac = factorial(3)
        self.assertEqual(6, fac[-1])
        np.testing.assert_equal(np.array([1, 2, 6]), fac)
        print('3 ok')

    def test_zero(self):
        # 计算0的阶乘，测试通过
        self.assertEqual(1, factorial(0))
        print('zero ok')

    def test_negative(self):
        # 计算负数的阶乘，测试不通过
        # 这里本抛出ValueError异常，但我们断言其抛出indexError异常
        self.assertRaises(IndexError, factorial(-10))

# if __name__ == '__main__':
#     unittest.main()



""" nose 和 测试装饰器

nose是python框架，使得（单元）测试更加容易。nose可以帮助你组织测试代码。任何匹配正则表达式
(?:^|[b_.-][Tt]est)的Python源代码文件、文件夹或库都将被收集用于测试。nose 充分利用了装饰器
numpy.testing模块中有很多装饰器。
numpy.testing.decorators.deprecated         在运行测试时过滤掉过期警告
numpy.testing.decorators.knownfailureif     根据条件抛出knowFailureTest异常
numpy.testing.decorators.setastest          将函数标记为测试函数或非测试函数
numpy.testing.decorators.skipif             根据条件抛出skipTest异常
numpy.testing.decorators.slow               将测试函数标记为“运行缓慢"

此外，还可以调用decorate_metods函数，将装饰器应用到能够匹配正则表达式或字符串的类方法上。
"""

@setastest(False)   # 用于测试
def test_false():
    pass
@setastest(True)    # 不用于测试
def test_true():
    pass

@skipif(True)   # 跳过测试
def test_skip():
    pass

@knownfailureif(True)   # 使函数总是不通过
def test_alwaysfail():
    pass

# 定义一个可以被nose执行的函数和对应的测试类：
class TestClass():
    def test_true2(self):
        pass
    
class TestClass2():
    def test_false2(self):
        pass

# 将test_false2在测试中禁用
decorate_methods(TestClass2, setastest(False), 'test_false2')


# 执行下列命令测试
# nosetests -v QC.py








