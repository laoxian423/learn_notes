"""
http://matplotlib.sourceforge.net/gallery.html
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
# from matplotlib.finance import quotes_historical_yahoo
# matplotlib.finance 已经没有了，拆出来成了一个单独的包mpl_finance
import mpl_finance as mpf
import sys
from datetime import date




def draw_ploy():
    """ 绘制多项式函数 """

    # 以自然对数序列作为多项式的系数，使用Poly1d函数创建多项式
    func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
    # 使用linspace创建x轴的数值，在-10和10之间产生30个均匀分布的值
    x = np.linspace(-10, 10, 30)
    # 计算多项式的值
    y = func(x)
    # 绘制图像
    plt.plot(x, y)
    # 添加x 轴,y 轴标签
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.show()

def draw_ploy_derivative():
    """ 绘制多项式函数及其导函数 """
    
    # 创建多项式及其导函数
    func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
    func1 = func.deriv(m=1)
    x = np.linspace(-10, 10, 30)
    y = func(x)
    y1 = func1(x)
    # 红色圆形绘制多项式，绿色虚线绘制导函数
    plt.plot(x, y, 'ro', x, y1, 'g--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def draw_ploy_derivative12():
    """ 绘制多项式函数及其1阶、2阶导函数 """
    
    # 创建多项式及其导函数
    func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
    x = np.linspace(-10, 10, 30)
    y = func(x)
    func1 = func.deriv(m=1)
    y1 = func1(x)
    func2 = func.deriv(m=2)
    y2 = func2(x)

    # 使用subplot创建子图，改函数第一个参数是子图的行数，第二个参数是子图的列数，第三个参数
    # 是从开始的序号。另一种方式是将这3个参数结合成一个数字，如311
    plt.subplot(311)
    plt.plot(x, y, 'r-')
    plt.title("Polynomial")

    plt.subplot(312)
    plt.plot(x, y1, 'b^')
    plt.title("First Derivative")

    plt.subplot(313)
    plt.plot(x, y2, 'go')
    plt.title("Second Derivative")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def draw_k():
    """ 绘制股票全年价格 """
    #today = date.today()
    #start = (today.year -1, today.month, today.day)
    # 创建定位器,在轴上定位月份和日期
    alldays = DayLocator()
    months = MonthLocator()
    # 创建一个日期格式化器格式化X轴上的日期
    month_formatter = DateFormatter("%b %Y")
    d, o, h, l, c = np.loadtxt('NumPy_Beginner_Guide/BHP.csv',
                                delimiter=',',
                                usecols=(0, 1, 2, 3, 4, 5),
                                unpack=True)
    # 创建一个figure顶层容器
    fig = plt.figure()
    # 增加一个子图
    ax = fig.add_subplot(111)
    # x轴的主定位器设置为月定位器
    ax.xaxis.set_major_locator(months)
    # x轴次定位器设置为日定位器
    ax.xaxis.set_minor_locator(alldays)
    # 将x轴上的主格式化器设置为月格式化器，负责x轴上较粗刻度的标签
    ax.xaxis.set_major_formatter(month_formatter)
    # 绘制K线
    mpf.candlestick_ohlc(ax,(d,o,h,l,c),width=1.0,colorup='r',colordown='green', alpha=1)
    # 将x轴上的标签格式化为日期
    fig.autofmt_xdate()
    plt.show()

draw_k()