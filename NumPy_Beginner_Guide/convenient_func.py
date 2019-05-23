""" 便捷函数 """
""" 股票相关性分析
    协方差描述的是两个变量共同变化的趋势，其实就是归一化前的相关系数，使用cov函数
    计算股票收益率的协方差矩阵
"""
import numpy as np
import matplotlib.pyplot as plt

def get_close(csv_filepath, default_fild=6):
    """ 从数据文件中得到股票的收盘价 """
    C = np.loadtxt(csv_filepath, 
                    delimiter=',', 
                    usecols=(default_fild), 
                    unpack=True)
    return C

def get_vol(csv_filepath, default_fild=7):
    """ 从数据文件中得到股票的收盘价 """
    V = np.loadtxt(csv_filepath, 
                    delimiter=',', 
                    usecols=(default_fild), 
                    unpack=True)
    return V

def rate_of_return(csv_filepath):
    """ 根据数据文件计算股票收益率 
    
    简单收益率：指相邻两个价格之间的变化率。
    对数收益率：指所有价格取对数后两两之间的差值。
    """
    # 计算简单收益率
    # NumPy的diff函数可以返回一个由相邻数组元素的差值构成的数组，类似于微分。
    # 我们还需要用差值除以前一天的价格。
    # diff返回的数组比收盘价少一个元素。
    C =get_close(csv_filepath)
    returns = np.diff(C) / C[:-1]
    # print(returns)
    # 计算标准差
    # print("Standard deviation",np.std(returns))

    # 计算对数收益率
    # logreturns = np.diff(np.log(C))

    return returns


def rate_related():
    """ 计算两只股票的收益率相关性 """
    csv_bhp = 'NumPy_Beginner_Guide/BHP.csv' 
    csv_vale = 'NumPy_Beginner_Guide/vale.csv'
    bhp_returns = rate_of_return(csv_bhp)
    vale_returns = rate_of_return(csv_vale)

    # 1.协方差描述两个变量共同变化的趋势,得到协方差矩阵
    covariance = np.cov(bhp_returns, vale_returns)
    print(covariance)
    # 2.使用diagonal函数查看对角线上的元素
    # 协方差矩阵的对角线元素并不相等，这与相关系数矩阵不同
    print(covariance.diagonal())
    # 3.使用trace函数计算矩阵的迹，即对角线上元素之和
    print(covariance.trace())
    # 4.两个向量的相关系数被定义为协方差除以各自标准差的乘积。计算向量a和b的相关系数公式如下：
    # corr(a,b)=cov(a,b)/（a的标注差 * b的标准差）
    print(covariance/(bhp_returns.std() * vale_returns.std()))
    # 用相关系数来度量这两只股票的相关程度，相关系数的取值范围在-1到1之间，与自身相关系数是1
    # 相关系数矩阵是关于对角线对称的。
    print(np.corrcoef(bhp_returns, vale_returns))
    
    # 判断两只股票价格是否同步,如果他们收盘价差值偏离了平均差值2倍于标准差的距离，则不同步
    bhp_close = get_close(csv_bhp)
    vale_close = get_close(csv_vale)

    difference = bhp_close - vale_close
    avg = np.mean(difference)
    dev = np.std(difference)
    print(np.abs(difference[-1] - avg) > 2 * dev)

    # 绘图
    t = np.arange(len(bhp_returns))
    plt.plot(t, bhp_returns, lw=1)
    plt.plot(t, vale_returns, lw=2)
    plt.show()


def polynomial_fit():
    """ 多项式拟合的演示 
    
    用Polyfit对数据进行多项式拟合
    用polyval计算多项式的取值
    用toots求得多项式函数的根
    用polyder求解多项式函数的导函数
    """
    # 用一个三次多项式拟合两只股票收盘价的差价
    csv_bhp = 'NumPy_Beginner_Guide/BHP.csv' 
    csv_vale = 'NumPy_Beginner_Guide/vale.csv'
    N = 3
    bhp = get_close(csv_bhp)
    vale = get_close(csv_vale)
    t = np.arange(len(bhp))
    poly = np.polyfit(t, bhp - vale, N)
    print(poly)
    # poly 输出的是多项式系数。用这个值推断下一个值
    print(np.polyval(poly, t[-1] + 1))
    # 理想情况下，BHP和VALE差价越小越好，在极限情况下，差值可以在某个点为0，使用roots
    # 函数找出我们拟合的多项式函数什么时候到达0值。
    print(np.roots(poly))
    # 使用polyder对多项式函数求导,输出即为导函数的系数
    der = np.polyder(poly)
    print(der)
    # 求出导数函数的根，即找出原多项式函数的极值点
    print(np.roots(der))
    vals = np.polyval(poly, t)
    # 使用argmax argmin 找出最大值点和最小值点
    vals = np.polyval(poly, t)
    print(np.argmax(vals))
    print(np.argmin(vals))
    # 绘制源数据和拟合函数
    plt.plot(t, bhp - vale)
    plt.plot(t, vals)
    plt.show()


def demo_obv():
    """ 净额成交量 OBV 又叫能量潮指标

    可以有当日收盘价、前一天的收盘价以及当日成交量计算得出。可以认为基期的OBV值为0
    若当日收盘价高于前一日收盘价，则本日OBV等于基期OBV加上当日成交量。
    若当日收盘价低于前一日收盘价，则本日OBV等于基期OBV减去当日成交量。
    若收盘价没有变化，则当日成交量以0计算。
    """
    csv_bhp = 'NumPy_Beginner_Guide/BHP.csv' 
    c = get_close(csv_bhp)
    v = get_vol(csv_bhp)

    # 用diff计算收盘价的变化量，diff可以计算数组中两个连续元素的差值
    change = np.diff(c)
    print(change)

    # sign 函数可以返回元素的正负符号，正为1，负为-1，否则0
    signs = np.sign(change)
    print(signs)
    # 使用piecewise也可获得正负符号，可以分段给定取值
    pieces = np.piecewise(change, [change < 0, change > 0], [-1, 1])
    print(pieces)
    print(np.array_equal(signs, pieces))

    # 计算OBV值
    print(v[1:] * signs)

def calc_profit(open, high, low, close):
    """ 以比开盘价稍低的价格买入

    如果价格不在当日股价范围内，买入失败，否则，以收盘价卖出
    所获得的利润即买入和卖出的差价
    """
    buy = open * 0.999
    # daily range
    if low < buy < high:
        return (close-buy)/buy
    else:
        return 0


def simulation_trade():
    """ 交易过程模拟 """
    # 读入数据 
    csv_bhp = 'NumPy_Beginner_Guide/BHP.csv' 
    o, h, l, c = np.loadtxt(csv_bhp, delimiter=',', usecols=(3, 4, 5, 6), unpack=True)
    # vectorize 相当于 map 函数
    func = np.vectorize(calc_profit)
    profits = func(o, h, l, c)
    print(profits)
    real_trades = profits[profits != 0]
    print("Number of trades",len(real_trades), round(100.0 * len(real_trades)/len(c), 2), "%")
    print("Average profit/loss %", round(np.mean(real_trades) * 100, 2))

    # 正盈利的交易日利润
    winning_trades = profits[profits  > 0 ]
    print("Number of winning trades", len(winning_trades), round(100.0 * len(winning_trades)/len(c),2), "%")
    print("Average profit %", round(np.mean(winning_trades) * 100, 2))


def data_smoothing():
    """ 平滑数据
    
    对于噪声数据往往难以处理，通常要对其进行平滑处理。除了计算移动平均线的方法，
    还可以用np.hanning()函数处理，这事一个加权余弦的窗函数。
    """
    # 调用hanning函数计算权重，生成一个长度为N的窗口：
    N = 8
    weights = np.hanning(N)
    print(weights)
    # 使用convolve函数计算BHP和VALE的股票收益率，以归一化处理后的weights作为参数
    csv_bhp = 'NumPy_Beginner_Guide/BHP.csv' 
    csv_vale = 'NumPy_Beginner_Guide/vale.csv'
    bhp = np.loadtxt(csv_bhp, delimiter=',', usecols=(6,), unpack=True)
    bhp_returns = np.diff(bhp) / bhp[:-1]
    smooth_bhp = np.convolve(weights/weights.sum(), bhp_returns)[N-1:-N+1]

    vale = np.loadtxt(csv_vale, delimiter=',', usecols=(6,), unpack=True)
    vale_returns = np.diff(vale) / bhp[:-1]
    smooth_vale = np.convolve(weights/weights.sum(), vale_returns)[N-1:-N+1]

    # 绘图
    t = np.arange(N -1 , len(bhp_returns))
    plt.plot(t, bhp_returns[N-1:], lw=1.0)
    plt.plot(t, smooth_bhp, lw=2.0)
    plt.plot(t, vale_returns[N-1:], lw=1.0)
    plt.plot(t, smooth_vale, lw=2.0)
    plt.show()




data_smoothing()
