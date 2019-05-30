"""
http://matplotlib.sourceforge.net/gallery.html
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from dateutil.parser import parse ## 导入转换到指定格式日期的工具
# from matplotlib.finance import quotes_historical_yahoo
# matplotlib.finance 已经没有了，拆出来成了一个单独的包mpl_finance
import mpl_finance as mpf
import sys
#from datetime import date
import datetime



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

def date2nums(s):
    """ 日期转换成对应的数字
    """
    return datetime.datetime.strptime(str(s,encoding='utf8'), "%d-%m-%Y").toordinal()
    
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
                                usecols=(1, 3, 4, 5, 6),
                                converters={1:date2num},
                                unpack=True)
    d = ["%s" % datetime.date.fromordinal(int(d[i])) for i in range(len(d))]
    data = []
    for i in range(len(d)):
        temp = (d[i], o[i], h[i], l[i], c[i])
        data.append(temp)
    # data = (d,o,h,l,c)
    # print(data)
    # return
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
    mpf.candlestick_ohlc(ax, data, width=1.0, colorup='r', colordown='green', alpha=1)
    # 将x轴上的标签格式化为日期
    fig.autofmt_xdate()
    plt.show()

from matplotlib.pylab import date2num ## 导入日期到数值一一对应的转换工具

def draw_k1():
    """ K线，上面那个调不好 ，找一个充数"""

    d, o, h, l, c = np.loadtxt('NumPy_Beginner_Guide/BHP.csv',
                                delimiter=',',
                                usecols=(1, 3, 4, 5, 6),
                                converters={1:date2nums},
                                unpack=True)
    # 把日期转换为字符串
    d = ["%s" % datetime.date.fromordinal(int(d[i])) for i in range(len(d))]
    data = []
    for i in range(len(d)):
        # 把日期转换为matplotlib使用的格式，这个日期转换很操蛋
        temp = (date2num(parse(d[i])) , o[i], h[i], l[i], c[i])
        data.append(temp)
    # 设置字体
    plt.rcParams['font.family'] = 'SimHei' 
    # 创建图片和坐标轴 
    fig, ax = plt.subplots() 
    # 调整底部距离 
    fig.subplots_adjust(bottom=0.2) 
    # 设置X轴刻度为日期时间 
    ax.xaxis_date() 
    # 设置X轴刻度线并旋转45度 
    plt.xticks(rotation=45) 
    # 设置Y轴刻度线 
    plt.yticks() 
    # 设置图片标题 
    plt.title("股票代码 ** K线图") 
    # 设置X轴标题 
    plt.xlabel("时间") 
    # 设置Y轴标题 
    plt.ylabel("股价（元）") 
    # 设置网格线 
    plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3) 
    # 股票数据，格式是往列表里添加元组, 每个元组代表一个股票信息。其中元组的格式是（日期，开盘价，最高价，最低价，收盘价） 
    # data_list_ = [(date2num(parse(str(20181110))),10,20,5,15),(date2num(parse(str(20181111))),11,22,6,14)]
    # 设置利用mpf画股票K线图 
    mpf.candlestick_ohlc(ax, data, width=1.0, colorup='r', colordown='green', alpha=1)
    # 显示图片 
    plt.show() 
    # 保存图片
    # plt.savefig("K线.png") 
    # 关闭plt，释放内存
    # plt.close() 

