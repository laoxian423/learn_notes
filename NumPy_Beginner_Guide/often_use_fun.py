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

def sum_week():
    """ 按周汇总数据 """
    dates, close = np.loadtxt('NumPy_Beginner_Guide/appl.csv', 
                       delimiter=' ', 
                       usecols=(0, 4), 
                       converters={0:date2num},  # 这里读出的是字节码，需要在转换函数中转成字符串
                       unpack=True)
    #close = close[:16]
    #dates = dates[:16]

    # 找到第一个星期一
    first_monday = np.ravel(np.where(dates == 0))[0]
    # 找到最后一个星期五
    last_friday = np.ravel(np.where(dates == 4))[-2]
    # 建立一个数组，存放每周内每一天的索引值
    weeks_indices = np.arange(first_monday, last_friday + 1)
    # 按照每个子数组5个元素，用split切分数组
    weeks_indices = np.split(weeks_indices, len(weeks_indices)/5)

    print(last_friday, weeks_indices)


sum_week()