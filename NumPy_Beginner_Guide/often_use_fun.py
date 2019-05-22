""" 常用函数 """
# 创建一个单位矩阵并将其存到文件中
import numpy as np

def create_eye_save_txt(n):
    """ 创建单位矩阵并保存为eye.txt """

    # Numpy中提供 eye 创建单位矩阵，参数为 1 的个数
    i2 = np.eye(n)
    print(i2)
    # 保存文件
    np.savetxt('NumPy_Beginner_Guide/eye.txt', i2)


def read_stock_from_csv():
    """ 从csv文件中读取股票数据 """

    # 只取开盘、收盘
    # unpack=True 意思是分拆存储不同列的数据
    O, C = np.loadtxt('NumPy_Beginner_Guide/appl.csv', delimiter=' ', usecols=(2, 5), unpack=True)
    print(O, C)

def stock_vwap():
    """ Volume-Weighted Average Price

    成交量加权平均价格，它代表着金融资产的”平均“价格，某个价格的成交量
    越高，该价格所占的权重就越大。VWAP是以成交量为权重计算出来的加权平
    均值。常用于算法交易。
    """
    C, V = np.loadtxt('NumPy_Beginner_Guide/appl.csv', delimiter=' ', usecols=(4, 5), unpack=True)
    vwap = np.average(C, weights=V)
    return vwap

def mean():
    """ 计算算数平均值 """
    m = np.loadtxt('NumPy_Beginner_Guide/appl.csv', delimiter=' ', usecols=(5), unpack=True)
    return np.mean(m)

def stock_twap():
    """ 时间加权平均价格 
    
    TWAP(Time-Weighted Average Price) 基本的思想就是最近的价格重要性
    大一些，所以应该对近期的价格给以较高的权重。本书中关于股价分析的大部分
    示例都仅仅是为了说明问题。
    """
    C = np.loadtxt('NumPy_Beginner_Guide/appl.csv', delimiter=' ', usecols=(4), unpack=True)
    # 生成一个自然数序列，做一个粗糙的权重
    t = np.arange(len(C))
    return np.average(C, weights=t)

def max_min_price():
    """ 找出最高和最低价格 """
    C, V = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                       delimiter=' ', 
                       usecols=(1, 3), 
                       unpack=True)
    # ptp() 返回C 中最大值和最小值的极差
    return (np.max(C),np.min(C),np.ptp(C))

""" 统计分析 """
def calc_median():
    """ 计算中位数 、方差 
    
    Numpy中方差的定义和统计学中定义不一致，但更为通用。
    方差指个体数据和个体数据算术平均值的离差平方和，除以个体个数所得到的值
    这个值越大，表面参与计算的个体数据之间差距越大，收盘价方差表示一定的收
    盘价的价格变动幅度。
    """

    C = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                    delimiter=' ', 
                    usecols=(4), 
                    unpack=True)
    # 验证一下中位数是否正确
    # sorted_close = np.msort(C)
    # N = len(C)
    # sorted_close = list(sorted_close)
    # print(sorted_close[int((N-1)/2)])

    return (np.median(C), np.var(C))

# 中位数和方差
# abc = calc_median()
# print("media = {0}, VAR = {1}".format(abc[0], abc[1]))


def rate_of_return():
    """ 股票收益率 
    
    简单收益率：指相邻两个价格之间的变化率。
    对数收益率：指所有价格取对数后两两之间的差值。
    """
    # 计算简单收益率
    # NumPy的diff函数可以返回一个由相邻数组元素的差值构成的数组，类似于微分。
    # 我们还需要用差值除以前一天的价格。
    # diff返回的数组比收盘价少一个元素。
    C = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                    delimiter=' ', 
                    usecols=(4), 
                    unpack=True)

    returns = np.diff(C) / C[:-1]
    # print(returns)
    # 计算标准差
    # print("Standard deviation",np.std(returns))

    # 计算对数收益率
    logreturns = np.diff(np.log(C))

    return (returns,logreturns)


# abc = rate_of_return()
# posertindices = np.where(abc[0] > 0)    
# print('元素中所有正值的索引:',posertindices)
# for i in posertindices:
#     print(abc[0][i])

def calc_Volatility():
    """ 计算波动率

    历史波动率（年波动率或月波动率）：
    年波动率等于对数收益率的标准差除以均值，再除以交易日倒数的平方根，通常取252天。
    """
    logreturns = rate_of_return()[1]
    annual_volatility = np.std(logreturns)/np.mean(logreturns)
    # Python中整数的除法和浮点数的除法运算机制不同，这里必须用浮点除法才能正确。
    annual_volatility = annual_volatility / np.sqrt(1./252.)
    return annual_volatility

# print('收盘价年波动率:',calc_Volatility())

""" 日期分析 
    Numpy会尝试把日期转换成浮点数，需要显示的告诉Numpy怎样来转换日期。
    在loadtxt中有一个参数 converters ,它是一个数据列和转换函数之间进行映射的字典。
    需要自己写出转换函数。
"""
import datetime

def date2num(s):
    """ 日期转换成对应的数字（星期几）

    monday: 0  .....  sunday: 6
    """
    return datetime.datetime.strptime(str(s,encoding='utf8'), "%m-%d-%Y").date().weekday()


def trans_dates_number():
    """ 将日期转换成一个数字序列 
    
    将股票日期转换成数字星期几，然后计算每个星期几的平均值
    """

    dates, close = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                       delimiter=' ', 
                       usecols=(0, 4), 
                       converters={0:date2num},  # 这里读出的是字节码，需要在转换函数中转成字符串
                       unpack=True)
    averages = np.zeros(5)
    for i in range(5):
        # 取出每星期几对应的索引
        indices = np.where(dates == i)
        # 根据这个索引取出对应的收盘价
        prices = np.take(close, indices)
        # 算术平均
        avg = np.mean(prices)
        averages[i] = avg 

    return averages



# avg = trans_dates_number()
# print(avg,type(avg))
# #print('星期一:{0} 星期二：{1} 星期三：{2} 星期四：{3} 星期五：{4}'.format(avg[0],avg[1],avg[2],avg[3],avg[4]))
# # {0[0]}  第一个0 表示format中的第一个变量（list)，[0]表示这个变量的第一个元素
# print('星期一:{0[0]} 星期二：{0[1]} 星期三：{0[2]} 星期四：{0[3]} 星期五：{0[4]}'.format(avg))


""" 汇总数据 """
def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    # take 根据 a 中的索引取出对应的值，保存在h 中。
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]
    return ("APPL", monday_open, week_high, week_low, friday_close)


def sum_week():
    """ 按周汇总数据 """
    dates, open, high, low, close = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                       delimiter=' ', 
                       usecols=(0, 1, 2, 3, 4), 
                       converters={0:date2num},  # 这里读出的是字节码，需要在转换函数中转成字符串
                       unpack=True)
    close = close[:25]
    dates = dates[:25]
    # 找到第一个星期五，因为数据是按时间降序存放的。
    first_friday = np.ravel(np.where(dates == 4))[0]
    # 找到最后一个星期一
    last_monday = np.ravel(np.where(dates == 0))[-1]
    print(np.where(dates == 0))
    # 建立一个数组，存放每周内每一天的索引值
    weeks_indices = np.arange(first_friday, last_monday + 1)
    # 用split切分数组,分为5段，每个段5个元素
    weeks_indices = np.split(weeks_indices, 5)
    # 用apply_along_axis进行统计
    weeksummary = np.apply_along_axis(summarize, 1, weeks_indices,
                                      open, high, low, close)

    print(weeksummary)
    np.savetxt('NumPy_Beginner_Guide/weeksummary.csv',weeksummary, delimiter=',', fmt='%s')


""" 真实波动幅度均值(ATR)
    用来衡量股价波动性的指标
    ATR是基于 N 个交易日的最高价和最低价进行计算的，通常取最近20个交易日
"""

def calc_ATR():
    """ 计算股价波动幅度 """
    dates, open, high, low, close = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                       delimiter=' ', 
                       usecols=(0, 1, 2, 3, 4), 
                       converters={0:date2num},  # 这里读出的是字节码，需要在转换函数中转成字符串
                       unpack=True)
    # 取最近20个交易日数据
    N = 20 
    high = high[-N:]
    low =  low[-N:]
    # 前一交易日的收盘价格
    previousclose = close[-N-1 : -1]
    """
    对于每一个交易日计算以下数据：
    h - l  最高减最低，当日股价范围，当日最高减去当日最低
    h - previousclose  当日最高价和前一个交易日收盘价之差
    previousclose - l   前一日收盘价和当日最低价之差
    波动值就是这三者最大值
    maximun,分别计算这三个值，然后保存最大值。
    """
    truerange = np.maximum(high -low, high - previousclose, previousclose - low)
    print(truerange)
    #创建一个长度为N的数组atr,初始化为0
    #这个数组的首个元素就是truerange数组元素的平均值
    atr = np.zeros(N)
    atr[0] = np.mean(truerange)
    print(atr[0])
    #用如下公式计算其他元素的值，((N-1)PATR+TR)/N
    #PATR表示前一个交易日的ATR值，TR即当日的真实波动幅度
    for i in range(1, N):
        atr[i] = (N - 1) * atr[i-1] + truerange[i]
        atr[i] /= N 

    print(atr) 


""" 简单移动平均线(simple moving average)
    需要第一一个N个周期的移动窗口，即N个交易日，按照时间序列滑动这个窗口，并计算窗口内数据的均值
    简单移动平均线只不过是计算与等权重的指示函数的卷积，也可以是不等权重的。
    简单移动平均线可以用信号处理技术求解：与1/N的权重进行卷积运算，N为窗口大小。
    np.convolve函数
"""
import matplotlib.pyplot as plt

def simple_moving_average():
    """ 简单移动平均线的计算 """
    # 设置移动窗口大小
    N = 5
    # 准备权重值，这里是等权重
    weights = np.ones(N) / N
    # 调用convolve()函数
    close = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                       delimiter=' ', 
                       usecols=(4), 
                       unpack=True)
    sma = np.convolve(weights,close)[N-1:-N+1]
    # [N-1:-N+1] 取出中间部分(两者做卷积运算时完全重叠的区域)
    # 其实就是把小于窗口大小的那几个值去除掉了，本列中就是头4个和尾4个。
    print(sma)
    t = np.arange(N -1, len(close))
    plt.plot(t, close[N-1:], lw=1.0)
    plt.plot(t, sma, lw=2.0)
    plt.show()


""" 指数移动平均线 exponential moving average
    EMA使用的权重是指数衰减的，对历史上的数据点赋予的权重以指数速度减小，但永远不会达到0
"""

def exp_moving_average():
    """ 计算指数移动平均线 """
    # 生成指数权重
    N = 5
    # exp 计算每个元素的指数
    # linspace(起始值，终止值，元素个数) 返回一个元素值在指定的范围内均匀分布的数组。
    weights = np.exp(np.linspace(-1., 0., N))
    print(weights)
    # 对权重值做归一化操作
    weights /= weights.sum()
    print(weights)
    close = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                       delimiter=' ', 
                       usecols=(4), 
                       unpack=True)
    ema = np.convolve(weights, close)[N-1:-N+1]
    t = np.arange(N-1, len(close))
    plt.plot(t, close[N-1:], lw=1.0)
    plt.plot(t, ema, lw=2.0)
    plt.show()


""" 布林带
    用以刻画价格波动的区间。基本形态由三条轨道线组成的带状通道（中轨和上、下轨各一条）
    中轨：简单移动平均线
    上轨：比简单移动平均线高两倍标准差的距离
    下轨：比简单移动平均线低两倍标准差的距离
"""

def calc_boll():
    """ 绘制布林带 """
    # 设置移动窗口大小
    N = 5
    # 准备权重值，这里是等权重
    weights = np.ones(N) / N
    # 调用convolve()函数
    close = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                       delimiter=' ', 
                       usecols=(4), 
                       unpack=True)
    sma = np.convolve(weights,close)[N-1:-N+1]
    deviation = []
    c = len(close)
    for i in range(N-1, c):
        if i + N < c:
            # 构建与移动平均线相关的数据子集
            dev = close[i: i+N]
        else:
            dev = close[-N:]
        
        averages = np.zeros(N)
        averages.fill(sma[i - N -1])
        # 计算标准差
        dev = dev - averages
        dev = dev ** 2
        dev = np.sqrt(np.mean(dev))
        deviation.append(dev)
    # 简单移动平均加减2倍的标准差，计算上轨和下轨
    deviation = 2 * np.array(deviation)
    upperBB = sma + deviation
    lowerBB = sma - deviation

    c_slice = close[N-1:]
    between_bands = np.where((c_slice < upperBB) & (c_slice > lowerBB))

    # 绘图
    t = np.arange(N-1, c)
    plt.plot(t, c_slice, lw=1.0)
    plt.plot(t, sma, lw=2.0)
    plt.plot(t, upperBB, lw=3.0)
    plt.plot(t, lowerBB, lw=4.0)
    plt.show()


""" 线性模型
    用线性模型预测价格:假设一个股价可以用之前股价的线性组合表示出来，也就是说这个股价等于
    之前的股价与各自的系数相乘后再做加和的结果，系数由我们决定。就是一个求解最小二乘法的问题。
"""
def linalg_stock():
    """ 线性模型在股价上的应用 """
    c = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                       delimiter=' ', 
                       usecols=(4), 
                       unpack=True)
    N = 5
    # 1. 首先，获取一个包含N个股价的向量b
    b = c[-N:]
    b = b[::-1]
    # 2. 初始化一个N * N 的二维数组A，元素全部为0
    A = np.zeros((N, N), float)
    print(A)
    # 3. 用 b 向量中的N个股价填充数组 A
    for i in range(N):
        A[i,] = c[-N-1-i : -1-i]
    print(A)
    # 4.确定线性模型中的系数
    # 系数向量x, 残差数组，A的秩，A的奇异值
    (x, residuals, rank, s) = np.linalg.lstsq(A, b)
    print(x, residuals, rank, s)
    # 5. 使用dot计算系数向量与最近N个价格构成的向量的点积(dot product)
    print(np.dot(b, x))


""" 绘制趋势线
    根据所谓的枢轴点绘制的曲线，趋势线描绘的价格变化的趋势，这里只是为了阐述原理
"""
def fit_line(t, y):
    A = np.vstack([t, np.ones_like(t)]).T
    return np.linalg.lstsq(A, y)[0]

def draw_trendline():
    """ 趋势线的绘制 """
    h, l, c = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                       delimiter=' ', 
                       usecols=(2, 3, 4), 
                       unpack=True)
    # 确定枢轴点的位置，假设它们等于最高价、最低价和收盘价的平均值
    pivots = (h + l + c) / 3
    print(pivots)
    # 从这些枢轴点推导出所谓的阻力位和支撑位
    # 定义一个函数用直线 y = at + b 来你和数据，该函数返回系数a 和 b 
    # 将直线方程重写为y = Ax的形式，其中 A =[t l], x= [a b]
    # 假设支撑位在枢轴点下方一个当日股价区间的位置，而阻力位在枢轴点上方一个当日股价区间的位置
    t = np.arange(len(c))
    sa, sb = fit_line(t, pivots - (h - l))
    ra, rb = fit_line(t, pivots + (h - l))
    support = sa * t + sb
    resistance = ra * t + rb
    # 判断一下有多少数据落在支撑位和阻力位之间，如果只有一小部分，就没有意义
    condition = (c > support) & (c < resistance)
    print(condition)
    between_bands = np.where(condition)
    print("between_bands:", between_bands)
    # 复查一下具体取值：
    print(support[between_bands])
    print(c[between_bands])
    print(resistance[between_bands])

    between_bands = len(np.ravel(between_bands))
    print("Number points between bands", between_bands)
    print("Ration between bands", float(between_bands)/len(c))
    # 绘图
    plt.plot(t, c)
    plt.plot(t, support)
    plt.plot(t, resistance)
    plt.show()


""" 数组的修剪和压缩 """

def ndarray_func():
    """ ndarray 修剪和压缩常用方法 """
    # clip() 将所有比给定的最大值、最小值全部设定为给定的最大值最小值。
    a = np.arange(5)
    print(a)
    print(a.clip(1, 2))

    # compress()返回一个根据给定条件筛选后的数组
    a = np.arange(4)
    print(a)
    print(a.compress(a > 2))



""" 计算阶乘 """
def clac_factorial():
    """ 计算阶乘 """
    b = np.arange(1, 9)
    print(b)
    print(b.prod()) 
    # 1 - 8 所有阶乘值
    print(b.cumprod())

clac_factorial()