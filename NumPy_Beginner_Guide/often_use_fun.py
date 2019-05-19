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
    # 生成一个自然数序列，做一个粗澡的权重
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



print(max_min_price())


